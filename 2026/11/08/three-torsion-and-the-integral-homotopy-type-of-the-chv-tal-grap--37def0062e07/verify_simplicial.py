"""Independent simplicial boundary rank computation for the Chvatal matching complex.
Python 3 standard library only. Invoke: python3 verify_simplicial.py
"""
from collections import Counter
from itertools import combinations

EDGES=((0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11))


def simplices_by_dimension():
    # Enumerate by size, independent of bitmask face recursion.
    output=[]
    for k in range(1,7):
        layer=[]
        for candidate in combinations(range(len(EDGES)),k):
            endpoints=[v for idx in candidate for v in EDGES[idx]]
            if len(set(endpoints))==2*k:
                layer.append(candidate)
        output.append(layer)
    return output


def rank_boundary(columns,row_pos,p):
    pivots={}
    for sigma in columns:
        column={row_pos[sigma[:i]+sigma[i+1:]]:(1 if i%2==0 else p-1) for i in range(len(sigma))}
        while column:
            i=min(column)
            if i not in pivots:
                inv=pow(column[i],-1,p)
                pivots[i]={j:(a*inv)%p for j,a in column.items() if a%p}
                break
            t=column[i]
            for j,v in pivots[i].items():
                a=(column.get(j,0)-t*v)%p
                if a:column[j]=a
                elif j in column:del column[j]
    return len(pivots)


def main():
    layers=simplices_by_dimension()
    assert list(map(len,layers))==[24,204,752,1175,628,52]
    maps=[{sigma:i for i,sigma in enumerate(layer)} for layer in layers]
    for p in (2,3,5):
        ranks=[rank_boundary(layers[k],maps[k-1],p) for k in range(1,6)]
        assert ranks==([23,181,571,575,52] if p==3 else [23,181,571,576,52])
        # Over a field H_0 is connected and H_k dimensions from nullity-minus-next-rank.
        betti=[len(layers[k])-(ranks[k-1] if k>0 else 0)-(ranks[k] if k<5 else 0) for k in range(6)]
        reduced=[betti[0]-1]+betti[1:]
        assert reduced==([0,0,0,29,1,0] if p==3 else [0,0,0,28,0,0])
        print('p='+str(p)+' boundary_ranks_1_to_5='+','.join(map(str,ranks))+' reduced_betti_0_to_5='+','.join(map(str,reduced)))
    print('CHVATAL_MATCHING_DIRECT_SIMPLICIAL_PASS')

if __name__=='__main__':main()
