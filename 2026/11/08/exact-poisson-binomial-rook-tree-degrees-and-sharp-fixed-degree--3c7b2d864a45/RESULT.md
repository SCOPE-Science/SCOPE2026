# Exact Poisson-binomial rook-tree degrees and sharp fixed-degree leaf extrema

## Finding

Let \(m,n\ge2\) be integers, \(G_{m,n}=K_m\square K_n\) the Cartesian rook graph, \(T_{m,n}\) a uniformly sampled spanning tree, and \(D_{m,n}\) the degree in \(T_{m,n}\) of any fixed vertex. Set \(s=m+n\), \(p_0=2/s\), \(p_m=(m+1)/(ms)\), and \(p_n=(n+1)/(ns)\). Then the **exact finite-size law** is

\[
D_{m,n}\overset{d}=1+X_0+X_m+X_n,
\qquad X_0\sim\operatorname{Bernoulli}(p_0),\quad
X_m\sim\operatorname{Binomial}(m-2,p_m),\quad
X_n\sim\operatorname{Binomial}(n-2,p_n),
\]

where the three variables on the right are independent (with zero-trial binomials interpreted as zero). In particular, the leaf probability and expected leaf fraction are both exactly

\[
L_{m,n}=\Pr(D_{m,n}=1)=(1-2/s)(1-p_m)^{m-2}(1-p_n)^{n-2}.
\]

For every fixed integer \(s\ge6\), among all \(m,n\ge2\) with \(m+n=s\), the value \(L_{m,n}\) is **strictly minimized** when \(\{m,n\}=\{\lfloor s/2\rfloor,\lceil s/2\rceil\}\), and **strictly maximized** at \(\{m,n\}=\{2,s-2\}\). Up to swapping factors, the extremizers are unique. At \(s=4,5\) the only possibilities are symmetric to each other. Moreover, for all \(m,n\ge2\),

\[
d_{\mathrm{TV}}\bigl(\mathcal L(D_{m,n}),\mathcal L(1+\operatorname{Pois}(1))\bigr)\le\frac{17}{4(m+n)}.
\]

This final estimate is quantitative; the existence of the universal Poisson local limit on high-degree regular graphs is prior work, not claimed as new.

## Assumptions and scope

The graph is finite, unweighted and simple; each spanning tree has equal probability. Every vertex is equivalent by automorphisms of the Cartesian product, so the displayed leaf probability also equals the expected fraction of leaves. The optimization fixes the **original graph degree** \(s-2\), not its number of vertices \(mn\). The exact law and inequality include the boundary \(m=2\) or \(n=2\).

## Proof

**1. Spectral decomposition.** Write \(J_r\) for the all-ones \(r\times r\) matrix, \(Q_r=J_r/r\) and \(P_r=I_r-Q_r\). With graph Laplacian \(\mathcal L=mP_m\otimes I_n+nI_m\otimes P_n\), its Moore–Penrose inverse is

\[
\mathcal L^+=\frac1mP_m\otimes Q_n+\frac1nQ_m\otimes P_n+\frac1{m+n}P_m\otimes P_n.
\]

For the root \(v=(0,0)\), orient all incident edges away from \(v\). Let \(b_e\) be the corresponding signed incidence vector and define their transfer-current matrix \(K=(b_e^{\mathsf T}\mathcal L^+ b_f)_{e,f\sim v}\). Index first the \(m-1\) edges changing the first coordinate, and then the \(n-1\) edges changing the second coordinate. Direct substitution into the displayed pseudoinverse gives

\[
K=\begin{pmatrix}
\alpha(I_{m-1}+J_{m-1}) & s^{-1}J_{m-1,n-1}\\
s^{-1}J_{n-1,m-1} & \beta(I_{n-1}+J_{n-1})
\end{pmatrix},\qquad
\alpha=\frac{m+1}{ms},\quad\beta=\frac{n+1}{ns}.
\]

**2. Exact characteristic polynomial.** Within the first and second coordinate groups, zero-sum vectors have eigenvalues \(\alpha\) and \(\beta\), of multiplicities \(m-2\) and \(n-2\). The remaining orthonormal constant-vector sector is represented by

\[
B=\frac1s\begin{pmatrix}
m+1 & \sqrt{(m-1)(n-1)}\\
\sqrt{(m-1)(n-1)} & n+1
\end{pmatrix}.
\]

Its trace is \(1+2/s\) and determinant \(2/s\), so its eigenvalues are exactly \(1\) and \(2/s\). For a uniform spanning tree, the transfer-current determinant theorem (equivalently, the weighted matrix-tree theorem plus the matrix determinant lemma) states

\[
\mathbb E[z^{D_{m,n}}]=\det\bigl(I+(z-1)K\bigr).
\]

Thus the determinant factors into \(z(1+p_0(z-1))(1+p_m(z-1))^{m-2}(1+p_n(z-1))^{n-2}\). Since these factors are probability generating functions of independent Bernoulli sums and probability generating functions determine finite distributions, this proves the exact law.

**3. Sharp extremizers.** The factor \(1-2/s\) does not depend on the split. Set, for real \(t\in[2,s-2]\),

\[
f_s(t)=(t-2)\log\left(1-\frac{t+1}{st}\right).
\]

Then \(\log L_{m,s-m}=\log(1-2/s)+f_s(m)+f_s(s-m)\), and explicit differentiation yields

\[
f_s''(t)=\frac{(4s-5)t-2}{t^2((s-1)t-1)^2}>0.
\]

Hence \(f_s'(t)-f_s'(s-t)<0\) for \(t<s/2\). The symmetric sum decreases strictly toward \(s/2\) and increases strictly afterward. Its minimum occurs at the closest integer split and maximum at the two endpoints. The stated small-\(s\) cases are immediate.

**4. Uniform limit bound.** For \(m,n\ge2\), the independent Bernoulli summands have total mean \(\mu=1-2/(mn)\). A standard Poisson coupling and Le Cam's inequality give

\[
d_{\rm TV}(D_{m,n},1+\operatorname{Pois}(1))\le
p_0^2+(m-2)p_m^2+(n-2)p_n^2+\frac2{mn}.
\]

Because \(p_0=2/s\), \(p_m,p_n\le3/(2s)\), and \(mn\ge s\), the right-hand side is at most \(9/(4s)+2/s=17/(4s)\). No limiting relative-aspect-ratio hypothesis is required.

## Verification

The included `VERIFY.py` independently constructs the graph Laplacian, evaluates weighted matrix-tree determinants with exact integers, and checks the predicted degree PGF with exact rational arithmetic for small rectangular rook graphs. It also enumerates all spanning trees of several small instances, compares complete degree histograms, and verifies finite-split leaf extrema. Running `python VERIFY.py` on the included checker prints `VERIFY_OK 2522 exact assertions`. These finite checks corroborate the formulas; the infinite quantifier and asymptotic assertions follow from the preceding proof, not from enumeration.

## Relationship to prior work

Hladký, Nachmias and Tran (2017) analyze UST local limits for dense graph families. Nachmias and Peres (2020), Theorem 1.1, prove a Poisson(1) conditioned branching-process local limit for **all** regular connected graph sequences with degree tending to infinity; this already implies the asymptotic marginal \(1+\operatorname{Pois}(1)\) law and is not reproduced here as a novelty claim. Rapoport (2023), Sections 3–4, gives a general finite-graph degree-field probability framework from transfer currents, and explicitly works out the complete graph. These general methods provide the starting principles, while the evaluated two-class rook graph kernel, exact all-parameter independent-summands law, explicit uniform rate and fixed-original-degree leaf extremization are the additional specific results assessed here.

An accessible prior result on the **covariance of tree degrees at adjacent rook-graph vertices** concerns two different vertices and does not determine this marginal distribution or the balancing extremum. General transfer-current formulas do permit a calculation for this graph and remain a historical-priority qualification; no independent originality certification is claimed.

## Limitations

The comparison fixes \(m+n\), hence a constant original graph degree but a varying number of vertices. This theorem does not determine joint distributions at two or more vertices, full tree shape or the distribution of the total leaf count. The fixed-degree leaf extremality and exact finite-degree factorization have no independent priority audit; any overlooked exact table or specialization of the general formulas could alter the originality assessment. The deterministic checker does not certify an infinite theorem independently.

## References

1. J. Hladký, A. Nachmias, T. Tran, *The local limit of the uniform spanning tree on dense graphs*, arXiv:1711.09788, initial public version 2017-11-27. https://arxiv.org/abs/1711.09788
2. A. Nachmias, Y. Peres, *The local limit of uniform spanning trees*, arXiv:2011.08833, initial public version 2020-11-17. https://arxiv.org/html/2011.08833v1
3. A. Rapoport, *Correlations in uniform spanning trees: a fermionic approach*, arXiv:2312.14992, initial public version 2023-12-22. https://arxiv.org/abs/2312.14992
