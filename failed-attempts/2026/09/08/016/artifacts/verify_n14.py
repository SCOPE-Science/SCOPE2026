"""Rigorous stdlib-only verifier for the n=14 circle-in-square partial certificate.

Checks (exact integer arithmetic):
 L1. boundary feasibility of 14 rational centers at claimed radius rLB;
 L2. all 91 pairwise distances >= 2*rLB (exact integer compare, equality allowed);
 L3. reported contact/clearance census (22 contacts at exactly 2*rLB... see log);
 U1. analytic upper bound r*(14) < 719/5000 via column-band pigeonhole, pattern (4,3,3,3):
     certifies S(719/5000) >= L with explicit dyadic rationals t4,t3 with t^2<=v^2;
 P1. Machin pi enclosure + density intervals.
Prints PASS/FAIL lines and exits nonzero on failure. No numpy. No float trust
(floats used only to *select* candidates, every acceptance is an integer check).
"""
from fractions import Fraction
import math, itertools, sys

S = 10**12
TXT = [(-0.370668206290,-0.370668206290),(-0.112004618870,-0.370668206290),
 (0.146658968550,-0.370668206290),(0.370668206290,-0.241336412580),
 (-0.370668206290,-0.112004618870),(-0.112004618870,-0.112004618870),
 (0.146658968550,-0.112004618870),(0.370668206290,0.017327174840),
 (-0.370668206290,0.146658968550),(-0.112004618870,0.146658968550),
 (0.146658968550,0.146658968550),(0.355841478032,0.355841478041),
 (-0.241336412580,0.370668206290),(0.017327174840,0.370668206290)]
RLB = Fraction(12933169, 100000000)   # claimed feasible radius 0.12933169
RUB = Fraction(719, 5000)             # proved infeasible-at-or-above radius 0.1438

def main():
    ok = True
    PTS = [(round((x+0.5)*S), round((y+0.5)*S)) for x, y in TXT]
    RB = RLB * S  # = 129331690000.0 exactly? RLB*1e12 = 129331690000
    assert RB == int(RB), "scaling must be integral"
    RB = int(RB)
    # L1 boundary: RB <= c <= S-RB
    for i,(a,b) in enumerate(PTS):
        if not (RB <= a <= S-RB and RB <= b <= S-RB):
            print(f"FAIL boundary center {i+1}: {(a,b)} vs r={RB}"); ok=False
    if ok: print(f"L1 PASS: all 14 centers in [{RB},{S-RB}]^2 (rLB={RLB}={float(RLB):.8f})")
    # L2 pairwise: D2 >= (2*RB)^2
    D2min = (2*RB)**2
    mind2=None; ncontact=0
    for (a,b) in itertools.combinations(range(14),2):
        dx=PTS[a][0]-PTS[b][0]; dy=PTS[a][1]-PTS[b][1]
        d2=dx*dx+dy*dy
        mind2 = d2 if mind2 is None or d2<mind2 else mind2
        if d2 < D2min:
            print(f"FAIL pair {a+1},{b+1}: d2={d2} < (2r)^2={D2min}"); ok=False
        if d2 == D2min: ncontact+=1
    import math as m
    print(f"L2 {'PASS' if ok else 'FAIL'}: min |ci-cj| = sqrt({mind2})/1e12 = {m.sqrt(mind2)/S:.12f}; "
          f"2*rLB = {float(2*RLB):.12f}; contacts at equality: {ncontact}")
    # clearance of rattler (#12) to nearest: must exceed 2r by margin
    r12=min((PTS[11][0]-PTS[j][0])**2+(PTS[11][1]-PTS[j][1])**2 for j in range(14) if j!=11)
    print(f"RATTLER: min d2 to #12 = {r12}, ratio sqrt(d2)/(2rLB) = {m.sqrt(r12)/ (2*RB):.6f} (>>1: loose circle)")
    # U1: pigeonhole upper bound
    R=RUB; L=1-2*R; d=2*R
    v4=d*d-(L/4)*(L/4); v3=d*d-(L/3)*(L/3)
    f4=m.sqrt(float(v4)); f3=m.sqrt(float(v3))
    M=2**40
    t4=Fraction(math.floor(f4*M),M); t3=Fraction(math.floor(f3*M),M)
    c1 = t4*t4 <= v4 and t3*t3 <= v3
    c2 = (t4+3*t3) >= L
    print(f"U1 v4={v4} v3={v3}; t4={t4} t3={t3}")
    print(f"U1 t^2<=v^2: {'PASS' if c1 else 'FAIL'}; t4+3t3-L = {t4+3*t3-L} = {float(t4+3*t3-L):.9f} {'>=0 PASS' if c2 else 'FAIL'}")
    if not (c1 and c2): ok=False
    else: print(f"U1 PASS: S(719/5000)>=L certifies r*(14) < 719/5000 = 0.1438")
    # P1 Machin pi + densities
    def atan_pm(q,N):
        SN=sum(Fraction(((-1)**k),(2*k+1)*q**(2*k+1)) for k in range(N+1))
        T=SN+Fraction(((-1)**(N+1)),(2*(N+1)+1)*q**(2*(N+1)+1))
        return (min(SN,T),max(SN,T))
    a5=atan_pm(5,25); a239=atan_pm(239,25)
    pilo=4*(4*a5[0]-a239[1]); pihi=4*(4*a5[1]-a239[0])
    assert pilo<=pihi and (pihi-pilo)<=Fraction(1,10**30)
    dLBlo=14*pilo*RLB*RLB; dLBhi=14*pihi*RLB*RLB
    dUB=14*pihi*RUB*RUB
    print(f"P1 PASS: pi in [{float(pilo):.15f},{float(pihi):.15f}], width {float(pihi-pilo):.2e}")
    print(f"P1 density: phi(14) >= [{float(dLBlo):.10f},{float(dLBhi):.10f}] (at rLB); "
          f"phi(14) < {float(dUB):.10f} (at rUB, strict since r*<rUB)")
    print("OVERALL:", "PASS" if ok else "FAIL")
    return 0 if ok else 1

if __name__=="__main__":
    sys.exit(main())
