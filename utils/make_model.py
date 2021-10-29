
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
from sklearn.decomposition import NMF
from sklearn.preprocessing import normalize

def make_col_cos_model(col ,p, pidx):
    col = col.fillna('')
    col[pidx] = p

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(col)
    col_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    return col_sim


def make_ibcf_model(score_matrix, df):
    song_sim = linear_kernel(score_matrix, score_matrix)
    recommend_matrix = pd.DataFrame(data=song_sim, index=score_matrix.index, columns=score_matrix.index)
    
    return recommend_matrix


def make_nmf_model(core):
    nmf = NMF(n_components=6)

    nmf_feature = nmf.fit_transform(core)
    return nmf_feature

def normalize(feature):
    norm_feature = normalize(feature)
    
    return norm_feature