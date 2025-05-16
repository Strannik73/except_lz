import pandas as pd
#from __ import __


class obrabotka:
    def __init__(self): 
        self.df = pd.read_csv('var3.csv')
        self.dfi = pd.read_csv('var3i.csv')
        
        try:
            self.df = self.dfi
        except FileNotFoundError:
            print('файла нет')
            raise
        except pd.errors.EmptyDataError:
            print('файл пустой')
            raise
        
        try:    
            if self.df != self.dfi:
                raise TypeError 
        except TypeError:
            print('ошибка в колонках')
            
        try:
            self.v3 = str(self.df.dtypes)
            self.v3i = str(self.dfi.dtypes)
            if self.v3 != self.v3i: 
                print('другой тип данных')
                raise TypeError 
            else:
                print('есть совпадение')
        except TypeError:
            print('несовпадение файлов ожидплся изменный файл')
                
        
    def __del__(self):
        print('удаление')


def main():
    obr_a = obrabotka('var3.csv')
    obr_a = obrabotka('var3i.csv')
    obr_a.dann()

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    