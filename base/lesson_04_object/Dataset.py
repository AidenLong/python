from sklearn import svm, datasets

class Dataset:
    # 我们创造一个dataset的类，这个类会帮我们下载相关的数据集，
    # 并给我们分类好x,y
    def __init__(self, name):
        # 告诉类，我们需要哪一个数据集
        # 我们有两个选择，一个是'iris'一个是'digits'
        self.name = name

    def download_data(self):
        # 从sklearn的自带集中下载我们指定的数据集
        if self.name == 'iris':
            # 这里是sklearn自带的数据集下载方法，更多信息可以参照官网
            self.downloaded_data = datasets.load_iris()
        elif self.name == 'digits':
            self.downloaded_data = datasets.load_digits()
        else:
            # 如果不是我们预想的两种数据集，则报错
            print('Dataset Error: No named datasets')

    def generate_xy(self):
        # 通过这个过程来把我们的数据集分为原始数据以及他们的label
        # 我们先把数据下载下来
        self.download_data()
        x = self.downloaded_data.data
        y = self.downloaded_data.target
        print('\nOriginal data looks like this: \n', x)
        print('\nLabels looks like this: \n', y)
        return x, y

    def get_train_test_set(self, ratio):
        # 这里，我们把所有的数据分成训练集和测试集
        # 一个参数要求我们告知，我们以多少的比例来分割训练和测试集
        # 首先，我们把XY给generate出来：
        x, y = self.generate_xy()

        # 有个比例，我们首先得知道 一共有多少的数据
        n_samples = len(x)
        # 于是我们知道，有多少应该是训练集，多少应该是测试集
        n_train = (int) (n_samples * ratio)
        # 好了，接下来我们分割数据
        X_train = x[:n_train]
        y_train = y[:n_train]
        X_test = x[n_train:]
        y_test = y[n_train:]
        # 好，我们得到了所有想要的玩意儿
        return X_train, y_train, X_test, y_test
# ====== 我们的dataset类创造完毕=======

# 比如，我们使用digits数据集
data = Dataset('digits')
# 接着，我们可以用0.7的分割率把xy给分割出来
X_train, y_train, X_test, y_test = data.get_train_test_set(0.7)


clf = svm.SVC()
print(clf.fit(X_train, y_train))
test_point = X_test[12]
y_true = y_test[12]
clf.predict(test_point)