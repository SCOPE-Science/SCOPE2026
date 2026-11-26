# Quartic-root critical jamming in random length-two-path adsorption on complete bipartite graphs

## Finding

Consider random sequential adsorption of disjoint three-vertex paths on the complete bipartite graph \(K_{a_N,b_N}\), with \(N=a_N+b_N\). Give every initially possible (unoriented) length-two path an independent continuous random priority; scan paths in increasing priority and retain one only when all its vertices are still free. Let \(U_N\) denote the number of vertices left free when no more paths fit.

**Theorem (macroscopic jamming and its balanced crossover).** Suppose \(a_N,b_N\ge1\), \(N\to\infty\), and \(\delta_N=(a_N-b_N)/N\).

1. If \(\delta_N\to\delta\in(-1,1)\setminus\{0\}\), then
   \[
   \frac{U_N}{N}\xrightarrow{\mathbb P}|\delta|^{3/2},
   \qquad
   \frac{\mathbb E U_N}{N}\longrightarrow|\delta|^{3/2}.
   \]
2. If \((a_N-b_N)/\sqrt N\to\lambda\in\mathbb R\), then, for a standard normal \(Z\),
   \[
   \frac{U_N}{N^{1/4}}\xrightarrow{\mathrm d}|Z+\lambda|^{3/2}.
   \]
   In particular, perfectly balanced classes exhibit non-Gaussian \(N^{1/4}\)-scale terminal fluctuations rather than a positive limiting vacant density.

For the graph \(K_{9m,6m}\), the path hypergraph has a perfect vertex packing for every positive integer \(m\), yet the random greedy procedure leaves the fraction \(5^{-3/2}=0.0894427191\ldots\) unoccupied asymptotically. This comparison shows kinetic jamming even where exact packing is feasible.

## Assumptions and scope

Every simple three-vertex path has one center in one bipartition class and two endpoints in the other. Each distinct vertex triple representing a path is counted once; all have equally distributed independent continuous priorities. No weights, deletions, backtracking, or late rearrangement are allowed. The two classes are labeled but internally exchangeable. The parameter \(N\) is the **total** number of vertices, not the size of one side. The theorem concerns the terminal *accepted-path count process*, not finite physical arrival time. No claim is made about intermediate regimes where \(a_N-b_N\) grows faster than \(\sqrt N\) but is \(o(N)\), or about dimension-uniform constants beyond the stated limits.

The example \(K_{9m,6m}\) has a perfect packing: choose \(m\) paths consuming one vertex on the first side and two on the second, and \(4m\) consuming two on the first and one on the second. These paths consume respectively \(m+8m=9m\) and \(2m+4m=6m\) vertices.

## Proof

### 1. The exact two-class chain

Let \(X,Y\) be the numbers of currently free vertices in the two classes, and \(S=X+Y\), \(D=X-Y\). A path using two first-class vertices can be chosen in \(\binom X2Y\) ways; one using two second-class vertices in \(X\binom Y2\) ways. Given at least one feasible path, the next *accepted* path is uniform among the currently feasible ones. Indeed, because rejected paths can never become admissible, the unused relative order of the feasible paths stays exchangeable. For \(S\ge3\), \(X,Y\ge1\), the exact transitions are

\[
\begin{aligned}
(X,Y)&\longmapsto(X-2,Y-1),&&p=\frac{X-1}{S-2},\\
(X,Y)&\longmapsto(X-1,Y-2),&&1-p=\frac{Y-1}{S-2}.
\end{aligned}
\]

Consequently, every acceptance reduces \(S\) by three and changes \(D\) by \(\pm1\). Exactly,
\[
\mathbb E[\Delta D\mid X,Y]=-\frac{D}{S-2},\qquad
\operatorname{Var}(\Delta D\mid X,Y)=1-\frac{D^2}{(S-2)^2}.
\]
The process stops when one side becomes empty, or when fewer than three vertices remain. In particular, at any terminal state with \(S>3\), \(|D|=S\).

### 2. A gamma-ratio martingale and its size

For positive integers \(s\), put
\[
h(s)=\frac{\Gamma(s/3)}{\Gamma((s+1)/3)}.
\]
Gamma recurrence gives, for \(s>3\),
\[
\frac{h(s-3)}{h(s)}=\frac{s-2}{s-3}.
\]
Therefore \(M=h(S)D\) is an exact martingale whenever a deposition step has \(S>3\). For the argument, stop the martingale at physical termination or on first reaching \(S\le3\). Its conditional increment variance at a step starting with \(S=s>3\) is
\[
 h(s-3)^2\left(1-\frac{D^2}{(s-2)^2}\right)\le h(s-3)^2.
\]
As \(s\to\infty\), gamma-ratio asymptotics give
\[
 h(s)=3^{1/3}s^{-1/3}(1+O(s^{-1})),\qquad
 h(s)s=3^{1/3}s^{2/3}(1+O(s^{-1})).
\]
Since accepted steps visit each third integer only once,
\[
 \sum_{\substack{4\le s\le N\\s\equiv N\pmod3}}h(s-3)^2
 \le C N^{1/3}
\]
where the terms with \(s-3\ge1\) only are included. Doob's inequality then yields
\[
\max |M-M_0|=O_{\mathbb P}(N^{1/6})
\]
for the stopped process, uniformly over all initial class sizes.

### 3. Off balance: macroscopic residual

Suppose \(D_0/N\to\delta\ne0\). The initial martingale is
\[
M_0=3^{1/3}\delta N^{2/3}+o(N^{2/3}).
\]
The martingale error from step 2 is negligible compared with \(N^{2/3}\). Reaching \(S\le3\) would give a stopped martingale of bounded magnitude and thus has probability tending to zero. At the true terminal state, with high probability,
\[
|M_{\mathrm{term}}|=h(U_N)U_N.
\]
The asymptotic behavior of \(h(u)u\) forces \(U_N\) to be of order \(N\) and then gives
\[
\left(\frac{U_N}{N}\right)^{2/3}\xrightarrow{\mathbb P}|\delta|.
\]
Raising both sides to the power \(3/2\) proves the first probability limit. Because \(0\le U_N/N\le1\), convergence of expectations follows.

### 4. Balanced critical window: a Gaussian martingale with a nonlinear barrier

Assume \(D_0/\sqrt N\to\lambda\). Fix the deterministic stopping level \(r_N\) in the progression \(N,N-3,N-6,\ldots\) with \(r_N=N^{1/2}+O(1)\). Reaching an absorbing state before this level would force \(|M|\ge h(r_N)r_N\asymp N^{1/3}\), whereas the starting value and maximal martingale fluctuation are both \(O_{\mathbb P}(N^{1/6})\). Thus this early-stopping event has probability tending to zero.

Consider the martingale down to \(r_N\). Its predictable quadratic variation is
\[
V_N=\sum_{s>r_N}h(s-3)^2
 \left(1-\frac{D_s^2}{(s-2)^2}\right),
\]
where the sum follows the permitted progression and is stopped on the negligible early-termination event. The uncorrected sum satisfies
\[
\sum_{s>r_N}h(s-3)^2
 =3^{2/3}N^{1/3}(1+o(1)).
\]
For every \(s\ge r_N\), the second-moment martingale bound gives
\[
\mathbb E[D_s^2]\le C N^{1/3}s^{2/3}
\]
on the still-active part of the chain (zero after stopping). Hence the expected correction to the preceding sum is at most
\[
C N^{1/3}\sum_{s\ge r_N}s^{-2}
=O(N^{1/3}/r_N)=o(N^{1/3}).
\]
The martingale increments are bounded by \(2h(r_N-3)\), which is \(o(N^{1/6})\). The martingale central limit theorem consequently gives
\[
\frac{M_{r_N}}{3^{1/3}N^{1/6}}
\xrightarrow{\mathrm d}\lambda+Z,
\qquad Z\sim\mathcal N(0,1).
\]
Here \(M_{r_N}\) denotes the stopped value if a negligible early-termination event occurs.

The total *remaining* quadratic variation after \(r_N\), down to the first terminal state or \(S\le3\), is bounded by
\[
 C\sum_{4\le s\le r_N}h(s-3)^2=O(r_N^{1/3})=o(N^{1/3}).
\]
Another application of Doob's inequality shows that the final stopped martingale has the same limiting law after division by \(3^{1/3}N^{1/6}\). If the physical terminal remainder were bounded by a fixed constant, the corresponding stopped martingale would be bounded; because the limiting Gaussian has no atom at zero, the probability of such a bounded remainder tends to zero. Thus \(U_N\to\infty\) in probability and the auxiliary cutoff \(S\le3\) is asymptotically irrelevant.

Finally \(|M_{\mathrm{term}}|=h(U_N)U_N\), with high probability. Inverting its deterministic asymptotic gives
\[
\frac{U_N}{N^{1/4}}
 =\left|\frac{M_{\mathrm{term}}}{3^{1/3}N^{1/6}}\right|^{3/2}
 +o_{\mathbb P}(1)
 \xrightarrow{\mathrm d}|Z+\lambda|^{3/2}.
\]
This completes the proof.

## Verification

Run the attached standard-library script with `python trimer_checks.py`. It enumerates the actual allowable three-vertex paths on labeled bipartite graphs and compares their exact rational terminal distributions to an independently implemented two-count recurrence. For example, \(K_{4,2}\) yields \(\mathbb P(U=0)=3/4\) and \(\mathbb P(U=3)=1/4\), while \(K_{5,4}\) yields \(25/28\) and \(3/28\), respectively. The script also checks the one-step drift and variance identities over 99 positive-size states, the gamma recurrence on 125 successive integers, and reproducible finite-size simulations. Numerical experiments are checks only; neither limiting statement relies on an extrapolated finite sample.

## Relationship to prior work

Random sequential adsorption (RSA) and kinetic jamming have a long literature. De Oliveira and Tomé (1994) study inhomogeneous RSA on linear and square **bipartite lattices**, not three-vertex paths on a dense complete bipartite graph. Cieśla and Barbasz (2013), whose full open-access text was inspected, analyze physical trimers on a planar continuum collector numerically; they do not obtain the present exact two-count chain or its terminal limits. Pippenger (1989) treats random greedy monomer/dimer adsorption on sparse or locally treelike graphs. Bennett and Bohman (2012) analyze approximately regular random greedy hypergraph matchings, rather than this imbalanced model and its explicit stopping distribution. Glock and collaborators (2022/2024) establish general near-perfect conflict-free hypergraph matching results under regularity and codegree conditions, not this terminal quartic-root law.

A complete bipartite graph supplies a natural dense mean-field substrate, while V-shaped three-site adsorbates create competing \((2,1)\) and \((1,2)\) removal events; this specific combination is critical to the exponent \(1/4\). No claim is made to originality of gamma-martingale or martingale-CLT methods themselves.

## Limitations

The work treats an exact complete bipartite substrate with equal attempt rates for all three-vertex paths. It does not address sparse lattices, heterogeneous rates, other adsorption shapes, continuous physical time, or intermediate imbalance regimes. The proof provides convergence in distribution in the balanced window, not convergence of all moments or an explicit finite-size error rate. Analogous results may exist under urn-process terminology; incomplete access to some older primary papers remains a bibliographic risk.

## References

1. M. J. de Oliveira and T. Tomé, *Inhomogeneous random sequential adsorption on bipartite lattices*, Physical Review E **50**, 4523–4527 (1994), DOI: 10.1103/PhysRevE.50.4523. Published December 1, 1994.
2. M. Cieśla and J. Barbasz, *Random sequential adsorption of trimers and hexamers*, Journal of Molecular Modeling **19**, 5423–5427 (2013), DOI: 10.1007/s00894-013-2031-5. Public online November 6, 2013; accessible full text.
3. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics **2**, 393–401 (1989), DOI: 10.1137/0402034. Accessible abstract and metadata.
4. P. Bennett and T. Bohman, *A natural barrier in random greedy hypergraph matching*, arXiv:1210.3581 (first posted October 12, 2012).
5. S. Glock, F. Joos, J. Kim, M. Kühn, and L. Lichev, *Conflict-free hypergraph matchings*, arXiv:2205.05564 (first posted May 11, 2022); Journal of the London Mathematical Society (2024), DOI: 10.1112/jlms.12899.
