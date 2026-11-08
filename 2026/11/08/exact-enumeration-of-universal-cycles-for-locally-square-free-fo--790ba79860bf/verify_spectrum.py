"""Exact spectrum, arborescence, and universal-cycle count checks.

Requires Python 3 and SymPy; no floating-point arithmetic.
"""
import itertools
from math import factorial, comb
import sympy as sp


def squarefree4(word):
    a,b,c,d=word
    return a!=b and b!=c and c!=d and (a,b)!=(c,d)


def laplacian(q):
    vertices=[w for w in itertools.product(range(q),repeat=3)
              if w[0]!=w[1] and w[1]!=w[2]]
    pos={w:i for i,w in enumerate(vertices)}
    mat=sp.zeros(len(vertices))
    for w in vertices:
        i=pos[w]
        for d in range(q):
            word=w+(d,)
            if squarefree4(word):
                j=pos[word[1:]]
                mat[i,i]+=1
                mat[i,j]-=1
    return mat


def tree_formula(q):
    a=q*(q*q-3*q+1)
    b=(q-1)*(q-2)//2
    return (q**(q-2)*(q-1)**(a-2)*(q-2)**(2*(q-1))
            *((q-2)**2+1)**b)


def tour_formula(q):
    return (tree_formula(q)*factorial(q-3)**(q*(q-1))
            *factorial(q-2)**(q*(q-1)*(q-2)))


def predicted_characteristic(q,x):
    a=q*(q*q-3*q+1)
    b=(q-1)*(q-2)//2
    quadratic=x*x-(2*q-4)*x+(q-2)**2+1
    cubic=x**3-(3*q-4)*x*x+(3*q*q-8*q+5)*x-q*(q-2)**2
    return sp.Poly(x*(x-(q-1))**a*quadratic**b*cubic**(q-1),x)


def main():
    x=sp.Symbol('x')
    for q in range(3,7):
        L=laplacian(q)
        assert L.rows == q*(q-1)**2
        assert L.charpoly(x)==predicted_characteristic(q,x)
        tree=int(L[1:,1:].det(method='domain-ge'))
        assert tree==tree_formula(q), (q,tree,tree_formula(q))
        assert tour_formula(q)>0
        print('q=',q,'vertices=',L.rows,'rooted_arborescences=',tree,
              'cycles=',tour_formula(q),flush=True)
    print('SPECTRUM_VERIFY_OK')

if __name__=='__main__':main()
