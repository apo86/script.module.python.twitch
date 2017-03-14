# -*- encoding: utf-8 -*-
# https://github.com/justintv/Twitch-API/blob/master/v3_resources/users.md

from twitch import keys
from twitch.queries import V5Query as Qry
from twitch.queries import query


@query
def by_id(identification):
    q = Qry('users/{id}')
    q.add_urlkw(keys.ID, identification)
    return q


# Needs Authentification
@query
def user():
    q = Qry('user')
    return q


# Needs Authentification
@query
def streams():
    raise NotImplementedError


# Needs Authentification
@query
def videos():
    raise NotImplementedError
