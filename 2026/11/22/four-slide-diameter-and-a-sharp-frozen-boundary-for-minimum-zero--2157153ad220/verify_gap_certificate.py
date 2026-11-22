"""Independent certificate validation for all cyclic-gap types of a pair of optimum triples."""
from itertools import product, combinations
from collections import Counter


def success(n, whites):
    """Literal zero forcing on complement of C_n (independent of pair-pattern shortcuts)."""
    unseen=set(whites)
    while unseen:
        candidates=[]
        for u in range(n):
            if u in unseen:
                continue
            neighbors=[v for v in unseen if v != u and (v-u)%n not in (1,n-1)]
            if len(neighbors)==1:
                candidates.append(neighbors[0])
        if not candidates:
            return False
        unseen.difference_update(candidates)
    return True


def all_canonical_profiles():
    for m in (4,5,6):
        for gaps in product(range(1,8),repeat=m):
            if sum(gaps)<7:
                continue
            if gaps != min(gaps[i:]+gaps[:i] for i in range(m)):
                continue
            yield m,gaps


def coordinates(gaps):
    result=[]
    curr=0
    for g in gaps:
        result.append(curr)
        curr+=g
    return result,curr


def mask_points(mask, coords):
    return [coords[i] for i in range(len(coords)) if mask & (1<<i)]


def candidate_keys(m,gaps):
    coords,n=coordinates(gaps)
    choices=[]
    for subset in combinations(range(m),3):
        mask=sum(1<<i for i in subset)
        if success(n,mask_points(mask,coords)):
            choices.append(mask)
    choices.sort()
    mask_all=(1<<m)-1
    for A,B in combinations(choices,2):
        if A|B==mask_all:
            yield (m,gaps,A,B)


def check():
    observed={}
    filename='gap_certificate.tsv'
    with open(filename,encoding='utf-8') as f:
        for line_id,line in enumerate(f,1):
            fields=line.rstrip('\n').split('\t')
            assert len(fields)==6,(line_id,'format')
            m=int(fields[0]);gaps=tuple(map(int,fields[1].split(',')))
            A=int(fields[2]);B=int(fields[3]);helper=int(fields[4])
            states=list(map(int,fields[5].split(',')))
            key=(m,gaps,A,B)
            assert key not in observed,(line_id,'duplicate')
            marked,n=coordinates(gaps)
            assert len(marked)==m and n>=7 and len(states)-1<=4
            assert states[0]==A and states[-1]==B
            assert helper==-1 or (helper not in marked and 0<=helper<n
                and min(min((helper-x)%n,(x-helper)%n) for x in marked)<=2)
            coords=marked+([] if helper==-1 else [helper])
            allowed_mask=(1<<len(coords))-1
            for mask in states:
                assert mask & ~allowed_mask == 0 and mask.bit_count()==3,(line_id,'cardinality')
                assert success(n,mask_points(mask,coords)),(line_id,'non-forcing intermediate')
            for old,new in zip(states,states[1:]):
                gone=old & ~new;gained=new & ~old
                assert gone.bit_count()==gained.bit_count()==1,(line_id,'one token')
                old_position=coords[gone.bit_length()-1]
                new_position=coords[gained.bit_length()-1]
                assert (old_position-new_position)%n not in (0,1,n-1),(line_id,'not an edge of complement')
            observed[key]=True
    expected=set()
    profiles=0
    for m,gaps in all_canonical_profiles():
        profiles+=1
        expected.update(candidate_keys(m,gaps))
    assert set(observed)==expected,('incomplete certificate',len(observed),len(expected),len(expected-set(observed)),len(set(observed)-expected))
    assert profiles==23659 and len(observed)==10713
    print('VALID_CERTIFICATE profiles=%d eligible_pairs=%d all_paths_at_most_four=PASS'% (profiles,len(observed)))

if __name__=='__main__':
    check()
