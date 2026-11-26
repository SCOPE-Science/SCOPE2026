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

The derivation identity on the alternating bracket forces D=(A,0;w,tr A) in block notation, with all six entries of A,w free, including in characteristic two. The frozen proof's explanation at lines 73–76 is imprecise: the last column need not be independent of the first two as written (take A=diag(1,0) and w=(0,1) over F₂). However, for nonzero τ=tr A, each v in ker A extends to a unique kernel vector (v,−wv/τ), proving the stated rank formula rank D=rank A+1. At τ=0 the rank rises by one exactly for w outside row(A). Counting rank-one A=uvᵗ modulo rescaling gives q²−1 of trace zero and q(q²−1) of nonzero trace. Among the q³ trace-zero matrices, q²(q−1) are nonsingular. These counts and the free row give the four stated rank coefficients. Nilpotence holds exactly when A is nilpotent, with q² choices for A and q² for w. Then D² has only the lower-left block wA. For A≠0 nilpotent the left kernel of A equals its one-dimensional row space; this gives the stated index counts and identifies the nonzero square-zero maps with the rank-one maps. Independent parameter enumerations over F₂,F₃,F₄,F₅,F₇ agreed with all coefficients; direct checks of all 512 and 19,683 linear maps over F₂ and F₃ found 64 and 729 derivations, respectively. Methods, outputs and scope: /workspace/branches/ec3a9923-cc39-4502-9dd1-2c95db36d314/independent-check-record4.md, lines 10–30. The supplied verify.py was inspected, not executed. The finite checks corroborate but do not prove the field-uniform formulas. The finding is correct with the indicated proof justification; the frozen file remains unchanged.

## originality

FAIL

A distinct indexed result gives a complete, strictly finer census of the very same ordinary H₃ derivations over every finite field, tabulated by similarity class of the quotient block and central-row stratum. The rank and nilpotency enumerators follow by coarsening that census, including the characteristic-two case. This is a mathematical implication of the inspected result, not merely a matching title or a chronological priority inference.

## value

FAIL

The rank and index are natural invariants, and the census is correct. But the exact counts and structural observations here are obtained by summing a fully specified existing orbit table and applying elementary rank and square-zero tests to its representatives. The submission does not isolate a new invariant, regime or boundary needing further mathematics; recomputing this known coarsening is not an independent research-level contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
