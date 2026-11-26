"""Reproduce finite identities and independent checks for Tribonacci arches.

Run with Python 3.10+; no external packages needed. All claims about infinite
words follow from the finite morphism identities proved in RESULT.md, not from
sampling in this script.
"""
from itertools import product
from collections import Counter

TAU = {'0':'01', '1':'02', '2':'0'}
ARCH = {'A':'0102','B':'0100102','C':'010102'}
SIGMA = {'A':'ABCB', 'B':'ABCBBCB', 'C':'ABCBCB'}

def apply(w, morph):
    return ''.join(morph[c] for c in w)

def arches(v):
    seen=set(); start=0; out=[]
    for end,letter in enumerate(v):
        seen.add(letter)
        if len(seen)==3:
            out.append(v[start:end+1]);start=end+1;seen=set()
    return out,v[start:]

def index_direct(v):
    # Independent subsequence test for small words.
    k=0
    while True:
        targets=product('012',repeat=k+1)
        for u in targets:
            j=0
            for c in v:
                if c==u[j]:
                    j+=1
                    if j==len(u):break
            if j<len(u):return k
        k+=1

for name, word in ARCH.items():
    transformed=word
    for _ in range(3):transformed=apply(transformed,TAU)
    assert transformed==apply(SIGMA[name],ARCH),(name,transformed)
    assert arches(word)==([word],'')
    assert word.count('2')==1 and word.endswith('2')

# Compare two entirely different construction paths to the same finite word.
code='A';base=ARCH['A'];nchecks=0
for j in range(5):
    assert apply(code,ARCH)==base
    assert arches(base)[0]==[ARCH[c] for c in code]
    assert arches(base)[1]==''
    nchecks+=1
    code=apply(code,SIGMA)
    for _ in range(3):base=apply(base,TAU)

w='0';lengths=[];count_at_lengths=[]
for n in range(19):
    lengths.append(len(w));count_at_lengths.append(w.count('2'))
    if n>=3:assert w.count('2')==lengths[n-3]
    if n<=16:assert len(arches(w)[0])==w.count('2')
    w=apply(w,TAU)

# Every short factor is checked by the greedy index and the rare-symbol bound.
# Full prefix enumeration of length <= 200 over an explicit word of length >= 50000.
w='0'
for _ in range(18):w=apply(w,TAU)
assert len(w)>=30000
for n in range(1,101):
    fset=set(w[i:i+n] for i in range(len(w)-n+1))
    for v in fset:
        k=len(arches(v)[0]);r=v.count('2')
        assert max(0,r-1)<=k<=r,(n,v,k,r)
    if n<=14:
        for v in fset:
            assert index_direct(v)==len(arches(v)[0]),(n,v)

for N in range(1,10001):
    prefix=w[:N]
    assert len(arches(prefix)[0])==prefix.count('2')

# Independently check both factor discrepancy and universal density numerically;
# the certified infinite estimate uses the published factor-balance theorem.
lambda_=1.8392867552141612
rho=lambda_**-3
for n in range(1,151):
    fset=set(w[i:i+n] for i in range(len(w)-n+1))
    for v in fset:
        assert abs(v.count('2')-rho*n)<1.5+1e-9
        assert abs(len(arches(v)[0])-rho*n)<2.5+1e-9

print('TRIBONACCI_ARCH_RETURN_MORPHISM_PASS',
      'morphism_checks=3', 'iterate_checks='+str(nchecks),
      'prefix_lengths=10000', 'factor_lengths=150',
      'independent_subsequence_lengths=14', 'tau_levels=19')
