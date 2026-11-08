# Scientific review: renewal-tumbled circular swimmers

## Correctness — PASS

The claim follows from an exact complete-arc representation and a bounded complex-martingale coboundary. With \(m=\mathbb E e^{i\omega T}\), the martingale difference is proportional to \(U_j-m\), giving a deterministic conditional variance. The first renewal index crossing observation time is a finite-mean stopping time; its stopped quadratic variation is exactly that variance times the mean crossing count. Uniform bounds on the incomplete circular arc and coboundary control the error, and the elementary renewal theorem converts run count to time. The \(|m|=1\) case follows from equality in the triangle inequality and a geometric sum, plus the renewal strong law. Finite diagnostic computations reproduce these identities independently. No infinite-time conclusion is based solely on finite computation.

## Originality — PASS, with a specifically identified literature risk

The motivating primary text by Olsen and Löwen (2024), arXiv:2405.14326, establishes the Poisson case and observes informally that non-Poissonian half-circle turns might yield ballistic motion. It does not formulate or prove the all-law characteristic-function trichotomy or the sharp two-point timing-jitter singularity. The nearest broad reference is Detcheverry (2017), whose accessible abstract states that a non-Poisson operator formalism applies to curved trajectories. The full text of that paper could contain the general diffusivity identity and was not examined; this is a genuine risk to formula-level priority. The stronger all-law arithmetic resonance criterion and the explicit singular regularization remain the distinct assessed statements. No new general renewal methodology is claimed. Available overlap searches and comparison of the recoverable statements did not establish coverage, but failed searches do not prove uniqueness.

## Value — PASS

The problem is a natural one identified in the motivating study itself: Poisson tumble events cannot realize ballistic skipping, whereas carefully timed non-Poisson intervals can. The result proves a complete, sharp boundary between deterministic boundedness, finite mean-square diffusion, and ballistic motion for every positive finite-mean renewal law. The jump from ballistic speed \(2/\pi\) to diffusivity asymptotic \(4/(\pi\sigma^2)\) for arbitrarily small jitter is quantitatively meaningful for phase-controlled microswimmer transport, not a numerical slice or routine reformulation of the Poisson case.

## Scientific limitations and residual risks

The theorem uses a fixed turn angle, constant curvature, no angular Brownian motion and finite-mean positive i.i.d. run lengths. It does not give a process-level CLT. The exact original derivations in Detcheverry (2017) remain a significant incomplete prior-work comparison; their possible stronger coverage requires independent literature review. The 2024 paper's diffusivity uses a different Euclidean normalization, which is reconciled explicitly in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
