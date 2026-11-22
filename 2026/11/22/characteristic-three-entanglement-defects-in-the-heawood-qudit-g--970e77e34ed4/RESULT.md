# Characteristic-three entanglement defects in the Heawood qudit graph state

## Finding

**Theorem (complete balanced-cut arithmetic entanglement law).** Let \(H\) be the fourteen-vertex point–line incidence graph of the Fano plane, with one point vertex and one line vertex for each of its seven points and lines. For every **prime** \(p\ge3\), prepare the standard pure \(p\)-level graph state \(\lvert H,p\rangle\): initialize each local state to \(p^{-1/2}\sum_{a\in\mathbb F_p}\lvert a\rangle\) and apply one unit-weight controlled-phase gate \(\lvert a,b\rangle\mapsto\exp(2\pi i ab/p)\lvert a,b\rangle\) on each of the 21 incidence edges. Consider all \(\binom{14}{7}/2=1716\) unordered balanced seven-versus-seven vertex bipartitions. On each partition the nonzero Schmidt probabilities are exactly equal, with number \(p^r\); hence **every** positive-order Rényi entropy and the von Neumann entropy equals \(r\log_2 p\) bits.

The complete histogram of the exponent \(r\) is

| Prime dimension | \(r=4\) | \(r=5\) | \(r=6\) | \(r=7\) |
|---|---:|---:|---:|---:|
| \(p=3\) | 21 | 273 | 729 | 693 |
| Every prime \(p\ge5\) | 21 | 273 | 700 | 722 |

**Exactly 29 unordered cuts** have a one-unit exponent deficit in characteristic three relative to every prime \(p\ge5\). They are precisely the canonical point-versus-line cut and the following 28 geometric cuts: choose any of the 28 noncollinear triples \(T\) of Fano points, and form one side from the four point vertices outside \(T\) and the three line vertices corresponding to the lines joining pairs of points in \(T\). These 29 cuts have exponents \(r=6\) at \(p=3\) and \(r=7\) at every prime \(p\ge5\). No other prime at least three changes a balanced-cut entanglement exponent. These claims concern the specified prime-dimensional graph state, not a generic fourteen-party state.

## Assumptions and scope

The Fano plane has seven points, seven lines, three points on each line, three lines through each point, and one line through each pair of distinct points. The Heawood graph \(H\) is its simple bipartite incidence graph, with fourteen vertices and 21 edges. Its graph-state adjacency weights are exactly one, not arbitrary nonzero elements of \(\mathbb F_p\). Prime \(p\ge3\) is required for the asserted finite-field rank formula. A balanced cut has seven vertices on each side; unordered cuts identify a set with its complement. A noncollinear triple means a three-point subset not equal to a Fano line, of which there are \(\binom73-7=28\). Logarithms of entropy use base two.

## Proof

**1. Graph-state cut spectrum.** For a balanced cut \(S\sqcup S^c\) with \(\lvert S\rvert=\lvert S^c\rvert=7\), let \(M_S\) be the integral \(7\times7\) adjacency matrix between the sides. Local phase gates internal to a side are local unitaries and do not change its Schmidt spectrum. The cross-cut state has coefficient phases \(\omega^{a^{\mathsf T}M_S b}\), where \(\omega=\exp(2\pi i/p)\). Taking the partial trace and using character orthogonality shows that its nonzero reduced eigenvalues are exactly \(p^{-r}\), each repeated \(p^r\), where \(r=\operatorname{rank}_{\mathbb F_p}(M_S)\). This proves the equality of all stated entropies. This is the standard graph-state cut-rank mechanism [1–3], not an originality claim.

**2. Exact complementary-incidence reduction.** Write the Fano incidence matrix \(N\) with point rows and line columns. Suppose \(S\) contains \(k\) point vertices indexed by \(X\) and precisely \(7-k\) line vertices indexed by \(L\setminus Y\), where \(\lvert X\rvert=\lvert Y\rvert=k\). After reordering rows and columns, the cross adjacency matrix is

\[
M_S\cong\operatorname{diag}\bigl(N[X,Y],\,N[P\setminus X,L\setminus Y]^{\mathsf T}\bigr).
\]

Therefore the integral Smith factors of \(M_S\), its rank over every prime, and its rank over the rationals can be determined from two complementary incidence minors. For a fully reproducible finite certificate, number the Fano points \(0,\ldots,6\) and take its seven lines to be \(\{j,j+1,j+3\}\pmod7\), for \(j=0,\ldots,6\). These form a projective plane because every point is on three lines and every pair on exactly one line. Build the symmetric fourteen-vertex zero-one adjacency matrix. Enumerate all size-seven vertex sets containing point vertex \(0\): there are \(\binom{13}{6}=1716\), exactly one from each unordered cut. For each, compute the *exact integer* Smith normal form of its \(7\times7\) cross adjacency matrix. The complete list of nonzero diagonal factors, with zero factors omitted, is:

| Smith factors | Number of unordered cuts |
|---|---:|
| \((1,1,1,1)\) | 21 |
| \((1,1,1,1,1)\) | 273 |
| \((1,1,1,1,1,1)\) | 476 |
| \((1,1,1,1,1,1,1)\) | 336 |
| \((1,1,1,1,1,2)\) | 196 |
| \((1,1,1,1,2,2)\) | 28 |
| \((1,1,1,1,1,1,2)\) | 252 |
| \((1,1,1,1,1,1,4)\) | 84 |
| \((1,1,1,1,1,2,4)\) | 21 |
| \((1,1,1,1,1,1,6)\) | 28 |
| \((1,1,1,1,2,2,6)\) | 1 |

This is an **exhaustive finite calculation**, with a complete deterministic program `verify_smith.py`; no extrapolation from a partial sample is used. The entries sum to 1716. An independent standard-library program `verify_modular.py` constructs the same Fano plane using nonzero vectors and orthogonality in \(\mathbb F_2^3\), enumerates all 1716 cuts, and recomputes their characteristic-dependent ranks using separate block-wise modular elimination. Their matching full histograms provide a second check, but the complete integer Smith census is the proof certificate for *all* prime dimensions simultaneously. The only nonunit prime divisors appearing in this census are \(2\) and \(3\). Removing factors divisible by \(p\) from the ranks gives exactly the two claimed histogram rows for \(p\ge3\).

**3. Geometric location of the characteristic-three defects.** The Smith census has 28 cuts with factors \((1,1,1,1,1,1,6)\) and one with \((1,1,1,1,2,2,6)\); these and only these 29 cuts lose a rank in characteristic three. For a noncollinear triple \(T\), the three lines joining its pairs are distinct. On the cut consisting of its four complementary point vertices and those three side-line vertices, the two incidence blocks from Step 2 have sizes four and three, with absolute determinants \(3\) and \(2\), respectively. (The three-by-three block is \(J-I\), of determinant \(2\); direct incidence inspection gives determinant magnitude \(3\) for the complementary four-by-four block.) The resulting cross matrix has determinant magnitude \(6\), giving full rank in every characteristic at least five and rank six in characteristic three. There are exactly 28 distinct noncollinear triples, yielding 28 such cuts. The canonical point-versus-line cut has cross matrix \(N\), with \(\lvert\det N\rvert=24\), rank seven at primes at least five and six at three. The code's equality test between these 29 explicitly constructed geometric cuts and the complete set of characteristic-three defective cuts proves the **converse**; no unexamined cuts remain. The two independent codes give the same equality.

## Verification

Run `python3 verify_smith.py` with Python 3.10+ and SymPy (tested with its integer `smith_normal_form`), and run `python3 verify_modular.py` with Python 3.10+ and no third-party dependency. Each executable independently enumerates all 1716 unordered balanced cuts. The first asserts the entire eleven-class integer Smith table, every rank histogram at primes 2, 3, 5, 7, 11 and 101, and the exact geometric description of the 29 characteristic-three cuts. The second constructs the incidence graph differently and independently verifies complete modular histograms at primes 2, 3, 5 and 101 and the same exceptional-cut geometry. Prime 2 is checked as an independent consistency control only; its histogram is **not** asserted to be a new contribution here. Smith factors prove the ranks for *all primes*, including those not explicitly checked in the finite-field program. These exact computations exhaust the specified finite graph, but provide no classification of different graphs or arbitrary weighted graph states.

## Relationship to prior work

Hein, Eisert and Briegel [1] give the foundational graph-state entanglement framework. Looi and collaborators [2] construct qudit graph states and quantum codes; Helwig [3] explicitly explains prime-dependent graph-state entanglement and efficient cut tests. They supply the framework used here, and this theorem does **not** claim new cut-rank principles or the existence of prime-dependent entanglement in general. A previously available complete binary Heawood balanced-cut census determines the qubit histogram, which is credited as prior and is not a contribution of this theorem. Cautrès and collaborators [4] study projective-plane incidence graphs as graph-state resources in a different, qubit vertex-minor/pairability setting. The closest publicly examined incidence matching-fault result [5] classifies deleted preparation gates across the **fixed point-versus-line qubit bipartition** of even-order projective planes, whereas this theorem fixes all original gates and classifies **every balanced bipartition for odd-prime qudits**, including the 28 triangular exceptions. This is not implied by that matching-fault theorem or the cited general cut-rank formulas without additional graph-specific arithmetic calculation. These comparisons establish scope separation, not a proof of historical uniqueness.

## Limitations

Only the ideal *pure*, unit-weight, prime-dimensional graph state on the fourteen-vertex Heawood graph is covered; no result is asserted for nonprime local dimension, arbitrary edge weights, noisy preparations, adaptive measurements, or a growing family of projective planes. The 29 exceptional cuts are characteristic-three defects relative to primes at least five; they are not necessarily exceptions relative to qubit entanglement, which is governed by different arithmetic. The exhaustive enumeration establishes this finite exact classification rather than a new general entanglement criterion. Despite searches of closely related literature and public research records, older or unindexed equivalent tabulations cannot be ruled out; there has been no independent scientific validation.

## References

1. M. Hein, J. Eisert and H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (first public version 18 July 2003), https://arxiv.org/abs/quant-ph/0307130 .
2. S. Y. Looi, L. Yu, V. Gheorghiu and R. B. Griffiths, *Quantum Error Correcting Codes Using Qudit Graph States*, arXiv:0712.1979 (first public version 12 December 2007), https://arxiv.org/abs/0712.1979 .
3. W. Helwig, *Absolutely Maximally Entangled Qudit Graph States*, arXiv:1306.2879 (12 June 2013), https://arxiv.org/abs/1306.2879 .
4. C. Cautrès, A. Claudet, M. Mhalla, S. Perdrix, J. Savin and S. Thomassé, *Vertex-minor universal graphs for generating entangled quantum subsystems*, arXiv:2402.06260, https://arxiv.org/abs/2402.06260 .
5. *Sharp incidence-matching fault threshold for graph-state entanglement on even-order projective planes*, publicly accessible scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-incidence-matching-fault-threshold-for-graph-state-entangl--0f1e8bff6768 .
