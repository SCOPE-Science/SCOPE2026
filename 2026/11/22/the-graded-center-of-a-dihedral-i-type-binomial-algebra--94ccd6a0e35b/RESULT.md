# The graded center of a dihedral I-type binomial algebra

## Finding
Let \(k\) be any field. Let \(A\) be the coefficient-free graded monoid algebra on \(x_0,x_1,x_2,x_3\), subject to
\[
\begin{gathered}
x_0^2=x_3x_1,\quad x_0x_1=x_1x_2,\quad x_0x_2=x_2x_0,\\
x_1^2=x_3^2,\quad x_1x_3=x_2^2,\quad x_2x_3=x_3x_0.
\end{gathered}
\]
This is the coefficient-free form of Algebra 21 from Bhatoy's four-generator I-type examples. With each generator in degree one, its **entire graded center** has Hilbert series
\[
\boxed{H_{Z(A)}(t)=\sum_{d\ge0}\dim_k Z(A)_d\,t^d
=\frac{1-t^2+t^4}{(1-t^2)^2(1-t^4)^2}.}
\]
In particular the odd-graded center vanishes, and its dimensions at degrees \(0,2,4,6,8,10,12,14,16\) are respectively \(1,1,4,5,11,14,24,30,45\), independent of the characteristic.

More structurally, let \(D_8\) act on four coordinates by the permutations given below, and define the index-eight lattice
\[
\Lambda=\{u\in\mathbb Z^4:\ u_0-u_3\equiv0\pmod2,\quad u_0+u_1-u_2-u_3\equiv0\pmod4\}.
\]
Then there is a canonical graded algebra isomorphism
\[
 Z(A)\cong k[\Lambda\cap\mathbb N^4]^{D_8},
\]
where the action permutes lattice monomials; this invariant-ring description holds in every field characteristic.

## Assumptions and scope
Write permutations as maps on \(\{0,1,2,3\}\), composed from right to left. The four left actions of the I-type structure are
\[
L_0=(0\ 3),\qquad L_1=(0\ 1\ 3\ 2),\qquad L_2=(1\ 2),\qquad L_3=(0\ 2\ 3\ 1).
\]
They generate \(F\cong D_8\), of order eight. The source establishes that these relations define an I-type monoid, and that its fraction group embeds in \(\mathbb Z^4\rtimes F\) by \(x_i\mapsto(e_i,L_i)\), with a bijection between monoid elements and their nonnegative first coordinates. This structural input is used, not reproved. The theorem concerns the coefficient-free monoid algebra, not arbitrary scalar twists. The underlying coefficient-free monoid is characteristic-free, so the result holds for all fields \(k\).

## Proof
**1. Translation kernel.** Let \(G\subseteq\mathbb Z^4\rtimes F\) be the fraction group and \(N=\ker(G\to F)\). The injection of the monoid into \(G\) and the I-type coordinate bijection show that \(N\) is identified with a full sublattice of \(\mathbb Z^4\). Direct multiplication of the displayed generator pairs shows that the words \(x_0^2,x_1x_3,x_1x_0x_1x_0,x_2x_1x_1x_0\) have trivial permutation component and respective coordinate vectors
\[
(1,0,0,1),\quad (0,1,1,0),\quad(0,2,0,2),\quad(0,0,2,2).
\]
Their determinant has absolute value eight. Consequently these vectors generate an index-eight subgroup of \(\mathbb Z^4\) contained in \(N\). Because \(G/N=F\) has order eight, this subgroup equals \(N\). Each vector satisfies the two displayed congruences; those congruences themselves define an index-eight lattice. Thus \(N=\Lambda\) in first-coordinate form.

**2. Center versus finite conjugacy.** In \(G\), conjugating an element with nonidentity permutation component \(p\) by \((w,1)\in N\) alters its translation coordinate by \((1-p)w\). Since \(N\) has rank four, and \(p\ne1\) acts nontrivially, this yields an infinite conjugacy class. Thus every central element of the group algebra \(k[G]\) is supported on \(N\). Within \(N\), the \(G\)-conjugacy classes are exactly the finite \(F\)-orbits under the coordinate-permutation action. Hence \(Z(k[G])=k[N]^F\), in any characteristic. An element central in \(k[M]\) also commutes with the inverses of every generator inside \(k[G]\), and conversely any invariant positive-support group-algebra element centralizes \(k[M]\). The I-type bijection identifies \(N\cap M\) with \(\Lambda\cap\mathbb N^4\), which is stable under \(F\). Therefore \(Z(A)=k[\Lambda\cap\mathbb N^4]^F\).

**3. Exact graded Hilbert series.** Its degree-\(d\) basis consists of sums over \(F\)-orbits of nonnegative \(u\in\Lambda\) with \(\sum_i u_i=d\), regardless of characteristic. Integer Burnside counting applies to these orbit sets. Put \(s=t^2\). Applying the two congruences to vectors fixed by each of the eight permutations gives the following five types of fixed-vector generating functions:

| Permutation type | Multiplicity | Fixed-vector generating function |
|---|---:|---|
| Identity | 1 | \((1+6t^4+t^8)/((1-t^2)^2(1-t^4)^2)\) |
| Half-turn swapping \(0,3\) and \(1,2\) | 1 | \(1/(1-t^2)^2\) |
| Reflections of cycle type \((2,2)\) | 2 | \((1+t^4)/(1-t^4)^2\) |
| Reflections of cycle type \((2,1,1)\) | 2 | \((1+t^4)/((1-t^2)^2(1-t^4))\) |
| Four-cycles | 2 | \(1/(1-t^4)\) |

For completeness, each table entry is obtained by setting coordinates equal on cycles and reducing their residues modulo four; each free cycle coordinate then contributes a geometric denominator \(1-t^{4\ell}\), where \(\ell\) is its cycle length. For example, the half-turn fixes \(u=(a,b,b,a)\), and both congruences are automatic, giving \((1-t^2)^{-2}\). The remaining entries follow from the same at-most-four-residue check; `verify_center.py` independently enumerates the congruence solutions and permutation orbits. The average of these eight rational functions simplifies exactly to \((1-t^2+t^4)/((1-t^2)^2(1-t^4)^2)\). This proves the infinite formula.

## Verification
The accompanying standalone Python 3 script uses only the standard library. It constructs the eight-element permutation group from the four generators, independently walks the I-type positive coordinates and their permutation labels through degree sixteen, checks the kernel congruences on all encountered elements, counts actual translation-orbits, and compares every resulting degree with the coefficient expansion of the claimed rational series. It returns `I_TYPE_DIHEDRAL_CENTER_OK` on success. These computations are finite cross-checks of the preceding algebraic and rational-function proof, not a substitute for the infinite argument.

## Relationship to prior work
Bhatoy (2026), Example 6 and Table 1, supplies the coefficient-free algebra, the left-action permutations and its dihedral group of fractions, within a study of twisted monoid algebras and second group cohomology. The source does not state this center or its graded Hilbert series. Goffa–Jespers (2006) studies structural properties of IG-type monoid algebras, while other permutation-twist calculations give centers for cyclic single-permutation Zhang twists, not this nonabelian dihedral I-type structure. The present invariant lattice and its five-class Burnside calculation determine the exact center in this particular example. General structural results for monoid algebras and finite-group invariant rings underpin, but do not supply, the displayed lattice and rational series without a separate computation.

## Limitations
The theorem does not classify centers of all twenty-three binomial examples or nontrivial cocycle twists. It does not give a presentation of the invariant ring by minimal generators and relations. The priority comparison is based on the recent paper's relevant full-text sections, relevant existing structural literature, indexed mathematical claim searches; uncatalogued equivalent computations remain possible. Independent mathematical audit has not been performed.

## References
1. V. Bhatoy, *Binomial Artin-Schelter Regular Algebras and Twisted Monoid Algebras*, arXiv:2611.03989v1 (first public 2026-11-02), especially Example 6, Table 1, and Theorem 1. https://arxiv.org/abs/2611.03989
2. I. Goffa and E. Jespers, *Monoids of IG-type and Maximal Orders*, arXiv:math/0601546 (2006). https://arxiv.org/abs/math/0601546
