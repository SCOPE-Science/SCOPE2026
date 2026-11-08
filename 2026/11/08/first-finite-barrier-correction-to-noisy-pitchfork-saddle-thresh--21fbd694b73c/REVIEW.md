# Self-review

## Correctness — PASS
The result is the uniform \(r^{-1}\) correction, not the previously known leading profile. The stopped diffusion's backward Dirichlet problem yields a standard exact double integral. The integrand obeys the exact barrier identity \(2V_r(z)=r^2/2-(r-z^2)^2/2\). The inner well integral has no \(r^{-1}\) term; Gaussian saddle expansion gives the offset-dependent third moment \(e^{-2\beta^2}(\beta^2/4+1/8)\). Uniform domination for bounded offsets supplies the stated \(O_B(r^{-2})\) remainder. Independent finite-difference and quadrature computations in `verify_exit.py` check representative cases; finite computation is not the universal proof.

## Originality — PASS (provisional priority)
The source [1] uses exactly the same diffusion, exit problem at the deterministic saddles, and exact backward integral, but supplies no next-order asymptotic and instead fits an empirical multiplicative factor. Source [2, Sect. 4.3 Eq. (77)] already supplies the **general leading Gaussian error-function crossover** and saddle half-factor, so those are excluded from the novelty claim. Source [3] supplies classical Kramers theory, not the specific cubic-pitchfork \(r^{-1}\) coefficient. Published-record searches for first-order moving-threshold corrections did not uncover direct coverage. Equivalence via Laplace-method general formulas remains a material priority risk; the positive offset-dependent coefficient itself was not found in inspected documents.

## Mathematical value — PASS
The precise source [1] uses an empirical factor \(0.6\) for finite barrier heights. This result gives an analytic \(r\)-dependent replacement at the original detection threshold and a complete nonconstant first correction when detector placement is varied on its natural saddle scale. Since the first correction is strictly positive, it identifies the direction of finite-barrier bias; its explicit dependence on the detector location produces an effective offset shift \(\beta^2/2+1/4\), not a single global constant. This finite-size correction is a quantitative calibration of a naturally defined tipping-time observable, rather than a renamed leading Kramers limit. No claim is made of a broader new metastability law.

## Closest literature and limitations
The Gaussian crossover and one-half factor are already known [2]. General Laplace expansions may imply the coefficient by additional calculation; no exhaustive historical priority claim is made. The proof applies to fixed bounded offsets and the specified additive-noise pitchfork only. Numerical checks and this review are not independent scientific certification.

Self-review: passed. Independent audit: not yet performed.
