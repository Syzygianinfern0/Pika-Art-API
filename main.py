import argparse
import os
import shutil

from joblib import Parallel, delayed
from tqdm import tqdm

from model import Pika


def parse_args():
    parser = argparse.ArgumentParser(description="Generate videos from text using Pika.art")
    parser.add_argument(
        "--prompts",
        type=str,
        default="all_prompts.txt",
        help="File path of prompts",
    )
    parser.add_argument("--output_dir", type=str, default="./outputs", help="Directory to save generated videos")

    return parser.parse_args()


def main():
    args = parse_args()

    with open(args.prompts, "r") as file:
        prompts = file.readlines()

    model = Pika()

    os.makedirs(args.output_dir, exist_ok=True)

    # for prompt in tqdm(prompts):
    def process(prompt):
        prompt = prompt.strip()
        output_path = os.path.join(args.output_dir, f"{prompt}.mp4")

        # Skip if the video already exists
        if os.path.exists(output_path):
            tqdm.write(f"Skipping prompt '{prompt}' as video already exists: {output_path}")
            return

        # Generate the video with the specified model
        if args.model == "gen3-alpha":
            model.generate(prompt, output_path)
        elif args.model == "pika":
            model.generate(prompt, output_path)
        else:
            video_path = model.generate(prompt)
            shutil.copy(video_path, output_path)

        tqdm.write(f"Generated video for prompt '{prompt}': {output_path}")

    Parallel(n_jobs=4)(delayed(process)(prompt) for prompt in tqdm(prompts))


if __name__ == "__main__":
    main()
