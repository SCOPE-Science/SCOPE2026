"""Exhaustive endpoint-wise width verification for mixed Hamming products."""
from itertools import product, combinations, permutations
from check_ipco import antichain_width


def expected(a,b,root):
    erased=added=replaced=0
    for x,y,r in zip(a,b,root):
        if x==y:continue
        if x==r:added+=1
        elif y==r:erased+=1
        else:replaced+=1
    return 1+replaced+min(erased,added)


def main():
    cases=[(2,2,2,2),(3,3,3),(2,3,4),(2,2,3,3),(2,2,2,3)]
    for q in cases:
        r=(0,)*len(q)
        vertices=list(product(*(range(k) for k in q)))
        pair_count=path_count=0
        for a,b in combinations(vertices,2):
            coords=[i for i in range(len(q)) if a[i]!=b[i]]
            obtained=0
            for order in permutations(coords):
                x=list(a);path=[tuple(x)]
                for i in order:
                    x[i]=b[i];path.append(tuple(x))
                obtained=max(obtained,antichain_width(path,r))
                path_count+=1
            claim=expected(a,b,r)
            if obtained!=claim:
                raise AssertionError((q,a,b,obtained,claim))
            pair_count+=1
        print('ENDPOINT_PASS',q,'pairs',pair_count,'paths',path_count)
    print('ALL_ENDPOINT_TESTS_PASS')

if __name__=='__main__':main()
