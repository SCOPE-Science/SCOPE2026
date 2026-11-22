# A spectral-order activation window and unique conductance-budget peak on friendship networks

## Finding
For each integer \(m\ge2\), let the friendship network \(F_m=K_1\vee(mK_2)\) consist of a central vertex attached to both vertices of each of \(m\) disjoint pairs, with an additional edge joining the two vertices in every pair. A hub–periphery (spoke) conductance costs \(\gamma>0\) per unit, each pair-internal conductance costs one unit, and the budget is \(B>0\). Every edge weight may be independently selected from \([0,\infty)\), subject to connected positive-conductance support and total price at most \(B\).

For every real spectral order \(p>0\), minimize \(\mathcal F_p(L)=\sum_{j=2}^{2m+1}\lambda_j(L)^{-p}\), where the \(\lambda_j\) are the positive eigenvalues of the weighted combinatorial Laplacian. At \(p=0\), minimize the continuous determinant endpoint \(\mathcal F_0(L)=-\sum_{j=2}^{2m+1}\log\lambda_j(L)\). **For every \(p\ge0\), the global minimizer exists and is unique**; in particular, independently adjustable edges must have a common spoke conductance \(a_{m,\gamma,p}>0\) and a common pair conductance \(b_{m,\gamma,p}\ge0\).

Put \(N=2m+1\), \(U_p=m-1+N^{-p}\), and
\[
 s_{m,\gamma,p}=\max\left\{1,\left(\frac{m\max\{4\gamma-1,0\}}{U_p}\right)^{1/(p+1)}\right\}.
\]
Then the complete exact optimum (including the determinant endpoint) is
\[
 a_{m,\gamma,p}=\frac{2B}{m(s_{m,\gamma,p}+4\gamma-1)},\qquad
 b_{m,\gamma,p}=\frac{a_{m,\gamma,p}}2(s_{m,\gamma,p}-1).
\]
**Strict support criterion:** all pair-internal edges are purchased if and only if
\[
 \gamma>\gamma_c(m,p):=\frac{2m-1+N^{-p}}{4m}.
\]
In particular, \(\gamma_c(m,0)=1/2\), \(\gamma_c(m,p)\) decreases strictly with \(p\), and its limit as \(p\to\infty\) is \((2m-1)/(4m)\).

**Spectral-order activation and single hump.** Fix
\[
 \frac{2m-1}{4m}<\gamma<\frac12.
\]
There is exactly one finite activation order
\[
 p_c=-\frac{\log(4m\gamma-(2m-1))}{\log(2m+1)}>0.
\]
The unique optimal design spends nothing on pair edges for \(0\le p\le p_c\), spends strictly positive budget on every pair edge for \(p>p_c\), and its pair-edge fraction of total spending
\[
 f(p)=\frac{m b_{m,\gamma,p}}{B}=\frac{s_{m,\gamma,p}-1}{s_{m,\gamma,p}+4\gamma-1}
\]
has exactly **one strict global maximum** at an order \(p_*>p_c\). Moreover \(f(p)\to0\) as \(p\to\infty\), with
\[
 \frac{b_{m,\gamma,p}}{a_{m,\gamma,p}}\sim\frac1{2p}\log\!\left(\frac{m(4\gamma-1)}{m-1}\right).
\]
Thus the determinant-optimal design omits every internal edge, intermediate spectral moments activate them, and the high-order design asymptotically spends zero on them. This is a *finite-order support activation followed by asymptotic withdrawal*, not an assertion of a second finite support-deletion point.

As the smallest example, take \(m=2\), the five-vertex friendship network, and \(\gamma=7/16\). The transition is \(p_c=\log 2/\log 5\); all \(p>p_c\) purchase each of the two pair edges, but their total budget fraction tends to zero at high spectral order.

## Assumptions and scope
Graphs are finite, simple, undirected. Spokes and pair edges are eligible for independent nonnegative conductance allocation. Positive support must be connected; zero pair weights are permitted and the all-spoke star is connected. The Laplacian is unnormalized and has one zero eigenvalue. Nonzero eigenvalues are counted with multiplicity. Prices are strictly positive and uniform within each of the two edge orbits, and the total weighted-linear conductance budget is an upper bound. Order \(p=0\) is defined by the negative logarithm of the positive-eigenvalue product; this is the finite, explicitly specified extension of the inverse-spectral-moment family, not the value of \(\sum_j\lambda_j^0\). The theorem describes the unique optimum for each finite \(p\ge0\). The \(p\to\infty\) statement concerns limits of these finite-order designs; it does not assert uniqueness for the independent spectral-gap optimization endpoint.

## Proof
**1. Existence, full-budget use and uniqueness without a symmetry assumption.** A feasible all-spoke star exists. The closed budget simplex is compact, and every approach to disconnection sends a formerly positive Laplacian eigenvalue to zero. For \(p>0\) this makes \(\mathcal F_p\to+\infty\); for \(p=0\), the negative log positive-eigenvalue product also tends to \(+\infty\). Hence the optimum exists and is connected. Increasing all positive conductances by a common factor lowers the objective (by homogeneity for \(p>0\), and logarithmically for \(p=0\)); thus the budget is exhausted.

Restrict \(L\) to \(\mathbf1^\perp\) as a positive-definite matrix \(X\). For \(p>0\), \(x\mapsto x^{-p}\), and for \(p=0\), \(x\mapsto-\log x\), have strictly positive scalar second derivatives and strictly increasing first derivatives. The Hessian of their trace spectral function at diagonalized \(X\), in any symmetric direction \(H\ne0\), is a sum of strictly positive diagonal terms \(f''(\lambda_i)|H_{ii}|^2\) and off-diagonal terms \(2[f'(\lambda_i)-f'(\lambda_j)]/(\lambda_i-\lambda_j)|H_{ij}|^2\), with the repeated-eigenvalue ratio interpreted as \(f''\). Consequently \(\operatorname{tr} f(X)\) is strictly convex. The map from the edge conductances to \(X\) is injective, since a simple graph's off-diagonal Laplacian entries recover all edge weights. Thus the optimum is globally unique even against arbitrary asymmetric allocations. Automorphisms permute all \(2m\) spokes transitively and all \(m\) pair edges transitively, forcing respective common conductances \(a,b\).

**2. Spectrum and exact scalar objective.** For symmetric weights \(a>0,b\ge0\), the full Laplacian spectrum is
\[
 0\ (1),\qquad a\ (m-1),\qquad a+2b\ (m),\qquad Na\ (1).
\]
The budget identity is \(m(2\gamma a+b)=B\). Define \(s=(a+2b)/a\ge1\). Then
\[
 a=\frac{2B}{m(s+4\gamma-1)},\qquad b=\frac{a(s-1)}2.
\]
For \(p>0\), direct substitution yields
\[
 \mathcal F_p=\left(\frac{m}{2B}\right)^p(s+4\gamma-1)^p\bigl(U_p+ms^{-p}\bigr),\quad U_p=m-1+N^{-p}.
\]
The derivative of its logarithm has the sign of
\[
 U_p-m(4\gamma-1)s^{-(p+1)}.
\]
If \(4\gamma-1\le0\), the sign is positive for all \(s\ge1\); otherwise it increases strictly through at most one zero. Hence the minimizer on \([1,\infty)\) is the stated \(s_{m,\gamma,p}\), unique in every parameter regime. For \(p=0\), dropping additive constants, \(\mathcal F_0=2m\log(s+4\gamma-1)-m\log s\). Its derivative has the sign of \(s-(4\gamma-1)\), so \(s_* = \max\{1,4\gamma-1\}\), agreeing with the formula at \(p=0\). The condition \(s>1\) rearranges to \(4m\gamma>2m-1+N^{-p}\); equality gives the unique boundary optimizer \(b=0\). This proves the optimizer and exact support threshold.

**3. Activation and exactly one spending peak.** Assume \((2m-1)/(4m)<\gamma<1/2\), and write \(c=4\gamma-1\). Then \((m-1)/m<c<1\). Since \(U_p=m-1+N^{-p}\) decreases strictly from \(m\) to \(m-1\), the equation \(mc=U_p\) has exactly the given solution \(p_c>0\), with \(b=0\) at and below \(p_c\) and \(b>0\) above it.

For \(p>p_c\), set
\[
 h(p)=\log\frac{mc}{U_p},\qquad \log s(p)=\frac{h(p)}{p+1}.
\]
Here \(h(p_c)=0\), \(h'(p)=(\log N)N^{-p}/U_p>0\), and
\[
 h''(p)=-\frac{(m-1)(\log N)^2N^{-p}}{U_p^2}<0.
\]
The sign of \(s'(p)\) equals that of \(k(p)=(p+1)h'(p)-h(p)\). This function decreases strictly because \(k'(p)=(p+1)h''(p)<0\). Moreover \(k(p_c)=(p_c+1)h'(p_c)>0\), whereas \(k(p)\to-\log[mc/(m-1)]<0\) as \(p\to\infty\). Therefore exactly one \(p_*>p_c\) satisfies \(k(p_*)=0\), with \(s\) strictly increasing before, decreasing after. The spending fraction \(f=(s-1)/(s+c)\) is strictly increasing in \(s\), since \(c+1=4\gamma>0\), proving the unique strict maximum. Finally \(h(p)\to\log[mc/(m-1)]\), so \(s-1\sim\log[mc/(m-1)]/p\), yielding the stated ratio and zero spending limit.

## Verification
A standalone standard-library Python script, `verify.py`, tests the exact spectrum against independently diagonalized weighted Laplacian matrices, computes exact rational Laplacian pseudoinverse traces via grounded inverses, checks budget normalization and threshold sides, compares finite-order formula optima to scalar and nonsymmetric random feasible competitors, and tests the five-vertex activation and high-order law. Executing `python3 verify.py` on the packaged copy produced `VERIFY_OK 2239`. These finite diagnostics test implementation and sample points; the quantified all-parameter theorem is established by the preceding analytic proof, not by enumeration.

## Relationship to prior work
Ghosh, Boyd and Saberi developed convex effective-resistance network design and studied trees, wheels and other examples. Their work supplies the broader first-order conductance-allocation framework. Two subsequently published exact clique-windmill allocation results, *Universal edge-support threshold in Kirchhoff-index design of clique windmills* and *Universal price cutoff for resistance-optimal clique windmills*, solve the \(p=1\) first-inverse-moment problem for the whole clique-windmill family; their sharp threshold specializes here to \(\gamma_c(m,1)=m/(2m+1)\). That known special case, as well as the general principle of strict convex optimization, is **not claimed as new**. At the determinant endpoint \(p=0\), the network is a cactus of triangles: the published *Exact price-driven support transitions for D-optimal conductances on cactus networks* establishes the complete optimal determinant allocation under arbitrary edge prices. Its dominant-cycle-edge criterion specializes to \(\gamma_c(m,0)=1/2\), so the determinant boundary and its isolated optimizer are also **known**. The original contribution asserted here is the single theorem linking these already-known endpoints across all real spectral orders, especially its one-peak interior spending law. The distinguishing claim is the simultaneous continuous-order classification, the finite activation order for determinant-to-power interpolation, the unique spectral-order investment peak, and its high-order withdrawal for the friendship subfamily.

Patterson and Bamieh analyze first- and second-order noisy-consensus coherence through inverse Laplacian spectral moments and motivate the family of spectral criteria, but do not derive the claimed price-dependent friendship-network support transition. The accessible windmill resistance-index literature predominantly evaluates fixed edge weights, not the all-orders priced optimization. An unindexed equivalent theorem, or one in inaccessible full text, would limit originality; the overlap checks below are not a priority or independence certification.

## Limitations
Uniform prices within each edge class, a shared linear budget, undirected combinatorial Laplacian and independent nonnegative edge conductances are essential. No assertion is made for arbitrary heterogeneous prices, directed chains or discrete installation costs. The internal edges never return to exactly zero at any finite order once activated: the second loss of investment occurs **only as \(p\to\infty\)**. The price support laws at both the determinant and first inverse-spectral-moment endpoints were previously published, while the present claimed contribution is their exact spectral-order interpolation and unique peak. Literature searches cannot exclude every unindexed or inaccessible equivalent. The analytic work and its numerical checker have not received an independent mathematical audit.

## References
1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems (2006), author-hosted paper https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf ; expanded SIAM Review 50(1), 37–66 (2008), https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf.
2. S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks*, first public arXiv submission October 9, 2013, https://arxiv.org/abs/1310.2592.
3. *Universal edge-support threshold in Kirchhoff-index design of clique windmills* (published November 2, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-universal-edge-support-threshold-in-kirchhoff-index-design-of-cl--5bb3f4f9b118.
4. *Universal price cutoff for resistance-optimal clique windmills* (published November 8, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-universal-price-cutoff-for-resistance-optimal-clique-windmills--2fd993460ba7.
5. *Exact price-driven support transitions for D-optimal conductances on cactus networks* (published November 2, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-price-driven-support-transitions-for-d-optimal-conductance--9435e031bf05.
6. M. S. Sardar and S.-J. Xu, *Resistance Distance and Kirchhoff Index in Windmill Graphs* (2024), https://doi.org/10.2174/0115701794299562240606054510 (abstract accessible; entire full text not inspected).
