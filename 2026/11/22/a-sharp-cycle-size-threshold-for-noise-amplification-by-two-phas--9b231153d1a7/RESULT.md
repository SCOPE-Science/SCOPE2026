# A sharp cycle-size threshold for noise amplification by two-phase directed circular blur

## Finding
For every integer \(m\ge 2\) and rates \(0<a,b<1\), define the positive row-stochastic blur on \(2m\) circular samples by
\[
(Px)_{2j}=(1-a)x_{2j}+a x_{2j+1},\qquad
(Px)_{2j+1}=(1-b)x_{2j+1}+b x_{2j+2},
\]
where indices are modulo \(2m\). Let \(H=\{x\in\mathbb R^{2m}:\sum_j x_j=0\}\), representing arbitrary zero-mean image perturbations about a constant background. Then the **exact** induced Euclidean gain \(G_m=\sup_{x\in H\setminus\{0\}}\|Px\|_2/\|x\|_2\) is
\[
G_m=\max\left\{\sqrt{\frac{(1-2a)^2+(1-2b)^2}{2}},\ \sqrt{\frac{T+\sqrt{T^2-4\Delta_m}}{2}}\right\},
\]
where
\[
T=(1-a)^2+a^2+(1-b)^2+b^2,
\quad
\Delta_m=[(1-a)(1-b)]^2+(ab)^2-2ab(1-a)(1-b)\cos(2\pi/m).
\]
In particular the exact nonexpansivity frontier is
\[
\boxed{G_m\le1\quad\Longleftrightarrow\quad |a-b|\le2\sqrt{ab(1-a)(1-b)}\sin(\pi/m).}
\]
The inequality is strict on both sides: below the parameter frontier \(G_m<1\), and above it \(G_m>1\). Equality at the frontier gives \(G_m=1\).

For fixed unequal rates \(a,b\), sufficiently large cycles always amplify some zero-mean data in one step, even though the blur is pointwise a convex average. If \(0<d=|a-b|/[2\sqrt{ab(1-a)(1-b)}]<1\), the **first expanding** number of two-site cells is exactly \(\lfloor\pi/\arcsin d\rfloor+1\) (and the corresponding number of sample sites is twice this integer). If \(d=1\), the first expanding value is \(m=3\); if \(d>1\), it is \(m=2\). At \(a=b\) no cycle expands. For example \(a=2/5\), \(b=3/5\) has \(G_7<1<G_8\), so 16 sites are the first expanding cycle in this family.

## Assumptions and scope
All arithmetic in the theorem is exact; \(m\) is any integer at least two; the two mixing coefficients satisfy \(0<a,b<1\). The norm is the ordinary, unweighted Euclidean norm. The domain is the ordinary arithmetic-mean-zero real subspace \(H\); the output is measured in the full Euclidean space, without recentering. The operator \(P\) itself is not generally mean-preserving when \(a\ne b\). Replacing \(H\) by a stationary-weighted mean-zero subspace or measuring a weighted norm changes the question.

## Proof
**1. Fourier blocks.** Write \(x_{2j}=u_j\), \(x_{2j+1}=v_j\), and take the unitary length-\(m\) discrete Fourier transform in the cell index \(j\). At frequency \(\theta_k=2\pi k/m\), \(k=0,\dots,m-1\), the action becomes the \(2\times2\) complex block
\[
B(\theta)=\begin{pmatrix}1-a&a\\be^{i\theta}&1-b\end{pmatrix}.
\]
Every nonzero frequency is automatically in the complexification of \(H\), and its full two-dimensional block is unrestricted. At frequency zero, the mean-zero condition removes \((1,1)\); the surviving vector is proportional to \((1,-1)\), on which the gain is
\[
g_0=\frac{\|B(0)(1,-1)^{\mathsf T}\|_2}{\sqrt2}
=\sqrt{\frac{(1-2a)^2+(1-2b)^2}{2}}<1.
\]
Complexification does not change the operator norm of a real matrix restricted to a real subspace; the maximum singular gain of a nonzero-frequency block is realized by a real perturbation using a conjugate Fourier pair (or a real alternating mode when the frequency is \(\pi\)).

**2. Exact block norms and the winning frequency.** The trace of \(B(\theta)^*B(\theta)\) equals \(T\), independent of \(\theta\), and its determinant is
\[
\Delta(\theta)=[(1-a)(1-b)]^2+(ab)^2-2ab(1-a)(1-b)\cos\theta.
\]
Thus its larger eigenvalue is \([T+\sqrt{T^2-4\Delta(\theta)}]/2\). Because \(ab(1-a)(1-b)>0\), this eigenvalue is strictly increasing with \(\cos\theta\). Among the \(m-1\) nonzero Fourier frequencies its largest value occurs at \(k=1\) or \(k=m-1\), giving the formula with \(\Delta_m=\Delta(2\pi/m)\). Together with the zero-frequency line this proves the exact norm formula.

**3. The sharp frontier.** Since \(0<a,b<1\),
\[
T=2-2[a(1-a)+b(1-b)]<2.
\]
Therefore at any nonzero frequency the larger eigenvalue of \(B(\theta)^*B(\theta)\) exceeds one precisely when \(\det(I-B(\theta)^*B(\theta))<0\); the two eigenvalues cannot both exceed one. Direct expansion yields the exact identity
\[
\det(I-B(\theta)^*B(\theta))
=4ab(1-a)(1-b)\sin^2(\theta/2)-(a-b)^2.
\]
Apply this at \(\theta=2\pi/m\). Since \(g_0<1\), the asserted strict/non-strict inequalities follow, including equality. The critical size formula follows from strict monotonic decrease of \(\sin(\pi/m)\) on integers \(m\ge2\). For \(a=2/5,b=3/5\), the condition becomes \(1/5>(12/25)\sin(\pi/m)\), or \(\sin(\pi/m)<5/12\). It fails at \(m=7\) and holds at \(m=8\), as stated.

**4. Structural interpretation.** The operator is strictly positive along every self-loop and directed forward edge. It is an irreducible, aperiodic row-stochastic cycle map, so all its nonconstant eigenmodes have spectral radius below one. But its stationary left probability vector is not uniform: at each even site \(\pi_{2j}=b/[m(a+b)]\), and at each odd site \(\pi_{2j+1}=a/[m(a+b)]\). Jensen's inequality and stationarity give \(\|Px\|_{\pi}\le\|x\|_{\pi}\) for \(\|x\|_{\pi}^2=\sum_j\pi_j|x_j|^2\), even on cycles where the unweighted Euclidean gain on \(H\) exceeds one. The frontier therefore quantifies a genuine norm-dependent nonnormal transient, not a loss of positivity or Markov stability.

## Verification
The standalone `verify.py` uses only Python's standard library. Running `python verify.py` returns `VERIFY_OK 538 checks`: 405 exact-rational identities for the key Gram determinant, 132 independent finite ring gain/threshold comparisons using direct operator/transposed-operator power iteration, and one explicit seven-cell/eight-cell boundary check. Finite tests are diagnostic; the theorem for all dimensions and all real rates follows from the four analytic proof steps above.

## Relationship to prior work
González del Cueto and Guevara Vasquez, *Fast circular convolution with periodic kernels* (arXiv:2611.16144v1, first public November 12, 2026), establish unitary Fourier-block representations for periodic circular kernels and apply them to deconvolution and periodic-chain dispersion. The block decomposition itself is not new here. The present result solves an exact restricted singular-norm problem for the independently motivated two-phase **one-sided positive averaging** family, including its complete cycle-size threshold for amplification of mean-zero perturbations. The cited paper does not analyze this restricted norm or its phase frontier. The standard Markov weighted-norm contraction is likewise not claimed as new; the sharp unweighted finite-size boundary is the contribution.

## Limitations
The characterization concerns one forward averaging step and an alternating two-rate, two-tap kernel. It is not a general theorem for arbitrary periodic kernels, repeated-step maximum gain, or floating-point perturbations. The ordinary mean-zero domain is not invariant unless the two rates agree. The theorem is reviewed mathematically within this package, not independently audited; a search for earlier equivalent exact criteria cannot rule out unindexed prior work.

## References
1. F. González del Cueto and F. Guevara Vasquez, *Fast circular convolution with periodic kernels*, arXiv:2611.16144v1, November 12, 2026, https://arxiv.org/html/2611.16144v1 (especially Sections 4, 7, and 8).
2. F. R. K. Chung, *Spectral Graph Theory*, CBMS Regional Conference Series in Mathematics 92, American Mathematical Society, 1997 (background on stochastic/graph spectral methods; not a claimed source of the new threshold).
