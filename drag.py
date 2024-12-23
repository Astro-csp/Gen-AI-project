import pandas as pd
import os

# 设置效率因子 e 和展弦比 AR
efficiency_factor = 0.8  # 一般取值 0.7~0.85
aspect_ratio = 7.5       # 展弦比 (需要根据机翼实际情况调整)

# 输入和输出文件夹
input_folder = "/Users/chany/Gen-AI project on git/Datasets from GitHub (1)"  # 输入文件夹路径，存放多个 CSV 文件
output_folder = '/Users/chany/Gen-AI project on git/naca_airloil_with_drag_components'  # 输出文件夹路径
os.makedirs(output_folder, exist_ok=True)  # 确保输出文件夹存在

# 遍历输入文件夹中的所有文件
for file_name in os.listdir(input_folder):
    if file_name.endswith(".csv"):  # 只处理 CSV 文件
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, f"processed_{file_name}")
        
        # 读取数据
        df = pd.read_csv(input_path)
        
        # 计算升力诱导阻力系数和寄生阻力系数
        df['C_Di'] = (df['Cl'] ** 2) / (3.1416 * efficiency_factor * aspect_ratio)
        df['C_Dp'] = df['Cd'] - df['C_Di']
        
        # 保存结果到新文件
        df.to_csv(output_path, index=False)
        print(f"已处理文件：{file_name}，结果保存至：{output_path}")

print("所有文件处理完成！")
