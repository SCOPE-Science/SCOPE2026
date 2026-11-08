"""Finite base cases and boundary-lift checks for factor-completion theorem.

The mathematical induction for every n >= 4 is in RESULT.md; this
program verifies exact finite bases, not an unbounded search.
Standard library only; one-based word positions are used throughout.
"""
from itertools import product

B = ['','101']
for i in range(1,13):
    B.append(B[i]+B[i][i:])
for i in range(1,14):
    assert len(B[i]) == (1 << (i-1)) + i+1
    assert B[i].endswith('01')
w = B[13]
assert len(w)==4110

def allowed(n):
    return {''.join(t) for t in product('01',repeat=n)
            if '00' not in ''.join(t)}

def first(word):
    at=w.find(word)
    return at+1 if at>=0 else None

def f(p):
    return (1<<(p-2))+p

r={1:1,2:5,3:13,4:2061}
assert all(first('1'*n)==r[n] for n in (1,2,3,4))
assert f(r[2]) == r[3] and f(r[3]) == r[4]
assert f(r[4])==(1<<2059)+2061

# Explicit small safe bases: for each n-word, a start at least n+2
# but at most r_n. At n=4, every word except 1111 is already safe
# by r_3 = 13.
safe3 = {'010':7,'011':9,'101':6,'110':5,'111':13}
safe4 = {'0101':7,'0110':9,'0111':12,'1010':6,
         '1011':8,'1101':10,'1110':13,'1111':2061}
for n,safe in ((3,safe3),(4,safe4)):
    assert set(safe)==allowed(n)
    assert all(n+2 <= p <= r[n] and w[p-1:p-1+n] == v
               for v,p in safe.items())
assert all(p <= r[3] for v,p in safe4.items() if v!='1111')

# Check the boundary prefixing identity directly for every modest
# stage, separately from any first-occurrence or factor census.
for p in range(2,13):
    old=B[p-1]
    new=B[p]
    assert new[len(old)-2:len(old)+min(18,len(old)-p+1)] == (
        '01'+old[p-1:p-1+min(18,len(old)-p+1)])

# Compute the explicit induction witnesses at length 5 from the
# safe length-4 and length-3 witnesses; all nonconstant witnesses
# are less than or equal to r_4. The fifth all-one factor would
# occur only at the far larger symbolic r_5.
safe5={}
for v,p in safe4.items():
    safe5['1'+v] = f(p)
for v,p in safe3.items():
    safe5['01'+v] = f(p)-1
assert set(safe5)==allowed(5)
for word,p in safe5.items():
    assert p>=7
    if word=='11111':
        assert p == (1<<2059)+2061
    else:
        assert p<=r[4]
        assert w[p-1:p+4]==word
assert all(first(t) is not None for t in allowed(5) if t!='11111')
assert first('11111') is None

# The exact finite completion/penultimate-onset calculations.
for n in (2,3,4):
    firsts={t:first(t) for t in allowed(n)}
    assert all(v is not None for v in firsts.values())
    assert max(firsts.values())==r[n]
    assert [t for t,p in firsts.items() if p==r[n]]==['1'*n]
    assert max(firsts[t] for t in allowed(n) if t!='1'*n) == (2 if n==2 else r[n-1])
    assert max(firsts.values())+n-1 == {2:6,3:15,4:2064}[n]
print('BRIK_COMPLETION_VERIFY_OK base_3_4 lifted_5 2064')
