from django.shortcuts import render
from django.http import HttpResponse
import pickle
from utils import utils #import file for load  pickel files 

#utils.load_all_pickel() # this function will load all the pickel file that is built in another python file.

# Create your views here.
def classifier(request):
    #return HttpResponse("classifier")
    return render(request, 'toxic_comment_classifier/classifier.html')

def predict(request):
    data = request.GET['comment']
    result = utils.predict_toxicity(data)
    return render(request , 'toxic_comment_classifier/predict.html', {'comment_text':data, 'results':result})