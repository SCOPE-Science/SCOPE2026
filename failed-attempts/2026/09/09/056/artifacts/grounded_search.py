"""Heuristic search for grounded straight-segment realizations (target stress-test).
Model: base xi=i (order fixed by permutation p), tip (X_i,Y_i), Y>0.
Exact segment intersection via orientation predicates."""
import random, math, json

def seg_intersect(ax,ay,bx,by,cx,cy,dx,dy, tol=1e-9):
    # segments AB and CD: proper or endpoint touching counts as intersect,
    # but bases are distinct on y=0 so base-base never intersect.
    def orient(px,py,qx,qy,rx,ry):
        return (qx-px)*(ry-py)-(qy-py)*(rx-px)
    o1=orient(ax,ay,bx,by,cx,cy); o2=orient(ax,ay,bx,by,dx,dy)
    o3=orient(cx,cy,dx,dy,ax,ay); o4=orient(cx,cy,dx,dy,bx,by)
    # general case
    if o1*o2<0 and o3*o4<0: return True
    # collinear/touching cases with bounding box
    def on_seg(px,py,qx,qy,rx,ry):
        return min(px,rx)-tol<=qx<=max(px,rx)+tol and min(py,ry)-tol<=qy<=max(py,ry)+tol
    if abs(o1)<tol and on_seg(ax,ay,cx,cy,bx,by): return True
    if abs(o2)<tol and on_seg(ax,ay,dx,dy,bx,by): return True
    if abs(o3)<tol and on_seg(cx,cy,ax,ay,dx,dy): return True
    if abs(o4)<tol and on_seg(cx,cy,bx,by,dx,dy): return True
    return False

def score_of(tips, edges_set, n):
    # tips[i]=(X,Y); bases (i,0)
    score=0; bad=[]
    for i in range(n):
        for j in range(i+1,n):
            inter=seg_intersect(i,0,tips[i][0],tips[i][1], j,0,tips[j][0],tips[j][1])
            want=((i,j) in edges_set)
            if inter==want: score+=1
            else: bad.append((i,j,inter,want))
    return score, bad

def random_search(n, edges, iters=40000, seed=0):
    rng=random.Random(seed)
    edges_set=set(tuple(sorted(e)) for e in edges)
    total=n*(n-1)//2
    # init tips
    tips=[(rng.uniform(-2,n+2), rng.uniform(0.5,4)) for _ in range(n)]
    best,_=score_of(tips,edges_set,n)
    best_t=[t for t in tips]
    cur=[t for t in tips]; cur_s=best
    for it in range(iters):
        T=1.0/(1+it/2000)
        i=rng.randrange(n)
        old=cur[i]
        nx=old[0]+rng.gauss(0,0.7*(T+0.2)); ny=abs(old[1]+rng.gauss(0,0.5*(T+0.2)))+0.05
        cur[i]=(nx,ny)
        s,_=score_of(cur,edges_set,n)
        if s>=cur_s or rng.random()<math.exp((s-cur_s)/max(T,0.05)):
            cur_s=s
            if s>best:
                best=s; best_t=[t for t in cur]
                if best==total: break
        else:
            cur[i]=old
    return best,total,best_t

if __name__=="__main__":
    import sys
    arch=json.load(open("output/artifacts/mycielski_adj.json"))
    for name in ["M4","M5"]:
        E=[tuple(e) for e in arch[name]["edges"]]; n=arch[name]["n"]
        print(f"== {name} n={n} m={len(E)} ==", flush=True)
        for seed in range(6):
            b,t, tips=random_search(n,E,iters=15000,seed=seed)
            print(f" seed {seed}: {b}/{t}  ({100*b/t:.1f}%)", flush=True)
