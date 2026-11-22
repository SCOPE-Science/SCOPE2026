"""Independent reference-first verification via deletion-output bit sets.
Run: python verify_reference.py
"""
from itertools import product,combinations
from collections import Counter

alphabet='012'

def capacity(ref):
    triples=sorted({''.join(ref[i] for i in inds) for inds in combinations(range(len(ref)),3)})
    masks=[]
    for word in triples:
        shadow={word[:j]+word[j+1:] for j in range(3)}
        masks.append(sum(1 << (3*int(x[0])+int(x[1])) for x in shadow))
    memo={}
    def solve(i,used):
        if i==len(triples): return (0,0)
        state=(i,used)
        if state in memo:return memo[state]
        a,na=solve(i+1,used)
        b=-1;nb=0
        if not (used&masks[i]):
            b,nb=solve(i+1,used|masks[i]);b+=1
        if b>a:ans=b,nb|(1<<i)
        else:ans=a,na
        memo[state]=ans
        return ans
    k,which=solve(0,0)
    return k,tuple(triples[i] for i in range(len(triples)) if which>>i&1)

expected={
  3:{1:27},4:{1:81},5:{1:33,2:210},
  6:{1:39,2:336,3:342,4:12},
  7:{1:45,2:570,3:1074,4:498},
  8:{1:51,2:1002,3:2490,4:3018},
  9:{1:57,2:1824,3:5292,4:11214,5:1296}}
for t in range(3,10):
    hist=Counter()
    opt=[]
    for p in product(alphabet,repeat=t):
        k,code=capacity(p);hist[k]+=1
        if t==6 and k==4:
            opt.append((''.join(p),code))
            assert set().union(*({w[:i]+w[i+1:] for i in range(3)} for w in code))==set(a+b for a in alphabet for b in alphabet)
    assert dict(hist)==expected[t],(t,hist)
    if t==6:
        assert len(opt)==12
        print('length_6_optimizers',len(opt),'representative_code',opt[0])
    print('t',t,'verified_distribution',dict(sorted(hist.items())))
print('RESULT: independent direct reference graph computation PASS')
