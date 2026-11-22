# Spectral-order migration of optimal two-leader placements on weighted double stars

## Finding
Let a weighted double-star tree have two adjacent hubs, with \(p\ge2\) unit-conductance pendant edges incident to the first hub and \(q\ge2\) unit-conductance pendant edges incident to the second hub. The hub-to-hub edge has conductance \(t>0\). Exactly two vertices are held at zero (perfect leaders). For the follower set \(F\) and its positive-definite grounded combinatorial Laplacian \(L_{FF}\), minimize
\[
\Phi_r(S)=\operatorname{tr}\bigl(L_{FF}(S)^{-r}\bigr),\qquad |S|=2,\quad r\ge1,
\]
over **all** unordered two-vertex sets, with real spectral order \(r\).

Set \(N=p+q\), \(m=\min\{p,q\}\), and
\[
\alpha_\pm(m,t)=\frac12\left(1+\frac{m}{t+1}\ \pm\sqrt{\left(1+\frac{m}{t+1}\right)^2-\frac4{t+1}}\right),\qquad
T_r(m,t)=\alpha_+(m,t)^r+\alpha_-(m,t)^r.
\]
Then the **exact unrestricted optimum** is
\[
\boxed{\min_{|S|=2}\Phi_r(S)=N-2+\min\{2,T_r(m,t)\}.}
\]
All optimal pairs are completely classified. If \(T_r(m,t)>2\), the unique optimum consists of both hubs. If \(T_r(m,t)<2\), optimal pairs consist of the hub incident to the larger number of leaves and any one leaf attached to the opposite, smaller side; when \(p=q\), either orientation is optimal. If \(T_r(m,t)=2\), both hubs and all those cross-hub–leaf pairs are exactly the optimizers. No leaf–leaf or same-side hub–leaf pair ever ties for the optimum.

For each \(m\ge2\) and \(r\ge1\), there is a unique critical conductance \(t_r(m)>0\) satisfying \(T_r(m,t_r(m))=2\). The two-hub optimum occurs below this threshold, the cross-hub–leaf optimum above it, with both types at equality. The threshold is **strictly increasing in spectral order** and obeys
\[
\boxed{t_1(m)=m-1,\qquad
 t_2(m)=m-2+\sqrt{(m-1)^2+m^2},\qquad
 \lim_{r\to\infty}\frac{t_r(m)}r=\frac{m-1}{\log2}.}
\]
Thus for every \(m\ge2\), the nonempty open interval \(t_1(m)<t<t_2(m)\) gives **different, disjoint, unique-orbit optimal leader-placement types** for first and second inverse spectral moments: first order chooses the cross-hub–leaf type, while second order chooses both hubs. For example, with \(p=q=2\) and \(t=2\), the first-order optimum is \(11/3<4\) (cross-hub–leaf), whereas the second-order cross-hub–leaf cost is \(37/9>4\), so both hubs are second-order optimal.

## Assumptions and scope
The graph has \(p+q+2\) vertices and every leaf edge has conductance exactly one; the only adjustable edge parameter in the theorem is the **given**, not optimized, positive hub conductance \(t\). Every eligible set contains exactly two distinct perfectly grounded (noise-free) vertices; the same pair is used to define \(L_{FF}(S)\). There are \(N=p+q\) ungrounded vertices. All eigenvalues of every grounded Laplacian are positive, so its negative real powers are defined by standard spectral calculus. The objective is unnormalized; multiplying by a positive constant does not change the argmin. The second spectral moment \(r=2\) is the inverse-square criterion used, for instance, with position-noise variance in proportionally damped second-order leader-following systems. The result is a mathematical statement about the stated criterion and does not assume a universally applicable dynamical noise normalization.

## Proof
**1. Spectrum with a grounded hub and an opposite-side leaf.** Ground the first hub and one leaf at the second hub, which has \(a\ge2\) leaves total. The leaves on the grounded hub's side are isolated follower blocks of Laplacian value one. The remaining block contains the second hub and its \(a-1\) ungrounded leaves, with grounded Laplacian
\[
B_a(t)=\begin{pmatrix}t+a&-\mathbf1_{a-1}^{\mathsf T}\\-\mathbf1_{a-1}&I_{a-1}\end{pmatrix}.
\]
Its Schur complement at the hub is \(t+1\), so
\[
 B_a(t)^{-1}=\operatorname{diag}(0,I_{a-1})+\frac{1}{t+1}\mathbf1_a\mathbf1_a^{\mathsf T}.
\]
There are \(a-2\) eigenvalues one (the differences between ungrounded leaves). The two remaining positive eigenvalues have sum \(1+a/(t+1)\) and product \(1/(t+1)\): precisely \(\alpha_+(a,t)\) and \(\alpha_-(a,t)\). The other grounded-hub-side leaves also yield eigenvalue one. In total the follower inverse has \(N-2\) eigenvalues one and these two special eigenvalues, giving
\[
\Phi_r(\text{cross-hub--leaf on side }a)=N-2+T_r(a,t).
\]
For \(a\ge2\), the quadratic at one is \(-(a-1)/(t+1)<0\), so \(\alpha_+(a,t)>1>\alpha_-(a,t)>0\).

**2. Every other hub–leaf orbit is strictly dominated.** If the second pinned vertex is instead a leaf adjacent to the *grounded* hub and the other (free) hub has \(a\) leaves, its inverse block is
\[
\operatorname{diag}(0,I_a)+t^{-1}\mathbf1_{a+1}\mathbf1_{a+1}^{\mathsf T}.
\]
Its special eigenvalues have sum \(1+(a+1)/t\), product \(1/t\), and its total inverse again has \(N-2\) unit eigenvalues. Compare the two special pairs for this configuration and for a cross-hub–leaf pinned vertex at the opposite hub. The special largest eigenvalue is strictly greater in the same-side configuration, because its positive rank-one matrix contains a principal \(a\)-by-\(a\) matrix with coefficient \(1/t>1/(t+1)\), and positive-matrix Perron monotonicity applies. Its special eigenvalue sum is also strictly greater: \(1+(a+1)/t>1+a/(t+1)\). For two nonnegative two-vectors, larger maximum and larger total imply weak majorization; every increasing convex power \(x\mapsto x^r\), \(r\ge1\), has at least as large a sum, strictly here. Thus each same-side hub–leaf pair is worse than the corresponding cross-hub–leaf pair. Likewise, for fixed \(t\), increasing the opposite-side leaf count \(a\) strictly raises both the largest special eigenvalue and the special eigenvalue sum. Hence \(T_r(a,t)\) is strictly increasing with \(a\), and the better cross-hub–leaf orientation leaves the **smaller** side ungrounded at its hub.

For completeness, the weak-majorization fact used here follows directly by sorting both pairs in descending order: transferring mass from the smaller component to the larger component cannot decrease the sum of a convex function, and increasing either component cannot decrease an increasing function. This argument applies also at \(r=1\), where the strict total-sum inequality suffices.

**3. Leaf–leaf pairs cannot beat both hubs.** Grounding the two hubs leaves precisely \(N\) independent unit eigenvalues in \(L_{FF}^{-1}\), so \(\Phi_r(\text{two hubs})=N\). For two pinned leaves on the same hub's side, with the opposite hub incident to \(b\ge2\) leaves, elementary grounded-tree resistance or a two-hub Schur complement gives
\[
\Phi_1(\text{same-side leaves})=N+\frac{N-4}{2}+\frac{b+1}{t}>N.
\]
For one pinned leaf on each side, the corresponding calculation gives
\[
\Phi_1(\text{opposite-side leaves})=N+\frac{t(N-4)+N-2}{2t+1}>N.
\]
To see these are complete calculations, eliminate all ungrounded leaves: if \(k_A,k_B\) leaves are pinned at the respective hubs and neither hub is pinned, the residual two-hub Schur matrix is
\[
\begin{pmatrix}t+k_A&-t\\-t&t+k_B\end{pmatrix},\qquad k_A+k_B=2.
\]
Undoing the Schur elimination gives the displayed inverse diagonal sums. Since \(N\ge4\), both expressions are strictly greater than \(N\). For any positive inverse eigenvalues \(z_1,\ldots,z_N\), Jensen's inequality for real \(r\ge1\) gives
\[
\sum_{i=1}^N z_i^r\ge N\left(\frac1N\sum_{i=1}^Nz_i\right)^r.
\]
Thus every leaf–leaf pair has \(\Phi_r>N\) for **all** \(r\ge1\). The eight pair orbits have now all been compared: hub–hub, four hub–leaf orbits, and three leaf–leaf orbits. Only hub–hub and the specified cross-hub–leaf orbits can win, proving the exact objective and complete optimizer classification.

**4. Unique threshold and its strict order monotonicity.** For fixed \(m\ge2\), \(T_r(m,t)\) decreases strictly with \(t>0\): its nontrivial part is \(\operatorname{tr}(B_m(t)^{-r})-(m-2)\), and differentiation of the trace spectral function gives
\[
\frac{\partial}{\partial t}\operatorname{tr}(B_m(t)^{-r})
=-r\bigl(B_m(t)^{-r-1}\bigr)_{11}<0.
\]
As \(t\downarrow0\), the special eigenvalues tend to the positive roots of \(x^2-(m+1)x+1=0\), whose sum is \(m+1>2\). The convex power-mean inequality therefore gives \(T_r(m,0+)\ge2((m+1)/2)^r>2\) for every \(r\ge1\). As \(t\to\infty\), the special pair converges to \((1,0)\), so \(T_r\to1\). Hence there is exactly one root of \(T_r=2\) for every \(r\ge1\), with the indicated winner on each side.

For fixed \(t>0\), the function \(f(r)=\alpha_+^r+\alpha_-^r\) is strictly convex on \([0,\infty)\), satisfies \(f(0)=2\), has \(f'(0)=\log(\alpha_+\alpha_-)=-\log(t+1)<0\), and diverges as \(r\to\infty\) because \(\alpha_+>1\). Consequently, its unique positive return to level two is crossed with strictly positive derivative. At a threshold \(t_r(m)\), increasing spectral order makes \(T_r>2\); restoring the equality requires strictly increasing \(t\). Thus \(r\mapsto t_r(m)\) is strictly increasing.

At \(r=1\), the equality \(1+m/(t+1)=2\) gives \(t_1=m-1\). At \(r=2\), the quadratic identity \(\alpha_+^2+\alpha_-^2=(1+m/(t+1))^2-2/(t+1)\) yields \((t+1)^2-2(m-1)(t+1)-m^2=0\); its unique positive root is the stated \(t_2\). Strict order monotonicity implies \(t_1<t_2\), giving the disagreement interval.

Finally fix \(m\) and let \(r\to\infty\). Necessarily \(t_r\to\infty\), for otherwise \(\alpha_+>1\) would make \(T_r\) diverge. With \(s=t+1\), the quadratic gives uniformly for large \(s\)
\[
\alpha_+=1+\frac{m-1}{s}+O_m(s^{-2}),\qquad \alpha_-=s^{-1}+O_m(s^{-2}).
\]
At the threshold, \(\alpha_-^r\to0\), so \(r\log\alpha_+\to\log2\). The expansion and positivity first imply \(s=\Omega_m(r)\); then the quadratic remainder multiplied by \(r\) is negligible, yielding \(r(m-1)/s\to\log2\). Since \(s-t=1\), the asserted asymptotic follows. This completes the proof. \(\square\)

## Verification
The standalone checker `verify.py` uses exact rational matrix inverses to compare every two-leader pair against the \(r=2\) formula for 45 parameter choices (1,290 exact pair inversions). Independently it uses numerical grounded-Laplacian eigenvalues to compare the full optimum against the continuous-order formula in 1,280 parameter-and-order instances, spanning 5,960 distinct leader-pair spectra. It also numerically checks 96 order-threshold relationships. Running `python verify.py` with `numpy` installed prints `VERIFY_OK exact_parameter_instances=45 exact_pair_inversions=1290 continuous_parameter_order_instances=1280 leader_sets=5960 threshold_checks=96`. The checker exercises finite ranges only; the unlimited claims follow from the proof, not from enumeration.

## Relationship to prior work
Lin, Fardad and Jovanović [1] formulate optimal noise-free leader selection using \(\operatorname{tr}(L_{FF}^{-1})\) and develop relaxation/greedy methods, not an all-spectral-order two-hub classification. Clark, Bushnell and Poovendran [2] study leader selection under link noise with supermodularity, a distinct noise setting. Siami and Motee [3] investigate first- and second-order disturbance propagation in *ungrounded* networks, but do not classify two perfectly pinned leaders on weighted double stars. Fitch and Leonard [5] develop joint centrality using ordinary and squared *full-Laplacian* pseudoinverses, but the leader-selection performance minimized in their noise-free model is the first grounded inverse moment; they give explicit path and cycle placements, not the real-order double-star thresholds. The publicly available result *Exact two-leader coherence transition on weighted double stars* [4] gives the first-order, \(r=1\), classification on exactly the same graph, with the bridge parameter expressed as a resistance. That previously known endpoint agrees with \(t_1=m-1\) after taking the reciprocal. It does **not** imply the monotone positive-real-order threshold curve, the inverse-square boundary, the disagreement interval, or the large-order slope without the new spectral and order comparisons above. The novel claim is the complete order-dependent theorem, not the first-order special case or the generic Schur complement.

## Limitations
The theorem requires \(p,q\ge2\), positive unit leaf conductances, a single common positive hub conductance, exactly two perfectly grounded leaders, and spectral orders \(r\ge1\). It does not assert the optimizer classification for orders below one (indeed the Jensen step no longer applies), for finite-gain noisy leaders, arbitrary heterogeneous pendant weights, or simultaneous edge-weight optimization. The large-order asymptotic keeps \(m\) fixed. The literature comparison supports originality only against material actually inspected; inaccessible or unindexed specialized equivalent results remain a publication-priority risk. Numerical diagnostics neither prove an infinite theorem nor establish priority.

## References
[1] F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, first posted 2013-02-03, https://arxiv.org/abs/1302.0450.

[2] A. Clark, L. Bushnell and R. Poovendran, *A Supermodular Optimization Framework for Leader Selection under Link Noise in Linear Multi-Agent Systems*, arXiv:1208.0946, first posted 2012-08-04, https://arxiv.org/abs/1208.0946.

[3] M. Siami and N. Motee, *Fundamental Limits and Tradeoffs on Disturbance Propagation in Large-Scale Dynamical Networks*, arXiv:1403.1494, first posted 2014-03-06, https://arxiv.org/abs/1403.1494.

[4] *Exact two-leader coherence transition on weighted double stars*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-two-leader-coherence-transition-on-weighted-double-stars--21774459d1f0.

[5] K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first posted 2014-07-07, https://arxiv.org/abs/1407.1569.
