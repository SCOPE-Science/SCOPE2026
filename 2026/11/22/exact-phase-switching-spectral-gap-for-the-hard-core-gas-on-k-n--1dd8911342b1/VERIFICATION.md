---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The two labeled product cubes share only the empty vertex. In the reversible Euclidean representation the odd shore-exchange sector has zero empty coordinate and is exactly the killed negative generator A. The even sector has a doubled reversible weight on every nonempty paired state, so after deletion of the empty coordinate its principal submatrix is again A (the extra √2 factors are only in couplings to the deleted vertex). Its first eigenvalue is zero and interlacing bounds its second below by the least eigenvalue of A; that least eigenvalue is realized in the odd sector. This argument covers the full state space, not only occupancy counts. The unglued cube return probability is (1+λ exp(−bt))^n/b^n, b=1+λ. Its resolvent cofactor therefore vanishes in (0,b) at exactly the stated secular root, since the diagonal resolvent is strictly increasing from −∞ to +∞; positive definiteness and interlacing identify the first Dirichlet eigenvalue. The sum at fixed a strictly increases with n by binomial coefficient comparison, which independently proves strict size descent. For n=1 the root is 1. For n=2 the two-state killed count matrix has trace 3+λ and determinant 2, giving the claimed smaller root; site-permutation symmetry of the unique positive ground state legitimizes this count calculation. For fixed p=λ/b, write m=np and u=1−p. Taylor expansion of E[1/X; X≥1] gives 1/m+u/m²+u(2−p)/m³+O_p(n⁻⁴): in the central window use the second and third centered moments m u and m u(1−2p), the fourth 3m²u²+O(n), signed fifth O(n²) and absolute sixth O(n³); the discarded window is exponentially small. Writing the root as g=1/S_n(g), g≤1/S_n(0)=O_λ(n b⁻ⁿ), and (S_n(g)−S_n(0))/S_n(0)=O_λ(g/n)=O_λ(b⁻ⁿ) by the inverse second moment bound. Inversion yields 1−1/(λn)−b/(λ² n²) times nλ/b^n with the claimed relative remainder. The frozen scripts and recorded checks were read, not executed; the structural proof and moment calculation establish the universal claims.

## originality

PASS

Flegg and Pollett already give the very same killed-Ehrenfest secular root, and in fact all the corresponding killed count-chain decay parameters. No originality is credited to that polynomial, the equivalent binomial equation as a killed-process statement, or its unglued product resolvent. The distinct contribution of the frozen Finding is that this root is the exact gap of the full balanced hard-core chain, plus the all-size comparison and fixed-activity relaxation expansion through two relative corrections. The inspected hitting-time and distinct same-day point-killing results do not imply this full-chain identification or that expansion.

## value

PASS

The biclique is a natural two-phase hard-core test with an exponential relaxation bottleneck. An exact full-chain relaxation rate is useful here specifically because a count-chain computation alone need not exclude slower labeled modes. The identified rate provides a benchmark across all sizes and activities, and the fixed-activity two-term relative correction quantifies how far the true relaxation rate is from its leading metastable prefactor. This is a different invariant from an expected transition time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
