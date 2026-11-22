"""Directly check the displayed two-cycle witness without any external packages."""
p = 11
c1 = (0,1,2,8,3,4,5,10,6,7,9)
c2 = (0,1,2,10,3,4,5,9,6,7,8)
def signature(c,k):
    assert len(c) == p and sorted(c) == list(range(p))
    f = dict(zip(c,c[1:]+c[:1]))
    x = list(range(p))
    rows = []
    for t in range(1,k+1):
        x = [f[y] for y in x]
        rows.append(tuple(int(x[j]>j) for j in range(p)))
    return rows
u,v=signature(c1,7),signature(c2,7)
assert c1!=c2 and u[:6]==v[:6] and u[6]!=v[6]
print('WITNESS PASS: first six direction rows agree; seventh differs')
print('interior six-step rows:',*(''.join(map(str,row[1:-1])) for row in u[:6]),sep='\n')
print('seventh interior rows:', ''.join(map(str,u[6][1:-1])), ''.join(map(str,v[6][1:-1])))
