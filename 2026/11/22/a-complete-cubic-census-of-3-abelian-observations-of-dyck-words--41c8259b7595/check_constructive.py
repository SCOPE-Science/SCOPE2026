#!/usr/bin/env python3
"""Construct one Dyck word for every claimed feasible profile parameter."""

def compositions(total, runs, singles, descending):
    assert runs>=0 and 0<=singles<=runs
    if runs==0:
        assert total==0
        return []
    long=runs-singles
    if long==0:
        assert total==runs
        return [1]*runs
    extra=total-singles-2*long
    assert extra>=0
    if descending:
        return [2+extra]+[2]*(long-1)+[1]*singles
    return [1]*singles+[2]*(long-1)+[2+extra]

def params(word):
    runs=[];prev=None
    for x in word:
        if x==prev:runs[-1]+=1
        else:runs.append(1)
        prev=x
    a,b=runs[::2],runs[1::2]
    return len(a),sum(x==1 for x in a),sum(x==1 for x in b),int(a[0]==1),int(b[-1]==1)

def make_word(m,p,u,v,alpha,beta):
    if p==m:
        assert alpha==beta==1 and u==v==p
        return '10'*m
    t=alpha+beta
    mm=m-t;rr=p-t;uu=u-t;vv=v-t
    a=compositions(mm,rr,uu,True)
    b=compositions(mm,rr,vv,False)
    core=''.join('1'*ai+'0'*bi for ai,bi in zip(a,b))
    return ('10' if alpha else '')+core+('10' if beta else '')

def sig(word):
    return tuple(sum(word[i:i+k] == format(j, f'0{k}b')
                     for i in range(len(word)-k+1))
                 for k in (1,2,3) for j in range(2**k))

def is_dyck(word):
    height=0
    for c in word:
        height += 1 if c=='1' else -1
        if height<0:return False
    return height==0

def main():
    for m in range(1,23):
        profiles=set(); tuples=0
        for p in range(1,m+1):
            if p==m:
                cases=[(p,p,p,1,1)]
            else:
                lo=max(0,2*p-m)
                cases=[(p,u,v,a,b) for a in (0,1) for b in (0,1)
                    for u in range(max(lo,a+b),p)
                    for v in range(max(lo,a+b),p)]
            for pa in cases:
                word=make_word(m,*pa)
                assert len(word)==2*m and is_dyck(word), (m,pa,word)
                assert params(word)==pa, (m,pa,params(word),word)
                x=sig(word)
                assert x not in profiles, (m,pa)
                profiles.add(x);tuples+=1
        expected=m*(m*m-3*m+5)//3
        assert tuples==expected and len(profiles)==expected,(m,tuples,expected)
        if m in (1,2,3,5,10,20,15,18,22):print(f'm={m:2d}, constructed distinct spectra={len(profiles):6d}')
    print('PASS: explicit constructive witnesses and no duplicate profiles to semilength 22')

if __name__=='__main__':main()
