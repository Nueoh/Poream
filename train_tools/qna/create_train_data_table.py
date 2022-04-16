#챗봇 학습 데이터 테이블 생성
import pymysql
#from config.DatabaseConfig import *

DB_HOST='13.124.191.162'
DB_PORT=58796
DB_USER='root'
DB_PASSWORD='dmsgh_0609'
DB_NAME='chatbot'
db = None

try:
    db = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )

    sql = '''
        CREATE TABLE IF NOT EXISTS `chatbot_qna` (
        `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
        `intent` VARCHAR(45) NULL,
        `ner` VARCHAR(1024) NULL,
        `query` TEXT NULL,
        `answer` TEXT NOT NULL,
        `answer_image` VARCHAR(2048) NULL,
        PRIMARY KEY (`id`))
    ENGINE = InnoDB DEFAULT CHARSET=utf8
    '''

    # 테이블 생성
    with db.cursor() as cursor:
        cursor.execute(sql)
        
except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()