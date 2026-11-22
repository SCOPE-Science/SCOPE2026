"""Independent direct subset-pair enumeration certificate, pure Python.

Run: python check_direct.py
No exact-cover recursion is used; all normalized pairs are tested directly.
"""
import itertools, math, json

GROUPS=((16,),(8,2),(4,4),(4,2,2),(2,2,2,2))

def run(dims):
    elements=list(itertools.product(*(range(d) for d in dims)))
    loc={p:j for j,p in enumerate(elements)}
    N=len(elements)
    E=max(dims)
    addition=tuple(tuple(loc[tuple((a+b)%d for a,b,d in zip(x,y,dims))]
                         for y in elements) for x in elements)
    subtraction=tuple(tuple(loc[tuple((a-b)%d for a,b,d in zip(x,y,dims))]
                         for y in elements) for x in elements)
    phase=tuple(tuple(sum((a*b*(E//d) for a,b,d in zip(x,y,dims)))%E
                      for x in elements) for y in elements)

    normalized={s:list(itertools.combinations(range(1,N),s-1)) for s in [1,2,4,8,16]}
    zeros={}
    def zero_set(B):
        B=tuple(B)
        if B in zeros:return zeros[B]
        out=0
        for y in range(1,N):
            residue=[0]*E
            for x in B:residue[phase[y][x]]+=1
            if sum(abs(residue[j]-residue[j+E//2]) for j in range(E//2))==0:
                out|=1<<y
        zeros[B]=out
        return out

    # For each proposed normalized spectrum, calculate the EXACT set of its
    # nonzero pairwise differences. Also identify all subgroup spectra.
    proposals={}; subgroups={}
    for s in [1,2,4,8,16]:
        proposals[s]=[];subgroups[s]=[]
        for r in normalized[s]:
            H=(0,)+r
            req=0
            for x,y in itertools.combinations(H,2):
                req|=1<<subtraction[x][y]
            proposals[s].append(req)
            if all(addition[x][y] in H for x in H for y in H):
                subgroups[s].append(req)
    Bsets={s:[(0,)+r for r in normalized[s]] for s in [1,2,4,8,16]}
    cnt={s:0 for s in [1,2,4,8,16]}
    bad={s:0 for s in [1,2,4,8,16]}
    for s in [1,2,4,8,16]:
        m=N//s
        for A in itertools.combinations(range(N),s):
            common=(1<<N)-2
            ncomp=0
            for B in Bsets[m]:
                used=0
                valid=True
                for a in A:
                    for b in B:
                        bit=1<<addition[a][b]
                        if used&bit:
                            valid=False
                            break
                        used|=bit
                    if not valid:break
                if valid and used==(1<<N)-1:
                    ncomp+=1
                    common &= zero_set(B)
            if ncomp==0:continue
            cnt[s]+=1
            if not any((requirement & common)==requirement for requirement in proposals[m]):
                raise AssertionError(('No common spectrum',dims,A))
            if not any((requirement & common)==requirement for requirement in subgroups[m]):
                bad[s]+=1
    return {'group':list(dims),'tile_count':sum(cnt.values()),
            'tile_count_by_size':{str(s):cnt[s] for s in cnt},
            'non_subgroup_universal_spectrum_count':sum(bad.values()),
            'non_subgroup_count_by_size':{str(s):bad[s] for s in bad},
            'all_tiles_have_universal_spectrum':True}

if __name__=='__main__':
    print(json.dumps([run(ds) for ds in GROUPS],sort_keys=True,indent=2))
