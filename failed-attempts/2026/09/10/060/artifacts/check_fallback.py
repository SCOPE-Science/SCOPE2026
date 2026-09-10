"""Bounded fallback attempt for lane-649 preset fallback (N0=X_2, e2=S_2).

Checks, from text layer of Akbulut-Yasui 1208.1053v3 Secs.2-3:
  (a) Lemma 3.1 algebra for p=2 (even): with basis (T_2,S_2) and matrix
      [[0,1],[1,-1]], every class v with v^2=-1 equals +-S_2 (brute force).
  (b) Clause (i): <c1,S_2>=-3, S_2^2=-1 -> 2g-2>=|-3|-1=2 -> g>=2. CERTIFIED.
  (c) Naive-tubing upper bound: with minimal feasible genera g(R_2)=0 (sphere,
      allowed since |K.R_2|+R_2^2 = 3-9 <0) and g(T_2)=1 (torus, forced by
      |K.T_2|+T_2^2=0 -> g>=1), iterated tubing of 1 R-sheet with 4 T-sheets
      along the 4 transverse R.T intersections gives genus 0+4*1=4.
      So the standard tubing route yields g<=4, NOT the required g<=2.
      A genus-2 representative would need a direct 7-component Seifert surface
      audit from Fig.2, which is not in the text layer. RECORDED AS BLOCKED.
"""
import sys


def lemma31_even():
    sols = []
    for a in range(-6, 7):
        for b in range(-6, 7):
            if 2 * a * b - b * b == -1:
                sols.append((a, b))
    ok = all((a == 0 and abs(b) == 1) for a, b in sols) and len(sols) == 2
    print(f"Lemma3.1(p=2): v^2=-1 solutions in window: {sols} -> {'OK' if ok else 'FAIL'}")
    return ok


def clause_i():
    kdot, sq = -3, -1
    bound = abs(kdot) + sq
    gmin = (bound + 2) / 2
    print(f"Clause(i): K.S_2={kdot}, S_2^2={sq}, 2g-2>={bound} -> g>={gmin} [{'OK' if gmin == 2 else 'FAIL'}]")
    return gmin == 2


def naive_tubing():
    gR, gT, sheets = 0, 1, 4
    genus = gR + sheets * gT
    print(f"Naive tubing: g(R_2)={gR} (min feasible), g(T_2)={gT} (forced), "
          f"{sheets} intersections -> genus {genus} (need <=2) -> "
          f"{'GAP: 4>2, route fails' if genus > 2 else 'OK'}")
    return genus


def main():
    ok_a = lemma31_even()
    ok_b = clause_i()
    genus = naive_tubing()
    print("Summary: clause (i) g>=2 CERTIFIED; clause (ii) genus-2 surface NOT "
          "exhibited (naive tubing gives 4; direct Fig.2 Seifert audit unavailable).")
    if not (ok_a and ok_b):
        sys.exit(1)
    print("FALLBACK_ATTEMPT_LOGGED: (i) proved, (ii) blocked.")
    return genus


if __name__ == "__main__":
    main()
