---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The scalar quadratic terms with non-top value are graph homomorphisms to the product path a-b-c-d. A bipartite graph admits such a map, and a missing edge can be separated even when its endpoints have opposite colours: label those endpoints by the two nonadjacent ends of the path, and map the remaining vertices in each colour class to their compatible middle label. Same-colour and disconnected endpoints can be assigned one common colour. Different linear sets separate by evaluating the second form at omega while the first includes a term taking an incomparable value. The excluded empty support is replaced in the count by the absorbing cube. Jiao's exact normal-form and separation lemmas prove the same cancellation for ordered matrix supports, including loops, at every size k>=2. As a direct check, at matrix entry (1,2) and intermediate index 1, choose the (1,1) entry to be a for the first offending variable and c otherwise, and the shared (1,2) entry to be d for the second offending variable and b otherwise. Only the selected ordered pair gives top there; at intermediate 2 the (2,2) entries c make all products omega, and any further indices can use b,c. This also separates a missing loop. The formal EGF follows from the labelled exponential formula, and the upper/lower bounds give the ratio of logarithms, not a ratio of dimensions. Independent closure under the operations on projection signatures gives scalar ranks 1–4 as 2,5,17,86 without using the graph normal form. Replay: python3 /workspace/review_evidence/check_3.py.

## originality

FAIL

The scalar bijection itself, not merely the abstract equational theory, is a direct corollary of the proof of Lyu–Ren–Yue Proposition 4.5. Lemma 4.2 lists all possible nontrivial monomial inequalities in an embedded subsemiring, and Proposition 4.5 imports that list for the same six-element semiring then eliminates its sole non-absorbing case (a missing quadratic joining an odd-path pair). Thus a nonempty regular bipartite support admits no additional monomial in a valid inequality. Equality of two such polynomials implies both inclusions of their monomial supports, while the other cases are exactly the absorbing expressions. Counting these scalar supports is the immediate binomial transform of a known labelled graph count. The matrix supports are already completely classified by Jiao, as acknowledged. The scalar EGF then multiplies a known square-root EGF by e^z, and elementary counting bounds give the growth ratio. Lack of an exact previously printed semiring sequence does not undo this coverage.

## value

FAIL

Free spectra are a useful invariant and the scalar–matrix comparison is intelligible, but the claimed addition here is only direct enumeration of fully determined normal forms, a standard labelled EGF transform, and elementary growth bounds. No new needed classification, obstruction or structural consequence survives the exact prior coverage; the ratio is immediate once the prior supports are counted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
