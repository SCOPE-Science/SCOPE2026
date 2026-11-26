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

Independent finite extension of the two linear orders realizes every pair of insertion gaps. When both gaps differ, their differences force each orientation; when a gap is shared the two new points can be put in either order within it. Thus the formula includes equality and diagonal ones. For the integral presentation, take successive differences on both axes of the column relations. The mixed difference is -e_{k-1,l-1}-e_{kl}; the two boundary difference lists are the row/column tail sums, and the corner relation may be taken at (n,0), where it is the total sum. The change is reversible by summation. The mixed differences eliminate all interior variables with unit pivots, leaving alternating signs on each diagonal. Consecutive tail-sum differences then identify v_{n-k}=(-1)^k u_k for 1<=k<n; the other list yields (1-(-1)^n)u_k=0. One last row sum eliminates the shared diagonal variable u_0 and the total sum eliminates v_n, leaving u_n free. The last opposite tail sum imposes sum_{1<=k<n} [(-1)^n-(-1)^k]u_k=0. This is redundant modulo 2u_k for odd n and is twice a primitive linear form for even n, since then n>=2 and u_1 has coefficient 2. At n=1 the inner lists are empty and just one generator remains free. The stated cokernels, unit counts, and field ranks follow without using a rank comparison to infer the integral torsion exponent.

## originality

PASS

The reviewed advance is the all-order integer Smith classification of a natural grid kernel, not the classical existence of the homogeneous permutation or the finite-extension derivation of its entries. Comparison under coordinate reversal and the grid-zeta formulation found no demonstrated prior coverage. Distinct catalogue analogues with unavailable full passages are retained as bounded comparison risks.

## value

PASS

The matrix is motivated by extension feasibility, and independently is a natural comparability matrix of a square grid. A complete integral presentation distinguishes parity-dependent free rank from genuine 2-torsion and rules out higher prime powers, neither of which follows from a characteristic-two rank table. The result gives exact working invariants for related gap-kernel and order-feasibility calculations, not merely a few small spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
