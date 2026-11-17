# A bounded-to-exponential transition in pure majority oscillations on cyclic clique strips

## Finding

For each integer \(n\ge3\) and \(r\in\{3,4\}\), let \(G_{r,n}=C_n\square K_r\) have labelled vertices \((i,j)\), with \(i\in\mathbb Z/n\mathbb Z\) and \(0\le j<r\). Let \(F_{r,n}\) be synchronous strict open-neighbor binary majority with incumbent tie retention. A *pure two-cycle configuration* is a state \(x\) satisfying \(F_{r,n}(x)=\bar x\), where \(\bar x\) is the coordinatewise complement. Denote the number of such labelled configurations by \(P_r(n)\).

For width three there is complete rigidity:
\[
\boxed{P_3(n)=3\bigl(1+(-1)^n\bigr).}
\]
For width four, let \(\mathcal B\) be the six length-four binary words of Hamming weight two. Index a \(36\times36\) integer matrix \(M\) by ordered pairs \((a,b)\in\mathcal B^2\). Define
\[
M_{(a,b),(b',c)}=\begin{cases}
1,&b=b'\text{ and for every }j\in\{0,1,2,3\},\ (a_j,b_j,c_j)\ne(0,0,0),(1,1,1),\\
0,&\text{otherwise}.
\end{cases}
\]
Then the complete exact all-size pure-cycle census is
\[
\boxed{P_4(n)=\operatorname{tr}(M^n)+4\bigl(1+(-1)^n\bigr).}
\]
The explicitly defined integer matrix has exactly 90 nonzero entries, and its full characteristic polynomial is
\[
\begin{aligned}
\chi_M(z)={}&(z-1)^3(z+1)^4(z^2+1)^3(z^3-2z^2-4z+1)\\
&\cdot(z^4-z^3-3z+1)^2(z^4+z^3+2z^2-3z+1)^3.
\end{aligned}
\]
If \(\lambda=3.16424793846021\ldots\) is the unique root greater than three of \(z^3-2z^2-4z+1\), then
\[
\boxed{P_4(n)=\lambda^n+O(2^n),\qquad \lim_{n\to\infty}\frac{\log P_4(n)}n=\log\lambda.}
\]
Every state counted above belongs to a genuine temporal orbit of least period two, with its other phase the complement; the number of distinct pure temporal orbits is \(P_r(n)/2\). Therefore changing the column clique from three to four vertices changes the pure-oscillation entropy from zero (on the nonempty even-length subsequence) to \(\log\lambda\).

## Assumptions and scope

The cycle \(C_n\) is simple, so \(n\ge3\) ensures the left and right spatial neighbors are distinct. The clique \(K_r\) supplies \(r-1\) within-column neighbors; every vertex has degree \(r+1\). At each update a vertex adopts the strict majority of its neighbors, preserving its previous bit on equality. Binary complement commutes with this rule, even when ties occur. The statement counts initial *fully flipping* states, not all primitive two-cycles, nonperiodic initial states, their basins, or their transient times.

## Proof

**Local full-flip test.** Since complementing every bit interchanges the neighbor counts and preserves the tie rule, \(F(\bar x)=\overline{F(x)}\). Thus \(F(x)=\bar x\) implies \(F^2(x)=x\) and gives a genuine two-cycle. A vertex changes from its present bit precisely when strictly more than half of its \(r+1\) neighbors disagree. Hence for \(r=3\) it may have at most one same-colored neighbor, and for \(r=4\) at most two.

**Three-vertex clique columns.** A monochromatic column would give every vertex two same-colored clique neighbors and cannot flip. Thus every column has a two-to-one color split. Each of its two majority-colored vertices already has one same-colored neighbor inside the column, so both corresponding positions in each adjacent column must have the opposite bit. The neighboring column cannot be monochromatic, hence its last bit must also be opposite. Consequently consecutive columns are complements. Conversely, an alternating sequence of complementary, nonmonochromatic columns satisfies the local full-flip test. Closure around the cycle requires even \(n\). There are exactly six possible starting nonmonochromatic three-bit columns, establishing the first formula.

**Four-vertex clique columns.** A monochromatic column is impossible, because every vertex already has three same-colored clique neighbors. If a column has a three-to-one split, its three majority-colored sites already have two same-colored clique neighbors and require both adjacent horizontal neighbors to have the opposite bit. Each adjacent column therefore has three forced opposite bits; its fourth bit must also be opposite, since a monochromatic column is forbidden. Thus adjacent columns are complementary three-to-one splits, and all columns alternate in this way. These exceptional states contribute eight configurations if \(n\) is even and zero otherwise.

In all other pure states every column is balanced, having two zeroes and two ones. Each site then has exactly one same-colored clique neighbor and can flip precisely if its two horizontal neighbors are not both the same as itself. Equivalently, for every fixed row \(j\), no three consecutive column bits are all equal. The matrix \(M\) above encodes this complete local constraint: an edge \((a,b)\to(b,c)\) is allowed exactly when the central column \(b\) passes all four tests. Closed walks of length \(n\) correspond bijectively to labelled cyclic balanced-column sequences satisfying all these tests (with prescribed starting column index). Therefore their number is \(\operatorname{tr}(M^n)\). The exceptional and balanced cases are disjoint, proving the exact formula.

**Exact spectrum and entropy.** Expanding \(\det(zI_{36}-M)\) in integer arithmetic yields the displayed characteristic polynomial. The standalone symbolic checker explicitly builds all 36 states and computes the determinant's characteristic polynomial without floating-point arithmetic. The eigenvalue power-sum identity gives \(\operatorname{tr}(M^n)\) as a sum of algebraic eigenvalues raised to \(n\), counted with multiplicity, regardless of any Jordan blocks. The cubic has exactly one real root greater than three. Direct exact root isolation, or the polynomial and its derivative together with rational sign checks, place this root in \((3.1642,3.1643)\). The cubic changes sign across each of the three disjoint rational intervals \((-2,-1)\), \((0,1)\), and \((3,16/5)\); since its degree is three, exactly one root lies in each. For both quartics, the strict real Schur reduction applied to \(h(w)=p(2w)\) certifies every root is in the open disk of radius two. Namely, at each step the absolute value of the constant coefficient is strictly less than the leading coefficient's absolute value, and we replace \(h(w)=a_dw^d+\cdots+a_0\) by \((a_dh(w)-a_0w^dh(1/w))/w\), dividing out a common integer factor. For \(z^4-z^3-3z+1\), the successive exact coefficient pairs \((a_d,a_0)\) are \((16,1),(255,-88),(57281,-10736),(3103,-2074)\). For \(z^4+z^3+2z^2-3z+1\), they are \((16,1),(255,-104),(54209,44536),(6583,3110)\). These strict tests certify all quartic roots have modulus below two. The checker independently reconstructs these certificates using exact integer arithmetic. The remaining eigenvalues are \(\pm1,\pm i\). Hence the simple dominant root contributes \(\lambda^n\), and every other contribution is \(O(2^n)\), proving the asymptotic and entropy limit.

## Verification

`check_transfer.py` constructs the exact integer transfer matrix, verifies its 90 entries and entire symbolic characteristic polynomial, checks transfer counts for \(3\le n\le12\), and checks strict spectral separation using rational cubic root intervals and exact integer Schur reductions for both quartics. `verify_direct.cpp` independently simulates the vertex-level strict majority update and exhaustively checks all \(2^{rn}\) bit states for \(r=3,\ 3\le n\le7\) and \(r=4,\ 3\le n\le6\). The two methods agree where their ranges overlap. The labelled counts for widths three/four at \(n=3,4,5,6\) are, respectively, \((0,90),(6,98),(0,270),(6,1388)\). The direct enumeration examines 20,292,096 states in total; this finite check supports but does not substitute for the all-size bijection.

## Relationship to prior work

General symmetric threshold dynamics is known to converge to fixed points or two-cycles (Goles and Olivos, 1980). Benjamini and collaborators (2014) study convergence and disagreement for majority dynamics on general graphs. Turau (2022) characterizes pure majority two-cycles on *trees*; cyclic clique strips have many triangles and nontrivial cycles, so that tree characterization does not enumerate the present family. The closest accessible prior exact result on \(C_n\square K_3\), *Exact majority-fixed census and entropy on triangular cylindrical strips* (published-finding corpus, 2026), counts **fixed** configurations only, and explicitly does not count primitive two-cycles. The present pure-cycle formula and its width-three/width-four entropy discontinuity are not implications of those fixed-state counts or the general period-at-most-two theorem. The models are compared by dynamical object and counted population, not by title alone.

## Limitations

No formula for two-cycles that contain both stationary and flipping vertices is claimed. No description of attraction basins or first-entry times is claimed. The entropy transition compares only two natural consecutive clique widths and does not assert an all-width phase diagram. The symbolic determinant is an exact finite calculation; its checked factorization is independently reproducible but not a manual cofactor expansion. Unindexed or unavailable equivalent results may exist, so historical priority is not certified. Independent mathematical validation has not been performed.

## References

- E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, doi:10.1016/0012-365X(80)90121-1. https://pure.uai.cl/en/publications/periodic-behaviour-of-generalized-threshold-functions/
- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first posted 2014-05-11, arXiv:1405.2486v1. https://arxiv.org/abs/1405.2486
- V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, first posted 2022-02-03, arXiv:2202.01580. https://arxiv.org/abs/2202.01580
- *Exact majority-fixed census and entropy on triangular cylindrical strips*, result `874a8ff5f9e5`, available in published-finding corpus/2026 repository: https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-majority-fixed-census-and-entropy-on-triangular-cylindrica--874a8ff5f9e5/RESULT.md
