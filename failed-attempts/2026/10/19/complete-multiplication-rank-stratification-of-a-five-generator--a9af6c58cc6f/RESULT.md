# Complete multiplication-rank stratification of a five-generator elementary-abelian group algebra

## Finding

Let \(q=2^f\) with \(f\ge1\), let \(G=C_2^5\), and identify its group algebra with
\[
A=\mathbb F_q[G]\cong\mathbb F_q[z_1,\ldots,z_5]/(z_1^2,\ldots,z_5^2),
\qquad z_i=g_i-1.
\]
Write \(J=(z_1,\ldots,z_5)\) for the augmentation ideal and \(L_a:A\to A\) for multiplication by \(a\in J\). Every such operator satisfies \(L_a^2=0\).

Put
\[
\begin{aligned}
B_2(q)&=(q-1){5\brack2}_q,\\
B_4(q)&={5\brack1}_q q^2(q-1)(q^3-1),
\end{aligned}
\]
where \({n\brack r}_q=\prod_{i=0}^{r-1}(q^{n-i}-1)/(q^{r-i}-1)\). The complete rank enumerator is
\[
\boxed{\begin{aligned}
\mathcal H_q(T):=\sum_{a\in J}T^{\operatorname{rank}L_a}
={}&1+(q-1)T+q(q^5-1)T^2\\
&+q^6B_2(q)T^4+q^6B_4(q)T^6\\
&+q^{15}B_2(q)T^8+(q-1)q^{15}B_2(q)T^{10}\\
&+q^{16}B_4(q)T^{12}+(q^5-1)q^{26}T^{16}.
\end{aligned}}
\]
Consequently the attainable ranks are exactly \(0,1,2,4,6,8,10,12,16\). In particular rank \(10\), absent for homogeneous quadratic multiplication, appears precisely through a mixed quadratic–cubic interaction.

More precisely, write the unique homogeneous decomposition \(a=a_1+a_2+a_3+a_4+a_5\), with \(a_d\in\bigwedge^d V\) and \(V=\operatorname{span}(z_1,\ldots,z_5)\), using the characteristic-two identification of the squarefree algebra with its exterior algebra. Then the rank is determined by the *first nonzero homogeneous term*, except in the following single case: if \(a_1=0\) and the nonzero bivector \(a_2\) has alternating rank two, the operator rank is \(10\) when \(a_2\wedge a_3\ne0\), and \(8\) when \(a_2\wedge a_3=0\). If \(a_2\) has alternating rank four, the operator rank is \(12\), regardless of higher terms. With \(a_1=a_2=0\) and \(a_3\ne0\), the operator rank is \(2+\operatorname{rank}(\star a_3)\), where \(\star a_3\) denotes the alternating bilinear matrix obtained from the volume-form identification \(\bigwedge^3V\cong\bigwedge^2 V^*\).

For \(q=2\), in increasing rank order \(0,1,2,4,6,8,10,12,16\), the multiplicities are
\[
(1,1,62,9920,55552,5079040,5079040,56885248,2080374784),
\]
which sum to \(2^{31}\), the size of the augmentation ideal.

## Assumptions and scope

The base field must have characteristic two, but need not be prime. The group is exactly the elementary abelian group of rank five. The enumerated objects are *all individual elements of the augmentation ideal*, not only linear forms, not isomorphism classes, and not conjugacy orbits. The rank is the ordinary \(\mathbb F_q\)-linear rank of multiplication on the full \(32\)-dimensional regular module. No assertion is made for groups of other ranks or odd characteristic.

For a bivector \(Q\in\bigwedge^2V\), its alternating rank is the rank of the associated skew-symmetric coefficient matrix (alternating in every characteristic). For a trivector \(C\in\bigwedge^3 V\), the rank of \(\star C\) is basis independent. In characteristic two, \(\bigwedge V\) is commutative and every positive-degree element squares to zero.

## Proof

**1. Linear leading terms.** If \(a_1\ne0\), a linear change of variables followed by the substitution \(z_1\mapsto a\) defines an algebra automorphism: all images square to zero, and its induced map on \(J/J^2\) is invertible. Therefore \(L_a\) is similar to multiplication by \(z_1\), of rank \(16\). There are exactly \((q^5-1)q^{26}\) such elements.

**2. Rank-four quadratic term.** Suppose \(a_1=0\) and \(Q=a_2\) has alternating rank four. A linear coordinate change puts \(Q=z_1z_2+z_3z_4\). Every squarefree monomial of degree at least three contains one of \(z_1,\ldots,z_4\). The linear derivative terms from substituting \(z_1,\ldots,z_4\) by themselves plus homogeneous corrections of degree \(d-1\) span the entire degree-\(d\) space for \(d=3,4,5\), because the paired derivatives of \(Q\) are \(z_2,z_1,z_4,z_3\). Eliminating successively the terms of degrees three, four and five yields an algebra automorphism sending \(Q\) to \(a\). The degree-\(d\) step changes only degrees at least \(d\); terms in higher degrees are eliminated subsequently. Thus \(\operatorname{rank}L_a=\operatorname{rank}L_Q\). The maps from degrees \(0,1,2\) to degrees \(2,3,4\) in \(\bigwedge\langle z_1,\ldots,z_4\rangle\) have ranks \(1,4,1\), respectively; tensoring with \(\bigwedge\langle z_5\rangle\) gives rank \(12\) on \(A\).

**3. Rank-two quadratic term and the mixed invariant.** Now take \(Q=z_1z_2\), and write \(B=\mathbb F_q[z_3,z_4,z_5]/(z_3^2,z_4^2,z_5^2)\). Every \(a\) with quadratic term \(Q\) has a unique expression
\[
a=z_1z_2(1+R)+z_1P+z_2S+\gamma z_3z_4z_5,
\]
with \(R\in(z_3,z_4,z_5)B\) and \(P,S\in(z_3,z_4,z_5)^2B\). Multiplication by the unit \((1+R)^{-1}\) does not change \(\operatorname{rank}L_a\) and brings this to \(z_1z_2+z_1P'+z_2S'+\gamma z_3z_4z_5\). Because \(P'S'=0\) in the three-generator algebra \(B\), the substitution \(z_1\mapsto z_1+S'\), \(z_2\mapsto z_2+P'\) reduces the element to \(z_1z_2+\gamma z_3z_4z_5\). All substitutions are algebra automorphisms with identity linear part.

If \(\gamma=0\), multiplication by \(z_1z_2\) has rank \(2^{5-2}=8\). If \(\gamma\ne0\), the multiplication complex is the tensor product, over characteristic two, of the complexes \((\bigwedge\langle z_1,z_2\rangle,L_{z_1z_2})\) and \((\bigwedge\langle z_3,z_4,z_5\rangle,L_{\gamma z_3z_4z_5})\). Their homology dimensions are respectively \(2\) and \(6\). The Künneth formula over a field gives homology dimension \(12\) on \(A\), hence rank \((32-12)/2=10\). The scalar \(\gamma\) is nonzero precisely when \(Q\wedge a_3\ne0\). For each fixed rank-two \(Q\), the map \(a_3\mapsto Q\wedge a_3\in\bigwedge^5V\) is a nonzero linear functional on a \(10\)-dimensional space, so \(q^9\) cubic terms give rank eight and \((q-1)q^9\) give rank ten. The higher terms \(a_4,a_5\) contribute an independent factor \(q^6\).

**4. No quadratic term.** If \(a_1=a_2=0\) and \(C=a_3\ne0\), multiplication by \(a\) has image generated in distinct leading degrees by \(a\cdot1\) (degree three), \(C\wedge V\) (degree four), and \(C\wedge\bigwedge^2V\) (degree five). The last map is nonzero by perfect exterior duality, and the higher terms cannot increase these ranks. Thus its rank is \(2+\operatorname{rank}(C\wedge-:V\to\bigwedge^4V)\). Via a volume form, that rank is the alternating rank of \(\star C\), equal to two or four. If \(a_1=a_2=a_3=0\) and \(a_4\ne0\), multiplication has rank two; a nonzero pure top-degree element has rank one; zero has rank zero.

**5. Counts.** The numbers of alternating coefficient tensors of ranks two and four on a five-space are respectively
\[
B_2(q)={5\brack2}_q(q-1),\qquad
B_4(q)={5\brack1}_q\frac{|\operatorname{GL}_4(q)|}{|\operatorname{Sp}_4(q)|}
={5\brack1}_q q^2(q-1)(q^3-1).
\]
Indeed, choose the radical of codimension two or four and then a nondegenerate alternating form on the quotient. The same counts apply to cubic tensors via a volume form. Combining these with the free higher-degree coefficients in the preceding steps gives exactly the displayed enumerator. Evaluating at \(T=1\) gives \(q^{31}\), as required. Positivity of every coefficient proves that all nine stated ranks occur.

## Verification

The self-contained programs `verify.cpp` and `verify_gf4.py` implement exterior multiplication directly on the squarefree monomial basis rather than using the proof's normal-form reductions. Run `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify` and `python3 verify_gf4.py`. The first exhausts all \(2^{20}\) binary quadratic/cubic coefficient pairs with zero higher terms, then checks \(40,000\) complete binary examples and the global binary count. The second computes matrix ranks over the actual extension field \(\mathbb F_4\) for \(580\) independent prescribed and sampled cases. Both were successfully run on the packaged source before delivery. These checks are finite, not substitutes for the proof for arbitrary \(q\).

## Relationship to prior work

Carlson, Friedlander and Pevtsova study Jordan types and rank varieties of modules over elementary abelian group algebras, in particular restriction to cyclic shifted subgroups generated by elements independent modulo the square of the augmentation ideal. Their Proposition 1.1 accounts for the maximal-rank linear-leading-term stratum above. The present census treats all elements of the full augmentation ideal, especially those lying in its square. An earlier general calculation of multiplication ranks for *homogeneous bivectors* determines the quadratic-only ranks \(8\) and \(12\), but not the additional rank \(10\) produced by the mixed wedge invariant \(a_2\wedge a_3\), nor the cubic and higher strata and their exact finite-field populations. Erdmann and Holloway provide an earlier rank-variety setting for truncated polynomial algebras; a full-document comparison with that source remains a bibliographic limitation.

## Limitations

The theorem is a complete census only for the five-generator, characteristic-two regular module. It does not classify simultaneous multiplication by several elements, or arbitrary modules, and makes no claim of independent verification or absolute bibliographic priority. A result equivalent to this explicit finite-field stratification could exist in historical modular representation literature under different terminology. Calculations have been reproduced over \(\mathbb F_2\) and \(\mathbb F_4\), but the unrestricted quantifiers are justified by the proof rather than experiments.

## References

1. J. F. Carlson, E. M. Friedlander and J. Pevtsova, *Representations of elementary abelian p-groups and bundles on Grassmannians*, arXiv:1106.4474, first posted 2011-06-22; *Advances in Mathematics* **229** (2012), 2985–3051.
2. K. Erdmann and M. Holloway, *The Avrunin and Scott theorem and a truncated polynomial algebra*, *Journal of Algebra* **299** (2006), 344–373, doi:10.1016/j.jalgebra.2005.12.031, available online 2006-03-22.
3. A. Iarrobino, P. Macias Marques and C. McDaniel, *Artinian algebras and Jordan type*, arXiv:1802.07383, first posted 2018-02-21.
