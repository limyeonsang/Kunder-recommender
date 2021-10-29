
import pandas as pd


def phrase_rec(title_sim, desc_sim, pidx):
    sim_score = title_sim[pidx] + desc_sim[pidx]
    sorted_arg = sim_score.argsort()[::-1]
    music_idx = sorted_arg[1:10]
    
    return music_idx


def item_based_rec(song_id, recommendation_matrix):
    rec_len = len(recommendation_matrix[recommendation_matrix[song_id]>0][song_id])
    return list(recommendation_matrix[song_id].sort_values(ascending=False)[:rec_len].index)


def nmfF_rec(target, norm_feature, song_ids):
    df = pd.DataFrame(norm_feature)
    x = df.join(song_ids)
    pivot_df = pd.pivot_table(x, x[[0,1]], ['song_id'])

    value = pivot_df.loc[target]
    similarities = pivot_df.dot(value)

    return list(similarities.nlargest(len(similarities)).index)