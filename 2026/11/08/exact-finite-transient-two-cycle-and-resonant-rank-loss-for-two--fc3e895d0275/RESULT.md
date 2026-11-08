# Exact finite-transient two-cycle and resonant rank loss for two-row PolarGrad

## Finding

Consider the nuclear-norm-scaled polar gradient update on the isotropic two-row matrix quadratic. At **every fixed normalized step \(0<\alpha<2\), \(\alpha\ne1\)**, its full-rank dynamics admit an exact, exceptional-set classification.

Let \(c=|1-\alpha|\in(0,1)\), and for the two positive singular values \(s_1\ge s_2>0\) of a nonzero full-row-rank initial error, put
\[
r_0=\frac{s_1-s_2}{s_1+s_2}\in[0,1).
\]
If \(r_0=0\), the entire trajectory is \(E_t=(1-\alpha)^tE_0\). If \(r_0=c^k\) for an integer \(k\ge1\), the rank drops from two to one **exactly at iteration \(k\)**, and then
\[
E_{k+j}=(1-\alpha/2)^jE_k,\qquad j\ge0.
\]
For every other full-row-rank initial error, set
\[
x=\frac{\log r_0}{\log c}>0,\qquad m=\lfloor x\rfloor.
\]
After precisely \(m\) initial updates, the singular-value contrast enters \(r_m\in(c,1)\), where it obeys an exact two-cycle:
\[
r_{m+1}=\frac{c}{r_m},\qquad r_{m+2}=r_m,\qquad
E_{m+2}=(1-\alpha)E_m,
\]
and these relations repeat thereafter. Thus **generic errors become exact scalar two-step orbits in finitely many iterations**, while the countable set of contrast values \(c,c^2,c^3,\ldots\) gives finite-time rank loss and a different subsequent linear rate. This holds for every column count \(n\ge2\), arbitrary singular vectors, and every real matrix \(E_0\) of row rank two.

## Assumptions and scope

Let \(n\ge2\), \(X_\star\in\mathbb R^{2\times n}\), and \(f(X)=\frac12\|X-X_\star\|_{\mathrm F}^2\). Write \(E_t=X_t-X_\star\). For \(E=U\operatorname{diag}(s_1,\dots,s_r)V^\top\) its thin singular value decomposition, set
\[
\Phi(E)=\|E\|_*\operatorname{polar}(E)
=\left(\sum_{j=1}^{r}s_j\right)UV^\top,\qquad
\Phi(0)=0.
\]
The exact iteration is
\[
E_{t+1}=E_t-\frac{\alpha}{2}\Phi(E_t),
\quad 0<\alpha<2,\quad\alpha\ne1.
\]
The factor \(1/2\) normalizes the Hessian trace \(\operatorname{tr}(I_2)=2\). For any rank-one error, \(\Phi(E)=E\), so the rank-one formula above applies immediately with \(k=0\). Rank-zero errors remain zero.

The classification assumes exact arithmetic, in which rank is unambiguous. When \(r_0\) is a power of \(c\), the rank collapse is an exact equality, not a numerical-small-singular-value event.

## Proof

**Step 1: reduce to singular values without restricting singular vectors.**
Let the full-row-rank error have SVD \(E=U\operatorname{diag}(s_1,s_2)V^\top\) with \(s_1\ge s_2>0\); the two columns of \(U\) and \(V\) are orthonormal. Its update has the *same* singular vector factors before the signs of its two diagonal coefficients are absorbed:
\[
E^+
=U\operatorname{diag}(s_1-\alpha\bar s,\ s_2-\alpha\bar s)V^\top,\qquad
\bar s=\frac{s_1+s_2}{2}.
\]
Write \(s_1=\bar s(1+r)\), \(s_2=\bar s(1-r)\), \(0\le r<1\). The two signed coefficients become
\[
\bar s(1-\alpha+r),\qquad
\bar s(1-\alpha-r).
\]
Their *absolute values* are the new singular values.

**Step 2: the exact contrast map.**
Set \(c=|1-\alpha|\). If \(0<r<c\), the two coefficients have the same sign, the new singular-value mean is \(c\bar s\), and their contrast is \(r/c\). If \(c<r<1\), they have opposite signs, the new mean is \(r\bar s\), and their contrast is \(c/r\). If \(r=c\), one coefficient vanishes and the updated error has rank one. Therefore, while full row rank persists,
\[
T_c(r)=
\begin{cases}
r/c,&0<r<c,\\
c/r,&c<r<1,
\end{cases}
\]
and the *only* rank-loss threshold is \(r=c\). At \(r=0\), both singular values are equal, \(\Phi(E)=2E\), and \(E^+=(1-\alpha)E\), preserving equality.

**Step 3: finite entry or exact rank loss.**
For \(0<r_0<1\), write \(r_0=c^x\) with \(x=\log r_0/\log c>0\). Whenever \(x>1\) the first branch applies and replaces \(x\) by \(x-1\). If \(x=k\) is an integer, after \(k-1\) such steps \(r=c\), and the next step has rank one: the first rank drop occurs at iteration \(k\). Since a rank-one matrix has \(\Phi(E)=E\), every later step is \(E^+=(1-\alpha/2)E\), preserving rank one because \(0<1-\alpha/2<1\).

If \(x\notin\mathbb Z\), after \(m=\lfloor x\rfloor\) subtractions the new exponent is \(u=x-m\in(0,1)\), hence \(r_m=c^u\in(c,1)\). On this interval \(T_c(r)=c/r\), which maps \((c,1)\) into itself and is an involution. This gives an exact two-cycle of contrasts, with no rank loss.

**Step 4: exact matrix, not just singular-value, two-step scaling.**
For \(c<r<1\), the two signed coefficients from Step 1 have opposite signs. After the first update their absolute values have mean \(r\bar s\). The second step subtracts \(\alpha r\bar s\) times the polar factor of \(E^+\), respecting those two opposite signs. Substituting the signed entries separately gives
\[
E^{++}=
\begin{cases}
c\,E,&0<\alpha<1,\\
-c\,E,&1<\alpha<2.
\end{cases}
=(1-\alpha)E.
\]
This identity is independent of the original left and right singular vectors; it holds in the original matrix coordinates because the two steps preserve their singular directions up to signs. Repeating the argument yields \(E_{t+2}=(1-\alpha)E_t\) for all \(t\ge m\). Consequently
\[
f(X_{t+2})=c^2 f(X_t)\qquad(t\ge m).
\]
The rank-one, rank-zero, equal-singular and resonant cases complete the classification.

## Verification

For \(\alpha=7/10\) (so \(c=3/10\)), a full-rank diagonal start with singular values \(3/2,1/2\) has contrast \(1/2\in(c,1)\) and obeys \(E_2=(3/10)E_0\). For \(\alpha=13/10\), the same start instead obeys \(E_2=-(3/10)E_0\). These are identities in exact rational arithmetic.

For the resonant start \(E_0=\operatorname{diag}(109/100,91/100)\) and \(\alpha=7/10\), the contrast equals \(9/100=c^2\), so the first update preserves full rank and the second has rank exactly one. The standalone `checker.py` reproduces these and other rational examples, compares the exact contrast recursion with direct polar-SVD updates over deterministic numerical cases, and checks the post-entry two-step identity. Finite checks support implementation correctness but do not prove the arbitrary-dimension or infinite-iteration statements.

## Relationship to prior work

Shulgin, Laing, Orvieto and Richtárik, *A Quadratic Lens on Muon's Polar Update* (2026), derive the full-row-rank covariance-root recursion (Appendix I), its fixed dual-adapted-step counterpart, and exact **line-search** two-row spectral flattening and post-collapse behavior (Proposition 18 and Corollary 6). They also give a commuting-case singular-value formula for general normalized steps. The **line-search/normalized-step \(\alpha=1\)** collapse is their prior theorem and is **excluded** here. The present classification treats every distinct fixed parameter \(0<\alpha<2,\alpha\ne1\) in the isotropic two-row case: finite entry into a two-step scalar orbit, exact exceptional powers causing rank loss, and explicit different rates after rank loss. Their general root recurrence is a starting point, but their paper does not state this complete off-line-search dynamical phase classification.

Jawanpuria, Garai and Mishra (2026) establish uniform convergence for nuclear-scaled polar descent over \(0<\alpha<2\) and exhibit invariant rank-one directions; their results do not determine this singular-ratio return map, finite transient, or resonant rank-loss set. Lau, Long and Su (2025) introduce PolarGrad and its nuclear-norm scaling.

## Limitations

The setting is an exact-polar, deterministic, isotropic matrix quadratic with exactly two rows and \(n\ge2\), at normalized fixed steps strictly between zero and two and different from one. It does not assert the same classification for anisotropic Hessians, larger row counts, approximate polar maps, momentum, stochastic updates, or floating-point rank detection. The exceptional rank-loss condition is exact and can be numerically unstable under perturbations. The full-rank two-step scaling and subsequent rank-one rate are analytic; independent mathematical validation remains unperformed, and unindexed priority cannot be ruled out.

## References

1. E. Shulgin, S. Laing, A. Orvieto, and P. Richtárik, *A Quadratic Lens on Muon's Polar Update: Benefits, Pitfalls, and the Role of Newton–Schulz*, arXiv:2610.30280v1 (first public 2026-10-21). https://arxiv.org/html/2610.30280v1
2. P. Jawanpuria, B. Garai, and B. Mishra, *Constant Step Sizes for Muon-Type Spectral Optimizers on Strongly Convex Quadratics*, arXiv:2610.27747v1 (first public 2026-10-20). https://arxiv.org/html/2610.27747v1
3. T. T.-K. Lau, Q. Long, and W. Su, *PolarGrad: A Class of Matrix-Gradient Optimizers from a Unifying Preconditioning Perspective*, arXiv:2505.21799 (first public 2025-05-27). https://arxiv.org/abs/2505.21799
