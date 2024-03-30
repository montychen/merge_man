import os
from PIL import Image


def img_info(dir):  # 列出目录下，图片的分辨率
    # '/Users/dj/STUDY/merge_man/static/body_com/身体'

    # 遍历目录中的文件
    for filename in os.listdir(dir):
        if filename.endswith(".png"):  # 检查文件扩展名是否为.png
            filepath = os.path.join(dir, filename)  # 获取文件的完整路径
            with Image.open(filepath) as img:
                width, height = img.size  # 获取图片的尺寸
                print(f"{filename}: {width}x{height}")  # 打印文件名和分辨率




def change_filename(top_level_dir):
# 遍历顶级目录
    for root, dirs, files in os.walk(top_level_dir):
        print(f"root:{root}\ndirs:{dirs}\nfiles:{files}\n")
        for dir_name in dirs:
            # 构建第二级目录的完整路径
            second_level_dir = os.path.join(root, dir_name)
            # 遍历第二级目录中的所有文件
            for filename in os.listdir(second_level_dir):
                # 构建原始文件的完整路径
                old_file = os.path.join(second_level_dir, filename)
                # 构建新的文件名，以第二级目录名称作为前缀
                new_filename = f"{dir_name}_{filename}"
                # 构建新文件的完整路径
                new_file = os.path.join(second_level_dir, new_filename)
                # 重命名文件
                os.rename(old_file, new_file)
                # print(f"Renamed '{old_file}' to '{new_file}'")

# change_filename("/Users/dj/STUDY/mojo_study/body")
                

def merge_man():
    image_files = {
        'hair': '头发.png',
        'head': 'head.png',
        'expression': '普通表情_15.png',
        'body': 'body.png',
        'left_hand': 'hand2.png',
        'right_hand': 'hand1.png',
        'left_leg': 'foot2.png',
        'right_leg': 'foot1.png'
    }

    base_dir = "/Users/dj/STUDY/merge_man/static/test_merge_img"
    # 加载所有图片
    images = {name: Image.open(f"{base_dir}/{path}") for name, path in image_files.items()}

    # 假设所有图片大小相同，并获取宽高
    width, height = images['body'].size

    # 创建一个新的图像，背景透明
    result_image = Image.new('RGBA', (width, 2 * height))

    # 将“身体”放在中间
    result_image.paste(images['body'], (0, height // 2))

    # 将“头”放在“身体”上方，将“表情”覆盖在“头”上
    head_y = height // 2 - images['head'].height
    result_image.paste(images['head'], (0, head_y), images['head'])
    result_image.paste(images['expression'], (0, head_y), images['expression'])

    # 将“左手”和“右手”放在“身体”的两侧
    # 注意：可能需要根据实际图片调整手的精确位置
    result_image.paste(images['left_hand'], (-width // 4, height // 2), images['left_hand'])
    result_image.paste(images['right_hand'], (width // 4 * 3, height // 2), images['right_hand'])

    # 将“左腿”和“右腿”放在“身体”下方
    # 注意：可能需要根据实际图片调整腿的精确位置
    result_image.paste(images['left_leg'], (0, height // 2 * 3), images['left_leg'])
    result_image.paste(images['right_leg'], (width // 2, height // 2 * 3), images['right_leg'])

    # 保存结果图像
    result_image.save('完整的人体.png')
              
merge_man()