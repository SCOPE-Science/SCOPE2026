# A sharp square-root sampling budget for positive one-step deterministically sketched Ritz values

## Finding

A symmetric positive-definite matrix of condition number exactly \(K>1\) can produce a **negative** one-step deterministically sketched Rayleigh–Ritz (dsRR) eigenvalue even when Q-DEIM selects a full-rank sketch of the genuine two-dimensional Krylov space. On a natural permutation-symmetric rank-one family, the exact smallest and largest sketched Ritz values are

\[
\boxed{\quad \theta_{\min,\max}=\frac{K+1}{2}\mp\frac{K-1}{2}\sqrt{1+\frac{(n-s)^2}{s^2(n-1)}}\quad}
\]

for \(n\ge3\), \(2\le s\le n\), and every full-rank \(s\)-row coordinate selector on that space. When \(s<n\), both bounds are attained by a nondegenerate Krylov start. The minimum remains strictly positive for **every** nondegenerate member of the family if and only if

\[
\boxed{\quad s>\frac{n}{1+2\sqrt{K(n-1)}/(K-1)}.\quad}
\]

Equality in this strict inequality allows a zero Ritz value, and smaller budgets allow a negative value. For fixed \(K>1\), the first uniformly sign-safe integer row budget in this family is asymptotic to \(\frac{K-1}{2\sqrt K}\sqrt n\); any fixed row count permits a negative Ritz value diverging in magnitude like \(\frac{K-1}{2s}\sqrt n\).

For \(K=2\) and the minimally permitted \(s=2\), dimension \(n=35\) is the **first** dimension permitting a negative Ritz value. At \(n=37\), an exactly rational matrix with spectrum \(\{1,2\}\) yields the sharp Q-DEIM-selected scalar \(\theta=-1/24\), although its ordinary Rayleigh quotient is \(99/74\). Adding a third sampled row eliminates negative Ritz values for every member of this \(n=37,K=2\) family.

## Assumptions and scope

All statements concern real exact arithmetic, unweighted sampling of distinct coordinate rows, one retained trial vector, and row selection based on **both** Krylov vectors as in the one-step case of dsRR. Let \(n\ge3\), \(K>1\), and let \(\mathbf1\in\mathbb R^n\) denote the all-ones vector. Define two orthonormal vectors

\[
v=\frac{\mathbf1}{\sqrt n},\qquad
w=\frac{(-(n-1),1,\ldots,1)^\mathsf T}{\sqrt{n(n-1)}}.
\]

For an angle \(\phi\) with \(\sin\phi\cos\phi\ne0\), put

\[
u_\phi=\cos\phi\,v+\sin\phi\,w,\qquad
A_\phi=I_n+(K-1)u_\phi u_\phi^\mathsf T.
\]

The matrix \(A_\phi\) is SPD with eigenvalues \(K\) once and \(1\) with multiplicity \(n-1\), and the starting vector is \(b=v\). Its genuine two-step Krylov space is \(\mathcal K_2(A_\phi,v)=\operatorname{span}\{v,w\}\). Form the basis \(V_2=[v,w]\). A selector \(S\in\mathbb R^{s\times n}\) extracts \(s\) distinct standard-coordinate rows with \(2\le s\le n\), and is required to satisfy \(\operatorname{rank}(SV_2)=2\). The one-step dsRR scalar, equivalently the exact one-vector whitened sketched Rayleigh quotient, is

\[
\theta(S,\phi)=\frac{(Sv)^\mathsf T(SA_\phi v)}{\|Sv\|_2^2}.
\]

Q-DEIM initializes a full-rank two-row selector using pivoted QR on \(V_2^\mathsf T\); an oversampling procedure may add other distinct rows. The theorem applies to **every** full-rank selector of the displayed size, so it includes any such extension of that initialization. It does not assert a universal guarantee over arbitrary SPD matrices or a particular oversampling heuristic's efficacy outside this family.

## Proof

**1. Spectrum and exact Krylov space.** Since \(v\perp w\) and both have norm one, \(u_\phi\) is unit. The rank-one update \(A_\phi\) has spectrum \(\{1,K\}\), hence its condition number is \(K\). Direct multiplication gives

\[
A_\phi v=[1+(K-1)\cos^2\phi]v+(K-1)\sin\phi\cos\phi\,w.
\]

The assumed nonzero product makes \(v,A_\phi v\) linearly independent, proving the asserted two-dimensional Krylov space and its basis.

**2. Row selection and Q-DEIM.** All ordinary rows \(j=2,\ldots,n\) of \(V_2\) are the same, while row \(1\) is different. Thus omitting row \(1\) makes \(SV_2\) rank at most one. Every full-rank selector must contain that exceptional row and \(s-1\) arbitrary ordinary rows. Conversely each such selector has rank two. The squared row norm of \(V_2\) is \(1\) at row \(1\) and \(1/(n-1)\) at any other row. Pivoted QR on \(V_2^\mathsf T\) therefore selects row \(1\) first and necessarily an ordinary row second. All admissible \(s\)-row selectors give the **same** scalar, so no tie breaking or choice of remaining rows affects the answer.

**3. Exact scalar.** Since all sampled entries of \(v\) equal \(1/\sqrt n\),

\[
\frac{(Sv)^\mathsf T(Sw)}{\|Sv\|_2^2}
=\frac{\sqrt n}{s}\sum_{j\in S}w_j
=-\frac{n-s}{s\sqrt{n-1}}=:-d_{n,s}.
\]

Substitution of Step 1 into the sketched quotient yields

\[
\theta(S,\phi)=1+(K-1)(\cos^2\phi-d_{n,s}\sin\phi\cos\phi)
=\frac{K+1}{2}+\frac{K-1}{2}(\cos2\phi-d_{n,s}\sin2\phi).
\]

The final sinusoid has exact range \([ -\sqrt{1+d_{n,s}^2},\sqrt{1+d_{n,s}^2}]\), proving both sharp endpoints. For \(s<n\), \(d_{n,s}>0\), so extremizing angles satisfy the nondegeneracy condition. For \(s=n\), the endpoints \(1,K\) are only limits as the Krylov start approaches an eigenvector; for all allowed nondegenerate starts the quotient lies strictly between them.

**4. Necessary and sufficient positivity budget.** The smallest scalar is strictly positive exactly when

\[
\sqrt{1+d_{n,s}^2}<\frac{K+1}{K-1}
\iff d_{n,s}<\frac{2\sqrt K}{K-1}
\iff s>\frac{n}{1+2\sqrt{K(n-1)}/(K-1)}.
\]

At equality the attained lower endpoint is zero, and if the inequality fails strictly its attained lower endpoint is negative. Thus the sharp *integer* budget protecting every nondegenerate member is

\[
s_{\min}(n,K)=\max\left\{2,\left\lfloor\frac{n}{1+2\sqrt{K(n-1)}/(K-1)}\right\rfloor+1\right\}.
\]

The asymptotic row budget follows by dividing the threshold by \(\sqrt n\) at fixed \(K\). At fixed \(s\), \(d_{n,s}\sim\sqrt n/s\), whence \(\theta_{\min}=-(K-1)\sqrt n/(2s)+O(1)\).

**5. First negative dimension and exact attaining rational witness.** At \(K=2,s=2\), negativity occurs precisely when \((n-2)^2>32(n-1)\), equivalent to \(n^2-36n+36>0\). This fails for integers \(3\le n\le34\) and holds from \(n=35\) onward. At \(n=37\), set

\[
t=(-6,1,\ldots,1)^\mathsf T\in\mathbb Z^{37},\quad
A=I_{37}+\frac{tt^\mathsf T}{72},\quad b=\frac{\mathbf1}{\sqrt{37}}.
\]

Then \(\|t\|_2^2=72\), so \(A\) has the stated eigenvalues. The first row sum of \(A\) is \(-3/2\); each of the other 36 row sums is \(17/12\). Q-DEIM on the exact two-vector Krylov space selects row 1 and any other row; its one-step dsRR scalar is the mean of these two sums,

\[
\theta=\tfrac12(-\tfrac32+\tfrac{17}{12})=-\tfrac1{24}.
\]

The all-coordinate Rayleigh quotient is \(37^{-1}(-3/2+36\cdot17/12)=99/74\). Here \(d_{37,2}=35/12\) and \(\sqrt{1+d_{37,2}^2}=37/12\); hence the attained scalar equals the sharp lower bound \((3-37/12)/2=-1/24\). For three rows the family-wide positivity threshold is satisfied, and the displayed fixed matrix gives \(\theta=4/9\). Every identity above is exact.

## Verification

Run the embedded standalone `verify.py` with Python 3, NumPy and SciPy. It independently evaluates 37-dimensional exact-rational row sums and sketched quotients; runs pivoted QR of the actual two-column Krylov basis at nine dimensions; and constructs the rank-one SPD examples at numerous sizes, contrasts, sketch counts and angles, comparing the computed scalar with the analytic formula and its extrema. The script completed `VERIFY_OK 2596` (2,596 assertions). Finite tests corroborate the formulas; the all-dimension and all-parameter conclusions follow solely from the proof above.

## Relationship to prior work

Bergermann [1], Sections 4–5 and Algorithm 6, defines dsRR, its two-vector sketch-building stage, Q-DEIM/DEIM initialization, and the prescribed options for oversampling. Drmač and Gugercin [2] introduce the pivoted-QR selection mechanism. Nakatsukasa and Tropp [3] show that sketching can spoil symmetric Ritz spectral behavior; spurious Ritz values are **not** a new qualitative observation.

The published study *Sharp one-vector sketching envelope and positive-stability threshold for symmetric systems* [4] already establishes a universal extremal scalar interval in terms of **given subspace-embedding distortion**. That earlier general inequality is consistent with the present result and provides relevant machinery, but it does not specify the Q-DEIM-constrained row sets or imply this exact dimension-dependent row budget without the new construction and row analysis. The published result *Optimal two-row sketches can produce nonreal Ritz values for condition-two SPD systems* [5] concerns two **retained** Krylov vectors and a nonreal eigenvalue pair; the present result retains one vector, samples the second for pivoting, and quantifies oversampling to protect positivity. The published row-selection distortion separation [6] concerns a distinct condition-number objective, and the coordinate-sampled GMRES residual threshold [7] concerns least-squares residuals rather than a sketched Ritz eigenvalue. These precise prior claims are acknowledged, not retested or amended.

The new assessed claim is the **entire explicit Q-DEIM-compatible rank-one family** with its exact sharp Ritz range, necessary-and-sufficient within-family sign-safe sketch size, and minimal-dimension rational failure witness. It is not a new general warning that nonnormal projections might yield spurious spectral values. The literature comparison cannot certify exhaustive historical priority.

## Limitations

All sharp thresholds are specific to the stated structured rank-one SPD family and distinct, **unweighted** coordinate selectors. Although all full-rank row subsets in this family are covered, the positivity budget is not a universal sufficient condition for arbitrary matrices, Krylov directions, sketch matrices, or higher retained Krylov dimension. No finite-precision behavior, approximate eigenvector convergence, numerical cost advantage, or behavior of similarity-restored variants is claimed. The preceding literature may contain equivalent specialized examples not indexed by the searches. Independent validation has not been performed.

## References

1. K. Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158v1 (first publicly posted 2026-04-08), especially §§4–5 and Algorithm 6; https://arxiv.org/abs/2604.07158 ; https://arxiv.org/html/2604.07158v2 .
2. Z. Drmač and S. Gugercin, *A New Selection Operator for the Discrete Empirical Interpolation Method*, arXiv:1505.00370 (2015); https://arxiv.org/abs/1505.00370 .
3. Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113 (first posted 2021-10-29), §6.8; https://arxiv.org/abs/2111.00113 .
4. *Sharp one-vector sketching envelope and positive-stability threshold for symmetric systems*, mathematical result dated 2026-10-26; https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-one-vector-sketching-envelope-and-positive-stability-thres--64c030573be9 .
5. *Optimal two-row sketches can produce nonreal Ritz values for condition-two SPD systems*, mathematical result dated 2026-10-25; https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-optimal-two-row-sketches-can-produce-nonreal-ritz-values-for-con--15c0a9d20140 .
6. *Unbounded distortion gap for minimum-singular-value row selection on well-conditioned Krylov spaces*, mathematical result dated 2026-11-08; https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-unbounded-distortion-gap-for-minimum-singular-value-row-selectio--f48cbf6a3e92 .
7. *Sharp coordinate-sampling threshold and unbounded one-step sketched GMRES residual on near-identity SPD systems*, mathematical result dated 2026-11-02; https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-coordinate-sampling-threshold-and-unbounded-one-step-sketc--46affa6189d7 .
