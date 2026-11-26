# Independent chain-level representation verification, including no reliance on Lefschetz computation.
from itertools import combinations
from sympy import SparseMatrix, Matrix,eye,ZZ
p=17; R={x*x%p for x in range(1,p)}
E=[c for c in combinations(range(p),2) if (c[1]-c[0])%p in R]
T=[t for t in combinations(range(p),3) if all((v-u)%p in R for u,v in combinations(t,2))]
ei={e:i for i,e in enumerate(E)};ti={t:i for i,t in enumerate(T)}
B=SparseMatrix(68,68,{(ei[(j,k)],n):1 for n,(i,j,k) in enumerate(T)}|{(ei[(i,k)],n):-1 for n,(i,j,k) in enumerate(T)}|{(ei[(i,j)],n):1 for n,(i,j,k) in enumerate(T)})
rref,pivots=B.rref();free=[j for j in range(68) if j not in pivots]
assert len(pivots)==52 and len(free)==16
K=Matrix.hstack(*B.nullspace());assert K.shape==(68,16)
assert K.extract(free,list(range(16)))==eye(16)

def sign(z):return -1 if sum(z[i]>z[j] for i in range(len(z)) for j in range(i+1,len(z)))%2 else 1

def act(a,b):
    A=Matrix.zeros(68,68)
    for j,t in enumerate(T):
        transformed=tuple((a*x+b)%p for x in t)
        A[ti[tuple(sorted(transformed))],j]=sign(transformed)
    H=(A*K).extract(free,list(range(16)))
    assert A*K==K*H
    return H

T1=act(1,1);U2=act(2,0)
assert T1**17==eye(16)
assert U2**8==eye(16)
assert U2*T1==T1**2*U2
assert T1.trace()==-1 and U2.trace()==0
cp1=T1.charpoly().as_expr(); cp2=U2.charpoly().as_expr()
from sympy import Symbol
x=Symbol('lambda')
assert cp1==sum(x**k for k in range(17))
assert cp2==(x**8-1)**2 or cp2.expand()==((x**8-1)**2).expand()
assert all(x.q==1 for x in K), "Cycle basis must be integral"
assert all(x.q==1 for x in T1), "Translation action must be integral"
z=eye(16).col(0)
O=Matrix.hstack(*(T1**j*z for j in range(16)))
assert O.det(method='domain-ge')==-1, "Orbit must be unimodular"
assert sum((T1**j for j in range(17)), Matrix.zeros(16,16))==Matrix.zeros(16,16), "Norm must vanish"
print('Integral cyclic orbit determinant -1 and norm zero verified')
print('C17 generator characteristic Phi_17 verified')
print('QR multiplier generator: 16x16 integral, characteristic (x^8-1)^2')
print('Conjugation relation checked, all kernel constraints checked')
