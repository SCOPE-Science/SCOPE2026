"""Substep 4: Whitehead data + periodic directions + homology trace for pair1.
Pair1 (verified automorphisms in check_auto2.py):
  phi: a1->a2,a2->a3,a3->a4,a4->a5,a5->a1a2a3
  psi: a1->a2,a2->a3,a3->a4,a4->a5,a5->a1a3a2
"""
import numpy as np, sympy as sp, json
def inv(d): return d+5 if d<5 else d-5
def neg(w): return tuple(inv(d) for d in reversed(w))
def red(w):
    st=[]
    for d in w:
        if st and st[-1]==inv(d): st.pop()
        else: st.append(d)
    return tuple(st)
def show(d): return ('a' if d<5 else 'A')+str((d%5)+1)
def apply(f,w):
    out=[]
    for d in w:
        out.extend(f[d] if d<5 else neg(f[d-5]))
    return red(tuple(out))
f_phi={0:(1,),1:(2,),2:(3,),3:(4,),4:(0,1,2)}
f_psi={0:(1,),1:(2,),2:(3,),3:(4,),4:(0,2,1)}
def Df(f,d): return f[d][0] if d<5 else neg(f[d-5])[-1]
def turns_of(f):
    # taken turns: adjacent direction pairs inside f^k(e) for k=1..6 (stable), as unordered pairs
    cur={i:tuple(f[i]) for i in range(5)}
    taken=set()
    for k in range(6):
        for i in range(5):
            w=cur[i]
            for a,b in zip(w,w[1:]):
                taken.add(tuple(sorted((inv(a),b))))
        cur={i:apply(f,cur[i]) for i in range(5)}
    return taken
def periodic(f):
    per=[]
    for d in range(10):
        x=d
        for k in range(1,11):
            x=Df(f,x)
            if x==d: per.append((d,k)); break
    return per
for f,nm in [(f_phi,'phi'),(f_psi,'psi')]:
    imgs={d:Df(f,d) for d in range(10)}
    print(nm,'Df:',{show(k):show(v) for k,v in imgs.items()})
    # illegal turns: pairs mapping to same
    from collections import defaultdict
    col=defaultdict(list)
    for d in range(10): col[imgs[d]].append(d)
    ill={tuple(sorted(v)) for v in col.values() if len(v)>1}
    print(nm,'illegal turns:',[[show(d) for d in t] for t in ill])
    per=periodic(f)
    print(nm,'periodic dirs:',sorted(show(d) for d,k in per),'count=',len(per))
    print(nm,'periods:',{show(d):k for d,k in per})
    tk=turns_of(f)
    print(nm,'#taken turns:',len(tk))
    # LW connectivity at vertex (all 10 directions, edges=taken turns)
    adj={d:set() for d in range(10)}
    for a,b in tk: adj[a].add(b); adj[b].add(a)
    seen={0}; st=[0]
    while st:
        x=st.pop()
        for y in adj[x]:
            if y not in seen: seen.add(y); st.append(y)
    print(nm,'LW connected:',len(seen)==10,'degs:',{show(d):len(adj[d]) for d in range(10)})
    # stable taken turns among periodic dirs only
    P=set(d for d,k in per)
    stk=[t for t in tk if t[0] in P and t[1] in P]
    print(nm,'stable taken turns:',len(stk),sorted([[show(a),show(b)] for a,b in stk]))
M=[[0,0,0,0,1],[1,0,0,0,1],[0,1,0,0,1],[0,0,1,0,0],[0,0,0,1,0]]
Mm=sp.Matrix(M)
print('charpoly:',Mm.charpoly(sp.symbols('x')).as_expr())
print('factor:',sp.factor(Mm.charpoly(sp.symbols('x')).as_expr()))
print('trace M:',Mm.trace(),'trace M^-1:',Mm.inv().trace())
print('det:',Mm.det())
Mn=np.array(M); print('M^8>0:',bool(((np.linalg.matrix_power(Mn,8))>0).all()))
json.dump({'M':M,'trace':0,'trace_inv':int(Mm.inv().trace())},
          open('output/artifacts/matrix_data.json','w'))
