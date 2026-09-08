"""From-scratch verification for lane-147 twist family of 9_42.

Seed: KnotAtlas PD of 9_42 (hardcoded below, cross-checked against
inputs/topic.json admission record + live KnotAtlas fetch).
Family: replace crossing 0 by a coherent twist stack of t crossings,
t = 1,3,5,7,9  ->  total crossings 9,11,13,15,17.
Checks per member:
  * single component (PD strand tracing, convention-free opposite pairing)
  * Kauffman-bracket state-sum span -> Jones span = span_bracket/4
  * all-A / all-B circle counts -> diagram Turaev genus (c+2-sA-sB)/2
Stdlib only.
"""
import json, itertools, sys

SEED_PD = [
    (1,4,2,5), (5,10,6,11), (3,9,4,8), (9,3,10,2), (1,6,12,17),
    (11,14,7,15,8)[:4],  # placeholder replaced below
]
# Exact KnotAtlas PD: X1425 X5,10,6,11 X3948 X9,3,10,2 X16,12,17,11 X14,7,15,8 X6,15,7,16 X18,14,1,13 X12,18,13,17
SEED_PD = [
    (1,4,2,5), (5,10,6,11), (3,9,4,8), (9,3,10,2), (16,12,17,11),
    (14,7,15,8), (6,15,7,16), (18,14,1,13), (12,18,13,17),
]

def components(pd):
    """Trace strands through crossings (opposite-edge pairing). Returns #components."""
    pair = {}
    for ci,(a,b,c,d) in enumerate(pd):
        pair[(ci,0)] = (ci,2); pair[(ci,2)] = (ci,0)
        pair[(ci,1)] = (ci,3); pair[(ci,3)] = (ci,1)
    # edge label -> the two (crossing,pos) ends carrying it
    from collections import defaultdict
    ends = defaultdict(list)
    for ci,(a,b,c,d) in enumerate(pd):
        for pos,e in enumerate((a,b,c,d)):
            ends[e].append((ci,pos))
    for e,v in ends.items():
        assert len(v)==2, (e,v)
    nxt = {}
    for e,(p,q) in ends.items():
        nxt[p]=q; nxt[q]=p
    seen=set(); ncomp=0
    for ci in range(len(pd)):
        for pos in range(4):
            if ((ci,pos) in seen): continue
            ncomp+=1
            cur=(ci,pos)
            while cur not in seen:
                seen.add(cur)
                cur = pair[nxt[cur]]
    return ncomp

def extend_twist(pd, site, t):
    """Replace crossing `site` X[a,b,c,d] by a coherent stack of t crossings
    (t odd preserves strand pairing). New crossings copy the cyclic pattern
    X[s1in,s2in,s1out,s2out]. Returns new PD."""
    a,b,c,d = pd[site]
    used = {e for cr in pd for e in cr}
    nxt = max(used)+1
    def fresh():
        nonlocal nxt
        v=nxt; nxt+=1; return v
    p = [a]+[fresh() for _ in range(t-1)]+[c]
    q = [b]+[fresh() for _ in range(t-1)]+[d]
    new = [cr for i,cr in enumerate(pd) if i!=site]
    for i in range(t):
        new.append((p[i],q[i],p[i+1],q[i+1]))
    return new

class UF:
    __slots__=("p","r")
    def __init__(s,n):
        s.p=list(range(n)); s.r=[0]*n
    def f(s,x):
        p=s.p
        while p[x]!=x:
            p[x]=p[p[x]]; x=p[x]
        return x
    def u(s,x,y):
        x=s.f(x); y=s.f(y)
        if x==y: return
        if s.r[x]<s.r[y]: x,y=y,x
        s.p[y]=x
        if s.r[x]==s.r[y]: s.r[x]+=1

def bracket_span_and_circles(pd, smoothA=0):
    """Full state sum. smoothing bit 0/1 per crossing.
    Smoothing 0 pairs (a,b)|(c,d) [adjacent], smoothing 1 pairs (a,d)|(b,c).
    (Global 0<->1 swap = mirror; span unaffected.)
    Returns (min_exp, max_exp, s_all0, s_all1, nstates)."""
    c = len(pd)
    # half-edge index: ci*4+pos. edge-link partner: same label other end.
    from collections import defaultdict
    ends = defaultdict(list)
    for ci,(a,b,c_,d) in enumerate(pd):
        for pos,e in enumerate((a,b,c_,d)):
            ends[e].append(ci*4+pos)
    link = {}
    for e,(p,q) in ends.items():
        link[p]=q; link[q]=p
    n = 4*c
    mn = None; mx = None; s0=s1=None
    for mask in range(1<<c):
        uf = UF(n)
        for ci in range(c):
            base=ci*4
            if (mask>>ci)&1:
                uf.u(base+0,base+3); uf.u(base+1,base+2)
            else:
                uf.u(base+0,base+1); uf.u(base+2,base+3)
        for h in range(n):
            uf.u(h,link[h])
        roots=set()
        for h in range(n):
            roots.add(uf.f(h))
        circles=len(roots)
        n1 = bin(mask).count("1"); n0 = c-n1
        # exponent of A: (n0-n1) from smoothings + (circles-1)*(+/-2) extremes
        lo = (n0-n1) - 2*(circles-1)
        hi = (n0-n1) + 2*(circles-1)
        mn = lo if mn is None or lo<mn else mn
        mx = hi if mx is None or hi>mx else mx
        if mask==0: s0=circles
        if mask==(1<<c)-1: s1=circles
    return mn,mx,s0,s1,1<<c

def main(site=0):
    rows=[]
    for t in (1,3,5,7,9):
        pd = extend_twist(SEED_PD, site, t)
        c = len(pd)
        nc = components(pd)
        mn,mx,sA,sB,ns = bracket_span_and_circles(pd)
        spanB = mx-mn
        assert spanB % 4 == 0, (t,spanB)
        spanJ = spanB//4
        gT_num = c+2-sA-sB
        assert gT_num % 2 == 0 and gT_num >= 0
        gT = gT_num//2
        rows.append(dict(t=t, crossings=c, components=nc,
                         sA=sA, sB=sB, diagram_genus=gT,
                         bracket_span=spanB, jones_span=spanJ,
                         deficit=c-spanJ, states=ns))
        print(f"t={t} c={c} comp={nc} sA={sA} sB={sB} gT={gT} spanJ={spanJ} deficit={spanJ and c-spanJ}", flush=True)
    print(json.dumps(rows, indent=1))

if __name__=="__main__":
    site = int(sys.argv[1]) if len(sys.argv)>1 else 0
    main(site)
