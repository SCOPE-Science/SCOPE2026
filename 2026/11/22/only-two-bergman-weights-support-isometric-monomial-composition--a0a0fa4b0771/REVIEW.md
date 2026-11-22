# Self-review

## Correctness — PASS

The monomial norm identities are moments of finite positive measures. Substitution \(u=t^N\) and Hausdorff uniqueness force the exact coefficient-modulus generating function \(Q(t)=Nt^{N-1}(1+\cdots+t^{N-1})^\alpha\). The off-diagonal moment identities, justified by Cauchy–Schwarz integrability, force at most one nonzero multiplier coefficient in each residue class modulo \(N\). Thus \(Q\) is a polynomial. Rational logarithmic derivatives at simple nontrivial \(N\)-th roots of unity make \(\alpha\) a nonnegative integer, and support length forces \(\alpha\in\{0,1\}\). Explicit coefficient norms and disjoint supports verify both isometry branches for all monomials, with extension by density. Boundaries: \(N\ge2\), \(\alpha>-1\), all analytic multipliers; there are no arbitrary-polynomial or numerical assumptions. `check.py` passes 7,106 exact finite supplementary checks, not an infinite certification.

## Originality — PASS (qualified)

Full text of Chalendar–Partington arXiv:1910.01475, especially Theorem 4.3, Remark 4.4 and Proposition 4.5, gives generic isometric measure-pullback criteria and the \(\alpha=0\) derivative construction, but not the \(\alpha=1\) phase torus or exclusion of every other \(\alpha\). Zorboska's May 2018 slides give the pullback density criterion for arbitrary standard Bergman weights and special cases, but no full classification for monomial power composition with unrestricted analytic multiplier. Kim's 2022 thesis §5.3 fixes *both* symbols to be monomials; Mas–Vukotić study surjective isometries. Comparisons with published mathematical records for the same symbols, parameters, and equivalent formulations did not identify the same classification. An inaccessible full original paper by Zorboska (2018) remains a genuine potential historical-priority risk; a general criterion may be specialized, but the integer-residue rigidity proof and the exact phase classification require additional nontrivial analysis.

## Mathematical value — PASS

A natural precise classification problem left implicit by general measure criteria is settled for every integer covering degree and every standard Bergman power exponent. The isolated \(\alpha=1\) isometry family and its \(N\) independent phases, together with the impossibility for other exponents, disclose a sharp structural boundary: weighted Hilbert-space isometry is highly sensitive to the radial measure. This is not a routine renaming or a finite numerical observation, and its elementary methods explain the rigidity rather than just exhibiting examples.

## Limits and residual priority risk

The result does not cover arbitrary inner functions or all radial weighted spaces. The reviewed 2018 journal paper was not available in full through accessible open sources; its 2018 author's lecture and a subsequent 2019 paper state the general characterizations but not this explicit classification. Independent mathematical review has not been performed.

Self-review: passed. Independent audit: not yet performed.
