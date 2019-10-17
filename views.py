from flask import render_template, session, request

from route_helper import simple_route


@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """
    return render_template('index.html', world=world)


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


@simple_route("/save/")
def save_name(world: dict, *args) -> str:
    """
    Update the name of the monster.

    :param world: The current world
    :param monsters_name:
    :return:
    """
    #for key, value in request.values.items():
    #    world['corgis'][0][key] = value
    world['met_corgi?'] = True
    world['corgis'][0]['Name'] = request.values.get('monster_name')
    world['corgis'][0]['Mood'] = request.values.get('monster_mood')
    try:
        world['corgis'][0]['Age'] = int(request.values.get('age'))
    except ValueError:
        world['corgis'][0]['Age'] = None
    world['corgis'][0]['Fluffy'] = 'true' == request.values.get('is_fluffy', False)

    return render_template('name_monster.html', world=world)
