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

The mathematical proof identifies sextactic points with \(E[6]\setminus E[3]\), six-point conics with zero-sum six-subsets, and reducible conics with subsets partitioning into collinear zero-sum triples. It uses \(Y^2=X^3-432\) to determine the only three possible Frobenius actions, and a complete fixed-subset count for the rational smooth-conic number 22 in the involution case.

Two standalone Python 3 scripts use only the standard library. Run `python verify.py` to construct actual torsion-point coordinates and projective lines over splitting fields of the prime fields with characteristics 5, 7 and 31, checking their Frobenius permutations and rational incidences. It must print `VERIFY_SEXTACTIC_LINES_OK`.

Run `python verify_conics.py` to enumerate all \(\binom{27}{6}=296010\) possible six-subsets in the abstract \(E[2]\oplus E[3]\) model, test all four modular group-coordinate sums, detect reducibility through zero-sum three-subsets, and enumerate full Frobenius cycles for all three actions. It must print `VERIFY_SEXTACTIC_CONICS_OK`. This second test is an exhaustive combinatorial check in the universal, finite 27-element group model, not merely a sampled finite-field experiment. It establishes totals 8244 conics, 2268 reducible, 5976 smooth and all reported cycle multiplicities. The mathematical identification of this model with each geometric conic is proved separately in `RESULT.md`.

The sources inspected document the earlier complex geometric counts and arrangements; no independently adjudicated novelty finding or independent audit is asserted. The full results concern the fixed Fermat plane cubic in characteristic at least five and do not determine singularities of the conic arrangement away from sextactic points.
