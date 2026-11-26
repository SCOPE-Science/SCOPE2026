---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The theorem is correct for ordinary powers, m≥2 and ℓ≥4. For each of the top three distinct eigenvalues of the ℓ-vertex path, zero at the center and arm multiples with coefficients summing to zero give m−1 independent spider eigenvectors. The annihilating cubic Q(A)=A³−s₁A²+s₂A−s₃I has entries 1 at distance three, −s₁ at distance two, and deg(u)+deg(v)−1+s₂ on edges (count the two ways to backtrack along the length-three walk and subtract their duplicate). Beyond distance three all entries vanish. Here s₁>0 and s₂≥0 for ℓ≥5; at ℓ=4, s₁=φ and s₂=(√5−3)/2>−2, whereas the walk count on any edge is at least 2. Thus Q is an exact-pattern nullity witness. Starting with the outer three vertices on m−1 arms, each depth t+3 forces t inward; these sources have depth at least four. Depths 3, 2, 1 in one of those arms then force the center and depths 1, 2 of the last arm, followed by the center forcing depth 3 and ordinary inward-to-outward spacing-three propagation. This also works at m=2 and ℓ=4. The inequalities null(Q)≤M≤Z and the forcing upper bound prove equality and hence the rank. Replay: RESULT.md lines 17–39 give the symbolic certificate; verify.py and verify_output.txt were inspected, not executed, and only corroborate finitely many cases.

## originality

FAIL

Two distinct earlier published Resultary records prove the full scalar claim with no additional hypotheses on the assigned case. The frozen record uses a different, correct cubic witness, but does not newly resolve the conjecture's cubic case or newly determine the minimum rank.

## value

FAIL

The conjecture is meaningful and the cubic witness is a useful exposition of the existing spectral criterion. However, the claimed exact invariants are already provided in broader scope; the different proof is a short path-eigenvalue specialization plus a walk count. No independently useful new property of the cubic matrix or new application is established as a separate surviving finding. No repair is proposed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
