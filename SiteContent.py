import requests
import locale
import datetime
from bs4 import BeautifulSoup


class SiteContent:
    def __init__(self, url):
        self._url = url
        self._site = ''
        self._title = ''
        self._published = ''
        locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

    def __str__(self):
        return 'Site: {}, Título: {}, Publicado em: {}'.format(self._site, self._title, self._published)

    def extract(self):
        bold_title = '<strong>{}</strong>'.format(self._title)
        url_formatted = '<<a href="{}">{}</a>>'.format(self._url, self._url)
        today = datetime.datetime.now().strftime('%d de %B de %Y')

        return '{}. [Blog]. {}. Publicação em {}. Disponível em: {}. Acesso em: {}.' \
            .format(self._site, bold_title, self._published, url_formatted, today)

    def format_title(self, title_element):
        if title_element.contents[0] is not None and isinstance(title_element.contents[0], str):
            self._title = title_element.contents[0].strip()

    def format_published(self, published_element):
        published_at = published_element.contents[0]
        published_formatted = published_at

        if published_element.has_attr('datetime'):
            published_formatted = published_element['datetime'].strip('').strip('\r').strip('\n')
            published_formatted = published_formatted[0:10]

        if "/" in published_formatted or "." in published_formatted:
            published_formatted = published_formatted.strip('').strip('\r').strip('\n')
            published_formatted = published_formatted[0:10]

        if published_element.has_attr('datetime') and published_element['datetime'].count('-') > 1:
            published_formatted = datetime.datetime.strptime(published_formatted, '%Y-%m-%d').strftime('%d de %B de %Y')
        elif published_element.has_attr('datetime') and published_element['datetime'].count('/') > 1:
            published_formatted = datetime.datetime.strptime(published_formatted, '%d/%m/%Y').strftime('%d de %B de %Y')
        elif "." in published_formatted and published_formatted.count(".") > 1:
            published_formatted = published_formatted.strip().strip('\n')
            published_formatted = published_formatted[0:10]
            published_formatted = datetime.datetime.strptime(published_formatted, "%d.%m.%Y").strftime('%d de %B de %Y')

        self._published = published_formatted.strip()

    def search(self):
        page = requests.get(self._url)
        soup = BeautifulSoup(page.text, 'html.parser')

        site_element = soup.find('meta', property='og:site_name')
        title_element = soup.find('h1')
        published_element = soup.find('time')

        if title_element != None:
            self.format_title(title_element)

        if site_element != None:
            self._site = site_element['content'].strip()

        if published_element != None:
            self.format_published(published_element)
