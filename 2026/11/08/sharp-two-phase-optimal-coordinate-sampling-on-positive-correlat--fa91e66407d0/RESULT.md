# Sharp two-phase optimal coordinate sampling on positive-correlation friendship matrices

## Finding

Let \(m\ge2\), \(q=2m\), \(0<s<1\), \(t>0\), and \(qt^2<1+s\). Consider the \((q+1)\times(q+1)\) real symmetric matrix \(C\) indexed by a hub \(0\) and \(m\) disjoint leaf pairs: its diagonal entries are one, every hub–leaf entry equals \(t\), the two distinct entries in each leaf pair have correlation \(s\), and all other leaf–leaf entries are zero. It is positive definite in exactly the specified parameter domain.

For the strictly convex quadratic \(f(z)=\tfrac12z^{\mathsf T}Cz-b^{\mathsf T}z\), select one coordinate \(i\) independently at each step with a fixed probability \(p_i\), and perform the exact update \(z^+=z-(Cz-b)_i e_i\). The sharp worst-direction one-step expected *squared \(C\)-energy decrement* is
\[
\rho(p)=\lambda_{\min}\!\left(C^{1/2}\operatorname{Diag}(p)C^{1/2}\right).
\]
Write \(c=1+s\), \(r=qt^2\), and \(s_0=(t+r)/(2+t)\). A globally optimal probability vector can always be chosen with hub mass \(x_*\) and a common mass \(y_*\) at each leaf. The exact maximum over **all** probability vectors, including nonsymmetric distributions, is:
\[
\begin{array}{c|c|c}
& 0<s\le s_0 & s_0<s<1\\ \hline
D & D_R=c+q+2qt & D_P=2s(1-s)+q(2s-r)\\[2pt]
x_* & (c+qt)/D_R & 2s(1-s)/D_P\\[2pt]
y_* & (1+t)/D_R & (2s-r)/D_P\\[2pt]
\rho_* & (c-r)/D_R & (1-s)(2s-r)/D_P
\end{array}
\]
The two branches coincide at \(s=s_0\); all applicable denominators and masses are positive. The class-symmetric optimum is unique, although uniqueness among nonsymmetric vectors is not asserted. The first regime is controlled by the smaller radial eigenvalue, while in the second the radial and within-pair antisymmetric constraints are simultaneously active. For \(m=2,s=1/2,t=1/5\), the optimum is \(x_*=25/193\), \(y_*=42/193\) and \(\rho_*=21/193\), exceeding the uniform-sampling decrement \(1/10\).

## Assumptions and scope

Every real parameter is as above, the vector \(b\) is arbitrary, and each step changes exactly one coordinate. A probability distribution is fixed and sampled independently of earlier steps; the optimization is of the worst-case conditional *one-step* expected squared energy, equivalently twice the objective gap. It does not address adaptive, block, accelerated, finite-horizon or approximate coordinate updates, and does not claim runtime optimality. The probability simplex includes its boundary, but an optimal distribution is strictly positive.

## Proof

**1. Spectrum and the exact descent objective.** The leaf space decomposes orthogonally into antisymmetric vectors on each pair (eigenvalue \(1-s>0\), multiplicity \(m\)) and vectors constant on each pair but having total leaf sum zero (eigenvalue \(c=1+s>0\), multiplicity \(m-1\)). The remaining normalized hub/all-leaf subspace has matrix
\[
B=\begin{pmatrix}1&\sqrt q\,t\\\sqrt q\,t&c\end{pmatrix},\qquad \det B=c-r>0.
\]
This proves positive definiteness. Write \(e=z-C^{-1}b\). Since \(C_{ii}=1\), exact coordinate minimization reduces \(e^{\mathsf T}Ce\) by \((Ce)_i^2\). Averaging over the chosen coordinate gives
\[
\mathbb E[\|e^+\|_C^2\mid e]=\|e\|_C^2-e^{\mathsf T}C\operatorname{Diag}(p)Ce,
\]
so the least possible relative decrement over all nonzero \(e\) is precisely \(\rho(p)\).

**2. Global symmetry reduction.** The least eigenvalue is concave as a function of an affine symmetric matrix. Therefore \(\rho(p)\) is concave in the sampling probabilities. Permuting the \(m\) leaf pairs and interchanging their members preserves \(C\) and \(\rho\). Averaging any candidate sampler over this automorphism group cannot decrease its performance. Thus the unrestricted maximum is attained among \(p=(x,y,\ldots,y)\) with \(x+qy=1\) and \(x,y\ge0\). At either endpoint a coordinate has zero sampling probability, making the smallest eigenvalue zero; a strictly positive sampler has positive rate.

**3. Correct radial matrix and the two active modes.** Nonzero eigenvalues of \(C^{1/2}\operatorname{Diag}(p)C^{1/2}\) are those of \(\operatorname{Diag}(\sqrt p)C\operatorname{Diag}(\sqrt p)\). For \(p=(x,y,\ldots,y)\), they are \((1-s)y\) with multiplicity \(m\), \(cy\) with multiplicity \(m-1\), and the two eigenvalues of the **correctly normalized** radial block
\[
R(x,y)=\begin{pmatrix}x&\sqrt{q}\,t\sqrt{xy}\\\sqrt{q}\,t\sqrt{xy}&cy\end{pmatrix}
=\begin{pmatrix}x&\sqrt{rxy}\\\sqrt{rxy}&cy\end{pmatrix}.
\]
In particular the off-diagonal square is \(rxy\), **not** \(qrxy\). Because \(1-s<c\), the objective reduces to
\[
\min\{(1-s)y,\lambda_-(R(x,y))\}.
\]
This normalization is essential for the stated transition and is consistent with the actual full matrix \(C\).

**4. Unconstrained radial optimum.** For a tentative positive rate \(\lambda\), write \(X=x/\lambda\), \(Y=y/\lambda\). The condition \(\lambda_-(R)\ge\lambda\) is exactly
\[
X\ge1,\quad cY\ge1,\quad (X-1)(cY-1)\ge rXY.
\]
For \(X>c/(c-r)\), its sharp lower boundary is \(Y=(X-1)/((c-r)X-c)\). Minimizing the total \(X+qY\) is equivalent to maximizing the radial eigenvalue under \(x+qy=1\). The derivative of the boundary is \(-r/((c-r)X-c)^2\); the unique stationary minimum has \((c-r)X-c=\sqrt{qr}=qt\), yielding
\[
X_R=\frac{c+qt}{c-r},\quad Y_R=\frac{1+t}{c-r},\quad
\lambda_R=\frac{c-r}{c+q+2qt}.
\]
This radial optimum meets the additional pairwise condition \((1-s)y_R\ge\lambda_R\) exactly when
\[
(1-s)(1+t)\ge c-r\iff s\le s_0=(t+r)/(2+t).
\]
In this first regime the radial upper bound is attained, proving the asserted formula and uniqueness within the symmetric class.

**5. Pair-limited regime.** Now take \(s>s_0\). Then \(2s-r>0\), since \(s(2+t)>t+r\) implies \(2s-r>t(1-s)>0\). At the radial maximizer \(x_R\), the pair eigenvalue \((1-s)y_R\) is too small. On the feasible line \(y=(1-x)/q\), the least radial eigenvalue is a strictly concave function of \(x\): it is the minimum eigenvalue of the affine pencil \(B^{1/2}\operatorname{diag}(x,y)B^{1/2}\), and its explicit two-by-two expression has positive off-diagonal coupling. It increases strictly from zero at \(x=0\) up to its unique radial maximizer \(x_R\). The competing pair eigenvalue \((1-s)(1-x)/q\) decreases strictly. Consequently there is exactly one crossing in \((0,x_R)\), and the minimum of the two constraints increases before this crossing and decreases afterward. Equating the smaller radial eigenvalue to \((1-s)y\) gives the determinant identity
\[
(x-(1-s)y)(cy-(1-s)y)=rxy,
\quad\frac{x}{y}=\frac{2s(1-s)}{2s-r}.
\]
Together with \(x+qy=1\) this gives the displayed \(x_*,y_*,\rho_*\). At equality \(s=s_0\), the two formulas coincide by direct substitution. Symmetry averaging from Step 2 proves unrestricted global optimality; the strict one-dimensional monotonicities prove class-symmetric uniqueness.

**6. Why a standard inverse-positive closed formula does not cover this family.** For \(m\ge2\), the positive correlations form overlapping triangles. In the displayed exact example \(m=2,s=1/2,t=1/5\), inversion of the leaf Schur complement gives negative within-pair entries and positive cross-pair entries. No diagonal sign change can make all such inverse entries nonnegative: within-pair signs would have to disagree while all signs from distinct pairs would have to agree. The inverse-positive matrix theorem therefore does not apply throughout this family, although the generic semidefinite E-optimal-design formulation does.

## Verification and reproducibility

The existing standard-library rational checker `artifacts/verify_friendship_sampling.py` reconstructs the full matrix, checks the correct determinant term \(rxy\), validates the probability formulas and positivity, verifies exact energy-loss identities and tests finite rational parameter grids. Its finite checks support the infinite-domain argument above but do not replace Steps 1–5. The proof above corrects a factor-of-\(\sqrt q\) transcription error in one displayed radial matrix of the earlier draft; it leaves the correctly normalized determinant calculations, final rates and optimal probabilities unchanged. The worked five-coordinate example is an exact independent arithmetic check.

## Relationship to prior work

General optimal-sampling semidefinite formulations appear in Qu and Richtárik (arXiv:1412.8060) and Gower and Richtárik (arXiv:1506.03296). Pukelsheim and Torsney (Ann. Statist. 1991, DOI:10.1214/aos/1176348265) give general optimal-design methodology; those frameworks do not by themselves evaluate this structured family or its phase transition. A published inverse-positive coordinate-sampling theorem assumes a property absent in the positive-triangle examples. The all-parameter explicit friendship-graph optimum is the claim evaluated here, not the general SDP itself. An older equivalent specialized result in matrix scaling or E-optimal design remains possible and is not ruled out simply by failed searches.

## Limitations

All statements concern exactly the specified normalized SPD family, fixed iid single-coordinate exact minimization, and sharp worst-case conditional one-step expected squared energy. They do not prove stability under approximate/noisy updates, uniqueness of every nonsymmetric optimizer, or adaptive optimality. Full historic priority cannot be certified without further specialist reading. No external formal certification is claimed.

## References

1. Z. Qu and P. Richtárik, *Coordinate Descent with Arbitrary Sampling I: Algorithms and Complexity*, https://arxiv.org/abs/1412.8060.
2. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, https://arxiv.org/abs/1506.03296.
3. F. Pukelsheim and B. Torsney, *Optimal weights for experimental designs on linearly independent support points*, Ann. Statist. **19** (1991), 1614–1625, https://doi.org/10.1214/aos/1176348265.
4. A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities* (2014), https://dash.harvard.edu/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/download.
