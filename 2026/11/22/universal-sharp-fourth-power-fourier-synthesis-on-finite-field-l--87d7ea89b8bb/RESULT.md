# Universal sharp fourth-power Fourier synthesis on finite-field line pencils

## Finding

Let \(q\ge 2\) be any prime power, let \(\mathbb F_q\) be the finite field, and let \(\mathscr L\) be any collection of \(k\) distinct one-dimensional linear subspaces of \(\mathbb F_q^2\), where \(1\le k\le q+1\). Put \(S=\bigcup_{L\in\mathscr L}L\). With the unitary Fourier transform and counting-measure norms specified below, the sharp spectral-synthesis constant
\[
\mathcal C_4(S)=\sup_{\substack{0\ne f:\mathbb F_q^2\to\mathbb C\\\operatorname{supp}f\subseteq S}}\frac{\|\widehat f\|_{\infty}}{\|\widehat f\|_4}
\]
depends only on \(q\) and \(k\), **not on which projective directions were selected**. If \(2\le k\le q+1\), define
\[
s=\left(\frac{q+1-k}{k-1}\right)^{1/3},\qquad d=k-1+ks,\qquad x=\frac{1+s}{d}.
\]
Then
\[
\boxed{\mathcal C_4(S)=\left(1+(q-1)\frac{s^3}{d^3}\right)^{-1/4}.}
\]
All nonzero extremizers, and no others, are the functions \(f(z)=\lambda\chi(z)h(z)\), where \(\lambda\in\mathbb C\setminus\{0\}\), \(\chi\) is an additive character of \(\mathbb F_q^2\), and
\[
h(0)=1-\frac{k(q-1)x}{q},\qquad
h(z)=\frac{x}{q}\quad (z\in S\setminus\{0\}),\qquad
h(z)=0\quad (z\notin S).
\]
Thus the center-to-arm ratio is exactly \(h(0)/h(z)=k-q/(1+s)\). The central coefficient is negative exactly when \(q>k(1+s)\); for three-line pencils it is positive at \(q=7\) and negative at \(q=8\). For \(k=1\), the sharp constant is \(q^{-1/4}\), with extremizers the modulated indicators of the line. The case \(k=q+1\) is the full plane and the formula gives \(\mathcal C_4(S)=1\), with extremizers the scalar additive characters. For each fixed \(k\ge2\), as prime powers \(q\to\infty\),
\[
\mathcal C_4(S)\sim k^{3/4}q^{-1/4}.
\]

## Assumptions and scope

Choose any nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C\) and write \(z\cdot\xi=z_1\xi_1+z_2\xi_2\). Our transform is \(\widehat f(\xi)=q^{-1}\sum_{z\in\mathbb F_q^2}f(z)\psi(-z\cdot\xi)\). The norms are \(\|\widehat f\|_4^4=\sum_{\xi\in\mathbb F_q^2}|\widehat f(\xi)|^4\), without probability-measure normalization, and \(\|\widehat f\|_\infty=\max_\xi|\widehat f(\xi)|\). There are exactly \(q+1\) projective directions, any two of which intersect only at zero. The theorem concerns fourth-power synthesis, not the opposite \(\ell^2\)-to-\(\ell^4\) extension estimate.

## Proof

**1. Fix a Fourier coefficient and reduce to a strictly convex minimization.** Modulate a candidate so its selected maximal Fourier coefficient occurs at zero and multiply by a nonzero scalar to impose \(F(0)=1\), where \(F(\xi)=\sum_z f(z)\psi(-z\cdot\xi)=q\widehat f(\xi)\). We need to minimize \(\Phi(f)=\sum_\xi|F(\xi)|^4\) subject to \(\operatorname{supp} f\subseteq S\) and \(\sum_z f(z)=1\). The map \(f\mapsto F\) is invertible; the real function \(w\mapsto |w|^4\) is strictly convex on \(\mathbb C\simeq\mathbb R^2\). Therefore \(\Phi\) is strictly convex on the constraint affine space. Coercivity gives existence, and strict convexity gives uniqueness. This unique minimizer yields the exact sharp ratio \(\Phi(f)^{-1/4}\); indeed any frequency can be modulated to zero, and the resulting normalized candidate has \(\Phi\) no smaller than this minimum.

**2. Scalar-line averaging is forced.** Every multiplication map \(z\mapsto tz\), for \(t\in\mathbb F_q^\times\), preserves \(S\), the constraint and \(\Phi\). Uniqueness makes the minimizer invariant. Consequently it has one coefficient \(a\) at zero and a constant \(b_j\) on each of the \(k\) punctured lines. No projective permutation of those directions is assumed. Set \(u_j=qb_j\), \(U=\sum_{j=1}^k u_j\), so that the normalization is \(a+(q-1)U/q=1\).

**3. Obtain an exact Fourier moment with a larger symmetry than the geometric set.** On a dual one-dimensional line \(L_j^\perp\setminus\{0\}\), character orthogonality gives \(F=1-U+u_j\). On each of the other \(q+1-k\) dual directions it gives \(F=1-U\); at the zero frequency, \(F(0)=1\). Thus
\[
\Phi=1+(q-1)\sum_{j=1}^k|1-U+u_j|^4+(q-1)(q+1-k)|1-U|^4.\tag{1}
\]
The exact expression is symmetric under **every permutation of the \(u_j\)**, independently of whether any linear automorphism of the field plane permutes the selected directions. As the restricted problem inherits the unique minimizer, all the \(u_j\) are equal. Complex conjugation also preserves (1) and the affine constraint, hence their common value \(x\) is real. The moment reduces to
\[
\Phi(x)=1+(q-1)\left[k\bigl(1-(k-1)x\bigr)^4+(q+1-k)(1-kx)^4\right].\tag{2}
\]

**4. Optimize the quartic exactly.** For \(2\le k\le q\), strict convexity yields the unique critical point
\[
(k-1)\bigl(1-(k-1)x\bigr)^3+(q+1-k)(1-kx)^3=0.
\]
Writing \(s^3=(q+1-k)/(k-1)\), the unique solution is \(x=(1+s)/(k-1+ks)\). At this point the two nonzero-frequency levels are \(s/d\) and \(-1/d\). Since \(q+1-k=(k-1)s^3\),
\[
k(s/d)^4+(q+1-k)(1/d)^4=s^3/d^3.
\]
Substitution in (2) proves the displayed constant. For \(k=q+1\), the absent exterior-frequency term makes \(x=1/q\), which the same formula obtains with \(s=0\). For \(k=1\), (2) is instead \(q+q(q-1)(1-x)^4\), minimized only at \(x=1\), yielding \(q^{-1/4}\). The explicit \(a\) follows from the normalization. Modulation and nonzero scaling recover every extremizer; the uniqueness established in Step 1 excludes all others.

**5. Sign and asymptotics.** The quotient of center and arm weights is \(q/x-k(q-1)=k-q/(1+s)\), proving the exact sign threshold. For \(k=3\), the threshold reads \(q>3\left(1+((q-2)/2)^{1/3}\right)\); it fails at the prime power seven and holds at eight (the inequality is monotone for real \(q\ge7\)). For fixed \(k\ge2\), \(s^3\sim q/(k-1)\) and \(d\sim ks\), giving \((q-1)s^3/d^3\sim q/k^3\) and the asymptotic claim.

## Verification

The standalone `check_line_pencils.py` independently enumerates the finite Fourier transform using explicit prime and extension-field arithmetic. It checked all direction subsets for small fields and sampled further combinations for larger ones; 3,015 optimizer and random-complex-data assertions passed over field orders \(2,3,4,5,7,8,9,11\). To reproduce, use a standard Python 3 interpreter and run `python check_line_pencils.py` in the directory containing that file. The code is finite supplemental evidence; the all-prime-power assertion is proved by Steps 1–5, not inferred from the numerical trials.

## Relationship to prior work

Iosevich, Li and Yu (2026, arXiv:2609.25404, Theorem 4.1) give an exact synthesis constant and indicator extremizers for affine-*transitive* supports. For a proper union of two or more distinct lines, the shared origin obstructs this transitivity, and the extremizer here generally has a distinct, sometimes negative, central coefficient. Their more general estimates do not present the exact \(k\)-direction classification. Bhowmik, Deodhar and Iosevich (2025, arXiv:2508.12194, Theorem 5) provide an indicator-based synthesis upper bound rather than this exact sharp extremizer solution. Previously derived two-line coordinate-cross constants match the \(k=2\) specialization; the substantive new result is the uniform theorem for **all** pencils and all directions, including the full complex equality classification and center-sign frontier. Published finite-field Fourier restriction/extension calculations involving two or three lines study a different operator or the opposite norm comparison.

## Limitations

No claim is made for unions of nonconcurrent affine lines, higher-dimensional arrangements, exponents other than four, or noise-robust inverse recovery. Equality is classified only for the specified complex-valued supported functions. The independent mathematical audit has not been performed. Exact historical priority remains subject to discovery of an older treatment of the same line-pencil inverse fourth-moment optimization.

## References

- A. Iosevich, Z. Li, and K. Yu, *Spectral synthesis with the complexity parameter in* \(\mathbb Z_N^d\), arXiv:2609.25404, first posted 2026-09-21, https://arxiv.org/html/2609.25404. Section 4, especially Theorem 4.1.
- P. Bhowmik, S. Deodhar, and A. Iosevich, *On spectral synthesis in* \(\mathbb Z_N^d\), arXiv:2508.12194, first posted 2025-08-17, https://arxiv.org/html/2508.12194v2. Theorem 5.
