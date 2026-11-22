"""Separately enumerate the proposed zero-position intervals and verify them by literal search."""
from itertools import product

def proposed_pairs(a,b,c):
    word='0'*a+'1'+'0'*b+'1'+'0'*c
    p=a; q=a+b+1
    M=max(a,b,c)
    Z={i for i,x in enumerate(word) if x=='0' and ((i<a and a==M) or (p<i<q and b==M) or (i>q and c==M))}
    def acceptable(marker):
        if marker==p:
            missing_left=b>a
            missing_right=c>b
            lo=max(q-a-1 if missing_left else 0, q if missing_right else 0)
            hi=min(q if missing_left else len(word)-1, q+b+1 if missing_right else len(word)-1)
        else:
            missing_left=a>b
            missing_right=b>c
            lo=max(p-(b+1) if missing_left else 0,p if missing_right else 0)
            hi=min(p if missing_left else len(word)-1,p+(c+1) if missing_right else len(word)-1)
        return {(min(marker,z),max(marker,z)) for z in Z if lo<=z<=hi}
    return acceptable(p)|acceptable(q)

def literal_ok(word,pair):
    mask=set(pair)
    words=set(word[i:j] for i in range(len(word)) for j in range(i+1,len(word)+1))
    covered={word[i:j] for i in range(len(word)) for j in range(i+1,len(word)+1) if any(i<=k<j for k in mask)}
    return words==covered

def test():
    triple_count=0; tested_pairs=0
    for a,b,c in product(range(1,9),repeat=3):
        word='0'*a+'1'+'0'*b+'1'+'0'*c
        pairs=proposed_pairs(a,b,c)
        assert len(pairs)>0
        for pair in pairs:
            assert literal_ok(word,pair),(a,b,c,pair)
            tested_pairs+=1
        triple_count+=1
    for s in range(3,111):
        vals=[]
        for a in range(1,s-1):
            for b in range(1,s-a):
                c=s-a-b
                pairs=proposed_pairs(a,b,c)
                vals.append(len(pairs))
        assert vals and min(vals)>=2
    print(f'INTERVAL_CONSTRUCTION_OK triples={triple_count} direct_covered_pairs={tested_pairs} composition_sums=108')

if __name__=='__main__':test()
