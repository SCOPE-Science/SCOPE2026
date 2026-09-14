import itertools

def ct(p):
    n=len(p); vis=[False]*n; lens=[]
    for i in range(n):
        if not vis[i]:
            j=i; l=0
            while not vis[j]:
                vis[j]=True; j=p[j]; l+=1
            lens.append(l)
    lens.sort(reverse=True); return tuple(lens)
def compose(a,b): return [a[b[i]] for i in range(len(a))]
def inv(p):
    q=[0]*len(p)
    for i,v in enumerate(p): q[v]=i
    return q
def cycstr(p):
    n=len(p); vis=[False]*n; out=[]
    for i in range(n):
        if not vis[i]:
            j=i; c=[]
            while not vis[j]:
                vis[j]=True; c.append(j); j=p[j]
            if len(c)>1: out.append(tuple(c))
    return out

u0=[1,2,3,0,5,6,4,8,7,10,9,11]
u1=[2,10,11,5,8,3,4,7,6,9,0,1]
uinf=inv(compose(u0,u1))
print("ct:",ct(u0),ct(u1),ct(uinf))
print("prod:",compose(compose(u0,u1),uinf))
print("u0:",cycstr(u0))
print("u1:",cycstr(u1))
print("uinf:",cycstr(uinf))
# parity
def sign(ct_):
    s=1
    for l in ct_:
        if (l-1)%2==1: s=-s
    return s
print("signs:",sign(ct(u0)),sign(ct(u1)),sign(ct(uinf)))
# transitivity
def orb(gens,start=0):
    seen={start}; st=[start]
    ig=[inv(g) for g in gens]
    while st:
        x=st.pop()
        for g in gens+ig:
            y=g[x]
            if y not in seen: seen.add(y); st.append(y)
    return seen
print("orbit size:",len(orb([u0,u1])))
# simultaneous centralizer in S12: elements c with c u0 = u0 c, c u1 = u1 c
# brute force 12! impossible; use backtracking search
import sys
sys.setrecursionlimit(10000)
n=12
def centralizer_size(gens):
    # backtrack c as bijection
    # constraints: c(g(x)) = g(c(x)) for g in gens
    count=0
    c=[-1]*n; cinv=[-1]*n
    # order: BFS
    order=list(range(n))
    def propagate():
        # closure under constraints given partial assignment; returns False if contradiction
        changed=True
        while changed:
            changed=False
            for g in gens:
                gi=inv(g)
                for x in range(n):
                    if c[x]!=-1:
                        y=g[x]
                        if c[y]==-1:
                            z=g[c[x]]
                            if cinv[z]!=-1 and cinv[z]!=y: return False
                            c[y]=z; cinv[z]=y; changed=True
                        else:
                            if c[y]!=g[c[x]]: return False
                    # also backward
                    if c[x]!=-1:
                        y=gi[x]
                        if c[y]==-1:
                            z=gi[c[x]]
                            if cinv[z]!=-1 and cinv[z]!=y: return False
                            c[y]=z; cinv[z]=y; changed=True
                        else:
                            if c[y]!=gi[c[x]]: return False
        return True
    # need recursive with state save
    def rec():
        nonlocal count
        # find first unassigned
        try: x=next(i for i in range(n) if c[i]==-1)
        except StopIteration:
            count+=1; return
        for z in range(n):
            if cinv[z]==-1:
                sc=list(c); si=list(cinv)
                c[x]=z; cinv[z]=x
                if propagate():
                    rec()
                # restore
                for i in range(n): c[i]=sc[i]; cinv[i]=si[i]
                # actually propagate may have assigned many; restore fully
        return
    if not propagate():
        return 0
    rec()
    return count
print("centralizer size:", centralizer_size([u0,u1]))
