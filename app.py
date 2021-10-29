from flask import Flask, request
from utils import get_db, make_model, recommendation, preprocessing, db

app = Flask(__name__)

# see you sooon~tj
@app.route('/phrase', methods=['POST'])
def rec_by_phrase():
    phrase = request.form.get('phrase', False)

    df = get_db.get_phrase_query(db)

    title_sim = make_model.make_cos_model(df.title, phrase, len(df.desc))
    desc_sim = make_model.make_cos_model(df.desc, phrase, len(df.desc))
    music_idx = recommendation.phrase_rec(title_sim, desc_sim, len(df.desc))
    what_to_rec = df['song_id'].iloc[music_idx].values.tolist()

    return {'phrase':what_to_rec}


@app.route('/ibcf', methods=['GET'])
def rec_by_itembased():
    song_id = int(request.args.get('song_id'))

    like, comment = get_db.get_user_item_table(db)
    score_matrix = preprocessing.for_ibcf(like, comment)
    recommendation_matrix = make_model.make_ibcf_model(score_matrix, score_matrix)
    what_to_rec = recommendation.item_based_rec(song_id, recommendation_matrix)

    return {'ibcf':what_to_rec}


@app.route('/lit', methods=['GET'])
def rec_by_genre():
    song_id = int(request.args.get('song_id'))

    df = get_db.get_genre_table(db)
    
    core = df[['genre','mood']]

    nmf_feature = make_model.make_nmf_model(core)
    norm_feature = make_model.normalize(nmf_feature)
    what_to_rec = recommendation.nmfF_rec(song_id, norm_feature, df.song_id)

    return {'lit_rec':what_to_rec}

if __name__ == '__main__':
    app.run(debug=True, port=5000)

    

