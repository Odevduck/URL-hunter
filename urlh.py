import requests
import sys
class urlh:
    countln = 0
    rv = -1
    def usage(self):
        print('''usage:
        ./urlh.py DirectoriesWorldlist.txt SubdomainWorldlist.txt http://www.examplesite.net/
        ''')
    def rln(self,arg=sys.argv):
        try:
            file = open(f'{arg[1]}', 'r')
            for line in file:
                urlh.countln = urlh.countln + 1
            urlh().rhttp()
        except:
            urlh().usage()
    def rhttp(self,url=sys.argv):
        try:
            if 'https://' in url[3] or 'http://' in url[3]:
                domainf = open(f'{url[2]}','r')
                domain = str(domainf.read()).split()
                one = 0
                two = 1
                for x in range(len(domain)):
                    for urlh.countln in range(urlh.countln):
                        file = open(f'{url[1]}', 'r')
                        x = file.read().split()
                        urlh.rv += 1
                        r = requests.get(url[3] + x[urlh.rv])
                        if r.status_code == 200:
                            print(url[3] + x[urlh.rv])
                    url[3] = url[3].replace(domain[one],domain[two])
                    one += 1
                    two += 1
                    urlh.rv = 0
        except:
            pass
urlh().rln()