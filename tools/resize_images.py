from PIL import Image
import os

# 定义要resize的图片的宽度和高度
width, height = 256, 256

# 指定包含图片的文件夹路径
folder_path = '/raid/lurenjie/p2p/dataset/project/dance_conrtol/dance_control_246_fps10/controlnet_openpose'
out_floder = '/raid/lurenjie/DisCo/mydatasets/dance_openpose_256'
os.mkdir(out_floder)

# 遍历文件夹中的所有文件
for file_name in os.listdir(folder_path):
    # 构造完整的文件路径
    file_path = os.path.join(folder_path, file_name)
    # 检查当前文件是否为文件（排除文件夹）
    if os.path.isfile(file_path):
        try:
            # 尝试打开图片文件
            with Image.open(file_path) as img:
                # Resize图片
                img_resized = img.resize((width, height))
                # 构造resize后图片的保存路径
                resized_file_path = os.path.join(out_floder, file_name)
                # 保存resize后的图片
                img_resized.save(resized_file_path)
                print(f'Resized and saved: {resized_file_path}')
        except Exception as e:
            print(f'Error processing file {file_path}: {e}')
