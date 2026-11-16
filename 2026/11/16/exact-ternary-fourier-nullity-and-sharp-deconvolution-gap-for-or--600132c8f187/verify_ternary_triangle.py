"""Independent monotone-triangle enumeration and Eisenstein-integer DFT.
No external packages: run `python3 verify_ternary_triangle.py`.
"""
from itertools import product
from collections import Counter

def matrices_from_triangles(n=4):
    result=[]
    def explore(bottom, levels):
        if len(bottom)==1:
            sets=[set(t) for t in levels[::-1]]
            old=set();rows=[]
            for s in sets:
                rows.append(tuple(int(j in s)-int(j in old) for j in range(n)))
                old=s
            result.append(tuple(rows));return
        for upper in product(*(range(bottom[i],bottom[i+1]+1) for i in range(len(bottom)-1))):
            if all(upper[i]<upper[i+1] for i in range(len(upper)-1)):
                explore(upper,levels+[upper])
    bottom=tuple(range(n));explore(bottom,[bottom])
    return result

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mult_omega(x):return (-x[1],x[0]-x[1])
def mult_omega2(x):return (x[1]-x[0],-x[0])
def squared_norm(z):return z[0]*z[0]-z[0]*z[1]+z[1]*z[1]

def spectrum():
    mats=matrices_from_triangles()
    assert len(mats)==42 and len(set(mats))==42
    size=3**9
    F=[(0,0) for _ in range(size)]
    for A in mats:
        assert all(sum(A[i])==1 for i in range(4))
        assert all(sum(A[i][j] for i in range(4))==1 for j in range(4))
        loc=sum((A[i][j]%3)*3**(3*i+j) for i in range(3) for j in range(3))
        assert F[loc]==(0,0)
        F[loc]=(1,0)
    # A separable DFT in exact Z[omega], omega^2+omega+1=0.
    scale=1
    for coordinate in range(9):
        for block in range(0,size,3*scale):
            for offset in range(scale):
                i=block+offset
                a,b,c=F[i],F[i+scale],F[i+2*scale]
                F[i]=add(add(a,b),c)
                F[i+scale]=add(add(a,mult_omega(b)),mult_omega2(c))
                F[i+2*scale]=add(add(a,mult_omega2(b)),mult_omega(c))
        scale*=3
    H=Counter(squared_norm(x) for x in F)
    assert H[0]==734 and H[3]==3504 and H[1764]==1
    assert len(H)==53 and sum(H.values())==19683
    assert sum(k*v for k,v in H.items())==42*19683
    assert min(x for x in H if x)>0 and min(x for x in H if x)==3
    print('PASS monotone-triangle bijection; 9-axis exact Eisenstein DFT; all 53 squared-magnitude levels')
    print('zero=',H[0],'least positive squared magnitude=',min(k for k in H if k>0),'sum norm squared=',sum(k*v for k,v in H.items()))
    return H

if __name__=='__main__':spectrum()
