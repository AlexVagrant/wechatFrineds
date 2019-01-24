import itchat
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pyecharts import Pie, Map
from utils import is_chinese

def get_attr(friends, key):
	return list(map(lambda user: user.get(key), friends));

class Wechat(object):

    def __init__(self):
        self.other_name = []
        self.sex = {
            'man': 0,
            'woman': 0,
            'other': 0
        }
        self.Signature = []
        self.Province = []
        self.Province_Dict = {
        }
        self.itchatDef()
        self.echars()
        self.map()
    def itchatDef(self):
        itchat.auto_login(hotReload=True)
        friends = itchat.get_friends()[1:]
        for friend in friends:
            sex1 = friend.sex
            Signature = friend.Signature
            Province = friend.Province

            if not Province:
                self.Province.append('其他')
                if '其他' in self.Province_Dict:
                    self.Province_Dict['其他'] += 1
                else:
                    self.Province_Dict['其他'] = 1
            elif is_chinese(Province):
                if Province in self.Province_Dict:
                    self.Province_Dict[Province] += 1
                else:
                    self.Province_Dict[Province] = 1

                self.Province.append(Province)

            if Signature and Signature.find("span") == -1:
                if is_chinese(Signature):
                    self.Signature.append(Signature)

            if sex1 == 1:
                self.sex['man'] += 1
            elif sex1 == 2:
                self.sex['woman'] += 1
            else:
                self.other_name.append(friend.RemarkName)
                self.sex['other'] += 1

    def wordClound(self):
        try:
            background_image = plt.imread('./naruto_0.jpg')
            wc = WordCloud(
                    background_color="white",
                    random_state=42,
                    mask = background_image,
                    font_path='simkai.ttf',
                    prefer_horizontal=10
            )
            wc.generate(' '.join(self.Signature))
            wc.to_file('test.png')
        except:
            print('生成词云出错了')
    def echars(self):
        sex = self.sex
        attr = ['男', '女', '未知']
        value = [sex['man'],sex['woman'],sex['other']]
        pie = Pie('男女比例图')
        pie.add('', attr, value, is_label_show=True)
        # pie.render()
    def map(self):
        Province_Dict = self.Province_Dict
        province_attr = list(Province_Dict.keys())
        province_value = list(Province_Dict.values())
        print(province_attr,province_value)
        map = Map("全国地图示例", width=1200, height=600)
        map.add("", province_attr, province_value, maptype='china', is_label_show=True)
        map.render()


if __name__ == '__main__':
    wechat = Wechat()
    wechat.wordClound()

