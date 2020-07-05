from SiteContent import SiteContent
from operator import attrgetter

def welcome_message():
    print("*************************************")
    print("******FORMATADOR DE REFERÊNCIAS******")
    print("*************************************")
    print("Preencha o arquivo 'links.txt' com as referências consultadas que o app irá gerar as referências formatadas ;)")
    print("Aguarde enquanto o app gera as referências!")


def finished_message():
    print("-----------------------------------------")
    print("Formatação finalizada. Consulte o arquivo 'references.html' para visualizar a formatação :)")
    print("-----------------------------------------")


welcome_message()
references_list = []

links_file = open("links.txt", "r")

for item in links_file:
    page = SiteContent(item.strip())
    page.search()
    references_list.append(page)

ordered_list = sorted(references_list, key=attrgetter('_site'))
extracted_list = [item.extract() for item in ordered_list]

references_file = open("references.html", "w")

for item in extracted_list:
    references_file.writelines([item, '<br /><br />'])

references_file.close()
finished_message()