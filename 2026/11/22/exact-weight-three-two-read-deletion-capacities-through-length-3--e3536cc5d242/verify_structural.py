"""Independent overlap-graph check for the finite weight-three reconstruction claim.
The direct-deck test below independently checks the generated local-move graph at small n.
"""
from itertools import combinations
from pathlib import Path
import json

cert=json.loads(Path(__file__).with_name('certificates.json').read_text(encoding='utf8'))['lengths']

def words(n):return list(combinations(range(n),3))
def desc(p,n):return {tuple((v if v<i else v-1) for v in p if v!=i) for i in range(n)}
def moved(a,b):
    # First-to-last differing positions must form a strictly alternating binary block.
    x={i for i in a};y={i for i in b}
    dif=sorted(x^y)
    if not dif:return False
    lo,hi=dif[0],dif[-1]
    return (hi-lo+1)%2==0 and all((i in x)!=(i in y) for i in range(lo,hi+1)) and all(((i in x)!=(i+1 in x)) for i in range(lo,hi))
for n in range(3,13):
    W=words(n); D=[desc(w,n) for w in W]
    for i,j in combinations(range(len(W)),2):
        assert (len(D[i]&D[j])>=2)==moved(W[i],W[j]),(n,i,j)
    print('direct deck/alternating local-move agreement:',n)
# Different implementation of the proof checker, using set equality rather than bit-encoded reads.
for n in [13,16,20,24,28,32]:
    W=words(n);p=cert[str(n)]; c=set(p['independent_indices'])
    assert len(c)==p['alpha']
    for i in c:
        # Every alternating-interval toggle must leave the selected code.
        a=set(W[i]);
        for lo in range(n):
            for hi in range(lo+1,n,2):
                if hi-lo+1<2:continue
                if all((j in a)!=(j+1 in a) for j in range(lo,hi)):
                    b=frozenset(a.symmetric_difference(range(lo,hi+1)))
                    if len(b)==3:
                        assert tuple(sorted(b)) not in {W[j] for j in c if j!=i},(n,i)
    print('independent alternating-toggle check:',n)
print('PASS')
