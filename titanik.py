import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

df = pd.read_csv("/Users/vanek/Downloads/train (1).csv")

n = int(input("кол-во строк для отображения: "))
print(df.head(n))

print(df.tail())

print("размер таблицы:", df.shape)

print(df.columns)

print(df.dtypes)

numeric = ["Age", "Fare", "SibSp", "Parch"]
categorical = ["Survived", "Pclass", "Sex", "Cabin", "Embarked"]
personal = ["Name", "Ticket", "PassengerId"]

print("числовые: ", numeric)
print("категориальные: ", categorical)
print("персональные: ", personal)

print(df[numeric].agg(["mean", "median", "min", "max", "std"]))

print(df["Pclass"].value_counts())

print("уникальных Embarked:", df["Embarked"].nunique())


size_before = df.shape

print("пропуски по столбцам:")
print(df.isna().sum())

print("процент пропусков:")
print(df.isna().mean() * 100)

print("больше всего пропусков в:", df.isna().sum().idxmax())

age_before = [
    df["Age"].mean(),
    df["Age"].median(),
    df["Age"].min(),
    df["Age"].max(),
    df["Age"].std(),
    df["Age"].count()
]
print(age_before)

med = df["Age"].median()
df["Age"] = df["Age"].fillna(med)

age_after = [
    df["Age"].mean(),
    df["Age"].median(),
    df["Age"].min(),
    df["Age"].max(),
    df["Age"].std(),
    df["Age"].count()
]

compare = pd.DataFrame({
    "показатель": ["среднее арифметическое", "медиана", "минимальный возраст",
                   "максимальный возраст", "стандартное отклонение",
                   "количество известных значений"],
    "до обработки": age_before,
    "после обработки": age_after
})
print(compare)

df = df.dropna(subset=["Embarked"])

cabin_share = df["Cabin"].isna().mean()
print("доля пропусков в Cabin:", round(cabin_share * 100, 2), "%")
if cabin_share > 0.5:
    df = df.drop(columns="Cabin")
    print("столбец Cabin удалён")

print("пропуски после обработки:")
print(df.isna().sum())

print("до обработки:", size_before)
print("после обработки:", df.shape)


age = df["Age"].to_numpy()
sex = df["Sex"].to_numpy()
surv = df["Survived"].to_numpy()
fare = df["Fare"].to_numpy()

print("выжило всего, %:", round(np.mean(surv) * 100, 2))

male_surv = np.mean(surv[sex == "male"]) * 100
female_surv = np.mean(surv[sex == "female"]) * 100
print("выжило мужчин, %:", round(male_surv, 2))
print("выжило женщин, %:", round(female_surv, 2))

male_age = np.mean(age[sex == "male"])
female_age = np.mean(age[sex == "female"])
print("средний возраст мужчин:", round(male_age, 2))
print("средний возраст женщин:", round(female_age, 2))

male_alive_age = np.mean(age[(sex == "male") & (surv == 1)])
male_dead_age = np.mean(age[(sex == "male") & (surv == 0)])
female_alive_age = np.mean(age[(sex == "female") & (surv == 1)])
female_dead_age = np.mean(age[(sex == "female") & (surv == 0)])
print("средний возраст выживших мужчин:", round(male_alive_age, 2))
print("средний возраст погибших мужчин:", round(male_dead_age, 2))
print("средний возраст выживших женщин:", round(female_alive_age, 2))
print("средний возраст погибших женщин:", round(female_dead_age, 2))

print("минимальная стоимость билета:", np.min(fare))
print("максимальная стоимость билета:", np.max(fare))
print("средняя стоимость билета:", round(np.mean(fare), 2))

print("стандартное отклонение возраста:", round(np.std(age, ddof=1), 2))

sex_table = pd.DataFrame({
    "показатель": ["выжило, %", "средний возраст",
                   "средний возраст выживших", "средний возраст погибших"],
    "мужчины": [male_surv, male_age, male_alive_age, male_dead_age],
    "женщины": [female_surv, female_age, female_alive_age, female_dead_age]
})
print(sex_table.round(2))


task1 = df[(df["Sex"] == "male") & (df["Age"] > 30) & (df["Pclass"] == 1)]
print("мужчин старше 30 в 1-м классе:", len(task1))
print(task1.head(10))

task2 = df[((df["Age"] < 18) | (df["Sex"] == "female")) & (df["Survived"] == 1)]
print("выживших детей до 18 или женщин:", len(task2))

fare_mean_3 = df[df["Pclass"] == 3]["Fare"].mean()
print("средняя стоимость билета в 3-м классе:", round(fare_mean_3, 2))
task3 = df[(df["Pclass"] == 3) & (df["Fare"] > fare_mean_3)]
print("пассажиров 3-го класса с билетом дороже среднего:", len(task3))
print(task3.head(10))

task4 = df[(df["Age"] >= 20) & (df["Age"] <= 40) & (df["Embarked"] == "S")]
print("пассажиров 20–40 лет из Southampton:", len(task4))
print(task4.head(10))


stats = df.groupby(["Pclass", "Sex"]).agg(
    count=("Survived", "size"),
    mean_age=("Age", "mean"),
    survived_pct=("Survived", "mean"),
    mean_fare=("Fare", "mean")
)
stats["survived_pct"] = stats["survived_pct"] * 100
stats = stats.round(2)
print(stats)

port_stats = df.groupby("Embarked").agg(
    count=("Survived", "size"),
    survived_pct=("Survived", "mean")
)
port_stats["survived_pct"] = port_stats["survived_pct"] * 100
print(port_stats.round(2))

class_surv = df.groupby("Pclass")["Survived"].mean() * 100
print(class_surv.round(2))
print("больше всего выживших в классе:", class_surv.idxmax())


df.to_csv("titanic_processed.csv", index=False)

stats.to_csv("titanic_statistics.csv")
print("файлы сохранены")

check = pd.read_csv("titanic_processed.csv")
print("размер загруженного файла:", check.shape)
print(check.head())
print("пропуски в загруженном файле:", check.isna().sum().sum())
print("совпадает с исходным:", check.shape == df.shape)



