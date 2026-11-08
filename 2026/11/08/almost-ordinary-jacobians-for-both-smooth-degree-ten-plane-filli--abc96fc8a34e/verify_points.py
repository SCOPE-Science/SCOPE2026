"""Two independent GF(49) models and exhaustive projective point counts.

Use: python3 verify_points.py. GF(49) = GF(7)[u]/(u^2-c), with c=6 or c=3.
Neither c is a square in GF(7). Each count includes the points at infinity.
"""
P=7
N=49
ONE=7

def count(c,k):
    def mul(u,v):
        a,b=divmod(u,7); x,y=divmod(v,7)
        return ((a*x+c*b*y)%7)*7+(a*y+b*x)%7
    def add(u,v):
        a,b=divmod(u,7); x,y=divmod(v,7)
        return ((a+x)%7)*7+(b+y)%7
    def sub(u,v):
        a,b=divmod(u,7); x,y=divmod(v,7)
        return ((a-x)%7)*7+(b-y)%7
    table=[[mul(a,b) for b in range(N)] for a in range(N)]
    def pow7(a):
        r=ONE
        for _ in range(7):r=table[r][a]
        return r
    squares=[table[a][a] for a in range(N)]
    seventh=[pow7(a) for a in range(N)]
    kk=7*k
    def F(x,y,z):
        term1=table[squares[x]][sub(table[seventh[x]][y],table[x][seventh[y]])]
        term2=table[squares[y]][sub(table[seventh[y]][z],table[y][seventh[z]])]
        factor=add(squares[z],table[kk][squares[x]])
        term3=table[factor][sub(table[seventh[z]][x],table[z][seventh[x]])]
        return add(add(term1,term2),term3)
    affine=sum(F(x,y,ONE)==0 for x in range(N) for y in range(N))
    infinity=sum(F(ONE,y,0)==0 for y in range(N))+int(F(0,ONE,0)==0)
    return affine,infinity,affine+infinity

def main():
    for k in [1,3]:
        counts=[count(c,k) for c in [6,3]]
        expected=103 if k==1 else 107
        assert counts[0]==counts[1]
        assert counts[0][2]==expected
        print('POINT_COUNT_F49_PASS',k,counts[0])
    print('DISTINCT_ZETA_AND_F7_ISOGENY_CLASSES_PASS')
if __name__=='__main__':main()
