# -*- coding: utf-8 -*-

from pyjon.reports import ReportFactory
import random
import os
import string
PATH_CURRENT = os.path.dirname(os.path.abspath(__file__))

def main():
    factory = ReportFactory()
    name = "tombola"
    nombre_ticket = 400
    # name = "repas"
    template = os.path.join(PATH_CURRENT, 'template', "%s.xml" % name)
    datas = []
    num_random = generate_numbers(nombre_ticket)
    for item in xrange(nombre_ticket):
        datas.append({'numero': item + 1,
                     'num_rand': num_random.next()})

    factory.render_template(
            template_file=template,
            title=u'tickets',
            data=datas,
            path_current = PATH_CURRENT)
    factory.render_document('%s.pdf' % name)
    factory.cleanup()

def generate_numbers(occurence):
    """Génére une liste de code unique de la forme
    CCCLL avec c chiffre et s une lettre"""
    l_numbers = []
    for item in xrange(occurence):
        control = True
        while control:
            start_num = str(random.randint(0, 999)).rjust(3, "0")
            end_num = "".join([string.letters[random.randint(0, 25)] for item in range(0,2)])
            num = start_num + end_num
            if not num in l_numbers:
                yield num
                control = False
    # return l_numbers








if __name__ == '__main__':
    main()
