import sys,itertools,collections
sys.path.insert(0,'/mnt/data/alt_candidate')
from verify import boolean_solutions,conservation_matrix,rule_bit
S,_,_=boolean_solutions(conservation_matrix(8))

def missing(f,g):
    trans=[[0]*4 for _ in range(8)]
    for bits in itertools.product((0,1),repeat=5):
        a,b,c,d,e=bits
        v=4*a+2*b+c; w=4*c+2*d+e
        symbol=2*rule_bit(f,(a,b,c,d))+rule_bit(g,(b,c,d,e))
        trans[v][symbol]|=1<<w
    Q=collections.deque([(255,())]);seen={255}
    while Q:
        subset,word=Q.popleft()
        for symbol in range(4):
            nxt=0
            for v in range(8):
                if (subset>>v)&1:nxt |= trans[v][symbol]
            if not nxt:return word+(symbol,),len(seen)
            if nxt not in seen:seen.add(nxt);Q.append((nxt,word+(symbol,)))
    return None,len(seen)

hist=collections.Counter();surj=[];bounds={}
for f,g in sorted(S):
    word,m=missing(f,g)
    if word is None:surj.append((f,g))
    else:
        hist[len(word)]+=1
        bounds[(f,g)]=word
print('surj count',len(surj),'surj',surj)
print('non-surj shortest forbidden pair lengths',hist,'max',max(hist))
print('extremals',[(k,v) for k,v in bounds.items() if len(v)==max(hist)][:20])
