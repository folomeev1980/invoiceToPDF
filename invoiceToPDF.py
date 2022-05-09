from xhtml2pdf import pisa
import datetime
from core import get_string_by_number as number_to_string
from django.template.loader import get_template
from django.template import Context
from django.template import Template
from django.conf import settings
import django
import os


def fetch_pdf_resources(uri, rel):
    print('fetch', uri)
    if uri[0:5] == 'media':
        path = os.getcwd()+"/media" + uri[5:]
        print(path)
    else:
        path = None
    return path


def toPDF(**kwarg):
    result = open('invoice.pdf', "w+b")
    with open('sample.html', 'r', encoding='utf-8-sig') as f:
        html = f.read()

    html = html.format(
        invoice_number=kwarg['invoice_number'],
        invoice_date=kwarg['invoice_date'],
        contragent=kwarg['contragent'],
        qty=kwarg['qty'],
        price=kwarg['price'],
        full_price=str(int(kwarg['qty']) * float(kwarg['price'])),
        words_price=number_to_string(
            float(int(kwarg['qty']) * float(kwarg['price']))))

    # template = Template(html)
    # context = Context({})
    # html = template.render(context)
    # print(html)
    pisa.pisaDocument(html.encode("UTF-8"), result, encoding='UTF-8', link_callback=fetch_pdf_resources)


if __name__ == '__main__':

    # MEDIA_ROOT = os.getcwd()
    # MEDIA_URL = '/media/'
    #
    # TEMPLATES = [
    #     {
    #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #         'DIRS': [],
    #     }
    # ]requirements.txt
    # settings.configure(TEMPLATES=TEMPLATES)
    # django.setup()

    input_json = {
        'invoice_number': '1',
        'contragent': "ЗАО «УНИГРА», 121099, Москва, ул.Новый Арбат, 34, стр.1, помещение 1, этаж4, комнаты 7,8, ИНН 7704245553, КПП 771932001, р/с 40702810900000000195, банк ООО 'ДОЙЧЕ БАНК', г. Москва, кор.счет 30101810100000000101, БИК 044525101 AAAAAA BBBBBB CCCCCCCC DDDDDDD ФФФФФФ",
        'price': '3750.12',
        'qty': '3',
        'invoice_date': datetime.datetime.now().strftime("%d.%m.%Y")}

    toPDF(**input_json)
