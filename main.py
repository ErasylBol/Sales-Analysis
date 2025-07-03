import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'sample.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

print("🔹 Первые 5 строк таблицы:")
print(df.head())

print("\n🔹 Информация о столбцах:")
print(df.info())

print("\n🔹 Проверка пропущенных значений:")
print(df.isnull().sum())


print("\nДата заказа: от", df['Order Date'].min(), "до", df['Order Date'].max())

top_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False ).head(5)
print("\n💰 Топ-5 прибыльных подкатегорий:\n", top_profit)

df['Month'] = df['Order Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Sales'].sum()



monthly_sales.plot(kind='line', figsize=(12, 5), title='Продажи по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Сумма продаж')
plt.tight_layout()
plt.show()
