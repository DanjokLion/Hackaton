from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import upload_file


def handling(upload_file_path):
    spark = SparkSession.builder.appName("DataHandling").getOrCreate()
    dataset_org_df = spark.read.csv("C:\Users\Pixel\Desktop\DatasetOrg.csv", header=True, inferSchema=True)
    upload_file_df = spark.read.csv(upload_file_path, header=True, inferSchema=True)
    columns_dataset_org = ['ID компании', 'Наименование полное', 'Наименование краткое', 'ИНН', 'Юр адрес', 'Факт адрес', 'ОГРН', 
                        'Головная компания (1) или филиал (0)', 'КПП', 'ОКОПФ (код)', 'ОКОПФ (расшифровка)', 'ОКВЭД2', 
                        'ОКВЭД2 расшифровка', 'Дата создания', 'статус по ЕГРЮЛ ', 'ОКФС код', 'ОКФС (форма собственности)',
                        'Компания действующая (1) или нет (0)', 'id Компании-наследника (реорганизация и др)', 
                        'ФИО директора', 'Название должности', 'доп. ОКВЭД2']
    result_df = spark.createDataFrame([], schema=dataset_org_df.schema)
    for column in columns_dataset_org:
        if column in upload_file_df.columns:
          filtered_df = dataset_org_df.filter(col(column).isin(upload_file_df.select(column).rdd.flatMap(lambda x: x).collect()))
          result_df = result_df.union(filtered_df)
        else:
          print(f"There is no such column: {column}")


    return result_df