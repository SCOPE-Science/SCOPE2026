# Scientific review: original-time relaxation at analytic sewed foci

## Correctness (PASS)

The theorem explicitly assumes analytic decreasing half-flight involutions with common slope \(-1\), a finite nonzero even mismatch \(\chi(x)=-c x^{2p}+O(x^{2p+1})\), and nonvanishing horizontal crossing speeds. The exact involution identity converts this mismatch into the positive-section recurrence \(r_{n+1}=r_n-c r_n^{2p}+O(r_n^{2p+1})\), with no change of coefficient. Reciprocal-power telescoping proves the sharp return-index law. Lower and upper flight times both shrink linearly with section radius, with original-time coefficient \(K=2(b_+^{-1}+|b_-|^{-1})\); summation yields the algebraic physical-time laws. At quadratic mismatch the \(O(r_n^3)\) recurrence remainder and \(O(r_n^2)\) clock remainder are summable after the \(r_n\sim1/(cn)\) estimate, giving a genuinely positive, finite exponential prefactor. The explicit polynomial examples verify attainability of every order. Critical identities are symbolically and numerically checked in the accompanying code.

Proof boundaries: the theorem concerns positive crossing radii and their original elapsed times, not an everywhere-defined signed coordinate rate. The analytic and finite-order hypotheses are essential; no claim is made for flat nonanalytic discrepancies or all Filippov singularities. The prefactor in the quadratic case is orbit dependent.

## Originality (PASS within inspected evidence)

The central source, Glendinning–Hogan–Homer–Jeffrey–Szalai (arXiv:2306.09743v1, 2023-06-16), is inspected in its accessible full HTML text. Its Theorem 1 and Section 2 already establish the sewed-focus alternatives, analytic involutions, the even-order discrepancy and infinite physical arrival time. Those components are credited as prior work. The new statement instead quantifies exactly *how* approach occurs in physical time for every finite discrepancy order, determines the crossing-speed prefactor and realizes each class by polynomial side fields. These formulas and the strong quadratic-mismatch asymptotic constant are not stated in the inspected article. The paper's nonanalytic finite-time examples are not equivalent: their return dynamics can be supercontractive and their arrival times are summable. Earlier published results on piecewise crossing systems and stationary/period geometry were compared by mathematical implication, not by similar terminology.

Residual risk: older Filippov and Bautin–Leontovich/Skriabin sources were described by the inspected primary source but their full original texts were not directly read; classical parabolic asymptotic theory may imply some discrete ingredients. Search noncoverage is not a proof of absolute publication priority. The physical-time conversion is the focal contribution.

## Mathematical value (PASS)

The distinction between infinite-time and finite-time approach is a principal question in the originating sewed-focus literature. A sharp original-time relaxation law refines that qualitative dichotomy for the complete finite-order analytic regime. The leading physical-time behavior changes genuinely in type—from exponential at order two to a hierarchy of algebraic rates at orders four, six, and above—even though all crossing-index rates are parabolic. Its constants retain both physical crossing speeds, and the explicit family demonstrates that all rates occur rather than being formal asymptotic possibilities. These are dynamical observables and a structural classification, not an arbitrary numerical evaluation. An open question for future work is whether analogous complete laws exist for infinitely flat smooth sewed foci.

Self-review: passed. Independent audit: not yet performed.
