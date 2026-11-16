# Three exact Fourier-cancellation motifs for five-vertex chordal graphs, and six-vertex recovery

## Finding

Write \(\mathcal C_n\) for the labelled simple chordal graphs on \([n]\), where chordal means having no induced cycle of length at least four. Each graph is identified with its incidence vector in \(\mathbb F_2^{\binom n2}\). For a set \(S\) of potential edges, define its unnormalized Walsh coefficient by
\[
W_n(S)=\sum_{G\in\mathcal C_n}(-1)^{|E(G)\cap S|}.
\]

**Theorem (exact orders five and six).** The transform \(W_5\) has precisely \(120\) zeros among its \(1024\) frequencies. These consist of the three vertex-relabeling orbits of frequency graphs:

| Frequency graph on five vertices | Orbit size | Example edge set |
|---|---:|---|
| A three-vertex path disjoint from a two-vertex edge, \(P_3\sqcup K_2\) | 30 | \(\{14,15,23\}\) |
| A triangle with two pendant edges incident to the same triangle vertex | 30 | \(\{12,13,14,15,23\}\) |
| A triangle with a pendant path of length two | 60 | \(\{12,15,23,24,34\}\) |

There are no other zeros of \(W_5\), and its smallest positive absolute coefficient is \(2\). In contrast, all \(32768\) coefficients \(W_6(S)\) are nonzero and satisfy the uniform congruence
\[
W_6(S)\equiv 2\pmod 4\qquad(S\subseteq E(K_6)).
\]
The congruence is sharp: one frequency with edge set \(\{12,13,14,15,16,23,24,34\}\) has \(W_6(S)=2\). Consequently the sharp smallest multiplier magnitude at order six is also \(2\).

For counting convolution \((T_nf)(x)=\sum_{G\in\mathcal C_n}f(x+1_{E(G)})\) on the binary edge cube, these statements give rank \(904\) at order five and full rank \(32768\) at order six. The Hilbert-space pseudoinverse norm at order five and inverse norm at order six are both exactly \(1/2\). In the completely invertible six-vertex case, the positive-spectrum condition number is \(9077\). The four-vertex case is already invertible, since \(|\mathcal C_4|=61\) is odd; hence the five-to-six transition is a genuine nonmonotone singularity of this natural graph-property kernel.

## Assumptions and scope

There are no asymptotic hypotheses. Graphs are finite, loopless, undirected, and labelled. The coefficient normalization above is a sum, not an average; all operator norm statements use unnormalized counting convolution and counting-measure \(\ell^2\). Graphs in frequency sets have the same vertex set but need not be chordal. An edge written \(ij\) means \(\{i,j\}\). Coordinate bits follow lexicographic order \(12,13,\ldots,1n,23,\ldots,(n-1)n\).

## Proof

**Five-vertex zero classification.** A graph is chordal if and only if it has no induced chordless cycle of length at least four. At five vertices, test all \(2^{10}=1024\) incidence masks. There are exactly \(822\) chordal masks. For each of the \(34\) vertex-relabeling orbits of frequency masks, evaluate \(W_5\) at the least integer representative, by summing the \(822\) corresponding signs. Permuting vertices preserves \(\mathcal C_5\), so the coefficient is constant throughout each orbit. The exhaustive integer table `five_vertex_orbits.csv` records each representative, its complete orbit size, its signed sum, degree sequence, component sizes and triangle count. Exactly the representatives \(28\), \(31\), and \(185\) have signed sum zero, with orbit sizes \(30\), \(30\), and \(60\), respectively; the table's orbit sizes add to \(1024\). The displayed graph descriptions follow from the representative edge sets. All remaining representatives have nonzero signed sum, and the smallest positive magnitude is \(2\). This is a finite exhaustive proof, not an inference from sampling.

The enumerations are checkable by two logically distinct chordality tests. `verify_cycles.py` explicitly enumerates every possible induced cycle of each length at least four, declaring a mask non-chordal precisely when all cycle edges and no chords are present. It computes each of the \(34\) representative signed sums directly without a Walsh transform. `verify_peo.cpp` instead repeatedly removes a vertex whose remaining neighbors form a clique; any induced chordless cycle is disjoint from every such vertex, so the procedure cannot erase a forbidden cycle, while chordal graphs admit perfect elimination orderings. That program evaluates the full Walsh vector by exact integer butterfly operations. Both tests cover every graph mask.

**Uniform six-vertex congruence.** Let \(A_e\) denote the number of six-vertex chordal graphs containing a specified edge \(e\). Exact enumeration gives
\[
|\mathcal C_6|=18154,\qquad A_e=8524\quad\text{for every }e\in E(K_6).
\]
The second equality for all edges follows from permutation symmetry once the count for edge \(12\) is established. For incidence bits \(x_e\in\{0,1\}\), the identity
\[
(-1)^{\sum_{e\in S}x_e}=\prod_{e\in S}(1-2x_e)
\equiv 1-2\sum_{e\in S}x_e\pmod4
\]
holds because terms involving at least two factors \(-2\) are multiples of four. Summation over all chordal graphs therefore yields
\[
W_6(S)\equiv18154-2\cdot8524|S|\equiv2\pmod4.
\]
Thus no coefficient vanishes. Direct exact signed enumeration at the frequency with lexicographic bit mask \(639\) gives \(W_6(639)=2\), proving sharpness. `six_vertex_edge_census.csv` gives independent reproducible incidence totals by edge count, while the two source programs verify the requisite totals independently. The full transform from `verify_peo.cpp` additionally has zero count zero, smallest absolute value two, and Parseval sum \(594870272=32768\cdot18154\).

**Convolution consequences.** Walsh characters diagonalize convolution, with eigenvalues \(W_n(S)\). Therefore its rank equals the number of nonzero coefficients, and its inverse or Moore–Penrose pseudoinverse Hilbert norm is the reciprocal of the least positive coefficient magnitude. The DC coefficient \(W_n(\varnothing)=|\mathcal C_n|\) is the largest magnitude by the triangle inequality, which gives the stated six-vertex condition number.

## Verification

All required artifacts are independent of the original execution environment and use only the C++17 standard library and Python 3 standard library:

```sh
g++ -O2 -std=c++17 verify_peo.cpp -o verify_peo
./verify_peo 5
./verify_peo 6
python3 verify_cycles.py
```

Expected check values are: at order five, \(822\) chordal graphs, \(120\) Walsh zeros, minimal positive magnitude \(2\), and Parseval sum \(841728\); at order six, \(18154\) chordal graphs, \(8524\) containing edge \(12\), zero Walsh zeros, minimal positive magnitude \(2\), and Parseval sum \(594870272\). The independent induced-cycle program checks the three orbit representatives, their sizes and complete coverage at order five and the two incidence counts and sharp witness at order six. No floating-point arithmetic or heuristic extrapolation is used.

## Relationship to prior work

The classical work of Wormald on labelled chordal-graph enumeration already supplies the ordinary counting setting; known labelled totals, including \(822\) and \(18154\), are also recorded as OEIS A058862. The later work of Hébert-Johnson, Lokshtanov and Vigoda gives polynomial-time exact counts and samplers for labelled chordal graphs. These are not claimed as new. The uniform modulo-four deduction is elementary once the edge-incidence parity is established, and any prior complete edge-count census can imply that deduction. What is additionally classified here is the cancellation of *arbitrary signed, labelled edge-subset characters* at order five, including the three distinct exceptional frequency shapes and their multiplicities. The cited counting theorems do not directly state this geometry-dependent Walsh classification. A separate early article of Chandran and Mathew concerns structural properties of \(k\)-chordal graphs, not Walsh sums.

## Limitations

The exact cancellation classification is limited to five vertices, and the uniform nonvanishing congruence is limited to six vertices. Nothing is inferred about chordal-graph Walsh zeros at larger orders. The novelty comparison is bounded: especially Wormald's 1985 paper was accessible through its abstract and metadata, not its complete text. Previously unpublished or unindexed signed enumerations may affect priority.

## References

- N. C. Wormald, *Counting labelled chordal graphs*, Graphs and Combinatorics 1 (1985), 193–200. DOI: https://doi.org/10.1007/BF02582944.
- L. Sunil Chandran and R. Mathew, *Bipartite powers of k-chordal graphs*, first public version 2011-08-01, https://arxiv.org/abs/1108.0277.
- Ú. Hébert-Johnson, D. Lokshtanov, and E. Vigoda, *Counting and Sampling Labeled Chordal Graphs in Polynomial Time*, https://arxiv.org/abs/2308.09703.
- OEIS A058862, *Number of chordal labeled graphs (connected or not) with n nodes*, https://oeis.org/A058862.
