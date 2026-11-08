# Exact multiplication-rank census in the five-generator elementary-abelian group algebra

## Finding
Let \(k=\mathbb F_q\), with \(q\) a power of two, and let
\[
A=k[C_2^5]\cong k[x_1,x_2,x_3,x_4,x_5]/(x_1^2,x_2^2,x_3^2,x_4^2,x_5^2).
\]
For \(f\in A\), write \(m_f:A\longrightarrow A\) for multiplication by \(f\). Set
\[
G(q)={5\brack2}_q=(q^2+1)(q^4+q^3+q^2+q+1),\qquad
B(q)=(q-1)G(q),\qquad C(q)=q^{10}-1-B(q).
\]
Then **every coefficient** of the complete multiplication-rank polynomial is given by
\[
\begin{aligned}
\mathscr R_q(T)=\sum_{f\in A}T^{\operatorname{rank}m_f}
={}&1+(q-1)T+q(q^5-1)T^2+B(q)q^6T^4+C(q)q^6T^6\\
&+B(q)q^{15}T^8+B(q)(q-1)q^{15}T^{10}+C(q)q^{16}T^{12}\\
&+(q^5-1)q^{26}T^{16}+(q-1)q^{31}T^{32}.
\end{aligned}
\]
In particular, over every field of characteristic two, the possible multiplication ranks in this algebra are exactly
\[
\{0,1,2,4,6,8,10,12,16,32\}.
\]
A structural distinction explains the two middle ranks. Let \(f\) have zero constant and linear parts and let its quadratic part \(f_2\ne0\) be decomposable. After a linear change of generators write \(f_2=ab\) and let \(W=\langle c,d,e\rangle\) be the complementary three-space. The image of the cubic part in \(\bigwedge^3(V/\langle a,b\rangle)\) is a well-defined scalar multiple \(\gamma\,cde\). Then
\[
\operatorname{rank}m_f=\begin{cases}8&\gamma=0,\\10&\gamma\ne0.\end{cases}
\]
Thus \(ab\) and \(ab+cde\) have the **same initial quadratic form**, but their multiplication ranks are \(8\) and \(10\). Five generators are the first number for which a cubic term disjoint from a decomposable quadratic term can cause this jump.

## Assumptions and scope
The field for the counting polynomial is any finite field of characteristic two; the normal forms, possible-rank list, and cubic-obstruction criterion hold over any field of characteristic two. The algebra is **unital** and has dimension \(32\). Each algebra element, not each distinct principal ideal, is counted once; the rank is the dimension of the principal ideal \((f)\) as a vector space. For elements with zero constant term, \(f^2=0\), so the multiplication Jordan type is \((2^r,1^{32-2r})\) when the rank is \(r\). Elements with nonzero constant term are units and are counted at rank \(32\).

## Proof
**1. Group-algebra identification and leading degree.** For the five standard commuting involutions \(g_i\), set \(x_i=g_i-1\). In characteristic two, \(x_i^2=0\), and the \(32\) squarefree monomials form a basis. The algebra is also the exterior algebra \(\bigwedge V\) in characteristic two. Any map sending its five generators to elements of the augmentation ideal with linearly independent linear parts is an automorphism: the images have square zero and induce an isomorphism on \(J/J^2\); Nakayama's lemma (or an elementary nilpotent-filtration argument) gives surjectivity, hence bijectivity. Multiplication rank is unchanged by algebra automorphisms and by multiplying \(f\) by a unit. If the constant term is nonzero, \(f\) is a unit, hence rank \(32\). If the constant vanishes but the linear part is nonzero, send one generator to \(f\) by an automorphism and complete its linear part to a basis; multiplication by that generator has rank \(2^4=16\).

**2. Quadratic leading part.** A nonzero \(f_2\in\bigwedge^2V\) is an alternating bivector of rank two or four. A rank-four form has normal form \(ab+cd\), with a fifth generator \(e\). Every squarefree monomial of degree \(3\), \(4\), or \(5\) contains at least one of \(a,b,c,d\). The first derivatives of \(ab+cd\) span precisely \(\langle a,b,c,d\rangle\). Replacing generators by a generator plus a term of degree \(j-1\) changes the degree-\(j\) part of this quadratic by an arbitrary element of \(\bigwedge^jV\), for \(j=3,4,5\), while only affecting already-unadjusted higher degrees. Eliminating degree \(3\), then \(4\), then \(5\), shows that \(f\) is automorphism-equivalent to \(ab+cd\). On \(\bigwedge\langle a,b,c,d\rangle\), multiplication by \(ab+cd\) has rank \(6\): its three nonzero graded pieces have ranks \(1,4,1\). Tensoring with the exterior algebra on \(e\) doubles the rank, giving \(12\).

For rank-two \(f_2\), choose \(f_2=ab\), \(V=\langle a,b\rangle\oplus W\), and \(\dim W=3\). Every higher correction can be written uniquely in the form
\[
f=ab\,u+a\alpha+b\beta+\gamma cde,
\]
with \(u\in\bigwedge W\) a unit of constant term one, \(\alpha,\beta\in\bigwedge^{\ge2}W\), and \(\gamma\in k\). First multiply by \(u^{-1}\); as \(u^{-1}(cde)=cde\), this retains \(\gamma\) and changes only \(\alpha,\beta\). The automorphism replacing \(a\) by \(a+\beta\) and \(b\) by \(b+\alpha\), fixing \(W\), takes \(ab+\gamma cde\) to the resulting element, because \(\alpha\beta=0\) in the three-variable exterior algebra. Hence \(f\) has the rank of \(ab+\gamma cde\). For \(\gamma=0\), this rank is \(1\cdot 8=8\). If \(\gamma\ne0\), regard multiplication by \(ab+\gamma cde\) as the square-zero operator
\[
m_{ab}\otimes I+I\otimes m_{\gamma cde}
\]
on the tensor product of the four-dimensional and eight-dimensional exterior algebras. The first factor has one size-two Jordan block and two size-one blocks; the second has one size-two block and six size-one blocks. The tensor differential has rank \(2+6+2=10\), by checking the four types of block tensors (or by its homology dimension \(2\cdot6=12\)). The class \(\gamma cde\) is intrinsically the projection of \(f_3\) to \(\bigwedge^3(V/\operatorname{supp}(f_2))\), so the dichotomy is independent of choices.

**3. Cubic and higher leading parts.** For a nonzero homogeneous \(f_3\in\bigwedge^3V\), the map \(V\to\bigwedge^4V\), \(v\mapsto f_3v\), has rank \(2\) or \(4\). Indeed, after identifying \(\bigwedge^4V\) with \(V^*\) using a volume form, it is represented by a nonzero alternating \(5\)-by-\(5\) matrix. In multiplication by \(f_3+f_4+f_5\), the unit input contributes one independent image with degree-three leading term, and multiplication of degree-two inputs surjects onto the one-dimensional degree-five space. Modulo that last image, the degree-one inputs contribute exactly the aforementioned rank \(2\) or \(4\). Higher inputs contribute zero. Consequently the total rank is \(4\) or \(6\), independently of \(f_4,f_5\). If \(f_4\ne0\) is the leading part, the images of degree-zero and degree-one inputs have independent dimensions \(1\) and \(1\), giving rank \(2\); if only \(f_5\ne0\), the rank is \(1\). The zero element has rank \(0\).

**4. Exact finite-field counts.** The number of nonzero decomposable bivectors is
\[
B(q)=(q-1){5\brack2}_q,
\]
since each determines a unique two-plane and a nonzero scalar in its one-dimensional second exterior power. The other nonzero bivectors number \(C(q)=q^{10}-1-B(q)\) and have rank four. Hodge duality makes the counts of rank-two and rank-four cubic forms the same. The higher coefficients for a prescribed nonzero cubic form have \(q^6\) choices; these give the coefficients at ranks \(4,6\). For a prescribed rank-four quadratic form, the higher coefficients have \(q^{10+5+1}=q^{16}\) choices and all give rank \(12\). For a prescribed decomposable quadratic form, the cubic obstruction takes the value zero for \(q^9\) cubic coefficients and a nonzero value for \((q-1)q^9\) cubic coefficients. Degree-four and degree-five coefficients contribute another \(q^6\) choices, giving coefficients at ranks \(8,10\). The other degrees contribute respectively \(q-1\), \(q(q^5-1)\), \((q^5-1)q^{26}\), and \((q-1)q^{31}\), corresponding to leading degrees five, four, one and zero. The displayed polynomial follows by disjoint cases, and its coefficients sum to \(q^{32}\).

## Verification
The included `check.py` calculates ranks of the **original multiplication matrices** in the squarefree-monomial basis using finite-field Gaussian elimination. Over \(\mathbb F_2\), it exhaustively checks all \(2^{16}\) high-degree perturbations of each of the two canonical quadratic ranks, all \(2^{10}\) quadratic leading forms, all \(2^{10}-1\) nonzero cubic forms, and the nonzero quartic/quintic forms; it also checks all \(64\) higher corrections for each canonical cubic. Over \(\mathbb F_4\), it performs \(160\) deterministic sampled original-matrix tests, using explicit extension-field arithmetic. It checks total polynomial coefficients sum to \(q^{32}\) for \(q=2,4,8\). Run `python3 check.py` from the extracted package directory; compare with `check_output.txt`. Finite checks corroborate, but do not establish, the all-field normal-form arguments.

For example, \(q=2\) yields coefficients at ranks \(0,1,2,4,6,8,10,12,16,32\), in that order, of
\[
1,\ 1,\ 62,\ 9920,\ 55552,\ 5079040,\ 5079040,\ 56885248,\ 2080374784,\ 2147483648.
\]

## Relationship to prior work
Moreno-Socías and Snellman (first public version 2000) study Hilbert series of **generic homogeneous** ideals in exterior and squarefree algebras, mainly in characteristic zero, including generic even-degree principal ideals. They do not furnish the finite-field census of all inhomogeneous principal multipliers or the cubic obstruction in this characteristic-two group algebra. Carlson, Friedlander and Pevtsova (2011) identify the same truncated-polynomial group algebras and analyze rank and radical varieties for modules restricted to linear shifted subgroups; their freeness criterion explains why nonzero linear parts have maximal square-zero multiplication rank, but does not count the higher-radical ranks. Lundqvist and Nicklasson (first public version 2016) classify Lefschetz behavior for powers of linear forms in monomial complete intersections, not all multiplication operators. Their 2018 work on generic principal ideals concerns homogeneous forms in the exterior algebra over the complex numbers, again a distinct counting question. The present result counts **all elements** with every possible rank and isolates the first cubic correction not determined by the lowest homogeneous piece. A yet-unidentified broader rank-enumeration theorem could still cover this result; historical priority is not independently established.

## Limitations
The complete finite-field formula is proved for exactly five generators and characteristic two. It does not enumerate the number of distinct principal ideals as opposed to the number of elements generating them; nor does it classify all ranks for larger elementary-abelian group algebras. The normal form and rank dichotomy hold over arbitrary characteristic-two fields, but the coefficient formula requires finite \(k\). No scheme-theoretic assertion or independent validation is made.

## References
1. G. Moreno-Socías and J. Snellman, *Some conjectures about the Hilbert series of generic ideals in the exterior algebra*, first public preprint 2000-07-14, arXiv:math/0007089, https://arxiv.org/abs/math/0007089.
2. J. F. Carlson, E. M. Friedlander and J. Pevtsova, *Representations of elementary abelian p-groups and bundles on Grassmannians*, first public preprint 2011-06-22, arXiv:1106.4474, https://arxiv.org/abs/1106.4474.
3. S. Lundqvist and L. Nicklasson, *On the structure of monomial complete intersections in positive characteristic*, first public preprint 2016-04-22, arXiv:1604.06820, https://arxiv.org/abs/1604.06820.
4. S. Lundqvist and L. Nicklasson, *On generic principal ideals in the exterior algebra*, first public preprint 2018-03-09, arXiv:1803.03563, https://arxiv.org/abs/1803.03563.
