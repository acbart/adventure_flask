"""
The simple_route decorator allows us to quickly make routes that have proper
state being passed in and manipulated.

This file also establishes the reset route, with the idea that everyone
would like to be able to reset their game.
"""

import json
from flask import request, session, redirect
from functools import wraps
from app import app

INITIAL_WORLD = {}


def simple_route(path: str, **options):
    """
    Creates a new route for the URL endpoint `path`. This decorator wraps
    the View endpoint to pass in the current `world` (deserialized from session data
    upon function entrance and serialized back into session once the function is
    done), any URL parameters, and then any request parameters (sorted by key name).

    :param path: The URL endpoint to use
    :type path: str
    :param options: Options to pass along to Flask's app.route. Usually you can ignore this.
    :return: Decorated function
    """
    def decorator(f):
        @app.route(path, **options)
        @wraps(f)
        def decorated_function(*args, **kwargs):
            world = json.loads(session.get('world', json.dumps(INITIAL_WORLD)))
            values = [v for k, v in sorted(request.values.items())]
            result = f(world, *args, *values, **kwargs)
            session['world'] = json.dumps(world)
            return result
        return decorated_function
    return decorator


@app.route("/reset/")
def reset():
    """
    Resets the game's world state (stored in session) and redirects to
    the root page.
    :return: Redirection to '/'
    """
    session['world'] = "{}"
    return redirect('/')

