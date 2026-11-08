# A sharp variance reversal despite stochastic outbreak dominance on cubic contact networks

## Finding
Let \(\Pi=C_3\square K_2\) be the triangular prism and let \(B=K_{3,3}\). The independent-bond epidemic on each graph starts at a uniformly sampled vertex; every edge independently transmits with probability \(p\), and \(X_G(p)\) is the number of vertices ultimately reached, including the source.

These are, up to isomorphism, the only two connected simple cubic graphs on six vertices. For every \(0<p<1\), \(X_B(p)\) strictly dominates \(X_\Pi(p)\) in first-order stochastic order, with equal tails at thresholds one, two, and three and strictly larger \(B\)-tails at thresholds four, five, and six. Nevertheless the variance ranking switches exactly once. There is a unique \(p_*\in(0,1)\), with \(p_*=0.479245294778868\ldots\), such that
\[
\operatorname{Var}X_B(p)>\operatorname{Var}X_\Pi(p)\quad(0<p<p_*),\qquad
\operatorname{Var}X_B(p)<\operatorname{Var}X_\Pi(p)\quad(p_*<p<1).
\]
The two variances agree at \(p=p_*\) and, trivially, at the boundary probabilities \(p=0,1\). Six vertices is the first connected cubic network order at which there are two distinct graph shapes to compare. This is a finite-six-vertex result, not a claim of a universal ordering of all cubic networks.

## Assumptions and scope
Graphs are finite, simple, undirected, connected and \(3\)-regular. There are six vertices, with the prism edges
\[
\{01,12,02,34,45,35,03,14,25\},
\]
and the bipartite edges \(\{uv:0\le u\le2,\ 3\le v\le5\}\). Each edge is independently open with common probability \(p\in[0,1]\). An independent uniform initial source is chosen among the six vertices. The outbreak is its connected component in the open-edge subgraph. This is the independent-transmission (Reed–Frost/bond-percolation) final-size model; it does not assert equivalent independence for a continuous-time SIR model with a shared random infectious period.

Write \(S_{G,k}(p)=\Pr(X_G(p)\ge k)\). Define \(\Delta S_k=S_{B,k}-S_{\Pi,k}\), and \(V_G=\operatorname{Var}X_G\).

## Proof
**1. Cubic graph minimum.** The number of vertices of a cubic simple graph is even. The only connected cubic graph on four vertices is \(K_4\); smaller ones do not exist. For six vertices, the complement is a simple \(2\)-regular graph, hence either a \(6\)-cycle or a disjoint union of two \(3\)-cycles. Their complements are respectively the triangular prism and \(K_{3,3}\). Thus these are the only six-vertex connected cubic graphs, proving the stated first-comparison boundary.

**2. Exact finite polynomial tails.** For a graph \(G\) with nine edges, let \(a_{G,k,e}\) be the total number of pairs \((F,v)\) in which \(F\subseteq E(G)\) contains exactly \(e\) edges, \(v\in V(G)\), and the connected component of \(v\) in \((V(G),F)\) has at least \(k\) vertices. There are only \(2^9=512\) edge subsets. By disjoint enumeration of every such state and all six roots,
\[
S_{G,k}(p)=\frac16\sum_{e=0}^{9}a_{G,k,e}p^e(1-p)^{9-e}.
\]
The complete signed difference counts, listed for successive \(e=0,1,\ldots,9\), are

| Threshold \(k\) | \((a_{B,k,e}-a_{\Pi,k,e})_{e=0}^{9}\) |
|---|---|
| 2 | \((0,0,0,0,0,0,0,0,0,0)\) |
| 3 | \((0,0,0,0,0,0,0,0,0,0)\) |
| 4 | \((0,0,0,24,54,36,6,0,0,0)\) |
| 5 | \((0,0,0,0,30,36,6,0,0,0)\) |
| 6 | \((0,0,0,0,0,36,6,0,0,0)\) |

These finite integer counts are independently reproduced by the standalone verifier using both exhaustive edge-subset enumeration and a different rooted induced-subgraph connectivity recursion. At \(k=1\) the tails necessarily agree. Substitution and polynomial factorization give
\[
\begin{aligned}
\Delta S_2&=\Delta S_3=0,\\
\Delta S_4&=p^3(1-p)^3(4-3p),\\
\Delta S_5&=p^4(1-p)^3(5-4p),\\
\Delta S_6&=p^5(1-p)^3(6-5p).
\end{aligned}
\]
Every factor in the last three lines is strictly positive for \(0<p<1\), proving strict first-order stochastic dominance at all nontrivial distinguishing thresholds.

**3. Exact mean and variance differences.** For every random variable supported on \(\{1,\ldots,6\}\), the tail-sum identities are
\[
\mathbb E X=\sum_{k=1}^6 S_k,\qquad
\mathbb E X^2=\sum_{k=1}^6(2k-1)S_k.
\]
Therefore
\[
\begin{aligned}
\mu_B-\mu_\Pi
 &=p^3(1-p)^3(4+2p+2p^2-5p^3),\\
\mathbb E[X_B^2]-\mathbb E[X_\Pi^2]
 &=p^3(1-p)^3(28+24p+30p^2-55p^3).
\end{aligned}
\]
The same finite enumeration yields the two exact means:
\[
\begin{aligned}
\mu_\Pi={}&1+3p+6p^2+8p^3+4p^4-32p^5-43p^6+131p^7-94p^8+22p^9,\\
\mu_B={}&1+3p+6p^2+12p^3-6p^4-24p^5-52p^6+150p^7-111p^8+27p^9.
\end{aligned}
\]
Since \(V_B-V_\Pi=(\mathbb E[X_B^2]-\mathbb E[X_\Pi^2])-(\mu_B-\mu_\Pi)(\mu_B+\mu_\Pi)\), exact expansion gives
\[
V_B(p)-V_\Pi(p)=p^3(1-p)^3Q(p),
\]
where
\[
\begin{aligned}
Q(p)={}&20-4p-34p^2-161p^3-26p^4+248p^5+596p^6\\
&-832p^7+168p^8-823p^9+1717p^{10}-1123p^{11}+245p^{12}.
\end{aligned}
\]

**4. Uniqueness of the variance crossing.** Set \(u=p/(1-p)\), a bijection from \((0,1)\) onto \((0,\infty)\). Clearing the positive denominator produces
\[
\begin{aligned}
(1+u)^{12}Q\!\left(\frac{u}{1+u}\right)
={}&20+236u+1242u^2+3679u^3+6235u^4+4684u^5\\
&-2428u^6-8366u^7-7038u^8-3191u^9\\
&-870u^{10}-135u^{11}-9u^{12}.
\end{aligned}
\]
In descending order the coefficients have exactly one sign change. Descartes' rule of signs gives at most one positive root, with multiplicity. But \(Q(0)=20>0\) and \(Q(1)=-9<0\), so the intermediate value theorem gives one root in \((0,1)\). The root is unique and simple; its sign separates the two variance regimes. Exact rational evaluation shows it lies in \((479/1000,480/1000)\), while numerical root isolation yields the displayed decimal.

## Verification
Run `python verify.py` with the requirements in `requirements.txt`. The checker (i) enumerates every one of 512 edge subsets of each graph and all six roots, (ii) independently evaluates the exact component probability using a vertex-subset connectedness recurrence, (iii) checks every threshold polynomial and its integer Bernstein-basis counts, (iv) reconstructs both moments and the variance difference from the distributions, and (v) checks the transformed polynomial and unique-root certificate. These exact finite checks validate the six-vertex claim only. The sign argument handles the infinite continuum of probabilities analytically; checking finitely many numerical probabilities would not suffice.

As concrete independent rational values, \(V_B-V_\Pi=6611555907/68719476736>0\) at \(p=1/4\), while \(V_B-V_\Pi=-5941/262144<0\) at \(p=1/2\).

## Relationship to prior work
Newman (2002) establishes the bond-percolation correspondence for independent edge transmission and general outbreak-size methods. Miller (2009) analyzes how clustering changes epidemic size and thresholds in large random-network ensembles; that model is not the pair of fixed six-vertex cubic graphs here and supplies no variance sign-change theorem for this pair. Allard and colleagues (2012) give an exact generic finite-graph percolation algorithm, which can calculate these distributions in principle, but its displayed results do not give the cubic-pair stochastic-dominance/variance-reversal classification or threshold. Ritchie and colleagues (2013/2014) analyze clustering and higher motifs using larger network ensembles, without the six-vertex exact comparison. The new mathematical content is the complete probability-tail comparison **together with** the unique variance crossing for the smallest nontrivial cubic-graph pair; merely evaluating an existing general algorithm is not claimed as novel.

## Limitations
Only a uniform source and independent, identically distributed edge transmission are considered. The result does not apply automatically to shared infectious-period SIR dynamics, site percolation, heterogeneous edges, or arbitrary cubic graphs. Earlier finite-network percolation tables or supplemental enumerations that may not have been indexed could have recorded parts of this example; historical priority is not independently certified. The comparison is mathematical, not a public-health forecast.

## References
1. M. E. J. Newman, *The spread of epidemic disease on networks*, 2002, original public preprint 30 April 2002, https://arxiv.org/abs/cond-mat/0205009.
2. J. C. Miller, *Percolation in clustered networks*, 2009, public preprint 21 April 2009, https://arxiv.org/abs/0904.3253.
3. A. Allard, L. Hébert-Dufresne, P.-A. Noël, V. Marceau and L. J. Dubé, *Exact solution of bond percolation on small arbitrary graphs*, 2012, https://arxiv.org/abs/1201.4369.
4. M. Ritchie, L. Berthouze, T. House and I. Z. Kiss, *Higher-order structure and epidemic dynamics in clustered networks*, 2013, https://arxiv.org/abs/1310.5047.
