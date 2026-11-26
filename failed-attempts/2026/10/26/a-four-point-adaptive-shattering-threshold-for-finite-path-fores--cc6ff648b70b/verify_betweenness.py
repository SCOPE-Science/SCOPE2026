"""Independent verifier of finite betweenness certificates and exact VC upper bounds.
Usage: python3 verify_betweenness.py finite_betweenness_certificate.json
"""
import json,itertools,sys,math
from pathlib import Path

def path_universe(n):
    arr=set()
    for t in itertools.permutations(range(n)):
        arr.add(min(t,t[::-1]))
    return sorted(arr)

def bt(path, triple):
    if len(set(triple))!=3:return False
    a,b,c=triple
    if set(triple)-set(path):return False
    ix={x:i for i,x in enumerate(path)}
    return (ix[a]<ix[b]<ix[c]) or (ix[c]<ix[b]<ix[a])

def query_universe(n):
    return [(a,b,c) for a,b,c in itertools.permutations(range(n),3) if a<c]

def check(c):
    n=c['n']; U=path_universe(n)
    assert c['number_of_unoriented_labeled_paths']==len(U)==(math.factorial(n)//2 if n>1 else 1)
    Q=set(query_universe(n))
    assert c['Ldim']<=int(math.log2(len(U))) if len(U)>1 else c['Ldim']==0
    visited=[]
    def visit(t,k,history):
        if k==0:
            assert set(t)=={'witness'}
            p=tuple(t['witness']);assert len(p)==n and set(p)==set(range(n));p=min(p,p[::-1]);assert p in U
            assert all(int(bt(p,q))==b for q,b in history)
            visited.append(p);return
        assert set(t)=={'query','zero','one'}
        q=tuple(t['query']);assert q in Q
        visit(t['zero'],k-1,history+[(q,0)])
        visit(t['one'],k-1,history+[(q,1)])
    visit(c['littlestone_tree'],c['Ldim'],[])
    assert len(visited)==2**c['Ldim'] and len(set(visited))==len(visited)
    vc=c['VCdim'];selected=[tuple(q) for q in c['vc_queries']]
    assert len(selected)==vc and len(set(selected))==vc and all(q in Q for q in selected)
    expected={format(j,f'0{vc}b') for j in range(2**vc)} if vc else {''}
    witnesses=c['vc_witnesses']
    assert set(witnesses)==expected
    for outcome, p in witnesses.items():
        canonical=min(tuple(p),tuple(p[::-1]));assert canonical in U
        assert ''.join(str(int(bt(canonical,q))) for q in selected)==outcome
    # Exhaustive upper proof: no (VC+1)-subset of ternary instances is shattered.
    # This suffices to exclude every larger set by heredity.
    C=0
    Qsorted=sorted(Q)
    masks=[sum(1<<i for i,p in enumerate(U) if bt(p,q)) for q in Qsorted]
    FULL=(1<<len(U))-1
    for idx in itertools.combinations(range(len(Qsorted)),vc+1):
        C+=1
        states=[FULL]
        for j in idx:
            mask=masks[j]
            nxt=[]
            for state in states:
                zero=state&~mask;one=state&mask
                if not zero or not one:
                    nxt=[];break
                nxt.extend((zero,one))
            if not nxt:
                break
            states=nxt
        else:
            raise AssertionError(f'VC bound failed at n={n}, {[Qsorted[j] for j in idx]}')
    print(f'n={n} paths={len(U)} VC={vc} Ldim={c["Ldim"]} checked_VC_obstruction_sets={C} adaptive_leaves={len(visited)}')

if __name__=='__main__':
    assert len(sys.argv)==2
    pack=json.loads(Path(sys.argv[1]).read_text())
    assert pack['format']=='betweenness_path_concept_cert_v1'
    assert [c['n'] for c in pack['cases']]==[1,2,3,4,5]
    for c in pack['cases']:check(c)
    print('BETWEENNESS_CERTIFICATES_ALL_PASS')
