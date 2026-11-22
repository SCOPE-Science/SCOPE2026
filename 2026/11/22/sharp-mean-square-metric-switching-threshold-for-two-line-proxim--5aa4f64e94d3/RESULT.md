# Sharp mean-square metric-switching threshold for two-line proximal splitting

## Finding

A proximal splitting map can converge linearly under either of two **fixed** positive-definite scalar metrics, and even under their **strict periodic alternation**, while independent random alternation between precisely the same two metrics causes exponentially growing expected squared primal--dual error. The gap is quantified exactly for two noncoincident lines and, more generally, for every reciprocal-symmetric probability law on positive scalar metrics.

Let \(0<c<1\), \(s=\sqrt{1-c^2}\), \(U=\operatorname{span}(e_1)\), and \(V=\operatorname{span}((c,s)^\top)\). Apply the three-operator proximal/dual update below with independent metrics \(M_k=m_kI_2\), where \(m_k>0\), \(m_k\overset{d}=m_k^{-1}\), and \(v=\mathbb E[m_k^2]<\infty\). For every deterministic compatible initial state, every integer \(k\ge0\), and the resulting iterates,
\[
\boxed{\mathbb E\bigl(\|z_k\|_2^2+\|u_k\|_2^2\bigr)
=\bigl[c^2(c^2+(1-c^2)v)\bigr]^k
\bigl(\|z_0\|_2^2+\|u_0\|_2^2\bigr).}
\]
Write \(p=c^2\). The complete classification is:

- If \(1\le v\le2\), every \(0<p<1\) is mean-square convergent; the edge \(v=2\) is included, with no uniform rate as \(p\uparrow1\).
- If \(v>2\), the iteration is mean-square convergent for \(0<p<1/(v-1)\), retains constant nonzero second moment at equality, and exhibits exponential mean-square divergence for \(1/(v-1)<p<1\) from **every nonzero deterministic compatible initial state**.

For the equally likely two-valued reciprocal law \(m_k\in\{r,r^{-1}\}\), with \(r\ge1\), the law is mean-square convergent for every pair of noncoincident lines **if and only if** \(r^2\le2+\sqrt3\). In contrast, the deterministic strict alternation \(r,r^{-1},r,r^{-1},\ldots\) converges for every such line whenever \(r^2<3+2\sqrt2\). Thus for
\[
\boxed{2+\sqrt3<r^2<3+2\sqrt2}
\]
there exist near-parallel lines for which independent switching is mean-square divergent while alternating the **same metric values deterministically** converges for every line angle. The deterministic-alternation threshold is known from earlier two-period analysis; the new claim is the exact independent-switching law and its strict stability separation.

An exact instance has \(c=3/\sqrt{10}\), \(s=1/\sqrt{10}\), and \(r=2\). Independent equiprobable switching gives mean-square factor \(801/800>1\). Strict alternating switching gives a two-step matrix with trace \(99/80\), determinant \(81/100\), and nonreal-conjugate eigenvalues of modulus \(9/10<1\).

## Assumptions and scope

Define \(\iota_U\) and \(\iota_V\) as the convex indicator functions of the two subspaces above, and minimize \(\iota_U+\iota_V\) on \(\mathbb R^2\). Its unique intersection is zero. With \(f=0\), the proximal/dual component of the variable-metric three-operator scheme is
\[
\begin{aligned}
x_{k+1}&=\operatorname{prox}_{M_k,\iota_U}(z_k-M_k^{-1}u_k),\\
z_{k+1}&=\operatorname{prox}_{M_k,\iota_V}(x_{k+1}+M_k^{-1}u_k),\\
u_{k+1}&=u_k+M_k(x_{k+1}-z_{k+1}),
\end{aligned}
\]
where \(\operatorname{prox}_{M,\iota_W}\) is the metric projection onto the subspace \(W\). For scalar metrics \(M=mI_2\), these projections are Euclidean. Assume compatible initialization \(z_0\in V\), \(u_0\in V^\perp\), with an arbitrary deterministic vector in each, not both zero. Let \((m_k)_{k\ge0}\) be independent identically distributed positive variables, independent of the initialization, with the reciprocal distribution symmetry and finite second moment stated above. For the deterministic comparison replace the random law by the prescribed alternating sequence. All statements concern the joint ordinary Euclidean primal--dual squared norm, **not** the moving metric norm and not pathwise divergence. The original published algorithm constrains successive metric proposals; the unconstrained switching studied here intentionally does **not** satisfy that safeguard.

## Proof

Put \(v_0=(c,s)^\top\) and \(n_0=(-s,c)^\top\). By compatibility and the projection formulas, write \(z_k=a_kv_0\), \(u_k=b_kn_0\). Then
\[
x_{k+1}=(a_kc+b_ks/m_k,0)^\top,
\quad a_{k+1}=c^2a_k+\frac{cs}{m_k}b_k,
\quad b_{k+1}=-m_kcs\,a_k+c^2b_k.
\]
These formulas prove the subspace compatibility persists. Equivalently, with \(w_k=(a_k,b_k)^\top\),
\[
w_{k+1}=T(m_k)w_k,\qquad
T(m)=\begin{pmatrix}c^2&cs/m\\-mcs&c^2\end{pmatrix}.
\]
For each constant \(m>0\), \(\operatorname{spec}T(m)=\{c^2+ics,c^2-ics\}\), each eigenvalue of modulus \(c<1\), proving stationary linear convergence.

Compute the exact conditional Gram matrix:
\[
T(m)^\top T(m)=
\begin{pmatrix}
c^4+c^2s^2m^2&c^3s(m^{-1}-m)\\
c^3s(m^{-1}-m)&c^4+c^2s^2m^{-2}
\end{pmatrix}.
\]
Reciprocal-distribution symmetry gives \(\mathbb E[m]=\mathbb E[m^{-1}]\) and \(\mathbb E[m^2]=\mathbb E[m^{-2}]=v\). All relevant moments are finite by Cauchy--Schwarz. Hence
\[
\mathbb E[T(m_k)^\top T(m_k)]=\lambda I_2,\qquad
\lambda=c^4+c^2s^2v=p[v-(v-1)p].
\]
Since the fresh metric is independent of \(w_k\), conditional expectation gives \(\mathbb E[\|w_{k+1}\|^2\mid w_k]=\lambda\|w_k\|^2\); iteration yields the stated identity for all \(k\). Orthogonality of \(v_0,n_0\) identifies \(\|w_k\|^2=\|z_k\|^2+\|u_k\|^2\). At \(\lambda<1\), the expected squared error decays geometrically; Markov's inequality and Borel--Cantelli also give almost-sure convergence of this joint state. At \(\lambda=1\) its expectation remains positive for any nonzero deterministic start; at \(\lambda>1\) it grows geometrically, but no claim about almost-sure divergence is made.

The exact factorization
\[
\lambda-1=-(1-p)\,[1-(v-1)p]
\]
with \(0<p<1\), proves the complete phase diagram. The case \(1\le v<\infty\) follows from \(v=(\mathbb E[m^2]+\mathbb E[m^{-2}])/2\ge1\). For the reciprocal two-point law, \(v=(r^2+r^{-2})/2\). Solving \(v\le2\) for \(r\ge1\) gives \(r^2\le2+\sqrt3\), including equality.

For the separate **deterministic** strict alternation, let \(P=T(r^{-1})T(r)\). Its two-step invariants are, for \(p=c^2\) and \(q=r^2+r^{-2}\),
\[
\operatorname{tr}P=2p^2-p(1-p)q,\qquad \det P=p^2.
\]
The real quadratic Schur criterion (two roots strictly inside the unit circle) requires \(1-\operatorname{tr}P+\det P>0\) and \(1+\operatorname{tr}P+\det P>0\). The first expression is \((1-p)(1+p+pq)>0\), and the second is \(1+3p^2-p(1-p)q\). Their positivity for all \(p\in(0,1)\) is equivalent to
\[
q<\min_{0<p<1}\frac{1+3p^2}{p(1-p)}=6,
\qquad
\frac{1+3p^2}{p(1-p)}=6+\frac{(3p-1)^2}{p(1-p)}.
\]
For \(r\ge1\), \(q<6\) means \(r^2<3+2\sqrt2\). This deterministic result is also available in the prior two-period literature. For any \(2+\sqrt3<r^2<3+2\sqrt2\), the independent-switching factor exceeds one for \(1/(v-1)<p<1\), yet periodic switching is spectrally convergent for every \(0<p<1\), yielding the sharp contrast window.

For the exact witness \(p=9/10\), \(cs=3/10\), and \(r=2\), the matrices are
\[
T(2)=\begin{pmatrix}9/10&3/20\\-3/5&9/10\end{pmatrix},\qquad
T(1/2)=\begin{pmatrix}9/10&3/5\\-3/20&9/10\end{pmatrix}.
\]
The independent expected-norm factor is \(p^2+p(1-p)(17/8)=801/800\). The alternating product has trace \(99/80\), determinant \(81/100\), and negative characteristic discriminant, so both eigenvalues have modulus \(9/10\). This establishes the explicit separation exactly.

## Verification

Run `python verify.py` with Python's standard library. The independent exact-rational diagnostic script directly performs the three projection/dual updates, independently checks the reduced transfer matrices, enumerates independent binary switching words through five iterations across seven rational line geometries, checks the conditional second-moment factor and strict alternating Schur invariants, and verifies the \(801/800\) versus stable two-step witness. It returned `VERIFY_OK 1481 exact-rational assertions; exact iid growth and stable alternating witness`. The infinite-horizon and all-angle conclusions are proved analytically above; finite checks are not substituted for proofs.

## Relationship to prior work

Suh and Isaac introduced the variable-metric proximal/dual scheme and made control of successive metric changes a central part of their convergence hypotheses; their Algorithm 1 restricts accepted metric proposals by line 15. It supplies the motivating exact update, **not** a guarantee for the unsafeguarded independent switching considered here. A published two-period subspace analysis, *Sharp two-period metric-ratio barrier for convex-subspace three-operator splitting*, computes the deterministic alternating threshold \(3+2\sqrt2\) in an equivalent transformed two-dimensional setting. That threshold is expressly credited, and the deterministic calculation is included only to exhibit the scientifically relevant gap. It does not contain the independent-metric conditional second-moment identity, reciprocal-law angle phase diagram, or uniform random threshold \(2+\sqrt3\). The classical fixed-metric Douglas--Rachford subspace convergence results have constant iteration maps rather than independent metric products. Nonstationary splitting convergence theorems requiring controlled or convergent steps do not imply an unrestricted independent-switching stability law.

A separately relevant stochastic preconditioned Douglas--Rachford study by Dong, Bredies and Sun treats stochastic updates in a separable-dual-variable saddle-point setting. Its abstract was accessible, but a sufficiently detailed lawful full text was not available in this investigation. Consequently one cannot rule out a historically equivalent specialized calculation in that article or other unindexed sources; neither a missing text nor unsuccessful search establishes absolute novelty.

## Limitations

The exact scalar conditional second-moment identity depends on the reciprocal symmetry of the metric distribution, independent fresh switching and the two-line geometry. Asymmetric distributions, general SPD metrics, nonlinear objectives and more than two dimensions require separate analysis. Mean-square divergence does not imply almost-sure divergence, and no such implication is claimed. The stochastic metrics violate the original safeguarded metric-proposal rule: the result does not contradict the paper's convergence theorems. The comparison is an exact arithmetic result, not evidence of a practical implementation defect. Full historical priority and independent scientific audit are outstanding.

## References

1. H. Suh and T. Isaac, *Variable Metric Three Operator Splitting*, arXiv:2610.38935v1, first submitted 2026-10-28, https://arxiv.org/html/2610.38935v1.
2. *Sharp two-period metric-ratio barrier for convex-subspace three-operator splitting*, publicly archived mathematical result, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-period-metric-ratio-barrier-for-convex-subspace-three--022a78167486.
3. D. A. Lorenz and Q. Tran-Dinh, *Non-stationary Douglas--Rachford and alternating direction method of multipliers: adaptive stepsizes and convergence*, arXiv:1801.03765, https://arxiv.org/abs/1801.03765.
4. H. H. Bauschke, J. Y. Bello Cruz, T. T. A. Nghia, H. M. Phan and X. Wang, *The rate of linear convergence of the Douglas--Rachford algorithm for subspaces is the cosine of the Friedrichs angle*, arXiv:1309.4709, https://arxiv.org/abs/1309.4709.
5. Y. Dong, K. Bredies and H. Sun, *A stochastic preconditioned Douglas--Rachford splitting method for saddle-point problems*, arXiv:2212.13001, https://arxiv.org/abs/2212.13001.
