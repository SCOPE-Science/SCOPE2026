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

For the symmetric irreducible kernel, the weighted Laplacian has kernel exactly the constants; the inverse trace on their orthogonal complement is the zero-diagonal Kemeny sum. Periodicity adds no exception. The resistance pair sum counts four copies of each core pair and 2m-1 contributions from each pendant bridge; dividing by 2m gives the asserted trace formula, including when the positive core support is a connected subgraph. For a positive definite Q the inverse-trace second variation in a nonzero symmetric direction D is twice tr(S²Q^-1)>0 with S=Q^-1/2 D Q^-1/2. Averaging over core automorphisms extended to the leaves therefore preserves the mean pendant rate and improves strictly unless the kernel was invariant. At fixed invariant pendant rate a, increasing the common core rate to (1-a)/d strictly improves the cost unless already saturated. Irreducibility gives 0<a<1. Thus the exact constrained minimum is B/(1-a)+C/a, and completing the square gives precisely the displayed regret and its sharp equality case. The cyclic specialization follows from the reciprocal Laplacian sum; for example the equal-edge cost is (3/2)B+3C, giving the stated polynomial and limiting ratio.

## originality

FAIL

A distinct indexed record gives the same unrestricted optimization in the strictly larger family with any fixed number r of private leaves per core vertex. Its proof already gives the exact fixed-mean minimum with the same equality conditions. The regret display is an algebraic rewrite of that minimum and the sunlet comparison is its r=1 cycle specialization. This is demonstrated statement/proof coverage, not an inference about publication order from a shared date.

## value

FAIL

The unrestricted exact design problem is worthwhile, but after removing the covered optimizer and sunlet formulas the only changed deliverable is the completed-square expression of the already available fixed-mean minimum. Its sharpness and equality classification are inherited unchanged. That is a convenient presentation, not an independently useful new mathematical gap resolved by the frozen finding; the alternate resistance derivation does not add a claimed new structural theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
