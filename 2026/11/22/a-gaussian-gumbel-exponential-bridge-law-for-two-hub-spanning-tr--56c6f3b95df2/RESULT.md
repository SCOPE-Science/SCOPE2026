# A Gaussian–Gumbel–exponential bridge law for two-hub spanning-tree polytopes

## Finding

For each integer \(q\ge2\), let \(P_q\subset\mathbb R^{2q}\) be the canonical Euclidean spanning-tree polytope of the complete bipartite graph \(K_{2,q}\). For independent standard Gaussian edge weights \(G_{ai},G_{bi}\), set \(U_i=\max(G_{ai},G_{bi})\), \(L_i=\min(G_{ai},G_{bi})\), \(B_q=\max_{1\le i\le q}L_i\), and let \(J_q\) be the almost surely unique index attaining this maximum. Its exposed spanning tree contains both edges to vertex \(J_q\); define the surplus on this double-edge bridge by \(\Delta_q=U_{J_q}-L_{J_q}\).

**Exact Gaussian support and marked extreme-value law.** For every real realization of the weights,
\[
h_{P_q}(G)=\sum_{i=1}^q U_i+B_q.
\]
The bridge bottleneck has distribution \(\Pr(B_q\le t)=(1-\overline\Phi(t)^2)^q\). Its joint density with its surplus is
\[
 f_{B_q,\Delta_q}(t,\delta)
 =2q\,\phi(t)\phi(t+\delta)\bigl(1-\overline\Phi(t)^2\bigr)^{q-1},\quad t\in\mathbb R,\ \delta>0.
\]
Here \(\phi\) and \(\Phi\) are the standard normal density and distribution function, and \(\overline\Phi=1-\Phi\).

For \(q>4\), put \(b_q=\Phi^{-1}(1-q^{-1/2})\) and \(a_q=q^{-1/2}/[2\phi(b_q)]\). As \(q\to\infty\), the following joint convergence holds:
\[
\left(
 \frac{\sum_{i=1}^q(U_i-1/\sqrt\pi)}{\sqrt{q(1-1/\pi)}},
 \frac{B_q-b_q}{a_q},
 b_q\Delta_q
\right)
\ \Longrightarrow\ (Z,G,E),
\]
where the three variables on the right are **mutually independent**, \(Z\) is standard normal, \(G\) is standard Gumbel with distribution \(\Pr(G\le x)=\exp(-e^{-x})\), and \(E\) is mean-one exponential.

**Sharp Euclidean mean-width expansion.** With Gaussian mean width defined by \(\mathcal W_q=\mathbb E[h_{P_q}(G)+h_{P_q}(-G)]\),
\[
\begin{aligned}
\mathcal W_q&=\frac{2q}{\sqrt\pi}+2\mathbb E B_q,\\
&=\frac{2q}{\sqrt\pi}+2\sqrt{\log q}
-\frac{\log\log q+\log(2\pi)-\gamma}{\sqrt{\log q}}
+o\!\left((\log q)^{-1/2}\right),
\end{aligned}
\]
where \(\gamma\) is Euler's constant. The exact bridge contribution to the Gaussian width is \(2\mathbb EB_q\), of order \(2\sqrt{\log q}\), despite the bulk contribution being linear in \(q\).

## Assumptions and scope

The graph has two labelled hub vertices and \(q\ge2\) labelled peripheral vertices, with all \(2q\) possible hub–peripheral edges and no other edges. The polytope is the convex hull of tree edge-indicator vectors with the **ordinary inherited Euclidean scalar product**. Its dimension is \(2q-1\). The Gaussian objective uses independent, unscaled standard normal weights in all \(2q\) edge coordinates. Gaussian mean width is an expected sum of opposing support functions; division by the expected Gaussian norm would convert it to a spherical-width normalization. Only the limit law requires \(q\to\infty\); the support and joint-density identities hold exactly at all \(q\ge2\).

## Proof

**1. Classification and support identity.** A spanning tree on \(K_{2,q}\) has \(q+1\) edges. Each peripheral vertex must have degree at least one, leaving exactly one excess edge over the \(q\) indispensable incidences. Therefore exactly one peripheral vertex has degree two, and every other peripheral vertex has degree one; this also suffices for connectivity and acyclicity. For a fixed double-incidence vertex \(j\), the optimal tree-weight sum is \(G_{aj}+G_{bj}+\sum_{i\ne j}U_i=\sum_i U_i+L_j\). Maximizing over \(j\) yields the stated support identity, as well as \(q2^{q-1}\) labelled trees. Ties have probability zero under the stated Gaussian law.

**2. Exact marked density.** Each pair \((U_i,L_i)\) has joint density \(2\phi(t)\phi(t+\delta)\) in coordinates \((L_i, U_i-L_i)=(t,\delta)\), with \(\delta>0\). The cdf of one minimum is \(F(t)=1-\overline\Phi(t)^2\). Summing over the \(q\) possible maximizing indices and requiring the other \(q-1\) minima to be at most \(t\) yields \(2q\phi(t)\phi(t+\delta)F(t)^{q-1}\). Integrating in \(\delta\) gives \(2q\phi(t)\overline\Phi(t)F(t)^{q-1}\), the derivative of \(F(t)^q\). Conditional on \(B_q=t\),
\[
\Pr(\Delta_q>z\mid B_q=t)
=\frac{\overline\Phi(t+z)}{\overline\Phi(t)},\qquad z\ge0.
\]
This is an exact regular conditional law for almost every real \(t\).

**3. Gumbel bottleneck and exponential bridge surplus.** By construction \(q\overline\Phi(b_q)^2=1\). The normal Mills ratio implies \(\overline\Phi(t)/\phi(t)\sim1/t\) and, uniformly for \(x\) in compact sets,
\[
q\overline\Phi(b_q+a_qx)^2\longrightarrow e^{-x},\quad
\frac{\overline\Phi(b_q+a_qx+u/b_q)}{\overline\Phi(b_q+a_qx)}\longrightarrow e^{-u}
\]
for each \(u\ge0\). (Here \(b_q\to\infty\), \(a_q\sim1/(2b_q)\).) The first estimate proves Gumbel convergence; using the second in the conditional tail formula, with the tightness of the Gumbel-scaled bottleneck, gives convergence of the pair to an independent standard Gumbel and mean-one exponential. Equivalently one may rescale the explicit joint density from Step 2.

**4. Independent Gaussian bulk.** Set \(\mu=\mathbb EU_1=1/\sqrt\pi\), \(\sigma^2=\operatorname{Var}(U_1)=1-1/\pi\). These moments follow from \(U_1=(G_{a1}+G_{b1}+|G_{a1}-G_{b1}|)/2\). To verify independence of the normalized bulk from the marked extreme, condition on a selected bottleneck value \(t=b_q+O(a_q)\). The other \(q-1\) pairs are independent with their minima restricted to \(L_i\le t\). In this range \(\Pr(L_i>t)=O(1/q)\), and for every fixed positive integer \(k\), normal tail bounds yield
\[
\mathbb E\left[|U_i|^k\mathbf1_{\{L_i>t\}}\right]
=O\left(\frac{(\log q)^{k/2}}q\right)
\]
uniformly on compact normalized bottleneck windows. Consequently the truncation changes the total mean of the normalized bulk by \(O(\sqrt{\log q/q})\), and changes its variance and Lyapunov bound by negligible amounts. The selected pair contributes only \(O_{\mathbb P}(\sqrt{\log q/q})\) to the normalized sum. Conditional Lindeberg–Feller convergence, uniform for normalized bottleneck and surplus in fixed compact sets, gives a standard normal limit independent of the limiting marked pair. Since those marks are tight, extending from compact sets proves the full three-way independence.

**5. Mean width and sharp second order.** Symmetry of Gaussian directions implies \(\mathbb Eh_{P_q}(-G)=\mathbb Eh_{P_q}(G)\). The support identity gives \(\mathbb Eh_{P_q}(G)=q/\sqrt\pi+\mathbb EB_q\). The exact expectation can also be evaluated by the convergent one-dimensional integral
\[
\mathbb EB_q=\int_0^\infty\left[1-F(t)^q\right]dt
-\int_{-\infty}^0F(t)^q\,dt.
\]
Standard Gaussian maximum tail bounds for \(F(t)^q\), with the Mills estimate on the right and the superexponential left tail at the \(a_q\)-scale, imply uniform integrability of \((B_q-b_q)/a_q\). Thus \(\mathbb EB_q=b_q+\gamma a_q+o(a_q)\). Inverting the normal tail yields
\[
 b_q=\sqrt{\log q}-\frac{\log\log q+\log(2\pi)}{2\sqrt{\log q}}+o\bigl((\log q)^{-1/2}\bigr),\quad
 a_q=\frac1{2\sqrt{\log q}}+o\bigl((\log q)^{-1/2}\bigr).
\]
Substitution gives the displayed width expansion, including its constant-order numerator correction. The normal-maxima asymptotics are classical inputs; the exact geometric decomposition and its marked realization are what connect them to this family of polytopes.

## Verification

`CHECK.py` is a standalone numerical and finite-enumeration checker using Python 3, NumPy and SciPy. Run `python3 CHECK.py`. It independently enumerates all \(q2^{q-1}\) tree indicator vectors for \(2\le q\le7\), comparing direct Gaussian support maximization to the claimed formula on 91 random objectives in each dimension (546 agreements). It also numerically verifies the exact bottleneck density normalization for five values of \(q\), the Gumbel cdf scaling in representative large dimensions, and the conditional exponential-surplus tail scaling. Its output ends in `GAUSSIAN_BRIDGE_POLYTOPE_PASS`. These computations validate finite instances and representative asymptotic diagnostics only; the infinite-dimensional limits follow from the preceding argument, not from these tests.

## Relationship to prior work

Albin, Clemens, Hoare, Poggi-Corradini, Sit and Tymochko (first public May 25, 2018) analyze fair edge usage and minimum expected overlap in random spanning trees. Aprile, Fiorini, Huynh, Joret and Wood (first public June 22, 2021) investigate extended formulations of graphic spanning-tree polytopes. Neither full text establishes the Gaussian support decomposition or the marked Gaussian–Gumbel–exponential limit here. The published study *Exact variance geometry of uniform bipartite spanning trees* treats uniformly sampled tree vertices and deterministic linear costs, not the Gaussian-exposed maximizing vertex. *Sharp Euclidean inball phases of complete-bipartite spanning-tree polytopes* studies fixed Euclidean supporting distances, not random supporting direction. *Exact variance and a nine-to-ten vertex extremal transition for bipartite spanning-tree overlap* studies pairs of uniformly chosen trees, not Gaussian optimizing trees. The general maximum spanning-tree algorithm and classical Gaussian extreme-value theorem are expressly not claimed as new. The bridge-index support decomposition and marked geometric fluctuation law are the claimed contribution; equivalence to an unindexed weighted-network extreme-value result cannot be excluded.

## Limitations

The result is restricted to the canonical two-hub complete-bipartite spanning-tree polytope and independent standard Gaussian objective coordinates. No formula for general \(K_{p,q}\) with \(p\ge3\), dependent edge weights, or full finite distribution of the Gaussian bulk support is asserted. The exact joint law concerns the bottleneck and the surplus, not arbitrary tree edge ranks. Its Gumbel and exponential limits are consequences of classical Gaussian tail behavior applied to this exact geometry. Independently refereed mathematical validation and exhaustive priority verification have not been performed.

## References

1. N. Albin, J. Clemens, D. Hoare, P. Poggi-Corradini, B. Sit and S. Tymochko, *Fairest edge usage and minimum expected overlap for random spanning trees*, arXiv:1805.10112, initial posting May 25, 2018, https://arxiv.org/abs/1805.10112.
2. M. Aprile, S. Fiorini, T. Huynh, G. Joret and D. R. Wood, *Smaller extended formulations for spanning tree polytopes in minor-closed classes and beyond*, arXiv:2106.11945, initial posting June 22, 2021, https://arxiv.org/abs/2106.11945.
3. *Exact variance geometry of uniform bipartite spanning trees*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-variance-geometry-of-uniform-bipartite-spanning-trees--10dc23028543.
4. *Sharp Euclidean inball phases of complete-bipartite spanning-tree polytopes*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-euclidean-inball-phases-of-complete-bipartite-spanning-tre--40615d09964e.
5. *Exact variance and a nine-to-ten vertex extremal transition for bipartite spanning-tree overlap*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-variance-and-a-nine-to-ten-vertex-extremal-transition-for--1c4136a0fe4a.
