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

Write p=E11, n=E12, L=E11+E21, and W=(Fp+Fn) plus M2(F)omega. In the specified multiplication, p(a+b omega)=pa+(bp)omega and likewise for n. The first components have zero second row, and right multiplication of b by p or n fills the first or second column respectively; therefore pO+nO=W, and every Phi value lies in W. With y=A+B omega and x=L, the first component is pLA-nAL=(a11-a21-a22)p+a12 n. The second component is B(Lp-bar(L)n)=B times the matrix with rows (1,0) and (1,1). For any target sp+tn+C omega take A with first row (s,t) and zero second row, and B=C times the matrix with rows (1,0) and (-1,1). This constructs a preimage in the fixed slice over every allowed field. The six target coordinates are independent. The determinants of p,n,p+n vanish, proving the stated norm orthogonality, and p,n are independent nonzero zero divisors. Parentheses are kept as in Phi, without associativity of the octonion algebra. The frozen verifier and its determinant-one-minor output were inspected, not executed; this algebraic check does not rely on that run.

## originality

FAIL

The cited v1 genuinely left a span-versus-image gap. The current v2 of the same paper establishes the image for the entire independent orthogonal zero-divisor case and gives the identical fixed surjective slice for this pair as a normal-form specialization. This is demonstrable current coverage including the stronger fixed-slice claim, not an assertion of earlier priority: v2 is dated November 23 UTC, after the frozen item dated October 13 UTC. No comparable exact coverage was identified in the bounded pre-record sources.

## value

FAIL

Showing that a single slice fills the exact image of this canonical pair was a mathematically motivated test of the v1 span-only gap, not an arbitrary choice of invariant. But as a current stand-alone narrow exact-image result, it adds no distinct fact beyond v2: the full image, the same slice, and the broader case are already given there. The explicit coordinate solution does not supply a separate new structural claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
