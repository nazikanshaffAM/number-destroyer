#import battle and text_file_write modules from Game module
import Game.Battle
import Game.text_file_write
 
#assign the function to text and call the function
text=Game.Battle.Battle_fun_don()
Game.text_file_write.statistics(text)
