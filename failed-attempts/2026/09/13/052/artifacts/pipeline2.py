"""pipeline2: streaming per-solution analysis (no big batches): enumerate solutions
one-by-one via callback; for each: expand, count Pasch (fast early-exit: >1 stops),
if single-Pasch: record + twin test (cheap necessary conditions first: Pasch-count of
mate must also be 1; block-intersection multisets equal), else skip iso.
Also records min-Pasch systems seen (for potential emergent use) and total counts.
State saved incrementally to JSONL so progress survives."""
import sys, time, json
sys.setrecursionlimit(100000)
from itertools import combinations
def sig(x): return x^1 if x<18 else x
P2id={}; n=0
def pid(a,b):
    global n
    if a>b:a,b=b,a
    sa,sb=sig(a),sig(b)
    e,f=(sa,sb) if sa<sb else (sb,sa)
    ra,rb=a,b
    if e<a or (e==a and f<b): ra,rb=e,f
    if (ra,rb) not in P2id: P2id[(ra,rb)]=n; n+=1
    return P2id[(ra,rb)]
for a in range(18):
    for b in range(a+1,18):
        if sig(a)==b: continue
        pid(a,b)
P3=[t for t in combinations(range(18),3) if not (sig(t[0])==t[1] or sig(t[0])==t[2] or sig(t[1])==t[2])]
P3=[t for t in P3 if t<tuple(sorted((sig(t[0]),sig(t[1]),sig(t[2]))))]
ALL6=list(combinations(range(21),6))

def expand(FIX,mix,p3):
    blocks=set()
    blocks.add((18,19,20))
    for i,f in enumerate(FIX):
        blocks.add(tuple(sorted((18+f,2*i,2*i+1))))
    for t in mix:
        blocks.add(tuple(sorted(t))); blocks.add(tuple(sorted((sig(t[0]),sig(t[1]),sig(t[2])))))
    for t in p3:
        blocks.add(tuple(sorted(t))); blocks.add(tuple(sorted((sig(t[0]),sig(t[1]),sig(t[2])))))
    return blocks

def pasches_limit(blocks,limit=2):
    res=[]
    for s6 in ALL6:
        s=set(s6)
        inside=[b for b in blocks if set(b)<=s]
        if len(inside)==4:
            from collections import Counter
            d=Counter(x for b in inside for x in b)
            if all(d[x]==2 for x in s6):
                res.append((s6,inside))
                if len(res)>=limit: return res
    return res

def switch(blocks,s6,inside):
    s=set(s6)
    used=set()
    for b in inside:
        for p in combinations(b,2): used.add(tuple(sorted(p)))
    opp=[]
    for t in combinations(s6,3):
        ps=[tuple(sorted(p)) for p in combinations(t,2)]
        if all(p in used for p in ps) and tuple(sorted(t)) not in inside:
            opp.append(tuple(sorted(t)))
    assert len(opp)==4
    return opp

def refine(blocks):
    blocks=list(blocks)
    blk_of=[[] for _ in range(21)]
    for bi,b in enumerate(blocks):
        for x in b: blk_of[x].append(bi)
    col={x:0 for x in range(21)}
    for _ in range(20):
        def key(x):
            return (col[x],tuple(sorted(col[y] for bi in blk_of[x] for y in blocks[bi] if y!=x)))
        keys=sorted(set(key(x) for x in range(21)))
        k2={k:i for i,k in enumerate(keys)}
        ncol={x:k2[key(x)] for x in range(21)}
        if ncol==col: break
        col=ncol
    return col

def maybe_iso(blocks1,blocks2):
    from collections import Counter
    c1=refine(blocks1); c2=refine(blocks2)
    if Counter(c1.values())!=Counter(c2.values()): return None
    classes={}
    for x in range(21): classes.setdefault(c1[x],[]).append(x)
    targets={}
    for x in range(21): targets.setdefault(c2[x],[]).append(x)
    order=sorted(range(21),key=lambda x:(len(classes[c1[x]]),x))
    bl1=list(blocks1); blkset2=set(blocks2)
    mapping={}; used=set()
    # precompute pair->block? small enough to brute force inline
    def bt(k):
        if k==21:
            return all(tuple(sorted(mapping[x] for x in b)) in blkset2 for b in bl1)
        x=order[k]
        for y in targets[c1[x]]:
            if y in used: continue
            ok=True
            for z,w in mapping.items():
                f1=any(x in bb and z in bb for bb in bl1)
                f2=any(y in bb and w in bb for bb in blocks2)
                if f1!=f2: ok=False; break
            if not ok: continue
            mapping[x]=y; used.add(y)
            if bt(k+1): return True
            del mapping[x]; used.remove(y)
        return False
    return mapping if bt(0) else None

def run_pattern(asg,cap,tlim,out):
    Fof=[int(c) for c in asg]
    fixcell=[[0]*9 for _ in range(3)]
    for i,f in enumerate(Fof): fixcell[f][i]=1
    m1col={}; nc=72
    for f in range(3):
        for i in range(9):
            if not fixcell[f][i]: m1col[(f,i)]=nc; nc+=1
    rows=[]
    for f in range(3):
        F=18+f
        for i in range(9):
            for j in range(i+1,9):
                if fixcell[f][i] or fixcell[f][j]: continue
                for x in (2*i,2*i+1):
                    for y in (2*j,2*j+1):
                        t=tuple(sorted((F,x,y))); s=tuple(sorted((sig(F),sig(x),sig(y))))
                        if t>s: continue
                        rows.append(([pid(x,y),m1col[(f,i)],m1col[(f,j)]],('MIX',t)))
    for t in P3:
        rows.append(([pid(t[0],t[1]),pid(t[0],t[2]),pid(t[1],t[2])],('P3',t)))
    col_rows=[[] for _ in range(nc)]
    for ri,(cl,_) in enumerate(rows):
        for c in cl: col_rows[c].append(ri)
    rowmask=[]
    for cl,_ in rows:
        m=0
        for c in cl: m|=(1<<c)
        rowmask.append(m)
    FULL=(1<<nc)-1
    from collections import Counter
    dist=Counter(); nsys=0; nsingle=0; ntw=0; nmin=10**9; minex=None
    t0=time.time(); stop=[False]
    def handle(s):
        nonlocal nsys,nsingle,ntw,nmin,minex
        nsys+=1
        mix=[rows[ri][1][1] for ri in s if rows[ri][1][0]=='MIX']
        p3=[rows[ri][1][1] for ri in s if rows[ri][1][0]=='P3']
        B=expand(Fof,mix,p3)
        P=pasches_limit(B,2)
        dist[len(P) if len(P)<2 else '2+']+=1
        if len(P)==1:
            nsingle+=1
            s6,inside=P[0]
            opp=switch(B,s6,inside)
            B2=(B-set(inside))|set(opp)
            P2=pasches_limit(B2,2)
            rec={"asg":asg,"fix":Fof,"mix":[list(t) for t in mix],"p3":[list(t) for t in p3],
                 "s6":list(s6),"inside":[list(t) for t in inside],"opp":[list(t) for t in opp],
                 "sig_pres_6set":bool(set(sig(x) for x in s6)==set(s6)),"mate_pasch":len(P2)}
            if len(P2)==1:
                m=maybe_iso(B,B2)
                rec["twin_iso"]=bool(m)
                if m:
                    rec["iso"]=m; ntw+=1
                    out.write(json.dumps(rec)+"\n"); out.flush()
                    print("TWIN-HIT "+json.dumps(rec)[:300],flush=True)
                    return True
            else:
                rec["twin_iso"]=False
            print("SINGLE "+json.dumps(rec)[:300],flush=True)
        else:
            Pfull=pasches_limit(B,100)
            if len(Pfull)<nmin: nmin=len(Pfull); minex=(mix,p3)
        return False
    def dfs(rem,chosen):
        if stop[0]: return True
        if time.time()-t0>tlim: stop[0]=True; return True
        if rem==0:
            hit=handle(chosen)
            if hit: stop[0]='HIT'; return True
            return nsys>=cap
        best=-1;bestn=10**9;besto=None
        r=rem
        while r:
            lsb=r&(-r); c=lsb.bit_length()-1; r^=lsb
            opts=[ri for ri in col_rows[c] if rowmask[ri]&~rem==0]
            if not opts: return False
            if len(opts)<bestn: bestn=len(opts);best=c;besto=opts
            if bestn<=1: break
        for ri in besto:
            chosen.append(ri)
            if dfs(rem&~rowmask[ri],chosen):
                if nsys>=cap or stop[0]: return True
            chosen.pop()
        return False
    dfs(FULL,[])
    print(f"pattern {asg}: systems={nsys} single={nsingle} twins={ntw} minpasch={nmin} timed={stop[0]} dist={dict(sorted((str(k),v) for k,v in dist.items()))}",flush=True)
    return stop[0]=='HIT'

if __name__=="__main__":
    asg=sys.argv[1]
    cap=int(sys.argv[2]) if len(sys.argv)>2 else 3000
    tlim=float(sys.argv[3]) if len(sys.argv)>3 else 600
    out=open("stream_hits_%s.jsonl"%asg,"a")
    hit=run_pattern(asg,cap=cap,tlim=tlim,out=out)
    out.close()
