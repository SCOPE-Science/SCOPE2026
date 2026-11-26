import math
from collections import Counter

def factor(alpha,x,n):
    return ''.join(str(math.floor(x+(i+1)*alpha)-math.floor(x+i*alpha)) for i in range(n))
def red(w):
    return w[:1]+''.join(w[i] for i in range(1,len(w)) if w[i]!=w[i-1])
def ab(w):
    return (len(w),w.count('1'))
def check(alpha,n):
    cuts=[0.0]+sorted(1-((j*alpha)%1) for j in range(1,n+1)) + [1.0]
    words=[factor(alpha,(cuts[i]+cuts[i+1])/2,n) for i in range(n+1)]
    if len(set(words)) != n+1: raise Exception('ordinary factor fail',alpha,n)
    counts=Counter(red(w) for w in words)
    abcounts=Counter(ab(red(w)) for w in words)
    expected=(2,3,4)[min(n,3)-1] if n<=3 else 4
    expected_ab=(2,2,3)[min(n,3)-1] if n<=3 else 3
    assert len(counts)==expected,(alpha,n,counts)
    assert len(abcounts)==expected_ab,(alpha,n,abcounts)
    if n>=3:
      t=[1-((j*alpha)%1) for j in (1,n-1,n)]
      ranks=sorted(next(i for i,c in enumerate(cuts[:-1]) if abs(c-u)<1e-10) for u in t)
      multiplicities=[ranks[0],ranks[1]-ranks[0],ranks[2]-ranks[1],n+1-ranks[2]]
      groups=[]
      for i in range(4):
          idx= (0 if i==0 else ranks[i-1])
          groups.append(red(words[idx]))
      assert len(set(groups))==4,(alpha,n,groups)
      assert sorted(counts.values())==sorted(multiplicities),(alpha,n,counts,multiplicities)
      if alpha>.5:
          alpha2=1-alpha
          # reduced equivalence preserved under complement; no need label sign proof
      else:
          ph=((n-1)*alpha)%1; th=(n*alpha)%1
          # event code in left-to-right order
          e=sorted([(1-th,'T'),(1-ph,'P'),(1-alpha,'A')])
          ord=''.join(z for x,z in e)
          assert ord in ['TPA','TAP','PAT','APT'],(alpha,n,ord)
          pair=(1,3) if ord in ['TPA','TAP'] else (0,2)
          assert ab(groups[pair[0]])==ab(groups[pair[1]]),(alpha,n,ord,groups)
          for a in range(4):
              for b in range(a+1,4):
                  assert (ab(groups[a])==ab(groups[b]))==((a,b)==pair),(alpha,n,ord,groups)
for alpha in [(math.sqrt(5)-1)/2, (3-math.sqrt(5))/2, math.sqrt(2)-1, math.sqrt(3)-1, math.pi-3, math.e-2,math.sqrt(11)-3,math.sqrt(13)-3, math.sqrt(7)-2, math.sqrt(19)-4]:
    for n in range(1,301): check(alpha,n)
print('PASSED 3000 alpha-length tests, including exact class/rank multiplicities and Abelian merging; all n<=300')
# Separate occurrence-based test, avoiding the rotation-interval construction.
for alpha in [(math.sqrt(5)-1)/2, math.sqrt(2)-1, math.pi-3, math.e-2]:
    text=''.join(str(math.floor((i+1)*alpha)-math.floor(i*alpha)) for i in range(12000))
    for n in range(1,101):
        corpus={text[i:i+n] for i in range(len(text)-n+1)}
        assert len(corpus)==n+1,(alpha,n,len(corpus))
        rr=Counter(red(w) for w in corpus)
        aa={ab(red(w)) for w in corpus}
        assert len(rr)==(2 if n==1 else 3 if n==2 else 4),(alpha,n,rr)
        assert len(aa)==(2 if n<=2 else 3),(alpha,n,aa)
print('PASSED separate direct-prefix enumeration: four irrational slopes, n=1..100, 12,000-symbol prefixes')
