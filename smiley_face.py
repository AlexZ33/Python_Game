#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/11
# @Author : AlexZ33
# @Site : 
# @File : smiley_face.py
# @Reference: https://opensource.com/article/18/4/easy-2d-game-creation-python-and-arcade
# @Software: PyCharm

import arcade

# 设置屏幕尺寸的常量
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# 打开窗户。设置窗口标题和尺寸（宽度和高度）
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "画个笑脸")

# 将背景色设置为白色。
# 有关命名颜色的列表，请参见：
# http://arcade.academy/arcade.color.html
# 颜色也可以指定为（红色，绿色，蓝色）格式，
# （红色，绿色，蓝色，alpha）格式。
arcade.set_background_color(arcade.color.WHITE)

# 开始渲染过程。必须在执行任何绘图命令之前完成此操作。
arcade.start_render()

# 画脸
x = 300
y = 300
radius = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

# 画右眼
x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# 画左眼
x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

# 画微笑
x = 300
y = 280
width = 120
height = 100
start_angle = 190
end_angle = 350
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

# 完成绘图并显示结果
arcade.finish_render()

# 使窗口保持打开状态，直到用户点击“关闭”按钮为止
arcade.run()