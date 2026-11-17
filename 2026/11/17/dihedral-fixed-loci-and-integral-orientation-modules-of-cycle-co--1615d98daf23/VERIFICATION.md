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

# Exact checks and scope

The standalone Python 3 verifier `VERIFY.py` is dependency-free. Run `python3 VERIFY.py` in the directory containing the extracted artifacts. It reconstructs all \(2^n-2\) orientations of \(C_n\) for \(3\le n\le12\), all \(2n\) elements of the vertex-dihedral group, and each action on oriented reference edges, then counts invariant acyclic orientations directly. It independently obtains each orientation sign by counting inversions in the vertex permutation. Separately, it forms the vertex-orbit quotient graph for each symmetry, detects equalities within a vertex orbit, enumerates its acyclic orientations, and compares its fixed-arrangement Euler characteristic to the Lefschetz expression \(1+(-1)^{n-3}\chi_n(g)\). It also verifies that every averaged invariant Betti rank is a nonnegative integer. The 150 independent group-element cases pass.

The file `verification_output.txt` records the exact reproducible output including all per-size invariant dimensions and the terminal success marker. No Smith-normal-form code is needed because the written long-exact-sequence proof identifies the homology module over \(\mathbb Z\) directly. These finite checks are not claimed to prove statements beyond order 12: the all-size conclusions rest on the geometric chamber argument and uniform orbit counting in `RESULT.md`.

No independent audit has been performed. An unindexed mathematical equivalence remains possible; the proof does not calculate integral homology of the full geometric quotient.
