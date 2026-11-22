"""Finite local obstruction to three-slide paths, using literal zero forcing."""
from itertools import permutations

def forcing(n, w):
    white=set(w)
    while white:
        found=[]
        for v in range(n):
            if v in white: continue
            neighbors=[x for x in white if x!=v and (x-v)%n not in (1,n-1)]
            if len(neighbors)==1: found.append(neighbors[0])
        if not found: return False
        white.difference_update(found)
    return True

def count_direct_three_moves(n, source, target):
    assert forcing(n,source) and forcing(n,target) and not (set(source)&set(target))
    count=0
    for src_order in permutations(source):
        for dst_order in permutations(target):
            white=set(source); ok=True
            for a,b in zip(src_order,dst_order):
                if (a-b)%n in (1,n-1): ok=False; break
                white.remove(a);white.add(b)
                if not forcing(n,white):ok=False;break
            if ok:count+=1
    return count

for n,s,t in [(7,(0,2,4),(1,5,6)),(8,(0,2,4),(1,3,5)),(9,(0,2,4),(1,3,5)),(11,(0,2,4),(1,3,5))]:
    c=count_direct_three_moves(n,s,t)
    assert c==0
    print(f'order={n} three_move_relocations={c} LOWER_BOUND_4')
print('LOWER_BOUND_CERTIFICATE_PASS')
