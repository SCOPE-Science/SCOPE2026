---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each fixed labeling of the queried prefix there is one set of possible suffix states, with the choices at unqueried coordinates unioned separately for that labeling. Taking both successors at a query preserves the universal quantifier over labels; a lost labeling cannot be recovered. All nondead suffix states accept the empty continuation. This proves the automaton invariant for every length, including the empty support. An independent reconstruction found 26 reachable nonsink families and the stated seven accepting classes plus sink, distinguished by future acceptance. Exact transfer-matrix determinants gave the displayed bivariate numerator and denominator. Multiplication checked A^11=A^6+3 on all 49 entries; scalar shifts commute with max-plus multiplication, so the identity propagates to every later length, seeded by the maxima 1,2,3,3,4,4,5,6,6,7. Independent trace enumeration agreed for all 2,047 supports at lengths 0–10, including both displayed polynomials. Replay: /workspace/branches/b1f763dc-46c0-4dc0-a79f-13d5f1a475c0/recompute_0011.py and recompute_0011.log; the direct trace check is bounded, while the finite identities plus induction prove the full claim.

## originality

PASS

The known machinery gives a means of recognition and enumeration, not the specific seven-state reduced description, weighted series, or five-step degree identity for this factor. Bounded comparison found no equivalent classification or broader quantitative theorem supplying it.

## value

PASS

For the entire language defined by one short contiguous forbidden word, the shattering complex is a natural invariant: it tells exactly which labeled coordinate sets admit every labeling. A minimal recognizer exposes nonlocal obstructions, the bivariate series counts every support, and the rate and boundary correction sharpen the naive prohibition on selecting four consecutive positions. These are useful quantitative benchmarks for other constrained languages, not just an instance of the general existence of a DFA.

The dated certificate retains the supplied scientific assessment, sources and limitations.
