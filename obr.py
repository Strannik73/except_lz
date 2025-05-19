import pandas as pd

class Tester:
    def __init__(self, df):
        try:
            self.df = pd.read_csv(df)
        except FileNotFoundError:
            print('отсутствует файл')
            raise SystemExit()
        
        except pd.errors.EmptyDataError:
            print('файл пуст')
            raise SystemExit()
        
        
        try:
            v3 = self.df.columns.to_list()
            self.data = pd.read_csv('var3.csv')
            v3i = self.data.columns.to_list()
            if v3 != v3i:
                raise TypeError 
        except TypeError:
            print('ошибка в колонках')
            
            
        try:
            self.d1 = str(self.df.dtypes)
            self.d2 = str(self.data.dtypes)
            
            if self.d1 == self.d2:
                raise TypeError('проблем нет')
            else:
                print('другой тип данных')
        except TypeError:
            print('разные файлы')


def main():
    df = 'var3i.csv'            
    df = Tester(df)

if __name__ == "__main__":
    main()
    