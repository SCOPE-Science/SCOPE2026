import numpy as np
def B3(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; beta=6/11
# G_k(x)=sum_n B3(x-n a)B3(x-n a-k beta); x in [0,a)
xs=np.linspace(0,a,2001,endpoint=False)
Ks=range(-7,8)
sups={}
for k in Ks:
    G=np.zeros_like(xs)
    for n in range(-10,11):
        G+=B3(xs-n*a)*B3(xs-n*a-k*beta)
    sups[k]=(G.min(),G.max(),G.mean())
    print(k, "min %.5f max %.5f mean %.5f"%(sups[k][0],sups[k][1],sups[k][2]))
s_ne0=sum(sups[k][1] for k in Ks if k!=0)
print("essinf G0 ~",sups[0][0]," sum_{kne0} sup =",s_ne0, " diag-dom?",sups[0][0]>s_ne0)
