import numpy as np
def B3f(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; beta=6/11
# Bessel upper bound: B <= b^{-1} sum_k sup G_k <= b^{-1} sum_k sup sum_n g g
xs=np.linspace(-3,3,60001)
BV=B3f(xs)
def sup_Gk(k):
    tot=np.zeros_like(xs)
    for n in range(-10,11):
        tot+=np.interp(xs-n*a,xs,BV)*np.interp(xs-n*a-k*beta,xs,BV)
    return tot.max()
S=0.0
for k in range(-7,8):
    s=sup_Gk(k); S+=s; print(k,f"{s:.6f}")
print("sum sup=",S,"B <=",S/b)
# G0 max
print("G0 max=",sup_Gk(0))
