# Complete Fourier-orthogonality stratification of four consecutively supported positive masses

## Finding

For arbitrary strictly positive real masses \(a,b,c,d\) with \(a+b+c+d=1\), consider
\[
\mu=a\delta_0+b\delta_1+c\delta_2+d\delta_3,
\qquad e_\lambda(j)=e^{2\pi i\lambda j}.
\]
Let \(\mathcal O(\mu)\) be the largest cardinality of a set of **distinct functions** \(e_\lambda\) mutually orthogonal in complex \(L^2(\mu)\); frequencies are arbitrary real numbers, and are equivalent modulo \(1\). Then the following ordered classification holds:
\[
\boxed{\mathcal O(\mu)=
\begin{cases}
4,&a=b=c=d,\\
3,&b=c=a+d,\\
2,&\bigl(a+c=b+d\bigr)\ \text{or}\ \left(d(d-b)=a(a-c),\ |d-b|<2a\right),\\
1,&\text{otherwise}.
\end{cases}}
\]
The clauses are evaluated in the displayed order. In the three-character regime, **every maximum-cardinality** orthogonal family is, up to a common real frequency translation and integer changes of frequencies, \(\{e_0,e_{1/3},e_{2/3}\}\). In the four-character regime every optimal family is similarly \(\{e_0,e_{1/4},e_{1/2},e_{3/4}\}\). In the two-character regime, one may use \(\{e_0,e_{1/2}\}\) when \(a+c=b+d\); otherwise the frequencies \(0\) and \(\arccos(t)/(2\pi)\), with \(t=(d-b)/(2a)\), work. The one-character regime contains no nontrivial orthogonal pair.

The three-character, non-spectral locus has the precise positive one-parameter structure \(a+d=1/3\), \(b=c=1/3\), and \(0<a,d<1/3\). It is nonuniform even though it allows three orthogonal exponentials. Maximum cardinality is different from inclusion-maximality: at \((a,b,c,d)=(1,2,2,1)/6\), the orthogonal pair with phases \(0,1/2\) cannot be extended, since the only triples are translates of the three equally spaced phases. The four-character regime is exactly the uniform law.

## Assumptions and scope

The support is exactly the four consecutive integers \(0,1,2,3\), with strictly positive **real** masses summing to one. The characters are scalar complex exponentials with arbitrary real frequencies. The result is unchanged by a common translation of the four support sites or by a nonzero affine scaling of their spacing, after rescaling frequencies. No assertion is made for nonconsecutive support, vanishing or complex masses, or multivariate supports. The definition concerns maximum **cardinality** of a mutually orthogonal set, not maximal-by-inclusion sets or optimal approximate frames.

## Proof

**Step 1: zeros of the Fourier mask control all pairs.** Set
\[
P(z)=a+bz+cz^2+dz^3,\qquad
\widehat\mu(\xi)=P(e^{-2\pi i\xi}).
\]
Thus \(\langle e_\lambda,e_\eta\rangle_{L^2(\mu)}=P(e^{2\pi i(\lambda-\eta)})\), up to the harmless convention of complex-conjugate inner products. A pair is orthogonal precisely when its nonzero frequency difference modulo \(1\) corresponds to a unit-circle zero of \(P\). Since \(P(1)=1\), no zero has phase \(0\). Because \(P\) has real coefficients and degree three, its set \(Z\) of distinct unit-circle root phases is contained in \(\{1/2,u,1-u\}\), with \(0<u<1/2\), where either the antipodal phase \(1/2\), the conjugate pair \(u,1-u\), or both may be absent.

**Step 2: a three-point phase clique forces cube-root or fourth-root resonance.** Translate any three orthogonal frequencies to \(0,x,y\) modulo \(1\). Then \(x,y,x-y\in Z\). If \(x,y\) are the conjugate phases \(u,1-u\), then \(2u\bmod1\in\{u,1-u,1/2\}\); as \(0<u<1/2\), the only solutions are \(u=1/3\) and \(u=1/4\). If one of \(x,y\) is \(1/2\), the other is a conjugate phase; requiring their difference also to lie in \(Z\) forces \(u=1/4\). A set \(Z=\{1/2\}\) clearly cannot yield three distinct frequencies. Therefore a triple forces either the primitive cube-root pair or all three nontrivial fourth roots of unity to be zeros of \(P\). Conversely either root configuration produces a triple, by taking \(\{0,1/3,2/3\}\) or \(\{0,1/4,1/2\}\).

**Step 3: coefficient rigidity for triples.** If both primitive third roots vanish, the real polynomial \(P\) is divisible by \(1+z+z^2\). Since the leading and constant coefficients are respectively \(d\) and \(a\), this divisibility gives
\[
P(z)=(a+dz)(1+z+z^2)
=a+(a+d)z+(a+d)z^2+dz^3,
\]
so it holds exactly when \(b=c=a+d\). If instead all three nontrivial fourth roots vanish, then \(P(z)=d(1+z+z^2+z^3)\), forcing \(a=b=c=d\). Thus any orthogonal triple obeys one of the first two coefficient conditions. The two conditions are disjoint for strictly positive weights. In the nonuniform triple condition, the only possible phase clique is the cube-root coset; this also proves the claimed classification of all triples.

**Step 4: four characters.** The four-dimensional Hilbert space \(L^2(\mu)\) cannot contain five nonzero mutually orthogonal characters. If four exist, let \(F\) be their \(4\times4\) matrix of normalized values, with rows indexed by the atoms and entries \(F_{j,k}=\sqrt{w_j}e^{2\pi i\lambda_kj}\). Its columns are orthonormal, hence \(F\) is unitary. Every row has squared Euclidean norm \(4w_j\), so \(4w_j=1\) for all rows and all weights equal \(1/4\). Conversely, the four frequencies \(0,1/4,1/2,3/4\) yield the standard four-point discrete Fourier basis for uniform weights. Translate one frequency to zero. The other three must have distinct residues \(1/4,1/2,3/4\) modulo \(1\), since these are the only nonzero zero phases of the uniform mask.

**Step 5: every possible orthogonal pair.** The phase \(1/2\) is a Fourier zero precisely when \(P(-1)=a-b+c-d=0\), equivalently \(a+c=b+d\). Any other unit-circle zero comes with its distinct complex conjugate. Such a pair can be written as the roots of \(z^2-2tz+1\) for a uniquely determined \(-1<t<1\). Thus it occurs exactly when
\[
P(z)=(a+dz)(z^2-2tz+1),\quad
b=d-2ta,\quad c=a-2td.
\]
Eliminating \(t=(d-b)/(2a)\) gives
\[
d(d-b)=a(a-c),\qquad |d-b|<2a.
\]
This condition is also sufficient: it constructs the conjugate unit-circle pair. Since every real cubic's unit-circle zeros are either \(-1\) or one such conjugate pair (or both), the displayed disjunction is the **complete** criterion for a nontrivial orthogonal pair. Taking the triple and quadruple cases first now gives the asserted four-stratum formula.

## Verification

The included executable \(CHECK.py\) checks both polynomial factorizations on 81 exact rational parameter tuples and, independently of the predicate's logical branches, enumerates the unit-circle roots and orthogonality graphs for all \(6^4=1296\) positive integer coefficient quadruples with entries from \(1\) to \(6\). All cases agree with the stated formula; the graph counts are \(1102,173,15,6\) for capacities \(1,2,3,4\), respectively. Repeated polynomial roots are first stripped algebraically before numerical root localization. The checker also tests explicit unbalanced three-character cases and boundary regimes. These **finite checks are not an exhaustive test of arbitrary real weights**; the proof above supplies that quantifier.

For direct hand checks: \((a,b,c,d)=(1,3,3,2)/9\) gives three orthogonal characters; \((1,1,1,1)/4\) gives four; \((1,2,4,3)/10\) gives two by the alternating zero; and \((1,3,2,1)/7\) has capacity one.

## Relationship to prior work

Fu and Song (first public 22 July 2026) prove rational-spectrum rigidity for **full, equal-mass finite Hadamard pairs**; this does not provide a maximal-cardinality classification for incomplete orthogonal families with arbitrary positive weights. Li and Wang (29 July 2026) study cardinality bounds for **infinite self-affine measures in three dimensions**, not finite four-atom line measures. Published results on Fourier zeros for **symmetric four-atom measures** and phase-only consecutive quadrinomials concern related root structures, but their public descriptions do not settle arbitrary unequal positive masses and the four-stratum orthogonality capacity. The present result uses the standard mask-zero criterion, then adds the exact triangle-clique obstruction and all-weight classification.

## Limitations

The classification does not imply a general theory for more than four atoms, nonconsecutive supports, or infinite convolutions. Its originality is assessed against the cited source material and indexed searches, not certified against every older or unindexed result; a restricted symmetric four-atom Fourier-zero result was identified, but its full text was not available for complete implication comparison. The claims in this document require independent mathematical review before they should be regarded as externally validated.

## References

1. Xiao-Ye Fu and Zi-Jian Song, *Rational Spectra for Finite Hadamard Pairs and Bounded Spectral Sets on the real line*, arXiv:2607.19858, first posted 22 July 2026. https://arxiv.org/abs/2607.19858
2. Ya-Qi Li and Zhi-Min Wang, *The Number of Orthogonal Exponential Functions of a Class of Self-Affine Measures in* \(\mathbb R^3\), *Axioms* 15 (2026), 563, 29 July 2026. https://doi.org/10.3390/axioms15080563
3. *Sharp parity-dependent complex-zero transition for symmetric four-atom Fourier transforms*, publicly indexed mathematical finding, 27 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/27/SCOPE-sharp-parity-dependent-complex-zero-transition-for-symmetric-fou--db8d34ed1235
4. *Parity classification of Fourier zeros for phase-only consecutive quadrinomials*, publicly indexed mathematical finding, 4 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-parity-classification-of-fourier-zeros-for-phase-only-consecutiv--f8559da4c3f3
