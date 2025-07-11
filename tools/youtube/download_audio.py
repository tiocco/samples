#!/usr/bin/env python3

import argparse
import os
import subprocess

def download_audio(url, output_path="./audio_bank"):
    """Downloads the audio from a YouTube video and saves it to a specified path."""
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    command = [
        "yt-dlp",
        "-x",  # Extract audio
        "--audio-format", "mp3",  # Audio format
        "--audio-quality", "0",  # Best audio quality
        "-o", os.path.join(output_path, "%(title)s.%(ext)s"),  # Output filename
        url,
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Successfully downloaded audio from {url} to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading audio: {e}")
    except FileNotFoundError:
        print("Error: yt-dlp not found. Please install it (e.g., pip install yt-dlp).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download audio from YouTube video.")
    parser.add_argument("url", help="URL of the YouTube video.")
    parser.add_argument("--output", default="./audio_bank",
                        help="Path to store the downloaded audio. Defaults to ./audio_bank.")
    
    args = parser.parse_args()
    download_audio(args.url, args.output)
