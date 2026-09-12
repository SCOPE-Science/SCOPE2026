import math
g1 = math.e - 2; g2 = math.sqrt(3) - 1
alpha_high = 1/12; beta0 = 0.5
# Bob obstruction needs, at some scale rho with Alice ball radius alpha*rho,
# many overlapping danger squares forcing Alice to intersect danger.
# Danger square half-side c*q^-1.5 around each (p+gamma)/q.
# Key stats per q: spacing s=1/q; danger radius r=c q^-1.5; overlap ratio r/s = c q^-0.5.
# Cluster count in Alice ball: N ~ (alpha*rho*q)^2 with rho~(c)^{2/3} q^{-3/2}*k...
# Instead directly: for q in range, compute overlap ratio + area fraction.
print("q, spacing, danger_r(c=0.05), overlap_ratio, area_frac_per_cell")
for q in [10, 50, 100, 500, 1000, 2000, 4000, 8000]:
    s = 1/q
    for c in [0.05]:
        r = c*q**-1.5
        print(q, "%.2e"%s, "%.2e"%r, "%.2e"%(r/s), "%.2e"%((2*r/s)**2))
# separation check: min distance between distinct centers at same q is exactly 1/q
# danger diameter 2c q^-1.5 << 1/q for all q>=1 when c<0.5*sqrt(q)... always disjoint.
print("disjointness: 2r < s ?", [(q, 2*0.05*q**-1.5 < 1/q) for q in [2,10,100,8000]])
# cross-q coincidence: min over p,p',q,q' of |(p+g)/q-(p'+g)/q'| for q,q'<=50 (1D per coord)
import itertools
def min_gap(Q):
    mg=1e9; arg=None
    for q in range(1,Q+1):
        for qq in range(1,Q+1):
            if qq==q: continue
            for p in range(q):
                for pp in range(qq):
                    d=abs((p+g1)/q-(pp+g1)/qq)
                    if d>1e-12 and d<mg: mg=d; arg=(q,p,qq,pp)
    return mg,arg
mg,arg=min_gap(30)
print("min cross-q gap q<=30:",mg,arg)
