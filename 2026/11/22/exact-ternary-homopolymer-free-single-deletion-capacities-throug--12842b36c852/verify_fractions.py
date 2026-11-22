"""Pure-Python exact checker for deletion-shadow fractional primal/dual certificates.
Usage: python3 verify_fractions.py
"""
import itertools,json,pathlib
from fractions import Fraction
HERE=pathlib.Path(__file__).resolve().parent

def words(n):
 return [''.join(t) for t in itertools.product('012',repeat=n)
         if all(t[i]!=t[i+1] for i in range(n-1))]

def desc(s):
 return {s[:i]+s[i+1:] for i in range(len(s))}

cert=json.loads((HERE/'fractional_certificate.json').read_text())
expected={2:Fraction(3,2),3:Fraction(3),4:Fraction(9,2),5:Fraction(42,5),6:Fraction(27,2),7:Fraction(99,4)}
for n,opt in expected.items():
 rec=cert[str(n)];W=words(n);D={w:desc(w) for w in W}
 R=set().union(*D.values())
 px={w:Fraction(*f) for w,f in rec['primal_weights'].items()}
 dy={y:Fraction(*f) for y,f in rec['dual_weights'].items()}
 assert set(px)<=set(W) and set(dy)<=R
 assert all(0<f<=1 for f in px.values()) and all(f>=0 for f in dy.values())
 assert all(sum(px.get(w,0) for w in W if y in D[w])<=1 for y in R)
 assert all(sum(dy.get(y,0) for y in D[w])>=1 for w in W)
 assert sum(px.values())==sum(dy.values())==opt
 assert Fraction(rec['fractional_optimum'])==opt
 print('EXACT_LP',n,opt)

codes=json.loads((HERE/'optimal_codebooks.json').read_text())
expected_integer={2:1,3:3,4:4,5:8,6:12,7:22}
for n,alpha in expected_integer.items():
 code=codes[str(n)];assert len(code)==len(set(code))==alpha
 assert set(code)<=set(words(n))
 seen=set()
 for w in code:
  assert not(seen&desc(w))
  seen|=desc(w)
 print('WITNESS',n,alpha)
print('FRACTION_AND_WITNESSES_OK')
