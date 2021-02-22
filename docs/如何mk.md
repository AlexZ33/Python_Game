# API讲解： Window Class

程序通常从Window类派生，或使用装饰器。这使程序员可以编写代码来处理绘图，更新和处理来自用户的输入。下面是用于启动基于Windows类的程序的模板。

```python
mport arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
```
Window类具有几种方法，我们写的程序可以覆盖这些方法来为程序提供功能。以下是一些最常用的方法：

- on_draw: 绘制屏幕的所有代码都在这里
- update: 用于移动物品并执行游戏逻辑的所有代码都在此处。每秒大约称为60次。
- on_key_press:按下按键时处理事件，例如提角色的速度
- on_key_release: 释放键时进行处理，在这里您可能会停止角色的移动
- on_mouse_motion: 鼠标移动时候被调用。
- on_mouse_press: 当鼠标按钮被按住时候调用。
- set_viewport: 这个函数用来滚动游戏。 调用它可以让编程人员设置屏幕里面画面哪些是可见的。

# API讲解：Sprites（精灵）类
Sprite是在Arcade中创建2D位图对象的简单方法。 Arcade的方法可以轻松绘制，移动和设置精灵动画。您还可以轻松地使用精灵检测对象之间的碰撞。
## 创建一个精灵实例

从图形创建Arcade Sprite类的实例很容易。程序员只需要图像的文件名即可基于sprite生成图像，还可以选择一个数字来按比例放大或缩小图像。例如：

```
SPRITE_SCALING_COIN = 0.2

coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)
```

这段代码将使用存储在coin_01.png中的图像创建一个精灵。图像将缩小到原始高度和宽度的20％。