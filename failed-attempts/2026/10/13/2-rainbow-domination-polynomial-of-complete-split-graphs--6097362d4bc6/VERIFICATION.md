---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For S_{r,n}=K_r join independent n, r,n>=2, split by whether independent-side vertices receive any empty labels. The resulting two disjoint cases establish the candidate three-term formula. Independent literal-definition enumeration for all (r,n) in 2..4 with r+n<=7 matched every weight coefficient, total and minimum. The claimed minimum gamma=2 and count r^2+2 if n=2, else r^2, also follow from the formula. The symbolic case partition, not finite testing, establishes arbitrary r,n.

## originality

FAIL

FAIL: The candidate asserts S_{r,n} is not complete multipartite for r>=2. In fact S_{r,n}=K_{n,1,1,...,1}, with exactly r singleton parts and one part of size n. The already published Resultary finding All 2-rainbow dominating functions of complete multipartite graphs explicitly counts the same all-weight labeled functions by an exhaustive multinomial profile formula for every K_{n1,...,nk}; substitute (n,1,...,1) and collect profiles. Therefore the candidate is fully covered as a prior theorem specialization, even though the displayed algebraic form differs. The October 13 source overlooked a published October 4 result and its own asserted noncontainment is false.

## value

FAIL

FAIL: The closed polynomial is a convenient simplified specialization, but the exact invariant for the entire graph family is already determined by the published all-weight complete-multipartite theorem. Algebraic evaluation of its singleton-part profile sum supplies no motivated new structural boundary or mathematical gap, so the claimed new classification is a known result in different notation. Correct computation and reproducibility do not salvage value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
