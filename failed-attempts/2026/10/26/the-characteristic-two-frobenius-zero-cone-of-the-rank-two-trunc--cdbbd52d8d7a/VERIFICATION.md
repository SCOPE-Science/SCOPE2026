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

Leibniz gives D(xy)=e x+a y+(b+v)xy; the eight coefficients of D²(x),D²(y) then agree with the eight independent entries of the square of M=[[v,c,a],[u,b,e],[w,d,b+v]]. This is an invertible linear change to traceless matrices and identifies the reduced height-one locus with traceless matrices squaring to zero. Off zero, these have rank one and are parametrized by a line L=im M in a plane H=ker M and a nonzero isomorphism k³/H→L. This identifies the punctured cone with a line bundle minus its zero section over the smooth rational complete flag variety, so it is smooth, rational and irreducible of dimension 3+1. Scaling puts the zero matrix in its closure. On this locus (a,e)=0 is equivalent to M e₃=0: otherwise M e₃=(b+v)e₃ with b+v nonzero would contradict M²=0. Thus the nonzero-constant locus is dense open in the smooth punctured cone. Over F_q the flag model gives 1+(q²+q+1)(q+1)(q−1)=q⁴+q³−q. Requiring e₃∈H gives only q+1 plane choices, and hence 1+(q+1)²(q−1)=q³+q²−q; the complementary count is (q²−1)q². This holds over every indicated finite field. The scope does not extend to the full restricted nilpotent cone: the regular nilpotent matrix E₁₂+E₂₃ has nonzero square and zero fourth power.

## originality

FAIL

The distinct indexed socle-detection record gives the same restricted-square coordinate isomorphism to sl₃, the full rank-one matrix parametrization, and exact arithmetic counts for the total locus and the same strata. Its rank-one description is the standard flag line-bundle model, which directly implies the remaining smoothness, rationality, irreducibility and dimension assertions. This is demonstrable coverage without a conclusion about historical priority. The primary Witt literature inspected is not used to establish that coverage.

## value

FAIL

This low-characteristic height-one cone is a natural object, but the indexed comparison already identifies it and counts the very same strata. The remaining geometric statements are the direct smooth line-bundle description of the known rank-one flag model plus its vertex, with no distinct new invariant established. No substantive repair is warranted by the remaining claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
