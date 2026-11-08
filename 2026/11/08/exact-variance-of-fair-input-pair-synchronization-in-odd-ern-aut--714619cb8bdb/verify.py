#!/usr/bin/env python3
"""Symbolic all-odd-size certificate and independent exact small-size recurrence check.
Requires Python 3 and SymPy. Run: python verify.py
"""
import sympy as S
N, L, I = S.symbols('N L I', integer=True)
h = (N - 1)/2

def zero(x):
    assert S.cancel(S.together(x)) == 0, S.factor(x)

# Pair-automaton (i,l), 0<=i<n, 1<=l<=(n-1)/2.
# Rotating input sends (i,l)->((i+1)%n,l). The second input fixes
# all states except (0,1)->sink, (0,l)->(1,l-1) for l>=2,
# (n-l,l)->(n-l,l+1) for l<h, (h+1,h)->(1,h).
f=lambda l:2*l*(2*N**2-4*N+1)-l*(l-1)*(4*N-2)
g=lambda l: (4*(2*N-1)**2*l**4
               -8*(2*N-1)*(2*N**2-2*N-1)*l**3
               -2*(8*N**2-2*N-7)*l**2
               +4*(4*N**5-10*N**4+8*N**3+N**2-7*N+2)*l)/3
m0=lambda l:1+(f(l)+f(l-1))/2
ml=lambda l,i:f(l)-2*(i-1)
mr=lambda l,i:m0(l)+2*(N-i)
s0=lambda l:2*m0(l)-1+(g(l)+g(l-1))/2
sl=lambda l,i:g(l)-(i-1)*(4*f(l)-2)+4*(i-1)*(i-2)
sr=lambda l,i:s0(l)+(N-i)*(4*m0(l)-2)+4*(N-i)*(N-i+1)

# From the recurrences: M = 1 + (M_after_first+M_after_second)/2,
# S = (2*M-1) + (S_after_first+S_after_second)/2.
# The generic self-loop/rotation equations are enforced by the explicit
# quadratic-in-i formulas; these checks cover every exceptional seam.
zero(f(0));zero(g(0))
zero(ml(L,I)-(1+(ml(L,I)+ml(L,I+1))/2))
zero(sl(L,I)-(2*ml(L,I)-1+(sl(L,I)+sl(L,I+1))/2))
zero(mr(L,I)-(1+(mr(L,I)+mr(L,I+1))/2))
zero(sr(L,I)-(2*mr(L,I)-1+(sr(L,I)+sr(L,I+1))/2))
zero(m0(L)-(1+(f(L)+f(L-1))/2))
zero(s0(L)-(2*m0(L)-1+(g(L)+g(L-1))/2))
# rotation wraps at i=n-1 to i=0 (the right extension at i=n)
zero(mr(L,N)-m0(L));zero(sr(L,N)-s0(L))
# special transition to the next separation length for L<h
zero(ml(L,N-L)-(1+(mr(L+1,N-L)+mr(L,N-L+1))/2))
zero(sl(L,N-L)-(2*ml(L,N-L)-1+(sr(L+1,N-L)+sr(L,N-L+1))/2))
# special transition at maximal separation L=h
zero(ml(h,h+1)-(1+(f(h)+mr(h,h+2))/2))
zero(sl(h,h+1)-(2*ml(h,h+1)-1+(g(h)+sr(h,h+2))/2))
# Seam consistency at i=1 and cycle boundary i=n-l+1
zero(ml(L,1)-f(L));zero(sl(L,1)-g(L))

mean=(N-1)**2*(2*N+1)/2
variance=N*(N-1)*(4*N**4-8*N**3+3*N**2+7*N-14)/6
zero(f(h)-mean)
zero(g(h)-mean**2-variance)

# Independent first-step equations on the original unordered pairs.
# Direct rational linear algebra; no use of the above phase coordinates.
for n in (3,5,7,9):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    ix={p:j for j,p in enumerate(pairs)}
    K=len(pairs)
    A=S.eye(K)
    for j,(x,y) in enumerate(pairs):
        transitions=[tuple(sorted(((x+1)%n,(y+1)%n))),
                     tuple(sorted((0 if x==n-1 else x,
                                   0 if y==n-1 else y)))]
        for pair in transitions:
            if pair[0]!=pair[1]:A[j,ix[pair]]-=S.Rational(1,2)
    v=A.inv()*S.ones(K,1)
    w=A.inv()*(2*v-S.ones(K,1))
    k=ix[(0,(n-1)//2)]
    assert v[k] == mean.subs(N,n)
    assert w[k]-v[k]**2 == variance.subs(N,n)
    print('DIRECT',n,'mean',v[k],'variance',w[k]-v[k]**2)
print('SYMBOLIC_ALL_ODD_N_OK')
