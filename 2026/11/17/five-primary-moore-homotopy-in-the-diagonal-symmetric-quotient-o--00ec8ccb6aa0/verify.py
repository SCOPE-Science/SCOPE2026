#!/usr/bin/env python3
"""Independent, exact-integer replay for the diagonal symmetric quotient of Delta(5,5).

Run: python verify.py
No external Python packages or network calls required.
"""
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
import json
import math

N = 5

def faces_and_actions():
    faces=[]
    by_size={}
    for k in range(1,N+1):
        entries=[]
        for rows in combinations(range(N),k):
            for cols in permutations(range(N),k):
                entries.append(frozenset(zip(rows,cols)))
        by_size[k]=entries
        faces+=entries
    index={face:i for i,face in enumerate(faces)}
    group=list(permutations(range(N)))
    actions=[[index[frozenset((p[i],p[j]) for i,j in face)]
              for face in faces] for p in group]
    return faces, by_size, index, group, actions

def orbit_cells(by_size,index,actions):
    seen={}
    cells=[]
    for q in range(1,N+1):
        for ranks in combinations(range(1,N+1),q):
            for top in by_size[ranks[-1]]:
                for ordering in permutations(sorted(top)):
                    chain=tuple(index[frozenset(ordering[:k])] for k in ranks)
                    if chain in seen:
                        continue
                    cell_id=len(cells)
                    cells.append(chain)
                    for action in actions:
                        transformed=tuple(action[i] for i in chain)
                        if transformed in seen:
                            assert seen[transformed]==cell_id
                        seen[transformed]=cell_id
    return cells,seen

def chain_complex(cells,seen):
    by_dim={d:[i for i,c in enumerate(cells) if len(c)==d+1] for d in range(N)}
    boundary={}
    for d in range(1,N):
        matrix={}
        for cell_id in by_dim[d]:
            chain=cells[cell_id]
            coefficients=Counter()
            for i in range(d+1):
                coefficients[seen[chain[:i]+chain[i+1:]]]+=(-1)**i
            matrix[cell_id]={k:v for k,v in coefficients.items() if v}
        boundary[d]=matrix
    return by_dim,boundary

def check_chain_condition(boundary):
    for d in range(2,N):
        for cell_id,col in boundary[d].items():
            image=Counter()
            for y,v in col.items():
                for z,w in boundary[d-1][y].items():
                    image[z]+=v*w
            assert not any(image.values()),(d,cell_id)

def independent_burnside(faces,group):
    # A fixed nested chain is obtained by partitioning the cycles of the
    # induced permutation on its fixed terminal matching into ordered nonempty stages.
    stirling=[[0]*(N+1) for _ in range(N+1)]
    stirling[0][0]=1
    for c in range(1,N+1):
        for q in range(1,N+1):
            stirling[c][q]=q*stirling[c-1][q]+stirling[c-1][q-1]
    tally=[0]*N
    for p in group:
        for face in faces:
            induced={e:(p[e[0]],p[e[1]]) for e in face}
            if set(induced.values())!=set(face):
                continue
            unseen=set(face)
            cycles=0
            while unseen:
                cycles+=1
                e=next(iter(unseen))
                while e in unseen:
                    unseen.remove(e)
                    e=induced[e]
            for q in range(1,cycles+1):
                tally[q-1]+=math.factorial(q)*stirling[cycles][q]
    assert all(v%len(group)==0 for v in tally)
    return [v//len(group) for v in tally]

def replay(by_dim,boundary,certificate):
    live={d:set(v) for d,v in by_dim.items()}
    for d,a,b in certificate['steps']:
        assert a in live[d-1] and b in live[d]
        pivot_col=boundary[d][b]
        pivot=pivot_col[a]
        assert abs(pivot)==1
        for x,col in boundary[d].items():
            if x==b or a not in col:
                continue
            quotient=col[a]//pivot
            for y,v in pivot_col.items():
                value=col.get(y,0)-quotient*v
                if value:col[y]=value
                else:col.pop(y,None)
        del boundary[d][b]
        live[d].remove(b)
        live[d-1].remove(a)
        if d>1:
            del boundary[d-1][a]
        if d+1<N:
            for col in boundary[d+1].values():
                col.pop(b,None)
    check_chain_condition(boundary)
    survivors={str(d):sorted(live[d]) for d in range(N)}
    assert survivors==certificate['survivors']
    assert {str(d):boundary[d] for d in range(1,N)} == {
        str(d):{int(k):{int(r):v for r,v in col.items()} for k,col in matrix.items()}
        for d,matrix in certificate['boundaries'].items()}
    assert [len(live[d]) for d in range(N)]==[1,0,1,1,0]
    assert len(boundary[3])==1
    assert list(boundary[3].values())[0] in ({list(live[2])[0]:5},{list(live[2])[0]:-5})
    return survivors

def main():
    cert=json.loads((Path(__file__).parent/'reduction_certificate.json').read_text('utf-8'))
    assert cert['n']==N
    faces,by_size,index,group,actions=faces_and_actions()
    cells,seen=orbit_cells(by_size,index,actions)
    by_dim,boundary=chain_complex(cells,seen)
    counts=[len(by_dim[d]) for d in range(N)]
    assert counts==[35,199,429,384,120]==cert['counts']
    check_chain_condition(boundary)
    assert independent_burnside(faces,group)==counts
    surviving=replay(by_dim,boundary,cert)
    assert len(cert['steps'])==582
    print('PASS: independent Burnside counts',counts)
    print('PASS: 582 integer unit cancellations yield ranks (1,0,1,1,0)')
    print('PASS: only reduced boundary is multiplication by 5 from degree 3 to 2')
    print('PASS: H_0=Z, H_2=Z/5, all other integral homology vanishes')
if __name__=='__main__':main()
