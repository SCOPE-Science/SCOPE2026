# Three irreducible components in the even Nijenhuis-operator locus of a four-dimensional perm superalgebra

## Finding

Let \(A=A_{\bar0}\oplus A_{\bar1}\) be the four-dimensional graded algebra specified below. The underlying reduced affine variety of **even Nijenhuis operators** is the union of precisely three geometrically irreducible, four-dimensional components, two affine spaces and one quadratic-cone product, with a common affine three-space as all their pairwise and triple intersections. Over every finite field \(\mathbb F_Q\), the number of even Nijenhuis operators is
\[
\#\operatorname{Nij}_{\bar0}(A)(\mathbb F_Q)=3Q^4-2Q^3,
\]
and exactly \(Q^2(Q-1)(3Q-4)\) of them are invertible. These are literal operators, not automorphism-conjugacy classes.

## Assumptions and scope

Let \(K\) be any field. The even basis is \(e_1,e_2\), the odd basis is \(f_1,f_2\), and the only nonzero basis products are \(e_1f_1=f_2\) and \(f_1f_1=e_2\). This is the perm superalgebra of Basdouri–Mosbahi–Zhang, Example 2.2. Triple products vanish. The even endomorphism \(N\), relative to the ordered basis \((e_1,e_2,f_1,f_2)\), has the coordinate matrix
\[
N=\begin{pmatrix}a&c&0&0\\b&d&0&0\\0&0&p&r\\0&0&u&s\end{pmatrix},\qquad a,b,c,d,p,r,u,s\in K.
\]
The defining Nijenhuis identity is \(N(x)N(y)+N^2(xy)=N(N(x)y+xN(y))\) for all homogeneous \(x,y\) and hence all \(x,y\) by bilinearity; it is the equation of Definition 2.4 in the motivating article. The polynomial classification also makes sense in characteristic two as a graded-algebra identity, without asserting any additional positive-characteristic superbialgebra results.

## Proof

**Exact equations.** Writing \(T_N(x,y)=N(x)N(y)+N^2(xy)-N(N(x)y+xN(y))\), bilinearity reduces the criterion to sixteen ordered basis pairs. Direct substitution of the two nonzero products gives the following necessary and sufficient system:
\[
r=0,\qquad (a-s)(p-s)=0,\qquad c(p-s)=0,\qquad c(a+d-2p)=0,\qquad bc+(d-p)^2=0.
\]
For complete traceability, before setting \(r=0\), the nonzero coefficient vectors of \(T_N\), in the basis order \((e_1,e_2,f_1,f_2)\), are:
\[
\begin{aligned}
T_N(e_1,f_1)&=(0,0,r(s-a),(a-s)(p-s)+ur),\\
T_N(e_1,f_2)&=(0,0,-r^2,r(a-s)),\\
T_N(e_2,f_1)&=(0,0,-cr,c(p-s)),\\
T_N(e_2,f_2)&=(0,0,0,cr),\\
T_N(f_1,f_1)&=(c(a+d-2p),bc+(d-p)^2,0,0),\\
T_N(f_1,f_2)&=T_N(f_2,f_1)=(-cr,r(p-d),0,0),\\
T_N(f_2,f_2)&=(0,r^2,0,0).
\end{aligned}
\]
All remaining basis-pair torsions vanish identically. Since \(K\) is a field, the last displayed row forces \(r=0\), after which exactly the five displayed scalar equations remain.

**Component decomposition.** Set
\[
\begin{aligned}
C_1&=\{r=c=0,\ d=p,\ a=s\},\\
C_2&=\{r=c=0,\ d=p,\ s=p\},\\
C_3&=\{r=0,\ s=p,\ a+d=2p,\ bc+(d-p)^2=0\}.
\end{aligned}
\]
If \(c=0\), the last equation forces \(d=p\), and the first product equation forces \(a=s\) or \(s=p\); these are \(C_1\) and \(C_2\). If \(c\ne0\), the middle equations force \(s=p\) and \(a+d=2p\); these give \(C_3\). Conversely, substitution shows every point of each \(C_i\) satisfies the equations. This proves the set-theoretic equality over every extension field, hence the equality of reduced algebraic sets.

Both \(C_1,C_2\) are affine four-spaces: their free coordinates are respectively \((b,u,p,s)\) and \((a,b,u,p)\). Write \(t=d-p\) on \(C_3\); then \(d=p+t\), \(a=p-t\), and \(C_3\) is isomorphic to
\[
\{(b,c,t):bc+t^2=0\}\times\mathbb A^2_{p,u}.
\]
The polynomial \(bc+t^2\), viewed as a primitive degree-one polynomial in \(b\) over \(K[c,t]\), is irreducible by Gauss's lemma because \(\gcd(c,t^2)=1\). The same argument holds over an algebraic closure. Thus \(C_3\) is geometrically irreducible of dimension \(4\). None of these components contains another, so the reduced variety has exactly these three irreducible components. All three pairwise intersections and their triple intersection are the same affine three-space
\[
L=\{r=c=0,\ a=d=p=s\},\qquad (b,u,p)\text{ free}.
\]

**Finite-field counts.** For \(K=\mathbb F_Q\), each \(C_i\) contains \(Q^4\) points. The affine cone \(bc+t^2=0\) has exactly \(Q^2\) points: for \(c\ne0\), there are \(Q(Q-1)\) solutions, and for \(c=0\), the equation gives \(t=0\) and any \(b\), yielding another \(Q\). All intersections contain \(Q^3\) points. Inclusion-exclusion gives \(3Q^4-2Q^3\).

The determinant is \((ad-bc)(ps-ru)\). On \(C_1\), \(C_2\), \(C_3\), it specializes respectively to \(a^2p^2\), \(ap^3\), \(p^4\). Thus invertible points number \(Q^2(Q-1)^2\), \(Q^2(Q-1)^2\), and \(Q^3(Q-1)\); each pairwise/triple intersection contributes \(Q^2(Q-1)\) invertible points. Inclusion-exclusion yields \(Q^2(Q-1)(3Q-4)\).

## Verification

A standalone Python 3 script, `verify.py`, implements the original multiplication and the Nijenhuis identity directly on all sixteen basis pairs; it checks the component formulas and invertibility without treating them as assumptions. Exhaustive enumeration covers all \(2^8\) and \(3^8\) even maps over \(\mathbb F_2,\mathbb F_3\), respectively. Over \(\mathbb F_5\) it enumerates all \(5^7\) candidates with \(r=0\), since \(r\ne0\) is excluded for every Nijenhuis operator by the proved \(r^2=0\) condition. The triples (tested, Nijenhuis, invertible) are \((256,32,8)\), \((6561,189,90)\), and \((78125,1625,1100)\), respectively. These finite checks corroborate, but do not replace, the all-field proof.

## Relationship to prior work

Basdouri, Mosbahi and Zhang [1, Example 2.2, Definition 2.4, Example 4.10 and Appendix B] provide this exact graded algebra and exhibit the two-parameter diagonal Nijenhuis family \(\operatorname{diag}(\mu,\nu,\nu,\mu)\), within a construction of perm superbialgebras. Remark 5.5 of [1] explicitly notes that its construction does not exhaust Nijenhuis operators. The above eight-coordinate classification, reduced geometric component decomposition, intersection structure and finite-field enumerations are not stated in [1]. The diagonal family is a strict slice of \(C_1\) (with \(b=u=c=r=0\)). Ma and Song [2] study ungraded Nijenhuis perm algebras, not the operator variety of this four-dimensional graded example. General Nijenhuis classifications on Lie, Hom-Lie, or other nonisomorphic algebras have different defining products and do not imply the five equations or three components by a known identification.

## Limitations

This result treats only **even** Nijenhuis operators on the single specified four-dimensional algebra, and classifies the **reduced** operator locus rather than the possibly nonreduced defining scheme. It does not classify odd operators, automorphism-conjugacy orbits, all four-dimensional perm superalgebras, or admissible Yang–Baxter tensors. The polynomial identity and its geometric/finite-field consequences extend to every field, but the source's additional super-bialgebra constructions assume characteristic zero. A literature search and comparison cannot rule out an unindexed earlier calculation of the same operator variety; independent mathematical audit has not occurred.

## References

[1] I. Basdouri, B. Mosbahi, Y. Zhang, *Admissible Yang–Baxter equation for Nijenhuis perm superalgebras*, arXiv:2611.17694v1, first public 2026-11-13. https://arxiv.org/html/2611.17694v1

[2] T. Ma, F. Song, *Admissible Yang–Baxter equation for Nijenhuis perm algebras*, arXiv:2410.07496v1, first public 2024-10-10. https://arxiv.org/abs/2410.07496
