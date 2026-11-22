# Scientific review: Matérn three-node quadrature positivity

## Correctness — PASS

The kernel, normalized integration probability, nodal range, and weights are specified with exact quantifiers. The three-by-three Gram solve gives both weights in elementary closed form with positive denominator. A pointwise strict-integrand inequality proves all outer weights positive. The central-weight sign reduces by an exact symbolic identity to a one-variable function whose cubic coefficient shows failure below the threshold; a global lower bound with strictly positive Taylor coefficients proves strict positivity above it, including equality. A separate exact Gram equation verifies flat-limit normalization. The accompanying Python script replayed four symbolic checks, 96 coefficient checks, 360 high-precision independent Gram-system comparisons, 12 limit checks, and two sign witnesses. Infinite correctness relies on the proof, not this finite sampling.

## Originality — PASS (best-knowledge, not independently certified)

The closest same-kernel article, Karvonen–Kanagawa–Särkkä (2018/2019), reports Matérn-\(3/2\) sign behavior numerically and explicitly says their established positivity theory does not explain it. Glaubitz–Reeger (2023) prove stability for compact-support and oversampled RBF settings, not this exact fixed three-node Matérn formula. The closest exact three-node Gaussian kernel theorem uses a different analytic covariance and has a different all-scale threshold \(1/\sqrt3\); it does not imply the present \(6-\sqrt{30}\) threshold. Targeted statements, aliases, parameter equivalences, and published research-record comparisons identified no proof already implying the entire present theorem. Unlocated specialized earlier derivations remain a priority risk.

## Value — PASS

The founding Matérn quadrature paper explicitly identifies unexplained positivity as a concrete theoretical gap. An exact all-lengthscale criterion on the minimal nontrivial symmetric design supplies a usable constructive guarantee and a sharp obstruction when the interval's interior sample is too close to its neighbors. The nontrivial global coefficient-positivity argument is distinct from ordinary polynomial interpolation or sign enumeration. Even without a larger-grid theorem, the precise boundary resolves a natural local kernel-quadrature question.

## Scope and unresolved questions

The theorem does not describe asymmetric nodes, other Matérn regularities, noise or polynomial augmentation, floating-point conditioning, or uniqueness of subcritical zeros. General optimality and convergence rates are not claimed. Independent review of the mathematics and historical priority has not occurred.

Self-review: passed. Independent audit: not yet performed.
