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

For every odd prime p != 7, the quotient T: W^2=Z^14+1 by (Z,W)->(Z^{-1},W/Z^7) has invariants X=Z+Z^{-1}, Y=(Z+1)W/Z^4 and equation Y^2=(X+2)D_7(X). The degree-eight squarefree right side has genus three. Invariant differential basis eta_j=omega_j-omega_{7-j}, j=1,2,3, and the hyperelliptic Cartier support rule (pi-j)/14 in [0,(p-1)/2] nonzero exactly for pi=j mod14 yield explicit arrows with nonzero binomial coefficients. Iteration gives profiles (3,3,3,3) at p=1 mod14; (3,2,1,0) at p=3,5; (3,1,0,0) at p=9,11; and (3,0,0,0) at p=13. Hence a-numbers 0,1,2,3 and p-ranks 3,0,0,0 respectively. Exact independent coefficient-expansion and modular rank tests passed for all 44 eligible odd primes through 199, including each residue class. Finite checks corroborate the all-prime congruence and nonzero-binomial proof; they do not replace it. The optional geometric automorphism claim requires p>13 and a separately cited theorem.

## originality

PASS

The superspecial p=-1 mod14 case and maximality are already implied by earlier sources, and are not claimed as new. What survives is the complete genus-three Cartier rank-iterate profile, particularly the nonmaximal p=3,5 intermediate ranks two and one and the p=9,11 rank-one then vanishing case. Primary material read does not yield these precise intermediate profiles; all conclusions are restricted to d=7.

## value

PASS

A complete all-prime Cartier degeneration classification for a natural genus-three Dickson–Chebyshev quotient is an exact algebraic-geometric invariant that is not routine from maximality. The nilpotent Jordan chains distinguish intermediate slopes and a-numbers even when all cases have p-rank zero. The superspecial corollary itself is previously known and is not the value contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
