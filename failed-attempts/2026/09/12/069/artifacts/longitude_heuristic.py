"""Search null-homologous words centralizing meridian in certified rep; report +1-filling centrality."""
import numpy as np, itertools
def red(w):
    st=[]
    for g,e in w:
        if st and st[-1][0]==g and st[-1][1]==-e: st.pop()
        else: st.append((g,e))
    return st
def mul(*ws):
    out=[]
    for w in ws: out.extend(w)
    return red(out)
def inv(w): return [(g,-e) for (g,e) in reversed(w)]
def wstr(w):
    d={(0,1):'a',(2,1):'b',(0,-1):'A',(2,-1):'B'}
    return ''.join(d[t] for t in w) or '1'
def W3(s):
    m={'x0':(0,1),'x1':(1,1),'x2':(2,1),'X0':(0,-1),'X1':(1,-1),'X2':(2,-1)}
    return [m[t] for t in s.split()]
r0=W3("x0 x2 X0 X2 x1 x2 x0 X2 X0 X0"); r2=W3("X2 X1 x2 x0 X2 x1")
x1s=[(0,1),(2,1),(0,-1)]; X1s=inv(x1s)
def subst(w):
    out=[]
    for g,e in w:
        if g==1: out.extend(x1s if e==1 else X1s)
        else: out.append((g,e))
    return red(out)
s0=subst(r0); s2=subst(r2)
w0=complex(0.5,-0.8660254037844387)
MA=np.array([[1,1],[0,1]],dtype=complex); MB=np.array([[1,0],[w0,1]],dtype=complex)
def weval(w):
    M=np.eye(2,dtype=complex)
    for (g,e) in w:
        G=MA if g==0 else MB
        if e==-1: G=np.linalg.inv(G)
        M=M@G
    return M
def comm_norm(m,l):
    A=weval(m); B=weval(l)
    return float(abs(np.linalg.det(A))*0+np.sum(np.abs(A@B-B@A)))
m=[(0,1)]
# null-homologous: expsum_a=expsum_b=0
lets=[(0,1),(2,1),(0,-1),(2,-1)]
cands=[]
for L in (4,6,8):
    for tup in itertools.product(lets,repeat=L):
        w=red(list(tup))
        if len(w)!=L: continue
        if sum(e for g,e in w if g==0)!=0: continue
        if sum(e for g,e in w if g==2)!=0: continue
        c=comm_norm(m,w)
        if c<1e-9:
            t=complex(np.trace(weval(w)))
            cands.append((wstr(w),L,c,float(abs(t))))
    print("L=",L,"hits so far:",len(cands))
for c in cands[:20]: print(c)
