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

The quotient square completion gives a squarefree quartic on U (quadratic discriminant 16Δ); its characteristic-seven Hasse coefficient is B(B²−AC). The prime-to-7 quotient isogeny gives the rank and a-number formulas. Each B is a smooth graph; each D is irreducible by odd valuations of (r²−4)(t²−4), and smooth on U because in coordinates (r,t,Bx) its derivative in Bx is 2Bx, nonzero on Dx=0 in U. Within each quotient a B and D cannot both vanish. An independent algebraic exhaustion over the algebraic closure avoids reliance on the frozen field sweep: write a=r²−4, b=s²−4, c=t²−4; the three D factors are 16Δ+3ac, 16Δ+3ab, 16Δ+3bc. BBB forces the origin since a nonzero triple would have squares 4. Two B's force two coordinates zero, and the remaining D then forces the other coordinate to be ±1. For Bz,Dx,Dy, the D difference gives t²=s²=h; substituting r=st/2 yields Dx=(h−4)²(3h−4)/4, forcing h=6, r=±3 and rst=4. With three D's, the squares are equal to h and v=rst satisfies 2v=3h²+3h+5, v²=h³; the eliminated equation factors as 2(h−2)(h−4)^3 in F7. Thus h=2, v=1. All resulting triples meet U, giving 1+6+12+4 points and the stated type and rationality counts. Transversality follows from the nonzero linear B derivatives at the origin; at the two-B points the 2-by-2 B minor is 16−4r² and the remaining derivative is 32r. At the one-B points the substituted equation has a simple root with h a local parameter; the difference of the D factors cuts out t=±s smoothly. At the three-D points equality of squares cuts out a smooth local parameter curve and h=2 is simple, with v nonzero. Rank one occurs along the intersection of two B branches near the origin outside the finite triple locus, and ranks two and three occur off further divisors. This proves reducedness for the stated common Hasse-zero scheme, not for arbitrary scheme structures supported on the rank-zero set.

## originality

FAIL

A distinct indexed record already covers the key claim at the statement level: the identical finite étale degree-23 marked Hasse intersection, its explicit orbits and transversality. The remaining divisor and B/D table assertions are direct consequences of the same displayed factors and orbit list. This is a judgment of equivalent coverage, not a claim of chronological priority between same-date records.

## value

FAIL

A first computation of the reduced marked intersection could have been useful. Here the exact scheme, saturation result, transversality and marked orbits are already available; the remaining counts are direct factor evaluations on four representatives and the component splitting is elementary from the displayed prior factors. They do not supply an independent mathematical gap or remedy the equivalent coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
