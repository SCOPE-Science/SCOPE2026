---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

At infinity an Artin–Schreier coboundary would have pole order divisible by 5, so the pole of order 6 gives a connected degree-five extension with one totally ramified point and no other ramification. The different exponent is 28; Riemann–Hurwitz and Deuring–Shafarevich give genus 10 and p-rank zero. The valuations of x, y and dx are −5, −6 and 18, so the ten listed differentials are regular and have distinct valuations. The affine map to the x-line is étale, so x is separating and there are no other poles of these differentials. In replay I expanded (y^5−f)^j as ordered choices of monomials, retained x-powers congruent to 4 modulo 5, and applied inverse Frobenius to the coefficients; all entries match the displayed Cartier matrix, including the full column 10. When (a,b,c) is not zero, columns 5–7 span the first coordinate line, columns 8–9 give the displayed two-row block P modulo it, and column 10 has an independent component in rows 3,6,8. Hence the rank is 2+rank(P), and P vanishes only at (a,b,c)=0. Its determinant has fifth power Q. The entire matrix vanishes at (a,b,c)=0 even if d is nonzero. Thus the a-number is 6, 7 or 10 on precisely the claimed strata. Substituting z=c+3a² makes Q=b²+4az. Rank 3 prevents linear factorization over the algebraic closure, the gradient gives exactly the free d-line, and the hypersurface has S2 and is regular in codimension one. This proves normality and the product with the surface A1 singularity along the line.

## originality

FAIL

A distinct same-day Resultary record covers the full classification and the same reduced quadratic-cone divisor in renamed variables. Normality is immediate from its reduced hypersurface model with codimension-two singular locus. This establishes equivalent coverage, not priority. The cited Zhou paper also already excludes both near-maximal values 8 and 9 in this family.

## value

FAIL

A new universal Cartier-rank stratification with an explicit normal jump divisor would be useful for studying genus-ten families, unlike a prime-field enumeration or a superspecial example alone. Here the full marked strata and underlying ordinary double point are available in the matched finding, and the frozen claim does not add a distinct invariant or calculation with separate scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
