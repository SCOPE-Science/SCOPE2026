"""Independent direct fixed-point-prefix cross-check, not an infinite proof."""

def expand(q,r,length):
    v=[0]
    while len(v)<length:
        v=[x for c in v for x in ([c]*r+[(c+1)%q])]
    return bytes(v)

cases=0
for q in range(3,6):
    for r in range(2,6):
        B=r+1; L=B*(B+1)
        word=expand(q,r,120000)
        observed=set()
        for n in (L,L+1):
            two=set()
            counts={}
            for i in range(len(word)-n+1):
                w=word[i:i+n]
                if len(set(w))<=2:two.add(w)
            if n==L:
                exp={bytes([a])+bytes(z for _ in range(r+1) for z in ([a]*r+[(a+1)%q]))+bytes([(a+1)%q])*r for a in range(q)}
                assert two==exp,(q,r,len(two))
            else:
                assert len(two)==0,(q,r,len(two))
        print('prefix PASS:',q,r,'max_length',L,'count',q)
        cases+=1
print('PASS:',cases,'parameter pairs with independent direct windows')
