# Self-review

## Correctness — PASS

The polynomial congruence \(D_p(X,a)\equiv X^p\pmod p\) and the normalized derivative identity \(D_p'(X,a)/p\equiv(X^2-4a)^{(p-1)/2}\pmod p\) identify every ordinary residue class. The resulting normalized branch polynomial is congruent to a nonzero linear function modulo \(p\), hence Hensel lifting gives an exact image ball, not merely a containment. For square parameters, the Dickson factorization \(D_p(Y,1)-2=(Y-2)P_p(Y)^2\), together with \(P_p(2)=p\) and \(P_p'(2)\equiv0\pmod p\), gives the exceptional surjection onto \(2+p^3\mathbb Z_p\). Oddness handles the negative branch. Disjointness, fiber sizes, and all-power counts follow. Direct symbolic identities at five primes and exhaustive finite residue enumerations in 108 cases corroborate the symbolic proof without replacing it. The small-prime restriction is real: the \(p=3\) example contradicts extrapolation.

## Originality — PASS, with a defined residual literature risk

The direct 1991 predecessor of Bremser and Gómez-Calderon establishes ordinary Dickson fibers and bounds exceptional branches but does not state the explicit all-power prime-index image/fiber law obtained here. Its source text was read for hypotheses, statements, and limitations, though the online typesetting of some formulas is imperfect. Shang's 2023 bounds are for general non-permutation polynomials and do not fix Dickson images. Brazelton, Harrington, Litman, and Wong address finite fields rather than the residue rings in this theorem. Equivalent descriptions via first-kind Chebyshev polynomials and the reduction of \(D_p\) modulo \(p\) were compared. No statement found implies the two exact local image densities and complete fiber law. The comparison is evidence of originality, not proof of absolute uniqueness; a more complete typeset 1991 text or other unlocated literature could clarify priority.

## Value — PASS

The prime-index case is a natural, characteristic-ramified boundary for first-kind Dickson maps. Instead of only bounding the exceptional fibers as in the closest predecessor, the theorem describes every residue at every power and quantifies precisely the change between quadratic-residue and quadratic-nonresidue parameters. The two narrow exceptional balls produce a measurable difference between the two \(p\)-adic image densities, while the uniform full fiber histograms give a reusable local-solubility criterion. The classification is not a numerical instance of a generic Hensel bound: its critical factorization resolves singular branches uniformly for every prime at least five.

## Closest literature and limitations

Bremser–Gómez-Calderon, *Value sets of Dickson polynomials over Galois rings*, J. Number Theory 38 (1991), DOI 10.1016/0022-314X(91)90087-R; Shikui Shang, *Value sets of non-permutation polynomials over the residue class rings of integers*, arXiv:2310.20226 (2023); Brazelton et al., *Residue sums of Dickson polynomials over finite fields*, arXiv:2103.09119 (2021). The theorem excludes ramified characteristic three, nonunit parameters, other degrees, and Galois rings of nontrivial residue degree. The direct predecessor's available online transcription has imperfect formulas. Finite computational checks do not certify arbitrary primes.

Self-review: passed. Independent audit: not yet performed.
