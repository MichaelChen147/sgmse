# import os
# import librosa
# import soundfile as sf

# # 输入文件夹路径和输出文件夹路径
# # input_folder = 'input_folder'  # 将此处的'input_folder'替换为你的输入文件夹路径
# # output_folder = 'output_folder'  # 将此处的'output_folder'替换为你的输出文件夹路径

# input_folder = '/misc/Work32/wenyichen/dataset/VoiceBank-DEMAND-48kHz/train/noisy'  # 将此处的'input_folder'替换为你的输入文件夹路径
# output_folder = '/misc/Work32/wenyichen/dataset/VoiceBank-DEMAND-16kHz/train/noisy'  # 将此处的'output_folder'替换为你的输出文件夹路径


# # 目标采样率
# target_sample_rate = 16000

# # 确保输出文件夹存在
# os.makedirs(output_folder, exist_ok=True)

# # 遍历输入文件夹中的所有文件
# for filename in os.listdir(input_folder):
#     if filename.endswith('.wav'):
#         input_file = os.path.join(input_folder, filename)
#         output_file = os.path.join(output_folder, filename)

#         # 读取输入音频文件
#         y, sr = librosa.load(input_file, sr=None)

#         # 将音频数据重新采样为目标采样率
#         y_resampled = librosa.resample(y, sr, target_sample_rate)

#         # 保存重新采样后的音频文件
#         sf.write(output_file, y_resampled, target_sample_rate)

########################################################################
# 使用tqdm记录进度

# import os
# import librosa
# import soundfile as sf
# from tqdm import tqdm

# # 输入文件夹路径和输出文件夹路径
# # input_folder = 'input_folder'  # 将此处的'input_folder'替换为你的输入文件夹路径
# # output_folder = 'output_folder'  # 将此处的'output_folder'替换为你的输出文件夹路径

# input_folder = '/misc/Work32/wenyichen/dataset/VoiceBank-DEMAND-48kHz/train/clean'  # 将此处的'input_folder'替换为你的输入文件夹路径
# output_folder = '/misc/Work32/wenyichen/dataset/VoiceBank-DEMAND-16kHz/train/clean'  # 将此处的'output_folder'替换为你的输出文件夹路径

# # 目标采样率
# target_sample_rate = 16000

# # 确保输出文件夹存在
# os.makedirs(output_folder, exist_ok=True)

# # 获取输入文件夹中的所有WAV文件列表
# input_files = [f for f in os.listdir(input_folder) if f.endswith('.wav')]

# # 使用tqdm创建进度条
# with tqdm(total=len(input_files), desc="Resampling") as pbar:
#     for filename in input_files:
#         input_file = os.path.join(input_folder, filename)
#         output_file = os.path.join(output_folder, filename)

#         # 读取输入音频文件
#         y, sr = librosa.load(input_file, sr=None)

#         # 将音频数据重新采样为目标采样率
#         y_resampled = librosa.resample(y, sr, target_sample_rate)

#         # 保存重新采样后的音频文件
#         sf.write(output_file, y_resampled, target_sample_rate)

#         # 更新进度条
#         pbar.update(1)



#####################################################################
# 使用多进程加快运行速度

import os
import librosa
import soundfile as sf
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor

# 输入文件夹路径和输出文件夹路径
# input_folder = 'input_folder'  # 将此处的'input_folder'替换为你的输入文件夹路径
# output_folder = 'output_folder'  # 将此处的'output_folder'替换为你的输出文件夹路径

input_folder = '/misc/Work32/wenyichen/dataset/VoiceBank-DEMAND-48kHz/train/clean'  # 将此处的'input_folder'替换为你的输入文件夹路径
output_folder = '/misc/Work32/wenyichen/dataset/VoiceBank-DEMAND-16kHz/train/clean'  # 将此处的'output_folder'替换为你的输出文件夹路径

# 目标采样率
target_sample_rate = 16000

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 获取输入文件夹中的所有WAV文件列表
input_files = [f for f in os.listdir(input_folder) if f.endswith('.wav')]

# 定义处理单个文件的函数
def process_file(filename):
    input_file = os.path.join(input_folder, filename)
    output_file = os.path.join(output_folder, filename)

    # 读取输入音频文件
    y, sr = librosa.load(input_file, sr=None)

    # 将音频数据重新采样为目标采样率
    y_resampled = librosa.resample(y, sr, target_sample_rate)

    # 保存重新采样后的音频文件
    sf.write(output_file, y_resampled, target_sample_rate)

# 使用tqdm创建进度条
with tqdm(total=len(input_files), desc="Resampling") as pbar:
    # 使用多进程并行处理文件
    with ProcessPoolExecutor(max_workers=10) as executor:  # 这里可以调整max_workers来控制并发度
        futures = [executor.submit(process_file, filename) for filename in input_files]
        for future in futures:
            future.result()  # 等待任务完成
            pbar.update(1)
