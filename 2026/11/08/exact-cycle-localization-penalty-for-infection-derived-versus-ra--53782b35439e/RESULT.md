# Exact cycle-localization penalty for infection-derived versus random immunity

## Finding

For the continuous-time Markov susceptible–infectious–removed (SIR) epidemic on a simple contact cycle, the mean size of a subsequent outbreak is strictly larger after infection-acquired immunity than after a uniformly random set of the same number of immune individuals, whenever at least two susceptible and at least two immune individuals remain. More precisely, for every integer \(n\ge4\), every \(2\le k\le n-2\), and all positive transmission and recovery rates \(\beta,\gamma\), put

\[
L=n-k,\qquad p=\frac{\beta}{\beta+\gamma}.
\]

Let \(E_{\mathrm{natural}}\) and \(E_{\mathrm{random}}\) denote the expected number of cases, **including the newly introduced infectious individual**, in the second outbreak under the two immunity schemes defined below. Then

\[
\boxed{E_{\mathrm{natural}}-E_{\mathrm{random}}=
\frac{2}{L}\sum_{d=1}^{L-1}
\left[L-d-\frac{n\binom{n-d-1}{k}}{\binom{n}{k}}\right]p^d>0.}
\]

Every coefficient of this polynomial is strictly positive. Therefore the gap increases strictly with edge transmissibility, and has the exact maximal limiting value

\[
\boxed{\lim_{p\uparrow1}(E_{\mathrm{natural}}-E_{\mathrm{random}})
=\frac{(k-1)(n-k-1)}{k+1}.}
\]

Two distinct population-size regimes are explicit. For fixed \(k\ge2\) and fixed \(0<p<1\), as \(n\to\infty\),

\[
E_{\mathrm{natural}}-E_{\mathrm{random}}
\sim\frac{2(k-1)p}{n(1-p)^2}.
\]

For \(k/n\to\alpha\in(0,1)\), with \(p\in(0,1)\) fixed, the gap tends to

\[
\boxed{\frac{2\alpha p}{(1-p)[1-(1-\alpha)p]}.}
\]

At the minimal nontrivial immunity count \(k=2\), the entire formula reduces to

\[
\frac{2}{(n-1)(n-2)}\sum_{d=1}^{n-3}d(n-2-d)p^d.
\]

If \(k=2\) and \(p=p_n\in(0,1)\) satisfies \(n(1-p_n)\to c\in[0,\infty)\), then the crossover is

\[
\lim_{n\to\infty}\frac{E_{\mathrm{natural}}-E_{\mathrm{random}}}{n}
=2\int_0^1 x(1-x)e^{-cx}\,dx
=\begin{cases}\frac{2[c-2+(c+2)e^{-c}]}{c^3},&c>0,\\
\frac13,&c=0.
\end{cases}
\]

All statements above concern the stated model and do not assert novelty for the previously known *qualitative* effect of spatially clustered immunity.

## Assumptions and scope

The contact graph \(C_n\) has vertices \(0,1,\ldots,n-1\) and an undirected edge between consecutive vertices modulo \(n\). An infectious vertex contacts each susceptible neighbor at rate \(\beta>0\) independently and recovers at rate \(\gamma>0\); recovered vertices are permanently immune. The graph is fixed and contacts occur through its edges only.

In the **natural-immunity scheme**, choose the first index vertex uniformly, run the epidemic until extinction, and condition on exactly \(k\) distinct infections in this primary outbreak. These \(k\) people are permanently immune at the start of the second outbreak. The conditioning event has positive probability for every admissible parameter choice and \(1\le k<n\).

In the **random-immunity scheme**, independently select a uniformly random \(k\)-subset of vertices and immunize it. In *either* scheme, select the new index infection uniformly among the \(L=n-k\) remaining susceptible vertices; evolve a fresh SIR epidemic using the same \(\beta,\gamma\) and new independent exponential clocks. The second-outbreak count includes its index and excludes the already immune \(k\) individuals. Thus both schemes have the identical immune count, original degree distribution, transmissibility, and number of candidates for reinvasion.

A primary epidemic infects a connected set because transmission follows edges. If it infects strictly fewer than \(n\) vertices on a cycle, that set is a single cyclic interval. Conditional on \(k\) infections, rotational symmetry gives a uniform choice among the \(n\) cyclic intervals of size \(k\). The residual susceptible graph is therefore a path with \(L\) vertices. For \(k=1\), the two schemes are identical; for \(L=1\), no onward transmission is possible, explaining the boundary exclusions in the strict inequality.

## Proof

**1. One-path transmission probability.** Removing a nonempty set of immune vertices from a cycle leaves a disjoint union of paths (allowing isolated vertices). Fix susceptible vertices \(u,v\) in the same residual path at graph distance \(d\ge1\). With a fresh infection at \(u\), vertex \(v\) is eventually infected if and only if infection succeeds successively across the unique path from \(u\) to \(v\). For each infectious vertex on this path, the contact clock toward the next vertex (rate \(\beta\)) races its independent recovery clock (rate \(\gamma\)), so the chance of that required transmission is \(p=\beta/(\beta+\gamma)\). These races involve distinct source vertices and are independent; transmissions on other edges cannot create an alternative path. Therefore

\[
\Pr(v\text{ is infected}\mid u\text{ is the new index})=p^d.
\]

This argument does *not* assume independence of transmissions from the same infectious vertex, which would generally be false for this CTMC.

**2. Expected cases given a susceptible forest.** Suppose the residual path components have lengths \(\ell_1,\ldots,\ell_m\) with \(\sum_j\ell_j=L\). In a path of length \(\ell\), exactly \(\ell-d\) unordered vertex pairs have distance \(d\). Average over all \(L\) possible new index infections and use linearity of expectation:

\[
E(Z\mid\ell_1,\ldots,\ell_m)
=1+\frac2L\sum_{j=1}^m\sum_{d=1}^{\ell_j-1}(\ell_j-d)p^d.
\]

For natural immunity, the unique residual component has length \(L\), giving

\[
E_{\mathrm{natural}}=1+\frac2L\sum_{d=1}^{L-1}(L-d)p^d.
\]

**3. Exact counting for uniform immune deletion.** For fixed \(d\in\{1,\ldots,L-1\}\), consider oriented clockwise segments of \(d\) consecutive edges around \(C_n\). There are \(n\) such segments. One survives intact when its \(d+1\) vertices avoid the \(k\) immune vertices, an event of probability \(\binom{n-d-1}{k}/\binom{n}{k}\). In a nonempty-immunized cycle every unordered pair at distance \(d\) in a residual path corresponds to exactly one such clockwise oriented segment (choose the starting endpoint according to the orientation of its unique remaining path); there is no double-counting via a second route around the cycle because that route contains an immune vertex. Therefore the expected number of connected susceptible vertex pairs at distance \(d\) is

\[
M_{n,k,d}=\frac{n\binom{n-d-1}{k}}{\binom{n}{k}}.
\]

Insert this in the previous path-sum formula:

\[
E_{\mathrm{random}}=1+\frac2L\sum_{d=1}^{L-1}M_{n,k,d}p^d,
\]

which gives the claimed exact gap.

**4. Strict coefficientwise inequality.** Elementary factorial cancellation gives

\[
\frac{M_{n,k,d}}{L-d}
=\prod_{j=1}^d\frac{L-j+1}{n-j}
=\prod_{j=1}^d\left(1-\frac{k-1}{n-j}\right).
\]

For \(2\le k\le n-2\) and \(1\le d\le L-1\), all these factors lie strictly between zero and one. Thus \(0<M_{n,k,d}<L-d\), so every coefficient in the finite polynomial is strictly positive. Differentiation gives strict increase in \(p\in(0,1)\).

**5. Perfect-transmission boundary.** At \(p\uparrow1\), the natural second epidemic eventually infects the entire residual path, so \(E_{\mathrm{natural}}\to L\). The hockey-stick identity yields

\[
\sum_{d=1}^{L-1}\binom{n-d-1}{k}=\binom{n-1}{k+1},
\]

and hence

\[
\lim_{p\uparrow1}E_{\mathrm{random}}
=1+\frac{2n}{L}\frac{\binom{n-1}{k+1}}{\binom{n}{k}}
=1+\frac{2(L-1)}{k+1}.
\]

The difference is \((k-1)(L-1)/(k+1)\). This is a limit of admissible positive recovery-rate models, not an assertion that recovery rate zero is allowed.

**6. Population-size limits.** Write \(g_{n,k,d}=L-d-M_{n,k,d}\). For fixed \(k,d\), the product in Step 4 gives \(g_{n,k,d}\to(k-1)d\) as \(n\to\infty\). Also \(0\le g_{n,k,d}\le(k-1)d\): use \(1-\prod(1-a_j)\le\sum a_j\) with \(a_j=(k-1)/(n-j)\), and \((L-d)/(n-j)\le1\) for \(j\le d\). The bound makes dominated convergence available for \(\sum_{d\ge1}g_{n,k,d}p^d\), where absent terms are treated as zero. Since \(\sum_{d\ge1}dp^d=p/(1-p)^2\) and \(L\sim n\), the fixed-\(k\) asymptotic follows.

For \(k/n\to\alpha\in(0,1)\), each fixed-distance natural coefficient \((L-d)/L\) tends to one, while the random coefficient \(M_{n,k,d}/L=\prod_{j=1}^d(L-j)/(n-j)\) tends to \((1-\alpha)^d\). Both are bounded by one. Dominated convergence of the geometrically weighted sums gives \(2\sum_{d\ge1}[1-(1-\alpha)^d]p^d\), the stated rational expression.

Finally, for \(k=2\), direct cancellation in Step 3 gives \(g_{n,2,d}=d(n-2-d)/(n-1)\). If \(n(1-p_n)\to c\in[0,\infty)\), the uniform approximation \(p_n^{\lfloor nx\rfloor}\to e^{-cx}\) on \(x\in[0,1]\), together with Riemann-sum convergence, gives the asserted \(n\)-scaled integral limit. Integration yields the closed expression for \(c>0\), with continuous value \(1/3\) at zero.

## Verification

The supplementary standalone Python script `verification/ctmc_cycle_checker.py` constructs the complete finite-state continuous-time Markov chain by its exponential event rates; it does **not** use the path-transmission formula in this recursion. It computes the exact expected second-outbreak count with rational arithmetic by first-step recursion, for every possible immune subset and each susceptible index. The script checks the independent CTMC answers against the path-count polynomial, its strictly positive gap, and its perfect-transmission limit in \(30\) nontrivial combinations: \(4\le n\le8\), all \(2\le k\le n-2\), and the two rate choices \((\beta,\gamma)=(1,1)\) and \((2,3)\). All checks passed. The enumerations validate examples and computations, not the infinite-domain claims; these follow from Steps 1–6.

Examples: at \(n=4,k=2,p=1/2\), the mean sizes are \(3/2\) and \(4/3\), a gap of \(1/6\). At \(n=6,k=3,p=1/2\), they are \(11/6\) and \(29/20\), a gap of \(23/60\).

## Relationship to prior work

Ueki, Thompson and Banaji (first public version January 20, 2026) study stochastic epidemics on networked populations and compare the sizes of secondary outbreaks after infection-acquired versus equally abundant random immunity, including spatial/ring architectures. Their numerical and analytical discussion supplies the motivating *comparison*, not the finite-cycle conditional all-\(k\) formula above. Hiraoka and coauthors (public preprint 2023; journal 2025) already identify the topological localization of infection-derived immunity as a mechanism weakening protection, including spatial networks. Ferrari, Bansal, Meyers and Bjørnstad (2006) establish the earlier network-frailty/interference picture and simulate repeat outbreaks. These qualitative effects and the standard SIR clock race are prior art, not the claimed new contribution.

The candidate contribution is the exact conditional finite-\(n\), all-\(k\) secondary-outbreak polynomial with coefficientwise sign and the distinct fixed-count, proportional-count, and high-transmissibility scaling laws. Literature searching did not locate this specific statement or a demonstrably stronger theorem implying it; this does not prove uniqueness. In particular, equivalent formulations within one-dimensional percolation or unindexed epidemic-network appendices remain possible.

## Limitations

This is an exact result for a homogeneous, static simple cycle, permanent immunity and exponentially distributed infection/recovery clocks. It does not establish an inequality for arbitrary networks, non-Markov infection duration laws, incomplete immunity, variants that evade immunity, or simultaneous multiple introductions. Natural immunity is conditioned on the first outbreak's **exact** size, not averaged over its size distribution. The model supplies no empirical epidemic calibration or clinical recommendation. High-transmissibility limits are mathematical, and the independence needed in Step 1 occurs across vertices along a unique path only. The primary scientific review was internal; independent validation has not been performed.

## References

1. M. Ueki, R. N. Thompson and M. Banaji, *Outbreak dynamics and population vulnerability in stochastic epidemic models on networks*, arXiv:2601.13730, initially public January 20, 2026. https://arxiv.org/abs/2601.13730
2. T. Hiraoka, Z. Ghadiri, A. K. Rizi, M. Kivelä and J. Saramäki, *Strength and weakness of disease-induced herd immunity in networks*, PNAS 122 (2025), e2421460122; original arXiv:2307.04700. https://doi.org/10.1073/pnas.2421460122
3. M. J. Ferrari, S. Bansal, L. A. Meyers and O. N. Bjørnstad, *Network frailty and the geometry of herd immunity*, Proceedings of the Royal Society B 273 (2006), 2743–2748. https://doi.org/10.1098/rspb.2006.3636
