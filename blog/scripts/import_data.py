from blog.models import Article

def run():
    for i in range(7,17):
        article = Article()
        article.title = "Article n° #%d" % i
        article.desc = "Description de l'article n° #%d" % i
        article.image = "http://default"
        article.save()
    
print("Opération réussie")
