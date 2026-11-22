# The first fractional single-deletion packing gap for \(132\)-avoiding permutations

## Finding
Let \(\mathcal A_n=\operatorname{Av}_n(132)\), the permutations of \(\{0,\ldots,n-1\}\) avoiding three positions \(i<j<k\) with \(\pi_i<\pi_k<\pi_j\). Set \(\mathcal A_0=\{\varepsilon\}\), containing the empty permutation. For \(\pi\in\mathcal A_n\), its one-deletion shadow \(D(\pi)\) is the *set* of all length-\(n-1\) permutations obtained by deleting one position and standardizing the survivors. Let \(M_n\) be the maximum size of a subset \(C\subseteq\mathcal A_n\) with pairwise disjoint shadows, and let \(P_n\) be the optimum of the natural fractional shadow-packing linear program
\[
 P_n=\max\Big\{\sum_{\pi\in\mathcal A_n}x_\pi:\ x_\pi\ge0,\ \sum_{\pi:\,s\in D(\pi)}x_\pi\le1\quad(s\in\mathcal A_{n-1})\Big\}.
\]
Then the exact values for \(1\le n\le6\) are

| \(n\) | \(|\mathcal A_n|\) | \(M_n\) | \(P_n\) |
|---|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 2 | 1 | 1 |
| 3 | 5 | 2 | 2 |
| 4 | 14 | 3 | 3 |
| 5 | 42 | 6 | 6 |
| 6 | 132 | 13 | \(2217/154\) |

In particular, \(n=6\) is the first nonintegral fractional shadow-packing instance in this hereditary Catalan source class, and already exhibits an integer-rounding failure: \(M_6=13<\lfloor P_6\rfloor=14\). Equivalently, the exact maximum size of a one-deletion-correcting code in \(\mathcal A_6\) is \(13\), although the fractional relaxation permits \(2217/154\approx14.3961\) codewords.

## Assumptions and scope
Every deletion removes **exactly one** unknown position, and the decoder receives only the relative-order permutation of the remaining five symbols; repeated deletion outcomes count once. The decoder knows that the source belongs to \(\mathcal A_n\). Distinct codewords must have disjoint sets of possible observations; unique reconstruction from the *entire* observation deck is a different model. The bound is exact for the stated lengths and is not an assertion about all permutations or asymptotic capacity. One-based labels may replace the zero-based labels in the certificate without changing any count.

## Proof
**1. Exhaustion of the source and observation space.** In a \(132\)-avoiding permutation of length \(n\), the maximum letter splits the remaining letters into a left \(132\)-avoider using all values larger than those on its right and a right \(132\)-avoider. Conversely every such split is valid. Recursing on the left size \(a\in\{0,\ldots,n-1\}\) gives exactly the Catalan family. The attached checker also generates every permutation directly and tests all ordered triples, and asserts equality of these two lists for each \(1\le n\le6\). Since pattern avoidance is hereditary, every standardized deletion shadow belongs to \(\mathcal A_{n-1}\). Each shadow is explicitly constructed by all \(n\) deletions, with duplicates removed.

**2. Integral optima.** Form the graph whose vertices are the source permutations, with an edge precisely when their deletion shadows intersect. Correcting codes are independent sets; equivalently they are cliques in its complementary compatibility graph. The attached `verify.py` contains a complete exact clique branch-and-bound procedure, not a heuristic or a numerical solver. At each recursive node it greedily partitions candidate vertices into proper color classes; no clique among those candidates can have more members than the number of classes. It explores the inclusion branch for every candidate in reverse color order, deleting that candidate before considering the next branch; any branch omitted by the color bound cannot improve the incumbent. Hence the entire finite search establishes \(M_1,\ldots,M_6=(1,1,2,3,6,13)\). The length-six search visits 50,809 nodes. For a direct, independently inspectable lower certificate, the following thirteen words have pairwise disjoint shadows (symbols are \(0,\ldots,5\)):

```
012345 234501 312045 324150 340125 345210 431025
452301 510234 523104 531240 543012 543210
```

**3. Exact fractional optima.** `LP_CERTIFICATE.json` contains only small nonnegative integer weights. For each \(n\le5\), it lists an integral set of observation words meeting the shadow of every source; its size equals the integral optimum in the table. These output covers prove \(P_n\le M_n\), while every integral code is a feasible fractional packing, proving equality. For \(n=6\), let \(a_\pi\) be its `source_weights` and let \(b_s\) be its `output_cover_weights` (missing dictionary keys have weight zero). The checker proves *by exact integer arithmetic*
\[
 \sum_{\pi:\,s\in D(\pi)}a_\pi\le308\quad\text{for every }s\in\mathcal A_5,
\qquad
 \sum_{s\in D(\pi)}b_s\ge308\quad\text{for every }\pi\in\mathcal A_6,
\]
\[
 a_\pi,b_s\in\mathbb Z_{\ge0},\qquad
 \sum_\pi a_\pi=\sum_s b_s=4434.
\]
Dividing by \(308\) supplies a primal feasible fractional packing and dual feasible observation cover with the same objective \(4434/308=2217/154\). Weak duality proves exact optimality. These certificates also exhibit \(P_6>14>M_6\), the claimed first strict rounding failure.

## Verification
Use Python 3.9 or later, without additional dependencies, from a directory containing both `verify.py` and `LP_CERTIFICATE.json`:

```
python3 verify.py
```

The actual replay produced `n=6 sources=132 outputs=42 capacity=13 nodes=50809 LP=4434/308`, `CODEBOOK_OK 13`, and `VERIFY_OK`. The script verifies the smaller lengths, two independent generating procedures, disjointness of the displayed codebook, the exact clique search, and all rational primal and dual inequalities. As a separate algorithmic check, a binary mixed-integer maximum-independent-set formulation on the same 132 sources and 1,995 conflict edges returned optimum 13; this numerical solver check is supplementary, not the proof of the upper bound.

## Relationship to prior work
Smith (2006) and Raykova (2006) study when a permutation can be reconstructed from its *entire set or multiset* of minors, including certain restricted classes; this does not give the capacity of a code decoding from one unknown deletion. Gabrys et al. (2014) formulate the exact relative-rank single-deletion channel and give general constructions and asymptotic bounds on the full permutation space; neither the sharp \(132\)-avoiding length-six capacity nor its fractional-packing value follows from their results. Published work on the one-deletion shadow-size distribution of \(132\)-avoiders supplies individual shadow counts but does not supply a maximum family of disjoint shadows or its fractional relaxation. Relevant alternate formulations were checked as output-hypergraph packings, conflict-graph independent sets, and deletion/insertion duals; no inspected result gives this exact pair \((13,2217/154)\) for this source class.

## Limitations
The integer optimum is proved by an exhaustive, reproducible finite search rather than a short closed-form combinatorial inequality. It is not extended beyond \(n=6\), and no uniqueness or enumeration of all optimal codes is asserted. Search-based historical-priority assessment cannot exclude unindexed equivalences; mathematical proof and reproducibility do not imply an independent audit. The reported LP gap concerns the standard shadow-incidence relaxation only, not all stronger valid inequalities or an operational time-varying channel.

## References
1. R. Smith, *Permutation Reconstruction*, Electronic Journal of Combinatorics 13 (2006), N11, published June 30, 2006, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v13i1n11/pdf/, DOI 10.37236/1149.
2. M. Raykova, *Permutation Reconstruction from Minors*, Electronic Journal of Combinatorics 13 (2006), R66, published August 3, 2006, https://www.cs.columbia.edu/~mariana/papers/perm_reconstruct.pdf, DOI 10.37236/1092.
3. R. Gabrys, E. Yaakobi, F. Farnoud, F. Sala, J. Bruck, L. Dolecek, *Single-Deletion-Correcting Codes over Permutations*, IEEE ISIT (2014), pp. 2764–2768, https://yaakobi.net.technion.ac.il/files/2015/04/40_Single_Deletion_Permutations_ISIT14.pdf, DOI 10.1109/ISIT.2014.6875337.
4. R. Simion and F. W. Schmidt, *Restricted Permutations*, European Journal of Combinatorics 6 (1985), 383–406; Catalan pattern-avoidance background as cited in Raykova (2006).
