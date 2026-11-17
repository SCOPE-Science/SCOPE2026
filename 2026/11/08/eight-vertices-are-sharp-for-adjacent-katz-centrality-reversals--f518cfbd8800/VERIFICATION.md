---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For trees the determinant D(t)=det(I-tA) is the matching polynomial with positive value for 0<t<1/rho(A). Multiplying the resolvent by D gives numerator coefficients N_v(t)=sum_{k<n}(sum_{j<=k} d_j (A^(k-j)1)_v)t^k. The exact rational barrier R>=1/rho maps t=R x/(1+x) to x>0; uniform transformed coefficient signs certify no zero or reversal on the entire admissible interval. Independent exact test on nonisomorphic trees n=2..8 reproduced edge totals 1,2,6,12,30,66,161 and precisely two uncertified/reversing edges, both on n=8. Independent rational-adjugate evaluation and max row sums of A^4 verify signs at (1/3,3/7) and (1/4,1/3) strictly inside admissible intervals. Complete Prüfer and canonical-tree method supports exhaustiveness; this does not imply for general graphs.

## originality

PASS

Katz 1953 and Benzi–Klymko identify attenuated walk centrality and parameter-dependent ranking limits; Aprahamian–Higham–Higham study matching resolvent to exponential centralities. None of their inspected statements characterizes the smallest tree on which *adjacent* endpoints reverse ordering for one fixed graph and uniform baseline, or classifies the two order-8 cases. Related centralization and PageRank finite thresholds change statistics/models and cannot imply this exact certificate.

## value

PASS

The first size of adjacent local ranking instability under a natural centrality parameter, with full minimal-case classification and rigorous exact integer sign certificates, is a motivated, reusable combinatorial spectral invariant. Not dependent on a downstream general graph theorem or arbitrary unmotivated numeric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
