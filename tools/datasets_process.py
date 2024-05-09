import os
import torchvision.transforms as T
from PIL import Image
from torchvision.transforms.functional import to_pil_image

# 参数设置
args = {
    'image_size': 64  # 假设image_size为64，您可以根据需要调整
}

# 定义转换操作
train_image_transform = T.Compose([
    T.RandomResizedCrop(args['image_size']*8, scale=(1.0, 1.0), ratio=(1., 1.), interpolation=T.InterpolationMode.BILINEAR),
    T.ToTensor(), 
])

test_image_transform = T.Compose([
    T.RandomResizedCrop(args['image_size']*8, scale=(1.0, 1.0), ratio=(1., 1.), interpolation=T.InterpolationMode.BILINEAR),
    T.ToTensor(), 
])

train_pose_transform = T.Compose([
    T.RandomResizedCrop(args['image_size']*8, scale=(1.0, 1.0), ratio=(1., 1.), interpolation=T.InterpolationMode.BILINEAR),
    T.ToTensor()
])

test_pose_transform = T.Compose([
    T.RandomResizedCrop(args['image_size']*8, scale=(1.0, 1.0), ratio=(1., 1.), interpolation=T.InterpolationMode.BILINEAR),
    T.ToTensor()
])

# 路径设置
data_dir = "/raid/lurenjie/MagicDance/TikTok-v4/TikTok-v4-densepose"
output_dir = "/raid/lurenjie/MagicDance/TikTok-v4/TikTok-v4-densepose_512"

# 创建输出目录
os.makedirs(output_dir, exist_ok=True)

# 数据集的处理和保存
def process_and_save_images(root_dir, transform):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.png'):
                file_path = os.path.join(subdir, file)
                img = Image.open(file_path)
                img = transform(img)
                # 转换回PIL图像以保存
                img = to_pil_image(img)
                # 确保目标目录存在
                save_dir = os.path.join(output_dir, os.path.relpath(subdir, data_dir))
                os.makedirs(save_dir, exist_ok=True)
                img.save(os.path.join(save_dir, file))

# 应用转换和保存图像
# process_and_save_images(os.path.join(data_dir, "train_set"), train_image_transform)
process_and_save_images(os.path.join(data_dir, "val_set"), test_image_transform)
# process_and_save_images(os.path.join(data_dir, "pose_map_train_set"), train_pose_transform)
process_and_save_images(os.path.join(data_dir, "pose_map_val_set"), test_pose_transform)
