# Complete signed-dimer Fourier spectrum and sharp recovery for the Chvátal graph

## Finding

Let \(G\) be the twelve-vertex Chvátal graph with the explicit numbered edges below, and let \(\mathcal M\) denote its perfect matchings. There are exactly \(52\) of them. Write \(E=E(G)\), so \(|E|=24\), and let \(\mu:\mathbb F_2^E\to\{0,1\}\) be the indicator of the perfect-matching incidence vectors. Consider the counting convolution \(Tf=\mu*f\) on functions on \(\mathbb F_2^E\), with counting-measure \(\ell^p\) norms.

For \(S\subseteq E\), the unnormalized Walsh multiplier is
\[
W(S)=\sum_{M\in\mathcal M}(-1)^{|S\cap M|}.
\]
Switching a set of edge signs at the edges incident to a vertex changes \(W\) only by an overall sign. After factoring out the group of all such vertex switches, every full frequency has one of \(8192\) reduced sign patterns and each reduced pattern occurs exactly \(2048\) times. The **complete reduced absolute spectrum** is:

| \(|W|\) | Reduced frequency multiplicity |
|---:|---:|
| 0 | 2536 |
| 4 | 2864 |
| 8 | 1708 |
| 12 | 574 |
| 16 | 304 |
| 20 | 120 |
| 24 | 52 |
| 28 | 24 |
| 32 | 8 |
| 52 | 2 |

Thus, for convolution over the **entire** \(24\)-dimensional edge cube,
\[
\operatorname{rank} T=5656\cdot 2048=11{,}583{,}488,
\qquad \operatorname{nullity} T=2536\cdot2048=5{,}193{,}728.
\]
Every surviving Fourier multiplier has absolute value at least \(4\), and the largest magnitude is \(52\). The positive-spectrum \(\ell^2\) condition ratio is exactly \(13\).

No character supported on zero or one edge vanishes. Among the \(\binom{24}{2}=276\) characters supported on exactly two edges, precisely **48** vanish. They consist exactly of incident edge pairs whose two edges occur in \(12\) and \(14\) of the \(52\) perfect matchings, respectively.

Let \(\mathcal R\subset\ell^p(\mathbb F_2^E)\) be the Fourier range of \(T\). For either endpoint \(p=1\) or \(p=\infty\), the minimum operator norm among **all** real or complex linear projections \(P\) onto \(\mathcal R\) is
\[
\boxed{\min_{P:\,P^2=P,\ \operatorname{ran}P=\mathcal R}
\|P\|_{\ell^p\to\ell^p}=\frac{5067}{256}.}
\]

## Assumptions and scope

The graph is the simple undirected graph on vertices \(\{0,1,\ldots,11\}\) with edges, in the stated order:

```
(0,1), (0,4), (0,6), (0,9), (1,2), (1,5), (1,7),
(2,3), (2,6), (2,8), (3,4), (3,7), (3,9), (4,5), (4,8),
(5,10), (5,11), (6,10), (6,11), (7,8), (7,11),
(8,10), (9,10), (9,11)
```

This labelled representative is isomorphic to the standard Chvátal graph, the classical smallest triangle-free, four-regular, four-chromatic graph. The result uses no edge weights, no monomers, and no normalization by \(52\). A perfect matching contains six pairwise vertex-disjoint edges covering all twelve vertices. Characters and Fourier transforms are over \(\mathbb F_2\), not over the vertex adjacency spectrum. The graph is not assumed planar.

## Proof

**1. Exhaustive, exact matching construction.** For a set \(U\) of unmatched vertices, take its smallest vertex \(u\) and, for each neighbor \(v\in U\), recursively enumerate perfect matchings of \(U\setminus\{u,v\}\) with edge \(uv\) added. The empty set has the sole empty matching. This recursion enumerates each matching once because the partner of the first vertex is unique. Applied to the explicit edge list it produces exactly \(52\) distinct six-edge masks. These can be independently tested by vertex disjointness and full coverage. For each edge \(e\), the count \(c_e=|\{M:e\in M\}|\) equals either \(12\) or \(14\); there are twelve edges of each kind. Each vertex is incident with precisely two edges of each kind. These integer assertions are reproduced in `verify_chvatal.py`.

**2. Gauge reduction and the full spectrum.** The edges incident to vertex \(v\) form its star \(\delta(v)\). Since any perfect matching meets \(\delta(v)\) in exactly one edge,
\[
W(S\mathbin\triangle\delta(v))=-W(S).
\]
As the graph is connected, its binary vertex-star span \(H\le\mathbb F_2^E\) has dimension \(12-1=11\). Choose the spanning tree selected by the ascending-edge-index construction in `verify_chvatal.py`; its eleven edge indices are
```
0, 1, 2, 3, 4, 5, 6, 7, 9, 15, 16
```
Every coset modulo \(H\) has a unique representative supported on the remaining thirteen chord edges. Let \(C\) denote these chords. For each \(x\in\mathbb F_2^C\), let \(b_x\) count matchings with chord-incidence vector \(x\). The reduced signed coefficients are **exactly**
\[
W_C(s)=\sum_{x\in\mathbb F_2^C}b_x(-1)^{\langle s,x\rangle}.
\]
An integer fast Walsh transform of the \(8192\) values \(b_x\) yields the table in the finding. As an independent calculation, a signed vertex-subset recursion, for each of the \(8192\) signings, calculates \(W_C(s)\) without using the \(b_x\) table; the outputs agree coefficient by coefficient. In addition, \(\sum_s W_C(s)^2=8192\cdot52\), consistent with the distinct chord-incidence masks. Each reduced coefficient has multiplicity \(|H|=2048\) in the original transform; the stated full rank and nullity follow. These are exact finite sums, not stochastic estimates.

**3. First cancellation support.** A single edge has multiplier \(52-2c_e\), equal to \(28\) or \(24\). For distinct edges \(e,f\) put \(c_{ef}=|\{M:e,f\in M\}|\). Inclusion-exclusion gives
\[
W(\{e,f\})=52-2(c_e+c_f)+4c_{ef}.
\]
If \(e,f\) share a vertex, \(c_{ef}=0\), and the multiplier vanishes exactly for the mixed incidence pair \(c_e=12,c_f=14\). Each vertex has two incident edges of each incidence type and hence four such mixed pairs. Distinct edges share at most one vertex, giving \(12\cdot4=48\) pairs. For disjoint edges, exact matching enumeration gives \(c_{ef}\ge2\) for mixed-type pairs and \(c_{ef}\ge3\) for pairs with two 14-incidence edges; pairs with two 12-incidence edges have \(W\ge4\) regardless. These bounds in the displayed formula exclude disjoint-pair zeros; all \(276\) pairs are also directly checked.

**4. Unrestricted optimum projection norm.** The Fourier multiplier of the canonical range projection \(P_0\) is \(1_{W\ne0}\). The range of \(T\) is translation invariant. If \(P\) is any real or complex projection onto this range, average \(\tau_aP\tau_{-a}\) over the finite translation group. The average is still a projection onto the same range (its restriction there is the identity, and its output lies there), commutes with translations, and has norm at most \(\|P\|\). Since a translation-invariant projection onto a specified Fourier range is unique, the average is \(P_0\); thus \(P_0\) minimizes every translation-invariant endpoint operator norm over **all** projections, without requiring them initially to be translation invariant.

Write \(p\) for the convolution kernel of \(P_0\). Its \(\ell^1\)- and \(\ell^\infty\)-operator norms are both \(\sum_{g\in\mathbb F_2^E}|p(g)|\). The support indicator \(1_{W\ne0}\) is invariant under \(H\), so Fourier orthogonality makes \(p\) vanish off \(H^\perp\), the thirteen-dimensional binary cycle space. Identifying that cycle space with \(\mathbb F_2^{13}\), its nonzero values are precisely
\[
p(y)=2^{-13}\sum_{s\in\mathbb F_2^{13}}1_{W_C(s)\ne0}(-1)^{\langle s,y\rangle}.
\]
The exact integer Walsh transform of the indicator has coefficient absolute sum \(162144\). Therefore
\[
\sum_y|p(y)|=\frac{162144}{8192}=\frac{5067}{256},
\]
which proves the claimed sharp norm simultaneously for real and complex projections at both endpoints.

## Verification

Run `python3 verify_chvatal.py` using Python 3 standard library only. It checks twelve vertices and twenty-four edges, triangle-freeness and the chromatic number, enumerates and validates 52 perfect matchings, derives 8192 reduced signed coefficients in **two different ways**, compares the entire exact spectrum, examines all one- and two-edge frequencies, and performs a second exact Walsh transform for the projection norm. Its stated output includes `PASS` and `projection 5067/256 full rank 11583488 nullity 5193728`. All arithmetic is integer or exact rational arithmetic. The finite exhaustive calculation is part of the proof of the finite assertion; it does not claim an infinite-family certificate.

## Relationship to prior work

Chvátal's original 1970 note establishes the canonical graph and its extremal chromatic character; it does not state signed perfect-matching Fourier coefficients. Björklund, Husfeldt, Kaski and Koivisto compute and tabulate the Chvátal graph's **Tutte polynomial**, an invariant of edge-subset connectivity; that polynomial is not the complete signed perfect-matching Fourier spectrum or the sharp range-projection norm. Goodall develops finite Fourier techniques for graph-polynomial and Tutte-Grothendieck invariants. Cimasoni and Giuliani–Jauslin–Lieb study Pfaffian techniques for dimer models under their respective graph/embedding assumptions. Those powerful general tools do not, in the inspected material, supply the exact 8192-class spectrum, the 48 minimum cancellation patterns, or the numerical projection constant for this graph. The present result is a graph-specific exact classification rather than a new general Pfaffian formalism.

## Limitations

The theorem concerns exactly this labelled representative (hence its isomorphism class), the unweighted binary perfect-matching indicator, and the stated Fourier normalization. It does not give an all-graph classification, a noise-robust algorithm beyond the sharp projection norm, or the best pseudoinverse norm for any separately chosen data model. The literature comparison is bounded, so an unpublished or unindexed equivalent exact spectral calculation is a genuine priority risk. The checked computational proof has not received an independent mathematical audit.

## References

- V. Chvátal (1970), *The Smallest Triangle-Free 4-Chromatic 4-Regular Graph*, Journal of Combinatorial Theory 9, 93–94, https://doi.org/10.1016/S0021-9800(70)80057-6.
- A. Björklund, T. Husfeldt, P. Kaski and M. Koivisto (first posted 16 November 2007), *Computing the Tutte polynomial in vertex-exponential time*, https://arxiv.org/abs/0711.2585, graph-specific appendix.
- A. Goodall (2008), *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis*, https://arxiv.org/abs/0806.4848.
- D. Cimasoni (2008), *Dimers on graphs in non-orientable surfaces*, https://arxiv.org/abs/0804.4772.
- A. Giuliani, I. Jauslin and E. H. Lieb (2015), *A Pfaffian formula for monomer-dimer partition functions*, https://arxiv.org/abs/1510.05027.
- D. Eppstein, dated 2 April 2009, *Chvátal graph* illustration, https://commons.wikimedia.org/wiki/File:Chv%C3%A1tal_graph.svg (date-stamped archival identification of the graph; not used to establish a spectral invariant).
