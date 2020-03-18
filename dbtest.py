import psycopg2
class sqlclass():
    def excutesql(sql):
        conn = psycopg2.connect(database="kzkt", user="kzkt",password="kzkt", host="10.4.7.199", port="5432")
        cursor = conn.cursor()
        print("数据库连接成功")
        try:
            cursor.execute(sql)
            print("正在执行sql：" + sql)
            conn.commit()
            print("执行成功！")
        except:
            print("执行出错了，请检查sql：" + sql)
            conn.rollback();
            conn.close()


