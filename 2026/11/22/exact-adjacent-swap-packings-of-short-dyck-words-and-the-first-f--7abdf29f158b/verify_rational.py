"""Exact-arithmetic validation of the Dyck one-swap packing certificates.
Run: python verify_rational.py
Requires Python standard library only; data file certificates.json beside this script.
"""
from pathlib import Path
import itertools
import json
from fractions import Fraction

DATA=json.loads(Path(__file__).with_name('certificates.json').read_text(encoding='utf-8'))

def dyck(m):
    ans=[]
    for chars in itertools.product('01',repeat=2*m):
        word=''.join(chars)
        if word.count('0')!=m:continue
        balance=0
        good=True
        for c in word:
            balance+=1 if c=='0' else -1
            if balance<0:
                good=False;break
        if good:ans.append(word)
    return ans

def outputs(word):
    s={word}
    for pos in range(len(word)-1):
        if word[pos]!=word[pos+1]:
            swapped=list(word)
            swapped[pos],swapped[pos+1]=swapped[pos+1],swapped[pos]
            s.add(''.join(swapped))
    return s

for m in range(1,6):
    d=DATA['instances'][str(m)]
    words=dyck(m)
    shadow={w:outputs(w) for w in words}
    all_out=set().union(*shadow.values())
    x={w:Fraction(v) for w,v in d['primal'].items()}
    y={z:Fraction(v) for z,v in d['dual'].items()}
    assert len(words)==d['source_count']
    assert len(all_out)==d['output_count']
    assert set(x)<=set(words) and set(y)<=all_out
    assert all(v>=0 for v in x.values()) and all(v>=0 for v in y.values())
    # Each possible output is covered by at most one unit of primal weight.
    for z in all_out:
        assert sum((x.get(w,0) for w in words if z in shadow[w]),Fraction(0))<=1
    # Every source has a dual coverage of at least one.
    for w in words:
        assert sum((y.get(z,0) for z in shadow[w]),Fraction(0))>=1
    primal=sum(x.values(),Fraction(0));dual=sum(y.values(),Fraction(0))
    assert primal==dual==Fraction(d['fractional_optimum'])
    witness=d['integer_witness']
    assert len(set(witness))==len(witness)==d['integer_optimum']
    assert set(witness)<=set(words)
    for a,b in itertools.combinations(witness,2):
        assert shadow[a].isdisjoint(shadow[b])
    assert len(witness)==primal.numerator//primal.denominator
    print('m=',m,'Dyck=',len(words),'outputs=',len(all_out),
          'maximum code=',len(witness),'fractional=',primal)

for code in DATA['length_ten_maximum_codebooks']:
    assert len(code)==len(set(code))==9
    for a,b in itertools.combinations(code,2):assert outputs(a).isdisjoint(outputs(b))
print('All rational certificates and 11 listed codebooks passed.')
