import web
import re
import os

render = web.template.render('templates/')
urls = ('/', 'index', '/post/(.*)', 'post')

class index():

	def __init__(self):
		print 'started'
		self.render = web.template.render('templates/')

	def GET(self):
		postDictFile = open('postDict', 'r')
		postDict = []
		postList = ''

		for line in postDictFile:
			postData = line.split(':') # 0 - Title, 1 - id, 2 - fileName
			postList += '<a href="post/' + str(postData[1]) + '">' + str(postData[0]) + '</a>' + '<p>'

		return self.render.index(postList)

class post():

	def __init__(self):
		self.render = web.template.render('templates/')

	def GET(self, value):
		value = value.replace(' ','')
		postDictFile = open('postDict', 'r')
		postDict = {}
		postData = ''

		for line in postDictFile:
			postData = line.split(':')
			postDict[postData[1]] = postData[2].strip('\n') + ':' + postData[0]

		postID = postDict[value]
		postData = postID.split(':')

		post = open('static/posts/' + postData[0], 'r')

		return self.render.post(post=post.read(), title=postData[1])
		
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()