"""
Sprite Collect Coins

sprite类使用的简单示例

"""

import random
import arcade

# --- 常数 ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = .25
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Collect Coins"

class MyGame(arcade.window):
  """我们自定义的Window类"""

  def __init__(self):
    """初始化"""
    # 调用父类的初始化器
    super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # 包含精灵列表的变量
    self.player_list = None
    self.coin_list = None

    # 设置玩家（角色）信息
    self.player_sprite = None
    self.score = 0

    # 不显示鼠标的光标
    self.set_mouse_visible(False)
    arcade.set_background_color(arcade.color.AMAZON)

def setup(self):
  """设置游戏并初始化变量"""

  # 精灵列表
  self.player_list = arcade.SpriteList()
  self.coin_list = arcade.SpriteList()

  # 得分
  self.score = 0

  # 设置玩家（角色）
  # Character image from keney.nl
  self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)