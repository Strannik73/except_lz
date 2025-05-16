import pandas as pd


class sumop:

    def __init__(self):
        self.df = pd.read_csv('var3.csv')

    def __neg__(self):
        return self.df.drop_duplicates()


    def dann(self):
        df = -self.df
        
        columns = ['Участники гражданского оборота','Тип операции','Сумма операции','Вид расчета','Место оплаты','Терминал оплаты','Дата оплаты','Время оплаты','Результат операции','Cash-back,Сумма cash-back']
        if not all(col in self.data.columns for col in columns):
            raise ValueError('CSV файл должен содержать колонки')