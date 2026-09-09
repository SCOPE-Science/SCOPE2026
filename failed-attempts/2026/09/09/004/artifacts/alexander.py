# Wirtinger presentation from PD -> Alexander polynomial via Fox calculus.
# PD convention (KnotTheory): X[a,b,c,d], a=incoming under, CCW order; under-pair=(a,c), over-pair=(b,d).
# Self-check: must reproduce 8_20 Alexander t^2-2t+3-2t^-1+t^-2 (up to +-t^k).
import sympy as sp
from pd_toolkit import parse_pd, PD820
t = sp.Symbol('t')
def build_traversal(pd):
    # pairing: through strands a-c, b-d. Walk single cycle; return list of (vtx, in_pos, out_pos, edge_label_traversed)
    n = len(pd)
    # stub key (v,p) with label; adjacency: label-> [stub1, stub2]
    lab = {}
    for v,q in enumerate(pd):
        for p,l in enumerate(q):
            lab.setdefault(l, []).append((v,p))
    pair = {0:2, 2:0, 1:3, 3:1}
    # start at stub holding label 1
    start = lab[1][0]
    seq = []  # (v, in_p, out_p, out_label)
    cur = start
    while True:
        v, ip = cur
        op = pair[ip]
        ol = pd[v][op]
        seq.append((v, ip, op, ol))
        dep = (v, op)
        nxt = lab[ol][0] if lab[ol][1] == dep else lab[ol][1]
        cur = nxt
        if cur == start:
            break
        assert len(seq) < 4*n+10, "not a single component or bug"
    return seq
def wirtinger(pd, over_pair=(1,3)):
    # over_pair: positions (b,d)=(1,3) per convention. Returns (arcs list per crossing: (over_gen, under_in_gen, under_out_gen, eps), ngen, signs)
    seq = build_traversal(pd)
    n = len(pd)
    # cut into arcs at over-passes: over-pass at vtx v means exit (or entry) via over strand.
    # Determine for each seq step whether we traverse over or under strand at v.
    op1, op2 = over_pair
    # assign gen id to each maximal run of steps between over-passes
    is_over = []
    for (v, ip, op, ol) in seq:
        # strand traversed: {ip,op} == over pair?
        s = {ip, op}
        is_over.append(s == {op1, op2})
    # gen id per seq index: new gen starts right after an over-pass step... standard: arc = between consecutive overcrossings.
    gen = [None]*len(seq)
    # find first over step; arcs numbered from there
    # Each maximal set of consecutive non-over steps + following over step? Convention: generator = arc that goes UNDER at its end.
    # Simple robust: cut before each over-step: arc k = steps (cut_k .. cut_{k+1}-1) where cuts are over-step indices... but over-steps belong to over-arc (previous arc). Assign: step i gets gen g; increment g after each over-step.
    g = 0
    started = False
    # rotate so we start right after an over step
    over_idx = [i for i,o in enumerate(is_over) if o]
    assert len(over_idx) == n, (len(over_idx), n)
    rot = (over_idx[0]+1) % len(seq)
    order = list(range(rot, len(seq))) + list(range(0, rot))
    gmap = {}
    g = -1
    is_under = [not o for o in is_over]
    under_idx = [i for i,o in enumerate(is_under) if o]
    rot = (under_idx[0]+1) % len(seq)
    order = list(range(rot, len(seq))) + list(range(0, rot))
    prev_was_under = True
    for i in order:
        if prev_was_under:
            g += 1
        gmap[i] = g
        prev_was_under = is_under[i]
    ngen = g+1
    assert ngen == n, (ngen, n)
    # per crossing: over step index, under-in step, under-out step
    info = {}
    for i,(v,ip,op,ol) in enumerate(seq):
        info.setdefault(v, []).append(i)
    rels = []
    for v in range(n):
        steps = info[v]
        over_steps = [i for i in steps if is_over[i]]
        under_steps = [i for i in steps if not is_over[i]]
        assert len(over_steps)==1 and len(under_steps)==1, (v, steps)
        go = gmap[over_steps[0]]
        # under traversal direction: enters via ip, exits via op. under-in gen = gen of under step; under-out gen = gen of NEXT step (which starts new arc? next step begins where?)
        iu = under_steps[0]
        gi_in = gmap[iu]
        # next step after iu in cyclic seq order:
        j = (iu+1) % len(seq)
        gi_out = gmap[j]
        # crossing sign: orientation of under strand (in->out positions) vs over strand.
        (vv,ip,op,ol) = seq[iu]
        io = over_steps[0]
        (vo,ipo,opo,olo) = seq[io]
        # positions: under in-pos ip, out-pos op; over in-pos ipo, out-pos opo.
        # sign via cyclic order: with CCW order (0,1,2,3), sign = +1 iff (over_in, under_in, over_out) ... use permutation parity:
        # Standard formula: sign = +1 iff going CCW we meet: under-in, over-in, under-out, over-out? Let's just compute both and validate vs known Alexander.
        rels.append((v, go, gi_in, gi_out, (ip,op,ipo,opo)))
    return rels, ngen
def sign_from_positions(ip, op, ipo, opo):
    # CCW cyclic order 0,1,2,3. Under: ip->op; over: ipo->opo.
    # sign +1 iff (op - ip) mod 4 == ... : rotate so ip=0: op must be 2 (through). Then over positions {1,3}: ipo=1 or 3.
    # Right-hand rule: +1 iff over direction crosses under left-to-right with under pointing up: under 0->2 (up), over 3->1 (rightward)? positions CCW: 0=bottom? Unknown absolute rotation; relative: sign=+1 iff ipo == (ip+3)%4 i.e. over-in is clockwise-adjacent to under-in? Convention choice; validated empirically below.
    if (ipo - ip) % 4 == 3:
        return 1
    else:
        return -1
def alexander(pd, try_both_signs=True):
    rels, ngen = wirtinger(pd)
    n = len(pd)
    M = sp.zeros(n, n)
    for (v, go, gii, gio, pos) in rels:
        eps = sign_from_positions(*pos)
        if eps == 1:
            # r = xj xi xj^-1 xk^-1 ; d(r)/dxj = 1 - t... Fox: dr/dxj = 1 - xj xi xj^-1 -> abelian: 1-t; dr/dxi = xj -> t; dr/dxk = -1
            M[v, go] += (1 - t); M[v, gii] += t; M[v, gio] += -1
        else:
            # r = xj^-1 xi xj xk^-1 ; dr/dxj = -xj^-1 + xj^-1 xi -> -1 + t... abelian: t-1? dr/dxj = -1+t? compute: d(xj^-1)/ = -xj^-1; d(xj^-1 xi xj)/dxj = -xj^-1 + xj^-1 xi (eval: -1 + t)
            M[v, go] += (t - 1); M[v, gii] += 1; M[v, gio] += -1
    A = M[0:n-1, 0:n-1]
    # clear denominators (entries already polynomial), det, normalize
    d = sp.expand(A.det())
    return normalize(d)
def normalize(p):
    p = sp.expand(p)
    if p == 0:
        return p
    # symmetric Laurent normalize: lowest degree -> shift so min deg 0, fix sign positive leading... standard: Delta(t)=Delta(t^-1), Delta(1)=1.
    poly = sp.Poly(p, t)
    degs = [m[0] for m in poly.monoms()]
    mn = min(degs)
    q = sp.expand(p / t**mn)
    # sign: make value at t=1 positive? Delta(1)=1 expected.
    if q.subs(t, 1) < 0:
        q = -q
    return sp.expand(q)
if __name__ == '__main__':
    pd = parse_pd(PD820)
    seq = build_traversal(pd)
    print("traversal steps:", len(seq), "(expect 16)")
    d = alexander(pd)
    print("Delta(8_20 computed) =", d)
    print("known            = t^2 - 2t + 3 - 2/t + 1/t^2  i.e. *t^2:", sp.expand(t**2*(t**2-2*t+3-2/t+1/t**2)))
