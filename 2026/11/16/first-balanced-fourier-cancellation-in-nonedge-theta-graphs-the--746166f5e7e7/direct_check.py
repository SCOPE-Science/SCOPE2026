"""Direct exact ternary Fourier census of simple three-path theta graph colourings.
Python 3, standard library. Prints JSON; assertions are part of the certificate.
"""
from itertools import product, combinations_with_replacement
import json

def census(lengths):
    vertices=2; edges=[];paths=[]
    for length in lengths:
        mid=list(range(vertices,vertices+length-1));vertices+=length-1
        path=[0]+mid+[1];paths.append(path)
        edges.extend((path[i],path[i+1]) for i in range(length))
    proper=[x for x in product(range(3),repeat=vertices)
            if all(x[a]!=x[b] for a,b in edges)]
    by_degree=[0]*(vertices+1)
    balanced_zeros=[];signature=[]
    for k in product(range(3),repeat=vertices):
        hist=[0,0,0]
        for x in proper:
            exponent=sum(t*s for t,s in zip(k,x))%3
            hist[exponent]+=1
        vanishes=(hist[0]==hist[1]==hist[2])
        if sum(k)%3==0:
            if vanishes:
                balanced_zeros.append(k)
                by_degree[sum(a!=0 for a in k)]+=1
        else:
            assert vanishes, (lengths,k,hist)
        signature.append(tuple(hist))
    return {'lengths':lengths,'vertices':vertices,'proper':len(proper),
            'balanced_zero_by_degree':by_degree,
            'balanced_zeros':balanced_zeros,
            'spectrum':signature, 'paths':paths, 'proper_colours':proper}

def run():
    summary=[]
    for a,b,c in combinations_with_replacement(range(2,8),3):
        if a+b+c>9:continue
        r=census((a,b,c));n=r['vertices'];z=len(r['balanced_zeros'])
        assert len(r['spectrum'])==3**n
        assert r['proper']>0
        assert z==(584 if (a,b,c)==(2,3,4) else 0),(a,b,c,z)
        if (a,b,c)==(2,3,4):
            assert r['balanced_zero_by_degree']==[0,0,4,8,74,106,210,138,44]
            nonzero_frequency_pairs=[k for k in r['balanced_zeros'] if sum(x!=0 for x in k)==2]
            assert len(nonzero_frequency_pairs)==4
            assert set(tuple(i for i,v in enumerate(k) if v) for k in nonzero_frequency_pairs)=={(3,7),(4,5)}
            for u,v in ((3,7),(4,5)):
                agree=sum(x[u]==x[v] for x in r['proper_colours'])
                assert agree==54
        summary.append({'paths':[a,b,c],'n':n,'proper':r['proper'],
                        'balanced_zeros':z,'nonzero_multipliers':3**(n-1)-z,
                        'zero_by_degree':r['balanced_zero_by_degree']})
    assert len(summary)==7
    return summary

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,separators=(',',':')))
