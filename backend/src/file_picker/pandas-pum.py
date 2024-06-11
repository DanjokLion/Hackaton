import pandas as pd
import upload_file


def handling(upload_file):
    colomn_DatasetOrg = ['ID компании', 'Наименование полное', 'Наименование краткое', 'ИНН', 'Юр адрес', 'Факт адрес', 'ОГРН', 'Головная компания (1) или филиал (0)', 'КПП', 'ОКОПФ (код)', 'ОКОПФ (расшифровка)', 'ОКВЭД2', 'ОКВЭД2 расшифровка', 'Дата создания', 'статус по ЕГРЮЛ ',
                         'ОКФС код', 'ОКФС (форма собственности)', 'Компания действующая (1) или нет (0)', 'id Компании-наследника (реорганизация и др)', 'ФИО директора', 'Название должности', 'доп. ОКВЭД2']
    with open('C:\Users\Pixel\Desktop\DatasetOrg.csv', 'r') as file:
        DatasetOrg = file.read()
        DatasetOrg = pd.DataFrame
        upload_file = pd.DataFrame
        for column in colomn_DatasetOrg:
            if column in upload_file[column]:
                    string = DatasetOrg[DatasetOrg[column].isin(upload_file[column])]
                    print(string)
            else:
                print(f"There is no such column: {column}")