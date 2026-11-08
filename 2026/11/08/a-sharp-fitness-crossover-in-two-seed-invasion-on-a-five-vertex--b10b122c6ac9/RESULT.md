# A sharp fitness crossover in two-seed invasion on a five-vertex bipartite population

## Finding

For the biased voter (death–Birth) process on the undirected, unweighted complete bipartite graph \(K_{2,3}\), fixing **two** initially mutant individuals, the optimal location changes exactly once as the mutant relative fitness \(r>0\) varies. At low and intermediate fitness the unique optimal type is both mutants in the two-vertex degree-three part; above a sharp threshold the unique optimal type is one mutant in each part. Seeding two members of the three-vertex degree-two part is never optimal.

Write \(A\) for the part of size two and degree three, \(B\) for the part of size three and degree two. Let \(F_{i,j}(r)\) be fixation probability when exactly \(i\) vertices of \(A\) and \(j\) of \(B\) initially carry mutants. Put

\[
Q(r)=8r^{6}+53r^{5}+113r^{4}+102r^{3}+113r^{2}+53r+8.
\]

The three two-mutant probabilities are exactly

\[
\begin{aligned}
F_{2,0}(r)&=\frac{72r^{7}+535r^{6}+1340r^{5}+1341r^{4}+794r^{3}+330r^{2}+80r+8}{10(r+1)Q(r)},\\
F_{1,1}(r)&=\frac{r(3r+2)(4r+1)(8r^{4}+51r^{3}+92r^{2}+27r+2)}{12(r+1)Q(r)},\\
F_{0,2}(r)&=\frac{r^{2}(20r^{5}+143r^{4}+335r^{3}+278r^{2}+107r+17)}{3(r+1)Q(r)}.
\end{aligned}
\]

There is exactly one positive real zero \(r_*\) of

\[
H(r)=48r^{7}+290r^{6}+365r^{5}-856r^{4}-2239r^{3}-1600r^{2}-460r-48,
\]

numerically \(r_*=2.05144026631733\ldots\). The maximizing seed type is exactly \((2,0)\) for \(0<r<r_*\), exactly \((1,1)\) for \(r>r_*\), and both types tie at \(r=r_*\). In particular, the change occurs strictly in the advantageous-mutant regime \(r>1\). The three neutral probabilities, in the same order, are \(1/2\), \(5/12\), and \(1/3\).

## Assumptions and scope

There are exactly five labeled individuals, occupying the vertices of \(K_{2,3}\). Mutants have constant relative reproductive fitness \(r>0\); residents have fitness one. At every discrete step, a vertex is chosen uniformly at random and replaces its current type by the type of a neighbor chosen proportionally to that neighbor's fitness. The update may leave the state unchanged. Vertices and edges have no weights, mutation is absent, and the graph never changes. Fixation is the event that eventually all five individuals are mutant. The seed budget is exactly two, not at most two; the three cases enumerated here exhaust seed sets modulo permutations within each part.

## Proof

Let \(i\in\{0,1,2\}\) and \(j\in\{0,1,2,3\}\). Because vertices in the same part have identical neighborhoods, the pair \((i,j)\) is a Markov lumping of the full configuration process. Set

\[
D_B(j)=3-j+rj,\qquad D_A(i)=2-i+ri.
\]

All denominators are positive for \(r>0\). Omitting the common factor \(1/5\), the four transition rates out of \((i,j)\) are

\[
\begin{aligned}
(i,j)\to(i+1,j)&:\quad (2-i)\frac{rj}{D_B(j)},\\
(i,j)\to(i-1,j)&:\quad i\frac{3-j}{D_B(j)},\\
(i,j)\to(i,j+1)&:\quad (3-j)\frac{ri}{D_A(i)},\\
(i,j)\to(i,j-1)&:\quad j\frac{2-i}{D_A(i)}.
\end{aligned}
\]

Each nonexistent boundary transition has coefficient zero. The absorbing states satisfy \(F_{0,0}=0\) and \(F_{2,3}=1\). For every other state the unique absorption-probability solution satisfies the backward equation given by the sum of each rate times the difference between the destination probability and the current probability, equal to zero. Uniqueness holds because from every transient state there is a positive-probability path to an absorbing state, and the finite chain is absorbed almost surely.

An explicit simultaneous rational solution is \(F_{i,j}=N_{i,j}/\bigl(60(r+1)Q(r)\bigr)\), with the following polynomial numerators; each bracket lists all degree-seven through degree-zero coefficients (leading zero coefficients may be omitted):

| State \((i,j)\) | Coefficients of \(N_{i,j}\), highest degree first |
|---|---|
| \((0,0)\) | \(0\) |
| \((0,1)\) | \((320,2120,4190,2000,350,20,0,0)\) |
| \((0,2)\) | \((400,2860,6700,5560,2140,340,0,0)\) |
| \((0,3)\) | \((432,3180,7980,8136,4854,1920,450,48)\) |
| \((1,0)\) | \((360,2535,5670,3975,900,60,0,0)\) |
| \((1,1)\) | \((480,3500,8405,7190,2525,380,20,0)\) |
| \((1,2)\) | \((480,3640,9580,10375,5710,1555,160,0)\) |
| \((1,3)\) | \((480,3660,9900,12000,8925,4290,1125,120)\) |
| \((2,0)\) | \((432,3210,8040,8046,4764,1980,480,48)\) |
| \((2,1)\) | \((480,3660,9620,10760,7340,3260,800,80)\) |
| \((2,2)\) | \((480,3660,9940,12550,10900,5770,1540,160)\) |
| \((2,3)\) | \((480,3660,9960,12900,12900,9960,3660,480)\) |

To verify without numerical approximation, substitute these polynomials into the ten transient backward equations, multiply by \(60(r+1)Q(r)D_A(i)D_B(j)\), and verify that every coefficient is zero. The attached standard-library `verify.py` checks all ten identities as integer polynomial equalities, including the absorbing boundary values. Since \(Q(r)>0\) for positive \(r\), this proves the rational expressions are the genuine fixation probabilities for every \(r>0\).

Direct polynomial subtraction gives

\[
\begin{aligned}
F_{2,0}-F_{0,2}
&=\frac{16r^{7}+175r^{6}+670r^{5}+1243r^{4}+1312r^{3}+820r^{2}+240r+24}{30(r+1)Q(r)}>0,\\
F_{1,1}-F_{0,2}
&=\frac{r(16r^{6}+128r^{5}+341r^{4}+326r^{3}+77r^{2}+8r+4)}{12(r+1)Q(r)}>0,\\
F_{1,1}-F_{2,0}&=\frac{H(r)}{60(r+1)Q(r)}.
\end{aligned}
\]

The first two differences are strictly positive because every displayed coefficient is positive and \(r>0\). In descending order, \(H\) has exactly one sign change. By Descartes' rule of signs it has at most one positive real root, counted with multiplicity. Since \(H(1)=-4500<0\), \(H(3)>0\), and the leading coefficient is positive, the intermediate-value theorem provides exactly one such root, with sign negative before it and positive after it. The asserted complete optimization and uniqueness properties follow.

## Verification

Run `python3 verify.py` using a standard Python 3 interpreter. The script verifies ten full polynomial backward equations, all three polynomial pairwise differences, and the sign assertion \(H(1)=-4500\) and \(H(2)<0<H(3)\), then independently solves the complete \(30\)-transient-state Markov chain at eight rational fitness values and compares all thirty states against the lumped rational formulas: \(254\) exact checks in total. All checks passed. The general claim follows analytically from the polynomial identities and the sign argument, not from the finite sampling.

## Relationship to prior work

Durocher, Karras, Pavlogiannis and Tkadlec (2022), the initiating source, establish the same biased-voter update convention, consider optimal initial seed sets, and give general hardness, approximation and submodularity results; their displayed examples already show that optimal seed sets may vary with fitness. The new statement is the explicit all-fitness, three-type sharp threshold on the natural five-vertex unequal complete bipartite population, not a claim to be first to observe fitness-dependent seeding in general. Zhang and coauthors' complete-bipartite analysis uses birth–death replacement instead of the death–Birth rule here. De Souza and Neves derive exact birth–death and death–Birth fixation laws for stars; \(K_{2,3}\) is not a star. Later general mixed-update results give neutral formulas for bidegreed graphs and special star/cycle formulas, rather than this two-seed all-fitness classification. No mathematical-record comparison identified a statement that implies the three probabilities and unique threshold together. Equivalence in unindexed or inaccessible literature remains possible.

## Limitations

The conclusion is specific to the unweighted undirected graph \(K_{2,3}\), constant fitness, exactly two initial mutants, and death–Birth updating. It does not classify arbitrary complete bipartite graphs, other seed budgets, birth–death updating, different competition rules, or fixation times. The polynomial certificate establishes probabilities for all positive fitness values; finite full-state cross-checks alone would not prove that. Publication priority is not independently established and may be affected by unindexed exact-enumeration studies.

## References

- L. Durocher, P. Karras, A. Pavlogiannis and J. Tkadlec, *Invasion Dynamics in the Biased Voter Process*, first public arXiv version 20 January 2022, https://arxiv.org/abs/2201.08207; IJCAI 2022, https://doi.org/10.24963/ijcai.2022/38.
- C. Zhang et al., *Fixation Probabilities on Complete Star and Bipartite Digraphs*, 2012, https://doi.org/10.1155/2012/940465 (birth–death convention in the compared bipartite analysis).
- E. P. de Souza and A. G. M. Neves, *Exact fixation probabilities for Birth-Death and Death-Birth frequency-dependent Moran processes on the star graph*, 2020, https://arxiv.org/abs/2003.05462.
- P. Petsinis, A. Pavlogiannis and P. Karras, *Maximizing the Probability of Fixation in the Positional Voter Model*, 2022, https://arxiv.org/abs/2211.14676 (different optimization: positional bias).
- D. A. Brewster et al., *The Mixed Birth-death/death-Birth Moran Process*, first public 2025, https://arxiv.org/abs/2511.18252 (later neutral bidegreed and one-mutant results, used only for comparison).
