# First integer-rounding failure for one-swap codes on Motzkin excursions

## Finding

For each integer \(1\le n\le7\), let \(\mathcal M_n\) be the set of length-\(n\) Motzkin excursions on the three labeled steps `U`, `D`, `H`. A received word may be the original word or the result of exchanging exactly one pair of adjacent *unequal* symbols; it need not itself be a Motzkin excursion. Let \(M_n\) be the largest zero-error code size (pairwise disjoint sets of possible received words). Let \(P_n\) be the optimum of the standard fractional output-incidence packing relaxation.

The complete exact classification through length seven is

| \(n\) | \(|\mathcal M_n|\) | \(M_n\) | \(P_n\) |
|---:|---:|---:|---:|
| 1 | 1 | 1 | \(1\) |
| 2 | 2 | 2 | \(2\) |
| 3 | 4 | 2 | \(2\) |
| 4 | 9 | 4 | \(4\) |
| 5 | 21 | 7 | \(7\) |
| 6 | 51 | 14 | \(71/5\) |
| 7 | 127 | 28 | \(5515/182\) |

Thus length six is the **first strict fractional gap**, while length seven is the **first failure of integer rounding**:

\[
M_6=14< P_6=\frac{71}{5},\quad
M_7=28<\lfloor P_7\rfloor=30.
\]

This is an exact finite classification, not a claim about larger lengths or asymptotic rates.

## Assumptions and scope

`U` increases height by one, `D` decreases it by one, and `H` leaves it unchanged. A Motzkin excursion has nonnegative height after every prefix and final height zero. The source alphabet consists of these three distinct symbols. For a source word \(w=w_1\cdots w_n\), define

\[
B(w)=\{w\}\cup\{w_1\cdots w_{i-1}w_{i+1}w_iw_{i+2}\cdots w_n:
1\le i<n,\ w_i\ne w_{i+1}\}.
\]

Crucially, the receiver is not required to satisfy the nonnegative-height condition. A code \(C\subseteq\mathcal M_n\) corrects the channel exactly when \(B(u)\cap B(v)=\varnothing\) for all distinct \(u,v\in C\). The fractional packing is the rational linear program

\[
P_n=\max\sum_{w\in\mathcal M_n}x_w,\qquad
x_w\ge0,\quad\sum_{w\,:\,y\in B(w)}x_w\le1\ \text{for each received word }y.
\]

The constraints range over the actual union of output balls, with no additional receiver restrictions.

## Proof

**1. Composition decomposition.** Every adjacent exchange preserves the number of `U`, `D`, and `H` symbols. Because each source has equally many up and down steps, let \(k\) denote their common number. Then \(0\le k\le\lfloor n/2\rfloor\) and different \(k\)-layers have disjoint received alphabets. Therefore both the integer maximum and fractional optimum add over \(k\). The number of sources in a layer is \(\binom{n}{2k}C_k\), with \(C_k=\frac{1}{k+1}\binom{2k}{k}\), since one chooses the nonhorizontal positions and fills them with a Dyck excursion.

**2. Finite certificate reduction.** For each \(n\) from one to seven and each valid \(k\), enumerate every source by the full nonnegative-prefix test; generate the exact set \(B(w)\) by the defining swaps, not by a graph-distance heuristic. Form a simple *compatibility graph* on the sources: two distinct words are adjacent exactly if their output sets are disjoint. A zero-error code in that layer is precisely a clique. The `verify.py` program reconstructs these graphs and proves their maximum clique sizes by complete branch-and-bound traversal. Every branch fixes a word and restricts remaining candidates to its compatible neighbors. The only pruning uses a proper greedy vertex coloring of remaining candidates: a clique can use at most one vertex of each color, so a branch with present size plus available color count at most the incumbent cannot improve it. The checker contains and invokes the entire search, not just a stored search log.

**3. Matching lower and upper certificates.** The `certificates.json` file lists an explicit optimal integer codebook for *every* layer. For every layer it also lists nonnegative rational primal source weights and nonnegative rational dual received-word weights. The checker recalculates *every* primal output inequality and *every* dual source inequality using exact fractions, and verifies equality between the two objective values. By weak duality they give the exact fractional optimum independently of floating-point optimization. Explicit integer codebooks achieve the enumerated clique bounds. This supplies matching lower and upper certificates at each of the 19 layers.

At length seven, the layer contributions are

| \(k\) | Sources | Integer maximum | Fractional optimum |
|---:|---:|---:|---:|
| 0 | 1 | 1 | \(1\) |
| 1 | 21 | 6 | \(6\) |
| 2 | 70 | 14 | \(2785/182\) |
| 3 | 35 | 7 | \(8\) |

Their integer maxima sum to \(28\), and their fractional maxima sum to \(5515/182\). The length-six layer values give integer maximum \(1+4+7+2=14\) and fractional maximum \(1+21/5+7+2=71/5\). At each of lengths one through five both maxima equal each other; hence all first-occurrence assertions follow.

## Verification

Put `verify.py` and `certificates.json` in the same directory, then run `python3 verify.py` (Python standard library, version 3.9 or newer). Its complete deterministic replay reports:

```text
VERIFY_OK groups=19 nodes=1870
Integer capacities: 1,2,2,4,7,14,28
Fractional optima: 1,2,2,4,7,71/5,5515/182
```

`certificates.json` contains all 19 component codebooks and exact nonnegative rational primal/dual certificates; no optimization package is needed for checking. As a separate computational cross-check, integer programming and continuous linear programming were also solved from independently constructed output-incidence matrices through length seven, agreeing with the returned integers and fractions. The proof of optimality is the self-contained exact checker and its documented exhaustive recurrence, not the optimizer's success flag.

## Relationship to prior work

Barcucci, Bilotta, Pergola, Pinzani and Succi use Motzkin paths to construct cross-bifix-free synchronization sets, a different condition based on prefix–suffix overlaps rather than radius-one adjacent exchanges. Buzaglo, Yaakobi, Etzion and Bruck study adjacent-transposition-correcting codes on permutations and multipermutations in the Kendall metric, with systematic constructions for rank modulation; they do not impose the Motzkin prefix constraint or determine this exact capacity sequence. Kulkarni and Kiyavash develop fractional hypergraph packing bounds for constrained *deletion* sources, providing a methodological antecedent, not a result for the adjacent-exchange channel. Kovačević, Kiah and Goyal address general-alphabet adjacent-transposition coding and asymptotic bounds, without specializing their finite optima to Motzkin excursions. None of these inspected results supplies an implication determining the seven-step capacity \(28\) or fractional optimum \(5515/182\).

## Limitations

The exact computation and proof cover only lengths one through seven, with three uncolored Motzkin steps and the at-most-one *adjacent-exchange* channel. They do not establish maximum code sizes for larger lengths, simultaneous multiple swaps, other constrained path families, or asymptotic rates. Exhaustive finite verification is not a proof for untested lengths. Historical priority is qualified by possible equivalent unindexed earlier computations; no independent external audit has been performed.

## References

1. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, first public preprint November 13, 2012, https://arxiv.org/abs/1211.3128.
2. S. Buzaglo, E. Yaakobi, T. Etzion and J. Bruck, *Systematic Codes for Rank Modulation*, first public preprint November 27, 2013, https://arxiv.org/abs/1311.7113.
3. E. Barcucci, S. Bilotta, E. Pergola, R. Pinzani and J. Succi, *Cross-bifix-free sets via Motzkin paths generation*, first public preprint October 17, 2014, https://arxiv.org/abs/1410.4710.
4. M. Kovačević, H. M. Kiah and K. Goyal, *Bounds on Codes Correcting Adjacent Transpositions*, first public preprint September 8, 2025, https://arxiv.org/abs/2509.06692.
