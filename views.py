from flask import render_template, session

from route_helper import simple_route

GAME_HEADER = """
<h1>Welcome to adventure quest!</h1>
<p>At any time you can <a href='/reset/'>reset</a> your game.</p>
"""


@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """
    return render_template('index.html', world=world)


ENCOUNTER_MONSTER = """

"""


@simple_route('/goto/<where>/')
def move_to_place(world: dict, where: str) -> str:
    """
    Update the player location and encounter a monster, prompting the player
    to give them a name.

    :param world: The current world
    :param where: The new location to move to
    :return: The HTML to show the player
    """
    world['location'] = where

    if not world['corgis']:
        world['corgis'].append({"Name": "???", "Mood": "Unknown"})

    return render_template('encounter_monster.html', world=world)


@simple_route("/save/name/")
def save_name(world: dict, monster_name: str, monster_mood: str) -> str:
    """
    Update the name of the monster.

    :param world: The current world
    :param monsters_name:
    :return:
    """
    world['corgis'][0]['Name'] = monster_name
    world['corgis'][0]['Mood'] = monster_mood

    return render_template('name_monster.html', world=world)