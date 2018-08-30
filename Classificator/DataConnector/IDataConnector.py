# Интерфейс для реализации конектеров. Все реализации интерфейсы должны включать реализации данных методов.
# Принимаемые и возвращаемые параметры должны быть соблюдены


class IDataConnector(object):

    # Получить id нулевой темы форума
    # Принимает id форума в формате int
    # Возвращает id нулевой темы в формате int
    # Если у данного форума нет нулевой темы, то возвращает None
    # def GetNullTemInForum(self, NumForum):
    def get_null_tem_in_forum(self, num_forum):
        raise NotImplementedError(
            'Определите GetNullTemInForum в %s.' % self.__class__.__name__)

    # Извлечь темы по форуму
    # Принимает id форума в формате int
    # Возвращает id нулевой темы в формате int
    # Если у данного форума нет нулевой темы, то возвращает None
    def get_list_tem_in_forum(self, num_forum):
        raise NotImplementedError(
            'Определите GetListTemInForum в %s.' % self.__class__.__name__)

    # Извлечь id форумов
    # Возвращает список форумов. Если форумов нет, то возвращает пустой список.
    def get_list_forum(self):
        raise NotImplementedError(
            'Определите GetListTemInForum в %s.' % self.__class__.__name__)

    # Выполнить Sql запрос
    def run_sql_query(self, sql_query):
        raise NotImplementedError(
            'Определите RunSqlQuery в %s.' % self.__class__.__name__)
