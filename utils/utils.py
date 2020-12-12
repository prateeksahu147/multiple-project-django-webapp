import pickle

with open('./toxic_comment_classifier/pickelfile/tfif.pkl', 'rb') as t:
    tfidf= pickle.load(t)
        
with open('./toxic_comment_classifier/pickelfile/toxic_classifier.pkl', 'rb') as t:
    toxic_clf= pickle.load(t)
        
with open('./toxic_comment_classifier/pickelfile/threat_classifier.pkl', 'rb') as t:
    threat_clf= pickle.load(t)
        
with open('./toxic_comment_classifier/pickelfile/severe_toxic_classifier.pkl', 'rb') as t:
    severe_clf= pickle.load(t)
        
with open('./toxic_comment_classifier/pickelfile/obscene_classifier.pkl', 'rb') as t:
    obscene_clf= pickle.load(t)
        
with open('./toxic_comment_classifier/pickelfile/insult_classifier.pkl' ,'rb') as t:
    insult_clf= pickle.load(t)
        

with open('./toxic_comment_classifier/pickelfile/identity_classifier.pkl', 'rb') as t:
    identity_clf= pickle.load(t)


"""
def load_all_pickel():

    with open('./toxic_comment_classifier/pickelfile/tfif.pkl', 'rb') as t:
        tfidf= pickle.load(t)
        
    with open('./toxic_comment_classifier/pickelfile/toxic_classifier.pkl', 'rb') as t:
        toxic_clf= pickle.load(t)
        
    with open('./toxic_comment_classifier/pickelfile/threat_classifier.pkl', 'rb') as t:
        threat_clf= pickle.load(t)
        
    with open('./toxic_comment_classifier/pickelfile/severe_toxic_classifier.pkl', 'rb') as t:
        severe_clf= pickle.load(t)
        
    with open('./toxic_comment_classifier/pickelfile/obscene_classifier.pkl', 'rb') as t:
        obscene_clf= pickle.load(t)
        
    with open('./toxic_comment_classifier/pickelfile/insult_classifier.pkl' ,'rb') as t:
        insult_clf= pickle.load(t)
        

    with open('./toxic_comment_classifier/pickelfile/identity_classifier.pkl', 'rb') as t:
        identity_clf= pickle.load(t)
        

    print('all pickel are loaded')"""


#load_all_pickel()


def predict_toxicity(text):
  vect_text=tfidf.transform(list(text))
  toxic_pred=round(toxic_clf.predict_proba(vect_text)[0][1],2)
  severe_pred= round(severe_clf.predict_proba(vect_text)[0][1], 2)
  obscene_pred=round(obscene_clf.predict_proba(vect_text)[0][1], 2)
  threat_pred=round(threat_clf.predict_proba(vect_text)[0][1], 2)
  insult_pred=round(insult_clf.predict_proba(vect_text)[0][1] , 2)
  identity_hate_pred=round(identity_clf.predict_proba(vect_text)[0][1], 2)
  return {'Toxic' : toxic_pred, 'Severe': severe_pred, 
          'Obsene': obscene_pred, 'Threat' :threat_pred, 'Insult': insult_pred,  
          'Identity Hate': identity_hate_pred}
