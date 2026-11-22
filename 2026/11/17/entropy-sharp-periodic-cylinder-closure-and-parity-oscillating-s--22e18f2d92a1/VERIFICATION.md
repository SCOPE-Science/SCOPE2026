---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For a finite irreducible 0-1 adjacency B with lambda>1, every p<n closing period gives exactly tr(B^p) distinct length-n prefixes of p-periodic infinite paths; the denominator is A_n=1^T B^(n-1)1. Nonprimitive graph period d is retained. Irreducible Perron-Frobenius bounds make A_n comparable to lambda^n, and the trace is O(lambda^p); summing p<=n-k gives the upper lambda^-k bound. For the lower bound choose the largest multiple of d at most n-k, whose trace is d lambda^p+o(lambda^p) (d simple peripheral eigenvalues). The upper/lower bounds hold uniformly for 1<=k<=n-L. Tail-sum identity yields the three regimes for E exp(t Z_n); graph path closing overhead is bounded by strong connectivity, so E eta_n=n+O(1) and variance O(1). The exact R_n trace identity and residue class limits follow from the same cyclic PF decomposition. The K3 no-repeat eigenvalues (2,-1,-1) give 2/3 and K_(2,3) bipartite eigenvalues (+sqrt6,-sqrt6) give odd/even 12/25 and 1/5; independent finite K3 enumeration checked counts for n<=11. No finite run was extrapolated to the general statement.

## originality

PASS

PASS best-of-knowledge: periodic specification and PF are classical, as are unrestricted word borders; however the combined uniform word/shortest periodic closing deficit, sharp entropy-critical moments for irreducible possibly imprimitive matrices, and exact parity-dependent shorter-period count are not implied by the inspected unrestricted random-word theorem or other indexed shift results. Physical three-rotor periodicity is explicitly outside scope.

## value

PASS

A uniform finite-type shift periodic-closing statistic is a natural combinatorics/dynamics observable. The sharp entropy-tail and exponential-moment transition distinguish summability regimes, and the irreducible but nonmixing parity limit is an informative boundary case. Even though PF is classical, these precise finite-word limit quantities are useful and nonroutine.

The dated certificate retains the supplied scientific assessment, sources and limitations.
