---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For W_k=(0123)^k, greedy embedding requires 1+D(v) permutation blocks; deleting any letter reduces weak-descent count by at most one. Thus D(v)=k, decreasing first/last adjacent pairs and all interior local decrement Delta(a,b,c)=1 are necessary/sufficient for a minimal absent scattered subsequence. The 16 pair-state transfer has F=z e^T(I-T)^{-1}e; inspected certificate.json defines H,Q,P and the polynomial verifier checks (I-T)H=Qe and z e^TH=P with Q(0)=1. Independent dynamic-programming recurrence confirmed 14 successive k coefficients through k=14. Universal identity relies on the exact finite-degree polynomial certificate and combinatorial proof, not this finite prefix.

## originality

FAIL

A published November 2 general-q statement already gives exactly the identical weak-descent criterion and q²-state bivariate transfer formula for every q>=3. Specialize q=4 and set the length variable to 1 to obtain this exact quaternary all-minimal enumeration; the displayed order-10 numerator/denominator are an exact algebraic evaluation of that already covering formula. Numerical coefficients need not match prior typography for their consequences to be covered.

## value

FAIL

The host alphabet and all-minimal antichain are natural, but the proposed contribution is a fixed-q rational simplification of a previously published all-q exact transfer enumeration. No separate structural invariant, exceptional behavior, nontrivial new bound or motivated independent mathematical gap survives the known general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
