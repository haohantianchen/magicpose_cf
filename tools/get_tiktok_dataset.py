import os
import shutil

# 源文件夹路径
src_root = "/raid/T2V-datasets/TikTok/TikTok_dataset/TikTok_dataset"

# 训练集目标文件夹路径
dst_root_train_set = "/raid/lurenjie/MagicDance/TikTok-v4/TikTok-v4-densepose/train_set"
dst_root_pose_map_train = "/raid/lurenjie/MagicDance/TikTok-v4/TikTok-v4-densepose/pose_map_train_set"

# 验证集目标文件夹路径
dst_root_val_set = "/raid/lurenjie/MagicDance/TikTok-v4/TikTok-v4-densepose/val_set"
dst_root_pose_map_val = "/raid/lurenjie/MagicDance/TikTok-v4/TikTok-v4-densepose/pose_map_val_set"


os.makedirs(dst_root_train_set, exist_ok=True)
os.makedirs(dst_root_pose_map_train, exist_ok=True)
os.makedirs(dst_root_val_set, exist_ok=True)
os.makedirs(dst_root_pose_map_val, exist_ok=True)

# 遍历每个子文件夹（如00001, 00002等）
for subdir in os.listdir(src_root):
    src_subdir_path = os.path.join(src_root, subdir)
    
    if os.path.isdir(src_subdir_path):  # 确保是文件夹
        # 根据文件夹编号选择目标文件夹
        if int(subdir) >= 335:
            dst_images_path = os.path.join(dst_root_val_set, subdir)
            dst_densepose_path = os.path.join(dst_root_pose_map_val, subdir)
        else:
            dst_images_path = os.path.join(dst_root_train_set, subdir)
            dst_densepose_path = os.path.join(dst_root_pose_map_train, subdir)
        
        # 处理images文件夹
        src_images_path = os.path.join(src_subdir_path, 'images')
        
        if not os.path.exists(dst_images_path):
            os.makedirs(dst_images_path)  # 创建目标文件夹
        
        for file in os.listdir(src_images_path):
            if file.endswith('.png'):
                src_file_path = os.path.join(src_images_path, file)
                dst_file_path = os.path.join(dst_images_path, file)
                shutil.copy(src_file_path, dst_file_path)  # 复制文件
                
        # 处理densepose文件夹
        src_densepose_path = os.path.join(src_subdir_path, 'densepose')
        
        if not os.path.exists(dst_densepose_path):
            os.makedirs(dst_densepose_path)  # 创建目标文件夹
        
        for file in os.listdir(src_densepose_path):
            if file.endswith('.png'):
                src_file_path = os.path.join(src_densepose_path, file)
                dst_file_path = os.path.join(dst_densepose_path, file)
                shutil.copy(src_file_path, dst_file_path)  # 复制文件
