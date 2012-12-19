#!/usr/bin/env python2.7

import jinja2
import sys
from pygments import highlight
from pygments.lexers import DiffLexer
from pygments.formatters import HtmlFormatter


def main(tmpfile):
    f = open(tmpfile,'r')
    mydiff = f.read()
    f.close()
    hdiff = highlight_diff(mydiff)
    page = create_page(hdiff)
    write(page)

def highlight_diff(fd):
    htmldiff = highlight(fd, DiffLexer(), HtmlFormatter(linenos=True))
    return htmldiff

def create_page(diff, title='Svn demo diff'):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./', encoding='utf-8'))
    template = env.get_template('svndiff2html.tpl')
    return template.render({'title': title
                            , 'scripts': []
                            , 'styles': ['svndiff2html.css']
                            , 'diff': diff})

def create_css():
    f = open('svndiff2html_new.css', 'w')
    f.write(HtmlFormatter().get_style_defs('.highlight'))
    f.close()

def write(diff):
    f = open('diff.html','w')
    f.write(diff)
    f.close()


if __name__ == '__main__':
   main(sys.argv[1])
   create_css()


