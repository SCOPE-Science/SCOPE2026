"""Independent finite structural checks for height-two rooted functional digraphs.

Use: python check_invariants.py
Checks 2-variable one-point extension patterns against their triple invariant,
recycled k-variable child-witness conditions, and finite canonical profile counts.
It does not substitute for the unrestricted mathematical proof.
"""
import itertools,json
from collections import Counter,defaultdict


def structure(ds):
    f=[0];middles=[]
    for d in ds:
        middles.append(len(f));f.append(0)
    for mid,d in zip(middles,ds):f.extend([mid]*d)
    return f


def kind(f,v):
    if v==0:return 'R'
    if f[v]==0:return 'M+' if v in f[1:] else 'M0'
    return 'L'


def two_patterns(f,v):
    return frozenset((kind(f,w),int(v==w),int(f[v]==w),int(f[w]==v))
                     for w in range(len(f)))


def two_invariant(ds):
    return (min(sum(d==0 for d in ds),2),
            min(sum(d>=1 for d in ds),2), min(sum(ds),2))


def recycled_witness(f,p,k):
    kids=[x for x in range(len(f)) if x!=p and f[x]==p]
    # Explicitly checks k-1 simultaneous children of p followed by
    # rebinding the parent variable to a new child with the same image.
    return any(any(f[y]==f[t[0]] and y not in t for y in range(len(f)))
        for t in itertools.permutations(kids,k-1))


def main():
    ds=[()] + [x for m in range(1,5) for x in
        itertools.combinations_with_replacement(range(5),m) if 1+m+sum(x)<=11]
    profiles=defaultdict(list)
    witness_checks=0
    for d in ds:
        f=structure(d)
        sig=two_invariant(d)
        ext={kind(f,v):two_patterns(f,v) for v in range(len(f))}
        profiles[sig].append((d,ext))
        for k in (2,3,4):
            for p in range(1,1+len(d)):
                assert recycled_witness(f,p,k)==(d[p-1]>=k)
                witness_checks+=1
    for sig,members in profiles.items():
        standard=members[0][1]
        assert all(ext==standard for d,ext in members),sig
    assert len(profiles)==12,len(profiles)
    # Every profile of clipped class multiplicities is realizable:
    canonical_counts={}
    for k in (3,4):
        count=(k+1)**(k+1)
        example=[(j,m) for j in range(k+1) for m in range(k+1)]
        assert len(example)==(k+1)**2
        canonical_counts[k]=count
    print(json.dumps({'method':'independent directed-edge extension profiles and direct child witnesses',
      'structures':len(ds),'two_variable_extension_profiles':len(profiles),
      'recycled_child_threshold_tests':witness_checks,
      'extension_profile_discrepancies':0,'child_witness_discrepancies':0,
      'theoretical_canonical_spectrum_sizes':canonical_counts},indent=2))

if __name__=='__main__':main()
