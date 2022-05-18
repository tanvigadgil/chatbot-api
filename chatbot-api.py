from flask import Flask
from flask import request
import api
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression



def  getPrdiction(testId, age, score):
    df=pd.read_csv('dataset.csv')
    X_train, X_test, y_train, y_test=train_test_split(df[['Score']].values,df.Remark,test_size=0.2)

    model=LogisticRegression()
    model.fit(X_train,y_train)

    sample = [[score]]
    getString = model.predict(sample)
    result = getString[0]
    return result

app = Flask(__name__)
@app.route('/')

def  linear_regression():
    df=pd.read_csv('dataset.csv')
    X_train, X_test, y_train, y_test=train_test_split(df[['Score']].values,df.Remark,test_size=0.2)
    model=LogisticRegression()
    model.fit(X_train,y_train)

    sample = [[29]]
    result = model.predict(sample)
    firstarr = result[0]
    return firstarr

@app.route('/dignosis-data')
def getData():
    testId = request.args.get('testId')
    age = request.args.get('age')
    score = int(request.args.get('score'))

    finalScore = getPrdiction(testId=testId, age=age, score=score)

    return finalScore


# Provide texts with full forms and start with capital letters. Don't use 'I'm', 'don't' etc words.

@app.route('/chatbot')
def getChatbotResponse():
    text = request.args.get('text')
    response = ""
    
    if text in ['hi', 'hey', 'hello', 'Hi', 'Hey', 'Hello']:
        response = "Hello there! How are you feeling today?"
    
    elif text in ['bye', 'goodbye', 'see you again', 'Bye', 'Goodbye', 'See you again']:
        response = "Goodbye!"

# Positive feeling
    elif text in ['I am feeling happy', 'I am happy again', 'I am feeling grateful', 'I feel that I am on the right track']:
        response = "That's great! Keep up the good work. Please add a note of gratitude before you go. Just giving information that by writing gratitude you get the following benefits: \n1. Reducing the stress level: \nSomeone who is grateful have a tendency to keep oneself better, practice healthy living habits, and have good stress management skills. \n2. Getting a new perspective: \nBy writing the Gratitude Journal, we can start observing and seeing patterns about what we think is important in life. This can help us appreciate every little thing we experience and face. \nIn addition, the way we see a situation depends on the perspective we use. When we choose to look for things to be grateful, our perspective in seeing something will change and we are able to realize things that have never been thought of before. \n3. Give rise to self-awareness: \nKnowing any important thing in life can help you to be more mindfull in deciding something. You can be someone who is wiser in making decisions because you understand what you really like. \nThis can help you sort things when you have to make a choice. You can be a person who is not easily washed away on the current by following what many people are followed by most people. \n4. As a reminder in a difficult time: \nWithout the Gratitude Journal, you will have trouble remembering what good things you have experienced. Especially when in difficult times, anyone can easily dissolve in sadness and forget other things that can be grateful."

# Negative feeling
    elif text in ['I am feeling sad', 'I am very sad', 'I feel sad', 'I am feeling scared', 'I am angry', 'I feel humiliated', 'I feel very annoyed', 'I feel annoyed', 'I feel very overwhelming', 'I am overwhelmed']:
        response = "I am concerned that you are experiencing a situation like this. It must be very difficult for your situation. I know several ways like mindfulness to relieve stress. Do you want to know more about it?"

# Mindfulness
    elif text in ['yes', 'Yes', 'sure', 'Sure',]:
        response = "This is one of the meditation techniques that are widely used by many people, moreover this technique is trendy among teenagers. The technique is known as Mindfulness. \nMindfulness is a meditation that trains someone to focus on the situation(state) around them. This Mindfullness meditation has various benefits for the body, physical health, and mental health. Mindfullness meditation can be done by anyone without special requirements. This type of meditation can also be done anytime and anywhere, both at home, office, or meditation class. \nActually there are many simple ways to do Mindfullness and everyone has their respective preferences. I know 4 forms of Mindfullness exercises, such as: \n1. Attention: \nTry to spend a moment to pay attention to the environment using all the five senses owned. Starting from touch, voice, vision, smell, and taste. \nFor example when you eat your favorite food. Before eating, try smelling the aroma, feel, until it's really enjoyed. \n2. Focus on present: \nThe next mindfulness exercise is to try to focus on what happens to your life right now. Try to pay attention and accept what is already in life. So you will find excitement and pleasure though simple. \n3. Accept yourself: \nAnother form of mindfulness meditation that is good for the body is to accept oneself as it is. Treat yourself as a good friend figure. \n4. Focus on breathing: \nWhen you have negative thoughts, try to sit, take a deep breath and close your eyes. Focus on breathing in and out in the body. Even though your breathing exercises are for just one minute, still this can make you more calm. So negative thoughts can be appeased."

# Thanks
    elif text in ['thanks', 'Thanks', 'Thanks a lot', 'Thank you']:
        response = "Most welcome!"

    else:
        response = "Sorry, I don't understand what you mean. Please rephrase what you said"

    return {"text": response} 

if __name__ == '__main__':
    app.run('0.0.0.0')
