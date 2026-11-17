# A sharp six-oscillator ceiling for attracting antipodal states under repeated-index triadic coupling

## Finding

In the finite complete-graph, identical-frequency Kuramoto model with attractive pairwise interaction and the repeated-index three-body interaction \(\sin(2\theta_j-\theta_\ell-\theta_i)\), every nontrivial two-cluster phase-locked equilibrium is locally attracting modulo overall rotation **if and only if** it consists of one solitary oscillator against \(N-1\) coincident oscillators, \(3\le N\le6\), and
\[
\frac{K_2}{K_1}>\frac{N^3}{(N-1)[8(N-1)-N^2]}.
\]
This condition is sharp, including its equality boundary: no nontrivial two-cluster phase-locked state is Lyapunov stable at or below the displayed threshold, and for \(N\ge7\) none is Lyapunov stable at any positive coupling ratio. The four thresholds for \(N=3,4,5,6\) are, respectively, \(27/14\), \(8/3\), \(125/28\), and \(54/5\). The completely synchronized state is always exponentially attracting modulo rotation. Hence the exact number of attracting two-cluster-or-synchronized equilibrium circles is \(N+1\) above threshold for \(3\le N\le6\), and one otherwise; this does not count unrelated equilibria or attractors.

## Assumptions and scope

Fix an integer \(N\ge3\), coupling strengths \(K_1,K_2>0\), and common natural frequency \(\Omega\). The phase space is \((\mathbb R/2\pi\mathbb Z)^N\) and the dynamics are
\[
\dot\theta_i=\Omega+\frac{K_1}{N-1}\sum_{j=1}^N\sin(\theta_j-\theta_i)
+\frac{K_2}{N^2}\sum_{j=1}^N\sum_{\ell=1}^N
\sin(2\theta_j-\theta_\ell-\theta_i),\quad 1\le i\le N.
\]
**Repeated indices are included** in both sums; the diagonal pairwise terms vanish, but repeated indices in the three-body term affect its derivative. This is the complete-graph, equal-frequency specialization of the finite-size network model of Sharma et al. The common frequency is removed by a co-rotating reference frame. A two-cluster configuration has precisely two distinct phase values, both nonempty; a phase-locked configuration has constant phase differences (so it is an equilibrium after a common frequency shift). Local exponential attraction and Lyapunov stability are understood transverse to the global phase-shift circle. The classification is restricted to these two-cluster configurations.

Write \(A=NK_1/(N-1)\) and \(B=K_2\). Define \(Z_r=N^{-1}\sum_j e^{ir\theta_j}\). The phase vector field after removing \(\Omega\) is exactly
\[
\dot\theta_i=\operatorname{Im}\bigl[(AZ_1+B Z_2\overline{Z_1})e^{-i\theta_i}\bigr].
\]

## Proof

**Exact cluster separation.** Take \(n\) oscillators at phase \(0\) and \(m=N-n\) at phase \(\Delta\), where \(n,m\ge1\). Such configurations form an invariant two-cluster submanifold. Substituting \(Z_1=(n+me^{i\Delta})/N\), \(Z_2=(n+me^{2i\Delta})/N\) and subtracting the two group velocities gives
\[
\dot\Delta=-\sin\Delta\left[A+B\left(\frac{(n-m)^2}{N^2}+\frac{4nm}{N^2}\cos\Delta\right)\right].\tag{1}
\]
Any non-antipodal two-cluster locked separation satisfies \(0<\Delta<2\pi\), \(\Delta\ne\pi\), and the bracket in (1) is zero. The derivative of the right-hand side there is \(4Bnm\sin^2\Delta/N^2>0\). It is therefore linearly unstable even within the two-cluster manifold. The remaining possibilities are antipodal separations \(\Delta=\pi\) and synchrony.

**Antipodal transverse spectrum.** At an antipodal configuration set \(s_i=+1\) for \(n\) oscillators and \(s_i=-1\) for \(m\), and \(S=n-m\). Direct differentiation of the *full* repeated-index sum gives
\[
J_{iv}=\frac{A}{N}\sum_j s_i s_j(\mathbf1_{v=j}-\mathbf1_{v=i})
+\frac{B}{N^2}\sum_{j,\ell}s_i s_\ell
(2\mathbf1_{v=j}-\mathbf1_{v=\ell}-\mathbf1_{v=i}).\tag{2}
\]
The terms indexed by \(j\) retain their factor two, even when \(j=\ell\). The Jacobian preserves within-cluster zero-sum perturbations and perturbations constant on each block. In the first two subspaces the eigenvalues are
\[
\lambda_n=-\frac{S}{N}(A+B)\quad(n-1\text{ times}),\qquad
\lambda_m=\frac{S}{N}(A+B)\quad(m-1\text{ times}).\tag{3}
\]
The two-block quotient has one rigid-rotation eigenvalue zero and one relative-phase eigenvalue
\[
\lambda_{\rm rel}=A+B\left(1-\frac{8nm}{N^2}\right).\tag{4}
\]
Equations (2)–(4) can be checked directly by adding entries of the corresponding Jacobian blocks; no continuum or large-population limit is used.

If \(n>m\ge2\), then \(\lambda_m>0\), so the antipodal state is unstable. The case \(m>n\ge2\) is symmetric. If \(n=m\ge2\), the linearization has zero internal modes; nevertheless this case is also **nonlinearly unstable**, as follows. Keep all \(m=n\) negative-block phases at \(\pi\), split two positive-block phases symmetrically to \(\pm u\), and leave its other phases at zero. This submanifold is invariant, its order parameters are real, and
\[
Z_1=\frac{2(\cos u-1)}N,
\qquad Z_2=1+\frac{2(\cos(2u)-1)}N,
\qquad \dot u=-Z_1(A+BZ_2)\sin u.
\]
For every sufficiently small \(u>0\), \(\dot u>0\). The small positive perturbations therefore move away from the antipodal configuration, establishing Lyapunov instability for all \(A,B>0\), including when the linear relative mode is neutral or attracting.

It remains to consider \(n=N-1\), \(m=1\). The within-majority eigenvalue is negative and the minority internal mode is absent. Thus exponential attraction is equivalent to
\[
A+B\left(1-\frac{8(N-1)}{N^2}\right)<0.
\]
The coefficient of \(B\) is strictly negative precisely when \(N^2-8N+8<0\), i.e. at integer sizes \(N=3,4,5,6\). Solving for \(B/K_1\) gives the threshold in the Finding. At the equality threshold the cluster equation (1) has, writing \(\Delta=\pi+u\), the expansion
\[
\dot u=\frac{2B(N-1)}{N^2}u^3+O(u^5),
\]
whose positive cubic coefficient rules out Lyapunov stability. Below threshold the positive relative eigenvalue already rules it out. At every strict stability point all non-rotational modes are negative, implying local exponential attraction to the equilibrium circle by the standard normal-hyperbolicity theorem.

At full synchrony, differentiation gives \(N-1\) transverse eigenvalues \(-(A+B)<0\), so synchrony is always attracting. Exactly \(N\) labelled choices of a solitary oscillator exist whenever its threshold is met, yielding the claimed count.

## Verification

The accompanying `verify.py` differentiates every pair and every repeated-index triadic term independently using exact rational arithmetic. For \(238\) finite choices of size, partition and coupling, it verifies the zero phase mode, all internal eigenmodes, and the relative quotient eigenvalue in (3)–(4). It also evaluates the exact rational thresholds for sizes three through six and checks that the denominator changes sign at seven. Execute `python verify.py` with a standard Python interpreter. These finite computations corroborate, but do not replace, the all-size argument, the nonlinear equality-boundary analysis, or the classification of the invariant two-cluster dynamics.

## Relationship to prior work

Sharma, Suman, Anvari, Shrimali, del Genio and Jalan (first public 2026-07-07; arXiv:2611.09564v1, Section 2.1, equation (1)) introduce precisely this repeated-index three-body interaction over globally coupled triples, and investigate network-dependent synchronization transitions for nonidentical frequencies numerically. They do not claim a finite-size all-two-cluster stability classification, a sharp six-site limit or exact equality-boundary instability.

A related published result titled *Exact finite-size stability and re-entrant loss of antipodal states under distinct-triad Kuramoto coupling* analyzes instead the **ordered-distinct** interaction \(\sin(\theta_j+\theta_\ell-2\theta_i)\), whose mean-field term is \(Z_1^2e^{-2i\theta_i}\) rather than the present \(Z_2\overline Z_1 e^{-i\theta_i}\). Its strict finite-size stability windows and even stable seven-oscillator examples do not imply the present complete-graph repeated-index cutoff. Conversely the present cutoff does not imply its result. The distinct-index and repeated-index models cannot be identified by merely rescaling coefficients or discarding repeated-index summands: their phase arguments and Jacobian spectra differ.

Carballosa et al. (arXiv:2308.05406) and Kovalenko et al. (arXiv:2107.03818) also use the symmetric \(\sin(\theta_j+\theta_\ell-2\theta_i)\) coupling, generally with natural-frequency distributions. León, Muolo, Hata and Nakao (arXiv:2309.09265, Eq. (1)) examine two-cluster phase diagrams for a distinct **symmetric** triadic \(\sin(\theta_j+\theta_\ell-2\theta_i)\) interaction (with phase lags). Xu and Skardal (arXiv:2010.02300) examine pure higher-order clustering in the thermodynamic-limit setting. The present claim is only the exact finite-dimensional two-cluster classification in the specified asymmetric coupling. It does not claim novelty of the Kuramoto reduction, triadic synchronization, antipodal clustering or representation by complex order parameters.

## Limitations

Only equilibria with one or two synchronized populations are classified. More complicated equilibria, periodic orbits, multicluster attractors, basins and robustness under heterogeneous frequencies or graph sparsification are not addressed. The proof depends on repeated-index all-to-all three-body summation exactly as written, and on strictly positive pairwise and triadic gains. This is not a full census of all attractors. Historical priority remains provisional because not every related higher-order interaction paper can be exhaustively inspected. Independent mathematical validation has not been performed.

## References

1. A. Sharma, A. Suman, M. Anvari, M. D. Shrimali, C. I. del Genio, S. Jalan, *Synchronization transitions in Kuramoto oscillators with mixed interactions*, *European Physical Journal Special Topics* 235, 7741–7748 (published online 2026-07-07), DOI: https://doi.org/10.1140/epjs/s11734-026-02482-w; lawful open preprint https://arxiv.org/html/2611.09564v1.
2. *Exact finite-size stability and re-entrant loss of antipodal states under distinct-triad Kuramoto coupling*, 2026-11-08, https://github.com/published-finding corpus/2026.
3. A. Carballosa et al., *Cluster States and π-Transition in the Kuramoto Model with Higher Order Interactions*, arXiv:2308.05406, https://arxiv.org/abs/2308.05406.
4. C. Xu and P. S. Skardal, *Spectrum of extensive multiclusters in the Kuramoto model with higher-order interactions*, *Physical Review Research* 3, 013013 (2021), arXiv:2010.02300, https://arxiv.org/abs/2010.02300.
5. I. León, R. Muolo, S. Hata and H. Nakao, *Higher-order interactions induce anomalous transitions to synchrony*, *Chaos* 34, 013105 (2024), https://arxiv.org/pdf/2309.09265.
6. K. Kovalenko et al., *Contrarians Synchronize beyond the Limit of Pairwise Interactions*, *Physical Review Letters* 127, 258301 (2021), arXiv:2107.03818, https://arxiv.org/abs/2107.03818.
