---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

In characteristic three the quotient is by the coordinate cubes and D³ is a derivation zero on generators, so only lengths 1–3 occur. Independently verified small monomial calculations give (m1,m2,m3)=(3,0,0),(2,2,1),(2,2,7). For example on the length-three generator block, degree three in basis x²y,x²z,xy²,xyz,xz²,y²z,yz² has image spanned by x²y, x²z+xy², xyz, xz²+2y²z, and the square has image spanned by x²z+xy². Degrees above the middle are dual to the lower degrees via the top-monomial pairing, with D dual to −D. For a primitive tensor with J3, multiplication by u=x+y on k[x,y]/(x³,y^s) is free of rank s over k[u]/(u³) by the characteristic-three change of variables; J2⊗J2 has ranks 2 and 1. Modulo projectives, each nontrivial block therefore contributes 2(1+J2), with (1+J2)²=2(1+J2). This proves h and both ranks in arbitrary dimension, with the remaining multiplicity obtained from dimension 3^n. Unique factorization recovers a and b+c from h and the known dimension distinguishes b from c. D=0 if and only if T=0. The standard module centralizer has dimension (a+b+c)²+(b+c)²+c² and semisimple quotient Mat_a×Mat_b×Mat_c; its radical accounts for the q-power in the unit-group order, giving matrix counts by orbit–stabilizer, not a count of orbits. The three-dimensional example agrees. VERIFICATION.md and VERIFY.py were inspected, not executed.

## originality

PASS

The supported distinction is the exact primitive-action Jordan spectrum for the entire height-one algebra and its single-rank inverse for the cubic-zero generator class. The tensor rules themselves are standard/data already shared with cyclic-group Green rings, and the class cardinality formula is standard. The strongest inspected related results classify different operators or tensor factors. The site of remaining plausible overlap is the broader modular truncated-symmetric-power literature; this assessment is bounded and not a priority certification.

## value

PASS

A single derived rank is a complete invariant of the inducing nilpotent partition at known dimension, even though the length-two and length-three generator blocks become indistinguishable in the stable ring. Recovering the missing split from dimension and separating the trivial factors by prime valuations give an exact inverse useful for classifying this natural family. The finite-field distribution is an accompanying application, not the main basis for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
