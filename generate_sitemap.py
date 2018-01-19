from lxml import html
import codecs

print "reading sitemap/index.html"

tree = html.parse('sitemap/index.html')

sitemap = codecs.open('sitemap.txt', 'w', 'utf-8')

links = list(set(tree.xpath('//a/@href')))
links.sort()

print "writing links to sitemap.txt"

for link in links:
	sitemap.write(link + '\n')

print "complete"