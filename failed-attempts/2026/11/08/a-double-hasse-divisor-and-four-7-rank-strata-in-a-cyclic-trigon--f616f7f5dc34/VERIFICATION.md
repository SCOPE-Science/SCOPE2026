---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For separable characteristic-7 quintic F=x^5+a x^2+b x+c, the genus-four differential basis dx/y, x^i dx/y^2 (i=0,1,2) and degree congruent 6 mod7 Cartier extraction give coefficient matrix diag(2b,B) with det B=2b Delta and Disc(F)=Delta, hence det H=4b^2 Delta as polynomial identity. On smooth b=0, rank Cartier is exactly 2 by a nonzero 2x2 minor, a-number=2. Normalize c to 1, A^5=a^5/c^3. Twisted semilinear matrix products have gcd 2x2 minors of P2 equal A^4(A^10-1), gcd entries P3=A, and P3 nonzero at A^5=1; singular A^5=-1 excluded. Thus geometric eventual 7-ranks 0 at A=0,1 at A^5=1,2 elsewhere; smooth b !=0 ordinary rank4. Independent exact SymPy determinant, discriminant and polynomial Euclidean computations reproduced; finite F7/F49 counts are corroboration only.

## originality

FAIL

FAIL: A published full-family universal quintic result proves det H=Delta(F)*([x^6]F^2)^2, whose substitution c3=c4=0,c1=b gives exactly 4b^2 Delta and double nonordinary b=0 divisor. A separately published fully read b=0 subfamily theorem gives the exact smooth p-rank 0/1/2 and constant a-number 2 criteria, including singular exclusion. Their conjunction covers the full mathematical finding; an independent certificate or elementary F7/F49 parameter census cannot restore originality.

## value

FAIL

FAIL as an independent mathematical contribution: the natural curve family is important and calculations correct, but every principal parameter stratum and determinant multiplicity is already implied by published universal Hasse and exact subfamily rank theorems. Re-deriving them, computing finite counts and adding checks has reproducibility utility but is known-invariant recomputation, not a new mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
