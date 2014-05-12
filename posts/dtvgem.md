DirecTV STB Web Control Ruby Gem
================================

After creating a DirecTV remote interface for work purposes, I took it upon my self to create a gem so others may use the functions in their own scripts. Surprisingly enough, this was a pretty simple task. All commands are simple HTTP requests sent to the STB (Set-Top Box). In which a JSON page is sent back. The JSON is the parsed and the appropriate values returned.

**Install:**

	gem install dtvcontroller

[**Documentation and Example Usage**](http://github.com/nickpetty/dtvcontroller-gem)