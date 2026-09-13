import numpy as np, sys, time
sys.path.insert(0,'output/artifacts')
from fastdelta import Delta_grid
t0=time.time()
scales=[0.05,0.04,0.03,0.02,0.015,0.01]
menu=[(s1*h1,s2*h2) for h1 in scales for h2 in scales for s1 in (1,-1) for s2 in (1,-1)]
print("menu size",len(menu))
for pt in [np.array([[0.6325,0.115]]), np.array([[0.8225,0.6125]]), np.array([[0.8133131,0.82538592]])]:
    for N in [12,16,20,24]:
        best=min(abs(Delta_grid(pt,a,b,N=N)[0])/abs(a*b) for (a,b) in menu)
        print("pt",pt[0],"N",N,"menu-max-ratio min",best,"time",round(time.time()-t0,1))
