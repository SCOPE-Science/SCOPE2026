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

For algebraically closed k of characteristic zero and the filtration cutoff 2m+1, the quotient by (x) is k[y], so every square-zero element lies in (x). The faithful Jordan-plane matrix coordinates give all and only matrices (Wa,W²b;c,Wd), with c of degree at most m and a,b,d of degree at most m−1. In the two entries involving right multiplication by W, PBW commutation replaces U by U+W, an invertible filtered change, so the stated entry spaces are attained. The c-only family supplies the affine lower bound D_m. The Ore normal form over k[T] makes the finite homogeneous coefficient equations polynomial in T, hence the projective family is proper. Scaling U identifies all nonzero fibers, so Stacks Tag 0D4I bounds their dimension by the fiber at zero without a flatness assumption. In the commutative domain, c=0 forces a=d=0, and c≠0 forces d=−a and a²=−bc. For a≠0, after removing gcd(b,c), the residual factors are coprime squares up to units, giving a=HFG, b=−HF², c=HG². With degrees r,s,t the bound r+s+t≤m−1 and the free one-dimensional simultaneous rescaling give image dimension at most D_r+D_s+D_t−1≤D_{m−1}+1≤D_m. The b-only and c-only pieces and finite union preserve that bound. Removing zero and projectivizing drops one dimension; at m=0 the projective locus is one point. This verifies the full locus including mixed parity, not a truncated quotient or a finite-field extrapolation. The finite uploaded checker was inspected, not executed, and is not needed for the proof.

## originality

PASS

The checked primary paper explicitly leaves the identical all-m projective dimension equality as Conjecture 5.14. It supplies the embedding, lower-bound families and the m=1 case, not this uniform upper bound. The closest indexed exact hit is the identical record, not distinct coverage. The supported distinct contribution is the full all-cutoff dimension result via proper specialization and the commutative factorization bound.

## value

PASS

The dimension is the exact unknown in a stated conjecture and controls the full filtered square-zero variety, which neither the odd component nor the degree-three example can measure. The uniform argument supplies an upper bound matching the previously known linear family at every cutoff; it does not merely enlarge a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
