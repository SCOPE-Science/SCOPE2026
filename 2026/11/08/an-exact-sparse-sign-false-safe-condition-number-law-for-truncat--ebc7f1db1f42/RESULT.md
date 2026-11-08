# An exact sparse-sign false-safe condition-number law for truncated Arnoldi

## Finding

Fix integers \(s\ge\zeta\ge2\) and \(N\ge\max\{s+1,5\}\). Draw \(S\in\mathbb R^{s\times N}\) with independent columns, each uniformly supported on exactly \(\zeta\) of the \(s\) rows and carrying independent signs \(\pm1/\sqrt{\zeta}\) there. Put \(M=2^\zeta\binom{s}{\zeta}\). For a real threshold \(\tau\ge\sqrt{2\zeta-1}\) and a parameter

\[
0<\varepsilon<\min\Bigl\{\tfrac1{10},\frac{\sqrt{2/\zeta}}{\tau+1}\Bigr\},
\]

there is a symmetric positive-definite matrix \(A_\varepsilon\), approaching the identity in operator norm, whose first two normalized, unorthogonalized Krylov vectors form \(B_\varepsilon\) and satisfy the two simultaneous exact laws

\[
\kappa_2(B_\varepsilon)=\frac{\sqrt{4+\varepsilon^2}}{\varepsilon},
\qquad
\Pr\bigl(\kappa_2(SB_\varepsilon)\le\tau\bigr)
=\frac{M-2}{M^2}>0.
\]

Every accepted sketch has condition number at most \(\sqrt{2\zeta-1}\), even though \(\kappa_2(B_\varepsilon)\to\infty\). For \(s=\zeta=8\), the exact false-safe probability is \(127/32768\), while for \(s=30,\zeta=8\) it is \((1498348800-2)/(1498348800)^2\), approximately \(6.6740\times10^{-10}\). The latter probability is extremely small, not a statement that ordinary experiments frequently fail.

## Assumptions and scope

All algebra is real and exact. A rank-deficient rectangular matrix has spectral condition number \(+\infty\). The result concerns the **condition-number screening statistic** for the first two \(t=0\) normalized truncated-Arnoldi vectors, before any final rank-one correction; it does not assert a failure of a complete restarted matrix-function approximation.

For \(j\le N\), let \(e_j\) be the standard coordinate vector and define

\[
u=e_1-e_2,\quad
b_1=\frac{u+\varepsilon e_3}{\sqrt{2+\varepsilon^2}},\qquad
b_2=\frac{u+\varepsilon e_4}{\sqrt{2+\varepsilon^2}},\qquad
B_\varepsilon=[b_1\ b_2].
\]

The two basis vectors are unit vectors with common inner product \(c=2/(2+\varepsilon^2)\). Define \(\sigma=\sqrt{1-c^2}\), \(q_1=b_1\), \(q_2=(b_2-cb_1)/\sigma\), \(q_3=e_5\), and \(\delta=\varepsilon^2/10\). The three \(q_j\) are orthonormal. Construct

\[
\begin{aligned}
A_\varepsilon={}&I+(c-1)q_1q_1^\mathsf T
+\sigma(q_1q_2^\mathsf T+q_2q_1^\mathsf T)\\
&+(c^{-1}-1)q_2q_2^\mathsf T
+\delta(q_2q_3^\mathsf T+q_3q_2^\mathsf T).
\end{aligned}
\]

The sketch is chosen independently of \(A_\varepsilon\) and \(b_1\). The source algorithm's practical sparsity \(\zeta=8\) and its adaptive threshold \(10^6\) are possible parameter choices, but the theorem addresses this two-column screening event rather than all adaptive-loop or restarting decisions.

## Proof

**Step 1: the two columns are a genuine Krylov prefix of a nearly identity positive-definite matrix.** The Gram matrix of \(B_\varepsilon\) is \(\left(\begin{smallmatrix}1&c\\c&1\end{smallmatrix}\right)\), so its singular values are \(\sqrt{1\pm c}\), giving
\[
\kappa_2(B_\varepsilon)=\sqrt{\frac{1+c}{1-c}}=\frac{\sqrt{4+\varepsilon^2}}{\varepsilon}.
\]
Direct multiplication shows \(A_\varepsilon b_1=cq_1+\sigma q_2=b_2\). Thus, with zero truncated-orthogonalization parameter, normalized multiplication by \(A_\varepsilon\) produces exactly \(b_2\) from \(b_1\). Also \(A_\varepsilon b_2\) has nonzero \(q_3\)-coefficient \(\sigma\delta\), making the first three Krylov vectors linearly independent. Since \(\sigma\le\varepsilon\), \(|c-1|\le\varepsilon^2/2\) and \(c^{-1}-1=\varepsilon^2/2\),
\[
\|A_\varepsilon-I\|_2\le |c-1|+\sigma+(c^{-1}-1)+\delta
\le\varepsilon+\tfrac{11}{10}\varepsilon^2<1.
\]
The symmetric \(A_\varepsilon\) is therefore positive definite, and tends to \(I\) in norm.

**Step 2: isolate the shared-direction sketch collision.** Denote the first four independent columns of \(S\) by \(s_1,s_2,s_3,s_4\); each has Euclidean norm one and is uniform over \(M\) distinct signed-support vectors. Put \(v=s_1-s_2\). Then
\[
SB_\varepsilon=(2+\varepsilon^2)^{-1/2}
[\,v+\varepsilon s_3\quad v+\varepsilon s_4\,].
\]
Two distinct signed-support vectors obey \(\|s_1-s_2\|_2\ge\sqrt{2/\zeta}\): a support change creates at least two differing coordinates, while a sign change on fixed support creates a larger squared difference. With \(v\ne0\), test the matrix on the unit coefficient vectors \((1,1)/\sqrt2\) and \((1,-1)/\sqrt2\). The largest singular value is at least \(\sqrt{2/(2+\varepsilon^2)}(\|v\|_2-\varepsilon)\), and the smallest is at most \(\sqrt{2/(2+\varepsilon^2)}\varepsilon\); hence
\[
\kappa_2(SB_\varepsilon)\ge
\frac{\sqrt{2/\zeta}-\varepsilon}{\varepsilon}>\tau.
\]
Thus **every** sketch satisfying the screening test must have \(s_1=s_2\). That collision has probability exactly \(1/M\).

**Step 3: count all and only the accepted sketches.** Conditional on \(s_1=s_2\), the sketch is a common nonzero scalar multiple of \([s_3\ s_4]\). If \(s_3=\pm s_4\) it has rank one and is rejected; this happens with conditional probability \(2/M\). Otherwise, the normalized column inner product \(r=s_3^\mathsf Ts_4\) obeys \(|r|\le(\zeta-1)/\zeta\). Indeed distinct supports overlap in at most \(\zeta-1\) entries; on identical support, any nonparallel sign pattern contains both matching and mismatching signs. The two singular values of \([s_3\ s_4]\) are \(\sqrt{1\pm|r|}\), giving
\[
\kappa_2(SB_\varepsilon)=\sqrt{\frac{1+|r|}{1-|r|}}\le\sqrt{2\zeta-1}\le\tau.
\]
Independence of the four sketch columns therefore yields, **exactly at every admissible positive \(\varepsilon\)**,
\[
\Pr\bigl(\kappa_2(SB_\varepsilon)\le\tau\bigr)=\frac1M\left(1-\frac2M\right)=\frac{M-2}{M^2}.
\]
There are no other accepted outcomes; this proves the claim.

## Verification

The companion standalone \(\texttt{verify.py}\) checks the SPD Krylov realization at three positive parameters, enumerates all \(256\) signed columns for \(s=\zeta=8\), confirms exactly \(254\) nonparallel choices, verifies the minimum squared noncollision distance \(1/2\) and the maximum nonparallel inner product magnitude \(3/4\), and checks four exact binomial probability formulas. Run it with \(\texttt{python3 verify.py}\); the expected terminal status is \(\texttt{VERIFY_OK}\). These finite tests corroborate, but do not replace, the proof for all integers and the full parameter interval.

## Relationship to prior work

Güttel, Liu and Nyman (2026), Section 2.2, define this independent-column sparse sign sketch, and their Algorithm 4 checks \(\kappa(SB_j)\) against an adaptive threshold. Their analysis conditions on a valid subspace embedding; it does not state the exact false-safe collision probability above for a degenerate-limit normalized Krylov pair. Palitta et al. (2025) study truncated/sketched matrix-function Krylov methods and the value of whitening, but do not supply this four-column sparse collision law. Nelson and Nguyen (2013) prove broad sparse-embedding dimension/sparsity lower bounds; rank-loss upon coordinate collisions is related background, not the particular full-rank, **well-conditioned yet misleading** sketched basis with a nearly-identity SPD Krylov realization. Grigori et al. (2026) study similarity restoration for randomized Arnoldi; their target is a different defect.

## Limitations

The accepted event also makes the **sketched column norms shrink like \(\varepsilon\)**, so a separate norm-sensitive guard could detect it. The event can be exceedingly rare for practical sketch dimensions; at \(s=30,\zeta=8\) it is below one in a billion. This is a mathematical exact-arithmetic counterexample to interpreting a **condition number alone** as a full-rank embedding certificate, not a prediction of typical rounding error, a theorem about all sketches, or a contradiction of high-probability OSE guarantees. The result concerns the first two \(t=0\) normalized Krylov vectors; it neither establishes a complete restarted algorithm error nor treats orthogonalization parameters \(t>0\).

## References

1. S. Güttel, J. Liu, L. Nyman, *Sketch-and-Restart: Randomized Sketching in Quadrature-Based Restarting for Matrix Functions*, arXiv:2607.10354, first submitted 11 July 2026, https://arxiv.org/html/2607.10354v2; see Sections 2.2, 4.1 and 6.
2. D. Palitta et al., *Sketched and Truncated Polynomial Krylov Methods: Evaluation of Matrix Functions*, *Numerical Linear Algebra with Applications* (2025), https://onlinelibrary.wiley.com/doi/10.1002/nla.2596.
3. J. Nelson, H. L. Nguyen, *Lower Bounds for Oblivious Subspace Embeddings*, arXiv:1308.3280 (2013), https://arxiv.org/abs/1308.3280.
4. L. Grigori, D. Kressner, N. Shao, I. Simunec, *Restoring similarity in randomized Krylov methods with applications to eigenvalue problems and matrix functions*, arXiv:2601.10248 (2026), https://arxiv.org/abs/2601.10248.
