"""Strong SA optimizer for grounded-segment M4 realization. Variables: base b_i, tip (X_i,Y_i)."""
import random, math, json, sys, time

def orient(ax,ay,bx,by,cx,cy):
    return (bx-ax)*(cy-ay)-(by-ay)*(cx-ax)

def segs_hit(a,b,c,d):
    o1=orient(a[0],a[1],b[0],b[1],c[0],c[1]); o2=orient(a[0],a[1],b[0],b[1],d[0],d[1])
    o3=orient(c[0],c[1],d[0],d[1],a[0],a[1]); o4=orient(c[0],c[1],d[0],d[1],b[0],b[1])
    if o1*o2<0 and o3*o4<0: return True
    tol=1e-12
    def on(p,q,r):
        return min(p[0],r[0])-tol<=q[0]<=max(p[0],r[0])+tol and min(p[1],r[1])-tol<=q[1]<=max(p[1],r[1])+tol
    if abs(o1)<tol and on(a,c,b): return True
    if abs(o2)<tol and on(a,d,b): return True
    if abs(o3)<tol and on(c,a,d): return True
    if abs(o4)<tol and on(c,b,d): return True
    return False

def full_score(b, tips, Eset, n):
    pts=[[(b[i],0.0),tips[i]] for i in range(n)]
    s=0; bad=0
    for i in range(n):
        for j in range(i+1,n):
            h=segs_hit(pts[i][0],pts[i][1],pts[j][0],pts[j][1])
            if h==((i,j) in Eset): s+=1
            else: bad+=1
    return s

def anneal(n, Eset, iters, seed, init=None):
    rng=random.Random(seed)
    if init is None:
        b=[rng.uniform(0,10) for _ in range(n)]
        tips=[(rng.uniform(-3,13), rng.uniform(0.3,6)) for _ in range(n)]
    else:
        b,tips=init
        b=list(b); tips=list(tips)
    # enforce distinct bases by tiny jitter (order free)
    cur=full_score(b,tips,Eset,n)
    best=cur; bb=list(b); bt=list(tips)
    total=n*(n-1)//2
    for it in range(iters):
        T=max(0.02, 1.0-it/iters)
        i=rng.randrange(n)
        which=rng.random()
        ob=b[i]; ot=tips[i]
        if which<0.3:
            b[i]=ob+rng.gauss(0,0.9*T+0.05)
        else:
            nx=ot[0]+rng.gauss(0,(0.9*T+0.05)*(2 if which<0.65 else 0.5))
            ny=abs(ot[1]+rng.gauss(0,0.6*T+0.03))+0.05
            tips[i]=(nx,ny)
        # distinctness guard
        if min(abs(b[a]-b[c]) for a in range(n) for c in range(a+1,n))<1e-6:
            b[i]=ob; tips[i]=ot; continue
        s=full_score(b,tips,Eset,n)
        if s>=cur or rng.random()<math.exp((s-cur)/(T+0.05)):
            cur=s
            if s>best:
                best=s; bb=list(b); bt=list(tips)
                if best==total: break
        else:
            b[i]=ob; tips[i]=ot
    return best,total,bb,bt

if __name__=="__main__":
    arch=json.load(open("output/artifacts/mycielski_adj.json"))
    n=arch["M4"]["n"]; E=[tuple(e) for e in arch["M4"]["edges"]]
    Eset=set(tuple(sorted(e)) for e in E)
    t0=time.time(); budget=float(sys.argv[1]) if len(sys.argv)>1 else 240
    iters=int(sys.argv[2]) if len(sys.argv)>2 else 30000
    seed0=int(sys.argv[3]) if len(sys.argv)>3 else 0
    best=0; bs=None; k=0
    while time.time()-t0<budget:
        b,t,bb,bt=anneal(n,Eset,iters,seed0+k*7919)
        k+=1
        if b>best:
            best=b; bs=(bb,bt)
            print(f"[{time.time()-t0:.0f}s] restart {k}: new best {b}/{t} ({100*b/t:.1f}%)", flush=True)
            json.dump({"b":bb,"tips":bt,"score":[b,t]}, open("output/artifacts/m4_best.json","w"))
        if best==t:
            print("PERFECT FOUND"); break
    print(f"DONE {k} restarts best={best}/{t}")
