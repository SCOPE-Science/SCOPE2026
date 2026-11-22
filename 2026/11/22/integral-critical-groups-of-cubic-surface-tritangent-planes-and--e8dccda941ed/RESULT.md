# Integral critical groups of cubic-surface tritangent planes and a cospectral quadrangle mate

## Finding
Let \(S\) be a smooth cubic surface over an algebraically closed field of characteristic zero. Let \(\Gamma_S\) be the graph with one vertex for each of its \(45\) tritangent planes, with two distinct planes adjacent if they contain a common line on \(S\). Its integral graph critical group is

\[
K(\Gamma_S)\cong (\mathbb Z/3\mathbb Z)^6\oplus(\mathbb Z/15\mathbb Z)^4\oplus(\mathbb Z/45\mathbb Z)^5\oplus(\mathbb Z/135\mathbb Z)^{14}.
\]

The second \(45\)-vertex adjacency matrix in Edward Spence's published collection of strongly regular graphs with parameters \((45,12,3,3)\), denoted \(\Gamma_2\), is cospectral with \(\Gamma_S\), but

\[
K(\Gamma_2)\cong (\mathbb Z/3\mathbb Z)^4\oplus(\mathbb Z/15\mathbb Z)^4\oplus(\mathbb Z/45\mathbb Z)^3\oplus(\mathbb Z/135\mathbb Z)^{16}.
\]

Thus the two graphs have identical adjacency eigenvalues and spanning-tree counts, but their integral critical groups are different. The minimum number of generators of their \(3\)-primary critical groups is respectively \(29\) and \(27\).

## Assumptions and scope
A smooth cubic surface over an algebraically closed field of characteristic zero is the blowup of \(\mathbb P^2\) in six general-position points. Write its Picard group in the ordered basis \((H,E_1,\ldots,E_6)\), with \(H^2=1\), \(E_i^2=-1\), other pairings zero. Each exceptional line is one of the \(27\) classes

\[
E_i\ (6),\qquad H-E_i-E_j\ (15),\qquad 2H-\sum_{j\ne i}E_j\ (6).
\]

The anticanonical class is \(-K_S=3H-\sum_iE_i\). A tritangent plane corresponds to an unordered triple of these exceptional lines whose divisor classes sum to \(-K_S\). Define the integral Laplacian \(L=12I-A\), where \(A\) is the symmetric adjacency matrix of \(\Gamma_S\). We use the critical-group normalization \(K(\Gamma_S)=\operatorname{tors}(\operatorname{coker}(L:\mathbb Z^{45}\to\mathbb Z^{45}))\), equivalently the cokernel of any reduced \(44\)-by-\(44\) Laplacian.

The comparison graph is exactly the second displayed binary adjacency matrix, not an arbitrary choice from the catalogue. Its original \(45\) matrix rows are embedded as `spence_second.txt`, allowing unambiguous reproduction of the comparator. Neither critical group is claimed to be the algebraic Picard, Brauer, or Jacobian group of \(S\).

## Proof
**Geometric enumeration.** Represent each divisor class \(aH-\sum b_iE_i\) by \((a,b_1,\ldots,b_6)\), and use the integral intersection pairing \((a,b)\cdot(a',b')=aa'-\sum b_ib_i'\). The three families above exhaust the \(27\) exceptional curves. Enumerate their unordered triples, retaining precisely those with class sum \((3,1,1,1,1,1,1)\) and every pair intersecting once. Exactly \(45\) triples remain; they are the tritangent sections. Two different triples share at most one line. Connecting triples with one common line gives a \(45\)-vertex graph with degree \(12\); any two distinct vertices, whether adjacent or not, have exactly three common neighbors. These finite assertions are exhaustively checked by the included verifier, using only the displayed divisor classes and intersection form.

**Spectrum and tree number.** Thus \(A\) is strongly regular with parameters \((45,12,3,3)\) and satisfies \(A^2=9I+3J\). Its eigenvalues are \(12\) once, \(3\) twenty times, and \(-3\) twenty-four times. Hence \(L\) has spectrum \(0\) once, \(9\) twenty times and \(15\) twenty-four times, and the Matrix–Tree theorem gives

\[
\det L_{\mathrm{red}}=\frac{9^{20}15^{24}}{45}=3^{62}5^{23}.
\]

Both graphs have this spectrum and determinant because the second catalogue matrix passes the identical strongly regular parameter checks.

**Integral Smith factors.** For each graph, take any reduced Laplacian. The exact local Smith valuations of its \(44\) nonzero diagonal factors, including zeros for units, are:

| Graph | Prime | Valuation multiplicities |
| --- | --- | --- |
| Cubic tritangent | \(3\) | \(0:15,\ 1:10,\ 2:5,\ 3:14\) |
| Cubic tritangent | \(5\) | \(0:21,\ 1:23\) |
| Spence second | \(3\) | \(0:17,\ 1:8,\ 2:3,\ 3:16\) |
| Spence second | \(5\) | \(0:21,\ 1:23\) |

These are computed by row and column swaps followed by elimination at a pivot with smallest \(p\)-adic valuation in the active submatrix. A pivot \(p^vu\) with \(u\) a unit is eliminated using its inverse modulo \(p^{k-v}\); the chosen precisions \(k=9\) for \(p=3\) and \(k=6\) for \(p=5\) exceed all observed valuations. Every operation is invertible over the indicated local ring, so this computes exact truncated Smith exponents; no factor is lost because the complete determinant has only primes \(3\) and \(5\), and the valuation sums are exactly \(62\) and \(23\). Pairing the ordered prime valuations positionwise yields precisely the invariant-factor groups stated above. The different \(3\)-ranks prove the groups are nonisomorphic and, consequently, the graphs are nonisomorphic despite being cospectral.

## Verification
Run `python3 verify_tritangent.py` in the directory containing `spence_second.txt`. The program uses only the Python standard library. It independently constructs the \(27\) line classes and the \(45\) tritangent triples from divisor arithmetic, checks all \(990\) unordered graph-vertex pairs against the strongly regular conditions, reads the second catalogue matrix, and verifies its symmetry and parameters. For both graphs and each of three different deleted vertices (indices \(0,9,20\)), it performs fraction-free Bareiss determinants of the resulting \(44\)-by-\(44\) matrices, and separate exact \(3\)-adic and \(5\)-adic Smith elimination. All six determinant checks yield \(3^{62}5^{23}\), and all twelve local Smith checks yield the respective spectra above. Successful output ends with `CUBIC_TRITANGENT_CRITICAL_GROUP_COMPARISON_OK`.

## Relationship to prior work
The tritangent–exceptional-line incidence is the classical generalized quadrangle \(GQ(4,2)\). Coolsaet, Degraer and Spence (2006) classify all \(78\) strongly regular graphs with parameters \((45,12,3,3)\), including the incidence graph's point graph; their classification and Spence's adjacency catalogue determine the ordinary graphs but do not state the two specific graph-critical-group structures calculated here. Özçelebi (2012), Chapter 6, studies Smith invariants of adjacency operators for a **different** graph: the non-collinearity/complement graph associated with \(GQ(4,2)\). Adjacency Smith invariants of a complement do not directly determine integral Smith factors of \(12I-A\). Biggs's 1999 chip-firing framework explains why these integral invariants can be finer than tree numbers; it does not present this pairwise classification.

The novelty is not a new strongly regular graph, a new graph spectrum, or a new count of tritangent planes. It is the explicit integral Laplacian Smith decomposition for the geometrically canonical \(45\)-vertex tritangent graph together with a parameter-matched, cospectral witness exhibiting a different critical group.

## Limitations
This is an exact finite calculation on two fully specified graphs, not a classification of critical groups for all \(78\) graphs in Spence's catalogue. It does not assert a correspondence between graph critical groups and the cubic surface's algebraic Picard group. A prior calculation under alternative labels such as the \(GQ(4,2)\) point graph, the tritangent-plane intersection graph, or elementary divisors of strongly regular Laplacians could duplicate the result; historical priority has not been independently certified. The formula is for algebraically closed characteristic-zero surfaces; arithmetic descent and positive-characteristic degenerations are not addressed.

## References
1. K. Coolsaet, J. Degraer and E. Spence, *The Strongly Regular (45,12,3,3) Graphs*, Electronic Journal of Combinatorics 13 (2006), R32, DOI: 10.37236/1058, full text: https://eprints.gla.ac.uk/12858/1/12858.pdf.
2. E. Spence, *Strongly Regular Graphs (45,12,3,3)*, adjacency-matrix catalogue: https://www.maths.gla.ac.uk/~es/SRGs/45-12-3-3 (second displayed graph used here).
3. Ç. G. Özçelebi, *Buildings and Kneser graphs* (2012), Chapter 6, especially Section 6.3.3 and Example 6.3.3.2: https://pure.tue.nl/ws/portalfiles/portal/3689733/721532.pdf.
4. J. A. Thas and H. Van Maldeghem, *Embeddings of Small Generalized Polygons*, https://cage.ugent.be/geometry/Files/128/smallemb.pdf (tritangent-plane incidence realization).
5. N. L. Biggs, *Chip-Firing and the Critical Group of a Graph*, Journal of Algebraic Combinatorics 9 (1999), 25–45, https://www2.math.ethz.ch/EMIS/journals/JACO/Volume9_1/m6g7032786582625.fulltext.pdf.
