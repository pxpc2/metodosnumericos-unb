import numpy as np
import matplotlib.pyplot as plt


def tem_raiz(f, a, b):
    return f(a) * f(b) < 0


def bissecao_abs(f, a, b, tol, prt):
    if (f(a) * f(b)) > 0:
        print('nao ha raiz no intervalo')
        return []
    x1 = 0
    erro = -1
    for k in range(1, 200):
        erro = abs(b - a)
        # faz a bissecao / seria uma estimativa da raiz
        x1 = (a + b) / 2

        if prt:
            print("%d\t%.10f(%2d)\t%.10f(%2d)\t%.10f(%2d)\t%.1e"
                  % (k, a, np.sign(f(a)), x1, np.sign(f(x1)),
                     b, np.sign(f(b)), erro))

        if (erro < tol) | (f(x1) == 0):
            break
        if f(x1) * f(a) < 0:
            b = x1
        else:
            a = x1
    if prt:
        n_dec = int(np.ceil(np.abs(np.log10(erro))) + 1)
        form = "{:." + str(n_dec) + "f}"
        x1_str = form.format(x1)
        print(x1_str)
    return x1


def falsa_posicao(f, a, b, tol, prt):
    if not (tem_raiz(f, a, b)):
        print('nao ha raiz no intervalo')
        return []
    x1 = a
    na = 0  # contador estagnacao a esquerda
    nb = 0  # contador estagnacao a direita
    fa = f(a)
    fb = f(b)

    for k in range(1, 500):
        x0 = x1
        # calcula o novo x1 com a falsa posicao
        x1 = (a * f(b) - b * f(a) / (f(b) - f(a)))
        erro = -1
        if x1 != 0:
            erro = abs((x1 - x0) / x1)

        if prt:
            print('%i\t%.10f(%2d)\t%.10f(%2d)\t%.10f(%2d)\t%.1e' %
                  (k, a, np.sign(f(a)), x1, np.sign(f(x1)),
                   b, np.sign(f(b)), erro))

        if (erro != -1) & (erro < tol) | (f(x1) == 0):
            break

        if f(x1) * f(a) < 0:
            b = x1
            nb = 0
            na += 1
            if na > 1:
                fa /= 2
        else:
            a = x1
            na = 0
            nb += 1
            if nb > 1:
                fb /= 2
    if prt:
        n_dec = int(np.ceil(np.abs(np.log10(erro))) + 1)
        form = "{:." + str(n_dec) + "f}"
        x1_str = form.format(x1)
        print(x1_str)

    return x1


def func(x): return x ** 2 - 8 * x + 6


x2 = np.linspace(-2, 10, 500)
y = func(x2)
plt.plot(x2, y)
plt.grid()
plt.show()

r1 = bissecao_abs(func, 0, 1, 1e-1, True)
r2 = falsa_posicao(func, 0, 1, 1e-1, True)
print(r1, r2)
