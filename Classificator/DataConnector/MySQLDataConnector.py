import Classificator.DataConnector.IDataConnector as ModuleIDataConnector
import mysql.connector as mysql


class MySQLConnector(ModuleIDataConnector.IDataConnector):
    __MySQLConnector: mysql.connect

    def __init__(self):
        print('Connecting to MySQL database...')
        self.__MySQLConnector = mysql.connect(host='localhost', user='root', password='h8970102742', use_unicode=True,
                                              charset='utf8')
        self.__MySQLConnector.database = "lica"
        print("Connection established")

    def __del__(self):
        self.__MySQLConnector.close()

    def get_null_tem_in_forum(self, num_forum):
        cursor = self.__MySQLConnector.cursor()
        sql_statement = """
                                SELECT d.id
                                FROM hsuforum_discussions d
                                JOIN hsuforum_trash t ON d.id=t.discussionid
                                WHERE d.forum = %s
                        """
        cursor.execute(sql_statement, [num_forum])
        null_tem = cursor.fetchall()

        if len(null_tem) == 0:
            null_tem = None
        else:
            null_tem = null_tem[0][0]

        return null_tem

    def get_list_tem_in_forum(self, num_forum):

        return num_forum

    def run_sql_query(self, sql_query):
        return sql_query

    def get_list_forum(self):
        sql_statement = """
            SELECT distinct forum
                FROM hsuforum_discussions
        """
        cursor = self.__MySQLConnector.cursor()
        cursor.execute(sql_statement)
        tmp_list_forum = cursor.fetchall()

        list_forum = []
        if len(tmp_list_forum) != 0:

            for ElemList in tmp_list_forum:
                list_forum.append(ElemList[0])

        return list_forum


# Для тестирования реализации интерфейса
if __name__ == "__main__":
    connector = MySQLConnector()

    test_list_forum = connector.get_list_forum()
    print(test_list_forum)

    for test_num_forum in test_list_forum:
        test_null_tem = connector.get_null_tem_in_forum(test_num_forum)
        print(test_null_tem)
