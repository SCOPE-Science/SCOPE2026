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

For t=1,2 each closed word of 2t-bit column letters satisfying the local temporal constraints specifies a unique F^t-fixed labelled state: phase zero determines all later phases, and B is used only at column zero. This proves the trace normalization, with no division by rotations or by temporal period. I rebuilt the transfer with ±1 votes and the incumbent as the third vote at the defect, found components by mutual reachability, obtained characteristic polynomials independently with exact symbolic matrix arithmetic, and evaluated the trace convolutions with full D=det(I−zT) through degrees 16 and 256 (branches/reproduce-prism.py and .out). The proposed denominators divide D, the padded proposed numerators have degrees at most the respective matrix sizes, and the two exact trace identities follow by the adjugate degree bound. The residue identities and reduced denominators also reproduce exactly. There is a unique simple dominant eigenvalue φ or φ² in the intact trace, respectively. In the t=2 determinant the nonquadratic factors pose no hidden dominant poles: for either reciprocal quartic the eigenvalues obey y²±y+4=0 with y=λ−1/λ; y has real part ±1/2 and imaginary part ±√15/2, lying on the ellipse for |λ|=φ, whose semiaxes are φ−φ⁻¹=1 and φ+φ⁻¹=√5. Its semiaxes increase strictly for |λ|>1, so these roots have modulus φ or φ⁻¹. The intact leading amplitudes are one, and the defective ones are exactly 3/√5 and 2−3/√5. Subtracting H, which is exponentially smaller than P, and halving gives the claimed primitive temporal orbit decrease. The exact Fibonacci expression was checked by an identity of series: it matches at every physical n≥3 (indeed at n≥2), not at formal n=1, where the overlapping-column count is 4. Thus the coefficient-sequence wording in the proof must be read within the physical scope specified in the finding. A separate direct update enumeration matched both transfers for 3≤n≤8. These checks establish neither basin populations nor sharp transient lengths.

## originality

PASS

The intact baseline and the minority fixed-state amplitude are prior, and the even-n defective majority fixed-state law follows from the latter by bipartite spin switching; the frozen record credits these facts. The surviving claim is the evaluated defective period-dividing-two rational series and the matching opposite primitive-orbit response, with the odd-n majority fixed-state law. None of the checked overlaps supplies that evaluated census or an implication yielding it.

## value

PASS

The comparison affects the same natural two-rail recurrent-counting problem by exactly one missing bond. Evaluating the resulting all-circumference period-two census and its amplitude distinguishes the opposite effects on fixed and primitive oscillating orbits despite unchanged growth rates. The fixed-amplification constant alone is prior, and merely constructing the transfer matrix would not be the contribution; the evaluated return series and quantitative paired response supply the substantive content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
