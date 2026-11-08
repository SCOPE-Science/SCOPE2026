# Two-component commuting-involution geometry for a four-dimensional exterior algebra

## Finding
Let \(k\) be any field of characteristic two and let \(A=k[x,y]/(x^2,y^2)\). Write \(G\) for the smooth algebraic group of ordinary \(k\)-algebra automorphisms of \(A\), with the reduced algebraic-group structure specified in the proof. Let \(\mathcal X\) be the **reduced** variety of ordered pairs \((g,h)\in G^2\) satisfying \(g^2=h^2=1\) and \(gh=hg\); identity automorphisms are allowed.

**Theorem.** The group \(G\) is isomorphic over \(k\) to the affine group \(\operatorname{AGL}(2,k)\). Under this isomorphism, \(\mathcal X\) has exactly two geometrically irreducible components: a linear affine four-space \(T\), and a five-dimensional affine cone \(S\) over the smooth rational normal scroll of type \((2,2,1,1)\). The scroll cone has degree \(6\), is smooth away from its vertex, and has that vertex as its only singular point. Their intersection is the irreducible three-dimensional determinantal cone of rank-at-most-one \(2\)-by-\(2\) matrices. The reduced singular locus of \(\mathcal X\) is exactly \(T\cap S\). In particular \(\mathcal X\) is connected but non-equidimensional.

For every finite field \(\mathbb F_q\) of characteristic two,
\[
\#T(\mathbb F_q)=q^4,\qquad
\#S(\mathbb F_q)=q^5+q^4-q,\qquad
\#(T\cap S)(\mathbb F_q)=q^3+q^2-q,
\]
so the exact number of ordered commuting square-one automorphism pairs is
\[
\boxed{\#\mathcal X(\mathbb F_q)=q^5+2q^4-q^3-q^2.}
\]
The number of individual square-one automorphisms (including identity) is \(q^3+q^2-q\).

## Assumptions and scope
All assertions concern ordinary algebra automorphisms of the indicated unital commutative local algebra in characteristic \(2\); there is no assumption of algebraic closure except when geometric components are considered after extension. For a possibly nonperfect field, \(G\) is defined by the explicit smooth parametrization below, and \(\mathcal X\) is always the reduced support of the pair equations. No assertion is made about possible nilpotent infinitesimal directions in a larger automorphism functor or in the unreduced pair scheme. The ordered pair is allowed to contain identity.

## Proof
**1. Canonical affine-group identification.** Let \(V=kx\oplus ky\). The algebra has a vector-space decomposition
\[
A=k\oplus V\oplus\Lambda^2V,
\]
with multiplication of two elements of \(V\) given by their exterior product; because the characteristic is two, this agrees with ordinary multiplication in \(A\). The unique maximal ideal is \(V\oplus\Lambda^2V\). Every algebra automorphism preserves it and is uniquely given by an invertible linear map \(M\in\operatorname{GL}(V)\) and a linear map \(c:V\to\Lambda^2V\), acting as
\[
v\longmapsto Mv+c(v),\quad \omega\longmapsto\Lambda^2M(\omega).
\]
The canonical isomorphism \(V\simeq\operatorname{Hom}(V,\Lambda^2V)\), \(t\mapsto(v\mapsto t\wedge v)\), permits the unique notation \(c(v)=t\wedge Mv\). Composition then has the law
\[
(t,M)(s,N)=(t+Ms,MN).
\]
Thus the reduced automorphism group is \(V\rtimes\operatorname{GL}(V)=\operatorname{AGL}(V)\). In particular this is an algebraic, not just abstract finite-group, isomorphism.

**2. Equations.** Express the two affine transformations as \((a,I+N)\) and \((b,I+M)\), where \(a,b\in V\) and \(N,M\in\operatorname{End}(V)\). The square-one and commutation equations reduce exactly to
\[
N^2=M^2=0,\quad Na=Mb=0,\quad NM=MN,\quad Nb=Ma.
\]
Here invertibility of \(I+N\) and \(I+M\) is automatic. If a \(2\)-by-\(2\) square-zero endomorphism \(N\) is nonzero, it has rank one and its image and kernel are the same line \(L\). Its matrix centralizer is \(kI+kN\). A square-zero matrix in that centralizer is necessarily a scalar multiple of \(N\). Consequently, whenever at least one of \(N,M\) is nonzero, both are scalar multiples of the same rank-one nilpotent, and the vector equations force \(a,b\in L\). Conversely, any such quadruple satisfies all displayed equations. When \(N=M=0\), the vectors \(a,b\) are unrestricted.

**3. Irreducible components.** Let \(T\) be the locus \(N=M=0\); it is \(V^2\simeq\mathbb A^4\). Let \(S\) be the closed image of the incidence variety
\[
\{(L,N,M,a,b): L\in\mathbb P(V),\ N,M\in\operatorname{Hom}(V/L,L),\ a,b\in L\}.
\]
It is closed because projection from the product with \(\mathbb P(V)\) is proper. The incidence variety is the total space of
\[
\mathcal O_{\mathbb P^1}(-2)^{\oplus2}\oplus\mathcal O_{\mathbb P^1}(-1)^{\oplus2},
\]
which is irreducible of dimension \(1+4=5\). Every nonzero quadruple in \(S\) determines \(L\) uniquely: first from the image of a nonzero \(N\) or \(M\), and otherwise from a nonzero \(a\) or \(b\). The inverse \(L\)-map is regular on the standard open charts where one of these coordinates is nonzero. Accordingly \(S\setminus\{0\}\) is isomorphic to the incidence total space minus its zero section over the common vertex, and is smooth. Projectivizing the incidence gives the usual tautological embedding of \(\mathbb P(\mathcal O(-2)^2\oplus\mathcal O(-1)^2)\) as the smooth rational normal scroll \(S(2,2,1,1)\) in \(\mathbb P^9\). Its degree is the sum \(2+2+1+1=6\), and \(S\) is its affine cone. The cone is singular at the vertex since it has dimension five and its embedding span has dimension ten.

The classification in Step 2 gives \(\mathcal X=T\cup S\) on geometric points. Both are reduced closed subvarieties, and neither contains the other: \(S\) has points with nonzero \(N\), while \(T\) has pairs \((a,b)\) spanning \(V\). Hence these are exactly the two geometrically irreducible components. Their intersection is
\[
T\cap S=\{(a,b)\in V^2:\dim(ka+kb)\le1\}
=V(a_1b_2-a_2b_1)\subset\mathbb A^4.
\]
This is the irreducible rank-one determinantal cone of dimension three. Its singular point is the zero matrix. At every intersection point \(\mathcal X\) has distinct local branches, so is singular; outside the intersection it lies on just one smooth component. Therefore its reduced singular locus is precisely \(T\cap S\).

**4. Counting.** For \(k=\mathbb F_q\), the affine component has \(q^4\) points. The base \(\mathbb P^1\) has \(q+1\) points and each incidence fiber has \(q^4\) points. Every nonzero image point is represented by exactly one base line, while the zero quadruple is represented by all \(q+1\) lines. Hence \(\#S=(q+1)(q^4-1)+1=q^5+q^4-q\). The intersection consists of the zero pair and the \((q+1)(q^2-1)\) nonzero rank-one matrices \([a\ b]\), yielding \(q^3+q^2-q\) points. Inclusion-exclusion proves the formula. For an individual involution, either \(N=0\), giving \(q^2\) translations, or \(N\ne0\), giving \((q^2-1)q\) choices (\(q^2-1\) nonzero square-zero endomorphisms and \(q\) choices of \(a\in\ker N\)). This yields \(q^3+q^2-q\).

## Verification
The standalone code `verify_affine_involutions.py` enumerates the actual affine group law over \(\mathbb F_2,\mathbb F_4,\mathbb F_8\), tests square-one and commutation equations directly, and compares component and intersection counts. It returned:

```text
q=2: involutions=10, pairs=52, translation_component=16, scroll_component=46, intersection=10: PASS
q=4: involutions=76, pairs=1456, translation_component=256, scroll_component=1276, intersection=76: PASS
q=8: involutions=568, pairs=40384, translation_component=4096, scroll_component=36856, intersection=568: PASS
ALL_AFFINE_COMMUTING_INVOLUTION_CHECKS_PASS
```

An independent program `verify_exterior_automorphisms.py` evaluates automorphisms by the actual four-basis-element multiplication table, enumerates \(24\) automorphisms over \(\mathbb F_2\) and \(2880\) over \(\mathbb F_4\), and finds respectively \(52\) and \(1456\) commuting square-one pairs. Both programs use only the Python standard library. Enumeration proves only the listed finite cases; the general statement is proved by Steps 1–4.

## Relationship to prior work
Levy's original September 2006 preprint (`arXiv:math/0609180`) proves equidimensionality of the **unrestricted** restricted-nilpotent commuting variety in characteristic two. For matrices of size three, that ambient variety has equidimensional components of dimension six. The current object is the **affine-subgroup-constrained** intersection with the shape \(\left[\begin{smallmatrix}N&a\\0&0\end{smallmatrix}\right]\); equidimensionality of the unrestricted variety neither implies nor describes its non-equidimensional slice. Britnell–Wildon (`arXiv:1001.0811`) treat commutation of *similarity classes*, not dimensions and intersections of the affine subgroup's ordered square-one pair variety. Ngo (`arXiv:1209.1659`) studies commuting tuples in Lie algebras, with his principal \(2\)-by-\(2\) normality theorem stated for characteristic greater than two. Baek–Han (`arXiv:1610.07938`, original version October 25, 2016) classify distances in commuting-involution graphs of full linear groups, not the reduced pair variety of the affine subgroup. The classical semidirect-product law and determinantal-cone geometry are used rather than claimed as new. The combined two-component scroll/translation classification and corresponding exact point count are the present contribution; historical priority is provisional.

## Limitations
No claim is made about nilpotent embedded structures of the unreduced pair equation scheme or of a nonreduced automorphism functor, higher-dimensional affine groups, more than two commuting involutions, or complete conjugacy-orbit classifications. The geometry is for all fields of characteristic two; finite point counts are only for finite fields. Broader theorems on representation varieties of elementary abelian two-groups in parabolic subgroups may subsume the result and would need independent historical scrutiny.

## References
1. P. Levy, *Varieties of Modules for Z/2Z x Z/2Z*, first publicly posted 2006-09-06, arXiv:math/0609180, https://arxiv.org/abs/math/0609180.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, first publicly posted 2010-01-06, arXiv:1001.0811, https://arxiv.org/html/1001.0811v1.
3. N. V. Ngo, *Commuting varieties of r-tuples over Lie algebras*, first publicly posted 2012-09-07, arXiv:1209.1659, https://arxiv.org/abs/1209.1659.
4. S. Baek and C. Han, *Commuting involution graphs of linear groups*, first publicly posted 2016-10-25, arXiv:1610.07938, https://arxiv.org/html/1610.07938v2.
