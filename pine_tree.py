#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/11
# @Author : AlexZ33
# @Site : 
# @File : pine_tree.py
# @Software: PyCharm

# 本示例说明如何使用函数(function)绘制场景。 它并不假定程序员知道如何使用类。
import arcade

# 常数-不变的变量
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "使用函数绘制"


def draw_background():
    """
    此函数绘制背景。特别是天空和地面。
    """
    # 在三分之二的顶部绘制天空
    arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT,
                                      SCREEN_HEIGHT * (1 / 3),
                                      arcade.color.SKY_BLUE)

    # 在底部三分之一绘制地面
    arcade.draw_lrtb_rectangle_filled(0,
                                      SCREEN_WIDTH,
                                      SCREEN_HEIGHT / 3,
                                      0,
                                      arcade.color.DARK_SPRING_GREEN)


def draw_bird(x, y):
    """
    用几条弧线画一只鸟。
    """
    arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x + 40, y, 20, 20, arcade.color.BLACK, 90, 180)


def draw_pine_tree(x, y):
    """
    此函数在指定位置绘制一棵松树。
    """
    # 在顶部绘制三角形
    arcade.draw_triangle_filled(x + 40, y,
                                x, y - 100,
                                x + 80, y - 100,
                                arcade.color.DARK_GREEN)

    # 画行李箱
    arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcade.color.DARK_BROWN)


def main():
    """
    这是主程序。
    """

    # 打开窗户
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # 开始渲染过程。必须在执行任何绘图命令之前完成此操作。
    arcade.start_render()

    # 调用我们的绘图函数。
    draw_background()
    draw_pine_tree(50, 250)
    draw_pine_tree(350, 320)
    draw_bird(70, 500)
    draw_bird(470, 550)

    # 完成渲染。
    # 没有这个，什么都不会画。
    # 必须在所有绘制命令之后使用
    arcade.finish_render()

    # 保持窗在，直到有人将其关闭。
    arcade.run()


if __name__ == "__main__":
    main()