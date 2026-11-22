# Two-contact isotropic gossip favors path boundaries, unlike spectral-gap-optimal sampling

## Finding
Consider independent edge selections from a fixed probability distribution, with one exact equal-weight pairwise average at each contact. The problem is to choose the same edge distribution for **two contacts** so as to minimize the expected total squared disagreement from an isotropic random initial opinion field.

For a finite connected simple graph \(G\) with \(n\ge2\) vertices and \(m\) edges, let \(p_e\ge0\) and \(\sum_e p_e=1\). Let \(L(G)\) be its line graph and put
\[
B_G=I_m+\frac14A_{L(G)}.
\]
If \(x_0\) has common mean \(\mu\mathbf1\) and covariance \(I_n\), then for two independently sampled edges \(E_1,E_2\),
\[
\boxed{\mathbb E\|x_2-\bar x_0\mathbf1\|_2^2=n-3+p^{\mathsf T}B_Gp.}
\]
For one contact the corresponding expectation is \(n-2\), independent of \(p\). The matrix \(B_G\) is strictly positive definite on every simple graph, so the two-contact minimizer is **unique**. If \(q=B_G^{-1}\mathbf1\) is positive entrywise, this minimizer is \(p^*=q/(\mathbf1^{\mathsf T}q)\). For general graphs the unique solution is characterized by the nonnegative-simplex KKT conditions in the proof.

On the path \(P_{m+1}\), with edges indexed consecutively by \(i=1,\ldots,m\), define \(r=-2+\sqrt3\) and
\[
q_i=\frac23\frac{(1-r^i)(1-r^{m+1-i})}{1+r^{m+1}},\qquad S_m=\sum_{i=1}^{m}q_i.
\]
Every \(q_i\) is strictly positive, and the **unique** optimal sampling law and its minimum expected squared disagreement are
\[
\boxed{p_i^{(2)}=\frac{q_i}{S_m},\qquad \min\mathbb E\|x_2-\bar x_0\mathbf1\|_2^2=m-2+\frac1{S_m}.}
\]
The optimal probabilities have an alternating, exponentially localized boundary layer: with \(\rho=2-\sqrt3\), for each fixed \(i\ge1\),
\[
\lim_{m\to\infty}m p_i^{(2)}=1-(-\rho)^i.
\]
In particular, the limiting endpoint enhancement is \(3-\sqrt3\), whereas the second edge has a deficit \(1-\rho^2\). The bulk profile converges to uniform mass: \(m p_{\lfloor m/2\rfloor}^{(2)}\to1\).

For contrast, the **unique distribution maximizing the spectral gap** of the expected single-contact gossip matrix on the same path is the *centralized parabola*
\[
\boxed{p_i^{\mathrm{gap}}=\frac{6i(m+1-i)}{(m+1)m(m+2)}.}
\]
For every \(m\ge3\), its first two edges satisfy \(p_1^{\mathrm{gap}}<p_2^{\mathrm{gap}}\), while the two-contact isotropic optimum satisfies \(p_1^{(2)}>p_2^{(2)}\). These are distinct objectives; no claim is made that the two-contact optimum maximizes long-horizon convergence rates.

For four agents on a path, the two-contact optimizer is \((3/8,1/4,3/8)\), giving expected squared disagreement \(23/16\), compared with \(13/9\) under uniform edge selection: an exact decrease of \(1/144\). The spectral-gap optimizer instead is \((3/10,2/5,3/10)\).

## Assumptions and scope
The graph is finite, connected, simple, unweighted, and undirected. Each step selects exactly one edge from a **fixed** distribution, independently with replacement, then replaces its two endpoint values by their arithmetic mean, leaving all other values unchanged. Let \(x_0\) be independent of the sampled edges, have a finite second moment, satisfy \(\mathbb E x_0=\mu\mathbf1\) for some real \(\mu\), and have covariance \(I_n\). Only its first two moments enter the result, so Gaussianity is not assumed. The scalar \(\bar x_0=n^{-1}\mathbf1^{\mathsf T}x_0\) is the realized initial average. All expectations average over both initial opinions and the two edge choices.

The spectral-gap comparison concerns the second eigenvalue of the expected single-contact matrix, not the exact finite-horizon isotropic loss, nor a claimed exact almost-sure or mean-square convergence exponent. The case \(m=1\) is included.

## Proof
**Pair-average projections and their exact two-contact trace.** For an edge \(e=\{u,v\}\), let \(v_e=(e_u-e_v)/\sqrt2\) and \(P_e=I_n-v_ev_e^{\mathsf T}\). Then \(P_e\) is a symmetric orthogonal projection and \(P_e\mathbf1=\mathbf1\). Write \(C=I_n-\mathbf1\mathbf1^{\mathsf T}/n\). The centered initial data \(y_0=Cx_0\) have mean zero and covariance \(C\), because \(\mathbb E x_0=\mu\mathbf1\). Centering commutes with each \(P_e\). For deterministic edges \(e,f\), cyclicity of trace and idempotence of \(P_e\) give
\[
\mathbb E_{x_0}\|P_fP_ey_0\|_2^2
=\operatorname{tr}(CP_eP_fP_e)
=\operatorname{tr}(P_eP_f)-1
=n-3+(v_e^{\mathsf T}v_f)^2.
\]
Here \((v_e^{\mathsf T}v_f)^2\) equals \(1\) if \(e=f\), \(1/4\) if distinct edges share a vertex, and \(0\) if disjoint. Summing over independent edge probabilities proves the line-graph quadratic expression, including the coefficient \(1/4\) in \(B_G\). A single projection instead gives \(\operatorname{tr}(CP_e)=n-2\).

**Strict convexity and optimality conditions.** Let \(M\) be the unsigned vertex-edge incidence matrix of \(G\). Simplicity gives \(M^{\mathsf T}M=2I_m+A_{L(G)}\). Therefore
\[
B_G=\frac12I_m+\frac14M^{\mathsf T}M\succeq\frac12I_m,
\]
so the simplex quadratic has one minimizer. Its KKT conditions are: for a constant \(c\), \((B_Gp)_e=c\) on positive-probability edges, and \((B_Gp)_e\ge c\) on zero-probability edges, together with \(p\ge0\), \(\sum p=1\). If \(q=B_G^{-1}\mathbf1>0\), the stationary solution \(p=q/S\), \(S=\mathbf1^{\mathsf T}q\), is feasible and unique and has quadratic value \(1/S\).

**Exact path inverse.** The line graph of \(P_{m+1}\) is \(P_m\), so \(q=B_G^{-1}\mathbf1\) satisfies
\[
q_0=q_{m+1}=0,\qquad q_{i-1}+4q_i+q_{i+1}=4\quad(1\le i\le m).
\]
The constant particular solution is \(2/3\); the characteristic equation \(r^2+4r+1=0\) has roots \(r=-2+\sqrt3\) and \(r^{-1}=-2-\sqrt3\). Solving the two boundary conditions gives exactly
\[
q_i=\frac23\frac{1+r^{m+1}-r^i-r^{m+1-i}}{1+r^{m+1}}
=\frac23\frac{(1-r^i)(1-r^{m+1-i})}{1+r^{m+1}}.
\]
Since \(-1<r<0\), every numerator factor and denominator are strictly positive. This verifies the all-edge KKT solution, its uniqueness, and the formula for the minimum. Summing the geometric progression also yields
\[
S_m=\frac23\left[m-\frac{2r(1-r^m)}{(1-r)(1+r^{m+1})}\right].
\]
For fixed \(i\), the far-boundary powers vanish and \(S_m/m\to2/3\), giving \(m p_i^{(2)}\to1-r^i\); at a site with distance tending to infinity from both endpoints, both boundary terms vanish, giving the bulk limit. For \(m\ge3\), subtracting the first two closed-form entries gives
\[
q_1-q_2=\frac23\frac{(1-r)(r^{m-1}-r)}{1+r^{m+1}}>0,
\]
so the first edge has larger optimal mass than its neighbor.

**Opposite spectral-gap optimum.** For any path edge law \(p\), let \(L_p\) be its weighted graph Laplacian and \(\overline P=\sum_i p_iP_i=I-L_p/2\). For \(z_j=j-(n+1)/2\) and \(n=m+1\), one has \(z\perp\mathbf1\), \(\sum_jz_j^2=n(n^2-1)/12\), and \(\sum_i p_i(z_{i+1}-z_i)^2=1\). Thus
\[
\lambda_2(L_p)\le\frac{12}{n(n^2-1)}.
\]
Set \(c=6/[n(n^2-1)]\) and \(p_i=c i(n-i)\). The masses are positive and sum to one. Directly \((L_pz)_j=p_{j-1}-p_j=2c z_j\), with boundary values \(p_0=p_n=0\). To verify this is the **first** nonzero eigenvalue rather than just an eigenvalue, observe that \(L_p\) maps sampled polynomials in the vertex index of degree at most \(k\) to the same space, and on their leading coefficient multiplies by \(c k(k+1)\). The polynomial flags have successive dimensions \(1,\ldots,n\), so the real symmetric matrix has exactly the eigenvalues \(c k(k+1)\), \(k=0,\ldots,n-1\). Consequently \(\lambda_2(L_p)=2c\), meeting the upper bound. Equality in the Rayleigh bound for any other optimum forces \(z\) to be its eigenvector, so the recurrence \(p_{j-1}-p_j=2c z_j\), starting at \(p_0=0\), uniquely gives the same parabolic distribution. As \(\overline P\) is a convex combination of positive semidefinite projections, its second eigenvalue is \(1-\lambda_2(L_p)/2\). The spectral-gap solution favors interior edges: for \(m\ge3\), \(p_1^{\mathrm{gap}}<p_2^{\mathrm{gap}}\), the opposite of the two-contact solution.

## Verification
Run `python3 verify.py` from the same directory using only the Python standard library. The code computes exact rational pair-average matrices on several non-path networks and directly sums the two ordered-contact traces, independently comparing them to the line-graph quadratic. For paths it solves rational tridiagonal systems through thirty edges, checks positivity and the recurrence, compares with the closed radical formula, verifies the precise four-agent rational benchmark, and checks the separate parabolic spectral-gap eigenvector law through thirty vertices. It completed 297 assertions. Finite replay supports the algebra; the exact all-size results and asymptotics follow from the displayed analytic identities.

## Relationship to prior work
Boyd, Ghosh, Prabhakar and Shah [1,2] introduce and analyze independent random edge-averaging projections and optimize their long-horizon spectral convergence through a semidefinite program. Their projection formula and the connection between gossip and a weighted graph Laplacian are **prior work**, not claims of novelty here. The inspected optimization statements concern the second eigenvalue, not the expected squared loss under an isotropic initial law after exactly two contacts. The current closed form identifies a distinct finite-budget design and proves its opposite edge-ordering relative to spectral-gap optimization. An IEEE online availability date of 2005-05-16 was verified for the 2004 conference paper; the conference itself occurred in December 2004, but a day-specific public release of its proceedings before that online date was not verified.

Compared published results on deterministic path-sweep Gini contraction [3], two synchronous full-matching rounds [4], and homogeneous two-round stochastic averaging on strongly regular graphs [5] treat different random actions, objectives or graph families; none of their inspected claims implies the present fixed-iid single-edge two-contact path optimizer. published-finding corpus searches also returned no equivalent formula under terms including path, isotropic squared disagreement, inverse line-graph quadratic, two contacts, and spectral-gap comparison. Negative searches alone do not establish global bibliographic novelty.

## Limitations
The optimizer concerns **exactly two** independently sampled pairwise contacts, a fixed sampling law, and common-mean covariance-isotropic initial opinions. It need not optimize worst-case initial disagreement, other horizons, expected convergence time, adaptive choices, or communication latency. The spectral-gap comparison is a separate criterion and does not establish the exact asymptotic second-moment exponent for every initial distribution. The path formula is proved for every path length; no closed-form all-graph active-set classification is claimed. An equivalent identity in older Markov-chain, graph-design or randomized-projection literature may be indexed under different terminology; independent audit remains unperformed.

## References
[1] S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, “Analysis and Optimization of Randomized Gossip Algorithms,” *IEEE Conference on Decision and Control* (2004), 5310–5315. DOI: `10.1109/CDC.2004.1429652`. Public full text: https://web.stanford.edu/~boyd/papers/pdf/gossip_opt.pdf. IEEE online date: 2005-05-16.

[2] S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, “Randomized Gossip Algorithms,” *IEEE Transactions on Information Theory* **52** (2006), 2508–2530. DOI: `10.1109/TIT.2006.874516`. Public full text: https://web.stanford.edu/~balaji/papers/06randomizedgossip.pdf.

[3] “Exact Gini contraction of a left-to-right path gossip sweep,” public research record, 2026-11-17.

[4] “Exact two-round matching-averaging spectrum and logarithmic rank loss,” public research record, 2026-11-02.

[5] “A common-neighbor phase transition in two-round stochastic mixing on strongly regular graphs,” public research record, 2026-11-02.
