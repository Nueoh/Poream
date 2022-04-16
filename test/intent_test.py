from Preprocess import Preprocess
from IntentModel import IntentModel



p = Preprocess(word2index_dic='../train_tools/dict/raw_chatbot_dict.bin',
               userdic='../utils/user_dic.tsv')

intent = IntentModel(model_name='../models/intent/real_chatbot.h5', proprocess=p)
query = "사전학습 필수인가요?"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]

print(query)
print("의도 예측 클래스 : ", predict)
print("의도 예측 레이블 : ", predict_label)
