# Exact minimax omission sampling for a frustrated three-coordinate quadratic

## Finding
For each pair of real parameters \(0<c\le d<1\) satisfying \(2c^2+d<1\), define
\[
G=\begin{pmatrix}1&c&c\\c&1&-d\\c&-d&1\end{pmatrix},\qquad H=G^{-1},\qquad f(x)=\tfrac12x^{\mathsf T}Hx.
\]
At each iteration, independently omit exactly one of the three coordinates, with fixed probabilities \(p=(p_0,p_1,p_2)\), and *exactly minimize* \(f\) over the two coordinates not omitted, keeping the omitted coordinate fixed. For arbitrary deterministic \(x\ne0\), define the sharp conditional worst-direction expected retention
\[
\Lambda(p)=\sup_{x\ne0}\frac{\mathbb E[f(x^+)\mid x]}{f(x)}.
\]
Put \(Z=2c^2+d^2+3d\). The globally optimal choice and the exact minimax retention are
\[
\boxed{p^*=Z^{-1}\bigl(d(1+d),\ c^2+d,\ c^2+d\bigr),\qquad
\min_p\Lambda(p)=\frac{(1+d)(c^2+d)}{Z}.}
\]
The volume-sampling distribution on coordinate pairs is exactly uniform, and its sharp retention is
\[
\Lambda(p^{\rm vol})=\frac{1+d}{3},\qquad
\frac{\Lambda(p^{\rm vol})}{\min_p\Lambda(p)}
=1+\frac{d^2-c^2}{3(c^2+d)}.
\]
Consequently it is strictly suboptimal whenever \(c<d\), and optimal at \(c=d\). The ratio is strictly below \(4/3\) throughout the domain, with supremum \(4/3\), approached as \(c\downarrow0\) and \(d\uparrow1\) along admissible parameters. Equivalently, in that limit the best guaranteed *one-step decrement* is asymptotically \(3/2\) times the volume-sampling decrement. These are sharp conditional one-step comparisons, not claims about multistep runtime or global convergence-optimality.

## Assumptions and scope
The index convention is \(0\) for the central coordinate and \(1,2\) for the paired coordinates. The parameter restrictions guarantee \(G\succ0\), since its spectrum consists of \(1+d\) and the eigenvalues of \(\begin{psmallmatrix}1&\sqrt2 c\\\sqrt2 c&1-d\end{psmallmatrix}\); the latter matrix has positive determinant \(1-d-2c^2\). Probabilities may be zero at boundaries of the probability simplex, but in the stated range all three displayed optimal weights are positive. No assumptions about Gaussianity or external random errors are used. The outcome is an exact two-coordinate block minimization at each draw; weights are fixed rather than adapted to the current iterate.

## Proof
**1. Projection geometry.** Let \(e_j\) be a standard coordinate vector. After minimizing over the other two coordinates, the residual error is \(x^+=x_j H^{-1}e_j/(e_j^{\mathsf T}H^{-1}e_j)\), because the new gradient has zero entries at the optimized coordinates and \(x_j\) is unchanged. Since every diagonal of \(G=H^{-1}\) equals one, the normalized residual in the energy coordinate \(z=H^{1/2}x\) is the rank-one orthogonal projection \(z^+=v_jv_j^{\mathsf T}z\), with \(v_j=H^{-1/2}e_j\). Their Gram matrix is \(v_i^{\mathsf T}v_j=G_{ij}\). Hence
\[
\Lambda(p)=\lambda_{\max}\bigl(\textstyle\sum_jp_jv_jv_j^{\mathsf T}\bigr)
=\lambda_{\max}(P^{1/2}GP^{1/2}),\quad P=\operatorname{diag}(p).
\]
The first expression is convex in \(p\), and the Gram matrix is invariant under swapping leaves \(1\) and \(2\). Averaging any \(p\) with the leaf-swapped distribution cannot increase \(\Lambda\). Therefore there exists a globally optimal distribution \((a,b,b)\), where \(b=(1-a)/2\) and \(0\le a\le1\).

**2. The two competing modes.** For \((a,b,b)\), the antisymmetric leaf direction has eigenvalue
\[
T(a)=\frac{1-a}{2}(1+d).
\]
The central/symmetric-leaf subspace contributes a \(2\times2\) matrix
\[
\begin{pmatrix}a&c\sqrt{a(1-a)}\\c\sqrt{a(1-a)}&\frac{1-a}{2}(1-d)\end{pmatrix},
\]
whose larger eigenvalue is
\[
L(a)=\frac12\left[a+\frac{1-a}{2}(1-d)
+\sqrt{\left(a-\frac{1-a}{2}(1-d)\right)^2+4c^2a(1-a)}\right].
\]
Thus \(\Lambda(a,b,b)=\max\{T(a),L(a)\}\). The two branches cross exactly once in \((0,1)\), namely at
\[
a_*=\frac{d(1+d)}{Z},\quad b_*:=\frac{1-a_*}{2}=\frac{c^2+d}{Z}.
\]
To see this, substitute \(T(a)\) into the characteristic polynomial of the \(2\times2\) block: after cancelling \(1-a\), its zero equation is the linear identity \(d(1+d-(3+d)a)=2c^2a\). At \(a=a_*\), \(T(a_*)>a_*\), so the crossing is with the *larger* eigenvalue \(L\), not the smaller one. As \(T(0)>L(0)\) and \(T(1)<L(1)\), the larger of these two branches is \(T\) before the crossing and \(L\) afterwards.

**3. Global minimization.** The function \(T\) is strictly decreasing. The function \(L\) is strictly convex on \((0,1)\): the quadratic radicand \(Q(a)\) above has \(4Q_2Q_0-Q_1^2=8c^2(1-d-2c^2)>0\) when \(Q(a)=Q_2a^2+Q_1a+Q_0\). Direct differentiation at the crossing gives
\[
L'(a_*)=\frac{(2c^2-c(1+d)+2d)(2c^2+c(1+d)+2d)}{2(3c^2d+c^2+2d^2)}>0.
\]
Indeed, \(2c^2-c(1+d)+2d\ge c(c+1)>0\) under \(d\ge c\), and the other factor is positive. So \(L\) increases for all \(a\ge a_*\), while \(T\) decreases for all \(a\le a_*\). The maximum is uniquely minimized among leaf-symmetric laws at \(a_*\). Symmetrization proves global minimax optimality over every possible omission distribution. Its value is \(T(a_*)=(1+d)(c^2+d)/Z\).

**4. Volume sampling and the sharp gap.** Since each diagonal of \(G\) is one, the principal-minor cofactor identity gives \(\det H_{-j,-j}=\det(H)(H^{-1})_{jj}=\det(H)\) for all \(j\). Hence determinant-proportional sampling of the two retained coordinates omits each index with probability \(1/3\). The eigenvalues of \(G\) are \(1+d\) and the two eigenvalues of the symmetric block in step 1. When \(d\ge c\), the latter are at most \(1+d\), because \(\sqrt{d^2+8c^2}\le3d\). Therefore \(\Lambda(p^{\rm vol})=(1+d)/3\). Subtracting the exact values gives
\[
\Lambda(p^{\rm vol})-\Lambda(p^*)=\frac{(1+d)(d^2-c^2)}{3Z}.
\]
The ratio formula in the finding follows, with strict improvement precisely when \(c<d\). Finally \(0<d<1\) and \(c>0\) imply
\[
1+\frac{d^2-c^2}{3(c^2+d)}<1+\frac d3<\frac43.
\]
The upper bound is approached along, for example, \(d=1-\varepsilon\), \(c=\varepsilon/4\), with sufficiently small positive \(\varepsilon\); these satisfy \(2c^2+d<1\). In that limit the optimal and volume retentions tend to \(1/2\) and \(2/3\), respectively, so their guaranteed error decreases tend to \(1/2\) and \(1/3\), with ratio \(3/2\). This completes the proof.

## Verification
The standalone script `check.py` checks the symbolic identities, principal-minor and eigenvalue formulas, and a broad finite rational-parameter grid of candidate versus alternative probability distributions. Run `python check.py` in an environment with NumPy and SymPy. A recorded output is supplied as `checks.txt`. The infinite-parametric theorem is established by the proof above; finite computation is corroboration, not extrapolation.

## Relationship to prior work
Rodomanov and Kropotov (2019, arXiv:1904.04587) define volume-sampled block coordinate descent and derive its general expected descent matrix, but do not classify the sharp optimal fixed omission distribution for the frustrated signed triangle. Gower and Richtárik (2015, arXiv:1506.03296) give the general randomized block/sketch spectral-rate framework, not these explicit minimax weights or sharp gap. A related earlier result (opaque identifier `e118fcf8-fe26-4446-9cab-ac751657eead`) derives a sufficient closed-form optimal sampling rule when the normalized inverse Gram matrix can be sign-conjugated to an entrywise nonnegative matrix. The present matrix has nonzero cycle-sign product \(G_{01}G_{02}G_{12}=-c^2d<0\), so no diagonal sign conjugation makes it entrywise nonnegative; the sufficient hypothesis does not apply. This difference is mathematical, not merely terminological.

## Limitations
The result concerns exactly three coordinates, two-coordinate exact minimization, fixed iid omission sampling, and the signed-correlation regime \(0<c\le d<1\), \(2c^2+d<1\). It does not determine the minimax law for all admissible positive \(c,d\), higher-dimensional block structures, approximate block solves, multi-iteration optimality, or wall-clock performance. No claim of independent mathematical validation or of exhaustive literature precedence is made.

## References
1. A. Rodomanov and D. Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling*, arXiv:1904.04587 (first posted April 9, 2019); published in SIAM Journal on Optimization 30 (2020), 1878–1904. https://arxiv.org/abs/1904.04587
2. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296 (2015); SIAM Journal on Matrix Analysis and Applications 36 (2015), 1660–1690. https://arxiv.org/abs/1506.03296
