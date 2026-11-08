# Strict weighted arboreal-gas edge anticorrelation on \(K_1*C_4\) and every subdivision

## Finding

**Theorem.** Let \(W=K_1*C_4\) be the simple five-vertex wheel, and let \(G\) be obtained from \(W\) by subdividing edges finitely many times (possibly zero times, independently for each edge). Give every edge \(e\) of \(G\) an arbitrary positive real fugacity \(a_e\). Choose a spanning forest \(F\) from *all* acyclic subsets of \(E(G)\), including disconnected forests and isolated vertices, with law
\[
\Pr(F=A)=\frac{\prod_{e\in A}a_e}{Z_G(\mathbf a)},\qquad
Z_G(\mathbf a)=\sum_{A\subseteq E(G):\ A\text{ acyclic}}\prod_{e\in A}a_e.
\]
Then for every pair of **distinct** edges \(e\ne f\),
\[
\boxed{\operatorname{Cov}(\mathbf1_{\{e\in F\}},\mathbf1_{\{f\in F\}})<0.}
\]
Thus the multivariate forest polynomial of the five-vertex wheel is strictly Rayleigh at every positive point, and this remains true under arbitrary finite edge subdivisions.

## Assumptions and scope

All graphs are finite, undirected, without loops; subdivisions introduce distinct new degree-two vertices. Every parameter \(a_e\) is strictly positive and may differ from every other parameter. No upper or lower fugacity bound is imposed. The polynomial is the *unrooted all-forest* polynomial, not a spanning-tree determinant and not a rooted-forest polynomial. A series subdivision means replacing an edge \(uv\) with a path \(u-w-v\), where \(w\) is a new vertex; iterating this operation gives the claimed graph family.

For an edge \(e\), write \(\partial_e Z\) for differentiation with respect to \(a_e\). For distinct edges, the Rayleigh difference
\[
R_{ef}= (\partial_e Z)(\partial_f Z)-Z\partial_{ef}Z
\]
satisfies \(\operatorname{Cov}(\mathbf1_e,\mathbf1_f)=-a_ea_f R_{ef}/Z^2\). Therefore positive Rayleigh differences prove precisely the announced strict inequalities.

## Proof

**1. Exact multivariate wheel certificate.** Label the hub \(0\), the cyclic rim \(1,2,3,4\), and index the eight edges in the order
\[
(01),(02),(03),(04),(12),(14),(23),(34).
\]
Let their weights be \(a_0,\ldots,a_7\). For each mask \(m\in\{0,1\}^8\), let \(\chi(m)=1\) when the selected edges contain no cycle, and zero otherwise. The full, explicitly finite polynomial is
\[
Z_W(\mathbf a)=\sum_{m\in\{0,1\}^8}\chi(m)\prod_{i=0}^7 a_i^{m_i}.
\]
Direct union-find cycle testing over the \(256\) masks gives exactly \(134\) acyclic subsets, and defines every coefficient of the polynomial without interpolation or probabilistic sampling. The above formula can equally be evaluated by hand using the displayed list of edges.

Because \(Z_W\) is multiaffine, \(R_{ij}\) is independent of \(a_i,a_j\). The wheel's dihedral symmetry reduces its \(28\) unordered pairs to six classes, with representatives
\[
(0,1),\ (0,2),\ (0,4),\ (2,4),\ (4,5),\ (4,7).
\]
For five representative pairs, direct exact integer polynomial arithmetic from this finite sum gives the following complete coefficient certificates:

| Pair of edge indices | Nonzero coefficients | Smallest coefficient | Negative or zero stored coefficients |
|---|---:|---:|---:|
| \((0,1)\) | 172 | strictly positive | none |
| \((0,2)\) | 90 | strictly positive | none |
| \((0,4)\) | 240 | strictly positive | none |
| \((4,5)\) | 149 | strictly positive | none |
| \((4,7)\) | 93 | strictly positive | none |

The exact algorithm, not a floating-point test, is `check_wheel.py`: it constructs \(Z_W\) by graph-acyclicity checks, differentiates sparse polynomial dictionaries, enumerates the complete support of each \(R_{ij}\), and asserts strictly positive integer coefficients. Positive variables make each such nonzero polynomial strictly positive.

**2. The only exceptional coefficient pattern.** For \((i,j)=(2,4)\), some coefficients have negative signs, so coefficientwise positivity does not suffice. Put
\[
\alpha=a_0,\quad x=a_1,\quad \delta=a_3,\quad t=a_6,\quad u=a_5,\quad v=a_7,
\]
and define the following positive polynomials:
\[
\begin{aligned}
h&=(1+u)(1+v),\\
S&=\alpha\delta+\alpha u+\alpha v+\alpha+\delta u+\delta,\\
U&=S+h,\\
V&=\alpha\delta u+\alpha\delta v+\alpha\delta+\alpha u^2
  +2\alpha uv+2\alpha u+\alpha v^2+2\alpha v+\alpha
  +\delta u^2+\delta u,\\
Q&=UV,\qquad P=\frac{uvS^2+Q}{h}.
\end{aligned}
\]
The finite exact polynomial calculation certifies both that \(P\) is a polynomial with strictly positive integer coefficients and that the complete Rayleigh difference has the identity
\[
R_{2,4}=uvh\,x^2+(uvh-2uv\,tS)x+t(t+1)P.
\]
Since \(hP-uvS^2=Q=UV\), completion of the square gives the stronger identity
\[
\boxed{
R_{2,4}=uvh\left(x-\frac{tS}{h}\right)^2
       +uvh\,x+tP+\frac{t^2UV}{h}>0.
}
\]
Every term on the right is nonnegative, and the last three are positive when all six fugacities are positive. `check_wheel.py` verifies the three identities by exact coefficient-dictionary equality and positivity of all coefficients of \(P,U,V\), not by numerical sampling. This completes all six wheel orbits and hence all \(28\) distinct-edge pairs.

**3. Preservation by subdividing a nonbridge.** Consider any finite graph \(H\) with strictly negative correlations between every two distinct edges, and assume all edges lie on cycles. Replace an edge \(g\) by two consecutive edges with fugacities \(a,b>0\). Set
\[
q=1+a+b,\qquad \beta=\frac{ab}{q},\qquad u=\frac a q,\quad v=\frac b q.
\]
The new forest polynomial is exactly
\[
Z_{H'}(\ldots,a,b)=q\,Z_H(\ldots,\beta).
\]
Indeed, the new two-edge path has total weight \(q\) when at most one path edge is selected, corresponding to absence of the old edge, and weight \(ab=q\beta\) when both are selected, corresponding to presence of that edge. A cycle in the new graph uses both new path edges, and contracts to an old cycle; thus this correspondence preserves precisely acyclicity.

Let \(Y\) indicate that both new edges were selected (the effective old-edge indicator), with \(p=\Pr(Y=1)\). Conditional on \(Y=0\), the first new edge appears with probability \(u\) and the second with probability \(v\), never simultaneously; conditional on \(Y=1\), both appear surely. For old edges \(h\ne g\), conditional expectations of the new edge indicators are \(u+(1-u)Y\) and \(v+(1-v)Y\). Consequently, their covariance with any edge outside the new path is \((1-u)\operatorname{Cov}(Y,X_h)\) and \((1-v)\operatorname{Cov}(Y,X_h)\), respectively, which are strictly negative. The covariance of two unchanged edges is unchanged and remains strictly negative.

For the two edges of the new path, conditioning yields exactly
\[
\operatorname{Cov}(X_a,X_b)
=(1-p)\left[p(1-u)(1-v)-uv\right].
\]
Write \(Z_0\) for the forest partition function on \(H\setminus g\) and \(Z_1\) for the sum of weights of those forests on \(H\setminus g\) that remain acyclic after adjoining \(g\). Then \(p=\beta Z_1/(Z_0+\beta Z_1)\). As \(g\) is not a bridge, a path between its endpoints exists in \(H\setminus g\). A subforest of that path contributes strictly positively to \(Z_0-Z_1\). Thus \(Z_1<Z_0\), so
\[
p<\frac\beta{1+\beta}=\frac{ab}{(1+a)(1+b)}=\frac{uv}{(1-u)(1-v)},
\]
and the covariance of the new pair is strictly negative. Subdividing an edge of a bridgeless graph preserves the property that every edge is on a cycle; the argument iterates. The wheel is bridgeless, completing the proof for every finite subdivision. \(\square\)

## Verification

The sole necessary computational certificate is the included dependency-free Python 3 file `check_wheel.py`, run as `python3 check_wheel.py` with assertions enabled. It independently generates all forests from the explicitly listed eight edges; differentiates \(Z_W\) exactly in integer coefficient dictionaries; confirms the six symmetry-orbit identities, five strictly positive coefficient supports (term counts \(172,90,240,149,93\)), and the exceptional exact polynomial equality and square factorization. It additionally evaluates all \(28\) covariances at each of \(48\) independently generated nonuniform positive rational fugacity choices, giving \(1344\) independent exact probability comparisons. These examples are supplementary stress tests; the universal statement for all positive real fugacities follows from the analytic/polynomial certificates, not from those finite tests. No claim about correlation among three or more edge events is made.

## Relationship to prior work

Negative correlation for the all-forest (arboreal-gas) measure at arbitrary edge fugacities is a standing general problem. Huang (first public November 2, 2023) studies it, proves selected large-common-fugacity cases, and gives a general series-suppression theorem; the subdivision reduction in this proof is a direct explicit version of that known structural device. Erickson proves the Rayleigh property for series-parallel graphs, a class that excludes the 3-connected wheel \(K_1*C_4\). Semple and Welsh cover graph classes assembled from specified small blocks (not this wheel core). Grimmett and Winkler's finite-graph results concern uniform forest measures.

Bado's later paper proves strict correlations for all wheels **at unit edge weights**, employing a multivariate transfer matrix but specializing to unit weights for its correlation estimates. The present claim is restricted to the five-vertex wheel core but allows **every independent positive real edge fugacity** and proves that this stronger property survives arbitrary subdivisions. Çiçeksiz and Ravichandran (September 30, 2026) address common fugacities and high-fugacity regimes for broader graphs; those results do not imply arbitrary heterogeneous positive weights on this graph. Publication-priority assessment remains qualified because Bado's complete publisher text and some older comparisons could not be fully inspected; no general uniqueness claim is asserted.

## Limitations

This establishes only **pairwise** strict negative edge correlations. It does not prove the full negative-association property, nor a theorem for general wheels with five or more rim vertices or for all graphs. All edge weights must be positive; at zero fugacity, strictness can fail. The finite exact certificate enumerates only \(K_1*C_4\) and is supplemented by an analytic induction for its subdivisions, rather than an exhaustive verification over infinitely many graphs. Independent mathematical review and broader historical-priority verification have not been performed.

## References

- X. Huang, *On Negative Correlation of Arboreal Gas on Some Graphs*, arXiv:2311.00965, first version November 2, 2023. https://arxiv.org/abs/2311.00965
- A. Erickson, *Sums of squares and negative correlation for spanning forests of series parallel graphs*, arXiv:1008.3660 (2010); *Australasian Journal of Combinatorics* 52 (2012), 75–87. https://arxiv.org/abs/1008.3660
- C. Semple and D. Welsh, *Negative Correlation in Graphs and Matroids*, 2008.
- G. Grimmett and D. Winkler, *Negative association in uniform forests and connected graphs*, 2004. https://arxiv.org/abs/math/0302185
- I. O. Bado, *Negative edge correlation for uniform random forests on wheel graphs*, online 2026, journal issue 2027. https://doi.org/10.1016/j.spl.2026.110960
- R. A. Çiçeksiz and M. Ravichandran, *Negative Correlations for Forests and the \(q<1\) Random Cluster Model*, arXiv:2610.00549, first version September 30, 2026. https://arxiv.org/abs/2610.00549
