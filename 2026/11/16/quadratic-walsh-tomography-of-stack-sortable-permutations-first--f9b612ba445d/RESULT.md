# Quadratic Walsh tomography of stack-sortable permutations: first failure at six positions

## Finding

Let \(\mathcal A_n=\operatorname{Av}_n(231)\) be all permutations \(\pi\) of \(\{1,\ldots,n\}\) with no \(i<j<k\) for which \(\pi(j)>\pi(i)>\pi(k)\). Embed \(\pi\) in the Boolean cube of its \(n^2\) labeled position-symbol indicators \(X_{ia}(\pi)=\mathbf1_{\{\pi(i)=a\}}\). Let \(E_{n,2}\) evaluate all Walsh characters of Boolean degree at most two on \(\mathcal A_n\), over \(\mathbb R\). Thus its rows index allowed permutations and its columns the constant, single-indicator signs and products of two such signs.

For \(n=1,2,3,4,5,6\), its exact real ranks are respectively
\[
1,\quad 2,\quad 5,\quad 14,\quad 42,\quad 112.
\]
In particular, \(E_{n,2}\) has full row rank for **every** \(n\le5\), but **never** for any \(n\ge6\). At the sharp first failure \(n=6\), there are \(132\) stack-sortable permutations and the kernel of the two-position-marginal map on signed measures is exactly \(20\)-dimensional. It is not just a feature-count obstruction: \(382\) distinct feasible constant/one-position/two-position observation functions are available.

At order six, define an elementary three-switch cube by pairing the six positions into three disjoint pairs, independently exchanging the values within each pair, and requiring all eight permutations in the cube to avoid \(231\). There are exactly \(12\) distinct such cubes; their alternating signed trades are independent. They span a \(12\)-dimensional proper subspace of the full \(20\)-dimensional quadratic-moment kernel. Thus eight kernel dimensions remain after accounting for every elementary three-switch cube.

In particular, the two distinct probability laws each uniform on four permutations whose three adjacent two-letter blocks are independently increasing or decreasing, conditioned respectively on an even or an odd number of decreasing blocks, agree on **every** one- and two-position marginal. Appending an increasing fixed tail gives the same obstruction for all \(n\ge6\).

## Assumptions and scope

All positions and values are labeled; \(\mathcal A_0\) is not needed. A signed measure is a real function on \(\mathcal A_n\); its mass is the sum of its weights. The two-position marginal map records the numbers
\[
\sum_{\pi\in\mathcal A_n:\,\pi(i)=a,\,\pi(j)=b}\mu(\pi)
\]
for every \(1\le i<j\le n\) and \(a\ne b\), together with one-position marginals and total mass. Impossible events may be included as zero columns without altering rank. The Walsh convention is \(\chi_S(\pi)=\prod_{(i,a)\in S}(-1)^{X_{ia}(\pi)}\) for \(|S|\le2\), with no probabilistic normalization.

Because \((-1)^{X}=1-2X\), the degree-at-most-two Walsh span equals the span of \(1\), \(X_{ia}\) and \(X_{ia}X_{jb}\); identical positions or symbols give either lower-degree or identically zero functions. Consequently the Walsh evaluation rank and the two-position-marginal rank coincide over \(\mathbb R\).

## Proof

**1. Exhaustive Catalan decomposition.** A nonempty \(231\)-avoider has a unique expression \(L\,n\,R\), where \(L\) permutes the first \(k\) values, \(R\) permutes the remaining \(n-k-1\) smaller values after adding \(k\), and both parts avoid \(231\). Otherwise a left value greater than a right value, together with \(n\), would form the forbidden pattern. Conversely the displayed decomposition cannot create such a pattern. Starting with the empty permutation, this enumerates each avoider exactly once; the resulting orders one through six have \(1,2,5,14,42,132\) elements.

**2. Exact lower rank bounds.** For each enumerated permutation build its row of zero-one incidence against the constant, all feasible \(X_{ia}\) and all feasible products \(X_{ia}X_{jb}\). Exact Gaussian elimination in \(\mathbb F_2\) gives row ranks \(1,2,5,14,42,112\) for orders one through six. A nonzero minor modulo two is nonzero over \(\mathbb Q\), so the real ranks are at least these values. As the first five bounds equal the respective numbers of rows, the first five real ranks are full.

**3. Matching upper bound at order six.** The companion `kernel6.json` specifies twenty distinct, nonzero signed integer combinations of the \(132\) six-position avoiding permutations. Each has zero sum and zero sum against **every** allowed one- and two-position incidence column, checked by direct integer summation. The twenty coefficient vectors have rank twenty even after reduction modulo two, and thus are independent over \(\mathbb Q\). Therefore the real marginal nullity is at least twenty, giving rank at most \(132-20=112\). Combining this with the modular lower bound gives the exact rank and nullity. The bounded, finite check is a proof because the candidate rows and all observed incidence columns are generated exhaustively from their definitions; it is not an extrapolation from samples.

**4. Sharp unbounded loss of injectivity.** On positions \(1,\ldots,6\), independently choose each adjacent two-letter block to be either increasing or decreasing:
\[
(1,2)\text{ or }(2,1),\quad(3,4)\text{ or }(4,3),\quad(5,6)\text{ or }(6,5).
\]
All eight block direct sums avoid \(231\): if a triple meets different blocks, the blocks' increasing value ranges prevent the last selected value from being smaller than the first. Assign sign \((-1)^{\varepsilon_1+\varepsilon_2+\varepsilon_3}\) to the permutation with block-swap bits \(\varepsilon\). Any product of at most two position-symbol indicators depends on at most two bits, so summation over the unused bit cancels it exactly. This nonzero trade gives two distinct four-atom probability measures with the same quadratic observations. For any \(n>6\), append the fixed increasing values \(7,8,\ldots,n\). Avoidance remains true and all old and new degree-two observations still cancel. Thus no \(n\ge6\) is injective.

**5. Elementary-cube completeness at six positions.** Every three-disjoint-position-switch construction is specified by one of \(15\) pair partitions of the six positions and a starting avoider. Enumerate the resulting eight-element orbit and retain it exactly when all its permutations avoid \(231\). Identifying repeats by their sets of eight permutations leaves exactly \(12\) cubes. Their twelve coefficient vectors are independent over \(\mathbb F_2\); each is an alternating cube trade by the same cancellation argument. Their span over \(\mathbb R\) therefore has dimension twelve, strictly below the exact nullity twenty. The checker evaluates every pairing and every starting avoider, so this orbit census is complete.

## Verification

The complete reproducible package contains `verify_recursion.py`, `verify_bruteforce.py`, and `kernel6.json`. Put these in one directory and run `python3 verify_recursion.py` and `python3 verify_bruteforce.py`. Both use only the Python standard library. The first program generates avoiders using the Catalan decomposition, computes ranks exactly over \(\mathbb F_2\), checks all twenty integer null vectors and their independence, and enumerates the twelve three-switch cubes. The second independently tests each permutation for a forbidden triple, computes ranks over \(\mathbb F_3\), checks every signed certificate against all event columns, and checks the explicit eight-state trade at orders six, seven and eight. Both programs passed when run against the packaged files.

The finite incidence table, the modular lower bound and the integer nullspace certificate together prove real rank exactly at order six. The infinite noninjectivity assertion follows from the symbolic block construction; testing a few larger orders is supplementary only. All equations refer to unnormalized Walsh characters, so normalizing columns by a nonzero factor does not affect the rank statements.

## Relationship to prior work

Huang, Guestrin, Jiang and Guibas (2009) explicitly motivate first- and second-order permutation marginals as low-band Fourier statistics; their general factorization work does not compute their rank on the \(231\)-avoiding subset. Hyatt and Remmel (arXiv:1208.1052v1, August 5, 2012) classify \(231\)-avoiders by descents and maximum drop, and Albert and Bouvel (2015) study Wilf equivalence of Catalan structures. Both give relevant Catalan background, not this fixed-position two-marginal kernel.

A publicly available comparison-shattering theorem for \(231\)-avoiders concerns binary queries of the form \(\pi(i)<\pi(j)\). Here a query fixes **values at one or two labeled positions** and the question is recovery of arbitrary **distributions**; neither statement implies the other. The generic observation that cubic interactions can be invisible to quadratic marginals does not determine the exact first-failure rank \(112\), its nullity \(20\), or the exceptional eight dimensions beyond three-switch trades.

## Limitations

The full rank and nullity are not determined here for sizes above six. Only quadratic Boolean-Walsh observations are considered: there is no claim about the least degree needed for complete recovery at higher sizes or about conditioning. At size six, the twelve cubes are a specified family of local trades, not a classification of every possible minimal signed trade. The historical novelty assessment is bounded by accessible published sources; unindexed tables or other reformulations may affect priority.

## References

- J. Huang, C. Guestrin, X. Jiang, L. Guibas, *Exploiting Probabilistic Independence for Permutations*, Proceedings of AISTATS 2009, PMLR 5 (2009), 248–255, https://proceedings.mlr.press/v5/huang09b.html (bibliographic public date April 15, 2009).
- M. Hyatt, J. Remmel, *The classification of 231-avoiding permutations by descents and maximum drop*, arXiv:1208.1052v1, August 5, 2012, https://arxiv.org/abs/1208.1052.
- M. Albert, M. Bouvel, *A General Theory of Wilf-Equivalence for Catalan Structures*, Electronic Journal of Combinatorics 22 (2015), paper P4.45, https://doi.org/10.37236/5629.
- *Comparison shattering of stack-sortable permutations and a linear online gap*, publicly indexed mathematical finding, identifier `88a936fca69a`; relevant theorem compares positional orderings, rather than fixed-value marginal laws.
