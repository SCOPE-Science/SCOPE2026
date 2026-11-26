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

On the fixed subspace orthogonal to the all-ones vector, lambda2 is the minimum Rayleigh quotient even when weights disconnect the support. Hence W is convex, and averaging over leaf permutations and the hub exchange preserves b and cannot increase W. In the averaged matrix, the leaf-difference eigenvalue is a (absent for m=1), the symmetric sector contributes 0 and (m+1)a, and the antisymmetric sector has polynomial x²-((m+1)a+2b)x+2ab. For a,b>0, its signs at 0, a and (m+1)a put its roots strictly outside the other nonzero eigenvalues, and continuity covers a=0 or b=0. Substituting b=1-2ma gives W²=4-(12m+4)a+(9m²+10m+1)a². Its unconstrained stationary point has positive b for m=1,2 only; otherwise the interval minimum is at b=0. The values are (a,b,W²)=(2/5,1/5,4/5), (14/57,1/57,32/57), and (1/(2m),0,(m+1)²/(4m²)), respectively. For an arbitrary minimizer at m>=3, its bridge equals the averaged bridge and is zero. The Rayleigh lower bound (m+1)S_j/m for star j forces half the budget on each; equality makes the test vector (m,-1,...,-1) a top eigenvector and the leaf equations force uniform weights. For m=1,2, equality in the width average forces equality in the separate top-eigenvalue bound. The top vector of the averaged matrix has the same squared edge differences within each pendant orbit; its Rayleigh value in the unaveraged matrix is therefore the same and maximal. Its leaf equations force uniform weights as the leaf-hub difference is nonzero. This verifies uniqueness without assuming symmetry. Positive allocations approximate the boundary optimum, but no such allocation attains it for m>=3. The archived checker is diagnostic, not the proof; it was inspected, not run.

## originality

PASS

Prior work explicitly gives the general width-design problem and disconnected optimal supports. The verified distinct statement is the exact all-size optimizer, first bridge-deletion threshold, and uniqueness for unconstrained individual edge allocations on the balanced double star. This is not a claim to the objective, convexity method, or first example of disconnection.

## value

PASS

Minimizing spectral width is a natural network-design criterion. On this family, the answer determines the exact first size at which that criterion sacrifices the sole link between communities, and proves that deleting it is necessary rather than one symmetric choice. The closed form supplies a benchmark and distinguishes when a positive-connectivity requirement changes attainment. It does not generalize the cutoff to other graph families or claim that optimal support disconnection was previously unknown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
