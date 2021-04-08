from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

images = ["0.jpg", "1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg"]
names = ["1.Amitabh Bachchan", "2.Aamir Khan", "3.Ajay Devgn", "4.Shah Rukh Khan", "5.Irrfan Khan", "6.Hrithik Roshan", "7.Naseeruddin Shah", "8.Akshay Kumar", "9.Salman Khan", "10.Manoj Bajpayee"]

age_group = []
age_group_1 = []
age_group_2 = []
age_group_3 = []

gender_group = []

race_group = []

emotion_group = []

for img in images:

    imgs = cv2.imread(img)
    plt.imshow(imgs[:, :, ::-1])
    plt.show()

    age_result = DeepFace.analyze(imgs, actions=["age"])
    gender_result = DeepFace.analyze(imgs, actions=['gender'])
    race_result = DeepFace.analyze(imgs, actions=['race'])
    emotion_result = DeepFace.analyze(imgs, actions=['emotion'])

    #print(type(age_result))
    print("")
    print("predicted age is : ", age_result["age"]);
    print("Predicted gender is :", gender_result['gender']);
    print("Predicted race is :", race_result['race']);
    print("Predicted emotion is :", emotion_result['emotion']);


    if age_result["age"] > 0 and age_result["age"] < 30:
        age_group_1.append(age_result["age"])

    if age_result["age"] > 30 and age_result["age"] < 60:
        age_group_2.append(age_result["age"])

    if age_result["age"] > 60 and age_result["age"] < 100:
        age_group_3.append(age_result["age"])

    if age_result["age"]:
        age_group.append(age_result["age"])

    if "Man" in gender_result["gender"]:
        gender_group.append(gender_result["gender"])

    if race_result["dominant_race"]:
        race_group.append(race_result["dominant_race"])

    if emotion_result["dominant_emotion"]:
        emotion_group.append(emotion_result["dominant_emotion"])

print("")

print("Names of top 10 bollywood actors as scraped from IMDB: ")
for name in names:
    print(name)

print("")
print("ages of the actors is as follows: ")
print(age_group)

print("")
print("following is the predicted age categorization of the top 10 bollywood actors: ")
print("0 to 30 years of age : " + str(age_group_1))
print("31 to 60 years of age : " + str(age_group_2))
print("61 to 100 years of age : " + str(age_group_3))

print("")
print("following is the predicted gender categorization of the top 10 bollywood actors: ")
print(str(gender_group))

print("")
print("following is the predicted race categorization of the top 10 bollywood actors: ")
print(race_group)

print("")
print("following is the predicted emotion categorization of the top 10 bollywood actors: ")
print(emotion_group)

print("")
print("Submitted by:\n Sameer Nema: 18100BTCSES02798")