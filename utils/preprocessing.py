import pandas as pd

def for_ibcf(like, comment):
    like['islike'] = 1
    comment['iscomment'] = 1

    df = pd.merge(like, comment, how='outer', on=['user_id', 'song_id'])
    df.fillna(0, inplace=True)

    df['score'] = df['islike']+df['iscomment']
    df.drop(['islike','iscomment'], axis=1, inplace=True)

    score_matrix = df.pivot_table(values='score' , index='song_id', columns='user_id')
    score_matrix.fillna(0, inplace=True)

    return score_matrix