import os

def add_prefix_to_files(directory, prefix="A_"):
    # 遍历目录中的所有文件和文件夹
    for filename in os.listdir(directory):
        # 构建原始文件的完整路径
        old_file = os.path.join(directory, filename)
        # 检查这是否是一个文件
        if os.path.isfile(old_file):
            # 构建新文件名（添加前缀）
            new_filename = prefix + filename
            # 构建新文件的完整路径
            new_file = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(old_file, new_file)
            print(f"Renamed '{old_file}' to '{new_file}'")

# add_prefix_to_files("/Users/dj/STUDY/merge_man/static/body_com/表情_胡子", "胡子_")
# add_prefix_to_files("/Users/dj/STUDY/merge_man/static/body_com/表情_猪八戒", "猪八戒_")
# add_prefix_to_files("/Users/dj/STUDY/merge_man/static/body_com/普通表情", "普通表情_")



def fill_body_com_list() -> list:
    # 收集：身体部件的目录名  和 它下面的png文件。   ["头",[这里会包含这个目录下所有的png文件名]] 
    # [['头', ['27_head.png', '19_head.png', 'head.png', '31_head.png', '30_head.png']]]
    body_com_list = [["头",[]],] # ["表情",[]],  ["身体",[]],  ["手",[]],  ["腿脚",[]]  ]  
    cur_dir = os.getcwd()   # 获取当前目录
    for item in body_com_list:
        file_dir = os.path.join(cur_dir, "static/body_com", item[0])
        # print(file_dir)
        for filename in os.listdir(file_dir):
            if filename.lower().endswith(".png"):
                item[1].append(filename)
        # print( len(item[1]), "\n", item[1])
    return body_com_list

def get_body_com_url_pre() -> str:  # "http://127.0.0.1:8000/static/body_com/头/19_head.png"
    return "static/body_com"

# print(fill_body_com_list())
print(get_body_com_url_pre())