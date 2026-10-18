---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

FAIL

The numerical rational counterexample itself is correct: eigenvalues of P are 2,1, Q are 39/20,1/20, and <Pf,Qf> at (1,-3/2) is -1/40. However the advertised universal exact repair iff Q S_Lambda P∈GL+(H) is FALSE in the expressly real Hilbert-space setting. Set S_Lambda=I, P=diag(2,1), Q=[[1,1/10],[1/10,1]]; QP=[[2,1/10],[1/5,1]] is nonsymmetric, hence not GL+, while every real quadratic value <Pf,Qf>=f^T((QP+PQ)/2)f is bounded above and below by positive multiples of ||f||², because symmetric part [[2,3/20],[3/20,1]] has positive trace and determinant 791/400. Correct real iff condition is positivity of the symmetric part, not self-adjointness of QSP. In complex Hilbert spaces the requirement of real quadratic energy is different. The package does not distinguish these settings. A partial correct counterexample cannot validate the complete final claim; no full scientific correction with all affected files was staged.

## originality

PASS

The named 2026 source Theorem 2.1 explicitly asserts equivalence for arbitrary positive controls and its universal Corollary 2.2. Earlier literature explains that products of positive operators need not be positive, and published related controlled K-g-fusion counterexamples show similar mechanisms, but they target distinct operators/theorems. The exact source-specific one-point negative witness appears not to be fully stated in compared earlier sources; this is best-of-knowledge O for surviving witness, despite failed complete claim correctness.

## value

PASS

A counterexample falsifying a central general-frame equivalence in the smallest nontrivial dimension is materially useful; the quadratic-form flaw is structural. A corrected criterion would require symmetric part in real spaces, but the invalid original exact-iff assertion prevents acceptance of the full package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
