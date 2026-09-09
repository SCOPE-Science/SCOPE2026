"""Magic-manifold closed-genus-3 census (exact integer part + numeric filter).
Kin-Takasawa: fiber (x,y,z) primitive in fibered cone; dilatation = largest
real root > 1 of f(t) = t^{x+y-z} - t^x - t^y - t^{x-z} - t^{y-z} + 1;
prongs (x/g1, y/g2, (x+y-2z)/g3) with g1=gcd(x,y+z), g2=gcd(y,x+z),
g3=gcd(z,x+y); closed genus gp = (X_T - b + 2)/2, X_T = x+y-z,
b = g1+g2+g3. Cappable to CLOSED fiber iff every prong count >= 2
(no 1-prong; cf. Hironaka Cor 3.9 analogue, Kin Prop 3.3).
Benchmark P_H = t^6-t^4-t^3-t^2+1, lambda_H its largest root.

This script: (a) proves exact equality f(2,4,-3) = (t^3+1)*P_H;
(b) enumerates the stated box and prints the cappable table.
Exact claims use only sympy divisibility; numeric values are filters only.
"""
import sympy as sp
import math

t = sp.Symbol('t')
P_H = t**6 - t**4 - t**3 - t**2 + 1

def fpoly(x, y, z):
    return t**(x + y - z) - t**x - t**y - t**(x - z) - t**(y - z) + 1

def fiber(x, y, z):
    if not (x > 0 and y > 0 and x > z and y > z and x + y - z > 0):
        return None
    g1, g2, g3 = math.gcd(x, y + z), math.gcd(y, x + z), math.gcd(z, x + y)
    XT = x + y - z
    b = g1 + g2 + g3
    gp_num = XT - b + 2
    return {"g": (g1, g2, g3), "XT": XT, "b": b, "gp_num": gp_num,
            "prongs": (x / g1, y / g2, (x + y - 2 * z) / g3)}

def main():
    f = sp.expand(fpoly(2, 4, -3))
    q, r = sp.div(f, P_H)
    print("f(2,4,-3) / P_H: quotient =", q, " remainder =", r)
    assert r == 0
    q2, r2 = sp.div(f, t**3 + 1)
    print("f(2,4,-3) / (t^3+1): quotient =", sp.expand(q2), " remainder =", r2)
    f2 = sp.expand(fpoly(4, 2, -3))
    q3, r3 = sp.div(f2, P_H)
    print("f(4,2,-3) / P_H: quotient =", q3, " remainder =", r3)
    assert r3 == 0
    print("EXACT: f(2,4,-3) = f(4,2,-3) = (t^3+1)*P_H(t).")
    print("Hence lambda(2,4,-3) = lambda(4,2,-3) = lambda_H exactly",
          "(t^3+1 roots are on unit circle).")
    # Box census (integer data only; lam column intentionally omitted here
    # to keep this artifact exact — numeric filter lives in WORKLOG table).
    rows = []
    XN, YN, ZLO, ZHI = 24, 24, -8, 11
    for x in range(1, XN + 1):
        for y in range(1, YN + 1):
            for z in range(ZLO, ZHI + 1):
                d = fiber(x, y, z)
                if d is None or d["gp_num"] != 6:  # gp==3 <=> XT-b+2==6
                    continue
                if math.gcd(math.gcd(x, y), z) != 1:
                    continue
                p = d["prongs"]
                cappable = all(v >= 2 for v in p)
                rows.append((x, y, z, d, cappable))
    cap = [r for r in rows if r[4]]
    print(f"BOX x,y<={XN} z in [{ZLO},{ZHI}]: genus-3 primitive fibers={len(rows)},",
          f"cappable={len(cap)}")
    for (x, y, z, d, _) in sorted(cap)[:40]:
        print(f"  ({x},{y},{z}) b={d['g']} XT={d['XT']} prongs={d['prongs']}")

if __name__ == "__main__":
    main()
