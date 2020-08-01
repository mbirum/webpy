import web

urls = (
    '/', 'index',
    '/tree/on', 'treeon',
    '/tree/off', 'treeoff',
    '/tree', 'gettree'
)

class index:
    def GET(self):
        return "Hello, world!"

class gettree:
     def GET(self):
          return "Get tree"

class treeon:
     def POST(self):
          return "Tree on"

class treeoff:
     def POST(self):
          return "Tree off."

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
