# A sharp bridge-barbell antiphase threshold in the asymmetric mixed-order Kuramoto flow

## Finding

For the identical-frequency mixed pairwise/three-body Kuramoto flow defined below, let \(N=2h\ge4\) and take its pairwise graph to be the **barbell** formed from two disjoint cliques of order \(h\) joined by one edge. Set the phases of all oscillators in one clique to \(0\) and all those in the other to \(\pi\). This balanced antipodal configuration is an equilibrium modulo common rotation.

**The sharp result** is that this equilibrium is locally exponentially attracting modulo common rotation if and only if
\[
\boxed{\frac{K_2}{K_1}>\frac{2h^2}{(h^2-h+1)(h^2-2h+2)}.}
\]
Below equality it has a strictly positive transverse eigenvalue; at equality it has a non-rotational zero eigenvalue, so it is not exponentially attracting. The threshold is \(2h^{-2}(1+O(h^{-1}))=8N^{-2}(1+O(N^{-1}))\).

For context, the complete graph with the **same** asymmetric unrestricted-index three-body interaction does not possess any locally exponentially attracting non-synchronous antipodal state once \(N\ge7\). This follows from the complete-graph spectrum reproduced below; the six-oscillator ceiling is prior work and is **not** claimed as new here. Thus for every even \(N\ge8\), altering only the pairwise connectivity from complete to a single-bridge barbell restores an exponentially attracting balanced antipodal state, at a sharp triadic coupling threshold that vanishes quadratically with network order. The new contribution is the **barbell threshold and topology contrast**.

## Assumptions and scope

Let \(G\) be a connected simple undirected graph with \(N\ge2\) labelled vertices, adjacency matrix \(A\), and positive mean degree \(\bar d=N^{-1}\sum_{i,j}A_{ij}\). Remove the common natural frequency by passing to a co-rotating frame. The flow on the \(N\)-torus is
\[
\dot\theta_i=\frac{K_1}{\bar d}\sum_{j=1}^N A_{ij}\sin(\theta_j-\theta_i)
+\frac{K_2}{N^2}\sum_{j=1}^N\sum_{\ell=1}^N\sin(2\theta_j-\theta_\ell-\theta_i),
\qquad K_1,K_2>0.
\]
The two three-body indices are **unrestricted** and may coincide with each other or with \(i\). The interaction \(\sin(2\theta_j-\theta_\ell-\theta_i)\) is not the symmetric distinct-neighbour interaction \(\sin(\theta_j+\theta_\ell-2\theta_i)\). Altering that convention changes the Jacobian and the theorem. A phase configuration is *locally exponentially attracting modulo common rotation* when its circle of uniform phase translates is exponentially attracting in transverse distance. Only prescribed antipodal equilibria are classified, not all other invariant sets.

Write \(s_i=e^{i\theta_i}\in\{+1,-1\}\), \(m=N^{-1}\sum_i s_i\). For a perturbation \(\eta\), define \(\bar\eta=N^{-1}\sum_i\eta_i\) and \(s\!\cdot\!\eta=N^{-1}\sum_i s_i\eta_i\).

## Proof

**Step 1: exact linearization.** Each sine argument at an antipodal configuration is an integer multiple of \(\pi\), so all these configurations are equilibria. Differentiate the original *unrestricted* double sum; its cosine equals \(s_i s_\ell\), independent of \(j\). The triadic Jacobian action is exactly
\[
(J_2\eta)_i=K_2s_i\left(2m\bar\eta-\frac1N\sum_\ell s_\ell\eta_\ell-m\eta_i\right).
\]
The pairwise Jacobian is
\[
(J_1\eta)_i=\frac{K_1}{\bar d}\sum_j A_{ij}s_is_j(\eta_j-\eta_i).
\]
Both annihilate the constant vector. These identities are valid at every size, including \(N=2\).

**Step 2: complete-graph comparison (previously established, repeated to make the contrast self-contained).** Let \(P\) vertices have sign \(+1\) and \(Q=N-P\) have sign \(-1\); both are nonempty, and put \(m=(P-Q)/N\). The Jacobian preserves the \((P-1)\)-dimensional zero-sum fluctuations in the positive cluster, the \((Q-1)\)-dimensional corresponding negative-cluster space, and the two-dimensional cluster-constant space. The four eigenvalues, counting multiplicities, are
\[
\begin{aligned}
\lambda_+&=-m\left(\frac{NK_1}{N-1}+K_2\right),&\quad& P-1\text{ times},\\
\lambda_-&=m\left(\frac{NK_1}{N-1}+K_2\right),&& Q-1\text{ times},\\
\lambda_{\mathrm{rel}}&=\frac{NK_1}{N-1}+K_2(2m^2-1),&&1\text{ time},\\
\lambda_{\mathrm{rot}}&=0,&&1\text{ time}.
\end{aligned}
\]
The cluster-constant \(2\)-by-\(2\) block has row sums zero; its nonzero eigenvalue is its trace, giving \(\lambda_{\mathrm{rel}}\). Because the asymmetric three-body Jacobian need not be symmetric, the relative eigenvector need **not** be orthogonal to the rotational vector; only the eigenvalues and their transverse signs are required.

When \(P=Q\) and \(N\ge4\), the nonempty internal cluster spaces carry zero eigenvalues, precluding transverse exponential attraction. When \(N=2\), both cluster sizes are one, and there are no internal modes; the single transverse eigenvalue is \(2K_1-K_2\), so attraction holds precisely for \(K_2>2K_1\). For \(N\ge3\) and \(P\ne Q\), orient signs so \(P>Q\). If \(Q\ge2\), \(\lambda_->0\). Thus for \(N\ge3\) a potential attractor must have \(Q=1\). Then \(m=(N-2)/N\), \(\lambda_+<0\), and \(\lambda_{\mathrm{rel}}<0\) precisely when
\[
2(N-2)^2<N^2,\qquad
\frac{K_2}{K_1}>\frac{N^3}{(N-1)(-N^2+8N-8)}.
\]
For integers \(N\ge2\) the first inequality is equivalent to \(N\le6\). At equality the extra zero eigenvalue precludes exponential attraction, and below the threshold the positive relative eigenvalue gives instability. This supplies the needed complete-graph contrast. Its full finite-size classification is background, not the claimed new result.

**Step 3: exact barbell quadratic form.** Write the two clique means of a real perturbation \(v\) as \(\alpha,\beta\) and their bridge-endpoint deviations from their respective means as \(u,w\). Let \(\Delta=\alpha-\beta\). Because the antipodal partition is balanced, \(m=0\) and the full Jacobian is symmetric. Its negative quadratic form is
\[
-v^TJv=\frac{K_1}{\bar d}\left[h\sum_{i\in L}(v_i-\alpha)^2+h\sum_{j\in R}(v_j-\beta)^2-(\Delta+u-w)^2\right]+\frac{K_2h}{2}\Delta^2,
\]
where \(\bar d=(h^2-h+1)/h\). The within-clique complete-graph identity establishes the first two sums; the single cross-clique edge has negative cosine, hence the minus sign. The rank-one triadic contribution equals \(K_2(\sum_i s_iv_i)^2/N=K_2h\Delta^2/2\).

For fixed bridge deviations, the sharp zero-sum constraint yields
\[
h\sum_{i\in L}(v_i-\alpha)^2+h\sum_{j\in R}(v_j-\beta)^2\ge c(u^2+w^2)\ge\frac c2(u-w)^2,\qquad c=\frac{h^2}{h-1}>2.
\]
Both inequalities are attained by taking all nonbridge vertices of each clique to have identical deviations and setting \(u=-w\). Put \(z=u-w\); minimizing exactly over \(z\) gives
\[
\min_z\left\{\frac c2z^2-(\Delta+z)^2\right\}=-\frac{c}{c-2}\Delta^2.
\]
Consequently, the quadratic form is strictly positive for every nonconstant vector if and only if
\[
\frac{K_2h}{2}>\frac{K_1}{\bar d}\frac{c}{c-2},
\quad\text{equivalently}\quad
\frac{K_2}{K_1}>\frac{2h^2}{(h^2-h+1)(h^2-2h+2)}.
\]
Strict positivity implies all transverse eigenvalues are negative and hence local exponential attraction. If this inequality fails, the explicit sharpness choices produce a zero-energy nonconstant vector at equality and negative energy below; the latter gives a positive Jacobian eigenvalue by the variational principle. The uniform vector always has zero energy by rotational symmetry, completing the sharp classification.

**Step 4: new topology contrast.** On any \(K_N\) with \(N\ge7\), the previously established complete-graph spectrum in Step 2 rules out local exponential attraction for all nontrivial antipodal partitions. On the barbell with even \(N=2h\ge8\), Step 3 gives attraction for every ratio strictly exceeding its positive threshold. Division of the two degree-four polynomials in \(h\) yields the asymptotic ratio \(2h^{-2}(1+O(h^{-1}))\), proving the claimed scale and reversal.

## Verification

The bundled standalone `verify.py` constructs the Jacobian *from every summand* of the original nonlinear vector field using exact rational arithmetic; repeated three-body indices are included. As a background comparison, it checks rotational and within-cluster eigenvectors and the complete-graph inter-cluster eigenvalue for all \(2\le N\le11\) and every nontrivial partition, at two positive rational parameter pairs. It also checks the barbell signed-edge quadratic form, explicit sharp-threshold witness, and strict positive definiteness of the grounded negative Jacobian above threshold for \(h\in\{2,3,4,5,6,8\}\). Run from the same directory: `python verify.py`. This is finite corroboration only; the preceding algebra and exact minimization establish the claims at all stated sizes.

## Relationship to prior work

Sharma, Suman, Anvari, Shrimali, del Genio and Jalan introduced precisely the asymmetric unrestricted-index triadic model above in their 2026 paper, first published online **7 July 2026**. Their published study reports numerical finite-size and graph-density effects for Erdős–Rényi pairwise networks with distributed intrinsic frequencies; it does not give the sharp barbell stability threshold for identical frequencies. Their open arXiv version of 6 November 2026 permits inspection of the exact original equation, with the same asymmetric triadic indices.

Skardal and Arenas explicitly note the failure of stable multicluster memory states for the alternative asymmetric three-body phase-reduction term in a **pure three-node-simplex, distinct-index tensor** setting. This warning is important but does not imply instability in the present equation: the source uses an undirected triangle-adjacency tensor with no repeated indices or positive pairwise term, whereas the present global double sum includes repeated indices and thereby creates additional linearized effects. The exact all-index derivative in Step 1 and its rational tests directly resolve that distinction.

Mixed pairwise/triadic phase-cluster results by Carballosa et al., Kovalenko et al., and the published result *Exact finite-size stability and re-entrant loss of antipodal states under distinct-triad Kuramoto coupling* address related but non-equivalent models. In particular, that latter theorem uses **ordered-distinct symmetric** arguments \(\sin(\theta_j+\theta_k-2\theta_i)\), and obtains cluster-imbalance and upper-gain stability windows; those formulas do not apply to the asymmetric unrestricted-index model. Existing classical graph Laplacian methods motivate the exact quadratic minimization but do not by themselves supply either nonlinear model-specific threshold. The new claim is the sharp bridge-barbell criterion and its size-dependent comparison, not the previously established complete-graph ceiling, nor a claim that two-cluster oscillations are generally unknown.

## Limitations

The theorem is local, for exact identical intrinsic frequencies and undirected graph pairwise coupling, with strictly attractive gains and the printed asymmetric all-to-all triadic convention. It does not classify all stationary states, their global basins, limit cycles, nonzero frequency dispersion, stochastic perturbations, general sparse graphs, or nonlinear stability at the extra-zero-eigenvalue threshold. The finite checker is not an all-size proof. Although several closely related published results were inspected and compared by their equations and implications, a definitive exhaustive historical-priority guarantee is unavailable.

## References

1. A. Sharma, A. Suman, M. Anvari, M. D. Shrimali, C. I. del Genio and S. Jalan, *Synchronization transitions in Kuramoto oscillators with mixed interactions*, *European Physical Journal Special Topics* 235, 7741–7748 (2026), first published 7 July 2026, DOI: https://doi.org/10.1140/epjs/s11734-026-02482-w; accessible full-text preprint arXiv:2611.09564v1 (6 November 2026), https://arxiv.org/html/2611.09564v1.
2. A. Carballosa et al., *Cluster States and π-Transition in the Kuramoto Model with Higher Order Interactions*, arXiv:2308.05406 (2023), https://arxiv.org/abs/2308.05406.
3. K. Kovalenko et al., *Contrarians Synchronize beyond the Limit of Pairwise Interactions*, *Physical Review Letters* 127, 258301 (2021), arXiv:2107.03818, https://arxiv.org/abs/2107.03818.
4. *Exact finite-size stability and re-entrant loss of antipodal states under distinct-triad Kuramoto coupling*, published published-finding corpus mathematical finding, 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-finite-size-stability-and-re-entrant-loss-of-antipodal-sta--ec86172a8434.
5. P. S. Skardal and A. Arenas, *Memory selection and information switching in oscillator networks with higher-order interactions*, *Journal of Physics: Complexity* 2, 015003 (2021), first published online 30 November 2020, accessible primary manuscript https://webs-deim.urv.cat/~alexandre.arenas/publicacions/pdf/memoryosc.pdf (Section II, model conventions).
