# Three extension-field spin counts recover the branch splitting of a genus-three hyperelliptic curve

## Finding
Let \(k=\mathbb F_q\) be any finite field of odd characteristic, and let \(C/k\) be a smooth, geometrically connected hyperelliptic curve of genus three. Let \(B\) denote the eight-point reduced branch scheme of its canonical double cover to its genus-zero quotient. Let \(\Theta_{\mathrm{odd}}\) and \(\Theta_{\mathrm{even}}\) be the finite étale \(k\)-schemes whose geometric points are theta characteristics \(L\) with \(L^{\otimes 2}\cong\omega_C\), separated according to the parity of \(h^0(C_{\bar k},L)\). They have respective geometric degrees \(28\) and \(36\).

For \(n\ge 1\), define
\[
O_n=\#\Theta_{\mathrm{odd}}(\mathbb F_{q^n}),\qquad E_n=\#\Theta_{\mathrm{even}}(\mathbb F_{q^n}).
\]
**The six integers \((O_1,E_1,O_2,E_2,O_3,E_3)\) uniquely determine the Frobenius cycle partition of all eight geometric branch points**, equivalently the residue degrees of the closed points of \(B\). The bound three is sharp **over each odd finite field**: the two branch partitions \((1,7)\) and \((3,5)\) have identical first- and second-extension spin counts \((0,1)\) but different third-extension counts, respectively \((0,1)\) and \((3,1)\). Both partitions are realized by separable degree-eight polynomials over every finite field.

Moreover, the full Frobenius cycle spectra of the odd and even theta schemes separately distinguish only \(19\) and \(21\) of the \(22\) possible branch partitions. Their joint first-three-extension counts distinguish all \(22\). The complete degree \(28\) and \(36\) cycle spectra, as well as the three pairs of rational-point counts, are in `theta_spectra.csv`.

## Assumptions and scope
The field has characteristic different from two. All objects and divisors are considered over the algebraic closure when describing the geometric labels; rational theta characteristics are fixed points of the arithmetic Frobenius action on the finite étale theta-characteristic schemes. The quotient of a hyperelliptic genus-three curve by its hyperelliptic involution is a genus-zero curve; over the finite field it has a point and is therefore isomorphic to \(\mathbb P^1\). The eight geometric branch points may include infinity. No assumption is made that they are individually rational. The result concerns the splitting of the branch divisor, not its cross-ratios or the zeta function of \(C\).

## Proof
**1. Geometric identification of the two spin schemes.** Let \(\pi:C\to\mathbb P^1\) be the double cover, and let \(H\) be its degree-two fibre class. Write \(P_1,\ldots,P_8\) for the ramification points over \(\bar k\). The canonical class is \(K_C\sim 2H\), and \(2P_i\sim H\). Hence every unordered pair \(\{i,j\}\), with \(i\ne j\), gives a theta characteristic \(P_i+P_j\). These are precisely the \(28\) odd theta characteristics. The even ones consist of the distinguished class \(H\), together with the \(35\) classes
\[
L_S=\sum_{i\in S}P_i-H\quad\text{for}\quad |S|=4,\qquad L_S=L_{S^c}.
\]
Distinct complementary pairs \(\{S,S^c\}\) yield distinct classes. The standard identification of the Jacobian's geometric two-torsion with even branch subsets modulo complement verifies that these lists exhaust the \(64\) theta characteristics; the parity is read from the dimensions of their linear systems. These divisor constructions are functorial under all permutations of the branch points, so Frobenius acts on the odd theta characteristics as on the \(28\) two-subsets of an eight-element set, and on the even characteristics as on one fixed point plus the \(35\) unordered four-plus-four partitions.

**2. Exact fixed-point formula.** Fix any \(n\ge1\). Let \(c_d(n)\) be the number of length-\(d\) cycles of the \(n\)th power of Frobenius on \(B(\bar k)\); then \(\sum_d d c_d(n)=8\), and put \(r(n)=\sum_d c_d(n)\). An unordered two-subset is invariant exactly when its two entries are individually fixed or form a two-cycle. Thus
\[
O_n=\binom{c_1(n)}2+c_2(n).
\]
A four-subset is itself invariant if and only if it is a union of whole cycles. The number of such subsets is the coefficient
\[
A_n=[z^4]\prod_{d\ge1}(1+z^d)^{c_d(n)}.
\]
A four-subset can instead be sent to its complement precisely when every cycle has even length; in that case the subset alternates along each cycle, with two independent choices per cycle. Therefore its number is
\[
B_n=\begin{cases}2^{r(n)},&c_d(n)=0\text{ for every odd }d,\\0,&\text{otherwise.}\end{cases}
\]
Each fixed unordered complementary pair contributes exactly two four-subsets among the events counted by \(A_n+B_n\). The distinguished even characteristic is always rational, giving
\[
E_n=1+\frac{A_n+B_n}{2}.
\]
These formulas are uniform for arbitrary odd \(q\) and for all \(n\); no finite-field size approximation is involved.

**3. Exhaustive eight-point comparison.** Every permutation of eight branch points is conjugate to one of the \(22\) integer partitions of eight; the comparison enumerates all abstract types, even though a small finite field may not realize every type. For a partition \(\lambda=(d_1,\ldots,d_s)\), take the corresponding disjoint-cycle permutation \(\sigma_\lambda\), compute the cycle decompositions of \(\sigma_\lambda^n\) for \(n=1,2,3\), and apply the formulas. The resulting table (\(O_n,E_n\) in that order) is:

| Branch cycles | \(n=1\) | \(n=2\) | \(n=3\) |
|---|---|---|---|
| \(1^8\) | (28,36) | (28,36) | (28,36) |
| \(1^6 2\) | (16,16) | (28,36) | (16,16) |
| \(1^5 3\) | (10,6) | (10,6) | (28,36) |
| \(1^4 2^2\) | (8,8) | (28,36) | (8,8) |
| \(1^4 4\) | (6,2) | (8,8) | (6,2) |
| \(1^3 2 3\) | (4,4) | (10,6) | (16,16) |
| \(1^3 5\) | (3,1) | (3,1) | (3,1) |
| \(1^2 2^3\) | (4,4) | (28,36) | (4,4) |
| \(1^2 2 4\) | (2,2) | (8,8) | (2,2) |
| \(1^2 3^2\) | (1,3) | (1,3) | (28,36) |
| \(1^2 6\) | (1,1) | (1,3) | (4,4) |
| \(1 2^2 3\) | (2,2) | (10,6) | (8,8) |
| \(1 2 5\) | (1,1) | (3,1) | (1,1) |
| \(1 3 4\) | (0,2) | (2,2) | (6,2) |
| \(1 7\) | (0,1) | (0,1) | (0,1) |
| \(2^4\) | (4,12) | (28,36) | (4,12) |
| \(2^2 4\) | (2,6) | (8,8) | (2,6) |
| \(2 3^2\) | (1,1) | (1,3) | (16,16) |
| \(2 6\) | (1,3) | (1,3) | (4,12) |
| \(3 5\) | (0,1) | (0,1) | (3,1) |
| \(4^2\) | (0,4) | (4,12) | (0,4) |
| \(8\) | (0,2) | (0,4) | (0,2) |

The six-number rows are pairwise distinct. If only the first two pairs are retained, precisely three collisions remain:
\[
(1^2 3^2)\sim(2,6),\qquad (1^2 6)\sim(2,3^2),\qquad (1,7)\sim(3,5).
\]
Thus depth three is sufficient and depth two is not sufficient. Finite fields contain irreducible polynomials of every positive degree, so the last two branch partitions are realized over every odd \(\mathbb F_q\) by squarefree products of distinct irreducibles of degrees \(1,7\) and \(3,5\), respectively. This proves sharpness over each such field.

**4. Stronger cycle-spectrum comparison.** The action on each parity set also gives its complete zeta function: if \(a_d\) and \(b_d\) are the respective length-\(d\) orbit multiplicities, then
\[
Z(\Theta_{\mathrm{odd}},T)=\prod_d(1-T^d)^{-a_d},\qquad Z(\Theta_{\mathrm{even}},T)=\prod_d(1-T^d)^{-b_d}.
\]
The finite table in `theta_spectra.csv` checks that the odd spectra have exactly three pairs of collisions, \((1^2 2^3,2^4)\), \((1^2 2 4,2^2 4)\), and \((1^2 6,2 6)\). The even spectra have exactly one pair, \((1^4 4,1^2 2 4)\). The joint first-three-extension invariant has no collisions.

## Verification
Run `python3 check_theta.py` beside `theta_spectra.csv` with Python 3 and no third-party dependencies. It performs two different computations for each of the \(22\) partitions: (i) direct orbit traversal of all \(28\) two-subsets and \(35\) complementary four-subset classes, and (ii) the fixed-point formulas from the cycle polynomial and the alternating-cycle count, for every extension degree through the permutation's order (and at least degree three). The two calculations agree, all parity degrees are checked, and all \(22\) six-number fingerprints, all claimed collisions, and all CSV cells are compared exactly. The verified output is `THETA_GENUS_THREE_THREE_EXTENSION_INJECTION_VERIFIED`.

## Relationship to prior work
The branch-subset classification of geometric theta characteristics, including the parity split and the symmetric-group action, is classical: see Dolgachev, Section 5.2, particularly formulas (5.13) and Section 5.2.3. Dina and Ionica use genus-three theta characteristics and the vanishing theta-null criterion for complex multiplication and class polynomials. Braden and Disney-Hogg compute theta-characteristic orbit profiles induced by automorphism groups of selected complex curves, including genus-three examples in their Table 6, and discuss the general affine action. These results provide the established geometric foundation; they do not state the uniform finite-field inverse theorem that the six counts over extensions of degrees one through three recover all branch residue degrees. This result is an exhaustive finite classification derived from that standard foundation, not a new general classification of theta characteristics.

## Limitations
The invariant recovers the branch-point factor degrees, not their coordinates, a moduli point, a curve zeta function, or the full arithmetic isomorphism class. The theta schemes are used as given arithmetic invariants: this theorem does not assert that computing them is faster than directly factoring a branch polynomial. The proof does not address characteristic two. The classification was derived by finite exact arithmetic on all \(22\) conjugacy types after the general geometric reduction; it is not a claim of novel general theta-subset theory. Historical priority for the exact three-extension fingerprint, including an unindexed equivalent finite table, has not been established independently.

## References
- H. W. Braden and L. Disney-Hogg, *Orbits of Theta Characteristics*, arXiv:2404.09890v1, first posted 2024-04-15, especially Sections 1–2 and Appendix A, Table 6. https://arxiv.org/abs/2404.09890
- B. A. Dina and S. Ionica, *Genus 3 hyperelliptic curves with CM via Shimura reciprocity*, arXiv:2003.06386, first posted 2020-03-13, Sections 2.2–2.3. https://arxiv.org/abs/2003.06386
- I. Dolgachev, *Classical Algebraic Geometry: a modern view*, Section 5.2.2–5.2.4, particularly the geometric two-torsion and theta-subset classification. https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/CAG.21.pdf
