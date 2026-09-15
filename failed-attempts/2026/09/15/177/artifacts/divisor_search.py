"""Bounded recovery test for D7: x0^4+4*x1^4+7*x2^4-7*x3^4=0.
Test A: projective box search, max|xi|<=B, B=300. Result: only [0:0:1:1],[0:0:1:-1].
Test B: exact reduced-pair search. Any primitive integral solution has 14|x0,14|x1
 (mod-16 parity lemma + mod-7 fourth-power lemma). Write x0=14X,x1=14Y with x2,x3 odd.
 Then x3^4-x2^4 = 5488*(X^4+4*Y^4) =: D. For x3>x2>=0, (x2+1)^4-x2^4 > 4*x2^3,
 so x2 <= (D/4)^(1/3)+2 gives a rigorous finite bound per (X,Y). Checks all |X|,|Y|<=12.
 Result: no solutions (624 pairs checked, 0 hits).
Run: python3 divisor_search.py
"""
import math

def has_solution_for_XY(X, Y):
    v = X**4 + 4*Y**4
    if v == 0:
        return (True, "trivial fibre x2=x3 arbitrary")
    D = 5488*v
    xmax = int((D/4)**(1/3.0)) + 3
    sols = []
    for x2 in range(0, xmax+1):
        t = x2**4 + D
        x3 = int(round(t**0.25))
        for c in (x3-2, x3-1, x3, x3+1, x3+2):
            if c >= 0 and c**4 == t:
                sols.append((x2, c))
    return (len(sols) > 0, sols)

def main():
    B = 12
    checked = 0
    hits = []
    for X in range(-B, B+1):
        for Y in range(-B, B+1):
            if X == 0 and Y == 0:
                continue
            checked += 1
            ok, sols = has_solution_for_XY(X, Y)
            if ok:
                hits.append(((X, Y), sols))
    print(f"checked={checked} hits={len(hits)}")
    for h in hits[:10]:
        print(h)
    # reference values
    for X, Y in [(1,0),(0,1),(1,1),(2,1)]:
        v = X**4+4*Y**4; D = 5488*v
        print((X,Y), f"v={v} D={D} xmax={int((D/4)**(1/3.0))+3}", has_solution_for_XY(X,Y))

if __name__ == "__main__":
    main()
