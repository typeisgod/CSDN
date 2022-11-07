# CSDN
上班后看csdn少了，发送文件不及时，现在统一保存在git上。

目前文件夹对应：
- 学生成绩排名预测 [学生成绩排名预测(DC)](https://blog.csdn.net/qq_36614557/article/details/87994436)
#### 部分文件名乱码，尚未更改
- psf [改进维纳滤波的实现——光学稀疏孔径成像系统图像恢复算法研究 陈灏](https://blog.csdn.net/qq_36614557/article/details/108392989)
#### 数据load后需要归一化：
```matlab
psf = load('psf_101.TXT');
psf = psf ./ sum(psf(:));
```