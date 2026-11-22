"""Independent finite checks for a dicyclic endomorphism orbit formula."""
from math import gcd
from collections import Counter


def mul(x, y, n):
    a, b = x; c, d = y
    return ((a + (c if b == 0 else -c) + n*b*d) % (2*n), b ^ d)


def power(x, k, n):
    z = (0, 0)
    while k:
        if k % 2: z = mul(z, x, n)
        x = mul(x, x, n); k //= 2
    return z


def endos(n):
    elems = [(a, b) for b in range(2) for a in range(2*n)]
    out = set()
    for x in elems:
        if power(x, 2*n, n) != (0, 0): continue
        for y in elems:
            if power(y, 2, n) != power(x, n, n): continue
            if mul(y, x, n) != mul(power(x, 2*n-1, n), y, n): continue
            out.add((x, y))
    return out


def cases(n):
    e = 0;h = n
    while h % 2 == 0: h //= 2;e += 1
    caseA = {((u, 0), (v, 1)) for u in range(1, 2*n, 2) for v in range(2*n)}
    caseC = {((0, 0), (0, 0)), ((0, 0), (n, 0))}
    if e:
        caseC |= {((n, 0), (0, 0)), ((n, 0), (n, 0))}
    caseX = set()
    if e == 1:
        for u in range(2*n):
            x = (u, 1)
            for y in ((n//2, 0), (3*n//2, 0), ((u+n//2) % (2*n), 1), ((u+3*n//2) % (2*n), 1)):
                caseX.add((x, y))
    return caseA, caseC, caseX


def apply_alpha(g, r, s, n):
    a,b = g
    return ((r*a+s*b)%(2*n),b)


def conj(f, r, s, n):
    x, y = f
    t = pow(r, -1, 2*n)
    new_x = power(x, t, n)
    new_y = mul(power(x, (-s*t) % (2*n), n), y, n)
    return (apply_alpha(new_x, r, s, n), apply_alpha(new_y, r, s, n))


def orbit_partition(n, E, all_alphas):
    left=set(E);out=[]
    while left:
        x=next(iter(left))
        orb = {conj(x, r, s, n) for (r, s) in all_alphas}
        assert orb <= left, (n, x, len(orb-left))
        left-=orb
        out.append(orb)
    return out


def dsigma(n): return sum(k for k in range(1,n+1) if n%k==0)
def dtau(n): return sum(1 for k in range(1,n+1) if n%k==0)
def totient(n): return sum(gcd(k,n)==1 for k in range(1,n+1))

def calc_claim(n):
    if n == 2: return 7
    h=n;e=0
    while h%2==0: e+=1;h//=2
    return (3*2**e-1)*dsigma(h) + 2 + (e>0) + 3*(e==1)


def subgroup_order(n, f):
    x,y=f; seen={(0,0)}; frontier=[(0,0)]
    while frontier:
        z=frontier.pop()
        for a in (x,y):
            t=mul(z,a,n)
            if t not in seen:
                seen.add(t);frontier.append(t)
    return len(seen)


def predicted_rank_orbit_poly(n):
    if n==2:return {1:1,2:1,8:5}
    out=Counter({1:1,2:1+(n%2==0)})
    for u in range(1,2*n,2):
        d=gcd(u-1,2*n)
        out[4*n//gcd(u,n)] += dtau(d)
    if n%4==2:out[8]+=3
    return dict(out)


def verify(N=12):
    for n in range(2,N+1):
        a,c,x=cases(n); E=endos(n)
        assert not (a & c or a & x or c & x)
        assert E == a|c|x, (n, len(E), len(a|c|x), E-(a|c|x))
        alphas=[(r,s) for r in range(2*n) if gcd(r,2*n)==1 for s in range(2*n)]
        if n==2:
            # Q8 has six automorphisms permuting its three order-four subgroups.
            # Enumerate all 24 generator-image pairs, not only the affine subgroup.
            aut = {(p,q) for p,q in E if len({power(p,k,n) for k in range(4)} | {mul(power(p,k,n),q,n) for k in range(4)})==8}
            assert len(aut)==24
            alpha_maps=[]
            for p,q in aut:
                mapping={};aa=(1,0); bb=(0,1)
                for i in range(2*n):
                    mapping[(i,0)] = power(p,i,n)
                    mapping[(i,1)] = mul(power(p,i,n),q,n)
                inverse={v:k for k,v in mapping.items()}
                assert len(inverse)==4*n
                alpha_maps.append((mapping,inverse))
            left=E.copy();parts=[]
            while left:
                f=next(iter(left));orb=set()
                for amap,ainv in alpha_maps:
                    pre_a=ainv[(1,0)];pre_b=ainv[(0,1)]
                    def F(t):
                        i,j=t;return mul(power(f[0],i,n),power(f[1],j,n),n)
                    orb.add((amap[F(pre_a)],amap[F(pre_b)]))
                assert orb<=left
                parts.append(orb);left-=orb
            assert len(parts)==7
        else:
            parts=orbit_partition(n,E,alphas)
            assert len(parts)==calc_claim(n), (n,len(parts),calc_claim(n))
            classA=orbit_partition(n,a,alphas)
            classC=orbit_partition(n,c,alphas)
            classX=orbit_partition(n,x,alphas)
            assert len(classA)==sum(dtau(gcd(1-u,2*n)) for u in range(1,2*n,2))
            assert len(classC)==(2+(n%2==0))
            if n%4==2: assert sorted(map(len,classX))==[2*n,2*n,4*n],(n,sorted(map(len,classX)))
            else: assert len(classX)==0
            for (u0,v0) in a:
                d=gcd(1-u0[0],2*n)
                sig=gcd(v0[0],d)
                orb={conj((u0,v0),r,s,n) for r,s in alphas}
                assert len(orb) == (2*n//d)*totient(d//sig),(n,u0,v0,d,sig,len(orb))
                assert all(w[0]==u0 and gcd(w[1][0],d)==sig for w in orb)
        actual_rank_counts=Counter({subgroup_order(n,next(iter(orb))):0 for orb in parts})
        for orb in parts:actual_rank_counts[subgroup_order(n,next(iter(orb)))]+=1
        assert dict(actual_rank_counts)==predicted_rank_orbit_poly(n),(n,actual_rank_counts,predicted_rank_orbit_poly(n))
        print(f'n={n}: rank_orbit={dict(sorted(actual_rank_counts.items()))}; End={len(E)} Aut={len(alphas) if n>2 else 24} orbit={len(parts)} sizes={dict(sorted(Counter(map(len,parts)).items()))}')
    print('DICYCLIC_FULL_ENDOMORPHISM_ORBIT_CHECKS_PASSED')

if __name__=='__main__':verify()
