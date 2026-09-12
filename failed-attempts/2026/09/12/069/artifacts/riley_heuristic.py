"""Bounded test: Riley-type SL(2,C) representation of certified 2-gen presentation,
then longitude search among null-homologous words centralizing meridian."""
import cmath
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
A=[(0,1)]; B=[(2,1)]
# certified relators from cert1229b (x0->a, x2->b)
s0_str="a b A B a b A b a B A A"  # placeholder, replaced below
# rebuild exactly: s0 = subst(r0), s2 = subst(r2)
def W3(s):
    m={'x0':(0,1),'x1':(1,1),'x2':(2,1),'X0':(0,-1),'X1':(1,-1),'X2':(2,-1)}
    return [m[t] for t in s.split()]
r0=W3("x0 x2 X0 X2 x1 x2 x0 X2 X0 X0")
r2=W3("X2 X1 x2 x0 X2 x1")
x1s=[(0,1),(2,1),(0,-1)]; X1s=inv(x1s)
def subst(w):
    out=[]
    for g,e in w:
        if g==1: out.extend(x1s if e==1 else X1s)
        else: out.append((g,e))
    return red(out)
s0=subst(r0); s2=subst(r2)
print("s0=",wstr(s0)); print("s2=",wstr(s2))
def mm(X,Y): return [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]],[X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]]]
def mi(X):
    d=X[0][0]*X[1][1]-X[0][1]*X[1][0]
    return [[X[1][1]/d,-X[0][1]/d],[-X[1][0]/d,X[0][0]/d]]
def weval(w,MA,MB):
    M=[[1,0],[0,1]]
    for (g,e) in w:
        G=MA if g==0 else MB
        if e==-1: G=mi(G)
        M=mm(M,G)
    return M
def err(w,MA,MB):
    M=weval(w,MA,MB)
    return abs(M[0][0]-1)+abs(M[0][1])+abs(M[1][0])+abs(M[1][1]-1)
MA=[[1,1],[0,1]]
# Riley ansatz MB=[[1,0],[w,1]]; scan w on grid for err(s0)+err(s2)
best=None
N=160
for i in range(-N,N+1):
    for j in range(-N,N+1):
        w=complex(i*0.05,j*0.05)
        MB=[[1,0],[w,1]]
        e=err(s0,MA,MB)+err(s2,MA,MB)
        if best is None or e<best[0]: best=(e,w)
print("grid best:",best)
# Newton refine on stacked residual vector
def resid(w):
    MB=[[1,0],[w,1]]
    out=[]
    for r in (s0,s2):
        M=weval(r,MA,MB)
        out += [M[0][0]-1,M[0][1],M[1][0],M[1][1]-1]
    return out
w=best[1]
for it in range(200):
    R=resid(w); n=sum(abs(v)**2 for v in R)
    if n<1e-28: break
    h=1e-7
    R2=resid(w+h); J=[(a-b)/h for a,b in zip(R2,R)]
    # Gauss-Newton step
    num=sum((x.conjugate()*y).real for x,y in zip(J,R)) # not complex-correct; use Wirtinger-ish: try 4 real dirs
    import numpy as np
    Jn=np.array([[z.real,z.imag] for z in J])  # 8x2 real jacobian
    Rn=np.array([z.real for z in R]+[z.imag for z in R])
    Jn2=np.vstack([Jn[:8,0],Jn[:8,1]])  # careful: build properly below
    break
# simpler: real 2-param Newton with explicit 16x2 Jacobian
import numpy as np
w=best[1]
for it in range(100):
    R=resid(w)
    f=np.array([z.real for z in R]+[z.imag for z in R])
    if float(f@f)<1e-30: break
    h=1e-7
    Ra=resid(complex(w.real+h,w.imag)); Rb=resid(complex(w.real,w.imag+h))
    Ja=np.array([z.real for z in Ra]+[z.imag for z in Ra]); Ja=(Ja-f)/h
    Jb=np.array([z.real for z in Rb]+[z.imag for z in Rb]); Jb=(Jb-f)/h
    J=np.column_stack([Ja,Jb])
    step,_,_,_=np.linalg.lstsq(J,-f,rcond=None)
    w=complex(w.real+step[0],w.imag+step[1])
print("newton w=",w,"resid norm:",float(np.array([z.real for z in resid(w)]+ [z.imag for z in resid(w)])@np.array([z.real for z in resid(w)]+[z.imag for z in resid(w)])))
MB=[[1,0],[w,1]]
print("err s0:",err(s0,MA,MB),"err s2:",err(s2,MA,MB))
print("w satisfies? w^2+... :",w)
