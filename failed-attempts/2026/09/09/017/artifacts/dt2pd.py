"""DT code -> endpoint-PD conversion, validated on D0. Bounded step."""
import sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-314/output/artifacts')
from epd import bracket, det_of


def dt_to_pd(dt):
    """dt: list of n signed even ints (DT[i] for odd label 2i-1).
    Returns (cr, edges) in endpoint format (ports 0,1,2,3; over=(0,2)).
    Convention attempt V1: crossing i: odd visit (label 2i-1) is UNDER iff dt[i]>0?
    (KnotTheory: positive DT entry means ... calibrate.)
    Arcs: arc k = from label k to label k+1 (mod 2n), as edge. At crossing i, visits at
    labels L1=2i-1, L2=|dt[i]|. Each visit has in-arc (label-1 -> label) and out-arc.
    X-ports: under-in -> 1? We set: over strand ports (0,2), under (1,3), with
    0 = over-in-arc, 2 = over-out-arc, 1 = under-in-arc, 3 = under-out-arc.
    Caller tries sign conventions for which visit is over."""
    raise NotImplementedError


def dt_to_pd_v(dt, over_odd_if_pos):
    n = len(dt)
    N = 2 * n
    # arc k (1..2n): from label k to k+1 (mod 2n). Represent edge ids = k.
    # crossing i (1..n): visits L1 = 2i-1 (odd), L2 = abs(dt[i-1]) (even).
    # in-arc at visit L = arc L-1 (mod 2n); out-arc = arc L.
    cr = {}; edges = {}
    for k in range(1, N + 1):
        edges[k] = []  # arc k: endpoints filled below
    # endpoint helper: arc k has tail at label k, head at label k+1.
    for i in range(1, n + 1):
        L1 = 2 * i - 1
        L2 = abs(dt[i - 1])
        sgn = 1 if dt[i - 1] > 0 else -1
        # which visit is over?
        if over_odd_if_pos:
            odd_over = (sgn > 0)
        else:
            odd_over = (sgn < 0)
        a_in = L1 - 1 if L1 > 1 else N
        a_out = L1
        b_in = L2 - 1 if L2 > 1 else N
        b_out = L2
        if odd_over:
            # over: a_in -> a_out (ports 0,2); under: b_in -> b_out (1,3)
            ports = {0: (a_in, 'head', L1), 2: (a_out, 'tail', L1),
                     1: (b_in, 'head', L2), 3: (b_out, 'tail', L2)}
        else:
            ports = {0: (b_in, 'head', L2), 2: (b_out, 'tail', L2),
                     1: (a_in, 'head', L1), 3: (a_out, 'tail', L1)}
        cr[i] = (ports[0][0], ports[1][0], ports[2][0], ports[3][0])
        # register endpoints: arc k: tail at label k [(i,port)], head at label k+1
        for p, (ak, end, lab) in ports.items():
            if end == 'tail':
                edges[ak].append((i, p))  # placeholder, fix below
            else:
                edges[ak].append((i, p))
    # Fix: arc k connects label k (tail) to label k+1 (head). The two endpoints:
    # tail: crossing-visit at label k as OUTGOING (out-arc==k means visit label==k... out-arc at visit L is arc L: tail of arc L is at label L). Head: visit at label k+1 as INCOMING (in-arc==k means visit label k+1).
    # Rebuild cleanly:
    edges2 = {}
    for k in range(1, N + 1):
        tail_lab = k
        head_lab = k + 1 if k < N else 1
        edges2[k] = [('T', tail_lab), ('H', head_lab)]
    # map (tail/head, label) -> (crossing, port)
    # visit at label L (crossing i_L): out-arc = arc L (tail at L); in-arc = arc L-1 (head at L).
    pos_of = {}
    for i in range(1, n + 1):
        L1 = 2 * i - 1
        L2 = abs(dt[i - 1])
        sgn = 1 if dt[i - 1] > 0 else -1
        if over_odd_if_pos:
            odd_over = (sgn > 0)
        else:
            odd_over = (sgn < 0)
        if odd_over:
            pos_of[('out', L1)] = (i, 0)  # over-in? NO: out-arc tail...
            # tail of arc L1 is at label L1 (the visit): arc L1 leaves the visit: it's the OUTGOING.
            # port for outgoing over = 2. Incoming over (head of arc L1-1) = port 0.
            pos_of[('tail', L1)] = (i, 2)
            pos_of[('head', L1)] = (i, 0)
            pos_of[('tail', L2)] = (i, 3)
            pos_of[('head', L2)] = (i, 1)
        else:
            pos_of[('tail', L1)] = (i, 3)
            pos_of[('head', L1)] = (i, 1)
            pos_of[('tail', L2)] = (i, 2)
            pos_of[('head', L2)] = (i, 0)
    edges3 = {}
    for k in range(1, N + 1):
        tail_lab = k
        head_lab = k + 1 if k < N else 1
        edges3[k] = [pos_of[('tail', tail_lab)], pos_of[('head', head_lab)]]
    cr2 = {}
    for i in range(1, n + 1):
        L1 = 2 * i - 1
        L2 = abs(dt[i - 1])
        # over edge ids: arcs at over-visit (in-arc, out-arc); under similarly. For tuple, use arc ids:
        # ports (0:in-over-arc, 1:in-under-arc, 2:out-over-arc, 3:out-under-arc)
        sgn = 1 if dt[i - 1] > 0 else -1
        if over_odd_if_pos:
            odd_over = (sgn > 0)
        else:
            odd_over = (sgn < 0)
        in1 = L1 - 1 if L1 > 1 else N
        out1 = L1
        in2 = L2 - 1 if L2 > 1 else N
        out2 = L2
        if odd_over:
            cr2[i] = (in1, in2, out1, out2)
        else:
            cr2[i] = (in2, in1, out2, out1)
    return cr2, edges3


if __name__ == '__main__':
    dt0 = [4, 8, -12, 2, -14, -16, -6, -10]
    for v in (True, False):
        cr, edges = dt_to_pd_v(dt0, v)
        B = bracket(cr, edges)
        print('over_odd_if_pos=', v, 'det=%.3f' % det_of(B),
              dict(sorted((k, x) for k, x in B.items() if x != 0)))
    print('target: {-8:-1, 4:1, 12:1}, det 3')
