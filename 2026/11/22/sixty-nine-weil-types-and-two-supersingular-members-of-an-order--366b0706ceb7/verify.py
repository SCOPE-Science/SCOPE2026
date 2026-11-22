"""Exact finite-field certificate for a characteristic-eleven C6 genus-four family.

Usage: python verify.py   (requires numpy)
The input WEIL_TABLE.csv must be in the same directory.
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np

P = 11
# coefficients low-to-high of two different irreducible monic degree-n polynomials
MODULI = {
    'A': {1: (1,), 2: (1,0), 3: (1,0,4), 4: (1,0,0,4)},
    'B': {1: (1,), 2: (1,1), 3: (1,5,0), 4: (1,5,0,0)},
}

def finite_field(n, coefficients):
    q = P**n
    digits = np.array([[(k // P**i) % P for i in range(n)] for k in range(q)], dtype=np.int64)
    powers = P**np.arange(n,dtype=np.int64)
    def add(x, y):
        return np.sum(((digits[x] + digits[y]) % P)*powers, axis=-1)
    def multiply(x,y):
        ax=digits[x]; by=digits[y]
        shape=np.broadcast_shapes(ax.shape[:-1],by.shape[:-1]);
        ax=np.broadcast_to(ax,shape+(n,));by=np.broadcast_to(by,shape+(n,))
        tmp=np.zeros(shape+(2*n-1,),dtype=np.int64)
        for i in range(n):
            for j in range(n):
                tmp[...,i+j] += ax[...,i]*by[...,j]
        for k in range(2*n-2,n-1,-1):
            z=tmp[...,k].copy()
            for j in range(n):
                tmp[...,k-n+j] -= z*coefficients[j]
        return np.sum((tmp[...,:n]%P)*powers,axis=-1)
    def scalar(x,k):
        return np.sum(((digits[x]*(k%P))%P)*powers,axis=-1)
    # This exhaustive multiplicative check also certifies irreducibility of the
    # polynomial, since every nonzero element of the quotient is a unit.
    domain = np.arange(q,dtype=np.int64)
    unit_check = np.ones(q,dtype=np.int64)
    base=domain.copy(); exponent=q-1
    while exponent:
        if exponent&1:unit_check=multiply(unit_check,base)
        base=multiply(base,base);exponent//=2
    assert np.all(unit_check[1:]==1), ('not a field',n,coefficients)
    squares=np.zeros(q,dtype=np.bool_)
    squares[multiply(domain,domain)]=True
    sq= multiply(domain,domain)
    x4=multiply(sq,sq)
    x7=multiply(multiply(x4,sq),domain)
    x10=multiply(multiply(x4,x4),sq)
    common=add(x10,x7)
    def points(a,b):
        v=add(add(common,scalar(x4,a)),scalar(domain,b))
        chi=np.where(v==0,0,np.where(squares[v],1,-1))
        # Degree ten monic even hyperelliptic model: two rational infinities.
        return q+2+int(chi.sum())
    return points

def discriminant(a,b):
    return (-4*a**3+a*a+18*a*b-27*b*b-4*b)%P

def polynomial(counts):
    # Newton identities; reciprocal genus-four functional equation.
    sums=[P**(j+1)+1-counts[j] for j in range(4)]
    e=[1]
    for k in range(1,5):
        t=sum((-1)**(i-1)*e[k-i]*sums[i-1] for i in range(1,k+1))
        assert t%k==0
        e.append(t//k)
    coeff=[(-1)**j*e[j] for j in range(5)]
    return tuple(coeff+[P**(j-4)*coeff[8-j] for j in range(5,9)])

def cartier_matrix(a,b):
    # f^5=x^5 (u^3+u^2+a*u+b)^5, where u=x^3.
    v=[b%P,a%P,1,1]
    power=[1]
    for _ in range(5):
        new=[0]*(len(power)+3)
        for i,old in enumerate(power):
            for j,c in enumerate(v):new[i+j]=(new[i+j]+old*c)%P
        power=new
    def coefficient(index):
        return power[(index-5)//3] if index>=5 and (index-5)%3==0 and (index-5)//3<len(power) else 0
    return [[coefficient(11*i-j) for j in range(1,5)] for i in range(1,5)]

def rank(matrix):
    mat=[r[:] for r in matrix];m=len(mat);n=len(mat[0]);p=0
    for c in range(n):
        piv=next((i for i in range(p,m) if mat[i][c]),None)
        if piv is None:continue
        mat[p],mat[piv]=mat[piv],mat[p]
        inv=pow(mat[p][c],-1,P)
        mat[p]=[(t*inv)%P for t in mat[p]]
        for i in range(m):
            if i==p:continue
            mult=mat[i][c]
            mat[i]=[(mat[i][j]-mult*mat[p][j])%P for j in range(n)]
        p+=1
    return p

def main():
    file=Path(__file__).with_name('WEIL_TABLE.csv')
    with open(file,encoding='utf-8',newline='') as stream:
        rows=list(csv.DictReader(stream))
    assert len(rows)==101
    data={}
    for row in rows:
        a,b=int(row['a']),int(row['b'])
        assert 0<=a<11 and 0<b<11 and discriminant(a,b)!=0
        assert (a,b) not in data
        ncounts=tuple(int(row[f'N{i}']) for i in range(1,5))
        pol=polynomial(ncounts)
        assert pol[:5]==(1,)+tuple(int(row[f'L{i}']) for i in range(1,5))
        p_rank=max(i for i,v in enumerate(pol) if v%11)
        assert p_rank==int(row['p_rank'])
        data[a,b]=(ncounts,pol,p_rank)
    expected={(a,b) for a in range(11) for b in range(1,11) if discriminant(a,b)}
    assert set(data)==expected
    for label,moduli in MODULI.items():
        for n in range(1,5):
            count=finite_field(n,moduli[n])
            for (a,b),(ns,_,_) in data.items():
                assert count(a,b)==ns[n-1],(label,n,a,b)
    classes=defaultdict(list)
    for pair,(_,pol,_) in data.items():classes[pol].append(pair)
    assert len(classes)==69
    distribution=Counter(p for _,_,p in data.values())
    assert distribution=={0:2,1:5,2:15,3:79}
    zero={key for key,(_,_,p) in data.items() if p==0}
    assert zero=={(3,7),(8,3)}
    target=(1,0,11,0,0,0,1331,0,14641)
    assert all(data[pair][1]==target for pair in zero)
    assert rank(cartier_matrix(3,7))==rank(cartier_matrix(8,3))==2
    assert len(classes[target])==2
    assert Counter(len(v) for v in classes.values())=={1:49,2:13,3:5,5:1,6:1}
    print('C6_F11_WEIL_69_TYPES_101_CURVES_VERIFIED')

if __name__=='__main__':main()
