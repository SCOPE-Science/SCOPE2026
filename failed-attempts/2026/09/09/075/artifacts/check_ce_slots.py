"""Lane-480: Cartan-Eilenberg slot grid for the killing-window bidegrees (stdlib only).

Conventions (Burklund-Xu 2302.11869 v3, Sec 2.1; Remarks 2.4/2.5):
 - CE E2^{s,k,t} = Ext_P^{s,t}(F2, Ext_Q^k) => Ext_A^{s+k,t}(F2,F2).
 - Window target: Adams filt F = 2+r, internal t = 253+F (stem 253).
   Slots: s = 0..F, k = F-s.
 - GWX/algebraic-Novikov comparison sees only even t' = t-k (Remark 2.4:
   motivic/alg-Novikov Ext vanishes for odd t'). t-k = 253+s, so even <=> s odd.
   Even-s slots are comparison-blind (not zero, just invisible to that leg).
 - Coarse degree feasibility: each q-factor has odd internal degree >= 1, so
   t_Q >= k with t_Q = k mod 2; Ext_P needs even t_P = t - t_Q >= 2s
   (P = F2[xi_1^2, xi_2^2, ...], smallest generator degree 2).
   Feasible iff exists t_Q = k mod 2 with k <= t_Q <= t - 2s.

Result: lists, per window leg, the comparison-visible (s odd) slots and whether
coarse degree tests eliminate any (they do not — honest negative result that
structures the Leg-A search without claiming Ext (non)vanishing).

Run: python3 output/artifacts/check_ce_slots.py -> CE_SLOTS_OK
"""
import sys

def main():
    N = 253
    for F in (7, 8, 9, 10, 11):
        r = F - 2
        t = N + F
        print(f"F={F} (d_{r} target, t={t}):")
        for s in range(0, F + 1):
            k = F - s
            tp = t - k  # = N+s
            assert tp == N + s
            visible = (tp % 2 == 0)
            # coarse feasibility over odd-s (visible) slots
            feas = "n/a (comparison-blind: t' odd)" if not visible else ""
            if visible:
                lo, hi = k, t - 2 * s
                ok = lo <= hi  # parity auto: t_Q=k mod 2 attainable since step 2 within [lo,hi]? need hi-lo>=0 and parity match at lo
                feas = "coarse-feasible" if ok else "COARSE-EXCLUDED"
            print(f"  s={s} k={k} t'={tp} w={tp//2 if visible else '-'} [{ 'visible' if visible else 'blind'}] {feas}")
    print("CE_SLOTS_OK")

if __name__ == "__main__":
    sys.exit(main())
