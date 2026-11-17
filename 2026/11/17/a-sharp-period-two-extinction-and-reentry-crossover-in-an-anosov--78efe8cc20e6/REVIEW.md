# Scientific review: exact period-two extinction-and-reentry crossover

## Correctness — PASS

The domain, quantifiers, and exceptional endpoints are explicit in `RESULT.md`. The finite cat-map base census follows from determinants \(\det(A-I)=-1\) and \(\det(A^2-I)=-5\). A determinant-one matrix product represents the precise two-step Möbius fiber return. Its real trace has the analytic form \(2[\cos(2\pi\omega)+\varepsilon^2\cos(2\pi\mu\sigma_j)]/(1-\varepsilon^2)\). The trace decreases strictly over the parameter interval, giving exactly two, one, or zero boundary fixed points, with nonidentity proved separately at both parabolic equality cases. The single fixed base point supplies no primitive period-two orbit for \(\omega<1/2\). This exhaustion proves the full count. A trigonometric equality gives the sharp crossover, and differentiation proves its positive width slope. The standalone `verify.py` passed matrix determinant, trace, direct boundary-root, exact base-enumeration, and 400 ordering trials. Finite tests are secondary to the analytic proof.

## Originality — PASS within examined evidence

The originating paper, Chigarev–Kazakov–Pikovsky (arXiv:2305.18172v1, 2023-05-29), supplies the model, periodic-driver Möbius composition theory, and a numerical bifurcation atlas in its Section IV and Appendix A. Its accessible full text does not state the exact four boundary curves, equality case census, crossover threshold, or the disappearance/reappearance of the no-two-cycle frequency window. The closest identified published result, *Arithmetic isolation of identity resonances in a cat-driven Möbius map* (2026), derives a different statement on the strict zero-drift plane and cannot imply the two-sided drift transition. The new theorem uses established group theory rather than claiming it as new.

Residual risks: nonindexed equivalent calculations may exist in Möbius cocycle literature; a 2021 related article was assessed only by its accessible abstract and not used to make a whole-document noncoverage assertion. Published plotted bifurcation curves could allow retrospective derivation of the formula, but are not the exact symbolic classification or sharp three-parameter crossing asserted here. No independent audit has been performed.

## Mathematical value — PASS

The motivating problem is the periodic-orbit skeleton of a concrete Anosov-driven attractor–repeller collision model. Period two is the **first nontrivial base return**: its two distinct cat cycles provide the smallest natural complete nonfixed-driver census. The result distinguishes a finite-frequency interval with no primitive two-cycles from a parameter regime containing four distinct primitive two-cycles between different return-branch thresholds. The exact critical forcing and transverse crossing slope locate this structural change without reliance on plots, numerical continuation, or a non-exhaustive orbit sample. This is a natural complete classification of a low-period mechanism, not a claim of global chaotic-transition classification.

## Limits

Only \(\alpha=0\), \(0<\mu<1/2\), \(0<\varepsilon<1\), and \(0\leq\omega<1/2\) are covered. At \(\omega=1/2\), the fixed-base fiber becomes a projective involution, so this endpoint is excluded rather than silently assigned the same count. Higher-period and aperiodic dynamics are not characterized. Publication priority is not certified.

Self-review: passed. Independent audit: not yet performed.
