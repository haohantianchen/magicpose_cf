import os
import torchvision.transforms as T
from PIL import Image
from torchvision.transforms.functional import to_pil_image

# 参数设置
args = {
    'image_size': 512  # 设置目标尺寸为512x512
}

# 定义一个函数用于添加中心填充，使图像变为正方形
def make_square(img):
    w, h = img.size
    max_side = max(w, h)
    padding_l = (max_side - w) // 2
    padding_t = (max_side - h) // 2
    padding_r = max_side - w - padding_l
    padding_b = max_side - h - padding_t
    return T.Pad((padding_l, padding_t, padding_r, padding_b), fill=0)(img)

# 定义转换操作
transform = T.Compose([
    T.Lambda(make_square),  # 先将图像填充为正方形
    T.Resize((args['image_size'], args['image_size'])),  # 然后将图像大小调整为512x512
    T.ToTensor()
])

# 路径设置
data_dir = "/raid/lurenjie/MagicDance/TikTok-v4/TikTok-v4-densepose"
output_dir = "/raid/lurenjie/MagicDance/TikTok-v4/TikTok-v4-densepose_512_padd_resize"

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
process_and_save_images(os.path.join(data_dir, "train_set"), transform)
# process_and_save_images(os.path.join(data_dir, "val_set"), test_image_transform)
process_and_save_images(os.path.join(data_dir, "pose_map_train_set"), transform)
# process_and_save_images(os.path.join(data_dir, "pose_map_val_set"), test_pose_transform)
