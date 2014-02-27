import web
from web import form
import re
import os
import markdown
import yaml

render = web.template.render('templates/')
urls = ('/', 'index', '/post/(.*)', 'post', '/edit', 'edit', '/login', 'login')

class index():

	def __init__(self):
		print 'started'
		self.render = web.template.render('templates/')

	def GET(self):
		postDictFile = open('postDict', 'r')
		postDict = {}
		postData = ''
		postList = ''

		for line in postDictFile:
			postData = line.split(':') # 0 - Title, 1 - id, 2 - fileName
			summary = open('static/posts/' + postData[2].strip('\n')).read()
			postList += '<h3><center><a href="post/' + str(postData[1]) + '"><b>' + str(postData[0]) + '</b></a></center></h3><p>\n' + summary[0:600] + '...' + '<p>\n'

		postDictFile.close()
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
		postDictFile.close()

		return self.render.post(post=post.read(), title=postData[1])
		post.close()

editPost = form.Form(form.Textbox('postTitle'), form.Textarea('post'))

class edit():

	def __init__(self):
		self.render = web.template.render('templates/')
		f = open('user', 'r')
		if '0' in f.read():
			raise web.seeother('/login')
		#check to see if use is logged in
		#if not, seeother 'login'
		#if yes, proceed

	def GET(self):
		form = editPost()
		return render.edit(form)

	def POST(self):
		inputFromForm = web.input()
		post = inputFromForm.post
		postTitle = inputFromForm.postTitle

		f = open('temp', 'w')
		f.write(post)
		f.close()

		f = open('temp', 'r+')

		draft = f.read()

		html = markdown.markdown(draft)
		return render.preview(html)

		#get input from text box and run it through markdown converter
		#save to file
		#save to postDict file

loginForm = form.Form(form.Textbox('username'), form.Textbox('password'))

class login():

	def __init__(self):
		self.render = web.template.render('templates/')
		#check to see if user is already logged in

	def GET(self):
		form = loginForm()
		users = open('users.yaml', 'r').read()
		yaml.load(users)
		print yaml['nicholas']


		#present user login form

	def POST(self):
		form = loginForm()
		inputFromForm = web.input()
		username = inputFromForm.username
		password = inputFromForm.password

		if username == 'user' and password == 'pass':
			f = open('user', 'w')
			f.write('1')
			raise web.seeother('/edit')
		else:
			return render.login(form, var1='Wrong username/password')

		#get login info, save to file (db)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()









