"""Exact finite adaptive-Haar endpoint diagnostics (stdlib Python 3)."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product

@lru_cache(None)
def shapes(n):
    if n == 1:
        return (None,)
    return tuple((left, right)
                 for i in range(1, n)
                 for left in shapes(i) for right in shapes(n-i))

def enumerate_tree(tree):
    leaves, internals = [], []
    def visit(node, path):
        if node is None:
            leaves.append(path)
        else:
            internals.append(path)
            visit(node[0], path+(0,))
            visit(node[1], path+(1,))
    visit(tree, ())
    return leaves, internals

def full_binary_constant(h):
    return Q(2*h,3)+Q(5,9)+Q(4,9)*Q(-1,2)**h

def leaf_row_peak(paths, internal, i):
    x=paths[i]
    masses=[Q(1,2**len(y)) for y in paths]
    per_node=[]
    for v in internal:
        dep=len(v)
        if x[:dep]!=v: continue
        vx=1 if x[dep]==0 else -1
        per_node.append([0 if y[:dep]!=v else (2**dep)*vx*(1 if y[dep]==0 else -1) for y in paths])
    best=Q(-1)
    for signs in product((-1,1),repeat=len(per_node)):
        total=sum(masses[j]*abs(1+sum(s*c[j] for s,c in zip(signs,per_node)))
                  for j in range(len(paths)))
        if total>best:best=total
    return best

def run():
    count=0; row_count=0; spectra={}
    for n in range(1,8):
        observed=set()
        for sh in shapes(n):
            paths,internal=enumerate_tree(sh)
            maxdepth=max(map(len,paths))
            row_peaks=[leaf_row_peak(paths,internal,j) for j in range(n)]
            for p,u in zip(paths,row_peaks):
                assert u==full_binary_constant(len(p)), (n,paths,p,u)
                row_count+=1
            assert max(row_peaks)==full_binary_constant(maxdepth), (n,paths)
            observed.add(maxdepth)
            count+=1
        if n==1:want={0}
        else:want=set(range((n-1).bit_length(),n))
        assert observed==want,(n,observed,want)
        spectra[n]=[(d,str(full_binary_constant(d))) for d in sorted(observed)]
    print('EXHAUSTIVE_PLANE_FULL_BINARY_TREES_PASSED',count)
    print('INDEPENDENT_KERNEL_ROW_EXTREMA_PASSED',row_count)
    for n,vals in spectra.items():
        print('LEAF_COUNT',n,'EXACT_SPECTRUM',vals)
    print('ALL_ADAPTIVE_DYADIC_HAAR_CHECKS_PASSED')
if __name__=='__main__':run()
