# Fixed-cardinality independent path concepts: sharp VC rank and near-saturation online growth

## Finding
Let \(n\geq 1\) and \(0\leq k\leq\lceil n/2\rceil\). Regard the independent vertex sets of cardinality exactly \(k\) in the labelled path \(P_n\) as a Boolean concept class \(\mathcal I_{n,k}\) on coordinate queries \([n]\). Put \(r=n-2k+1\).

**Theorem.** The exact VC dimension, including all boundary cases, is
\[
\operatorname{VCdim}(\mathcal I_{n,k})=\min\{k,r\}.
\]
When \(r\geq1\), choose nonnegative integers \(b_1,\ldots,b_r\), as equal as possible, with \(\sum_i b_i=k\) (thus \(b_i\in\{\lfloor k/r\rfloor,\lceil k/r\rceil\}\)). The Littlestone dimension satisfies the explicit two-sided bounds
\[
\sum_{i=1}^{r}\left\lfloor\log_2(b_i+1)\right\rfloor
\ \leq\ \operatorname{Ldim}(\mathcal I_{n,k})\ \leq\
\min\left\{k,\left\lfloor\log_2\binom{k+r}{r}\right\rfloor\right\}.
\]
For \(r=0\), both dimensions vanish. In particular, if \(r\geq k\), then both dimensions equal \(k\); and if \(r=1\) (equivalently \(n=2k\)), the exact Littlestone dimension is \(\lfloor\log_2(k+1)\rfloor\).

For each fixed integer \(r\geq1\), setting \(n=2k+r-1\) and letting \(k\) tend to infinity gives
\[
\operatorname{VCdim}(\mathcal I_{2k+r-1,k})=r\quad(k\geq r),
\qquad
\operatorname{Ldim}(\mathcal I_{2k+r-1,k})=r\log_2 k+O_r(1).
\]
Thus the adaptive-minus-static dimension gap is unbounded at every fixed positive near-saturation defect \(r\), with exact logarithmic leading coefficient \(r\).

## Assumptions and scope
The labelled path \(P_n\) has vertices \(1,\dots,n\) and edges between successive indices. A concept is an independent subset \(I\subseteq[n]\) with \(|I|=k\). Querying \(j\in[n]\) returns \(1\) if and only if \(j\in I\). A set of coordinates is VC-shattered when every binary assignment on those coordinates occurs among the concepts. The Littlestone dimension is the greatest depth of a *complete* adaptive binary query tree such that each root-to-leaf labeling is consistent with at least one concept. All logarithms have base two. The constants in \(O_r(1)\) may depend on the fixed positive integer \(r\), but not on \(k\). There is no claim about general graphs or cardinalities outside \(0\leq k\leq\lceil n/2\rceil\).

## Proof
**1. A deficit bound via padded alternation.** Take any concept and write its incidence word \(x_1\cdots x_n\). Set \(x_0=x_{n+1}=0\). No two consecutive positions can be one. Each of the \(k\) ones contributes two distinct change edges in the padded word, and all other consecutive edges have value \(00\). Therefore exactly \(2k\) of its \(n+1\) edges change bit and exactly \(r=n-2k+1\) do not. Define \(y_i=x_i\oplus(i\bmod2)\) for \(0\leq i\leq n+1\). The number of changes in \(y\) is exactly \(r\), and its fixed endpoint values are \(y_0=0\), \(y_{n+1}=r\bmod2\).

No \((r+1)\)-element coordinate support can be VC-shattered. Indeed, given ordered queried positions \(s_1<\cdots<s_{r+1}\), prescribe the transformed labels \(y_{s_j}=j\bmod2\). The sequence of prescribed values, including both endpoints, alternates across all \(r+2\) successive intervals (because the final endpoint equals \((r+2)\bmod2\)). Every completion therefore has at least \(r+2\) changes, contradicting the exactly \(r\) changes available. This yields \(\operatorname{VCdim}\leq r\). Also, no set of more than \(k\) coordinates can be shattered because its all-one labeling would require more than \(k\) selected vertices. Hence \(\operatorname{VCdim}\leq\min\{k,r\}\).

**2. A gadget attaining the VC bound.** Put \(t=\min\{k,r\}\). Query the positions \(q_i=3i-2\) for \(1\leq i\leq t\). For any assignment, select exactly one of \(q_i\) and \(q_i+1\), choosing \(q_i\) precisely for a positive query label. These chosen vertices in successive pairs have separation at least two. Add the fixed vertices \(3t+1,3t+3,\ldots,3t+2(k-t)-1\) when \(k>t\). These are nonadjacent to one another and to the gadget choices, giving an independent set with exactly \(k\) vertices. Its final vertex is no greater than \(2k+t-1\leq n\), by \(t\leq r\). The construction also works at \(t=0\), where there are no queries. Thus the \(t\) queried positions are shattered and equality holds in the VC formula.

**3. Counting the concepts.** Writing the selected vertices as \(1\leq a_1<\cdots<a_k\leq n\), independence is equivalent to \(a_{j+1}\geq a_j+2\). The shift \(a_j\mapsto a_j-(j-1)\) bijects such sets with ordinary \(k\)-subsets of \([n-k+1]\). Consequently
\[
|\mathcal I_{n,k}|=\binom{n-k+1}{k}=\binom{k+r}{r}.
\]
Any depth-\(d\) Littlestone tree has \(2^d\) leaves, each needing a distinct consistent concept, so \(d\leq\lfloor\log_2\binom{k+r}{r}\rfloor\). Moreover the all-positive branch of a complete shattered tree queries \(d\) *distinct* positions: repeating one would leave an impossible opposite-label child. Its witnessing concept therefore has at least \(d\) ones, proving \(d\leq k\).

**4. A product of movable-defect thresholds.** Assume \(r\geq1\). Choose the balanced integers \(b_i\) from the theorem. Divide the \(n=2k+r-1\) positions into \(r\) consecutive blocks of lengths \(2b_i\), separated by one forced-zero vertex. In block \(i\), choose any independent set of size exactly \(b_i\). This defines a subclass of \(\mathcal I_{n,k}\), since the separators prevent adjacent selected vertices across blocks.

For a block of length \(2b\), each \(p\in\{0,\ldots,b\}\) defines an independent set of size \(b\): select odd local positions \(1,3,\ldots,2p-1\) and even local positions \(2p+2,2p+4,\ldots,2b\). These are all \(b+1\) possibilities, by the count in Step 3. Querying local position \(2j-1\) gives the threshold predicate \(j\leq p\). Balanced binary-search trees over \(p\) achieve complete depth \(\lfloor\log_2(b+1)\rfloor\) (depth zero for \(b=0\)). Concatenating the complete trees of the independent blocks, with the later block's tree appended at *every* leaf of the previous tree, produces a complete tree of depth \(\sum_i\lfloor\log_2(b_i+1)\rfloor\). This gives the stated lower bound.

When \(r\geq k\), the balanced blocks have \(k\) ones and the rest zeros, yielding lower bound \(k\), equal to the upper bound. When \(r=1\), there is one block of size \(2k\), so the lower bound is \(\lfloor\log_2(k+1)\rfloor\), which equals the cardinality upper bound. When \(r=0\), necessarily \(n=2k-1\), and exactly one independent size-\(k\) set exists; both dimensions are zero.

**5. The fixed-defect asymptotic.** For fixed \(r\geq1\), each balanced \(b_i=k/r+O_r(1)\). The preceding lower bound is \(r\log_2 k-O_r(1)\); the cardinality upper bound is \(r\log_2 k+O_r(1)\), since \(\binom{k+r}{r}=k^r/r!+O_r(k^{r-1})\). Their combination proves the asserted precise logarithmic leading term. The exact VC formula becomes \(r\) once \(k\geq r\). This completes the proof.

## Verification
The standalone `verify.py` enumerates every independent set at all admissible sizes for path lengths from one through fourteen and checks the exact VC rank by evaluating every possible support. It checks all gadget assignments through length twenty-one and independently computes finite Littlestone dimensions through length thirteen by exhaustive recursive splitting of the concept family; these dimensions are checked against both derived bounds and the exact one-defect formula. Run `python verify.py`. The successful outputs are `VC_ALL_PARAMETERS_PASS`, `GADGET_ALL_ASSIGNMENTS_PASS`, `LDIM_ALL_SMALL_PASS`, and `FIXED_SIZE_PATH_VC_ONLINE_PASS`. These are finite corroborations; all-length and asymptotic statements rest on the proof above.

## Relationship to prior work
Dyer and Müller (first public preprint 2018) study counting independent sets of prescribed cardinalities in cocomparability graphs, a broad counting problem that motivates working with exact-cardinality layers. Their theorems concern counting complexity, not VC or Littlestone dimensions of those layers. Adler, Benediktsson and Macpherson (first preprint 2020) establish VC bounds for the *neighborhood relation* in Johnson and Hamming graphs; despite a shared role for cardinality-constrained subsets, their queries are adjacency to another graph vertex rather than membership of an underlying path coordinate. Ghazi, Golowich, Kumar and Manurangsi (2021) give general closure bounds for online dimensions, not the sharp two-parameter fixed-path calculation. Munaro (first preprint 2013) notes that allowing *all* independent subsets of a graph gives VC dimension equal to its independence number; restricting to exactly \(k\) changes the answer, especially near maximum packing. The theorem above is not presented as an improvement to those general results.

## Limitations
The theorem gives an exact VC rank and two-sided online bounds; it does not determine the exact Littlestone dimension for every \((n,k)\), nor the full polynomial enumerating *all* shattered coordinate supports. It applies only to the linearly ordered path and precisely fixed independent-set cardinality, and its logarithmic asymptotic fixes \(r\) before taking \(k\) large. The searched and inspected sources do not establish a claim of global historical priority, especially under alternative language-of-words or fixed-weight hard-core terminology.

## References
- Martin Dyer and Haiko Müller, *Counting Independent Sets in Cocomparability Graphs*, arXiv:1808.09853 (first preprint 2018-08-29); *Information Processing Letters* 144 (2019), 31–36. DOI: 10.1016/j.ipl.2018.12.005.
- Isolde Adler, Bjarki Geir Benediktsson and Dugald Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042 (first preprint 2020-07-31); *Discrete Applied Mathematics* 312 (2022), 29–44.
- Badih Ghazi, Noah Golowich, Ravi Kumar and Pasin Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, PMLR 132 (2021), 686–696; https://proceedings.mlr.press/v132/ghazi21a.html.
- Andrea Munaro, *The VC-Dimension of Graphs with Respect to k-Connected Subgraphs*, arXiv:1302.6500 (first preprint 2013-02-26); *Discrete Applied Mathematics* 211 (2016), 148–164.
