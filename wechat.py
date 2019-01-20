import itchat
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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

		itchat.auto_login(hotReload=True)
		friends = itchat.get_friends()[1:]
		for friend in friends:
			sex1 = friend.sex
			Signature = friend.Signature
			if Signature and Signature.find("span") == -1:
				self.Signature.append(Signature)
			if sex1 == 1:
				self.sex['man'] += 1
			elif sex1 == 2:
				self.sex['woman'] += 1
			else:
				self.other_name.append(friend.RemarkName)
				self.sex['other'] += 1
	def wordClound(self):
		background_image = plt.imread('./naruto_0.jpg')
		wc = WordCloud(
				background_color="white",
				mask = background_image,
				random_state=42,             #   为每一词返回一个PIL颜色
				font_path='simkai.ttf',
				prefer_horizontal=10).generate(' '.join(self.Signature))       #   调整词云中字体水平和垂直的多少
		wc.to_file('test.png')

if __name__ == '__main__':

	wechat = Wechat()
	wechat.wordClound()
	print(wechat.sex)
	print(wechat.other_name)

