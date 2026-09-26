# Independent audit — 2026/09/09/062

## Correctness — FAIL for the claimed certified elimination log

The conclusion of non-Liouvillianity is salvageable, but the record's complete exact Kovacic certificate uses an incorrect case-3 candidate formula. It writes E_c={(6+k√(1+4b_c))/n: |k|≤n/2}∩Z for n∈{4,6,12}. The standard finite-primitive case has E_c={6+(12k/n)√(1+4b_c): |k|≤n/2}∩Z, followed by d=(n/12)(e∞−Σe_c). For example at b0=−1/4 the correct E0={6} for all three n, rather than {3/2} (empty), {1}, {1/2} as the record states. The reported case-3 branch enumeration and “generous” recurrence therefore do not certify what they claim.

An independent repair is straightforward: P has residues 1,1/2,1/2 and coefficient 2/x at infinity, so r's double-pole coefficients are −1/4,−3/16,−3/16 and −1/3, independent of q. Case 1 has nonreal infinity α=(1±i/√3)/2 against real finite α, hence no integer polynomial degree. Case 2 has e∞=e0=2 and e1,e2≥1, so d<0. In the correct case 3, e∞=6 (imaginary square root forces k=0), e0=6, and e1,e2≥3; d<0 for n=4,6,12. Alternatively the infinity exponent difference i/√3 gives infinite-order local monodromy, excluding a finite primitive group. Thus the mathematical non-Liouvillian conclusion holds for every q in this written family, but the accepted certificate is substantively invalid and must be replaced before acceptance.

## Originality — PASS, narrow

I found no matching accessory-independent non-Liouvillian statement for this exact four-singularity equation in the checked primary Heun/Kovacic sources. Its local-exponent argument is a routine application of a standard algorithm, and the named q=7/5 is inessential.

## Scientific value — PASS, limited

A corrected uniform-in-q decision could serve as a small symbolic-solver regression example. The current incorrect replay log cannot be relied on; it supplies neither the requested reducible neighbor nor a new general Heun method.

## Sources

- Original RESULT.md, METADATA.json; independent residue and corrected candidate arithmetic above.
- Kovacic, *An algorithm for solving second order linear homogeneous differential equations*, J. Symbolic Computation 2 (1986), https://doi.org/10.1016/S0747-7171(86)80010-4 .
- NIST DLMF Heun quadrature context, https://dlmf.nist.gov/31.8 .
