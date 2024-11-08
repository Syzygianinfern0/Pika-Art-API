import json
import time

import requests

from headers import job_headers, request_headers


class Pika:
    def __init__(self):
        pass

    def send_request(self, prompt):
        data = (
            "------WebKitFormBoundarylhk4yuvhmhQhMsem\r\n"
            'Content-Disposition: form-data; name="pikaffect"\r\n\r\n\r\n'
            "------WebKitFormBoundarylhk4yuvhmhQhMsem\r\n"
            f'Content-Disposition: form-data; name="promptText"\r\n\r\n{prompt}\r\n'
            "------WebKitFormBoundarylhk4yuvhmhQhMsem\r\n"
            'Content-Disposition: form-data; name="model"\r\n\r\n1.5\r\n'
            "------WebKitFormBoundarylhk4yuvhmhQhMsem\r\n"
            'Content-Disposition: form-data; name="options"\r\n\r\n'
            '{"aspectRatio":1.7777777777777777,"frameRate":24,"camera":{},"parameters":{"guidanceScale":12,"motion":1,"negativePrompt":""},"extend":false}\r\n'
            "------WebKitFormBoundarylhk4yuvhmhQhMsem\r\n"
            'Content-Disposition: form-data; name="userId"\r\n\r\n9074a1b4-82c2-4ec6-9a64-3ae088f5727d\r\n'
            "------WebKitFormBoundarylhk4yuvhmhQhMsem--\r\n"
        )

        response = requests.post("https://api.pika.art/generate/v1.5", headers=request_headers, data=data)
        response_json = response.json()

        if response_json["data"]["generation"]["videos"][0]["status"] == "queued":
            job_id = response_json["data"]["id"]
            return job_id
        else:
            return None

    def get_job(self, job_id):
        data = f'[{{"ids":["{job_id}"]}}]'

        response = requests.post("https://pika.art/my-library", headers=job_headers, data=data)
        response_json = json.loads(response.content.decode("utf-8").splitlines()[1][2:])

        try:
            video_url = response_json["data"]["results"][0]["videos"][0]["resultUrl"]
        except KeyError:
            video_url = None

        return video_url

    def generate(self, prompt, output_path):
        # Send initial request to start video generation
        job_id = self.send_request(prompt)
        if not job_id:
            raise ValueError("Failed to start Pika video generation job.")

        # Poll for video URL
        video_url = None
        start_time = time.time()
        while not video_url:
            if time.time() - start_time > 600:  # 10 minutes timeout
                tqdm.write(f"Timeout reached for prompt '{prompt}'. Skipping...")
                return None
            time.sleep(5)
            video_url = self.get_job(job_id)

        # Download and save the video
        response = requests.get(video_url, stream=True)
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return output_path
