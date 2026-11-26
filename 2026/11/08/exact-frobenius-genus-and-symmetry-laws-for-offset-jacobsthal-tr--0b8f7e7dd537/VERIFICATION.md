---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Writing s=(-1)^n, the recurrence gives b=8a+3s and c=16a+5s, so gcd(b,c)=1, gcd(a,b)=gcd(a,3), and 3c=8a+5b. Also 3 divides a exactly when 2^n=(-1)^n mod 9, or 3 divides n. In that branch c belongs to the two-generator semigroup T on a/3,b/3, and its residue shifts by 0,c,2c yield F=3F(T)+2c and g=3g(T)+c-1, also when T=N_0 at n=3. Otherwise an Apéry element can have neither an a summand, nor three c summands, nor a copies of b. In the class kb mod a there are therefore exactly the three candidate forms obtained from y=0,1,2 and the corresponding reduced b coefficient. For t=5/3 mod a and D=c-tb, the candidates differ from kb by yD plus the wrap terms 0,ab, or 2ab. When a=1 mod 3, D<0 and 2D+ab>0, giving the 0,1,2 strips; when a=2 mod 3 and a>=11, D+ab>0 and 2D+ab<0, giving the 0,2,1 strips at u=2t-a and t. Endpoint comparison gives the claimed maxima. In both coprime branches the strip sum differs from a(a-1)b/2 by a(a-5)(8-b)/3, giving the genus. The n=4 redundant c case has F=167 and g=84. Substitution gives both defects and establishes the exact symmetry condition. A separate forward membership computation through a full run of a consecutive representable integers verified F, genus, and the claimed residue minima for n=3,...,11 wherever applicable; it is finite corroboration only.

## originality

PASS

The strongest indexed analogue treats the same offsets for Pell numbers and shares the gluing/symmetry theme, but it uses a different recurrence and does not determine the Jacobsthal residue strips, Frobenius numbers or genera. The inspected Jacobsthal and generalized recurrence theorems use offset two, and the broader generator parameterization in the 2023 paper does not contain this family even when treated as an unindexed generator parameterization. The supported distinct contribution is the exact all-index invariant and Apéry determination, not a new general gluing or symmetry criterion.

## value

PASS

The offsets retain a short recurrence relation but lie outside the common offset-two triple, a natural nearby family in work on recurrent numerical semigroups. The exact thresholds describe every residue, not just exceptional indices or a finite sample. They determine both principal gap invariants in all indices, identify exactly where the defect vanishes, and provide Apéry data that can be used without running a residue graph search for each index. This is more than applying the known gluing or symmetry criterion to the symmetric branch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
