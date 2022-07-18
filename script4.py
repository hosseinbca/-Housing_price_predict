"""
 This script is final code and performs machine learning work and predict.
 also this code shows some information about our datas.
"""
print("\n================================\nLoading...")

from informationAndvariables import *
from tkinter import *
from sklearn.linear_model import ElasticNet , Lasso , Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(DATASETV3_20_ADDRESS)  # dataset file
dataset = dataset.iloc[:, 1:]

price_per_meter_df = pd.read_csv(PRICE_PER_METER_ADDRESS)
price_per_meter_df = price_per_meter_df.iloc[:, 1:]

ridge_score, ensemble_score, lasso_score, elastic_score = 0, 0, 0, 0

# create train & test
X = dataset.drop(["Price", "District"], axis=1)
y = dataset["Price"]
X_train, X_test, y_train, y_tests = train_test_split(X, y, test_size=0.2)

ridge = Ridge()
ridge.fit(X_train, y_train)
ridge.score(X_test, y_tests)
ridge_score = ridge.score(X_test, y_tests)

ensemble_reg = RandomForestRegressor()
ensemble_reg.fit(X_train, y_train)
ensemble_reg.score(X_test, y_tests)
ensemble_score = ensemble_reg.score(X_test, y_tests)

lasso = Lasso()
lasso.fit(X_train, y_train)
lasso.score(X_test, y_tests)
lasso_score = lasso.score(X_test, y_tests)

elastic = ElasticNet()
elastic.fit(X_train, y_train)
elastic.score(X_test, y_tests)
elastic_score = elastic.score(X_test, y_tests)

print("\n\n================================\nLoading finished")

class PredictWindow:            #UI
    def __init__(self, win):
        self.btn2 = Button(win, text='توضیحات', command=self.description)
        self.btn2.place(x=0, y=0)
        self.lbl0 = Label(win, text=': مساحت')
        self.lbl0.place(x=230, y=10)
        self.t0 = Entry()
        self.t0.place(x=100, y=10)
        self.lbl1 = Label(win, text=': سال ساخت')
        self.lbl1.place(x=230, y=40)
        self.t1 = Entry()
        self.t1.place(x=100, y=40)
        self.lbl2 = Label(win, text=': تعداد اتاق')
        self.lbl2.place(x=230, y=70)
        self.t2 = Entry()
        self.t2.place(x=100, y=70)
        self.lbl3 = Label(win, text=': منطقه')
        self.lbl3.place(x=230, y=100)
        self.t3 = Entry()
        self.t3.place(x=100, y=100)
        self.lbl4 = Label(win, text=': قیمت هر متر')
        self.lbl4.place(x=230, y=130)
        self.t4 = Entry()
        self.t4.place(x=100, y=130)
        self.var = IntVar()
        self.r1 = Radiobutton(win, text="Ridge", variable=self.var, value=1)
        self.r1.place(x=50, y=160)
        self.rbl1 = Label(win, text='score : '+str(ridge_score))
        self.rbl1.place(x=200, y=162)
        self.r2 = Radiobutton(win, text="Ensemble Regression", variable=self.var, value=2)
        self.r2.place(x=50, y=180)
        self.rbl2 = Label(win, text='score : '+str(ensemble_score))
        self.rbl2.place(x=200, y=182)
        self.r3 = Radiobutton(win, text="Lasso", variable=self.var, value=3)
        self.r3.place(x=50, y=200)
        self.rbl3 = Label(win, text='score : '+str(lasso_score))
        self.rbl3.place(x=200, y=202)
        self.r4 = Radiobutton(win, text="Elasticnet", variable=self.var, value=4)
        self.r4.place(x=50, y=220)
        self.rbl4 = Label(win, text='score : '+str(elastic_score))
        self.rbl4.place(x=200, y=222)
        self.btn1 = Button(win, text='محاسبه', command=self.predict)
        self.btn1.place(x=30, y=258)
        self.lbl5 = Label(win, text=': قیمت پیشبینی شده (تومان)')
        self.lbl5.place(x=230, y=260)
        self.t5 = Entry(bd=3)
        self.t5.place(x=100, y=260)
        self.b1 = Button(win, text='نمایش نمودار پراکندگی قیمت', command=self.showchart1)
        self.b1.place(x=200, y=310)
        self.b2 = Button(win, text='نمایش نمودار همبستگی', command=self.showchart2)
        self.b2.place(x=210, y=340)
        self.b3 = Button(win, text='نمایش نمودار درستی پیشبینی', command=self.showchart3)
        self.b3.place(x=200, y=370)
        self.b4 = Button(win, text='چاپ دیتاست', command=self.printinfo1)
        self.b4.place(x=80, y=310)
        self.b5 = Button(win, text='چاپ نوع متغیر ستون ها', command=self.printinfo2)
        self.b5.place(x=50, y=340)
        self.b6 = Button(win, text='چاپ تعداد عناصر خالی', command=self.printinfo3)
        self.b6.place(x=50, y=370)

    def description(self):
        newWindow = Tk()
        newWindow.title("توضیحات")
        newWindow.geometry("490x390")
        text_box = Text(newWindow,height=30,width=150 )
        text_box.tag_configure('tag-right', justify='right')
        text_box.pack(expand=True)
        text_box.insert('end',DESCRIPTION,'tag-right')
        text_box.config(state='disabled')


    def predict(self):  # گذاشتن شرط روی متغییر ها برای وارد نشدن اعداد غیر مجاز
        self.t5.delete(0, 'end')
        temp_info = [[0, 0, 0, 0]]
        temp_info[0][0] = int(self.t0.get())
        temp_info[0][1] = 1400-int(self.t1.get())
        temp_info[0][2] = int(self.t2.get())
        if self.t4.get() == "" :
            temp_info[0][3] = int(price_per_meter_df.at[int(self.t3.get()),'avarage'])
        else:
            temp_info[0][3] = int(self.t4.get())
        if self.var.get() == 1:
            self.t5.insert(END, int(float('%.08f' % ridge.predict(temp_info)[0])))
        elif self.var.get() == 2:
            self.t5.insert(END, int(float('%.08f' % ensemble_reg.predict(temp_info)[0])))
        elif self.var.get() == 3:
            self.t5.insert(END, int(float('%.08f' % lasso.predict(temp_info)[0])))
        elif self.var.get() == 4:
            self.t5.insert(END, int(float('%.08f' % elastic.predict(temp_info)[0])))
        else:
            self.t5.insert(END, str("Select a model"))

    def showchart1(self):
        fig, ax = plt.subplots(figsize=(8, 5))
        ax = dataset["Price"].hist(bins=600)
        plt.xlim(xmin=100000000, xmax=20000000000)
        ax.set(title="House Price Histogram",
               xlabel="House Price in T", ylabel="Freq")
        plt.show()

    def showchart2(self):
        import seaborn as sns
        X = dataset.drop("Price", axis=1)
        correlation_matrix = X.corr().round(2)
        fig, ax = plt.subplots(figsize=(8, 5))
        cmap = sns.diverging_palette(230, 20, as_cmap=True)
        ax = sns.heatmap(data=correlation_matrix, annot=True, cmap=cmap)
        plt.show()

    def showchart3(self):
        y_preds1 = ridge.predict(X_test)
        fig, ax = plt.subplots(2,2)
        ax[0,0].scatter(y_tests, y_preds1)
        ax[0,0].set(xlabel="Real Values", ylabel="Predictions (Ridge)")
        y_preds2 = ensemble_reg.predict(X_test)
        ax[0,1].scatter(y_tests, y_preds2)
        ax[0,1].set(xlabel="Real Values", ylabel="Predictions (Ensemble Regression)")
        y_preds3 = lasso.predict(X_test)
        ax[1,0].scatter(y_tests, y_preds3)
        ax[1,0].set(xlabel="Real Values", ylabel="Predictions (Lasso)")
        y_preds4 = elastic.predict(X_test)
        ax[1,1].scatter(y_tests, y_preds4)
        ax[1,1].set(xlabel="Real Values", ylabel="Predictions (Elasticnet)")
        plt.show()

    def printinfo1(self):
        print(dataset)

    def printinfo2(self):
        print("\nDataset columns data types :")
        print(dataset.dtypes)

    def printinfo3(self):
        print("\nDataset columns null values :")
        print(dataset.isnull().sum())


window = Tk()
mywin = PredictWindow(window)
window.title('پیشبینی قیمت مسکن')
window.geometry("400x410+10+10")
window.mainloop()