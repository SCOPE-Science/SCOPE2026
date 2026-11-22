"""Independent Coxeter-group Cayley/BFS test of a closed 0-Hecke centralizer theorem.
Run: python3 dihedral_independent_check.py
Uses the group law of D_{2m}, shortest reduced words and Demazure ascent,
not the proposed alternating-word product formula.
"""
from collections import deque, Counter

def group_mul(x,y,m):
    a,e=x;b,f=y
    return ((a+(-1 if e else 1)*b)%m,e^f)

def test(m):
    identity=(0,0); generators={'s':(0,1),'t':(1,1)}
    reduced={identity:''}; queue=deque([identity])
    while queue:
        x=queue.popleft()
        for a,g in generators.items():
            z=group_mul(x,g,m)
            if z not in reduced:
                reduced[z]=reduced[x]+a
                queue.append(z)
    assert len(reduced)==2*m
    def star(x,y):
        z=x
        for a in reduced[y]:
            v=group_mul(z,generators[a],m)
            if len(reduced[v])>len(reduced[z]):z=v
        return z
    c={x:sum(star(x,y)==star(y,x) for y in reduced) for x in reduced}
    assert len(c)==2*m
    if m%2==0:
        k=m//2
        expect=10*k*k+6*k
        cen=4
        for x,word in reduced.items():
            length=len(word)
            p = 2*m if length in (0,m) else k+3*((length+1)//2)
            assert c[x]==p,(m,x,word,c[x],p)
    else:
        k=(m-1)//2
        expect=10*k*k+12*k+4
        cen=2
        for x,word in reduced.items():
            length=len(word)
            p=2*m if length in (0,m) else k+3*((length+1)//2)-(length%2)
            assert c[x]==p,(m,x,word,c[x],p)
    assert sum(c.values())==expect,(m,sum(c.values()),expect)
    assert sum(v==2*m for v in c.values())==cen
    return m,len(c),expect,cen,sorted(Counter(c.values()).items())

if __name__=='__main__':
    for m in range(3,65):
        r=test(m)
        if m<=12 or m in [15,16,17,31,32,33,63,64]:
            print('m=%d elements=%d commuting_pairs=%d center=%d spectrum=%s' % r)
    print('PASS: independent dihedral group/BFS and Demazure multiplication, all m=3..64')
