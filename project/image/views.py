import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from django.shortcuts import render, redirect
import numpy as np
from .form import ImageForm
from .models import Image
import pickle as pk
from PIL import Image as im
import matplotlib.pyplot as plt

# Create your views here.
def index(request):
    if request.method == 'POST':
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            image_file = im.open(obj.image)
            if obj.disease == 'bt':
                image_file = image_file.resize((150, 150))
                image_file = image_file.convert('L')
                image_array = np.asarray(image_file)
                image_array = np.reshape(image_array, (150, 150))
                image_array = np.expand_dims(image_array, axis=0)
                prediction_model = pk.load(open('prediction_models/bt_bins_2.bin', 'rb'))
                prediction = np.argmax(prediction_model.predict(image_array))
                if prediction == 0:
                    prediction = 'The image does not indicate any tumor'
                else:
                    prediction = 'Unfortuately, the scan suggests the existence of a tumor'
                
            elif obj.disease == 'l':
                image_file = image_file.resize((100, 100))
                image_file = image_file.convert('L')
                image_array = np.asarray(image_file)
                image_array = np.reshape(image_array, (100, 100))
                image_array = np.expand_dims(image_array, axis=0)
                prediction_model = pk.load(open('prediction_models/l.bin', 'rb'))
                prediction = np.argmax(prediction_model.predict(image_array))
                if prediction == 0:
                    prediction = 'The image does not indicate Acute Lymphoblastic Lukemia'
                else:
                    prediction = 'Unfortuately, the image indicates the patient has Acute Lymphobastic Lukemia'

            elif obj.disease == 'p':
                image_file = image_file.resize((150, 150))
                image_file = image_file.convert('L')
                image_array = np.asarray(image_file)
                image_array = np.reshape(image_array, (150, 150))
                image_array = np.expand_dims(image_array, axis=0)
                prediction_model = pk.load(open('prediction_models/p_bins_2.bin', 'rb'))
                prediction = np.argmax(prediction_model.predict(image_array))
                if prediction == 0:
                    prediction = 'The image does not indicate any Pneumonia'
                else:
                    prediction = 'Unfortuately, the scan indicates the patient has Pneumonia'        

            return render(request, 'index.html', {
                'obj': obj, 
                'prediction': prediction,
                })
    else:
        form=ImageForm()
    img=Image.objects.all()
    return render(request, 'index.html', {
        'img': img, 
        'form': form,
        })