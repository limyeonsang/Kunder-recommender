import pandas as pd
from pandas.io.formats.format import return_docstring

def get_phrase_query(db):
    cur = db.cursor()
    query = """SELECT id, title, description 
                FROM song 
                ORDER BY id ASC
                """
    cur.execute(query)
    result = cur.fetchall()

    result = pd.DataFrame(result, columns=['song_id', 'title','desc'])
    return result


def get_user_item_table(db):
    cur = db.cursor()

    # get user_like_song table
    like_query = """SELECT * 
                FROM user_like_song    
                """
    cur.execute(like_query)
    like = cur.fetchall()
    like = pd.DataFrame(like, columns=['user_id','song_id'])

    # get user_comment_song table
    comment_query = """SELECT user_id, song_id
                FROM user_comment_song    
                """
    cur.execute(comment_query)
    comment = cur.fetchall()
    comment = pd.DataFrame(comment, columns=['user_id','song_id'])

    return like, comment


def get_genre_table(db):
    cur = db.cursor()
    query = """SELECT A.id, A.title, B.genre_type_id, C.mood_type_id
            FROM song A
            JOIN song_genre B ON A.id = B.song_id
            JOIN mood C ON A.id = C.song_id;
            """
    cur.execute(query)
    result = cur.fetchall()
    
    result = pd.DataFrame(result, columns=['song_id','song_title','genre','mood'])
    return result