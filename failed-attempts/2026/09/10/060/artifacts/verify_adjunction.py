"""Reproduce the Stein-adjunction lower bounds of Akbulut-Yasui 1208.1053 Sec.3.

Source data (text layer of arXiv:1208.1053v3, Sec.3):
  rotation numbers: r(alpha_p)=-1, r(beta_p)=1, r(gamma_p)=0
  R_p = [alpha_p - p*beta_p], T_p = [gamma_p]
  S_p = R_p + c(p)*T_p with c(2q-1)=(2q-1)^2-q+1, c(2q)=(2q)^2-q+1
  <c1,T_p> = 0 so <c1,S_p> = <c1,R_p> = -1 - p
  S_p^2 = -2 (p odd), -1 (p even)
Stein adjunction (Akbulut-Matveyev, recalled as Thm 3.4 of 1102.3049):
  2g - 2 >= |<c1,S_p>| + S_p^2   (for [S_p] != 0)

This script checks the LOWER bounds only. It does NOT construct the
genus-1 surface realizing S_1 (needs Fig.2 handle slides) and does NOT
identify X_3 as a single W1 cork twist of X_1 (not in the source text).
"""
import sys


def coeff(p):
    if p % 2 == 1:
        q = (p + 1) // 2
        return (2 * q - 1) ** 2 - q + 1
    q = p // 2
    return (2 * q) ** 2 - q + 1


def bound(p):
    kdot = -1 - p
    sq = -2 if p % 2 == 1 else -1
    return abs(kdot) + sq, kdot, sq, coeff(p)


def main():
    rows = []
    for p in [1, 2, 3, 4, 5, 6, 7]:
        b, kdot, sq, c = bound(p)
        gmin = (b + 2) / 2
        rows.append((p, c, kdot, sq, b, gmin))
        print(f"p={p} c={c} K.S={kdot} sq={sq} 2g-2>={b} -> g>={gmin}")
    # Target-relevant checks: p=1 gives g>=1 (no upper bound), p=3 gives g>=2
    checks = {1: 1.0, 3: 2.0}
    ok = True
    for p, want in checks.items():
        got = next(r[5] for r in rows if r[0] == p)
        status = "OK" if got == want else "FAIL"
        if got != want:
            ok = False
        print(f"check p={p}: lower bound g>={got}, expected >={want} [{status}]")
    # Lemma 3.1 transfer (purely algebraic statement, recorded not proved here):
    # any class v with v^2=-2 (odd p) equals +-S_p, so a diffeomorphism
    # X_3 -> X_1 must send S_3 to +-S_1. No computation needed.
    print("Lemma3.1-transfer: recorded (diffeomorphism must send S_3 to +-S_1).")
    if not ok:
        sys.exit(1)
    print("VERIFY_OK: lower bounds g1>=1, g3>=2 reproduced; "
          "upper bound g1<=1 and W1-twist identity NOT established.")


if __name__ == "__main__":
    main()
