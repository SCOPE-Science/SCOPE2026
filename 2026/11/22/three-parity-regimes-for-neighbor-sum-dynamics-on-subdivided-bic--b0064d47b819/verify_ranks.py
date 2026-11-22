#!/usr/bin/env python3
"""Independent bitset Gaussian elimination of adjacency powers for a subdivided biclique."""

def rank(rows, width):
    pivots = {}
    for value in rows:
        x=value
        while x:
            j=x.bit_length()-1
            if j not in pivots:
                pivots[j]=x
                break
            x ^= pivots[j]
    return len(pivots)

def multiply(rows, cols):
    # Rows of a binary matrix product, using row-index select.
    result=[]
    for x in rows:
        z=0
        while x:
            b=x&-x
            z ^= cols[b.bit_length()-1]
            x-=b
        result.append(z)
    return result

def expected(m,n):
    d=m+n+m*n
    if m%2==0 and n%2==0:
        return [d,2*(m+n-1),m+n,2,0],(d,0,0,0)
    if m%2 and n%2:
        p=2*(m+n-2)
        return [d,2*(m+n-1),2*(m+n)-3,p,p],(d-p,p,m+n-2,p)
    e,o=(m,n) if m%2==0 else (n,m)
    return [d,2*(m+n-1),2*e+o-1,2*e,2*e],(d-2*e,2*e,e-1,2*e-2)

def main():
    cases=0
    for m in range(2,9):
        for n in range(2,9):
            d=m+n+m*n
            rows=[0]*d
            for i in range(m):
                for j in range(n):
                    e=m+n+i*n+j
                    for v in (i,m+j):
                        rows[e] |=1<<v
                        rows[v] |=1<<e
            power=[1<<i for i in range(d)]
            ranks=[d]
            for t in range(1,5):
                power=multiply(rows,power)
                ranks.append(rank(power,d))
            exp,info=expected(m,n)
            assert ranks==exp, (m,n,ranks,exp)
            # Exact fixed-point dimensions via binary eliminations.
            recur=info[1]; fix1=info[2]; fix2=info[3]
            if not(m%2==0 and n%2==0):
                p=[1<<i for i in range(d)]
                for j in range(1,5):
                    p=multiply(rows,p)
                    if j in (1,2,4):
                        k=d-rank([p[i]^(1<<i) for i in range(d)],d)
                        target={1:fix1,2:fix2,4:recur}[j]
                        assert k==target, (m,n,j,k,target)
            else:
                assert all(x==0 for x in power)
            cases+=1
    print('RANK_CHECK_OK',cases,'matrix profiles', 'all ranks powers 0..4 and fixed subspace dimensions')

if __name__=='__main__':main()
