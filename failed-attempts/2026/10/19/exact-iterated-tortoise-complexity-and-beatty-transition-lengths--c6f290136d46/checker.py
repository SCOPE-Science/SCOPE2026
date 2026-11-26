"""Finite regression checks for the k-fold tortoise transform on Sturmian factors.
Scientific reference: Campbell and Rampersad, arXiv:2604.25811.
Python >=3.9, standard library only: python checker.py.
"""
from decimal import Decimal, getcontext
from itertools import product
getcontext().prec = 70
D=Decimal

def T(word):
    p=word.find('1')
    return word if p<0 else word[:p]+word[p+1:]+'1'

def power(word,k):
    for _ in range(k):word=T(word)
    return word

# Every arbitrary binary word, not just a Sturmian word: exact prefix identity.
n_word_tests=0;n_prefix_tests=0
for n in range(1,12):
    for b in product('01',repeat=n):
        w=''.join(b)
        for k in range(2,n+3):
            x=power(w,k)
            assert len(x)==n and x.count('1')==w.count('1')
            for m in range(n+1):
                if m<=n-k:
                    expected=max(w[:m+k].count('1')-k,0)
                else:
                    expected=max(w.count('1')+m-n,0)
                assert x[:m].count('1')==expected,(w,k,m,x,expected)
                n_prefix_tests+=1
            n_word_tests+=1
print('arbitrary-word prefix identities:',n_word_tests,'(word,k) cases and',n_prefix_tests,'prefix comparisons')

slopes={
'sqrt2_minus_1':D(2).sqrt()-1,
'phi_complement':(D(3)-D(5).sqrt())/2,
'sqrt5_minus_2':D(5).sqrt()-2,
'sqrt3_minus_1':D(3).sqrt()-1,
'one_over_sqrt2':1/D(2).sqrt(),
'sqrt7_minus_2':D(7).sqrt()-2,
'sqrt10_minus_3':D(10).sqrt()-3,
}

def mech_word(alpha,phase,n):
    s=[];v=phase
    for i in range(n):
        v2=v+alpha
        bit=int(v2)-int(v)
        assert bit in (0,1)
        s.append(str(bit));v=v2
    return ''.join(s)

def all_factors(alpha,n):
    cuts=[D(0),D(1)]+[1-(D(j)*alpha)%1 for j in range(1,n+1)]
    cuts.sort()
    assert len(cuts)==len(set(cuts)),(alpha,n)
    return {mech_word(alpha,(a+b)/2,n) for a,b in zip(cuts,cuts[1:])}

n_cases=0
for name,alpha in slopes.items():
    assert 0<alpha<1
    for n in range(1,69):
        factors=all_factors(alpha,n)
        assert len(factors)==n+1,(name,n,len(factors))
        for k in list(range(2,min(n+4,12)))+[n+4]:
            actual=len({power(w,k) for w in factors})
            expected=max(2,n+1-int(D(k)/alpha))
            assert actual==expected,(name,n,k,actual,expected)
            n_cases+=1
    print(name,'lengths 1..68, powers from 2 to 11 and n+4: checked')
print('Sturmian factor image counts:',n_cases,'(slope,length,k) cases')
print('ALL CHECKS PASS')
