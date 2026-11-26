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

The monic cubic with constant 1 can have only ±1 as rational roots; the evaluations 1 and −2u−1 exclude them for integral u. Direct expansion gives Δ=(u²+u−3)²−32, which cannot vanish. Writing m=u²+u−3 gives odd m≥−3; if Δ=k², the integers (m−k)/2 and (m+k)/2 multiply to 8 and have odd sum. The only such sums are ±9; the bound leaves 9, giving u=3,−4, each with Δ=49. The alternating criterion therefore gives precisely two cyclic parameters. For z=ζ₇+ζ₇⁻¹ the standard relation z³+z²−2z−1=0 gives F₃(1−z)=0. With w=−4+z+2z², reduction gives w²=16−4z−7z² and w³=−65+16z+29z², verifying F_{−4}(w)=0. Both generators have degree three, so their cubic field is the real seventh cyclotomic field. At p≠7 the good reduction Frobenius is trivial in (Z/7)×/{±1} exactly for residues ±1; it has three fixed points then and no fixed point otherwise. At every good prime for the remaining parameters, the S₃ conjugacy types have sizes 2,3,1 for 0,1,3 fixed roots. Chebotarev gives the natural densities and a prime divides some value iff it has a residue root. Each such root is simple and has one lift at every prime-power depth, with no other lifts. Finite checker evidence is not used to justify universal statements; no uploaded code was executed.

## originality

PASS

The field at the exceptional parameters is a classical simplest cubic, and the Frobenius and lifting arguments are classical deductions. The verified prior uses of the very same polynomial concern recurrence or Thue equations, or finite-field statistics across varying parameters. The available statements do not settle the all-integer exceptional locus for this fixed subfamily, which is what makes the density dichotomy exact for every u rather than generic.

## value

PASS

For the natural cubic specialization of the ABC family, the exhaustive exception calculation distinguishes two explicit integers from every other one when asking which primes divide polynomial values. A generic S₃ theorem or a varying-parameter finite-field statistic cannot be used for this purpose. The exact modulo-seven criterion and the stability through all good prime-power depths make the result directly usable, without presenting standard density machinery or the exceptional field itself as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
