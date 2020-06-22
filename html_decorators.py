def div(func):
    def wraper(*args, **kwargs):
        return '<div>{}</div>'.format(func(*args, **kwargs))
    return wraper

def article(func):
    def wraper(*args, **kwargs):
        return '<article>{}</article>'.format(func(*args, **kwargs))
    return wraper

def p(func):
    def wraper(*args, **kwargs):
        return '<p>{}</p>'.format(func(*args, **kwargs))
    return wraper
    
@div
@article
@p
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'

def run():
    print(saludo('Jorge'))

if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
