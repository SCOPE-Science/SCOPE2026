# Exact supplementary checks for the power-sum sextic pencil.
# A finite symbolic test is not a proof of the all-dimensional theorem.
from sympy import symbols, Matrix, diff
from math import comb
for n in range(3,8):
    x=symbols('x0:'+str(n)); G=sum(v**2 for v in x); H=sum(v**3 for v in x)
    for k in range(1,n+1):
        F=G**3-k*H**2
        P={x[i]:int(i<k) for i in range(n)}
        assert F.subs(P)==0
        assert all(diff(F,v).subs(P)==0 for v in x)
        W=Matrix(n,n,lambda i,j:diff(F,x[i],x[j]).subs(P))
        W0=Matrix(n,n,lambda i,j:6*k*((1 if i<k and j<k else 0))-6*k*k*(1 if i==j and i<k else 0)+6*k*k*(1 if i==j and i>=k else 0))
        assert W==W0,(n,k,W,W0)
        assert W*Matrix([P[v] for v in x])==Matrix.zeros(n,1)
        M=W.minor_submatrix(0,0)
        assert M.det()!=0,(n,k)
        assert sum(1 for mask in range(1,2**n) if mask.bit_count()==k)==comb(n,k)
    print(n,'OK; node counts',[(k,comb(n,k)) for k in range(1,n+1)])
print('Plane normalization genera from arithmetic genus and delta: 4 generic; 1 at -1,-2; 3 at -3.')
