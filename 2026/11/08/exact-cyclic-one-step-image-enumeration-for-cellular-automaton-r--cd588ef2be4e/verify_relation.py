"""Exact integer verification of the Rule 110 cyclic image enumerator.
No nonstandard packages. Boolean 4-by-4 matrices are packed row-major.
"""
from collections import deque

RULE = 110
Q = (1, -4, 6, -5, 1, 4, -4, 2, 0, -1)
P = (0, 1, -2, 3, -3, 3, -6, 6, -2, 1, 1)
IDENTITY = sum(1 << (5*i) for i in range(4))

def mul(u, v):
    result = 0
    for i in range(4):
        row = (u >> (4*i)) & 15
        for j in range(4):
            if any((row & (1<<k)) and (v & (1 << (4*k+j))) for k in range(4)):
                result |= 1 << (4*i+j)
    return result

def edge_masks():
    arr = [0, 0]
    for a in (0,1):
        for b in (0,1):
            for c in (0,1):
                local = (a<<2) | (b<<1) | c
                value = (RULE >> local) & 1
                arr[value] |= 1 << (4*(2*a+b) + (2*b+c))
    return tuple(arr)

def build():
    masks = edge_masks()
    elements = [IDENTITY]
    index = {IDENTITY:0}
    transitions = []
    for state in elements:
        nxt=[]
        for letter in masks:
            target=mul(state,letter)
            if target not in index:
                index[target]=len(elements)
                elements.append(target)
            nxt.append(index[target])
        transitions.append(tuple(nxt))
    return elements,transitions

def counts_to(limit):
    states,transitions=build()
    assert len(states)==75, len(states)
    v=[0]*len(states); v[0]=1
    counts=[0]   # formal constant coefficient, not a physical ring of size 0
    for n in range(1,limit+1):
        nxt=[0]*len(states)
        for idx,(a,b) in enumerate(transitions):
            if v[idx]:
                nxt[a]+=v[idx]
                nxt[b]+=v[idx]
        v=nxt
        counts.append(sum(v[i] for i,state in enumerate(states) if state & IDENTITY))
    return counts

def multiply_polynomials(u, v):
    out=[0]*(len(u)+len(v)-1)
    for i,a in enumerate(u):
        for j,b in enumerate(v):
            out[i+j]+=a*b
    return out

def polynomial_remainder(p, q):
    cur=list(p)
    while len(cur)>=len(q):
        c=cur[-1]  # q is monic
        for i in range(len(q)):
            cur[len(cur)-len(q)+i] -= c*q[i]
        while cur and cur[-1]==0: cur.pop()
    return cur

def main():
    factor_a=[1,-1]
    factor_b=[1,-1,0,0,-1]
    factor_c=[1,-2,1,-1,-1]
    assert multiply_polynomials(multiply_polynomials(factor_a,factor_b),factor_c)==list(Q)
    # E(z)=z^4+z^3-z^2+2z-1 is the dominant denominator factor.
    E=[-1,2,-1,1,1]
    p_plus_zqprime=[(P[i] if i<len(P) else 0)+(i*Q[i] if i<len(Q) else 0)
                    for i in range(max(len(P),len(Q)))]
    assert polynomial_remainder(p_plus_zqprime,E)==[]
    a=counts_to(100)
    assert a[1:19]==[1,2,5,10,22,41,79,154,302,582,1113,2125,4058,7737,14725,27994,53195,101048]
    residual=[sum(Q[j]*a[n-j] for j in range(len(Q)) if n-j>=0) - (P[n] if n < len(P) else 0) for n in range(1,86)]
    assert residual==[0]*85
    # For n>=11, 75 zero recurrence residuals certify the infinite
    # recurrence by Cayley-Hamilton for the 75-state integer transfer matrix.
    print('VERIFY_RELATION_OK states=75 first85=exact recurrence_n_ge_11=75 consecutive zero residues')
if __name__=='__main__':main()
