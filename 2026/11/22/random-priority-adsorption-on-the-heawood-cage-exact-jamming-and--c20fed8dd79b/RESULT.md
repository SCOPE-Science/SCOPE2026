# Random-priority adsorption on the Heawood cage: exact jamming and kinetic laws

## Finding
Let \(H\) be the fourteen-vertex point–line incidence graph of the Fano projective plane. Inspect its vertices in a uniformly random order, accepting a vertex precisely when no already accepted vertex is adjacent to it. Let \(J\) be the number ultimately accepted. The exact terminal distribution is
\[
\Pr(J=4)=\frac4{21},\qquad \Pr(J=5)=\frac7{15},\qquad \Pr(J=7)=\frac{12}{35}.
\]
The possible terminal configurations, including each *individual* configuration's probability, are exactly:

| Chosen Fano points | Chosen Fano lines | Number of configurations | Probability of each configuration |
|---:|---:|---:|---:|
| 7 | 0 | 1 | \(6/35\) |
| 0 | 7 | 1 | \(6/35\) |
| 4 | 1 | 7 | \(1/30\) |
| 1 | 4 | 7 | \(1/30\) |
| 2 | 2 | 21 | \(4/441\) |

In particular, no jammed configuration has six particles. The probability of reaching a maximum independent set is \(12/35\), versus \(2/37\) for a uniform draw among the thirty-seven maximal independent sets. The exact amplification is \(222/35\), and the total-variation distance between these two probability measures on maximal independent sets is \(293/777\). The expected occupancy and per-vertex fraction are
\[
\mathbb E J=\frac{577}{105},\qquad \frac{\mathbb E J}{14}=\frac{577}{1470}=\frac38+\frac{103}{5880}.
\]
Thus the exact kinetic occupancy of this distinguished cubic girth-six cage exceeds the familiar infinite cubic-tree random-priority adsorption density \(3/8\). This is a finite-graph comparison, not a new girth-asymptotic statement.

For the finite-time process with independent rate-one first-arrival times at all fourteen vertices, let \(J(t)\) be the number accepted by time \(t\), and set \(p=1-e^{-t}\). Its expected kinetics are given **exactly at every** \(t\ge0\) by
\[
\mathbb E J(t)=\sum_{k=0}^{14}\binom{14}{k}p^k(1-p)^{14-k}\mu_k,
\]
where \(\mu_k\) is the conditional expected accepted count when exactly \(k\) of the fourteen sites have arrived:

| \(k\) | \(\mu_k\) | \(k\) | \(\mu_k\) | \(k\) | \(\mu_k\) |
|---:|---:|---:|---:|---:|---:|
| 0 | \(0\) | 5 | \(43/13\) | 10 | \(70573/15015\) |
| 1 | \(1\) | 6 | \(2143/585\) | 11 | \(6698/1365\) |
| 2 | \(23/13\) | 7 | \(131/33\) | 12 | \(2323/455\) |
| 3 | \(31/13\) | 8 | \(381863/90090\) | 13 | \(1447/273\) |
| 4 | \(413/143\) | 9 | \(67261/15015\) | 14 | \(577/105\) |

## Assumptions and scope
The Fano plane has points \(\{0,\ldots,6\}\) and seven lines \(\ell_j=\{j,j+1,j+3\}\), with arithmetic modulo seven. The graph \(H\) has one vertex for each point and each line and edges only between incident point–line pairs. A maximal independent set is an independent set to which no further vertex can be added; it need not have maximum cardinality. At terminal saturation the algorithm has processed a complete uniform permutation of all vertices. For kinetic statements, each vertex makes a first attempted arrival at an independent exponential time of rate one. An attempted vertex adjacent to an already accepted one is forever rejected. All probabilities refer to this fixed graph and this process, not to random graph sampling or equilibrium hard-core sampling.

## Proof
**Classification.** For a chosen point set \(A\), maximality requires including *every* line disjoint from \(A\), since such lines are mutually nonadjacent. The Fano axiom that any two lines meet in one point gives all possibilities. No chosen points gives the entire line side; one chosen point gives the four nonincident lines; two chosen points give their two simultaneously nonincident lines; three chosen points cannot yield a maximal set (the collinear case leaves all lines excluded and the noncollinear case leaves an unblocked point); four chosen points yield a maximal set only if they are the complement of one line; and five or six chosen points with no admissible line can be extended. Seven chosen points give the other complete side. The five types and multiplicities in the Finding table follow.

**Rational event integral.** Give every vertex an independent uniform arrival time on \([0,1]\). For a specified maximal independent set \(I\), it is exactly the terminal output if and only if each vertex \(u\notin I\) arrives after at least one neighbor belonging to \(I\). Necessity is immediate from rejection. For sufficiency, the earliest outside vertex that could be accepted would have an earlier neighbor in \(I\), which itself could only be rejected by a yet earlier accepted outside vertex, a contradiction. Therefore
\[
\Pr(\text{output}=I)=\int_{[0,1]^I}\prod_{u\notin I}\left(1-\min_{v\in N(u)\cap I}t_v\right)\prod_{v\in I}dt_v.
\]
Partition the integration domain by the order \(t_{v_1}<\cdots<t_{v_r}\) of the selected sites. Define \(f_j\) to count those excluded vertices whose earliest selected neighbor has rank \(j\). The relevant ordered integral is
\[
\mathcal I(f_1,\ldots,f_r)=\int_{0<t_1<\cdots<t_r<1}\prod_{j=1}^{r}(1-t_j)^{f_j}\,dt_1\cdots dt_r.
\]
It is computed exactly by the polynomial recursion \(Q_0(x)=1\),
\[
Q_j(x)=\int_0^x Q_{j-1}(y)(1-y)^{f_j}\,dy,\qquad
\mathcal I(f_1,\ldots,f_r)=Q_r(1).
\]
For any one maximal output of each size, the complete rank-frequency certificates (frequency vector, number of selected-site orders, integral) are as follows; the point–line dual types have the same certificates:

| Output size | Rank-frequency vector | Multiplicity | Exact simplex integral |
|---:|---|---:|---:|
| 4 | (3,2,3,2) | 8 | \(1/2940\) |
| 4 | (3,3,2,2) | 16 | \(1/2520\) |
| 5 | (3,2,1,0,3) | 24 | \(1/19600\) |
| 5 | (3,2,1,3,0) | 24 | \(1/4900\) |
| 5 | (3,2,3,1,0) | 24 | \(1/2940\) |
| 5 | (3,3,2,1,0) | 48 | \(1/2520\) |
| 7 | (3,2,1,0,1,0,0) | 1008 | \(1/39200\) |
| 7 | (3,2,1,1,0,0,0) | 3024 | \(1/29400\) |
| 7 | (3,2,2,0,0,0,0) | 1008 | \(1/23520\) |

Their sums are respectively \(4/441\), \(1/30\), and \(6/35\). Incidence-plane symmetry permutes outputs of the same point–line type, and the Fano point–line duality exchanges the indicated dual types. Multiplying by the configuration counts proves the size probabilities. The exact mean, amplification and total-variation values follow directly.

**Independent residual recursion and kinetic formula.** For every subset \(S\) of the fourteen vertices, let \(F_S(z)\) be the probability-generating polynomial of the number of accepted vertices when the process starts with \(S\) available. The first eligible arrival is uniform on \(S\); hence the *finite, well-founded* identity
\[
F_\varnothing(z)=1,\qquad
F_S(z)=\frac{z}{|S|}\sum_{v\in S}F_{S\setminus(\{v\}\cup N(v))}(z)
\]
computes the entire law. In particular, \(F_V(z)=\frac4{21}z^4+\frac7{15}z^5+\frac{12}{35}z^7\), independently reproducing the integrals. At finite time, the number \(K\) of vertices having arrived is \(\operatorname{Binomial}(14,p)\); conditional on \(K=k\), their identities form a uniform \(k\)-subset and their order is uniform. Therefore
\[
\mu_k=\binom{14}{k}^{-1}\sum_{|S|=k}F'_S(1),
\]
which proves the kinetic Bernstein formula and evaluates the fifteen exact coefficients in the table.

## Verification
Run the accompanying standard-library-only `heawood_rsa_check.py` with Python 3. It builds the Fano incidence graph from the modular difference set, exhaustively enumerates all \(2^{14}=16384\) site subsets, verifies the published independent-set polynomial, enumerates all thirty-seven maximal independent sets, and computes every output-set probability by exact polynomial integration over every selected-site order. It independently computes the full size law from the residual recursion, and evaluates all fifteen finite-time conditional means with exact `Fraction` arithmetic. Its assertions verify the two methods agree exactly and check all reported fractions. No Monte Carlo results or floating-point values are used in the certificate.

## Relationship to prior work
Pippenger (1989) introduced and analyzed random sequential adsorption on graphs, including the cubic-tree/high-girth density \(3/8\); this classical asymptotic is credited, not claimed here. Brightwell, Janson and Luczak (arXiv:1510.05560, first posted October 19, 2015) studied the greedy independent-set algorithm on random graphs with specified degrees and its asymptotic jamming fraction, not the terminal law on this fixed Fano incidence graph. Perarnau and Perkins (arXiv:1611.01474, first posted November 4, 2016) proved that the Heawood graph maximizes the normalized hard-core independent-set partition function among cubic graphs of girth at least five. Their independence polynomial, \(1+14z+70z^2+154z^3+147z^4+56z^5+14z^6+2z^7\), is not a random-priority output law. The present finite kinetic law concerns a different sampling measure on maximal independent sets. The general finite-state recursion is standard; the distinctive statement is its exact evaluated Fano-incidence law and kinetic comparison, not the recurrence's invention.

## Limitations
This is an exact finite-graph result, not an extremality theorem for random-priority adsorption across all cubic graphs. The full text of Pippenger's 1989 article was not accessible for comparison; the available abstract focuses on high-girth limits and special cycle classes, so the historical-priority assessment retains that specific risk. The finite calculation does not prove any infinite family claim. The source-date field identifies the earliest day-verified archival source used for the mathematical direction, not a new publication date for these calculations. Independent mathematical audit has not been performed.

## References
- N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics **2** (1989), 393–401, DOI: https://doi.org/10.1137/0402034.
- G. Brightwell, S. Janson and M. Luczak, *The Greedy Independent Set in a Random Graph with Given Degrees*, arXiv:1510.05560, first public version October 19, 2015, https://arxiv.org/abs/1510.05560.
- G. Perarnau and W. Perkins, *Counting Independent Sets in Cubic Graphs of Given Girth*, arXiv:1611.01474, first public version November 4, 2016, https://arxiv.org/abs/1611.01474.
