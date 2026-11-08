# The finite-étale class and zeta function of maximal-flex tangent lines on Sziklai-optimal curves

## Finding
Let \(q\ge5\) be a prime power, \(k=\mathbb F_q\), \(d=q-1\), and \(\alpha,\beta,\gamma\in k^*\) with \(\alpha+\beta+\gamma=0\). Set
\[
C:\ \alpha X^d+\beta Y^d+\gamma Z^d=0,
\quad A=-\gamma/\alpha,\ B=-\gamma/\beta,\ D=-\beta/\alpha.
\]
Let \(T\) be the reduced union of all tangent lines with maximal contact order \(d\) at their points of tangency on \(C\). For \(v\in\{A,B,D\}\), put \(E_v=\operatorname{Spec}k[t]/(t^d-v)\), and write \(\mathbb L=[\mathbb A^1_k]\) in the Grothendieck ring \(K_0(\mathrm{Var}_k)\). Then \(T\) has exactly \(3d\) geometric line components and
\[
[T]=3+\mathbb L([E_A]+[E_B]+[E_D])-
\begin{cases}
[E_A\times E_B]+[E_A\times E_D]+[E_B\times E_D],&\operatorname{char}k\ne2,\\
2[E_A\times E_B],&\operatorname{char}k=2.
\end{cases}
\]
The geometric singularities are three ordinary \(d\)-fold vertices and \(3d^2\) distinct ordinary nodes when the characteristic is odd, or three ordinary \(d\)-fold vertices and \(d^2\) ordinary triple points in characteristic two. In particular, all singularities are accounted for.

For \(v\in\{A,B,D\}\), let \(r_v=\operatorname{ord}_{k^*}(v)\), and for integers \(n\ge1\), let \(e_v(n)=1\) when \(r_v\mid n\) and \(0\) otherwise. Put \(r_{vw}=\operatorname{lcm}(r_v,r_w)\) and \(R=\operatorname{lcm}(r_A,r_B,r_D)\). For \(Q=q^n\),
\[
\#T(\mathbb F_Q)=3+dQ\sum_v e_v(n)-
\begin{cases}
d^2\sum_{\{v,w\}}e_v(n)e_w(n),&\operatorname{char}k\ne2,\\
2d^2\,\mathbf 1_{R\mid n},&\operatorname{char}k=2.
\end{cases}
\]
The sum over unordered pairs contains the three pairs from \(\{A,B,D\}\). Therefore the complete Hasse–Weil zeta function is
\[
Z(T,t)=\frac{\displaystyle \prod_v(1-(qt)^{r_v})^{-d/r_v}}{(1-t)^3}
\begin{cases}
\displaystyle\prod_{\{v,w\}}(1-t^{r_{vw}})^{d^2/r_{vw}},&\operatorname{char}k\ne2,\\[1mm]
(1-t^R)^{2d^2/R},&\operatorname{char}k=2.
\end{cases}
\]
Every \(r_v\) and \(r_{vw}\) divides \(d\), so these exponents are integers. Each \(r_v>1\); consequently \(\#T(k)=3\) even though \(T\) has \(3d\) geometric lines. By Ferreira–Speziali's classification [1], this applies, up to \(k\)-projective equivalence, to every degree-\(q-1\) plane curve without a \(k\)-line component attaining the Sziklai point bound \((q-1)^2\).

## Assumptions and scope
The curve is smooth because \(p\nmid d\), the three coefficients are nonzero, and the partial derivatives have no common projective zero. An inflection tangent is counted as maximal only when its local intersection multiplicity with \(C\) is exactly \(d\); no characteristic-zero Hessian criterion is assumed, especially in characteristic two. The class is for the **reduced** tangent-line union, not the divisor \(C\cup T\) and not a set of only individually \(k\)-rational lines. The symbols \(E_v\) are finite étale schemes of degree \(d\). The formulas apply for every prime power \(q\ge5\) and extension degree \(n\ge1\).

## Proof
1. By the tangent-line formula for a smooth diagonal curve, if \(P=(0:y:z)\in C(\bar k)\), then \(y/z\) is a root of \(t^d=B\) and the tangent at \(P\) is \(Y=(y/z)Z\). Substitution into the equation of \(C\) leaves \(\alpha X^d\), so contact order is exactly \(d\). Similarly the two other coordinate-axis families are \(X=sZ\) with \(s^d=A\) and \(X=uY\) with \(u^d=D\). Their reduced union has explicit polynomial
\[
(\beta Y^d+\gamma Z^d)(\alpha X^d+\gamma Z^d)(\alpha X^d+\beta Y^d)=0.
\]
Its individual lines are distinct, because each parameter is nonzero and the families pass through three different coordinate vertices.

2. These are **all** maximal-order contact tangents, including in characteristic two. In characteristic \(p\), \(d=q-1\) has \(\binom{d}{j}=(-1)^j\) in \(k\) for all \(0\le j\le d\). Suppose a point \(P=(a:b:c)\) with \(abc\ne0\) has contact order \(d\) along its tangent. Pick a non-projectively-trivial direction \((u:v:w)\). Writing \(U=\alpha a^d\), \(V=\beta b^d\), \(W=\gamma c^d\) and \(s=u/a,t=v/b,h=w/c\), the constant, linear, and quadratic coefficients in \(F(P+\tau(u,v,w))\) give
\[
U+V+W=0,\quad Us+Vt+Wh=0,\quad Us^2+Vt^2+Wh^2=0.
\]
When \(s,t,h\) are all distinct, the Vandermonde determinant forces \(U=V=W=0\), impossible. When exactly two are equal, the first two equations force the remaining nonzero weight to vanish. Thus \(s=t=h\), a trivial projective direction, also impossible. Hence every maximal contact point lies on one coordinate axis, as in step 1. This proof does not invoke a Hessian, which can degenerate in characteristic two.

3. Each family is a pencil of \(d\) lines concurrent at a distinct \(k\)-rational coordinate vertex. Any two lines in different families meet once away from those vertices. The simultaneous three-family concurrence condition would be \(s=ut\). However
\[
A=(-B)D\quad\text{or equivalently}\quad BD=-A.
\]
In odd characteristic, \(s^d=A\) and \((ut)^d=BD=-A\) cannot coincide, so all \(3d^2\) cross-family intersections are distinct nodes. Their finite étale parameter schemes are \(E_A\times E_B\), \(E_A\times E_D\), and \(E_B\times E_D\). In characteristic two, \(-A=A\), and any intersection between two families lies on exactly one line of the third family. All \(d^2\) such points are ordinary triple points, parametrized by \(E_A\times E_B\). The coordinate vertices are never cross-family intersections and each carries \(d\) smooth transverse line branches.

4. The normalization of \(T\) is the disjoint union of three \(\mathbb P^1\)-bundles \(E_v\times\mathbb P^1\). To pass to \(T\) in \(K_0(\mathrm{Var}_k)\), replace each finite étale preimage \(E_v\) of its pencil vertex by one rational vertex, and replace each pair of branches above each ordinary node by one node; in characteristic two, replace each three branches above a triple point by one. Using the scissors relation yields
\[
[T]=(\mathbb L+1)\sum_v[E_v]-\sum_v[E_v]+3-
\begin{cases}\sum_{\{v,w\}}[E_v\times E_w],&p\ne2,\\2[E_A\times E_B],&p=2,\end{cases}
\]
which is precisely the stated class. Crucially, the vertex preimage \(E_v\) is not replaced by \(d\) independent \(k\)-rational points; its arithmetic twisting is retained.

5. If \(\theta^d=v\), then \(\theta^q=v\theta\), so \(\theta^{q^n}=v^n\theta\). Thus every root of \(E_v\) has Frobenius orbit of exactly \(r_v\), and each pair of roots from \(E_v\times E_w\) has orbit \(r_{vw}\). For each \(n\), \(\#E_v(\mathbb F_{q^n})=d\,e_v(n)\), and \(\#(E_v\times E_w)(\mathbb F_{q^n})=d^2e_v(n)e_w(n)\). Applying point-count realization to step 4 proves the point formula. Finally \(\exp(\sum_{m\ge1}a^{rm}t^{rm}/(rm))=(1-(at)^r)^{-1/r}\) gives the stated zeta factorization. Since \(v\ne1\) follows from \(\alpha+\beta+\gamma=0\) and nonzero coefficients, each \(r_v>1\), proving \(\#T(k)=3\).

## Verification
Run `python3 verify_tangent_union.py` using only the standard library. The checker independently constructs finite fields by irreducible polynomial arithmetic; for each tested normalized coefficient triple it counts projective \(\mathbb F_{q^n}\)-points of the displayed degree-\(3d\) polynomial directly and compares with the étale orbit formula. The all-triple census was replayed for \(q=5,7,8,9\) with \(n=2\), twelve sampled triples for \(q=11,13\) with \(n=2\), all triples for \(q=7\) with \(n=3\), and all triples for \(q=5,7,8,9\) with \(n=1\). It returned `VERIFY_HYPERFLEX_TANGENT_MOTIVE_OK`. The proof covers all \(q,n\); the finite tests do not substitute for the proof.

For instance, when \(q=7\), \((\alpha,\beta,\gamma)=(1,1,5)\) gives \((r_A,r_B,r_D)=(3,3,2)\). The count over \(\mathbb F_{7^3}\) is \(3+12\cdot7^3-36=4083\), because two entire pencils but not the third descend at extension degree three. In characteristic two, the same geometric cross-family locations collapse from three sets of nodes to one set of triple intersections.

## Relationship to prior work
Ferreira–Speziali [1] classify all Sziklai-optimal degree-\(q-1\) plane curves and thereby supply the natural source family. Dimca–Ilardi–Pokora–Sticlaru [2, Theorem 1.7] give the complex Fermat hyperflex tangent arrangement and use it to construct free divisors; its geometric polynomial and complex free exponents are prior knowledge. Moe–Toft [3, Sections 2.2 and 4.2] further describe complex Fermat inflection lines and intersections. Björner–Ekedahl [4] establish general combinatorial/cohomological methods for finite-field subspace-arrangement zeta functions. None of these sources is claimed to lack a method to derive arithmetic point counts; the contribution here is the **explicit finite-étale Grothendieck class, its characteristic-dependent rational incidence stratum, and the closed-form all-extension zeta in terms of the three coefficient-ratio orders** for this twisted Sziklai-optimal family. The known unweighted geometric line counts and characteristic-zero freeness statements are not presented as discoveries.

## Limitations
The class and zeta formulas apply only to the maximal-contact tangent-line union, not the full divisor obtained by adjoining the curve or coordinate axes. The smooth-curve classification requires \(q\ge5\), and the special uniform Frobenius root-cycle formula relies on \(d=q-1\). The results do not assert unknown automorphism groups or classification of arbitrary line arrangements. The geometric configuration itself is classical, and previously published general arrangement-zeta machinery may yield this exact formula after a short specialization; this is a genuine priority risk. Independent mathematical review has not been performed.

## References
[1] W. de Paula Ferreira and P. Speziali, *Optimal plane curves of degree \(q-1\) over a finite field*, arXiv:2211.14288v1, first public November 25, 2022. https://arxiv.org/html/2211.14288v1

[2] A. Dimca, G. Ilardi, P. Pokora, G. Sticlaru, *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117v1 (January 3, 2023), especially Theorem 1.7 (full accessible v4). https://arxiv.org/html/2301.01117v4

[3] T. K. Moe and N. P. A. Toft, *The Fermat curves, arrangements of lines, and intersections of osculating curves*, arXiv:2412.16993v1 (December 22, 2024). https://arxiv.org/html/2412.16993v2

[4] A. Björner and T. Ekedahl, *Subspace arrangements over finite fields: cohomological and enumerative aspects*, arXiv:math/9612217 (December 1996). https://arxiv.org/abs/math/9612217
