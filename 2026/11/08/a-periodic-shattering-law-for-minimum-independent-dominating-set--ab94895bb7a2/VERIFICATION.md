---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The claim is about all finite path sizes; its unrestricted validity rests on the gap/threshold proof in `RESULT.md`, not on finite enumeration. The independent program `verify_i_path.py` uses only Python 3 standard-library modules and can be run in a folder containing the mathematical result via `python3 verify_i_path.py`.

The program independently enumerates every minimum-cardinality independent dominating set of \(P_n\) through a gap recursion and, for \(n\le16\), compares against brute enumeration of *all* vertex subsets with explicit independence and domination tests. It exhaustively compares each shattered-support count of orders zero through three with the claimed polynomial for \(1\le n\le43\). It computes the exact adaptive tree recursion for the one-deficiency residue class through \(k=10\), and independently enumerates all two-time state pairs through \(r=15\).

On execution the checker reports `MIN_I_PATH_SHATTERING_AND_ONLINE_PASS n=1..43; brute n=1..16; online k=0..10; gap pair types r=3..15`. The finite cutoff is not an infinite proof. The proof's nonstandard steps that require human checking are the exhaustive classification of shattered pairs and the table excluding all three-query supports. The exact adaptive dimension for \(n\equiv1\pmod3\) is outside the claim. No independent audit has been performed.
