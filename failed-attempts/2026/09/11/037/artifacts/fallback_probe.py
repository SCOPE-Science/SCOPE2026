"""Lane-772 fallback probe: bounded attempt at the valuable partial fragment.

PARTIAL FRAGMENT (from survey_profile.valuable_partial_target):
  "A verified Ctau algebraic-Novikov differential at stem 53 with its
   C-motivic lift and logged Betti image, even if the final classical
   naturality needs more work."

WHAT THIS SCRIPT DOES (stdlib only, deterministic):
  1. Reuses the certified admissible-basis counts from lambda_probe.py
     (deg-53 length distribution {1:1, 2:17, 3:63, 4:68, 5:22}, total 171)
     as an UPPER BOUND on candidate source slots across filtrations 1-5.
  2. Checks each requirement of the fragment against available in-lane data:
     (a) named nonzero alg-Novikov differential on Ctau at (stem 53, filt);
     (b) explicit C-motivic lift with stated (s,t,weight) triple;
     (c) logged Betti image with matching bidegrees in machine Ext.
  3. Reports PASS only if all three are certifiable; otherwise BLOCKED.

RESULT: BLOCKED (documents ATTEMPTED_AND_BLOCKED, not a finding).
REASON: (a) needs Gheorghe Ctau tables (unreachable); (b) needs a unique
  certified (s,t,w) triple, but 171 raw candidate slots with zero certified
  differential ranks cannot single one out; (c) needs Bruner machine Ext
  (unavailable in lane). No guessing permitted by the audit plan.
USAGE: python3 fallback_probe.py  (stdlib only, deterministic)
"""
from lambda_probe import admissible_monomials, adm_basis, ext_dims


def main():
    print("== fallback attempt: partial Ctau fragment at stem 53 ==")
    # Step 1: candidate source slots (upper bound from certified counts)
    b53, d53, r53 = ext_dims(53, 6)
    total = sum(len(b53[f]) for f in range(1, 6))
    print(f"candidate source slots filtrations 1-5: {total} "
          f"({{1:{len(b53[1])}, 2:{len(b53[2])}, 3:{len(b53[3])}, "
          f"4:{len(b53[4])}, 5:{len(b53[5])}}})")
    print(f"certified differential ranks: {dict(r53)} "
          f"-> all zero: {all(v == 0 for v in r53.values())}")
    # Step 2a: Ctau alg-Novikov differential
    print("check (a) named nonzero Ctau alg-Novikov differential: "
          "MISSING (Gheorghe tables unreachable; zero certified ranks)")
    # Step 2b: motivic lift triple
    print("check (b) explicit (s,t,weight) lift: "
          f"AMBIGUOUS ({total} raw slots, 0 certified classes; "
          "no unique triple nameable without machine Ext)")
    # Step 2c: Betti image log
    print("check (c) Betti image in Bruner Ext: "
          "MISSING (no machine-Ext toolchain in lane)")
    print("FALLBACK VERDICT: BLOCKED "
          "(partial fragment attempted, all three legs unanchorable)")
    # Cross-check: admissible monomial sanity (independent count route)
    print(f"cross-check admissible deg-53 monomials: "
          f"{len(admissible_monomials(53))} (expect 171)")


if __name__ == "__main__":
    main()
