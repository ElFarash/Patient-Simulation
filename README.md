# Patient-Simulation
a question answering model takes a medical case read it and understand it then acts like a real patient. you can ask it about its symptoms and try to diagnose it. 

## Quick start
This repository is build upon Python v3.8. See [requirements.txt](https://github.com/ElFarash/Patient-Simulation/blob/main/requirements.txt) for other dependencies. you can install dependencies with the following commands.

```
pip3 install -r requirements.txt
```

Make sure to download the pretrained model provided by the deepspeech and save it in Speaker-Diarization/models/. You can download the pre-trained English model files for deepspeech with the following commands:
```
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm 
```
```
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
```
