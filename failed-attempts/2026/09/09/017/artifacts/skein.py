"""Skein-tree diagnostics for D1: dets of smoothings + writhe-normalized Jones."""
import sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-314/output/artifacts')
from epd import katlas_819, insert_twist, bracket, det_of
import cmath


def smooth(crX, eX, Y, opt):
    cr3 = {k: v for k, v in crX.items() if k != Y}
    e3 = {e: list(v) for e, v in eX.items()}

    def pop(end):
        for e, ends in e3.items():
            if end in ends:
                return e
    ea = pop((Y, 0)); eb = pop((Y, 1)); ec = pop((Y, 2)); ed = pop((Y, 3))
    oa = e3[ea][1] if e3[ea][0] == (Y, 0) else e3[ea][0]
    ob = e3[eb][1] if e3[eb][0] == (Y, 1) else e3[eb][0]
    oc = e3[ec][1] if e3[ec][0] == (Y, 2) else e3[ec][0]
    od = e3[ed][1] if e3[ed][0] == (Y, 3) else e3[ed][0]
    for e in (ea, eb, ec, ed):
        del e3[e]
    me = max(e3.keys()) + 1
    if opt == 0:
        e3[me] = [oa, ob]; e3[me + 1] = [oc, od]
    else:
        e3[me] = [oa, od]; e3[me + 1] = [oc, ob]
    return cr3, e3


def tracemap(crX, eX):
    port_edge = {}
    for e, ends in eX.items():
        for end in ends:
            port_edge[end] = e
    pair = {}
    for c in crX:
        pair[(c, 0)] = (c, 2); pair[(c, 2)] = (c, 0)
        pair[(c, 1)] = (c, 3); pair[(c, 3)] = (c, 1)
    seen = set(); cyc = []
    for c in crX:
        for j in range(4):
            if (c, j) in seen:
                continue
            L = 0; cur = (c, j)
            while cur not in seen:
                seen.add(cur); L += 1
                e = port_edge[cur]; ends = eX[e]
                nxt = ends[1] if ends[0] == cur else ends[0]
                cur = pair[nxt]
            cyc.append(L)
    return sorted(cyc)


if __name__ == '__main__':
    cr, edges = katlas_819()
    cr2, e2 = insert_twist(cr, edges, (4, 1), (4, 2), overA=True)
    print('D1 cycles:', tracemap(cr2, e2))
    for opt in (0, 1):
        crS, eS = smooth(cr2, e2, 9, opt)
        BS = bracket(crS, eS)
        print('smooth', opt, 'cycles:', tracemap(crS, eS),
              'det=%.4f' % det_of(BS),
              dict(sorted((k, v) for k, v in BS.items() if v != 0)))
