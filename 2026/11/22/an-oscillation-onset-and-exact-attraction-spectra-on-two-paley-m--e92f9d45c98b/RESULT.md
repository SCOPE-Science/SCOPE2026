# An oscillation onset and exact attraction spectra on two Paley majority networks

## Finding

For the undirected prime-order Paley graphs with \(p=13\) and \(p=17\), synchronous binary majority with tie retention has **no genuine two-cycles** at 13 vertices but **1,530 primitive two-cycle orbits** at 17 vertices. Both graphs have the same sharp six-update first-periodic-entry bound.

The complete attractor-basin census is below. A row \((\ell,b,m)\) means there are exactly \(m\) distinct temporal attractor orbits of least period \(\ell\), each attracting exactly \(b\) initial configurations (including its recurrent configurations).

| Order | Attractor type \((\ell,b,m)\) | Complete census |
|---|---|---|
| \(13\) | fixed | \((1,1,26), (1,5,78), (1,3888,2)\) |
| \(13\) | two-cycles | none |
| \(17\) | fixed | \((1,1,34), (1,29,68), (1,62323,2)\) |
| \(17\) | two-cycles | \((2,2,1122), (2,4,272), (2,8,136)\) |

Consequently the fixed-point counts are \(106\) and \(104\), the number of primitive two-cycle orbits is \(0\) and \(1530\), and the exact initial-configuration consensus probabilities are
\[
\Pr_{13}(\mathrm{consensus})=\frac{7776}{8192}=\frac{243}{256},\qquad
\Pr_{17}(\mathrm{consensus})=\frac{124646}{131072}=\frac{62323}{65536}.
\]

The first-periodic-entry distributions, with \(d\) denoting the first time at which the state lies on its eventual recurrent orbit, are:

| \(d\) | \(p=13\) | \(p=17\) |
|---:|---:|---:|
| 0 | 106 | 3164 |
| 1 | 1664 | 17782 |
| 2 | 3640 | 69054 |
| 3 | 2314 | 29376 |
| 4 | 78 | 9112 |
| 5 | 234 | 2040 |
| 6 | 156 | 544 |

Both maps \(F_p\) obey the sharp identity \(F_p^8=F_p^6\), while \(F_p^7\ne F_p^5\). The two consensus equilibria attract \(3888\) and \(62323\) configurations apiece for the respective orders. The total nonconsensus fixed-point attraction populations are \(416\) and \(2006\), while the larger graph has another \(4420\) initial configurations ultimately reaching two-cycles.

## Assumptions and scope

For \(p\in\{13,17\}\), set the *labelled* vertex set to \(\mathbb Z/p\mathbb Z\), represented by integers from \(0\) to \(p-1\). Join distinct vertices \(i,j\) precisely when the nonzero residue \(j-i\pmod p\) is a square. Because both primes are congruent to one modulo four, this adjacency is symmetric, and the degrees are \(6\) and \(8\) respectively. In particular, the graph on 17 vertices is the familiar self-complementary Ramsey construction with no complete or independent four-vertex set.

Write the state as a bit mask \(x\) with coordinates \(x_i\in\{0,1\}\) and let \(s_i(x)=\sum_{j\sim i}x_j\). If the degree is \(d_p=(p-1)/2\), the synchronous map is specified exactly by
\[
(F_p(x))_i=\begin{cases}
1,&2s_i(x)>d_p,\\
0,&2s_i(x)<d_p,\\
x_i,&2s_i(x)=d_p.
\end{cases}
\]

Thus ties retain the incumbent value. No self-loops, random tie resolution, asynchronous updates, weighted votes, or graph quotienting are included. Counts are for **labelled states**; only temporal rotations of a recurrent orbit are identified as the same attractor. First-entry time equals zero on periodic states.

## Proof

This is a **finite, complete, computer-assisted enumeration theorem**, not an inferred rule for all prime-order Paley graphs. The following finite algorithms exhaust every possible state, and their independent implementations are included.

**Adjacency construction.** The program `check_majority_python.py` forms the set \(R_p=\{a^2\bmod p:1\le a<p\}\) and for each vertex creates the mask of those \(j\) satisfying \(j-i\in R_p\). It verifies symmetry and the exact degree. Independently, `verify_paley_census.cpp` computes adjacency using Euler's criterion \((j-i)^{(p-1)/2}\equiv1\pmod p\), without using the first program's edge lists. The C++ transition counts signed neighbor opinions; the Python transition counts one-valued neighbors. These are algebraically equivalent to the displayed update rule, including ties.

**Exhaustive functional graph.** Both programs construct the successor of **each** of the \(2^{13}\) or \(2^{17}\) possible bit masks, so no state can lie outside the finite certificate. The Python algorithm computes all successor indegrees, repeatedly deletes indegree-zero states, discovers directed cycles among the survivors, and propagates orbit labels and distances backward along the deleted list. A directed functional graph has one directed cycle per component: the indegree-peeling process deletes precisely its noncycle vertices, and the reversed deleted order has its successor already labelled. This proves that the procedure calculates every first-entry time, least period, attractor and attraction basin exactly.

The C++ program instead performs successor-path tracing, detecting a repeat either within a newly followed path or in an already assigned component. In the first case the segment between visits is the directed recurrent orbit; in the second case the path connects to an identified attractor. It propagates depth and orbit label backward. It does not use indegree peeling or the Python neighbor-mask algorithm. Both implementations assert that all recurrent lengths encountered are one or two (also consistent with the general symmetric-threshold period theorem).

**Aggregation and boundary certificates.** Each program counts attractors by the pair (least period, total basin population) and records the complete first-entry histogram. The reproducibility program `compare_census.py` compares every published shared statistic, and checks the identities
\[
\sum_{d\ge0}H_p(d)=2^p,\qquad
\sum_{(\ell,b,m)}bm=2^p,\qquad
\sum_{(\ell,b,m):\ell=1}m=\#\mathrm{Fix}(F_p),
\]
with the corresponding sum for period-two orbits. The finite output files record the exact table rows above. The maximum depths are both six, with \(156\) and \(544\) states attaining six. For each state of depth at most six, \(F_p^6(x)\) is periodic of period one or two, giving \(F_p^8(x)=F_p^6(x)\). A state of depth six is not periodic at time five, so for such a state \(F_p^7(x)\ne F_p^5(x)\); hence the cutoff is sharp. The generated output identifies concrete witness masks (375 and 4971, respectively).

**Individual basin totals.** The full basin histograms show the two unanimous configurations are precisely the two fixed attractors with maximum basin size. Every other fixed basin and every two-cycle basin is explicitly accounted for. Summation gives the claimed consensus, nonconsensus-fixed and oscillation totals with no omitted configurations.

## Verification

Run `sh run_checks.sh` on a machine with Python 3, a C++17 compiler, and standard Unix `diff`. It executes **both complete independent state-space classifications**, compares their shared statistics and rechecks equality with the included output files. No packages, source-paper downloads or data imports are needed. Each program starts from the prime \(p\) and constructs its own adjacency, map and functional graph.

The certificate is finite and exhaustive for **exactly the two specified vertex orders**. The proof of the enumeration's completeness follows from the labelled-mask indexing and functional-graph decomposition; its correctness is therefore not based merely on a numerical pattern, sample, random test or failure-to-find. The included files are `check_majority_python.py`, `verify_paley_census.cpp`, `compare_census.py`, `run_checks.sh`, `census_python.jsonl` and `census_cpp.txt`.

## Relationship to prior work

Goles and Olivos proved eventual fixed or two-periodic dynamics for symmetric threshold systems. That theorem bounds *possible lengths*, not their number or basins on either Paley graph. Tamuz and Tessler analyze retention of information in majority dynamics; the inspected model assumes odd graph degrees to avoid ties and gives general dynamical statements, not this even-degree tie-retention census. Kaaser, Mallmann-Trenn and Natale give general and structural voting-time bounds, not the exact sharp clock or full attractor census for these two particular residue graphs. Their general results are not contradicted.

The known role of the seventeen-vertex Paley graph as a Ramsey construction motivates choosing this graph rather than an arbitrary small graph. A search of relevant published mathematical records found related undirected-graph majority censuses and Paley **tournament** majority dynamics, but the latter is directed and uses different neighbor sets, and none of the inspected statements supplies the exact numerical populations here. Similarity of model vocabulary does not certify novelty. The record of comparisons and material inspected is in `AUDIT.json`.

## Limitations

Only \(p=13\) and \(p=17\) are proved; no implication for any larger prime, monotone family-wide transition, or limiting consensus probability is claimed. Exact integer counts depend on synchronous **open-neighborhood majority with incumbent tie retention**. The two exhaustive programs share the same high-level mathematical definition but independently implement the adjacency tests and functional-graph computations; their agreement is a strong same-project finite certificate, not an independent external audit. Historical priority cannot be established by search alone: unindexed tables, alternative encodings, or inaccessible full texts could already imply some or all of the numbers.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1. https://doi.org/10.1016/0012-365X(80)90121-1
2. O. Tamuz and R. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:1307.4035, first preprint 2013-07-15. https://arxiv.org/abs/1307.4035
3. D. Kaaser, F. Mallmann-Trenn, and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519, first preprint 2015-08-14. https://arxiv.org/abs/1508.03519
4. A. King, *Proving that R(4,4)>17*, Plus magazine, mathematical exposition of the Paley-17 construction. https://plus.maths.org/proving-r4417
