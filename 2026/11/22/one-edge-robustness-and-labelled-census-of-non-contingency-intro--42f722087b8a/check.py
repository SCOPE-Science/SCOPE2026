"""Finite exhaustive cross-checks for symmetric non-contingency introspection.
Run: python3 check.py ; Python standard library only.
"""
from itertools import combinations
from math import comb, factorial


def adjacencies(n, edges):
    adj = [0]*n
    for bit, (i,j) in enumerate(combinations(range(n), 2)):
        if (edges >> bit) & 1:
            adj[i] |= 1 << j
            adj[j] |= 1 << i
    return adj


def modal_valid(adj):
    n=len(adj)
    for valuation in range(1<<n):
        truth = 0
        for i, mask in enumerate(adj):
            b=valuation & mask
            if b==0 or b==mask:
                truth |= 1<<i
        for i, mask in enumerate(adj):
            if (truth>>i)&1:
                b=truth & mask
                if b != 0 and b != mask:
                    return False
    return True


def component_parts(adj):
    n=len(adj)
    todo=set(range(n)); parts_all=[]
    while todo:
        seed=next(iter(todo)); component={seed}; active=[seed]; todo.remove(seed)
        while active:
            u=active.pop()
            for v in list(todo):
                if (adj[u]>>v)&1:
                    component.add(v); active.append(v); todo.remove(v)
        rem=set(component); parts=[]
        while rem:
            seed=next(iter(rem)); block={seed}; queue=[seed]; rem.remove(seed)
            while queue:
                u=queue.pop()
                for v in list(rem):
                    if not ((adj[u]>>v)&1):
                        block.add(v); queue.append(v); rem.remove(v)
            for u in block:
                for v in block:
                    if u!=v and ((adj[u]>>v)&1):
                        return None
            parts.append(block)
        parts_all.append(parts)
    return parts_all


def structure_valid(adj):
    return component_parts(adj) is not None


def edit_predictions(adj):
    parts_all=component_parts(adj)
    assert parts_all is not None
    isolate=0; star_centers=0; adds=deletes=0
    for parts in parts_all:
        sizes=[len(p) for p in parts]
        n=sum(sizes)
        if n==1:
            isolate+=1
            continue
        adds += sum(s==2 for s in sizes)
        if len(sizes)==2 and min(sizes)==1:
            deletes += sizes[0]*sizes[1]
            star_centers += 2 if n==2 else 1
        else:
            t=sum(s==1 for s in sizes)
            deletes+=comb(t,2)
    adds+=comb(isolate,2)+isolate*star_centers
    return adds,deletes


def bell(n):
    arr=[0]*(n+1); arr[0]=1
    for i in range(1,n+1):
        arr[i]=sum(comb(i-1,k)*arr[k] for k in range(i))
    return arr


def exact_expected(nmax):
    # Exponential generating coefficients in factorial-scaled integers.
    bellnums=bell(nmax)
    connected=[0]*(nmax+1)
    connected[1]=1
    for n in range(2,nmax+1):connected[n]=bellnums[n]-1
    totals=[0]*(nmax+1); totals[0]=1
    for n in range(1,nmax+1):
        totals[n]=sum(comb(n-1,k-1)*connected[k]*totals[n-k] for k in range(1,n+1))
    delete_connected=[0]*(nmax+1)
    for n in range(2,nmax+1):
        delete_connected[n]=comb(n,2)*bellnums[n-2]+(n*(n-1) if n>=3 else 0)
    marked=[0]*(nmax+1)
    for n in range(nmax+1):
        marked[n]=sum(comb(n,k)*delete_connected[k]*totals[n-k] for k in range(n+1))
    return totals,marked


def run():
    expected_graphs, expected_edits=exact_expected(6)
    tested_graphs=0; tested_valuations=0; tests_edit=0
    for n in range(7):
        edges=list(combinations(range(n),2))
        good=good_add=good_delete=0
        for bitset in range(1<<len(edges)):
            adj=adjacencies(n,bitset)
            valid=modal_valid(adj)
            classified=structure_valid(adj)
            assert valid==classified,(n,bitset,valid,classified)
            tested_graphs+=1
            tested_valuations+=1<<n
            if not valid:continue
            good+=1
            p_add,p_del=edit_predictions(adj)
            a=d=0
            for j in range(len(edges)):
                modified=adjacencies(n,bitset ^ (1<<j))
                if structure_valid(modified):
                    if (bitset>>j)&1: d+=1
                    else:a+=1
            assert (a,d)==(p_add,p_del),(n,bitset,(a,d),(p_add,p_del))
            good_add+=a;good_delete+=d
            tests_edit+=len(edges)
        assert (good,good_add,good_delete)==(expected_graphs[n],expected_edits[n],expected_edits[n]),(n,(good,good_add,good_delete),expected_graphs[n],expected_edits[n])
        print(f'n={n}: valid={good}, safe_add={good_add}, safe_del={good_delete}')
    print(f'VERIFY_OK graphs={tested_graphs} valuation_assignments={tested_valuations} edit_checks={tests_edit}')

if __name__=='__main__':run()
