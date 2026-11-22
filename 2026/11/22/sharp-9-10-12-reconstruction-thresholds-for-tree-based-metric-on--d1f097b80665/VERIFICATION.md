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

# Exact finite verification

Running `python3 artifacts/verify.py` recomputes all unlabelled trees from one through twelve vertices by leaf attachment, removes duplicates with centre-rooted AHU canonical codes, computes the complete polynomial of distance-\(1\) and distance-\(3\) label counts for every tree by an exact three-state dynamic program, and groups the resulting polynomials into scalar, occupied-distance and full-grade coincidence classes.

The class counts are \(1,1,1,2,3,6,11,23,47,106,235,551\), independently matching the unlabelled-tree enumeration A000055. First collision thresholds are nine, ten and twelve, with exactly one collision fibre containing two trees at each threshold. The exact coefficient vectors and witness edges are supplied in `artifacts/witnesses.json`; the full-order summary is in `artifacts/census.tsv`. For all six threshold witnesses, a separate direct enumeration over each of the \(3^n\) three-valued distance assignments independently verifies every coefficient from the tree dynamic program. At the nine-vertex scalar witness, an additional check evaluates every pairwise triangle inequality in the corresponding full metric. The accompanying captured stdout ends with `VERIFY_OK` and records the actual integer comparisons.

The finite census exhaustiveness relies on two mathematical facts: every nontrivial tree has a removable leaf, and the centre-rooted AHU code is a complete invariant of tree isomorphism. Thus the algorithm is exhaustive without enumerating all labelled trees. The dynamic-program recurrence has an induction proof in `RESULT.md`; the program's assertions corroborate these proofs rather than substitute for them.

To regenerate the tabular and structured witness artifacts, run `python3 artifacts/build_evidence.py` with `verify.py` in the same directory. Both programs use only the Python 3 standard library. No external data downloads or proprietary dependencies are required.

The earliest source date is taken from the arXiv version history, not from a later journal date. The main originality risk is possible unindexed earlier study of fixed-target Widom–Rowlinson tree homomorphism collision polynomials. The self-review is described in `REVIEW.md`; independent mathematical audit has not been performed.
