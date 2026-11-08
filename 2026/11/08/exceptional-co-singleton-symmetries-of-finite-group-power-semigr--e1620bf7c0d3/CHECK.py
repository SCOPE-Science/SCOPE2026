#!/usr/bin/env python3
"""Finite multiplication-table checks for co-singleton power-semigroup symmetries."""
from itertools import combinations, permutations


def cyclic(n):
    return [[(a+b) % n for b in range(n)] for a in range(n)]


def elementary_binary(d):
    n = 1 << d
    return [[a ^ b for b in range(n)] for a in range(n)]


def symmetric_three():
    items=list(permutations(range(3)))
    ix={p:i for i,p in enumerate(items)}
    mul=[[ix[tuple(a[b[j]] for j in range(3))] for b in items] for a in items]
    e=ix[(0,1,2)]
    # Put identity first and relabel multiplication table.
    order=[e]+[i for i in range(6) if i!=e]
    reverse={old:i for i,old in enumerate(order)}
    return [[reverse[mul[order[i]][order[j]]] for j in range(6)] for i in range(6)]


def multiply(table, x, y):
    n=len(table)
    acc=0
    for i in range(n):
        if (x >> i) & 1:
            for j in range(n):
                if (y >> j) & 1:
                    acc|=1 << table[i][j]
    return acc


def count_factorizations(table):
    n=len(table)
    all_mask=(1 << n)-1
    sets=[x for x in range(1,all_mask) if x.bit_count() >= 2]
    achieved={multiply(table,x,y) for x in sets for y in sets}
    return sum((all_mask ^ (1 << g)) in achieved for g in range(n))


def shifts(table):
    n=len(table); full=(1 << n)-1
    def transform(z,x):
        if x.bit_count()!=n-1:
            return x
        missing=next(i for i in range(n) if not ((x >> i)&1))
        return full ^ (1 << table[missing][z])
    for z in range(n):
        vals=[transform(z,x) for x in range(1,full+1)]
        assert len(set(vals))==full
        for x in range(1,full+1):
            for y in range(1,full+1):
                assert transform(z,multiply(table,x,y)) == multiply(table,transform(z,x),transform(z,y))
    return n


def automorphisms(table):
    n=len(table)
    autos=[]
    for tail in permutations(range(1,n)):
        p=(0,)+tail
        if all(p[table[a][b]]==table[p[a]][p[b]] for a in range(n) for b in range(n)):
            autos.append(p)
    return autos


def check_lifted(table):
    n=len(table); full=(1 << n)-1
    found=set()
    for p in automorphisms(table):
        for z in range(n):
            def lift(x):
                y=0
                for i in range(n):
                    if (x>>i)&1: y|=1 << p[i]
                if x.bit_count()==n-1:
                    missing=next(i for i in range(n) if not ((x>>i)&1))
                    y=full ^ (1<<table[p[missing]][z])
                return y
            vals=tuple(lift(x) for x in range(1,full+1))
            assert len(set(vals))==full
            assert vals not in found
            found.add(vals)
            for x in range(1,full+1):
                for y in range(1,full+1):
                    assert lift(multiply(table,x,y))==multiply(table,lift(x),lift(y))
    return len(found)


def main():
    data=[('C2',cyclic(2)), ('C3',cyclic(3)), ('V4',elementary_binary(2)),
          ('C4',cyclic(4)),('C5',cyclic(5)),('C6',cyclic(6)),
          ('S3',symmetric_three()),('C7',cyclic(7)),('E8',elementary_binary(3)),('C8',cyclic(8))]
    for name,table in data:
        n=len(table)
        decomposable=count_factorizations(table)
        expected=0 if name in ['C2','C3','V4'] else n
        assert decomposable==expected,(name,decomposable,expected)
        print(f'{name:3s} order={n} decomposable_co_singletons={decomposable}/{n}')
    for name,table,total in [('C3',cyclic(3),6),('V4',elementary_binary(2),24)]:
        assert shifts(table)==len(table)
        count=check_lifted(table)
        assert count==total
        print(f'{name}: explicit_distinct_power_automorphisms={count}')
    print('VERIFY_OK')

if __name__=='__main__':main()
