extends Control

@onready var worlds: Array = [$LevelIcon, $LevelIcon2, $LevelIcon3, $LevelIcon4, $LevelIcon5, $LevelIcon6, $LevelIcon7, $LevelIcon8, $LevelIcon9, $LevelIcon10, $LevelIcon11, $LevelIcon12]
var current_world: int = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	$MiniPlayerIcon.global_position = worlds[current_world].gobal_position

func _input(event):
	if event.is_action_pressed("ui_left") and current_world > 0:
		current_world -= 1
		$MiniPlayerIcon.global_position = worlds[current_world].gobal_position
	if event.is_action_pressed("ui_right") and current_world < 11:
		current_world += 1
		$MiniPlayerIcon.global_position = worlds[current_world].gobal_position
