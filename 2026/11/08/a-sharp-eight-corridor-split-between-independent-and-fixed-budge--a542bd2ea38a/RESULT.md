# A sharp eight-corridor split between independent and fixed-budget ecological connectivity rankings

## Finding

Consider an idealized landscape with a designated source habitat \(s\), a destination habitat \(t\), and distinct undirected dispersal corridors. Parallel corridor labels represent separately usable routes. A landscape has successful functional connectivity if its usable-corridor subgraph contains a path from \(s\) to \(t\). Under protocol I every corridor operates independently with probability \(p\in(0,1)\). Under protocol F exactly \(k\) of the \(m\) corridors operate, chosen uniformly among the \(\binom{m}{k}\) subsets.

Within the two-terminal series-parallel class, **eight corridors are the smallest possible number** for two networks which (i) have the same shortest source–destination path length at least two and the same minimum corridor-cut cardinality at least two, (ii) have strictly ranked connectivity probabilities in the same direction under protocol I for every \(p\in(0,1)\), but (iii) reverse that ranking under protocol F for at least one value of \(k\).

Two eight-corridor witnesses are as follows, where all displayed edge labels are separate corridor identities:

- Network A has vertices \(s,t,u,v,w,x,y\) and corridors \(su,ut,sv,vt,vw,wx,xy,yt\).
- Network B has vertices \(s,t,a,b,c,d\) and corridors \(sa,ab,bt,sc,ct,cd,dt_1,dt_2\); \(dt_1\) and \(dt_2\) are distinct parallel corridors.

Both have shortest \(s\)-to-\(t\) path length \(2\) and minimum \(s\)-to-\(t\) edge cut \(2\). For their independent-operation reliabilities,
\[
R_A(p)-R_B(p)=p^2(1-p)^2\bigl(2p^4-p^2-p+1\bigr)>0
\quad(0<p<1).
\]
Yet if precisely five corridors operate,
\[
\Pr_A(s\leftrightarrow t\mid k=5)-\Pr_B(s\leftrightarrow t\mid k=5)=-\frac1{56}.
\]
At independent survival \(p=1/2\) the same contrast is \(R_A(1/2)-R_B(1/2)=3/128>0\).

## Assumptions and scope

- Finite undirected **series-parallel two-terminal multigraphs**, built from a single labeled edge by taking series and parallel compositions. Every leaf edge is a distinct corridor; parallel leaves are independent in protocol I and independently selectable in protocol F. Graphs need not have equal habitat-vertex counts, and the witness has seven versus six vertices.
- Terminal habitat vertices are permanently viable. Corridor operability only determines the existence of at least one traversable path. The model makes no claim about dispersal travel times, animal behavior, effective genetic exchange or long-run metapopulation persistence.
- For the sharp-minimum assertion, compare pairs with equal shortest terminal distance \(d\ge2\) and equal minimum terminal edge-cut size \(c\ge2\), and exactly \(m\) corridors each. The comparison is not extended to arbitrary non-series-parallel graphs, vertex failures, heterogeneous survival probabilities or dependence beyond exact-count sampling.
- A strict rank reversal means \(R_A(p)>R_B(p)\) for all \(0<p<1\), yet for some integer \(k\), \(C_{A,k}<C_{B,k}\), where \(C_{G,k}\) counts successful \(k\)-corridor subsets. Interchanging A and B is equivalent.

## Proof

**Exact witness.** Let \(C_{G,k}\) count the subsets of exactly \(k\) working edges which connect the two terminals. A direct subset enumeration, independently reproduced by series-parallel polynomial operations, yields for \(k=0,1,\ldots,8\):
\[
(C_{A,k})=(0,0,2,12,29,37,26,8,1),
\quad(C_{B,k})=(0,0,1,9,27,38,25,8,1).
\]
The conditional probability is \(C_{G,k}/\binom{8}{k}\). Thus \(C_{A,5}-C_{B,5}=-1\), giving the claimed \(-1/56\).

Independence gives \(R_G(p)=\sum_{k=0}^{m}C_{G,k}p^k(1-p)^{m-k}\). Substitution and polynomial factorization give the displayed exact reliability difference. Its remaining quartic is strictly positive: indeed,
\[
2p^4-p^2-p+1
=\sum_{j=0}^{5}b_jp^j(1-p)^{5-j},
\qquad (b_0,\ldots,b_5)=(1,4,5,1,0,1).
\]
Every summand is nonnegative on \([0,1]\) and the \(j=0\) summand is positive for \(0<p<1\). The second-order boundary roots do not create interior ties. Direct path and cut inspection gives \(d=c=2\) for both networks.

**Sharp lower cutoff.** For polynomials \(F,G\) of edge-disjoint component networks, series and parallel composition yield \(F\cdot G\) and \(F+G-FG\). Starting from the single-edge polynomial \(p\), recursively combine every pair of polynomials with edge counts summing to \(m\) and deduplicate identical integer-coefficient polynomials. This generates all possible terminal-reliability polynomials for two-terminal series-parallel networks with \(m\) edges by structural induction. Its exact distinct polynomial counts for \(m=1,\ldots,8\) are \(1,2,4,10,24,64,174,496\).

For a nondegenerate terminal-reliability polynomial, the smallest positive exponent is exactly \(d\), the shortest terminal path length, and the multiplicity of \(1-p\) in \(1-R(p)\) equals \(c\), the smallest terminal edge cut. Hence deduplicating equal polynomials does not discard any \((d,c)\)-class. For each fixed \(m,d,c\), compare all unordered distinct polynomial pairs. Convert their difference from powers of \(p\) to the exact cardinality-count coefficients \(\Delta C_k\), using
\[
C_k=\sum_{j=0}^k a_j\binom{m-j}{k-j}
\qquad\text{when }R(p)=\sum_{j=0}^m a_jp^j.
\]
A conditional rank reversal requires both signs among the \(\Delta C_k\). For each such pair, compute the square-free decomposition of its difference polynomial over the rationals and check exactly for a factor of odd multiplicity with a root strictly between zero and one. Such an interior odd-multiplicity root proves the independent-protocol difference changes sign, ruling out an all-\(p\) ordering.

The exhaustive exact check has zero mixed-cardinality pairs at \(m\le6\); it has precisely \(50\) at \(m=7\), and **all 50** have an odd-multiplicity root in \((0,1)\). Thus the required reversal is impossible through seven corridors. At \(m=8\), the witness above establishes existence. This is a finite, exhaustive calculation for the specified recursively defined class, not an extrapolation from a sample.

## Verification

Run `python check.py` with Python 3 and SymPy installed (`requirements.txt` gives the dependency). It generates all series-parallel reliability polynomials through eight edges, uses exact integer coefficients and rational root counting for the lower cutoff, independently expands the two witness multigraphs into explicit indexed edges, and exhaustively checks all \(2^8\) operating-corridor subsets in each. It verifies the coefficients, analytic factorization, strictly positive quartic certificate, fixed-five sign and value at \(p=1/2\). No Monte Carlo or floating-point root estimates enter the proof.

## Relationship to prior work

Kramer-Schadt et al. (2004) study the ecological meaning of source-to-destination patch connectivity for dispersal, with spatially explicit mortality and behavioral dynamics; their ecological model does not imply a comparison between the two present idealized failure protocols. Classical two-terminal network reliability algebra supplies the known series and parallel formulas, not claimed here as new. Bertrand et al. (2018) study uniform reliability of *simple* two-terminal graphs with fixed vertex and edge counts, whereas the present construction permits parallel corridors and does not hold vertex count fixed. The present contribution is the sharp **equal distance-and-cut, series-parallel, fixed-size versus independent-failure distinction**. Prior work on signed reliability domination and coefficient comparisons is particularly relevant and may contain an equivalent result; priority is not independently certified.

## Limitations

The theorem concerns edge-operability connectivity, not proof that a real animal can successfully traverse a path or that an ecological population persists. The two exemplars have different numbers of habitat vertices and one has parallel links. The minimality is only within the specified series-parallel class and only for pairs with \(d,c\ge2\). Similar reliability-order reversals in general graphs or with different constraints are not classified. Relevant full-text access to some network-reliability literature was unavailable; the claim of originality remains provisional, and no independent scientific audit has occurred.

## References

1. Kramer-Schadt, S., Revilla, E., Wiegand, T., and Breitenmoser, U. (2004), *Fragmented landscapes, road mortality and patch connectivity: modelling influences on the dispersal of Eurasian lynx*, Journal of Applied Ecology 41, 711–723. First online 19 July 2004. https://doi.org/10.1111/j.0021-8901.2004.00933.x
2. Bertrand, H., Goff, O., Graves, C., and Sun, M. (2018), *On uniformly most reliable two-terminal graphs*, Networks 72, 200–216. https://doi.org/10.1002/net.21811
3. Boesch, F. T., Satyanarayana, A., and Suffel, C. L. (2009), *A survey of some network reliability analysis and synthesis results*, Networks 54, 99–107. https://doi.org/10.1002/net.20300
4. Brown, J. and DeGagné, C. D. C. (2021), *Roots of two-terminal reliability polynomials*, Networks 78, 153–163. https://doi.org/10.1002/net.22004
