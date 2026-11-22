# The complete five-frequency rank-incidence census for the ten-point Fourier transform

## Finding
Let \(\zeta=\exp(2\pi i/10)\), let \(F=(\zeta^{rc})_{r,c\in\mathbb Z/10\mathbb Z}\), and independently choose arbitrary five-element row and column sets \(R,C\). Among all \(\binom{10}{5}^{2}=63{,}504\) ordered pairs of unordered index sets, the complex ranks of \(F[R,C]\) have the exact multiplicities

\[
\begin{array}{c|rrr}
\operatorname{rank}_{\mathbb C} F[R,C]&3&4&5\\\hline
\#(R,C)&240&6{,}640&56{,}624.
\end{array}
\]

No restriction has rank below three. Moreover, **rank three occurs if and only if** one of the index sets is an even- or odd-residue coset modulo two, and the other meets the five residue classes modulo five with occupancies \((2,2,1,0,0)\) in some order. These two possibilities are disjoint, each contributes \(120\) pairs, and hence there are exactly \(240\) rank-three restrictions.

The following nine classes under \(R\mapsto aR+b\), \(a\in\{1,3,7,9\}\), \(b\in\mathbb Z/10\mathbb Z\), give the complete *row-set rank-incidence profiles*. In each table row, the three final counts refer to the \(252\) possible column sets for a single indicated row representative, not to the orbit as a whole.

| Representative row set \(R\) | Number of row sets in orbit | Rank 3 columns | Rank 4 columns | Rank 5 columns |
|---|---:|---:|---:|---:|
| \(\{0,1,2,3,4\}\) | 20 | 0 | 0 | 252 |
| \(\{0,1,2,3,5\}\) | 40 | 0 | 2 | 250 |
| \(\{0,1,2,4,5\}\) | 40 | 0 | 2 | 250 |
| \(\{0,1,2,3,6\}\) | 40 | 0 | 2 | 250 |
| \(\{0,1,2,4,6\}\) | 40 | 0 | 62 | 190 |
| \(\{0,2,3,4,6\}\) | 10 | 0 | 60 | 192 |
| \(\{0,1,2,5,6\}\) | 40 | 2 | 50 | 200 |
| \(\{0,1,3,5,6\}\) | 20 | 2 | 50 | 200 |
| \(\{0,2,4,6,8\}\) | 2 | 60 | 160 | 32 |

A five-frequency signal on the ten-point cyclic group is recovered from the five specified Fourier samples precisely in rank five; rank four or three leaves one or two independent directions undetermined, respectively. This is a complete central-cardinality incidence theorem, not just an existence statement for singular minors.

## Assumptions and scope
Rows and columns are taken as sets of distinct elements of \(\mathbb Z/10\mathbb Z\), with each set written in increasing order for computation. The *ordered pair* \((R,C)\) distinguishes the two roles; permutations within a set are not counted anew. Matrix rank is over \(\mathbb C\). Normalizing the Fourier matrix by \(1/\sqrt{10}\), or replacing \(\zeta\) by its conjugate, does not affect any rank or count. An affine row-set orbit uses only the four units modulo ten and ten translations; it does not assert that any arbitrary permutation of the ten indices preserves rank.

The archival motivation is the full-spark Fourier-frame problem and its earliest order-ten failure of a proposed uniform-residue criterion, studied in Alexeev--Cahill--Mixon (first posted 2011-10-17). The additional question here is how often each *amount of information loss* occurs for all central five-by-five restrictions, even among row sets that are not full spark.

## Proof
**Finite-field-to-cyclotomic exactness.** The tenth cyclotomic polynomial is \(\Phi_{10}(X)=X^4-X^3+X^2-X+1\). Every determinant \(\Delta\) of a square Fourier restriction of size \(k\le5\) is a signed sum of at most \(k!\) tenth-root monomials. Reduction modulo \(\Phi_{10}\) expresses it uniquely as

\[
\Delta=q(\zeta),\qquad q(X)=c_0+c_1X+c_2X^2+c_3X^3,
\quad c_i\in\mathbb Z,\quad |c_i|\le k!\le120.
\]

To see the coefficient bound explicitly, use \(\zeta^5=-1\) and \(\zeta^4=-1+\zeta-\zeta^2+\zeta^3\): each tenth-root monomial reduces to a polynomial whose individual coefficients lie in \(\{-1,0,1\}\). Each determinant expansion has at most \(k!\) such monomials.

In \(\mathbb F_{401}\), the four numbers \(29,83,329,362\) are precisely the four primitive tenth roots (verified by the attached program or direct modular powers). Hence \(q\) vanishes at all four roots if and only if all four coefficients are zero modulo \(401\), since its degree is at most three. But \(|c_i|\le120<401/2\), so divisibility by \(401\) then forces \(c_i=0\) in \(\mathbb Z\). This proves the exact equivalence

\[
\Delta=0\text{ in }\mathbb Q(\zeta)
\quad\Longleftrightarrow\quad
\Delta(\alpha)=0\text{ in }\mathbb F_{401}
\text{ for every }\alpha\in\{29,83,329,362\}.
\]

The equivalence applies to every minor of size at most five. Consequently, for every five-by-five restriction \(A\), its complex rank is **exactly the maximum** of its four ranks after substituting the above roots in \(\mathbb F_{401}\): any nonzero minor at one root proves nonvanishing in characteristic zero, and a complex nonzero minor cannot vanish at all four roots by the equivalence.

**Exhaustive rank certificate.** The independent, complete checkers `fourier10_rank.cpp` and `fourier10_cyclotomic.cpp` enumerate the \(252\) five-subsets in increasing binary-mask order and each of the \(63{,}504\) row-column pairs. The first performs exact modular Gaussian elimination for each of the four primitive roots, taking the maximum. The second, without using finite-field ranks, reduces actual determinant expansions in \(\mathbb Z[X]/(\Phi_{10})\) and tests minors of decreasing orders until an exact nonzero minor is found. Their rank totals independently coincide, proving the first table and the absence of rank-one or rank-two cases.

**Nine complete affine row classes.** Replacing a row index \(r\) by \(ar+b\), with \(a\) invertible modulo ten, permutes columns by \(c\mapsto ac\) and multiplies each column by a nonzero tenth root; this preserves the multiset of column-set ranks for a fixed row set. The first checker explicitly enumerates all affine transforms, selects the least ten-bit mask as canonical representative, checks the equality of the \(252\)-column rank profile on every member of each orbit, and emits the nine orbit representatives and their sizes. The orbit sizes sum to \(252\). Weighting each row's rank profile by its orbit size reproduces exactly \((240,6640,56624)\).

**Geometric characterization of the deepest defect.** Write \(H=\{0,2,4,6,8\}\), the order-five subgroup, and \(H+1\) for the other parity coset. When \(R\) equals either coset, the matrix \(F[R,C]\), up to row and column scalings and permutations, consists of columns of the fifth-order Fourier matrix indexed by the residues of \(C\) modulo five. Different residue classes give linearly independent columns by the prime-order Vandermonde determinant. Therefore its rank equals the number of distinct residues of \(C\) modulo five. Since \(|C|=5\) and each residue class has two representatives modulo ten, this number equals three exactly for occupancy pattern \((2,2,1,0,0)\). There are \(\binom{5}{3}\cdot3\cdot2=60\) such sets \(C\), giving \(2\cdot60=120\) pairs for parity-coset rows and another \(120\) after transposition. The checker exhaustively verifies the **converse** for all \(63{,}504\) pairs: no other pairs have rank three. The two described families do not overlap, since a parity coset has one element in each modulo-five class.

## Verification
In a C++17 environment, from the directory containing the two source files, run:

```sh
g++ -O2 -std=c++17 -Wall -Wextra fourier10_rank.cpp -o rank401
./rank401 > rank401.json
g++ -O3 -std=c++17 -Wall -Wextra fourier10_cyclotomic.cpp -o rank_exact
./rank_exact > rank_exact.json
```

The included `rank401.json` and `rank_exact.json` are outputs from execution of those programs. Both report the full rank histogram \((0,0,0,240,6640,56624)\), ordered by ranks zero through five. The first also records the nine orbit rows, their complete column-rank profiles, and an explicit all-pairs assertion of the rank-three criterion. All arithmetic is integer or prime-field arithmetic: numerical floating-point tolerances are not used. Runtime and executable binaries are not required for replay.

## Relationship to prior work
Alexeev, Cahill and Mixon (arXiv:1110.3548) proved the fundamental full-spark results for Fourier frames and exhibited an exceptional four-by-four singular restriction at order ten despite uniform distribution of the row indices. Their results do **not** enumerate central five-by-five rank losses. A subsequently published complete order-ten full-spark row-set classification gives which row masks are full spark (including the 20 consecutive-five row sets), but does not determine how many column sets have rank four rather than three, nor the complete nine-orbit incidence table. The full-spark facts are credited, not claimed as new.

Delvaux and Van Barel (2006 report; 2007 journal work) describe rank-one block constructions and maximal rank-deficient Fourier submatrices; these explain how subgroup-induced deficiencies arise but do not supply the all-pairs fifth-order rank distribution here. Published exact fifth-order rank-incidence tables for *different* cyclic orders twelve and fifteen are closely related in method, not covering cases at order ten. Recent principal-minor computations for order ten restrict to \(R=C\), so their assertions also do not imply the full independent row-column classification. Checks for equivalent rank-count formulations and databases did not identify a pre-existing statement of the complete order-ten fifth-order incidence table; this does not establish absolute novelty.

## Limitations
This theorem is finite and specific to ten-point Fourier transforms and five selected rows and columns. It does not provide sharp singular-value bounds, an asymptotic family, or a characterization of all cardinalities. It is not a new full-spark row-set classification. The exact checker fully certifies the finite domain, but its output is not a general formula for other Fourier orders. Historical-priority uncertainty remains for potentially unindexed numerical tables or differently framed sampling-matroid literature; independent validation has not yet been performed.

## References
1. B. Alexeev, J. Cahill and D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, first public version 2011-10-17, https://arxiv.org/abs/1110.3548.
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, K.U. Leuven Report TW 470, 2006-09-28, https://www.academia.edu/50129059/Rank_deficient_submatrices_of_Fourier_matrices; and *Rank-deficient submatrices of Kronecker products of Fourier matrices*, Linear Algebra Appl. 426 (2007), DOI:10.1016/j.laa.2007.05.009.
3. *Complete order-10 full-spark classification for harmonic Fourier row sets*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-complete-order-10-full-spark-classification-for-harmonic-fourier--579f4b382450.
4. *Complete fifth-order Fourier rank incidence on the twelve-cycle*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-complete-fifth-order-fourier-rank-incidence-on-the-twelve-cycle--db3ff8f3dd64.
5. *Exact three-dimensional loss and the complete five-frequency Fourier rank census at order fifteen*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-three-dimensional-loss-and-the-complete-five-frequency-fou--c7f8e777d742.
