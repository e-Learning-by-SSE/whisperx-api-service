import subprocess
import shlex

from src.api.config import HF_TOKEN


def run_whisperx(temp_mp3_path, lang, model, min_speakers, max_speakers):
    output_dir = "./data/"
    if min_speakers > 0 and max_speakers > 0:
        cmd = (f"whisperx {shlex.quote(temp_mp3_path)} --model {model} --language {lang} --hf_token {HF_TOKEN} --output_format all "
               f"--output_dir {output_dir}  --align_model WAV2VEC2_ASR_LARGE_LV60K_960H --diarize --min_sp"
               f"eakers {min_speakers} --max_speakers {max_speakers}")
    else:
        cmd = (f"whisperx {shlex.quote(temp_mp3_path)} --model {model} --language {lang} --output_format all "
               f"--output_dir {output_dir}  --align_model WAV2VEC2_ASR_LARGE_LV60K_960H")
    subprocess.run(shlex.split(cmd), check=True)
