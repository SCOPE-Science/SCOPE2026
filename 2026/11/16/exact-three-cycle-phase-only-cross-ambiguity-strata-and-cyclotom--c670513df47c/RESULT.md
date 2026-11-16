# Exact three-cycle phase-only cross-ambiguity strata and cyclotomic counts

## Finding

Let \(\omega=e^{2\pi i/3}\). Normalize nonvanishing, unit-modulus sequences \(f,g:\mathbb Z_3\to\mathbb T\) by \(f(0)=g(0)=1\), and define their unnormalized cross short-time Fourier transform by
\[
V_g f(x,k)=\sum_{t=0}^{2} f(t)\overline{g(t-x)}\,\omega^{-kt},\qquad x,k\in\mathbb Z_3.
\]
For \(x,j\in\mathbb Z_3\), define the two-dimensional torus
\[
\mathcal T_{x,j}=\bigl\{(f,g): f(t)=\omega^{jt}g(t-x)/g(-x)\ \text{for all }t\in\mathbb Z_3\bigr\}.
\]
The nine tori have the following exact incidence: tori with the same \(x\) are disjoint; any two with different \(x\) meet in exactly three points; all intersections are triple, with one torus for each \(x\). There are precisely 27 triple-intersection points, namely
\[
g(t)=\omega^{at^2+bt},\qquad f(t)=\omega^{jt}g(t),\qquad a,b,j\in\mathbb Z_3.
\]
The cross-STFT support is 3 at these 27 points, 7 at points in precisely one torus, and 9 elsewhere; all other values are impossible. For support 7 the two zeros lie on one fixed translation row; for support 3 there are two zeros on each of the three rows.

Moreover, for every integer \(q\ge3\) divisible by 3, restrict \(f,g\) to the \(q\)-th roots of unity and retain the independent global-phase normalization. Among the \(q^4\) ordered pairs, the exact counts of support 3, support 7, and support 9 are respectively
\[
\boxed{27,\quad 9q^2-81,\quad q^4-9q^2+54.}
\]
Thus the three-phase alphabet has only support sizes 3 and 9, whereas every alphabet with \(3\mid q\) and \(q>3\) admits all three support sizes. The formulas hold for arbitrarily large \(q\), not merely for the verified sample alphabets. The support-seven stratum has the explicit witness \(f=g=(1,1,\zeta)\), where \(\zeta\) is any primitive \(q\)-th root with \(q>3\) and \(3\mid q\); the constant pair witnesses support three, and \(f=(1,1,1),\ g=(1,1,\zeta)\) witnesses support nine.

## Assumptions and scope

All sequences have exactly three nonzero, equal-modulus entries; without loss of generality their common coordinate moduli are 1. The two global complex phases are removed separately using the values at zero. For discrete counting, the alphabet is \(\mu_q=\{e^{2\pi i m/q}:0\le m<q\}\), with \(q\ge3\) and \(3\mid q\). The normalization of the transform itself is irrelevant to its support. Every support assertion concerns the nine points of \(\mathbb Z_3\times\mathbb Z_3\).

## Proof

**Three-point Fourier rigidity.** If three complex numbers of modulus 1 sum to zero, they are a common scalar multiple of the three cube roots of unity, each occurring exactly once. Indeed, two unit vectors have a sum of unit length only when their angular separation is \(2\pi/3\). Since every permutation of the cube roots has exponents affine in \(t\in\mathbb Z_3\), the Fourier transform of a unimodular triple \(a(t)\) has a zero at some \(k\) if and only if \(a(t)=c\omega^{jt}\) for some \(c\in\mathbb T\) and \(j\in\mathbb Z_3\). In this case it has exactly one nonzero Fourier coefficient, at \(k=j\); otherwise all three coefficients are nonzero.

Apply this criterion to \(a_x(t)=f(t)\overline{g(t-x)}\). The translation row indexed by \(x\) has two zeros if and only if \((f,g)\in\mathcal T_{x,j}\) for one (necessarily unique) \(j\). Otherwise it has no zeros. The only issue is the possible number of exceptional translation rows.

Suppose distinct translations \(x,y\) both have two zeros. Dividing the defining identities shows that \(g(t-x)/g(t-y)\) is a scalar times a character \(\omega^{ht}\). A cyclic reindexing and the fact that \(x-y\ne0\) yield \(g(t)/g(t-1)=c\omega^{ht}\), possibly with a different \(c\) and \(h\). Multiplying this relation over \(t=0,1,2\) gives \(c^3=1\). Hence every successive ratio of \(g\) is a cube root of unity. Because \(g(0)=1\), \(g\) is a normalized ternary phase word, uniquely expressible as \(g(t)=\omega^{at^2+bt}\) with \(a,b\in\mathbb Z_3\). The exceptional-row identity then implies that \(f\) is ternary and \(f(t)=\omega^{jt}g(t)\) for some \(j\). Conversely, for every such pair,
\[
\frac{g(t)}{g(t-x)}=\omega^{2axt-ax^2+bx}
\]
is a scalar times a character; therefore all three translation rows have exactly two zeros. In particular precisely two exceptional rows never occur.

The parameters \(a,b,j\in\mathbb Z_3\) are independent and unique, giving exactly \(3^3=27\) triple-intersection points. At such a point the exceptional character slope for translation \(x\) is \(j+2ax\). Given distinct translations \(x,y\) and prescribed slopes \(j_x,j_y\), these two equations uniquely determine \(a\) and \(j\), leaving precisely three possibilities for \(b\). This gives three points in every cross-translation pairwise intersection. Same-translation tori cannot intersect because a Fourier row cannot have two different surviving frequencies. This proves the topological incidence and the support classification for arbitrary continuous phases.

For the finite alphabet \(\mu_q\), \(3\mid q\) ensures that all factors \(\omega^{jt}\) are permitted. Each torus therefore contains exactly \(q^2\) normalized pairs (choose the two free coordinates of \(g\)); its pairwise and triple intersections are the same 27 ternary points as above. There are nine tori. Their union has \(9q^2-81+27=9q^2-54\) points because the three choices of translation-pair and nine choices of slope-pair give 27 pairwise intersections, each of size three, while there are 27 triple points. Removing the 27 triple points yields \(9q^2-81\) support-seven pairs. The rest of the \(q^4\) pairs have full support. This proves every formula and every forbidden support value.

## Verification

The included standalone `check.py` enumerates all normalized phase-word pairs for \(q=3,6,9,12\), evaluates support by modular congruences, and independently recomputes all nine transform entries using the complex DFT. The exact modular test counts two missing Fourier values in a row precisely when its phase-exponent differences form a cube-root character. The two methods agree for every pair and yield respectively \((27,0,54)\), \((27,243,1026)\), \((27,648,5886)\), and \((27,1215,19494)\), in support order \((3,7,9)\). It also checks all nine torus membership sets and their pairwise intersections in the divisible-by-three cases, and checks \(q=2,4\) to test the distinct coprime-to-three boundary, without extending the stated enumerative claim. The finite tests corroborate but are not substitutes for the preceding proof for all divisible-by-three \(q\).

To reproduce, run `python3 check.py` with the standard Python library. The script has no package dependencies, file inputs, or network calls.

## Relationship to prior work

Krahmer, Pfander and Rashkov (arXiv:math/0611493, especially Figure 7 and Appendix 6.4) already classify possible cross-STFT support sizes for unrestricted nonzero vectors on the three-cycle; full-coordinate support permits additional support values 6 and 8 using unequal coefficient magnitudes. Therefore the present support-only statement is not original in an unrestricted setting. The new claim is the **phase-only** exclusion of those values and the complete nine-torus incidence, discrete alphabet counts and sharp three-phase versus larger-alphabet transition. These properties do not follow from the unrestricted existence census.

Nicola (arXiv:2204.14176, first posted 2022-04-29) describes equality in the general finite-cyclic STFT uncertainty bound; it does not classify the nonminimal phase-only stratum or the multiplicity of phase-quantized pairs. General time-frequency support lower bounds and a published one-step support gap do not fix the present phase-only spectrum or counts. The closest indexed three-tap and phase-alphabet results concern different prime lengths, sparse rather than full-support words, or alphabets coprime to the cycle length. All these implication comparisons concern the specific quantifiers of the stated claim, not just title overlap.

## Limitations

This is an exact theorem for length three. It does not extend these counts to longer cyclic orders, unequal-modulus signals, noisy data, or general support patterns. The 2006 unrestricted three-cycle classification substantially overlaps the elementary support framework, and the priority of the particular phase-only enumeration and torus incidence remains subject to older or unindexed specialist sources. The geometric argument is fully mathematical; numerical enumeration alone would not establish the theorem. No independent mathematical audit has been performed.

## References

- F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176 (first public version 2022-04-29), https://arxiv.org/abs/2204.14176.
- F. Krahmer, G. E. Pfander and P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, arXiv:math/0611493 (2006), especially Figure 7 and Appendix 6.4, https://arxiv.org/abs/math/0611493.
