# Scientific assessment: anisotropic bounded-noise curvature transition

## Correctness — PASS

The claim fixes the closed-disk support, \(0<a<b<1\), and all limits; no random-sample assertion is used. The unique compact invariant attractor is the Hausdorff-convergent Minkowski sum of the iterated noise ellipses. Its support is an absolutely convergent sum of square roots. Away from the fast-axis normals, two derivatives can be taken termwise, giving the explicit radius series. At the two axis tips, the reciprocal radius has a finite continuous limit even where the radius diverges; the graph identity \(dX/dY=-\tan\theta\) and its derivative show geometric \(C^2\) regularity without assuming the support is \(C^2\) in angle. At the critical ratio, geometric splitting at \(\log_q(1/|\tan\theta|)\) gives the exact logarithmic coefficient. Above it, bilateral series convergence uniformly in fractional logarithmic phase gives the periodic profile. A beta-integral with nonvanishing gamma factors proves genuine nonconstancy; sampled numerical phases alone would be insufficient. The standalone exact-rational and numerical checker corroborates these steps but is not offered as proof of an infinite-dimensional regularity or limit assertion.

## Originality — PASS within identified evidence

The strongest matching source is Lamb–Rasmussen–Tey (arXiv:2310.03437v1), which establishes a unique strictly convex \(C^1\) attractor in this setting and explicitly leaves precise smoothness, including \(C^2\), unresolved. Tey's 2022 thesis introduces the exact diagonal example and independently calls \(C^2\) a conjecture, but computes neither axis curvature nor sharp ratio threshold. Kourliouros and collaborators assume higher regularity in a conditional persistence theorem. Pochinka–Yagilev (2025) classify hyperbolic periodic points of the **boundary map** and its invariant normal bundle for distinct real eigenvalues, whereas the present claim computes a **geometric second derivative of the attractor boundary**, its zero-curvature locus, critical divergence and nonconstant scaling function. Hashemi–Ruths (2020) derive support-point formulas for finite sums of ellipsoids; the infinite geometric series and threshold are neither a finite case nor a direct stated corollary. The closest recovered mathematical research records address unrelated curvature functionals, flow balance laws, or other attractors. No mathematical implication of a checked stronger theorem subsumes the specified curvature classification. Discovery is limited by index coverage and possible unidentified literature, not by a proof of uniqueness.

## Value — PASS

The originating work explicitly asks for higher boundary regularity, partly because \(C^2\) smoothness is needed in a smooth-persistence framework. This result settles it for a natural, genuinely anisotropic diagonal family without artificial parameter fixing. The sharp quantity \(b^2/a\) distinguishes everywhere positive curvature from two flat endpoints even though \(C^2\) smoothness persists across the transition. The critical logarithmic law and nonconstant log-periodic power regime resolve the precise degeneracy, rather than merely improving a numerical bound. The geometry is intrinsically tied to long-term bounded-noise reachability and is not a rephrased finite-ellipse exercise.

## Sources and residual risks

Source-level comparisons inspected [1] the primary full article (Sections 2–5 and Outlook), [2] the matching thesis (Chapter 4 diagonal example and Chapter 5 curvature-map analysis), [3] the smooth persistence preprint's stated hypotheses and main results, [4] the 2025 publisher full-text article including its numbered main theorem and proof sections, and [5] the 2020 finite-ellipsoid-sum paper's full HTML mathematical exposition. The accessible texts do not state the same infinite-series curvature threshold or log-periodic asymptotics. A generic theorem about sums of convex bodies or an unindexed publication might imply part of the result; independent priority review remains necessary. The claim excludes nonpositive, repeated, complex or nonnormal spectra, non-ball noise supports, and nonlinear persistence. No external independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.

## References

[1] Lamb, Rasmussen, Tey, *Attractors of Linear Maps with Bounded Noise*, arXiv:2310.03437v1 (2023), https://arxiv.org/abs/2310.03437.

[2] Tey, *On Minimal Invariant Sets of Certain Set-Valued Dynamical Systems – A Boundary Map Approach*, PhD thesis (2022), https://www.researchgate.net/publication/366016533_On_Minimal_Invariant_Sets_of_Certain_Set-Valued_Dynamical_Systems_-_A_Boundary_Map_Approach.

[3] Kourliouros et al., *Smooth Persistence of Attractors for Set-Valued Dynamical Systems: A Boundary Map Approach*, arXiv:2303.01895, https://arxiv.org/abs/2303.01895.

[4] Pochinka and Yagilev, *Dynamics of the boundary map of a system with spherical noise*, Theoret. Math. Phys. 224 (2025), doi:10.4213/tmf10870.

[5] Hashemi and Ruths, *Generalized Outer Bounds on the Finite Geometric Sum of Ellipsoids*, arXiv:2006.08739 (2020), https://arxiv.org/abs/2006.08739.
