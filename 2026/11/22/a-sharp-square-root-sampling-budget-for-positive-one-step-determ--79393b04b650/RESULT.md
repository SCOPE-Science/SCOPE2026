# A sharp square-root sampling budget for positive one-step deterministically sketched Ritz values

## Finding

For the rank-one SPD family below, the sharp lower and upper endpoints (infimum and supremum) of the one-step deterministically sketched Rayleigh–Ritz (dsRR) scalar at condition number \(K>1\) are
\[
 \theta_{\inf,\sup}=\frac{K+1}{2}\mp\frac{K-1}{2}\sqrt{1+\frac{(n-s)^2}{s^2(n-1)}}.
\]
This holds for every full-rank, unweighted coordinate sketch with \(s\) distinct rows, \(2\le s\le n\), in dimension \(n\ge3\). For \(s<n\) both endpoints are attained by nondegenerate Krylov starts; for \(s=n\) the attainable interval is \((1,K)\). Strict positivity for every nondegenerate member holds exactly when
\[
 s>\frac{n}{1+2\sqrt{K(n-1)}/(K-1)}.
\]
Equality admits zero and a row count strictly below this threshold admits a negative value. At fixed \(K\), the smallest uniformly sign-safe integer count is asymptotic to \((K-1)\sqrt n/(2\sqrt K)\); at fixed \(s\), the lowest scalar behaves as \(-(K-1)\sqrt n/(2s)+O(1)\).

For \(K=2,s=2\), the first negative dimension is \(35\) **in this family**; a rational matrix example there gives \(-3/4898\). The dimension-\(37\) rational example gives \(-1/24\) and, unlike the dimension-\(35\) example, attains its dimension's sharp lower endpoint. A third row makes the scalar positive for every nondegenerate member with \(n=37,K=2\).

## Assumptions and scope

The claim is in real exact arithmetic. Put
\[
 v=\frac{\mathbf1}{\sqrt n},\qquad
 w=\frac{(-(n-1),1,\ldots,1)^{\mathsf T}}{\sqrt{n(n-1)}},\quad
 u_\phi=\cos\phi\,v+\sin\phi\,w,\quad
 A_\phi=I+(K-1)u_\phi u_\phi^{\mathsf T}.
\]
Here \(\sin\phi\cos\phi\ne0\), \(b=v\), and the two-vector basis used for sampling is \(V_2=[v,w]\). Only the first vector is retained in the projection. The selector \(S\) extracts \(s\) distinct coordinate rows and satisfies \(\operatorname{rank}(SV_2)=2\). The scalar is
\[
 \theta(S,\phi)=\frac{(Sv)^{\mathsf T}(SA_\phi v)}{\|Sv\|_2^2}.
\]
This normalization is unchanged by scaling the start vector or by applying a common nonzero scalar factor to the coordinate selector. Q-DEIM initializes the row set by pivoted QR on \(V_2^{\mathsf T}\); oversampling may append distinct rows. The result is uniform over all full-rank selectors of the indicated size in this family, not over general SPD inputs or weighted selectors.

## Proof

**1. Positive spectrum and genuine Krylov space.** The vectors \(v,w\) are orthonormal, so \(u_\phi\) is a unit vector and the eigenvalues of \(A_\phi\) are \(K\) once and \(1\) with multiplicity \(n-1\). Moreover,
\[
 A_\phi v=\bigl[1+(K-1)\cos^2\phi\bigr]v
 +(K-1)\sin\phi\cos\phi\,w.
\]
The last coefficient is nonzero, proving \(\mathcal K_2(A_\phi,v)=\operatorname{span}\{v,w\}\).

**2. Forced exceptional row.** Rows \(2,\ldots,n\) of \(V_2\) are identical, and the first row and a single ordinary row are linearly independent. Hence every full-rank sample includes row 1 and \(s-1\) arbitrary ordinary rows. Row 1 has squared norm 1; each ordinary row has squared norm \(1/(n-1)\). Q-DEIM selects row 1 in the first pivot, and any ordinary row in the second. A change of orthonormal basis of the same space preserves row lengths and projection residuals of the pivot procedure. Choice of ordinary rows and ordering of a full-rank sample do not affect the scalar.

**3. Exact endpoints.** For every admissible sample the quotient of cross term and squared norm is
\[
 \frac{(Sv)^{\mathsf T}(Sw)}{\|Sv\|_2^2}
 =\frac{\sqrt n}{s}\sum_{j\text{ sampled}}w_j
 =-\frac{n-s}{s\sqrt{n-1}}=:-d.
\]
Substituting Step 1 gives
\[
 \theta=1+(K-1)(\cos^2\phi-d\sin\phi\cos\phi)
 =\frac{K+1}{2}+\frac{K-1}{2}(\cos2\phi-d\sin2\phi).
\]
The last trigonometric expression in parentheses takes values between \(-\sqrt{1+d^2}\) and \(\sqrt{1+d^2}\). If \(d>0\), its extremizers have \(\sin2\phi\ne0\), so the displayed sharp endpoints are attained. When \(d=0\), the quotient is \(1+(K-1)\cos^2\phi\) and nondegeneracy excludes \(1,K\), although both can be approached.

**4. Sign-safe budget.** Positivity of the lower endpoint is equivalent to \(\sqrt{1+d^2}<(K+1)/(K-1)\), hence to \(d<2\sqrt K/(K-1)\). Solving for \(s\) gives the asserted inequality. Any equality or strict failure has \(s<n\), so its nonpositive lower endpoint is attained. The sharp integer count is
\[
 s_{\min}=\max\left\{2,\left\lfloor\frac{n}{1+2\sqrt{K(n-1)}/(K-1)}\right\rfloor+1\right\}.
\]
Dividing the threshold by \(\sqrt n\) gives its stated asymptotic, and at fixed \(s\), \(d=\sqrt n/s+O(n^{-1/2})\) gives the asymptotic lower endpoint.

**5. Exact examples.** For \(K=2,s=2\), negativity is equivalent to \((n-2)^2>32(n-1)\), or \(n^2-36n+36>0\). Since the roots are \(18\pm12\sqrt2\), the first permissible integer \(n\ge3\) with negativity is \(35\).

At \(n=35\) let \(z=(-35,6,\ldots,6)^{\mathsf T}\) and \(A=I+zz^{\mathsf T}/2449\). The squared norm of \(z\) is \(2449\) and its sum is \(169\); \(z\) belongs to \(\operatorname{span}\{v,w\}\) and its projections onto both axes are nonzero (its sum is nonzero and its entries are not constant). Thus this is a nondegenerate family member. The exceptional and ordinary row sums are \(-3466/2449\) and \(3463/2449\), respectively, and their average is the two-row scalar \(-3/4898\). This is a rational failure witness at the first negative dimension, not an attaining lower-endpoint example.

At \(n=37\) let \(t=(-6,1,\ldots,1)^{\mathsf T}\) and \(A=I+tt^{\mathsf T}/72\). The norm square of \(t\) is 72, and the same projection argument applies. The exceptional and ordinary row sums are \(-3/2\) and \(17/12\). Their mean gives the Q-DEIM scalar \(-1/24\), whereas the mean of all row sums, the ordinary Rayleigh quotient, is \(99/74\). Here \(d=35/12\) and \(\sqrt{1+d^2}=37/12\), so the negative scalar attains the lower endpoint. At \(s=3\), \(d=34/18<2\sqrt2\), which protects the whole dimension-37 condition-two family, and the same example yields \(4/9\).

## Verification

The exact identities in the proof establish the all-parameter conclusions. The supplied `verify.py` can separately check the rational dimension-37 example and compare finite QR and quotient computations with the formulas. The dimension-35 example is verified by the exact arithmetic in Step 5, not by that script. Finite checks are not substitutes for the proof.

## Relationship to prior work

Bergermann [1] defines dsRR with a sketch-building stage that uses the next Krylov vector, and Q-DEIM [2] defines the pivoted-QR initialization. Sketch-induced spectral pollution is already known [3]. The earlier sharp one-vector envelope in terms of subspace-embedding distortion [4] applies to the same scalar but allows arbitrary admissible sketch metrics and start directions. It does not classify row counts for this family: the rescaled embedding bound uses only the two extremal eigenvalues of the sampled Gram matrix, whereas the present scalar depends on the fixed start direction relative to their eigenspaces. The exact row budget uses the forced sample pattern and the attainable directional envelope. Prior coordinate sketches with two retained vectors and nonreal Ritz values [5], row selection distortion gaps [6], and one-step GMRES residual failures [7] concern different targets. The contribution is the exact row-count classification for this algorithm-compatible family, not the qualitative possibility of a negative sketched Ritz value or an assertion of historical priority.

## Limitations

The thresholds apply only to this structured rank-one family with one retained Krylov vector, a nondegenerate two-vector space for selecting distinct unweighted rows, and exact arithmetic. They do not establish a general sign-safe budget for all SPD problems, finite-precision behavior, a convergence rate, or a runtime advantage.

## References

1. K. Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158v2, Eq. (2.18), Algorithms 4.2 and 5.3. https://arxiv.org/abs/2604.07158
2. Z. Drmač and S. Gugercin, *A New Selection Operator for the Discrete Empirical Interpolation Method*, arXiv:1505.00370. https://arxiv.org/abs/1505.00370
3. Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113, §6.8. https://arxiv.org/abs/2111.00113
4. *Sharp one-vector sketching envelope and positive-stability threshold for symmetric systems*, Resultary record 64c030573be9 (2026-10-26).
5. *Optimal two-row sketches can produce nonreal Ritz values for condition-two SPD systems*, Resultary record 15c0a9d20140 (2026-10-25).
6. *Unbounded distortion gap for minimum-singular-value row selection on well-conditioned Krylov spaces*, Resultary record f48cbf6a3e92 (2026-11-08).
7. *Sharp coordinate-sampling threshold and unbounded one-step sketched GMRES residual on near-identity SPD systems*, Resultary record 46affa6189d7 (2026-11-02).
