from DatabaseConfig import *
from Database import Database
from Preprocess import Preprocess

# 전처리 객체 생성
p = Preprocess(word2index_dic='../train_tools/dict/raw_chatbot_dict.bin',
               userdic='../utils/user_dic.tsv')

# 질문/답변 학습 디비 연결 객체 생성
db = Database(
    host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME
)
db.connect()    # 디비 연결

# 원문
# query = "오전에 탕수육 10개 주문합니다"
# query = "화자의 질문 의도를 파악합니다."
# query = "안녕하세요"
query = "사전학습 필수인가요?"

# 의도 파악
from IntentModel import IntentModel
intent = IntentModel(model_name='../models/intent/real_chatbot.h5', proprocess=p)
predict = intent.predict_class(query)
intent_name = intent.labels[predict]

# 개체명 인식
'''
from models.ner.NerModel import NerModel
ner = NerModel(model_name='../models/ner/ner_model.h5', proprocess=p)
predicts = ner.predict(query)
ner_tags = ner.predict_tags(query)
'''
predicts = None
ner_tags = None

print("질문 : ", query)
print("=" * 100)
print("의도 파악 : ", intent_name)
print("개체명 인식 : ", predicts)
print("답변 검색에 필요한 NER 태그 : ", ner_tags)
print("=" * 100)

# 답변 검색
from FindAnswer import FindAnswer

try:
    f = FindAnswer(db)
    answer_text, answer_image = f.search(intent_name, ner_tags)
    answer = f.tag_to_word(predicts, answer_text)
except:
    answer = "포림이는 모르는 게 너무 많아~"

print("답변 : ", answer)

db.close() # 디비 연결 끊음