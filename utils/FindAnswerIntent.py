class FindAnswer:
    def __init__(self, db):
        self.db = db

    # 검색 쿼리 생성
    def _make_query(self, intent_name):
        sql = "select * from chatbot_qna" ## 바꿔야 할듯? 
        if intent_name != None:
            #sql = sql + " where intent='{}' ".format(intent_name)
            sql = sql + " where intent='{}' ".format(intent_name)
        # 동일한 답변이 2개 이상인 경우, 랜덤으로 선택
        sql = sql + " order by rand() limit 1"
        return sql

    # 답변 검색
    def search(self, intent_name):
        # 의도명, 개체명으로 답변 검색
        sql = self._make_query(intent_name)
        answer = self.db.select_one(sql)

        return (answer['answer'], answer['answer_image'])
