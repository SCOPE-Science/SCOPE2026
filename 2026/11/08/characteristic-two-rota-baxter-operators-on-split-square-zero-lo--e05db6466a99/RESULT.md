# Characteristic-two Rota–Baxter operators on split square-zero local algebras: exact counts and conjugacy orbits

## Finding
Let \(k\) be a field of characteristic two, \(m\ge2\), and \(A_m=k\oplus V\) with \(\dim_kV=m\), \(V^2=0\), and multiplication \((a+u)(b+w)=ab+aw+bu\). Every weight-zero Rota–Baxter operator \(R:A_m\to A_m\) is uniquely of the form
\[
R(a+u)=av+Tu,\qquad v\in V,\quad T\in\operatorname{End}_k(V),\quad T^2=0.
\]
Conversely every such pair defines an operator. In particular \(R^3=0\) for all operators, whereas \(R^2\ne0\) exactly when \(Tv\ne0\). Index-three operators exist already for \(m=2\).

Over \(k=\mathbb F_q\) for every power \(q\) of two, the number of operators with \(\operatorname{rank}T=s\) is
\[
q^m C_{m,q}(s),\quad C_{m,q}(s)={m\brack s}_q{m-s\brack s}_q\prod_{i=0}^{s-1}(q^s-q^i),\quad 0\le s\le\lfloor m/2\rfloor.
\]
Here \({n\brack j}_q\) is the Gaussian coefficient and an empty product is one. The total number is \(q^m\sum_s C_{m,q}(s)\); exactly
\[
\sum_{s=1}^{\lfloor m/2\rfloor}C_{m,q}(s)(q^m-q^{m-s})
\]
of these have nilpotence index three. The zero operator is assigned index one; every other operator has index two or three.

Up to conjugation by algebra automorphisms, the operators form exactly \(2m+1\) classes when \(m\) is even, and \(2m\) classes when \(m\) is odd, over **every** characteristic-two field (finite or infinite).

## Assumptions and scope
An algebra automorphism is unital and \(k\)-linear. The Rota–Baxter identity of weight zero is \(R(x)R(y)=R(R(x)y+xR(y))\) for every \(x,y\in A_m\). We consider labeled operators for finite-field counts; conjugacy classes are counted separately. No grading condition is imposed. The automorphism group of \(A_m\) is \(\mathrm{GL}(V)\) acting trivially on the residue field and naturally on \(V\).

## Proof
**1. Scalar parts vanish.** Write an arbitrary linear operator as \(R(a+u)=\alpha a+f(u)+av+Tu\), where \(\alpha\in k\), \(f:V\to k\), \(v\in V\), and \(T:V\to V\). Apply the Rota–Baxter identity to \(x,y\in V\) and compare scalar parts: \(f(x)f(y)=2f(x)f(y)\). Hence \(f(x)^2=0\) for each \(x\), so \(f=0\). With \(x=y=1\), comparison of scalar parts gives \(\alpha^2=2\alpha^2\), hence \(\alpha=0\). Thus every operator has image in \(V\), without any characteristic restriction.

**2. The exact operator equation.** For \(x=a+u\), \(y=b+w\) and \(R(a+u)=av+Tu\), the product \(R(x)R(y)\) vanishes because \(V^2=0\), while
\[
R(R(x)y+xR(y))=2ab\,Tv+aT^2w+bT^2u.
\]
Taking \((a,b)=(1,0)\) and \((0,1)\), and then \((1,1)\), gives the necessary and sufficient conditions \(T^2=0\) and \(2Tv=0\). In characteristic two the second condition disappears. Since \(R^2(a+u)=aTv\), the nilpotence-index assertion follows, including the explicit example \(Te_1=e_2\), \(Te_2=0\), \(v=e_1\).

**3. Labeled finite-field counts.** For each rank \(s\) square-zero \(T\), choose \(U=\operatorname{im}T\) of dimension \(s\), choose \(K=\ker T\) of dimension \(m-s\) containing \(U\), and choose an isomorphism \(V/K\cong U\). These choices number \({m\brack s}_q\), \({m-s\brack s}_q\), and \(|\mathrm{GL}_s(q)|\), respectively. They recover \(T\) uniquely. There are independently \(q^m\) choices of \(v\). Since \(Tv=0\) exactly for the \(q^{m-s}\) vectors in \(K\), the index-three count follows. The index-two count is total minus index-three minus one.

**4. Conjugacy orbit classification.** The radical \(V\) is characteristic in \(A_m\), so \(\operatorname{Aut}_k(A_m)=\mathrm{GL}(V)\). Under \(g\in\mathrm{GL}(V)\), the parameter pair transforms to \((gTg^{-1},gv)\). For each rank \(s\), write \(V\) as a \(k[t]/(t^2)\)-module via \(t\cdot u=Tu\): it is \((k[t]/(t^2))^s\oplus k^{m-2s}\). Its module automorphism group acts transitively on each nonempty one of the four disjoint vector classes
\[
\{0\},\quad \operatorname{im}T\setminus\{0\},\quad \ker T\setminus\operatorname{im}T,\quad V\setminus\ker T.
\]
To verify transitivity, choose bases \(e_i,f_i,g_j\) with \(Te_i=f_i\) and \(Tf_i=Tg_j=0\). Elementary invertible transformations commuting with \(T\) include simultaneous changes in the \((e_i,f_i)\)-pairs, independent changes in the \(g_j\), additions of \(f_i\) to the \(g_j\), and additions of \(g_j,f_i\) to the \(e_i\) (with the corresponding images preserved). These normalize nonzero vectors in each class to \(f_1\), \(g_1\), or \(e_1\), respectively. Thus rank \(s=0\) contributes two orbits; every \(0<s<m/2\) contributes four; and when \(m\) is even the final rank \(s=m/2\) contributes three, since \(\ker T=\operatorname{im}T\). Summation gives \(2m\) for odd \(m\) and \(2m+1\) for even \(m\), with no field-size assumption.

## Verification
The attached `verify_rb_square_zero.py` reconstructs the original multiplication and checks the Rota–Baxter identity on all ordered basis pairs for **every** linear map in dimensions three and four over \(\mathbb F_2\), and dimension three over \(\mathbb F_3\). It checks the predicted parametrizations and count formulas, conjugation-orbit counts over \(\mathbb F_2\), and the rank distribution for four-dimensional \(V\). Output is in `check_output.txt`. Representative complete results are \(16\) operators and five orbits for \(m=2,q=2\), and \(176\) operators and six orbits for \(m=3,q=2\), with \(6\) and \(84\) operators of index three respectively. The computations do not prove infinite-field or all-dimension statements; those follow from the preceding algebraic argument.

## Relationship to prior work
Guo–Rosenkranz–Zheng (2014 preprint; 2015 publication) study weight-zero operators on the untruncated polynomial algebra, principally monomial and injective operators in characteristic zero. Farooq (2026, Theorem 3.4) studies the **same** split square-zero algebra in characteristic zero and shows weight-zero operators square to zero. That theorem is acknowledged as the closest comparison, not presented as a new result here: its characteristic assumption excludes the present family, and the explicit characteristic-two operator of index three disproves a naive characteristic-free extension. The present finite-field census and complete automorphism-orbit classification are not stated in that work. Benito–Gubarev–Pozhidaev (2018) concern quadratic division, matrix and other algebras, not this commutative square-zero local family. Classical classification of square-zero endomorphisms is used rather than claimed new.

## Limitations
The result concerns weight-zero operators on \(k\oplus V\), not operators of nonzero weight, higher-order nilpotent radicals, deformations, or classification of Rota–Baxter algebra isomorphism types beyond conjugation by automorphisms of the fixed underlying algebra. The reduced orbit counts do not determine nonreduced scheme structure. Complete historical-priority verification and independent mathematical validation remain outstanding.

## References
1. L. Guo, M. Rosenkranz and S. Zheng, *Rota-Baxter operators on the polynomial algebras, integration and averaging operators*, arXiv:1407.5306, first posted 2014-07-20; *Pacific Journal of Mathematics* 275 (2015), 481–507. https://arxiv.org/abs/1407.5306
2. A. Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1, posted 2026-05-15, Theorem 3.4 and Section 3.1. https://arxiv.org/abs/2605.15670
3. P. Benito, V. Gubarev and A. Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras*, *Mediterranean Journal of Mathematics* 15 (2018), article 189. https://doi.org/10.1007/s00009-018-1234-5
