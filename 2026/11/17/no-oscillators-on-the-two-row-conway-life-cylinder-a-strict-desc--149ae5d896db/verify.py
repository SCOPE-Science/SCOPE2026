"""Exact finite checks for B3/S23 on two-row open-vertical cylinders.
Run: python3 verify.py . No nonstandard Python modules are required.
The all-size convergence assertion is proved separately, not inferred from enumeration.
"""
import json


def bitcount(s):
    return s.bit_count()


def direct_step(state, h, n):
    ans = 0
    for row in range(h):
        for col in range(n):
            neighbours = 0
            for dr in (-1, 0, 1):
                rr = row + dr
                if not (0 <= rr < h):
                    continue
                for dc in (-1, 0, 1):
                    if dr == dc == 0:
                        continue
                    cc = (col + dc) % n
                    neighbours += (state >> (n*rr+cc)) & 1
            on = (state >> (n*row+col)) & 1
            if neighbours == 3 or (on and neighbours == 2):
                ans |= 1 << (n*row+col)
    return ans


def col_rule(a,b,c):
    # Column encoding 0=00,1=10,2=01,3=11, least significant bit top.
    neighbour_sum = bitcount(a) + bitcount(c)
    out=0
    for row in (0,1):
        old=(b>>row)&1
        neigh=neighbour_sum+((b>>(1-row))&1)
        if neigh==3 or (old and neigh==2):
            out |= 1<<row
    return out


def col_step(state,n):
    cols=[((state>>j)&1) | (((state>>(n+j))&1)<<1) for j in range(n)]
    out=[col_rule(cols[(j-1)%n],cols[j],cols[(j+1)%n]) for j in range(n)]
    return sum(((a&1)<<j) | (((a>>1)&1)<<(n+j)) for j,a in enumerate(out))


def potential(state,n):
    sing=doub=0
    for j in range(n):
        s=((state>>j)&1) + ((state>>(n+j))&1)
        sing += s==1; doub += s==2
    return (n+1)*sing+doub


def transfer():
    t=[[0]*16 for _ in range(16)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                if col_rule(a,b,c)==b:
                    t[4*a+b][4*b+c]=1
    return t


def multiply(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def char_det_izt(t):
    # Newton identities with exact integer coefficients.
    n=len(t); cur=[[int(i==j) for j in range(n)] for i in range(n)]
    power_sums=[]
    for j in range(1,n+1):
        cur=multiply(cur,t)
        power_sums.append(sum(cur[i][i] for i in range(n)))
    c=[1]
    for k in range(1,n+1):
        numer=-sum(c[k-j]*power_sums[j-1] for j in range(1,k+1))
        assert numer%k==0
        c.append(numer//k)
    return c, power_sums


def main():
    matrix=transfer()
    coeff, traces=char_det_izt(matrix)
    assert coeff==[1,-1,0,-5,4,-4,4]+[0]*10,coeff
    assert sum(map(sum,matrix))==30
    all_counts=[]
    for n in range(3,9):
        fixed=0
        for state in range(1<<(2*n)):
            after=direct_step(state,2,n)
            assert after==col_step(state,n),(n,state)
            assert after==state or potential(after,n)<potential(state,n),(n,state)
            fixed+=after==state
        assert fixed==traces[n-1],(n,fixed,traces[n-1])
        all_counts.append([n,fixed])
    assert all_counts==[[3,16],[4,5],[5,26],[6,82],[7,43],[8,213]]
    # One-row dynamics has no births (at most two live neighbours).
    for n in range(3,9):
        for s in range(1<<n):
            y=direct_step(s,1,n)
            assert (s|y)==s
    n=4
    x=sum(1<<(n+1+j) for j in range(3))  # central row, columns 1,2,3
    y=direct_step(x,3,n)
    z=direct_step(y,3,n)
    assert x!=y and z==x
    assert y==(1<<2)|(1<<(n+2))|(1<<(2*n+2))
    print(json.dumps({"width2_det_coefficients_ascending":coeff,
                      "width2_transfer_edges":30,
                      "fixed_counts_n3_to_n8":all_counts,
                      "width2_transition_cases_checked":sum(1<<(2*n) for n in range(3,9)),
                      "width3_period_two_witness":{"n":4,"first":x,"second":y},
                      "all_tests":"PASS"},sort_keys=True))


if __name__=='__main__':
    main()
