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

The stated coproduct and antipode give ad_v(b)=vb-cbcv and ad_cv(b)=bv+cvbc; on (1,c,v,cv) the only nonzero entries are respectively -2 and +2 from c to cv. Conjugation by c is +1 on 1,c and -1 on v,cv. Thus the module splits as the two stated lines and the plane (c,cv); the plane has just one invariant line because the off-diagonal matrix unit sends every vector with nonzero c-coordinate outside its span. Restriction to the plane identifies the image algebra, with both diagonal entries and the lower entry free in odd characteristic. The fibers have size q and the vanishing patterns of the two diagonal entries give ranks 4, 2, 1, 0 with counts q²(q−1)², 2q²(q−1), q(q−1), q; the kernel is exactly k(v+cv). This is symbolic over every odd prime power. The supplied verifier reconstructs basis matrices and enumerates prime-field examples only; it was inspected, not executed.

## originality

PASS

Bounded to the explicit finite-field census: no distinct indexed record or inspected theorem giving the same census, or a stronger rank census that specializes to it, was found. This is not a finding of originality for the adjoint construction or a claim that the census is mathematically independent of standard H4 data. Those data make the census a mechanical calculation, which is decisive on value.

## value

FAIL

The adjoint module itself is a natural object, but no independent mathematical need is established for this isolated rank census. The triangular structure is read off from generator substitutions in the standard four-element basis, and once the two character evaluations and the single off-diagonal entry are written down, the forbidden rank and every fiber count are immediate. The result is a correct illustrative calculation, not a nonmechanical exact invariant or a substantively motivated boundary or obstruction; the distinction from the polynomial-identity literature does not remedy this.

The dated certificate retains the supplied scientific assessment, sources and limitations.
