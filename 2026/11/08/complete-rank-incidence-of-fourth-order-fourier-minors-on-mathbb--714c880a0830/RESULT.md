# Complete rank incidence of fourth-order Fourier minors on \(\mathbb F_5^2\)

## Finding
Let \(V=\mathbb F_5^2\), let \(\zeta=\exp(2\pi i/5)\), and let \(F=(\zeta^{a\cdot b})_{a,b\in V}\) be the unnormalized \(25\)-by-\(25\) additive Fourier matrix. For every pair of four-element sets \(A,B\subseteq V\), let \(r(A,B)=\operatorname{rank}_{\mathbb C}F[A,B]\). All \(\binom{25}{4}^2=160022500\) such **ordered pairs of sets** have the exact rank distribution
\[
\begin{array}{c|rrrr}
\text{rank}&1&2&3&4\\\hline
\text{number of pairs}&3750&600000&25875000&133543750.
\end{array}
\]
Thus exactly \(26478750\) fourth-order Fourier minors are singular.

The action of \(\operatorname{AGL}(2,5)\) on four-point sets has exactly five orbits. Encode \((x,y)\in V\) by the integer \(5x+y\); representatives and population sizes are
\[
\begin{array}{c|c|r}
\text{type}&\text{representative indices}&\text{population}\\\hline
L&(0,1,2,3)&150\\
T&(0,1,2,5)&6000\\
P&(0,1,5,6)&1500\\
Q&(0,1,5,7)&3000\\
R&(0,1,5,12)&2000.
\end{array}
\]
Here \(L\) consists of collinear fours, \(T\) of sets with exactly three collinear points, \(P\) of noncollinear parallelograms, and \(Q,R\) are the remaining two cap orbits.

For any **fixed** row four-set \(A\) of type indicated on the left, the number of column four-sets \(B\) of each type for which \(F[A,B]\) is singular is exactly
\[
\begin{array}{c|rrrrr|r}
 &L&T&P&Q&R&\text{total}\\\hline
L&25&4000&1000&2500&2000&9525\\
T&100&1000&500&600&0&2200\\
P&100&2000&150&400&400&3050\\
Q&125&1200&200&0&200&1725\\
R&150&0&300&300&300&1050.
\end{array}
\]
The complete rank distribution for any fixed row set of each type is
\[
\begin{array}{c|rrrr}
&\operatorname{rank}=1&2&3&4\\\hline
L&25&2000&7500&3125\\
T&0&25&2175&10450\\
P&0&50&3000&9600\\
Q&0&25&1700&10925\\
R&0&0&1050&11600.
\end{array}
\]
A finer type-by-type rank-incidence tensor, including the rank-two and rank-three entries, is implemented and explicitly asserted by the standalone exact checker `checker.py`.

## Assumptions and scope
The field is exactly \(\mathbb F_5\), the ambient group is the *elementary abelian* group \(\mathbb F_5^2\), and the Fourier pairing is the standard dot product. We count row and column index sets without internal ordering; the two sets occupy distinguished row and column positions. All ranks are over \(\mathbb C\). Changing Fourier normalization or character sign does not change the ranks. The theorem is a finite exhaustive classification, not a statement about arbitrary finite planes, prime-power cyclic groups, or Fourier minors of other orders.

## Proof
**1. The five affine orbits are exhaustive.** The affine group has size \(5^2(5^2-1)(5^2-5)=12000\). Enumerating its invertible linear maps and translations on each of the five displayed representatives gives disjoint orbits of cardinalities \(150,6000,1500,3000,2000\). Their sum is \(12650=\binom{25}{4}\), so these are all four-point sets and each belongs to exactly one type. This is verified by exact enumeration of the \(12000\) affine transformations, with no classification assumption needed beyond the displayed representatives.

**2. Affine invariance reduces every row to one representative.** An affine map \(a\mapsto Ma+t\), with \(M\) invertible, changes the Fourier submatrix by nonzero diagonal row and column factors and by the bijective column-index relabeling \(b\mapsto M^{\mathsf T}b\). Hence for fixed row type, the number of column sets of each affine type producing any given rank is unchanged. It suffices to inspect exactly the five displayed row representatives, rather than all \(12650\) row sets.

**3. Every tested determinant is exact.** A selected \(k\)-by-\(k\) submatrix, for \(k=2,3,4\), has entries fifth roots of unity. Expanding its determinant by all \(k!\) signed permutations produces integers \(c_0,\ldots,c_4\) such that the determinant equals \(\sum_{j=0}^4 c_j\zeta^j\). Since the monic minimal polynomial of \(\zeta\) is \(1+z+z^2+z^3+z^4\), this determinant vanishes **if and only if** \(c_0=c_1=c_2=c_3=c_4\). The resulting test uses only integer arithmetic. The exact rank is the largest size of a nonzero minor, testing sizes \(4,3,2\) in descending order; if every two-by-two minor vanishes, the rank equals one because every entry is nonzero.

**4. Full representative-by-column enumeration.** For each of the five row representatives, `checker.py` visits *every* one of the \(12650\) four-column sets, calculates the rank by the exact determinant criterion, and accumulates counts by the independently established column affine class. Every fine cell at ranks one, two, and three is compared against the integer tensor `EXPECTED`; rank four is its complement. The script also verifies every rank-specific symmetry \(n_i c_{ij}^{(r)}=n_j c_{ji}^{(r)}\), where \(n_i\) is the population of type \(i\). These are \(5\cdot12650=63250\) complete exact rank calculations, each checking the necessary minors: not sampled evidence.

**5. Extrapolation to all pairs is a proven finite symmetry reduction.** By Step 2, each fixed row type has the displayed rank counts. Multiplication by the exact populations \(n_i\) and summation yields the global rank totals \((3750,600000,25875000,133543750)\). The sum is \(160022500\). In particular \(3750+600000+25875000=26478750\) pairs are singular. Every count comes from an exhaustive finite computation over a completely specified integer domain.

## Verification
Run `python3 checker.py` and `python3 alt_checker.py` with the Python standard library. The script checks every affine orbit via \(12000\) exact transformations, then all \(63250\) reduced Fourier submatrices with exact fifth-root arithmetic, including subminor ranks and every rank-specific row/column transposition balance. Its final output is `F5_FOURTH_ORDER_FOURIER_MINORS_EXACT_PASS`. The accompanying `alt_checker.py` uses a different affine-normal-form orbit classification and separate exact determinant census to cross-check the global singular incidence; neither check introduces floating-point thresholds. The universal statement here is finite and is exhaustively verified by the standalone checker.

## Relationship to prior work
Tao's prime-order uncertainty principle establishes nonvanishing of minors of cyclic Fourier matrices of order prime; its Chebotarev property does not extend to the elementary-abelian group of order \(25\). Delvaux and Van Barel study maximal rank-deficient blocks and Hamming extremals of Kronecker products, including \(F_5\otimes F_5\), rather than the complete positional rank incidence of all its four-by-four minors. The earlier exact **ternary** affine-plane fourth-minor census has only two row-set types and a common singular degree \(45\); the five inequivalent singular degrees above distinguish the present result. The existing all-prime third-minor theorem applies only to three-by-three minors. Neither theorem implies the displayed fourth-minor rank distribution for \(\mathbb F_5^2\).

## Limitations
No formula is claimed for fourth-order minors in every odd characteristic or for the group \(\mathbb Z/25\mathbb Z\). Exhaustive computation is the finite certificate of the stated classification; the method is not a symbolic closed-form characterization of singularity for arbitrary row and column sets, beyond the exact cyclotomic determinant test. A prior tabulation or a stronger unlocated general theorem might also imply the same census. The cited comparisons do not establish absolute bibliographic priority.

## References
1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286v1 (first publicly submitted 2003-08-29), https://arxiv.org/abs/math/0308286.
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, KU Leuven Report TW477 (2006-11-15), later *Linear Algebra Appl.* **426** (2007), 349–367, https://doi.org/10.1016/j.laa.2007.05.009.
3. *The four-by-four Fourier-minor incidence of the ternary affine plane*, publicly available complete mathematical statement and proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-four-by-four-fourier-minor-incidence-of-the-ternary-affine-p--9f007d7c322e.
4. *Complete three-by-three Fourier-minor rank geometry on prime affine planes*, publicly available complete statement and proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-three-by-three-fourier-minor-rank-geometry-on-prime-aff--ba0b52ec4cec.
