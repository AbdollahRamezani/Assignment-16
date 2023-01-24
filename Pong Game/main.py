import arcade
from rocket import Rocket
from ball import Ball
class Game(arcade.Window):
    def __init__(self):
       super().__init__(width=800, height=500, title="Pong Game")
       self.player_1 = Rocket(40, self.height//2, arcade.color.RED, "Ma Long")
       self.player_2= Rocket(self.width-40, self.height//2, arcade.color.CYAN, "Ai")
       self.ball= Ball(self)     
             
       arcade.set_background_color(arcade.color.DARK_GREEN)

    def on_draw(self):
       arcade.start_render()
       arcade.draw_rectangle_outline(self.width//2, self.height//2, width=self.width-30, height=self.height-30, 
                                     color=arcade.color.WHITE, border_width=7)
       arcade.draw_line(self.width//2, 30, self.width//2, self.height-30, arcade.color.WHITE, line_width=7)
       self.player_1.draw()
       self.player_2.draw()
       self.ball.draw()

       arcade.draw_text(f'{self.player_1.name} : {self.player_1.score}', 300,465,arcade.color.RED,10, font_name= "Arial")
       arcade.draw_text(f'AI : {self.player_2.score}', 420,465,arcade.color.CYAN,10, font_name= "Arial")
       

       arcade.finish_render()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
      #  self.player_1.center_x = x چون در این بازی راکت باید فقط در جهت بالا و پایین حرکت کند این قسمت کامت میکنیم
       if self.player_1.height < y < self.height-self.player_1.height :  #نباید راکت از کادر بزنه بیرون 
           self.player_1.center_y = y

    def on_update(self, delta_time: float):
       self.ball.move() 
       self.player_2.move(self, self.ball) 
       if self.ball.center_y < 30 or self.ball.center_y > self.height -30 :
          self.ball.change_y *= -1

       if arcade.check_for_collision(self.player_1, self.ball):  # برای بررسی برخورد دو شی با هم باید برای هردو شی طول وعرض تعریف کنیم
          self.ball.change_x *= -1   

       if arcade.check_for_collision(self.player_2, self.ball):  
          self.ball.change_x *= -1      

       if self.ball.center_x < 0 :
          self.player_2.score += 1
          del self.ball
          self.ball= Ball(self)
       if self.ball.center_x > self.width :
          self.player_1.score += 1    
          del self.ball  
          self.ball= Ball(self)
       
               
          

game = Game()
arcade.run()      