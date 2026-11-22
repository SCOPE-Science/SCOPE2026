"""Direct occurrence-based verification of full five-run minimal-unique-factor classification."""
from collections import Counter,defaultdict
from itertools import product

def predicted(a,b,c,d,e):
    A=max(a,c,e)
    z={'0'*A} if [a,c,e].count(A)==1 else set()
    B=max(b,d)
    if b!=d:z.add('1'*B)
    p=min(a,c)+1
    if a!=c and not(A==p and [a,c,e].count(A)==1): z.add('0'*p+'1')
    p=min(c,e)+1
    if c!=e and not(A==p and [a,c,e].count(A)==1): z.add('1'+'0'*p)
    m=min(b,d)
    if abs(b-d)>=2:z|={'0'+'1'*(m+1),'1'*(m+1)+'0'}
    if b!=d:z.add('0'+'1'*m+'0')
    if c<=min(a,e):z.add('1'+'0'*c+'1')
    return z

def direct(s):
    counts=Counter(s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1))
    return {v for v,c in counts.items() if c==1 and (len(v)==1 or (counts[v[:-1]]>=2 and counts[v[1:]]>=2))}

hist=Counter();n=0
for a,b,c,d,e in product(range(1,7),repeat=5):
    s='0'*a+'1'*b+'0'*c+'1'*d+'0'*e
    got=direct(s);expected=predicted(a,b,c,d,e)
    assert got==expected,(a,b,c,d,e,got^expected,got,expected)
    hist[len(got)]+=1;n+=1
print('all_positive_five_run_parameter_tuples',n)
print('mus_count_histogram',dict(sorted(hist.items())))
print('status PASS')
