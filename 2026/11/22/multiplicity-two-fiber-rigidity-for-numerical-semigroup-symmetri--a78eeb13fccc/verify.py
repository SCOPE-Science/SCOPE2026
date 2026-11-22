#!/usr/bin/env python3
"""Finite checks for a theorem on fibers of pseudo-Frobenius row deletion.

The checker proves no infinite statement. Run: python3 verify.py
"""
from collections import Counter


def contains(mask, x, conductor):
    return x >= conductor or bool(mask & (1 << x))


def enumerate_almost_symmetric(F):
    conductor=F+1
    for core in range(1 << (F-1)):
        mask=1 | (core << 1)
        members=[x for x in range(conductor) if contains(mask,x,conductor)]
        if any(not contains(mask,a+b,conductor)
               for a in members[1:] for b in members[1:]):
            continue
        gaps=[x for x in range(1,conductor) if not contains(mask,x,conductor)]
        pf=[x for x in gaps if all(contains(mask,x+s,conductor)
                                  for s in members[1:])]
        if 2*len(gaps) != F+len(pf):
            continue
        yield mask,pf,gaps


def delete_pf_rows(mask,F,pf):
    # Gap-deletion in original order; PF positions are NEVER recomputed.
    removed=set(pf)-{F}
    word=[(mask >> x) & 1 for x in range(F+1) if x not in removed]
    fprime=len(word)-1
    assert word[0] == 1 and word[-1] == 0
    small=frozenset(i for i in range(fprime) if word[i])
    return fprime,small


def semigroup(members,conductor):
    return all(a+b>=conductor or (a+b in members)
               for a in members for b in members)


def run(max_f=20):
    hist=Counter(); images=Counter(); checked=0
    for F in range(1,max_f+1):
        for mask,pf,gaps in enumerate_almost_symmetric(F):
            checked+=1
            fp,T=delete_pf_rows(mask,F,pf)
            assert (fp+1)%2==0
            genus=(fp+1)//2
            assert len(T)==genus
            assert all(((i in T) != ((fp-i) in T)) for i in range(fp+1))
            # Every image of multiplicity 2 is one of the standard T_g.
            if min((i for i in T if i>0), default=fp+1)==2:
                target=frozenset(range(0,2*genus,2))
                assert T==target,(F,mask,pf,fp,T)
                m=min(x for x in range(1,F+2) if contains(mask,x,F+1))
                src=frozenset(x for x in range(F+1) if contains(mask,x,F+1))
                if genus==1:
                    assert src==frozenset({0}) and F==m-1
                    hist['g1']+=1
                elif genus==2:
                    expected=frozenset({0,m}) if m>=3 else frozenset({0,2})
                    assert src==expected and F==m+1
                    hist['g2']+=1
                else:
                    assert m==2 and F==2*genus-1
                    assert src==target
                    hist['g3plus']+=1
                images[genus]+=1
            # Independently ensure deleting the original PF rows and
            # iteratively applying the output sequence agree.
            retained=[x for x in gaps if x==F or x not in pf]
            newgap=[x-sum(y<x for y in pf if y!=F) for x in retained]
            assert newgap==[i for i in range(fp+1) if i not in T]
    for g in range(1, max_f//2 +1):
        if g*2-1<=max_f:
            assert images[g]>=1
    print('VERIFY_OK')
    print('source_frobenius_max',max_f)
    print('almost_symmetric_sources',checked)
    print('multiplicity_two_cases',sum(images.values()))
    print('source_case_profile',dict(hist))
    print('target_genus_profile',sorted(images.items()))


if __name__=='__main__':run()
