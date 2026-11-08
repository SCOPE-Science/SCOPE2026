# Exact finite-size stability and re-entrant loss of antipodal states under distinct-triad Kuramoto coupling

## Finding

For every integer \(n\geq3\), consider \(n\) identical phase oscillators on the complete graph, with attractive pairwise coupling \(\sigma>0\) and attractive, **ordered-distinct** triadic coupling \(\delta>0\). For a nontrivial partition into \(p\) vertices at phase \(0\) and \(q=n-p\) vertices at phase \(\pi\), interchange the two parts if necessary so \(p>q\geq1\), and set \(S=p-q>0\). Equal parts, possible for even \(n\), are always linearly unstable modulo common rotation.

The antipodal equilibrium circle is locally exponentially attracting modulo common rotation **if and only if** \(S^2>n\), \(\delta>\delta_{\mathrm{lo}}\), and, when \(S^2<n+S\), also \(\delta<\delta_{\mathrm{hi}}\), where
\[
\delta_{\mathrm{lo}}=\frac{\sigma n(n-2)}{2S^2},\qquad
\delta_{\mathrm{hi}}=\frac{\sigma S(n-2)}{2(n+S-S^2)}.
\]
When \(S^2\geq n+S\), no upper bound is needed. Every strict failure of a threshold away from its equality boundary produces a positive transverse eigenvalue, except that \(S^2\leq n\) admits no exponentially attracting antipodal state at any positive \(\delta\). The equality boundaries have zero transverse eigenvalues and are not assigned a nonlinear stability classification.

In particular, **re-entrant attraction** (a nonempty finite open window of \(\delta\) followed by renewed linear instability for larger \(\delta\)) occurs precisely for \(n<S^2<n+S\). This holds for infinitely many complete-graph sizes: choose any odd \(S\geq3\) and odd \(n\) satisfying \(S^2-S<n<S^2\), with \(p=(n+S)/2\), \(q=(n-S)/2\). For instance, with \(n=7\), \(p=5\), \(q=2\), the stability interval is exactly
\[
\frac{35\sigma}{18}<\delta<\frac{15\sigma}{2}.
\]
At \(\delta=2\sigma\), there are exactly \(29\) distinct exponentially attracting antipodal-or-synchronous equilibrium circles; at \(\delta=8\sigma\), there are exactly \(8\), all counted modulo global rotation (the missing \(21\) are the antipodal states with a two-vertex minority). No assertion is made that these are all attracting invariant sets.

## Assumptions and scope

After removing the common natural frequency by a uniformly rotating reference frame, the system is
\[
\dot\theta_i=\frac{\sigma}{n-1}\sum_{j\ne i}\sin(\theta_j-\theta_i)
+\frac{\delta}{(n-1)(n-2)}\sum_{\substack{j\ne i}}\sum_{\substack{k\ne i\\k\ne j}}
\sin(\theta_j+\theta_k-2\theta_i),\quad i=1,\ldots,n.
\]
The inner two summations run over ordered pairs of distinct neighbours, so each unordered pair occurs twice. The underlying phase space is the torus \((\mathbb R/2\pi\mathbb Z)^n\). Equilibria with phase values \(0\) and \(\pi\) are considered modulo the continuous action \(\theta_i\mapsto\theta_i+c\) for all \(i\). Local exponential attraction means an exponentially decaying distance to this equilibrium circle, uniformly for all sufficiently close configurations. The theorem concerns these prescribed antipodal equilibrium circles; it does not classify other fixed points or periodic, chaotic or chimera attractors. No random frequencies, phase lags or repeated-index triangle terms are permitted.

Let \(d=n-1\), \(s_i=1\) on the majority part and \(s_i=-1\) on the minority part; then \(S=\sum_i s_i\). Denote the distinct eigenvalues of the Jacobian by \(\lambda_+\), \(\lambda_-\), and \(\lambda_{\mathrm{rel}}\), with multiplicities described next.

## Proof

Every prescribed antipodal pattern is an equilibrium because all sine arguments are integer multiples of \(\pi\). Differentiating the actual ordered-pair summations gives, for distinct \(i,j\),
\[
J_{ij}=\frac{\sigma}{d}s_i s_j+
\frac{2\delta}{d(d-1)}s_j\sum_{k\ne i,j}s_k
=\frac{\sigma}{d}s_i s_j+
\frac{2\delta}{d(d-1)}s_j(S-s_i-s_j),
\]
and \(J_{ii}=-\sum_{j\ne i}J_{ij}\). The factor \(2\) in the derivative is necessary because \(j\) may occupy either position in an ordered triad.

The Jacobian preserves: (i) the zero-sum fluctuations within the \(p\)-part, dimension \(p-1\); (ii) the zero-sum fluctuations within the \(q\)-part, dimension \(q-1\); and (iii) the two-dimensional space of vectors constant within each part. Directly applying the row-sum formula yields
\[
\lambda_+=-\frac{\sigma S}{d}+\frac{2\delta(2p-S^2)}{d(d-1)}\quad (p-1\text{ times}),
\]
\[
\lambda_- =\frac{\sigma S}{d}+\frac{2\delta(2q-S^2)}{d(d-1)}\quad (q-1\text{ times}),
\]
\[
\lambda_{\mathrm{rel}}=\frac{\sigma n}{d}-\frac{2\delta S^2}{d(d-1)}\quad (1\text{ time}),
\]
and a single zero eigenvalue from rigid rotation. If \(q=1\), the displayed \(\lambda_-\) has multiplicity zero and is not a stability condition. The three non-neutral formulas and their multiplicities therefore constitute a complete spectrum for every partition.

Suppose first that \(p>q\). Necessarily \(\lambda_{\mathrm{rel}}<0\) exactly when \(\delta>\delta_{\mathrm{lo}}\). At this lower crossing one computes
\[
\lambda_+(\delta_{\mathrm{lo}})=\frac{\sigma(n+S)}d\left(\frac{n}{S^2}-1\right),\qquad
\lambda_-(\delta_{\mathrm{lo}})=\frac{\sigma(n-S)}d\left(\frac{n}{S^2}-1\right).
\]
If \(S^2\leq n\), then \(\lambda_+\) is nonnegative at the relative crossing. Because \(2p=n+S>S^2\), \(\lambda_+\) rises strictly with \(\delta\). Hence it cannot be negative whenever \(\lambda_{\mathrm{rel}}<0\), so exponential attraction is impossible.

If \(S^2>n\), both internal eigenvalues present at the lower crossing are strictly negative. Furthermore \(2q=n-S<S^2\), so \(\lambda_-\) decreases with \(\delta\) and remains negative thereafter. The \(p\)-internal eigenvalue \(\lambda_+\) decreases (or stays strictly negative) if \(S^2\geq n+S\). In the complementary case \(n<S^2<n+S\), it increases and first reaches zero precisely at \(\delta_{\mathrm{hi}}\). This upper value exceeds the lower one because
\[
\delta_{\mathrm{hi}}-\delta_{\mathrm{lo}}=
\frac{\sigma(n-2)(n+S)(S^2-n)}{2S^2(n+S-S^2)}>0.
\]
Thus every strict threshold and the three exhaustive sign conditions follow. Since all nonzero eigenvalues have negative real part exactly within the claimed region, standard local stability of smooth flows transverse to the rotationally neutral equilibrium circle proves local exponential attraction. Outside the strict window, a positive transverse eigenvalue proves linear instability; at a threshold equality the linearization is nonhyperbolic, which requires separate nonlinear analysis.

If \(p=q\), then \(S=0\) and \(\lambda_{\mathrm{rel}}=\sigma n/(n-1)>0\) for all \(\delta>0\), proving instability. The completely synchronized circle, excluded from the nontrivial-partition formulas, is attracting because its \(n-1\) transverse eigenvalues all equal \(-n(\sigma+2\delta)/(n-1)<0\).

For fixed \(n\), each subset of \(q\) labelled oscillators specifies one antipodal equilibrium circle with minority size \(q<p\), and different such subsets give different circles modulo common rotation. Thus the number of **linearly exponentially attracting antipodal-or-synchronous circles**, not necessarily the number of all attractors, is
\[
1+\sum_{q=1}^{\lfloor(n-1)/2\rfloor}\binom nq
\mathbf1\left\{S_q^2>n,\ \delta>\frac{\sigma n(n-2)}{2S_q^2},\ \bigl[S_q^2\geq n+S_q\ \text{or}\ \delta<\frac{\sigma S_q(n-2)}{2(n+S_q-S_q^2)}\bigr]\right\},
\qquad S_q=n-2q.
\]
The upper denominator is used only when it is positive. For \(n=7\), the only eligible nontrivial minority sizes are \(q=1\) and \(q=2\). The former has \(S=5\) and requires \(\delta>7\sigma/10\), without an upper bound. The latter has \(S=3\) and the claimed finite window. Therefore the two stated counts are \(1+\binom71+\binom72=29\) and \(1+\binom71=8\).

## Verification

The standalone `verify.py` uses exact rational arithmetic to construct Jacobians by differentiating **every ordered distinct triple** directly. It checks the rotational eigenvector, all independent internal difference eigenvectors and a cross-cluster eigenvector against the displayed eigenvalues. Across \(504\) finite configurations and rational coupling choices, it also compares eigenvalue signs with the proposed sharp thresholds. It checks both exact endpoints for the seven-node re-entrant example, the two orbit counts, and numerical derivatives of the original nonlinear vector field for three configurations. The program ran successfully with Python's standard library. These checks are finite corroborations, not a replacement for the proof for arbitrary \(n\).

Run with `python verify.py` from a directory containing this file and `verify.py`.

## Relationship to prior work

Wang, Zhu, Qi and Liu (arXiv:2603.14950, first posted 2026-03-16) introduce the identical normalized ordered-distinct-triad model on a cyclic ring and analyze twisted states and frequency heterogeneity. At odd \(n\) and full interaction range \(r=(n-1)/2\), their ring is exactly the complete graph above. The present theorem takes the separate homogeneous-frequency limit and classifies **all antipodal two-population equilibria**, including exact finite-size and re-entrant stability windows, rather than twisted states.

Zhang, Skardal, Battiston, Petri and Lucas (arXiv:2309.16581; *Science Advances*, 2024) develop mixed pairwise/triadic Kuramoto models and report two-cluster states, particularly for wider-range ring coupling. They do not claim the complete-graph antipodal finite-size sign classification or the \(29\)-to-\(8\) exact transition. Wang et al. (arXiv:2506.06791 and arXiv:2510.13321) study non-twisted versus twisted basins and quasipotentials; their primary analyses concern numerical landscapes or twisted states.

Carballosa et al. (arXiv:2308.05406) analyze mixed pairwise/triadic globally coupled models for distributed natural frequencies and cluster transitions using mean-field methods, not these exact distinct-index finite-dimensional Jacobian windows. Tanaka and Aoyagi (arXiv:1105.0064), Skardal and Arenas (arXiv:1903.12131), and Xu and Skardal (Phys. Rev. Research 3, 013013, 2021) establish important triadic cluster and extensive multistability phenomena but use pure-triad or thermodynamic-limit settings in their main stability analyses. Kovalenko et al. (*Phys. Rev. Lett.* 127, 258301, 2021) established higher-order-induced two-cluster synchronization, especially for negative pairwise coupling. Their Eq. (1) uses unrestricted indices in the triadic double sum (including repeated indices), unlike the ordered-distinct finite system here, and they do not present the claimed exact all-bipartition stability windows. Familiar rotation reduction and invariant-cluster eigenspaces are standard methods and are not claimed as new. The evidence supports a specific finite-size classification, not a global claim of unprecedented cluster behavior.

## Limitations

The theorem addresses linear and local exponential stability only for antipodal cluster equilibria, not their global basins, all equilibria, stochastic switching, twisted patterns, or general sparse hypergraphs. At the exact lower and upper boundaries, center-manifold behavior is not classified. The normalization insists on ordered **distinct** neighbors; changing it to allow repeated indices changes finite-size coefficients. A full historical priority guarantee is not available: the higher-order coupling literature is extensive, and equivalent finite-size formulas could appear in older or unindexed work. The observed number of stable antipodal states is not the total attractor count.

## References

1. Z. Wang, J. Zhu, W. Qi and X. Liu, *Frequency Heterogeneity can Promote Order yet Undermine Stability in Kuramoto Networks with Higher-Order Interactions*, arXiv:2603.14950 (first public 2026-03-16), https://arxiv.org/abs/2603.14950.
2. Y. Zhang, P. S. Skardal, F. Battiston, G. Petri and M. Lucas, *Deeper but smaller: Higher-order interactions increase linear stability but shrink basins*, *Science Advances* 10, eado8049 (2024), arXiv:2309.16581, https://doi.org/10.1126/sciadv.ado8049.
3. Z. Wang, W. Qi, J. Zhu and X. Liu, *How do higher-order interactions shape the energy landscape?*, arXiv:2506.06791 (2025), https://arxiv.org/abs/2506.06791.
4. Z. Wang, J. Zhu and X. Liu, *Moderate Higher-Order Interactions Enhance Stability While Preserving Basin Structure*, arXiv:2510.13321 (2025), https://arxiv.org/abs/2510.13321.
5. A. Carballosa, A. P. Muñuzuri, S. Boccaletti, A. Torcini and S. Olmi, *Cluster States and π-Transition in the Kuramoto Model with Higher Order Interactions*, arXiv:2308.05406 (2023), https://arxiv.org/abs/2308.05406.
6. T. Tanaka and T. Aoyagi, *Multistable attractors in a network of phase oscillators with three-body interactions*, *Phys. Rev. Lett.* 106, 224101 (2011), https://arxiv.org/abs/1105.0064.
7. P. S. Skardal and A. Arenas, *Abrupt Desynchronization and Extensive Multistability in Globally Coupled Oscillator Simplexes*, *Phys. Rev. Lett.* 122, 248301 (2019), https://arxiv.org/abs/1903.12131.
8. C. Xu and P. S. Skardal, *Spectrum of extensive multiclusters in the Kuramoto model with higher-order interactions*, *Phys. Rev. Research* 3, 013013 (2021), https://doi.org/10.1103/PhysRevResearch.3.013013.
9. K. Kovalenko et al., *Contrarians Synchronize beyond the Limit of Pairwise Interactions*, *Phys. Rev. Lett.* 127, 258301 (2021), https://doi.org/10.1103/PhysRevLett.127.258301.
