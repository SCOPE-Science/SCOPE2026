# Delayed complete-Pick failure in two-root fractional Schur products

## Finding

Fix \(0<a<1\) and \(0<b<1\). On the complex unit disk \(\mathbb D\), put \(t=z\overline w\) and
\[
 K_{a,b}(z,w)=\frac{1}{(1-t)^a(1-t^2)^b},\qquad
 c_n(a,b)=[t^n]\left(1-\frac1{K_{a,b}}\right),\quad n\ge1.
\]
Both factors \((1-t)^{-a}\) and \((1-t^2)^{-b}\) are normalized complete Nevanlinna–Pick kernels (the second is the pullback by \(z\mapsto z^2\)). Nevertheless **their product never has the complete Pick property** for \(b>0\): there are infinitely many negative odd coefficients \(c_n(a,b)\). For every fixed \(b\in(0,1)\), all sufficiently large even coefficients are positive and all sufficiently large odd coefficients are negative.

Write the first obstructing index as
\[
 N_a(b)=\min\{n\ge1:c_n(a,b)<0\}.
\]
For each fixed \(0<a<1\), this index exists and has the **sharp small-factor law**
\[
 \boxed{\displaystyle N_a(b)\sim
 \left(\frac{a}{2^a\Gamma(1-a)b}\right)^{1/a}}
 \qquad (b\downarrow0).
\]
More precisely, if \(b\downarrow0\), \(n\to\infty\), and \(bn^a\to x\in[0,\infty)\), then, separately for even and odd indices,
\[
 \boxed{\displaystyle n^{a+1}c_n(a,b)\longrightarrow
 \frac{a}{\Gamma(1-a)}+(-1)^n2^a x.}
\]
Here the parity is held fixed along the sequence. Thus any finite coefficient test stays positive when \(b\) is small enough, despite the eventual failure, and the exact growth scale of the first witness is determined. At the Hardy endpoint \(a=1\), the contrasting exact law is \(N_1(b)=3\) for every \(0<b<1\).

## Assumptions and scope

All powers use their holomorphic branch at \(t=0\). Parameters \(a,b\) are real. Coefficient signs are ordinary real Taylor signs. A normalized, nowhere-vanishing radial kernel \(K(z,w)=\sum_{n\ge0}k_n(z\overline w)^n\), whose coefficients are all strictly positive, has the complete Pick property exactly when all coefficients of \(1-1/K\) in degrees at least one are nonnegative. This is the normalized McCullough–Quiggin/Agler–McCarthy criterion: positivity of the radial kernel \(1-1/K\) is equivalent to positivity of all its Taylor coefficients. The stated product has strictly positive coefficients because the first factor does. For its second factor separately, the noninjective pullback formulation is used, with compatible interpolation data on identified points.

The first-index asymptotic is for **fixed** \(a\in(0,1)\) and \(b\downarrow0\); it is not claimed uniform as \(a\to0\) or \(a\to1\). An asymptotic first witness does not determine a finite closed-form integer for every pair of parameters.

## Proof

**1. Separate complete-Pick factors.** For \(0<\eta\le1\), the series
\[
 1-(1-t)^\eta=\sum_{j\ge1}(-1)^{j-1}\binom{\eta}{j}t^j
\]
has nonnegative coefficients, which sum to one at the boundary. Its positive-kernel feature representation shows that \((1-t)^{-\eta}\) is complete Pick. Composition of this representation with \(z\mapsto z^2\) proves the same for \((1-t^2)^{-b}\). Multiplication of positive kernels proves that \(K_{a,b}\) is a normalized positive, nowhere-vanishing kernel, with positive coefficients in every degree.

**2. Uniform two-endpoint coefficient lemma.** Set
\[
 F_b(t)=(1-t)^{a+b}(1+t)^b=\sum_{n\ge0}f_n(a,b)t^n,
 \qquad c_n(a,b)=-f_n(a,b)\ (n\ge1).
\]
Fix \(a\in(0,1)\), and choose \(b_0>0\) so small that \(a+b_0<1\). There is a constant \(C=C(a,b_0)\) such that for \(0<b\le b_0\) and \(n\ge1\),
\[
 \begin{aligned}
 c_n(a,b)&=A(b)n^{-a-b-1}+(-1)^nB(b)n^{-b-1}+R_n(a,b),\\
 A(b)&=-\frac{2^b}{\Gamma(-a-b)}>0,\qquad
 B(b)=-\frac{2^{a+b}}{\Gamma(-b)}>0,\\
 |R_n(a,b)|&\le C\big(n^{-a-b-2}+b\,n^{-b-2}\big).
 \end{aligned}
\]
To verify the error with its crucial factor \(b\), take a Cauchy coefficient contour cut into two fixed dented neighborhoods of \(t=1\) and \(t=-1\), with the remaining arcs lying outside the unit circle. At \(t=1\), expand the analytic factor \((1+t)^b=2^b+O_{b_0}(|1-t|)\); its first discarded singular term is of order \((1-t)^{a+b+1}\). At \(t=-1\), expand \((1-t)^{a+b}=2^{a+b}+O_{a,b_0}(|1+t|)\). The coefficient of the leading power \((1+t)^b\) is \((-1)^n n^{-b-1}/\Gamma(-b)+O(bn^{-b-2})\), uniformly as \(b\downarrow0\), by the exact Gamma-ratio formula. Every discarded power \((1+t)^{b+j}\), \(j\ge1\) fixed, has reciprocal Gamma factor \(1/\Gamma(-b-j)=O_j(b)\), giving the displayed second remainder. Algebraic singularity transfer on the two Hankel contour pieces supplies the first remainder, uniformly on the compact exponent interval. This also justifies the expansion without assuming a finite coefficient calculation is an infinite proof.

For a fixed \(b\in(0,1)\), the same two-branch-point transfer gives
\[
 c_n(a,b)=(-1)^n B(b)n^{-b-1}+o(n^{-b-1}),
\]
because the contribution from \(t=1\) is \(O(n^{-a-b-1})\). This continues to hold if \(a+b\) happens to be an integer, when the corresponding local term is analytic. Consequently, the even coefficients are eventually positive and the odd ones eventually negative. The complete Pick criterion now proves the first assertion and existence of \(N_a(b)\).

**3. Scaling profile.** For \(b\downarrow0\), the Gamma expansions give
\[
 A(b)\longrightarrow A_0=\frac{a}{\Gamma(1-a)},
 \qquad \frac{B(b)}b\longrightarrow2^a.
\]
If \(bn^a\to x<\infty\), then \(b\log n\to0\), hence \(n^{-b}\to1\). Multiply the uniform lemma by \(n^{a+1}\): the error is bounded by a constant times \(n^{-b-1}+bn^{a-b-1}\), which tends to zero. This proves the claimed parity-dependent scaling limit, including \(x=0\).

**4. Localization of the first negative index.** Put
\[
 M_a(b)=\left(\frac{A_0}{2^ab}\right)^{1/a}.
\]
For any fixed \(\varepsilon\in(0,1)\), the uniform lemma and the strictly positive margin \(A_0[1-(1-\varepsilon)^a]\) imply \(c_n(a,b)>0\) for all sufficiently small \(b>0\) and all integers \(1\le n\le(1-\varepsilon)M_a(b)\). To cover small indices, first fix a large integer \(n_0\) making the lemma's relative remainder small; for \(n<n_0\), coefficientwise continuity at \(b=0\) and the strictly positive coefficients of \(1-(1-t)^a\) provide positivity. For indices above \(n_0\), the lemma yields the uniform positive margin. On the other hand, choose an odd integer \(n\sim(1+\varepsilon)M_a(b)\); the scaling profile is strictly negative there. Thus
\[
 (1-\varepsilon)M_a(b)<N_a(b)\le(1+\varepsilon)M_a(b)+O(1).
\]
Letting \(\varepsilon\downarrow0\) proves the sharp equivalent.

**5. Hardy endpoint.** For \(a=1\), the reciprocal is \((1-t)(1-t^2)^b\). Direct expansion gives \(c_1=1\), \(c_2=b\), and \(c_3=-b\), so \(N_1(b)=3\).

## Verification

The standalone `CHECK.py` (Python standard library only) computes exact rational Taylor coefficients two independent ways: via the first-order differential-equation recurrence and via convolution of the two binomial series. It checks agreement and the first obstructing index for several rational parameters, with exact sign tests through thousands of coefficients. Run `python CHECK.py` after extracting the file. The finite checks test examples and code paths; the infinite sign law and small-parameter limit are proved by the two-endpoint argument above, not inferred from computations.

## Relationship to prior work

Bhattacharyya, Jaikishan and Kumar (2026, arXiv:2605.21808v1, section 3 and Theorem 3.2) study multiplicative linear functionals for Schur products of two complete Pick kernels. Their theorem assumes the factorization and characterizes linear functionals; it does not characterize when the product remains complete Pick or find its first negative reciprocal coefficient. The present example stays within that natural factorization class and analyzes a different property.

Aleman, Hartz, McCarthy and Richter (2018) prove function-space factorizations induced by a complete Pick factor, without a coefficient-detection law for products. Agler and McCarthy (2000) supply the general complete Pick criterion used here, not this two-root obstruction. A distinct published monomial-defect theorem classifies \((1-st^m)(1-t)^{-\gamma}\) and compares its threshold with multiplier contractivity; that is a **numerator defect**, not our infinite fractional **denominator Schur factor**. A separate monomial-pole family \([(1-t)^a(1-\tau t^m)]^{-1}\) exhibits a positive small-amplitude complete-Pick interval. Its analytic perturbing factor has its extra singularities outside the disk when \(\tau<1\), whereas the fractional factor here introduces a branch singularity at \(t=-1\) for every \(b>0\). Neither result implies the delayed threshold \(N_a(b)\sim C_ab^{-1/a}\).

## Limitations

The result concerns the displayed two-root fractional family, not arbitrary Schur products. The second factor is a pullback and has identical kernel sections at opposite points; it is complete Pick in the natural pullback sense. The first-obstruction index is asymptotically located, not expressed exactly for all finite parameters. No uniformity in \(a\) at its endpoints, sharp error bound for the integer first index, or stability under unrelated perturbations is claimed. Earlier equivalent coefficient asymptotics outside accessible indexed sources remain possible; this is a self-review, not an independent priority certification.

## References

1. T. Bhattacharyya, Jaikishan and P. Kumar, *Multiplicative linear functionals on reproducing kernel Hilbert spaces*, arXiv:2605.21808v1, 20 May 2026, https://arxiv.org/html/2605.21808v1.
2. J. Agler and J. E. McCarthy, *Complete Nevanlinna–Pick kernels*, Journal of Functional Analysis **175** (2000), 111–124, https://doi.org/10.1006/jfan.2000.3600.
3. A. Aleman, M. Hartz, J. E. McCarthy and S. Richter, *Factorizations induced by complete Nevanlinna–Pick factors*, Advances in Mathematics **335** (2018), 372–404, https://doi.org/10.1016/j.aim.2018.07.013.
4. *Sharp complete-Pick phase diagram for monomial defects of power kernels*, published published-finding corpus record, 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-complete-pick-phase-diagram-for-monomial-defects-of-power--a614d1883358.
5. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), Chapter VI (transfer of algebraic singularities), https://algo.inria.fr/flajolet/Publications/books.html.
