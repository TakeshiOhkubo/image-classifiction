from ImageClassifier import CreateDataAndModel


# https://pypi.org/project/image-classifier/
main = CreateDataAndModel(file_path="./folder/data/", model_file_name_to_save="./folder/model.hdf5", init_lr=0.0001, epochs=100, batch_size=32)

# Here "./data/" is the data folder where we have the label folder- "apple" and "banana" (Remember to include a "/" after the folder like "./data/" ). Basically, you have to give the data folder path where you have the label folders, it can also be like "./seg_pred/seg_pred/".   

main.create() # This will create the data and the model for you.

#--------------------
from ImageClassifier import Run

# 毎回、model.hdf5を消去しないと正しい判定にならない？

r = Run(model_file_name="./folder/model.hdf5") # The model file in your current directory

#img_to_predict = "./folder/grapes_0.jpg"
img_to_predict = "./folder/Malignant_melanoma_01.jpg"


pred = r.run(img_to_predict)
print('Probable=', pred)

#---------------------
import os

r = Run("./folder/model.hdf5")

file_path = "./folder/data"

for file in os.listdir(file_path):
    print(file)