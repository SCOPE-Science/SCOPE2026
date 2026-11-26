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

Since the characteristic is neither 2 nor 3, squarefreeness and ten simple geometric branch points are equivalent to b≠0 and separability of h. Degree ten gives genus four and no branch at infinity. The repeated-root cubics with b≠0 have roots r,r,−1−2r and are counted once for each r≠0,−1/2, including the triple root, giving q−2. Three distinct nonzero roots summing to −1 give (q²−6q+11)/6 by excluding zero coordinates and collisions before dividing by six. For one rational root r≠0 the irreducible quadratic has trace −1−r, with (q−1)/2 conjugate pairs for each trace; subtraction gives the irreducible-cubic count (q²−1)/3. For refinement in K=F_(q²), the cubes form a union of (q+1)/3 nonzero k-lines since k*=F_q* is all cubes. The trace-zero line is among them: w^(q−1)=−1 there, so w^((q²−1)/3)=1 as (q+1)/3 is even. Every other included line meets each nonzero trace in one point; removing the rational point and pairing conjugates gives (q−5)/6 quadratic pairs per nonzero trace and (q−1)/2 at zero. Exactly one allowable r gives trace zero. A rational h-root has one rational cube root and one pair; noncube roots of the quadratic lift through degree three over K and yield a six-cycle. For an irreducible cubic the cube map on F_(q³) is bijective and adjoining the nontrivial cube roots of unity gives the degree-six orbit. Together with x=0 this proves the types, counts, positivity for q≥5, and splitting degrees and branch zeta function. The rational point x=0 rules out Frobenius taking an even subset to its complement, so the rational 2-torsion dimension is c−2 for c cycles. The verification note and supplied code were inspected, not executed. The bounded independent replay /workspace/branches/e5d30ab9-87ee-4d6c-a029-ff6ae91fa034/independent_census.py, with arguments 5 and 125, recovered the exact counts (1,2,6,8) and (2481,2522,5166,5208) by full-polynomial Frobenius gcd counts and independently confirmed the cube/noncube split in the quadratic case. Those runs do not prove the all-field theorem; the trace and degree arguments do.

## originality

PASS

The family, the hyperelliptic 2-torsion representation, and elementary cubic and trace methods are not new. The supported distinct result is the four exact frequencies with the fixed x⁷ normalization, valid throughout q≡2 mod 3. The same-family sources inspected concern superspecial enumeration, Cartier or Weil data, not the cube-sensitive branch census. The closest full four-type branch table is for a different polynomial and a quadratic lifting mechanism. General quadratic/cubic irreducibility counts and the genus-four normal forms do not supply the trace-zero correction and mixed quadratic refinement for this coefficient slice. The asserted q≡1 comparator table was not retrieved; this is an explicit limitation, not absence evidence.

## value

PASS

This is an all-field arithmetic census of a previously studied two-parameter genus-four family, measuring a marked branch invariant not supplied by its superspecial or Weil classifications. It resolves the genuinely unequal cubic-lift split within one cubic factorization type and gives the exact sizes of the resulting rational-2-torsion and splitting strata, with a uniform formula that includes nonprime fields. This is more useful than listing possible cycle types or recomputing a few sample curves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
