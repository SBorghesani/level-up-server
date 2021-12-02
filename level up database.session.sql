SELECT game.id game_id, 
    game.title, 
    game.maker, 
    game.number_of_players,
    game.skill_level,
    game.game_type_id,
    game.gamer_id,
    user.first_name,
    user.last_name,
    user.first_name || " " || user.last_name full_name  FROM levelupapi_game game
JOIN levelupapi_gamer gamer
ON gamer.id = game.gamer_id
JOIN auth_user user ON gamer.user_id = user.id;