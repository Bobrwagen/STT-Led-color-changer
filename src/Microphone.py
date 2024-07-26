import subprocess

class Mic:
    def __init__(self, card_number=3, device_number=0):
        self.card_number = card_number
        self.device_number = device_number

    def record(self, duration=5):
        # Step 1: Record in WAV format
        wav_file = "record.wav"
        args = [
            "arecord",
            "-D", f"plughw:{self.card_number},{self.device_number}",
            "-f", "S16_LE",
            "-d", str(duration),
            "-r", "16000",  # Set sample rate to 16000 Hz
            wav_file
        ]
        print(f"Running command: {' '.join(args)}")
        subprocess.run(args, check=True)
        
        # Step 2: Convert WAV to FLAC using ffmpeg
        flac_file = "record.flac"
        ffmpeg_args = ["ffmpeg", "-i", wav_file, flac_file]
        print(f"Running command: {' '.join(ffmpeg_args)}")
        subprocess.run(ffmpeg_args, check=True)
        
