# Generic finite termination and dyadic nontermination of four-mode nuclear-scaled polar descent

## Finding
Consider the isotropic matrix quadratic \(f(X)=\tfrac12\|X\|_{\mathrm F}^2\) and the nuclear-scaled polar update
\[
X_{k+1}=X_k-\frac14\|X_k\|_*\operatorname{msign}(X_k),
\]
where the polar factor is zero on the null singular space. On real or complex \(4\times4\) matrices, **Lebesgue-almost every initialization terminates exactly** after finitely many iterations. The failure of exact termination has empty interior and measure zero, despite being nonempty and including full-rank matrices.

More explicitly, suppose a full-rank matrix has singular values \(a_1,a_2,a_3,a_4>0\). When exactly two are strictly above their arithmetic mean and the other two strictly below, with the two values in each group distinct, the iteration terminates in at most four further steps, assuming no earlier simultaneous termination. If \(X_0\ne0\) has rank less than four, exact termination is impossible.

For the full-rank family with singular values \((3,1+t,1,1-t)\), \(0<t<1/4\), put
\[
N(t)=\min\{n\in\mathbb Z_{\ge0}:2^n t>1/4\}.
\]
For every \(t\) that is **not an inverse power of two**, the exact stopping time is \(T(t)=N(t)+5\). For every \(t=2^{-j}\), integer \(j\ge3\), an intermediate singular value becomes zero while others remain nonzero: exact termination never occurs, though convergence to zero continues. Accordingly \(T(t)=\log_2(1/t)+O(1)\) along the nonresonant family as \(t\downarrow0\).

## Assumptions and scope
Real or complex matrices are of size \(4\times4\). The update is exact, deterministic, and uses the nuclear norm and rank-preserving polar convention at zero singular values; there is no momentum, rounding, or floating-point truncation. The singular values are labelled only to describe their iterates, not to prescribe a fixed ordering after crossings. Lebesgue almost everywhere refers to ordinary real coordinates on the real matrix space (and real and imaginary coordinates in the complex case).

## Proof
**Singular-value reduction.** Fix an initial singular-value decomposition. At every iterate we can keep its left and right singular vectors up to signs, so the singular magnitudes evolve as
\[
a_i^+=\begin{cases}|a_i-m|,&a_i>0,\\0,&a_i=0,\end{cases}\qquad m=\frac14\sum_{i=1}^4a_i.
\]
Thus, on the strictly positive orthant, the map is the absolute deviation from the arithmetic mean. Every zero coordinate stays zero. If exactly \(r<4\) entries remain positive, the signed-coordinate update is \(z\mapsto (I-ss^\top/4)z\) on the active support, where \(s\) has \(r\) signs; its eigenvalues are \(1\) and \(1-r/4>0\), so a nonzero rank-deficient state cannot reach zero in a finite step. The squared Frobenius norm decreases by
\[
\|X_k\|_{\mathrm F}^2-\|X_{k+1}\|_{\mathrm F}^2
=\Big(\frac12-\frac r{16}\Big)\|X_k\|_*^2\ge\frac14\|X_k\|_*^2,
\]
which also proves convergence to zero from every starting matrix, even on the exceptional nonterminating set.

**A two-plus-two step annihilates in four moves.** For positive \((a_1,a_2,a_3,a_4)\) with two entries above the mean, write its centered values, after rearrangement, as \((u,v,-w,-z)\) with \(u,v,w,z>0\) and \(u+v=w+z=S\). The first new magnitude vector is \((u,v,w,z)\), with mean \(S/2\). The next one is
\[
\big(|u-v|/2,|u-v|/2,|w-z|/2,|w-z|/2\big).
\]
If both displayed pair values are nonzero, the following step makes all four magnitudes equal, and the fourth sends them to zero. If both pair values are zero, termination occurs earlier. The only adverse case is when just one pair value is zero, causing premature rank loss. The latter requires an exact equality within one of the original two mean-side pairs, a proper hyperplane.

**Escape from one-versus-three.** If exactly one entry of a positive quadruple lies above its mean, the next magnitude vector has a unique largest value \(A\) equal to the sum of the other three values \(b_1+b_2+b_3\). Exactly three entries above the mean similarly produce after one step a vector with this property, by exchange of the above/below groups. On the cone \(A=b_1+b_2+b_3>0\), the mean equals \(A/2\). If a smaller entry is greater than \(A/2\), then there are exactly two entries above the mean, so the previous paragraph applies, except on its proper equality hyperplanes. If all three smaller entries are below \(A/2\), the next largest entry is \(A/2\) and normalized smaller coordinates \(y_i=b_i/A\) evolve by
\[
y_i^+=1-2y_i,\quad\sum_i y_i=1.
\]
No smaller coordinate can stay in \([0,1/2]\) through indefinitely many such steps unless every \(y_i=1/3\): indeed
\[
y_i^{(n)}=\frac13+(-2)^n\big(y_i^{(0)}-\frac13\big).
\]
Hence every nonexceptional positive starting quadruple enters a two-plus-two chamber after finitely many steps. The exceptional perpetual one-versus-three state has three equal smaller magnitudes and shrinks by \(1/2\) per step. At any finite stage, a premature zero, exact equality inside a mean-side pair, or the equal-triplet condition is a proper affine hyperplane or lower-dimensional affine set on each of finitely many linear sign chambers. Taking the countable union over all finite stages leaves a Lebesgue-null set of initial singular-value quadruples. The singular-value map from matrices is absolutely continuous away from repeated singular values and rank loss; those sets are themselves null. Therefore almost every full-rank matrix terminates exactly.

**Explicit resonance and time.** Take singular magnitudes \((3,1+t,1,1-t)\), with \(0<t<1/4\). Their mean is \(3/2\), and one update gives \((3/2,1/2-t,1/2,1/2+t)\). Divide the last three by the first to obtain
\[
\big(1/3-2t/3,\;1/3,\;1/3+2t/3\big).
\]
As long as one-versus-three persists, the deviations from \(1/3\) are multiplied by \(-2\) each time. It persists until \(2^n t>1/4\). If \(t\) is not an inverse power of two, the first strict crossing has \(1/4<2^{N(t)}t<1/2\), keeps every coordinate positive, and enters a strict two-plus-two chamber with two unequal entries on each side. Four more steps terminate: \(T=N(t)+5\). If \(t=2^{-j}\), one step hits a mean equality at the threshold \(2^{j-2}t=1/4\), producing one zero and three nonzero singular values; subsequent exact termination is impossible by the rank-deficient invertibility argument. This proves both the exact stopping law and the logarithmic delay.

## Verification
Run `python3 verify.py` in the unpacked package. The checker exercises exact rational iterates at inverse-power resonances, off-resonance stopping laws, and strict two-plus-two chambers, with supplementary reproducible finite random tests. All infinite and almost-everywhere assertions follow from the analytic proof above, **not** from numerical sampling. The one-step norm identity is independent of the checker.

## Relationship to prior work
Jawanpuria, Garai and Mishra (2026) establish global linear convergence of nuclear-scaled polar steps on strongly convex matrix quadratics under a trace-dependent step threshold; their Proposition 8 describes special invariant equal-amplitude singular directions and explicitly leaves the general rate dependent on initialization. The result here determines a qualitatively stronger *generic finite* termination phenomenon in the four-singular-value isotropic case and gives an exact arithmetic stopping-time bifurcation. Lau, Long and Su (2025) introduce the nuclear-scaled polar family and give rate theory, not the four-mode termination dichotomy. Gonon, Muşat and Boumal (2026) show lattice obstruction for the **unscaled** fixed-length polar step, which does not apply after nuclear scaling. A related independent Hadamard/sign-projection product result characterizes possible annihilating direction sequences, but does not force the endogenous sign sequence selected by nuclear-scaled descent or establish its generic stopping behavior.

## Limitations
This is an exact-arithmetic, four-singular-mode theorem at the specific optimal step \(1/4\). Neither stability under finite precision, generic finite termination in other dimensions, nor a practical iteration count bound uniform across all initializations is asserted. Full-rank dyadic resonances give arbitrarily slow exact stopping close to exceptional rays, so the exact-termination property is not robust under singular-value perturbations in the sense of uniform horizon bounds. Historical priority is qualified by the possibility of an unindexed equivalent absolute-deviation dynamical system.

## References
1. P. Jawanpuria, B. Garai and B. Mishra, *Constant Step Sizes for Muon-Type Spectral Optimizers on Strongly Convex Quadratics*, arXiv:2610.27747 (first public 2026-10-20), https://arxiv.org/abs/2610.27747.
2. T. T.-K. Lau, Q. Long and W. Su, *PolarGrad: A Class of Matrix-Gradient Optimizers from a Unifying Preconditioning Perspective*, arXiv:2505.21799 (2025), https://arxiv.org/abs/2505.21799.
3. A. Gonon, A.-A. Muşat and N. Boumal, *Insights on Muon from Simple Quadratics*, arXiv:2602.11948 (2026), https://arxiv.org/html/2602.11948v1.
