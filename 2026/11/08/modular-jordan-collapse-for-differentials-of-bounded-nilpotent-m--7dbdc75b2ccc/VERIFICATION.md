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

For commuting left and right multiplication L,T by N, both dth powers vanish and D=h(L,T) with h=Σ_{j=0}^{d−1}s^j t^{d−1−j}. In k[s,t]/(s^d,t^d), degree forces h² to be supported only on s^{d−1}t^{d−1}, contributed by exactly d ordered pairs, and h³=0. Thus rank D² is 0 if p|d and m_d² otherwise, since rank N^{d−1}=m_d and left/right multiplication by it has rank m_d². On a rectangular block pair of lengths a,b, choose a cyclic basis for each of the two independent shifts (reverse the right shift where needed), identifying D with multiplication by h in k[s,t]/(s^a,t^b). Since (s−t)h=0, the image is spanned by s^rh. For a+b>d, the term s^{d−b+r}t^{b−1} survives precisely for r≤a+b−d−1, and is the survivor with smallest s-exponent; above that threshold all terms vanish. For a+b≤d no term survives, and the surviving s^rh are independent by total degree. Summing ranks over ordered block pairs yields R and counting admissible column indices gives the same h_i expression. The ranks of D and D² now determine all Jordan multiplicities. The dual-number expansion gives the stated fixed-residue kernel count. If m_d>0, rank D>0 and its nilpotency index changes from 2 to 3 according to divisibility; if R=0 the map really is zero, which is compatible with square-zero wording.

## originality

PASS

The exact first rank and fixed-residue first-jet count are already covered by Resultary 5c39e77ec446 and are not independent contributions. The supported distinct claim is the full positive-characteristic Jordan signature, with the square controlled by p|d and the cube always zero. First-rank data do not imply that signature, and the available published treatments furnish the operator framework, entry formulas, or characteristic-zero Jordan forms rather than this modular result. Norman's plausible broader paper could not be inspected beyond its abstract and a secondary scope description; that limitation is not negative evidence.

## value

PASS

For a natural nilpotent input family this completely determines a linear operator's Jordan type from the input partition and characteristic. The first rank and finite-field lift dimensions alone cannot see the sharp modular change, whereas the square rank distinguishes genuinely different nilpotency indices as soon as a length-d input block is present. The theorem is not just a new rendition of tangent dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
