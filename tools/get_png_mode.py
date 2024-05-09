from PIL import Image

# 打开PNG图片
image = Image.open('/raid/lurenjie/MagicDance/TikTok-v4/TikTok-v4-densepose/train_set/00001/0001.png')

# 打印图像的颜色模式
print(image.mode)

# 根据颜色模式确定通道数
if image.mode == 'RGB':
    print("这是一张RGB图像，有3个通道。")
elif image.mode == 'RGBA':
    print("这是一张RGBA图像，有4个通道。")
elif image.mode == 'L':
    print("这是一张灰度图像，有1个通道。")
else:
    print(f"图像模式为 {image.mode}.")