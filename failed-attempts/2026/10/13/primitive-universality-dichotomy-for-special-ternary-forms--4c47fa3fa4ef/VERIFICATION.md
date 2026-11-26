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

For special d>1 the coprime decomposition d=A²+B² follows by choosing one Gaussian prime above each odd prime dividing d and, for even d, the factor 1+i once. The Gaussian integer and its conjugate then have no common rational prime divisor of their coordinates, and d>1 precludes an axis with coprime coordinates. In the displayed ansatz, Q_d(Ac+u,Bc+v,c)=2(Au+Bv)c+u²+v² and any triple gcd divides Au+Bv. For odd d, shifting the Bezout solution switches the required parity because A,B have opposite parity; for even d and odd m the sum of squares of the offsets is always odd. For even d with m=2 mod 4 the offset pair is chosen odd and Au+Bv=2, excluding a common factor 2. For m=0 mod 8 the offsets are twice a Bezout solution, their squares sum to 4 mod 8, and c is odd. In each case the shift has nonzero quadratic leading coefficient in c and hence in both other coordinates, so infinitely many distinct parameter values give nonzero triples. The d=1 formula uses consecutive a,c and varying b of fixed parity. Finally, for d=2 mod 8 and m=4 mod 8, odd c would force a²+b²=6 mod 8; even c forces a,b even. The constructive and forbidden-box evidence was inspected as finite regression only.

## originality

FAIL

The submitted classification is correct but is a direct corollary of explicit published polynomial families and the elementary modulo-8 check, not a new representation construction. In Dung–Thang (2021), pp. 3–7, the witnesses are exactly (Ac+u,Bc+v,c) with the same shift families and with Au+Bv=1 or 2. For rhs 1 any common divisor is already excluded. For rhs 2 and m=2 mod 4, their proof already uses both offsets odd. For rhs 2 and targets divisible by 4, their proof already uses both offsets even; after division by 2 their Bezout equation has rhs 1 with both coefficients odd, so the divided offsets have opposite parity. Consequently their c is odd for m=0 mod 8 and even for m=4 mod 8. The published families remain nonzero for all sufficiently large shifts and their c is unbounded. This is actual coverage by the formulas, not an inference from ordinary universality alone. Nowicki's explicit families cover the small endpoints d=1 and d=2 as well. The only extra ingredient for the exact classification is exclusion of 4 mod 8, by the immediate squared residues 0,1,4. No source read was found expressly stating the entire primitive classification; the reason for failure is the direct implication, not an unavailable paper.

## value

PASS

As a mathematical statement, the complete primitive value set distinguishes ordinary from primitive universality for an entire natural family and locates the exact obstruction, rather than only exhibiting individual failed representations. This usefulness does not make the result new given the published formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
