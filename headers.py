import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

generate_authorization = config["generate_authorization"]
library_cookie = config["library_cookie"]

request_headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "authorization": generate_authorization,
    "content-type": "multipart/form-data; boundary=----WebKitFormBoundarylhk4yuvhmhQhMsem",
    "dnt": "1",
    "origin": "https://pika.art",
    "priority": "u=1, i",
    "referer": "https://pika.art/",
    "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}

job_headers = {
    "accept": "text/x-component",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "text/plain;charset=UTF-8",
    "cookie": library_cookie,
    "dnt": "1",
    "next-action": "a4f7d00566d7755f69cb53e2b2bbaf32236f107e",
    "next-router-state-tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(dashboard)%22%2C%7B%22children%22%3A%5B%22my-library%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fmy-library%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
    "origin": "https://pika.art",
    "priority": "u=1, i",
    "referer": "https://pika.art/my-library",
    "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}
