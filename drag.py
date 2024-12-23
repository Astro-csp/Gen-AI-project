import pandas as pd

# 设置效率因子 e 和展弦比 AR
efficiency_factor = 0.8  # 一般取值 0.7~0.85
aspect_ratio = 7.5       # 展弦比 (需要根据机翼实际情况调整)

# 导入数据集
# 假设数据集是一个 CSV 文件，包含如下列：Mach, AoA, Reynolds, CL, CD
data_file = "/Users/chany/Downloads/Datasets from GitHub (1)/NACA4Digit_Dataset05Point.csv"  # 替换为实际数据文件路径
df = pd.read_csv(data_file)

# 计算升力诱导阻力系数和寄生阻力系数
df['C_Di'] = (df['Cl'] ** 2) / (3.1416 * efficiency_factor * aspect_ratio)  # 计算升力诱导阻力
df['C_Dp'] = df['Cd'] - df['C_Di']  # 计算寄生阻力

# 导出结果
output_file = "naca_airfoil_with_drag_components.csv"
df.to_csv(output_file, index=False)

print(f"已成功计算寄生阻力和升力诱导阻力，结果已导出到：{output_file}")

import shutil

# 源文件路径
source_file = "/Users/chany/Gen-AI project on git/naca_airfoil_with_drag_components.csv"

# 目标文件路径
destination_file = "/Users/chany/Downloads/naca_airfoil_with_drag_components.csv"

# 复制文件到目标路径
shutil.copy(source_file, destination_file)

print(f"文件已成功下载到：{destination_file}")