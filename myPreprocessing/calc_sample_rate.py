import librosa

# 指定音频文件的路径
audio_file = "/misc/Work32/wenyichen/dataset/VoiceBank-DEMAND-16kHz/test/clean/p257_434.wav"

# 加载音频文件
y, sr = librosa.load(audio_file, sr=None)

# 打印采样率
print("采样率 (Sample Rate):", sr)
