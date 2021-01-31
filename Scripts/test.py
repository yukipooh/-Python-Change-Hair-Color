def f(x):
    return x**4-2*x**3+x**2-2*x



for i in range(10):
    tmp = i - 3
    print(f"{tmp}:{f(tmp)}")
