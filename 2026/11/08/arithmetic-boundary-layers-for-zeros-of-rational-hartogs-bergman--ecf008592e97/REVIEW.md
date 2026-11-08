# Scientific review: arithmetic boundary layers for Hartogs Bergman zeros

## Correctness — PASS

The claim fixes the gap \(k\) before sending the coprime denominator \(n\) to infinity. The starting polynomial is the exact Edholm–Mathew numerator, recovered independently from integer tent sums and the original finite coefficient formula. A bounded-variation trapezoidal estimate proves a coefficient-and-derivative error of order \(m^{-2}\) after normalization, rather than only pointwise convergence. An exact Fejér evaluation at the nontrivial \(k\)-th roots of unity gives the residue-dependent positive value. Microscopic scaling at each double limiting root leaves a quadratic with distinct imaginary roots. Rouché's theorem yields a pair of simple roots, one on each side of the unit circle, with a uniform \(O_k(m^{-2})\) error in the original product variable. Degree counting and perturbation of the remaining real simple root finish the assertion. The proof does not infer infinitely many parameter cases from the finite script.

**Verification:** `python CHECK.py` with `requirements.txt` passed 1,544 finite consistency assertions against two separate coefficient representations, high-precision root-of-unity values, reciprocal symmetry, and sample root locations. The general result depends on the analytic derivation, not on the checker.

## Originality — PASS relative to inspected sources

Edholm–Mathew give the rational Bergman numerator and gap-one/two analysis, but not the explicit modular-inverse-dependent first-order radial displacement for arbitrary fixed gaps. Deng–Fu subsequently prove nonvanishing on the unit circle for all coprime pairs and present the Fejér identity; the exact splitting coefficient does not follow from that count or appear in their inspected theorem/proofs. A published gap-three result already determines the constant \(\sqrt6\) for \(k=3\), which is therefore **not** claimed new. Existing coarse fixed-gap leading-polynomial localization does not determine the first-order constant. Actual semantic searches for the general formula and residue splitting found no statement covering it. An inaccessible or overlooked equivalent in older rational Hartogs or root-splitting literature remains a publication-priority risk; no independent assessment is represented.

## Mathematical value — PASS

The object is the natural oblique Bergman-numerator zero locus, and its boundary zeros arise from double roots of the universal limiting polynomial. The sharp coefficient resolves how those zeros approach the unit circle, not just whether they do so. Crucially it detects an arithmetic bifurcation: for gap five and a fixed angular root, two distinct radial limits occur according to a congruence class of the numerator. The formula is universal for all fixed gaps and refines the earlier gap-three special case. No general claim for growing gaps, all finite parameters, or off-slice kernel zeros is made.

## Closest literature and limitations

The main exact kernel construction is L. D. Edholm and V. T. Mathew, *Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains*, arXiv:2505.20489. G. Deng and Q. Fu, *Bergman Kernel Zeros on Rational Hartogs Triangles*, arXiv:2611.07480, provide later all-gap positivity and the precise finite Fourier product identity. The public record *Cubic-root condensation of diagonal Bergman-kernel zeros in gap-three Hartogs triangles* already proves the sharp special-gap coefficient. The present asymptotics are for a fixed gap and selected diagonal product levels; the proof gives no global zero-set classification or independent priority certification.

Self-review: passed. Independent audit: not yet performed.
