#!/usr/bin/env python3
"""Exact integral boundary reductions for matching complexes of cycle complements.

Each pivot is +1 or -1 and only integer column/row operations are used.
The program exhaustively enumerates faces on graph orders 3 through 9.
"""
import json
from collections import defaultdict


def enumerate_complex(n):
    edges = [(i,j) for i in range(n) for j in range(i+1,n)
             if (j-i) not in (1,n-1)]
    faces = defaultdict(list)
    def search(i, mask, chosen):
        if i == len(edges):
            if chosen:
                faces[len(chosen)-1].append(chosen)
            return
        search(i+1, mask, chosen)
        a,b=edges[i]
        bit=(1<<a)|(1<<b)
        if mask&bit == 0:
            search(i+1, mask|bit, chosen+(i,))
    search(0,0,())
    return edges,faces


def boundary_matrix(faces,d):
    lower={face:i for i,face in enumerate(faces[d-1])}
    rows=[{} for _ in faces[d-1]]
    for col,face in enumerate(faces[d]):
        for j in range(len(face)):
            row=lower[face[:j]+face[j+1:]]
            rows[row][col]=1 if j%2==0 else -1
    return rows,len(faces[d])


def integral_unit_diagonalization(rows,ncols):
    """Return rank if the entire Smith form is diagonal with only unit entries.

    Select a sparse +/-1 pivot, clear its row by unimodular column additions,
    clear its column by unimodular row additions, and peel off that unit block.
    No division other than by a unit is used, hence integral homology is exact.
    """
    cols=[{} for _ in range(ncols)]
    live_columns=set()
    for r,row in enumerate(rows):
        for c,val in row.items():
            assert val in (-1,1)
            cols[c][r]=val
            live_columns.add(c)
    units=0
    while live_columns:
        candidates=[((len(rows[r])-1)*(len(cols[c])-1),r,c)
                    for c in live_columns for r,v in cols[c].items() if abs(v)==1]
        if not candidates:
            return {'rank_units':units,'residual_nonzero':sum(map(len,cols))}
        _,r,c=min(candidates)
        pivot=rows[r][c]
        for other_col,entry in list(rows[r].items()):
            if other_col == c:
                continue
            multiplier=entry*pivot
            for other_row,entry_col in list(cols[c].items()):
                updated=rows[other_row].get(other_col,0)-multiplier*entry_col
                if updated:
                    rows[other_row][other_col]=updated
                    cols[other_col][other_row]=updated
                else:
                    rows[other_row].pop(other_col,None)
                    cols[other_col].pop(other_row,None)
            if not cols[other_col]:
                live_columns.discard(other_col)
        for other_row in list(cols[c]):
            rows[other_row].pop(c,None)
        cols[c].clear()
        live_columns.remove(c)
        units+=1
    assert all(not row for row in rows)
    return {'rank_units':units,'residual_nonzero':0}


def verify(n):
    edges,faces=enumerate_complex(n)
    f={d:len(v) for d,v in sorted(faces.items())}
    if not f:
        return {'n':n,'edge_count':0,'faces':{},'boundary_ranks':{},'homology':{},
                'geometry':'empty'}
    ranks={}
    for d in sorted(f):
        if d==0: continue
        matrix,nc=boundary_matrix(faces,d)
        reduction=integral_unit_diagonalization(matrix,nc)
        assert reduction['residual_nonzero']==0, (n,d,reduction)
        ranks[d]=reduction['rank_units']
    if n>=5:
        assert ranks[1]==f[0]-1
    result={}
    for d in f:
        betti=f[d]-ranks.get(d,0)-ranks.get(d+1,0)
        if d==0:betti-=1
        assert betti>=0
        if betti:result[d]=betti
    return {'n':n,'edge_count':len(edges),'faces':f,'boundary_ranks':ranks,
            'reduced_integral_homology':result,
            'all_nonzero_integer_smith_factors_one':True}

if __name__=='__main__':
    data=[verify(n) for n in range(3,10)]
    assert [x.get('reduced_integral_homology') for x in data[2:]] == [
        {1:1},{1:6},{1:1},{2:42},{2:42,3:1}]
    print(json.dumps(data,sort_keys=True,separators=(',',':')))
    print('ANTICYCLE_COMPLEMENT_INTEGRAL_BOUNDARIES_PASS')
