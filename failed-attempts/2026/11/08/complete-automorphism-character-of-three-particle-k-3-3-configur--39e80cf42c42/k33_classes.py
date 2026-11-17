import contextlib,io
from k33_sym import *
import k33_sym
with contextlib.redirect_stdout(io.StringIO()):
    bas=[gauss_basis(cols) for cols in DD]
    chi=[]
    for gi,g in enumerate(AUT):
        tc=[chain_trace(gi,d) for d in range(4)]
        tb=[0]+[signed(trace_action_image(gi,i,*bas[i-1])) for i in (1,2,3)]+[0]
        chi.append(tuple(tc[i]-tb[i]-tb[i+1] for i in range(4)))
permindex={a[0]:i for i,a in enumerate(AUT)}
def mul(i,j):
    a=AUT[i][0];b=AUT[j][0]
    return permindex[tuple(a[b[v]] for v in V)]
def inv(i):
    x=AUT[i][0];y=[0]*6
    for j,v in enumerate(x):y[v]=j
    return permindex[tuple(y)]
unused=set(range(72)); classes=[]
while unused:
    i=min(unused)
    cl={mul(mul(g,i),inv(g)) for g in range(72)}
    assert cl<=unused
    unused-=cl
    classes.append((i,sorted(cl)))
print('classes:',len(classes))
for i,cl in classes:
  a=AUT[i]
  print('rep',i,'size',len(cl),'swap,p,q',a[2:], 'H1H2',chi[i][1:3]);assert len({chi[j] for j in cl})==1
print('sizes sum',sum(len(cl) for _,cl in classes),'H1 avg',sum(len(cl)*chi[i][1] for i,cl in classes),'H2 avg',sum(len(cl)*chi[i][2] for i,cl in classes))
