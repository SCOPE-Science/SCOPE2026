# Finite-core Fortuin–Kasteleyn reduction and mixed-Gaussian cluster fluctuations

## Finding

Fix an integer \(r\ge2\), a real cluster weight \(q>0\), and real activities \(a_1,\ldots,a_r>0\). For sufficiently large integers \(n\), put the Fortuin–Kasteleyn (FK) random-cluster measure on the complete bipartite graph \(K_{r,n}\), assigning probability parameter \(p_{i,n}=a_i/\sqrt n\) to every edge from distinguished hub \(i\in[r]\) to any of the \(n\) ordinary vertices. The weight of a bond configuration \(\omega\) is proportional to
\[
q^{k(\omega)}\prod_{e}\,p_e^{\omega_e}(1-p_e)^{1-\omega_e},
\]
where \(k(\omega)\) counts all connected components, including isolated vertices.

Define a graph \(H_n\) on the \(r\) hubs: join two hubs if at least one ordinary vertex has open bonds to both. Let \(C_n\subseteq[r]\) be the component of hub \(1\) in \(H_n\), and let \(Q_n\) be the number of ordinary vertices in the open cluster of hub \(1\) in the original bipartite graph.

Define \(\lambda_{ij}=a_i a_j/q\) and \(\pi_{ij}=1-e^{-\lambda_{ij}}\) for \(1\le i<j\le r\). Let \(H\) have the FK random-cluster law on the finite complete graph \(K_r\), with edge parameters \(\pi_{ij}\) and the *same* cluster weight \(q\):
\[
\Pr(H=F)=\frac{q^{k(F)}\prod_{ij\in E(F)}\pi_{ij}\prod_{ij\notin E(F)}(1-\pi_{ij})}{\displaystyle\sum_{F'\subseteq K_r}q^{k(F')}\prod_{ij\in E(F')}\pi_{ij}\prod_{ij\notin E(F')}(1-\pi_{ij})}.
\]
Let \(C\) be the hub-\(1\) component of \(H\). Independently of \(H\), take independent \(Z_i\sim\mathcal N(0,a_i/q)\). Then the entire projected hub graph and the centered number of ordinary vertices obey the joint limit
\[
\boxed{\left(H_n,\frac{Q_n-\sqrt n\sum_{i\in C_n}a_i/q}{n^{1/4}}\right)
\ \Longrightarrow\ \left(H,\sum_{i\in C}Z_i\right).}
\]
In particular, \(Q_n/\sqrt n\Longrightarrow\sum_{i\in C}a_i/q\), and conditional on the limiting hub component the second-order fluctuation is Gaussian with variance \(\sum_{i\in C}a_i/q\).

There is also an *exact*, all-finite-size reduction of the FK partition function to a product measure tilted by a bounded finite-core component factor, as established below. For two hubs, the resulting limiting probability that they connect is
\[
\boxed{\Pr(1\leftrightarrow2)=\frac{e^{a_1a_2/q}-1}{q+e^{a_1a_2/q}-1}.}
\]
For three or more hubs the limiting edges are generally **not independent** when \(q\ne1\). For instance, on a triangle with common limiting edge probability parameter \(\pi\in(0,1)\), the conditional chance that edge \(12\) is open is \(\pi\) when edges \(13\) and \(23\) are both open, but it is \(\pi/[\pi+q(1-\pi)]\) when both are closed. The two differ for every \(q\ne1\).

## Assumptions and scope

All limits are along integer \(n\to\infty\), with \(r\), \(q\), and each \(a_i\) fixed. No uniformity is asserted when these parameters themselves vary with \(n\). Parallel hub connections through distinct ordinary vertices are allowed; \(H_n\) records a simple edge if at least one such connection exists. The theorem applies to positive noninteger as well as integer FK cluster weight. In the special case \(q=1\), it reduces to independent bond percolation, already a known separate result; the substantive FK distinction is \(q\ne1\).

Write \(S_v\subseteq[r]\) for the set of hubs connected by open bonds to ordinary vertex \(v\). Let \(N_0\) count vertices with \(S_v=\varnothing\); for each \(i\), let \(N_i\) count vertices with \(S_v=\{i\}\); and for each pair \(i<j\), let \(B_{ij}\) count vertices with \(S_v=\{i,j\}\). All quantities are evaluated in the full FK measure unless explicitly marked otherwise.

## Proof

**1. Finite-volume factorization.** For each subset \(S\subseteq[r]\), let
\[
b_n(S)=\prod_{i\in S}p_{i,n}\prod_{i\notin S}(1-p_{i,n}),\qquad
w_n(S)=q^{\mathbf1\{S=\varnothing\}}b_n(S).
\]
Set \(W_n=\sum_S w_n(S)=1+(q-1)\prod_i(1-p_{i,n})\), which is strictly positive. Let \(\nu_n(S)=w_n(S)/W_n\), and sample \(n\) independent columns \(S_v\) with this law. Form a simple hub graph by connecting every pair in \(S_v\) for every column of cardinality at least two. Denote its component count by \(\kappa(H_n)\).

Every ordinary vertex with no open bond is an isolated FK component. Every other ordinary vertex is attached to a component containing at least one hub, and components among hubs are exactly those represented by \(H_n\). Consequently, for *every configuration*, not merely asymptotically,
\[
k(\omega)=N_0+\kappa(H_n).
\]
The original FK partition function therefore has the exact identity
\[
\boxed{\mathcal Z_{r,n}=W_n^n\mathbb E_{\nu_n^{\otimes n}}[q^{\kappa(H_n)}].}
\]
The full FK law of column types is the law \(\nu_n^{\otimes n}\) with Radon–Nikodym multiplier proportional to \(q^{\kappa(H_n)}\). Because the hub count is fixed,
\[
0<\min(q,q^r)\le q^{\kappa(H_n)}\le\max(q,q^r)<\infty.
\]
This boundedness is critical for passing asymptotic limits through the tilt.

**2. Rare bridges and singleton fluctuations under the product law.** The column probabilities satisfy, as \(n\to\infty\),
\[
\nu_n(\{i\})=\frac{a_i}{q\sqrt n}+O(n^{-1}),\qquad
\nu_n(\{i,j\})=\frac{a_i a_j}{qn}+O(n^{-3/2}),
\]
while \(\sum_{|S|\ge3}\nu_n(S)=O(n^{-3/2})\). Hence the probability of any triple-or-higher connector among the \(n\) ordinary vertices is \(O(n^{-1/2})\).

The multinomial triangular-array generating function yields joint convergence
\[
\left((B_{ij})_{i<j},\left(\frac{N_i-a_i\sqrt n/q}{n^{1/4}}\right)_{i=1}^r\right)
\Longrightarrow \left((P_{ij})_{i<j},(Z_i)_{i=1}^r\right),
\]
where the \(P_{ij}\) are independent Poisson random variables with means \(\lambda_{ij}\), and the \(Z_i\) are independent centered Gaussians with variances \(a_i/q\), independent of all \(P_{ij}\). To see this directly, expand the logarithm of the one-column joint moment-generating function, centering the singleton counts. The terms of order one consist exactly of
\[
\sum_{i<j}\lambda_{ij}(e^{t_{ij}}-1)+\frac12\sum_i(a_i/q)s_i^2.
\]
All mixed terms vanish because pair-event probabilities are order \(n^{-1}\), singleton-event probabilities are order \(n^{-1/2}\), and there are only finitely many types. The finite difference between the exact singleton means and \(a_i\sqrt n/q\) is \(O(1)\) and disappears after dividing by \(n^{1/4}\).

**3. Passing the FK tilt.** With probability tending to one, all multisite connectors have cardinality two; the finite hub graph \(H_n\) then has precisely the edges for which \(B_{ij}>0\). The product-law limit is the graph obtained by independently retaining pair \(ij\) with probability \(1-e^{-\lambda_{ij}}\). The bounded multiplier from step 1 depends in the limit only on this finite graph. Thus convergence under the tilted measure follows by bounded convergence for any bounded continuous function of the Gaussian coordinates and graph coordinates. Its normalizing constant converges to \(\mathbb E[q^{k(H^{(0)})}]>0\), where \(H^{(0)}\) is the independent-edge limiting graph. The resulting tilted graph law is exactly the stated finite \(q\)-random-cluster law; the independent Gaussian vector retains its original law because the tilt depends only on the graph.

**4. Component size.** Let \(R_n=\sum_{v}\mathbf1\{|S_v|\ge2\}\). Step 2 and bounded tilt imply \(R_n=O_{\Pr}(1)\). Every ordinary vertex with exactly one open edge belongs to the component of hub \(1\) if and only if its unique hub lies in \(C_n\). Consequently,
\[
\left|Q_n-\sum_{i\in C_n}N_i\right|\le R_n=O_{\Pr}(1).
\]
This is negligible on the \(n^{1/4}\) scale. The joint limit of the finite hub graph and singleton Gaussian coordinates from step 3 completes the proof by the continuous-mapping theorem on a finite discrete graph space.

**5. Two-hub formula and genuine dependence.** For two hubs the limiting independent-edge graph has no-edge probability \(e^{-\lambda_{12}}\), which has FK weight \(q^2\); its connected alternative has weight \(q\). Normalizing gives the displayed logistic-like expression. On three hubs, conditioning on the other two edges leaves edge \(12\) either as a cycle-closing edge (no change of component count, chance \(\pi\)) or as a component-merging edge (relative odds divided by \(q\), chance \(\pi/[\pi+q(1-\pi)]\)). Hence the finite-core limit cannot generally be represented by independently rescaling bond probabilities when \(q\ne1\).

## Verification

The standalone script `verify.py` enumerates the full FK edge state space of \(K_{3,n}\) for \(n=1,2,3\) and three rational values of \(q\). It compares the original bond-weight partition function and two-hub connectivity weight with independent-column reduction, using exact rational arithmetic. It also checks the limiting triangle conditional-probability identities for four cluster weights and three positive intensities. Running `python3 verify.py` yielded `PASS: 66 assertions, exact finite-state partition/connectivity and limiting triangle tests`.

The exact finite-size identity, the asymptotic expansion and the probabilistic limit are proved analytically above. Enumerating finitely many small systems is not an infinite-volume proof; the computational checks verify the construction and algebra for reproducibility.

## Relationship to prior work

The FK representation and its Potts coupling are classical [1,2]. Complete-graph FK critical phenomena with both sides growing have been studied [3], while random graphs built by adding small connected atoms have independent-edge and clustering asymptotic frameworks [4]. These results motivate the construction, but the particular fixed-hub bipartite regime, its finite-core FK limit, and the joint \(n^{1/4}\)-scale fluctuation statement are not claimed or established by the examined portions of those sources. Ordinary independent bond percolation at \(q=1\) already admits a corresponding mixed-Gaussian result; the present mathematical distinction is the retained FK component weight and its induced dependence of effective hub edges for \(q\ne1\).

The representation can also be understood for integer \(q\) by integrating out ordinary Potts spins at weak coupling. That interpretation alone does not supply the FK cluster-count and mixed fluctuation conclusion for all positive real \(q\). Searches did not find a directly equivalent statement, but cannot prove global historical originality.

## Limitations

The hub population is fixed. Neither growing numbers of hubs nor arbitrary nonconstant local cluster weights are covered. No rate of convergence of the full fluctuation law is asserted, and no infinite-volume lattice critical exponent is claimed. The result is a finite-core crossover rather than a thermodynamic singularity. For \(q=1\) the graph limit is independent-edge percolation and not a new assertion. The connection between weak Potts couplings and effective interactions is classical; priority for an independently stated FK finite-core limit remains subject to specialist review. General asymptotic frameworks or unindexed papers might contain a broader theorem implying this special result.

## References

[1] R. G. Edwards and A. D. Sokal, “Generalization of the Fortuin–Kasteleyn–Swendsen–Wang representation and Monte Carlo algorithm,” *Physical Review D* **38** (1988), 2009–2012. https://doi.org/10.1103/PhysRevD.38.2009

[2] G. Grimmett, “The Random-Cluster Model,” arXiv:math/0205237, first posted 2002-05-23. https://arxiv.org/abs/math/0205237

[3] B. Bollobás, G. Grimmett, and S. Janson, “The random-cluster model on the complete graph,” *Probability Theory and Related Fields* **104** (1996), 283–317. https://doi.org/10.1007/BF01213683

[4] B. Bollobás, S. Janson, and O. Riordan, “Sparse random graphs with clustering,” arXiv:0807.2040, first posted 2008-07-13. https://arxiv.org/abs/0807.2040
