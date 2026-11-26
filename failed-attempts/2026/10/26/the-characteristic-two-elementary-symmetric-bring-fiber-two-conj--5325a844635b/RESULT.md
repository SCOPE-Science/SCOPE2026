# The characteristic-two elementary-symmetric Bring fiber: two conjugate twisted cubics and five nodes

## Finding

Let \(e_j\) denote the \(j\)-th elementary symmetric polynomial in five homogeneous variables \(X_1,\ldots,X_5\). Define the projective curve
\[
B=V(e_1,e_2,e_3)\subset\mathbb P^4_{\mathbb F_2}.
\]
Over \(\mathbb F_4\), this curve is **exactly the reduced union of two smooth twisted cubics** \(C_1\cup C_2\). They are exchanged by arithmetic Frobenius and meet transversely at exactly five \(\mathbb F_2\)-rational points. These are all the geometric singularities of \(B\), each an ordinary node with two conjugate branches. The curve has degree six and arithmetic genus four, but is not geometrically integral.

For every integer \(n\ge1\), its number of rational points is
\[
\#B(\mathbb F_{2^n})=\begin{cases}
5,&n\text{ odd},\\
2^{n+1}-3,&n\text{ even}.
\end{cases}
\]
Its Hasse–Weil zeta function is
\[
Z(B/\mathbb F_2,T)=\frac{(1+T)^4}{(1-T)(1-4T^2)}.
\]
These assertions concern **the elementary-symmetric integral equations** and their characteristic-two fiber, not the literal reduction of the power-sum equations and not the stable reduction of an unspecified arithmetic model.

## Assumptions and scope

All schemes are projective over the stated field. Coordinates are homogeneous, and \(e_j=\sum_{1\le i_1<\cdots<i_j\le5}X_{i_1}\cdots X_{i_j}\) is interpreted over \(\mathbb F_2\). A twisted cubic means the degree-three rational normal curve in a projective three-space. \(\mathbb F_4\) is the unique quadratic extension of \(\mathbb F_2\). The theorem is a statement about every geometric point and every finite extension, not an extrapolation from the finite checks below.

In characteristic zero, Newton's identities identify \(e_1=e_2=e_3=0\) with the usual power-sum equations \(\sum_i X_i^j=0\) for \(j=1,2,3\) after inverting \(6\). This equivalence **does not survive** characteristic two: the second power sum is the square of the first. The choice of integral equations therefore matters.

## Proof

**1. The containing quadric and its rational points.** Put \(H=V(e_1)\cong\mathbb P^3_{\mathbb F_2}\) and \(Q=V(e_1,e_2)\subset H\). In characteristic two, on \(H\),
\[
\frac{\partial e_2}{\partial X_i}=e_1-X_i=X_i.
\]
A singular geometric point of \(Q\) would have \((X_i)_i\) proportional to the gradient \((1,1,1,1,1)\) of \(e_1\). Thus all coordinates would be equal. As \(e_1=5X_1=X_1\) in characteristic two, the only such vector is zero, not a projective point. Hence \(Q\) is a smooth quadric surface.

For \(X_i\in\mathbb F_2\), the condition \(e_1=0\) forces the number of nonzero coordinates to be two or four. At weight two, \(e_2=\binom22=1\); at weight four, \(e_2=\binom42=0\). Hence \(Q(\mathbb F_2)\) consists of precisely the five points whose homogeneous coordinates are four ones and one zero. There are five points rather than the nine points of a split smooth quadric over \(\mathbb F_2\); consequently \(Q\) is the nonsplit smooth quadric.

**2. All five rational points are singular on the cubic section.** On \(Q\),
\[
\frac{\partial e_3}{\partial X_i}=e_2-X_i(e_1-X_i)=X_i^2.
\]
At each of the five rational points, \(X_i^2=X_i\). Thus the differential of \(e_3\) is a scalar multiple of the differential of \(e_2\) modulo \(de_1\), so \(e_3|_Q\) vanishes to order at least two in the regular local ring at each such point. Moreover \(e_3=\binom43=0\) there. Therefore the divisor \(B\) on \(Q\) is singular at those five points.

**3. Two Frobenius graphs.** The nonsplit quadric \(Q\) is the quadratic-descent form of \(\mathbb P^1\times\mathbb P^1\). Because finite fields have trivial Brauer group, we may choose Segre coordinates \((u,v)\) over \(\mathbb F_4\) in which the nontrivial arithmetic descent sends
\[
(u,v)\longmapsto(v^2,u^2).
\]
In these coordinates the five \(\mathbb F_2\)-points are exactly \((u,u^2)\) for \(u\in\mathbb P^1(\mathbb F_4)\). Define
\[
C_1:\ v=u^2,\qquad C_2:\ u=v^2.
\]
The first graph is a divisor of bidegree \((2,1)\), the second has bidegree \((1,2)\). Both are smooth copies of \(\mathbb P^1\), and the Segre hyperplane bundle restricts to \(\mathcal O_{\mathbb P^1}(3)\); thus their images are twisted cubics. Arithmetic Frobenius exchanges them. The curves meet exactly at \(u^{4}=u\), namely the five \(\mathbb F_2\)-points. Their local equations have independent differentials \(dv\) and \(du\), including on the charts at infinity, so all five intersections are transverse.

**4. Exhaustion by intersection multiplicity.** The cubic section \(B\) is an effective divisor of bidegree \((3,3)\) on \(Q_{\mathbb F_4}\). If \(C_1\) were not a component, their total intersection length would be
\[
(3,3)\cdot(2,1)=3\cdot1+3\cdot2=9.
\]
But the cubic vanishes to order at least two at **each** of the five distinct points of \(C_1\cap C_2\), contributing intersection multiplicity at least ten: contradiction. Thus \(C_1\) is a component. Exchanging the rulings gives the same conclusion for \(C_2\). Since their bidegrees already add to \((3,3)\), the effective divisor is exactly \(C_1+C_2\) with multiplicity one and no residual part. This proves the complete geometric decomposition and that the singularities are precisely the five ordinary nodes.

**5. Genus and point counts.** The equations cut out a complete intersection of multidegree \((1,2,3)\) in \(\mathbb P^4\), hence degree six and arithmetic genus
\[
p_a(B)=1+\frac{1\cdot2\cdot3}{2}(1+2+3-5)=4.
\]
Equivalently, two rational components meeting transversely at five points give \(p_a=0+0+5-2+1=4\). If \(n\) is odd, Frobenius to the \(n\)-th power swaps the geometric components; every \(\mathbb F_{2^n}\)-point must lie on their intersection, and all five nodes are rational. If \(n\) is even, both components are defined over \(\mathbb F_{2^n}\), each contributes \(2^n+1\) points, and their five common rational points are counted once. This yields the stated point counts for all \(n\ge1\).

Finally, the same counts can be written uniformly as
\[
\#B(\mathbb F_{2^n})=1+2^n+(-2)^n-4(-1)^n.
\]
Using \(Z(T)=\exp(\sum_{n\ge1}\#B(\mathbb F_{2^n})T^n/n)\) gives the displayed zeta function.

## Verification

The standalone exact finite-field program `verify_counts.cpp` constructs \(\mathbb F_{2^n}\) as a polynomial quotient, generates the unique normalized representatives of \(\mathbb P^3(\mathbb F_{2^n})\), and evaluates the elementary symmetric equations directly for \(1\le n\le6\). Its observed counts are \(5,5,5,29,5,125\), exactly matching the theorem, and it reports `VERIFY_OK`. It is a computational cross-check, not a proof for unbounded \(n\). The uniform argument is Steps 1–5 above.

Compile and run on a C++17 implementation with `g++ -std=c++17 -O2 verify_counts.cpp -o verify_counts && ./verify_counts`.

## Relationship to prior work

Braden and Disney-Hogg, *Bring's curve: Old and New* (first public arXiv posting 2022-08-29), define the characteristic-zero curve by **power sums** and explicitly set aside extensions to positive characteristic (Introduction; §2, Definition 2.1). Their main smooth genus-four results therefore do not describe the chosen elementary-symmetric fiber at the bad prime two. Korchmáros, Lia and Timpanella, *A generalization of Bring's curve in any characteristic* (first public 2021-12-20), likewise study power-sum loci in characteristic \(p\ge7\), with \(m\le p-1\), not characteristic two. Both are source-context, not claims of this decomposition. The bidegree graph construction, complete singularity classification and point-count formula are the assessed additional assertions.

## Limitations

The result does not determine the stable reduction of Bring's curve over a specified discrete valuation ring, nor the special fibers obtained by reducing the literal power-sum model. It does not claim a classification of all possible integral forms. The five nodes are nonsplit over \(\mathbb F_2\); although the geometric components are rational over \(\mathbb F_4\), they are not separately defined over \(\mathbb F_2\). The novelty comparison cannot rule out every unindexed earlier computation. No independent external audit has been performed.

## References

1. H. W. Braden and L. Disney-Hogg, *Bring's curve: Old and New*, arXiv:2208.13692, initial posting 2022-08-29, https://arxiv.org/abs/2208.13692.
2. G. Korchmáros, S. Lia and M. Timpanella, *A generalization of Bring's curve in any characteristic*, arXiv:2112.10886, initial posting 2021-12-20, https://arxiv.org/abs/2112.10886.
