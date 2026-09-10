#!/usr/bin/env python3
"""R1b: general minimal-resolution engine for Ext_A^{s,t}(H^*V(1),F3) to t<=41, s<=3.

Strategy: work degree-by-degree in the augmentation ideal basis; free modules
recorded as {gen: } with A-basis monomials enumerated directly up to degree
DMAX=41 (fast: only ~hundreds of admissible monomials). Syzygies via linear
algebra over F3 in each internal degree. s=0..3, t<=41. Reports ranks
Ext^{s,t} for s in {6,8} neighborhood if reached, else diagnoses cost blowup.

To keep the run bounded: degree cap for A-monomials D=41; the F_k expanded
bases in degree t are |gens_k| x (#adm monos of deg t-g). Abort with a
machine-measured cost report if dim exceeds CAP=4000 in any degree.
"""
import json, math, time, sys
P = 3
t0 = time.time()
B = ('B',)
def Pp(i): return ('P', i)
def df(f): return 1 if f[0]=='B' else 4*f[1]
def dm(m): return sum(df(f) for f in m)
def binom_neg(n,k):
    if k<0: return 0
    if n<0: return 1 if k==0 else 0
    r=1; nn,kk=n,k
    while nn>0 or kk>0:
        ni,ki=nn%P,kk%P
        if ki>ni: return 0
        r=(r*(math.comb(ni,ki)%P))%P
        nn//=P; kk//=P
    return r
def addvec(a,b):
    c=dict(a)
    for k,v in b.items():
        c[k]=(c.get(k,0)+v)%P
        if c[k]==0: del c[k]
    return c
def is_adm(m):
    n=len(m); i=0
    while i<n:
        f=m[i]
        if f[0]=='B':
            if i+1<n and m[i+1][0]=='B': return False
            i+=1
        else:
            a=f[1]
            if i+1<n and m[i+1][0]=='P':
                if a<P*m[i+1][1]: return False
                i+=1
            elif i+1<n and m[i+1][0]=='B':
                if i+2<n and m[i+2][0]=='P':
                    if a<=P*m[i+2][1]: return False
                    i+=2
                else: i+=1
            else: i+=1
        return True
def adem_PP(a,b):
    out={}; t=0
    while P*t<=a:
        c=(((-1)**(a+t))*binom_neg((P-1)*(b-t)-1,a-P*t))%P
        if c:
            m=[]
            if a+b-t>0: m.append(Pp(a+b-t))
            if t>0: m.append(Pp(t))
            m=tuple(m); out[m]=(out.get(m,0)+c)%P
            if out[m]==0: del out[m]
        t+=1
    return out
def adem_PbP(a,b):
    out={}; t=0
    while P*t<=a:
        c=(((-1)**(a+t))*binom_neg((P-1)*(b-t)-1,a-P*t))%P
        if c:
            m=[B]
            if a+b-t>0: m.append(Pp(a+b-t))
            if t>0: m.append(Pp(t))
            m=tuple(m); out[m]=(out.get(m,0)+c)%P
            if out[m]==0: del out[m]
        t+=1
    return out
def reduce_once(vec,cap=200000):
    out={}; work=dict(vec); steps=0
    while work:
        if steps>cap: raise RuntimeError('rewrite cap')
        steps+=1
        m,c=work.popitem()
        if c%P==0: continue
        c%=P
        m=tuple(f for f in m if not (f[0]=='P' and f[1]==0))
        if any(m[i][0]=='B' and i+1<len(m) and m[i+1][0]=='B' for i in range(len(m)-1)):
            continue
        if is_adm(m):
            out[m]=(out.get(m,0)+c)%P
            if out[m]==0: del out[m]
            continue
        n=len(m); done=False; i=0
        while i<n:
            f=m[i]
            if f[0]=='P':
                a=f[1]
                if i+1<n and m[i+1][0]=='P' and a<P*m[i+1][1]:
                    exp=adem_PP(a,m[i+1][1]); pre,post=m[:i],m[i+2:]
                    for rm,rc in exp.items():
                        key=tuple(list(pre)+list(rm)+list(post))
                        work[key]=(work.get(key,0)+c*rc)%P
                    done=True; break
                elif (i+1<n and m[i+1][0]=='B' and i+2<n and m[i+2][0]=='P'
                      and a>=1 and a<=P*m[i+2][1]):
                    exp=adem_PbP(a,m[i+2][1]); pre,post=m[:i],m[i+3:]
                    for rm,rc in exp.items():
                        key=tuple(list(pre)+list(rm)+list(post))
                        work[key]=(work.get(key,0)+c*rc)%P
                    done=True; break
            i+=1
        if not done: raise RuntimeError(f'stuck {m}')
    return {k:v for k,v in out.items() if v%P!=0}

DMAX=41
# direct admissible enumeration by BFS on (last-constraint) — simpler: DFS with pruning
adm_by_deg={d:[] for d in range(DMAX+1)}
adm_by_deg[0]=[()]
def extends_ok(m,g):
    # check admissibility of pair-boundary only (suffix): full check cheap anyway
    return is_adm(m+(g,))
def gens_for(m):
    # candidate next factors with degree bound; P^i, i>=1, plus B
    out=[B]
    i=1
    while 4*i<=DMAX: out.append(Pp(i)); i+=1
    return out
# DFS
stack=[()]
seen={():0}
while stack:
    m=stack.pop()
    d=dm(m)
    for g in gens_for(m):
        if d+df(g)>DMAX: continue
        m2=m+(g,)
        if m2 in seen: continue
        if not is_adm(m2): continue
        seen[m2]=dm(m2)
        adm_by_deg[dm(m2)].append(m2)
        stack.append(m2)
counts={d:len(v) for d,v in adm_by_deg.items()}
total=sum(counts.values())
print(json.dumps({'admissible_counts':counts,'total':total,'time_s':round(time.time()-t0,1)}))
