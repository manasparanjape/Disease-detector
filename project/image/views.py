import os
import numpy as np
import pickle as pk
from PIL import Image as im
from .form import ImageForm
from .models import Image
from django.shortcuts import render

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ImageForm(data=request.POST, files=request.FILES)

        Image.objects.all().delete()
        for f in os.listdir('media/img/22'):
            os.remove(os.path.join('media/img/22', f))

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
                prediction_model = pk.load(
                    open('prediction_models/bt_bins_2.bin', 'rb'))
                prediction = np.argmax(prediction_model.predict(image_array))
                if prediction == 0:
                    prediction = 'The image does not indicate any tumor'
                else:
                    prediction = 'Unfortuately, the scan suggests' \
                                 ' the existence of a tumor. ' \
                                 'Please report these findings to a doctor ' \
                                 'and get a second opinion.'

            elif obj.disease == 'l':
                image_file = image_file.resize((100, 100))
                image_file = image_file.convert('L')
                image_array = np.asarray(image_file)
                image_array = np.reshape(image_array, (100, 100))
                image_array = np.expand_dims(image_array, axis=0)
                prediction_model = pk.load(
                    open('prediction_models/l.bin', 'rb'))
                prediction = np.argmax(prediction_model.predict(image_array))
                if prediction == 0:
                    prediction = 'The image does not indicate '\
                        'the cell is an immature leukemic blast'
                else:
                    prediction = 'Unfortuately, the image indicates the ' \
                                 'cell is an immature leukemic blast. '

            elif obj.disease == 'p':
                image_file = image_file.resize((150, 150))
                image_file = image_file.convert('L')
                image_array = np.asarray(image_file)
                image_array = np.reshape(image_array, (150, 150))
                image_array = np.expand_dims(image_array, axis=0)
                prediction_model = pk.load(
                    open('prediction_models/p_bins_2.bin', 'rb'))
                prediction = np.argmax(prediction_model.predict(image_array))
                if prediction == 0:
                    prediction = 'The image does not indicate any Pneumonia'
                else:
                    prediction = 'Unfortuately, the scan indicates the ' \
                                 'patient has Pneumonia' \
                                 'Please consult a doctor'

            elif obj.disease == 'k':
                image_file = image_file.resize((200, 200))
                image_file = image_file.convert('L')
                image_array = np.asarray(image_file)
                image_array = np.expand_dims(image_array, axis=0)
                image_array = image_array / 255.0
                prediction_model = pk.load(
                    open('prediction_models/k.bin', 'rb'))
                prediction = np.argmax(prediction_model.predict(image_array))
                if prediction == 1:
                    prediction = 'The image does not indicate any kidney ' \
                                 'disease'
                elif prediction == 0:
                    prediction = 'Unfortunately, the scan indicates the ' \
                                 'presence of a cyst in the patient\'s kidney.'
                elif prediction == 2:
                    prediction = 'Unfortunately, the scan indicates the ' \
                                 'presence of a stone in the patient\'s ' \
                                 'kidney.'
                elif prediction == 3:
                    prediction = 'Unfortunately, the scan indicates the ' \
                                 'presence of a tumor in the patient\'s ' \
                                 'kidney.'

            return render(request, 'prediction.html', {
                'obj': obj,
                'prediction': prediction,
            })
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request, 'index.html', {
        'img': img,
        'form': form,
    })


def result(request):
    if request.method == 'GET':
        return render(request, 'index.html')
