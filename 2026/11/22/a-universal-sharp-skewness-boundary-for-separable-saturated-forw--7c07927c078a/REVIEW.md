# Scientific review of the sharp planar saturation theorem

## Correctness — PASS

The statement has explicit quantifiers over all odd continuously differentiable, nondecreasing, bounded, unit-Lipschitz scalar saturations with the given endpoint derivatives, all real skew parameters and all positive stepsizes. The decisive cone argument applies to both signed coordinates: the saturation response and its residual occupy a common wedge of opening angle \(\pi/4\). It gives the stated sharp Fejér inequality. The local linearization at zero supplies necessity of the upper stepsize bound; the saturated large-state construction supplies necessity of the skew bound. A Jacobian column establishes that global pairwise nonexpansiveness is strictly stronger. The Lyapunov decrease of an explicitly defined convex potential establishes global convergence for strict subcritical steps. All limiting arguments and endpoints have been checked. `CHECK.py` passed 18,792 rational assertions. The tests support, but do not replace, the general proof.

## Originality — PASS (with historical-priority risk)

The closest primary source is Quan, Oikonomidis, Bodard and Patrinos, arXiv:2611.13916v1 (2026). Its Example 2.6 supplies the particular componentwise saturation and a skew example without Fejér monotonicity; Theorem 2.7 guarantees Fejér monotonicity for isotropic nonlinear preconditioners. Neither states a sharp universal skewness boundary for a class of separable saturations, a complete stepsize range, or the exact separation between convergence, Fejér behavior and pairwise nonexpansiveness in the specified planar family. The related Akram--Ishtiaq--Ahmad--Popa (2026) article gives general Jacobian criteria for nonexpansiveness in plug-and-play methods, but not the single-fixed-point Fejér boundary here. The algebraic techniques are elementary, and unknown unindexed equivalent formulations remain possible. No claim of exhaustive bibliographic certification is made.

## Value — PASS

There is an operational mathematical gap between convergence of an iteration, monotone decrease in distance to the root, and pairwise nonexpansiveness. The example motivating this study demonstrates loss of the second property for one selected skew; the theorem determines the exact angle at which that loss becomes unavoidable for an entire natural saturation class and proves that convergence survives beyond it. The sharp angular boundary and explicit derivative obstruction can inform the selection of geometric certificates and stepsizes for separable nonlinear preconditioning. This is a structural stability classification, not merely an additional finite example.

## Limits

The theorem concerns an exactly normal planar forward operator, two identical coordinate responses, exact arithmetic, and fixed stepsizes. It does not analyze larger systems, nonsymmetric coordinate nonlinearities, perturbations, noise, or practical runtimes. Convergence is not asserted at the limiting Fejér stepsize. Independent mathematical validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
