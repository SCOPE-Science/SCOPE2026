# Quadratic Galois descent in a three-dimensional pre-Lie Nijenhuis locus

## Finding

Let \(k=\mathbb F_q\), let \(V=k^2\), and let \(T\in\operatorname{GL}(V)\) have irreducible quadratic characteristic polynomial. On the three-dimensional, **nonassociative** left-symmetric (pre-Lie) algebra \(A_T=kt\oplus V\), define
\[
(at+u)\cdot(bt+v)=aTv\qquad(a,b\in k,\ u,v\in V).
\]
A linear map \(N:A_T\to A_T\) is Nijenhuis, in the pre-Lie sense, if and only if it belongs to the union of the following two linear families:
\[
\mathcal U=\{N(t)=at+u,\quad N|_V=aI_V:a\in k,\ u\in V\},
\]
\[
\mathcal C=\{N(t)=at,\quad N|_V=aI_V+B:a\in k,\ B\in k[T]\}.
\]
Their intersection is precisely the scalar line \(\{aI_{A_T}:a\in k\}\). In particular,
\[
\boxed{|\operatorname{Nij}(A_T)(\mathbb F_q)|=2q^3-q},
\quad\boxed{P_{\mathrm{rank}}(z)=1+(q^2+q-2)z+(q^2-1)z^2+2(q-1)(q^2-1)z^3}.
\]

Although the rational point set comprises these two affine three-spaces, the **geometric reduced solution variety** over an algebraic closure has exactly **four** irreducible affine-linear components: two of dimension four and two of dimension three. Frobenius interchanges the two four-dimensional components, while fixing the other two. In particular, the rational classification is not a geometric component classification.

More precisely, for \(s\ge1\), write \(Q=q^s\). The exact point count over \(\mathbb F_{q^s}\) is
\[
\boxed{M_s=\begin{cases}
2Q^3-Q,&s\text{ odd},\\
Q(2Q^3+2Q^2-4Q+1),&s\text{ even}.
\end{cases}}
\]
Thus the reduced Hasse--Weil zeta function is
\[
\boxed{Z_{A_T}(z)=\exp\!\left(\sum_{s\ge1}\frac{M_s}{s}z^s\right)=
\frac{(1-q^4z^2)^2}{(1-q^3z)^2(1-q^8z^2)(1+qz)}.}
\]

For comparison, if \(T\) instead has two distinct nonzero eigenvalues in \(\mathbb F_q\), its full Nijenhuis locus has
\[
\boxed{q(2q^3+2q^2-4q+1)}
\]
points with complete linear-rank polynomial
\[
\boxed{1+(q-1)(5q+2)z+(q-1)(4q^2+q-5)z^2
+2(q-1)(q^3-3q+2)z^3.}
\]

## Assumptions and scope

The irreducible assertion holds for every prime power \(q\), including characteristic two; no characteristic-zero or algebraic-closedness assumption is made. Irreducibility here refers to the degree-two characteristic polynomial of \(T\) over \(k\). Such a matrix exists over every finite field, with \(k[T]\cong\mathbb F_{q^2}\). The split comparison requires two *distinct nonzero* eigenvalues, hence exists for \(q\ge3\). The stated geometric component result refers to the reduced variety of solutions of the defining polynomial identities, not to possible nilpotent structure in the nonreduced operator scheme.

The multiplication is pre-Lie because all its left multiplications are scalar multiples of \(T\) on \(V\), while commutators lie in \(V\) and act by zero on the left. It is nonassociative: \(t\cdot(t\cdot v)=T^2v\ne0\) for \(v\ne0\), whereas \((t\cdot t)\cdot v=0\).

Nijenhuis means the original bilinear identity, for *all* \(x,y\in A_T\):
\[
N(x)\cdot N(y)=N\big(N(x)\cdot y+x\cdot N(y)-N(x\cdot y)\big).
\]
Counts are of labeled linear operators, not conjugacy classes. The primary subject is nonassociative (pre-Lie) operator classification; it does not assert the same census for the sub-adjacent Lie algebra or for general three-dimensional pre-Lie algebras.

## Proof

**Step 1: eliminate nonideal-preserving maps.** Write \(N(t)=at+u\) and \(N(v)=f(v)t+Sv\), with \(f\in V^*\). The identity on \((v,w)\in V^2\) is
\[
f(v)TSw=f(v)\big(f(Tw)t+STw\big).
\]
If \(f\ne0\), choose \(v\) with \(f(v)\ne0\); then \(f\circ T=0\), contradicting invertibility of \(T\). Hence \(f=0\), so every Nijenhuis operator preserves \(V\).

**Step 2: a necessary and sufficient matrix criterion.** With \(f=0\), evaluate the defining identity on \((t,t)\) and \((t,w)\). The only constraints are
\[
(S-aI)Tu=0,\qquad (S-aI)[T,S]=0.
\]
For \(B=S-aI\), equivalently
\[
\boxed{BTu=0,\qquad B[T,B]=0.}\tag{1}
\]
The pairs \((v,t)\) and \((v,w)\) then contribute zero. Since the identity is bilinear, these four basis-pair types give both necessity and sufficiency.

**Step 3: irreducible quadratic descent.** If \(B\) is a nonzero singular \(2\times2\) matrix, it has rank one: \(B=v\otimes\varphi\). Expanding the second equation of (1) gives
\[
\varphi(Tv)\varphi-\varphi(v)(\varphi\circ T)=0.
\]
If \(\varphi(v)=0\), then \(\varphi(Tv)=0\), forcing \(\varphi=0\) because \(v,Tv\) are linearly independent by irreducibility. If \(\varphi(v)\ne0\), then \(\varphi\circ T\) is a scalar multiple of \(\varphi\), a forbidden rational left eigenvector. Both contradict rank one. Therefore \(B=0\) or \(B\) is invertible. In the latter case, (1) forces \([T,B]=0\) and \(u=0\); conversely each nonzero element of \(k[T]\) is invertible, and any \(B\in k[T]\) with \(u=0\) satisfies (1). This proves the exact two-family parametrization and their intersection.

Counting \(|\mathcal U|=|\mathcal C|=q^3\) and \(|\mathcal U\cap\mathcal C|=q\) gives \(2q^3-q\). For ranks, in \(\mathcal U\), \(a=0\) gives one zero and \(q^2-1\) rank-one maps, while \(a\ne0\) gives \((q-1)q^2\) invertibles. In \(\mathcal C\setminus\mathcal U\), \(a=0,B\ne0\) gives \(q^2-1\) rank-two maps; \(a\ne0,B=-aI\) gives \(q-1\) rank-one maps; all remaining \((q-1)(q^2-2)\) maps are invertible. Adding yields the stated rank polynomial.

**Step 4: geometry after splitting.** Over a splitting field choose eigenbasis \(T=\operatorname{diag}(\lambda,\mu)\), with \(\lambda\mu(\lambda-\mu)\ne0\), and put
\[
B=\begin{pmatrix}p&r\\s&h\end{pmatrix},\qquad u=\begin{pmatrix}x\\y\end{pmatrix}.
\]
Equation (1) is equivalent to
\[
rs=pr=hs=0,\qquad p\lambda x+r\mu y=0,\qquad s\lambda x+h\mu y=0.\tag{2}
\]
It follows by considering \(r\ne0\), \(s\ne0\), and \(r=s=0\) that its full zero set (with \(a\) free) is precisely the union of the following four distinct linear affine spaces:
\[
\begin{array}{ll}
\mathcal X_0:&B=0,\ a,x,y\text{ free}\quad(\dim=3),\\
\mathcal X_c:&r=s=0,\ x=y=0,\ a,p,h\text{ free}\quad(\dim=3),\\
\mathcal X_+:&p=s=y=0,\ a,r,h,x\text{ free}\quad(\dim=4),\\
\mathcal X_-:&r=h=x=0,\ a,p,s,y\text{ free}\quad(\dim=4).
\end{array}
\]
None is contained in the union of the others, so these are exactly the irreducible components of the *reduced* geometric variety. For irreducible \(T\), its two eigenlines are exchanged by \(q\)-Frobenius; thus \(\mathcal X_+\) and \(\mathcal X_-\) are exchanged while \(\mathcal X_0,\mathcal X_c\) descend.

**Step 5: split and extension-field point counts.** Over a field of size \(Q\) in which the two eigenvalues lie, fix \(a\). In (2), the choices split disjointly into: \(B=0\), with \(Q^2\) choices of \(u\); nonzero diagonal \(B\) with both entries nonzero, \((Q-1)^2\) choices; diagonal \(B\) with exactly one nonzero entry, \(2Q(Q-1)\) choices including the free \(u\)-coordinate; and nonzero upper or lower offdiagonal \(B\), with \(2Q^2(Q-1)\) choices including the remaining free \(u\)-coordinate. Hence
\[
Q\big(Q^2+(Q-1)^2+2Q(Q-1)+2Q^2(Q-1)\big)
=Q(2Q^3+2Q^2-4Q+1).
\]
Splitting according to \(a=0\) or \(a\ne0\) and the rank of \(aI+B\) gives, respectively, rank zero \(1\), rank one \((Q-1)(5Q+2)\), rank two \((Q-1)(4Q^2+Q-5)\), and rank three \(2(Q-1)(Q^3-3Q+2)\). For a fuller count, the rank-three stratum has \(a\ne0\) and \(aI+B\) invertible and contributes
\[
(Q-1)[Q^2+(Q-2)^2+2Q(Q-2)+2Q(Q-1)^2].
\]
The rank-two stratum has \((Q-1)(2Q^2+2Q-4)\) maps with \(a\ne0\), and \((Q-1)^2(2Q+1)\) maps with \(a=0\). The rank-one coefficient follows by subtracting these and the zero map from the total, establishing the displayed polynomial without interpolation.

A separable quadratic irreducible polynomial over \(\mathbb F_q\) splits in \(\mathbb F_{q^s}\) precisely when \(s\) is even. Applying the appropriate case with \(Q=q^s\) gives \(M_s\). Finally expand logarithms of \((1-az)^{-1}\) and \((1+az)^{-1}\). The coefficient of \(z^s/s\) in the logarithm of the asserted rational zeta function equals \(M_s\) for odd and even \(s\), proving the identity.

## Verification

The standalone C++17 checker `verify_quadratic_prelie.cpp` enumerates **all** \(3\times3\) matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) with the indicated irreducible companion actions, and all matrices for split-distinct actions over \(\mathbb F_3,\mathbb F_5\). On each matrix it independently evaluates the defining pre-Lie Nijenhuis identity on all nine ordered basis pairs, compares it with (1) and with the four component conditions, computes the linear rank, and checks the proposed totals. Results:

| Field | Quadratic action | Rank counts \((0,1,2,3)\) | Total |
|---|---|---|---|
| \(\mathbb F_2\) | irreducible | \((1,4,3,6)\) | 14 |
| \(\mathbb F_3\) | irreducible | \((1,10,8,32)\) | 51 |
| \(\mathbb F_3\) | split distinct | \((1,34,68,80)\) | 183 |
| \(\mathbb F_5\) | irreducible | \((1,28,24,192)\) | 245 |
| \(\mathbb F_5\) | split distinct | \((1,108,400,896)\) | 1405 |

Compile and run with `g++ -O2 -std=c++17 verify_quadratic_prelie.cpp -o verify_quadratic_prelie && ./verify_quadratic_prelie`. The expected final line is `QUADRATIC_PRELIE_NIJENHUIS_VERIFIED`. The separate `verify_zeta.py` uses exact integer polynomial arithmetic to test the first six logarithmic coefficients at several field sizes. Finite checks support the proof but do not establish the all-field geometric or point-count claims.

## Relationship to prior work

Wang--Bai--Liu--Sheng (arXiv:1710.03749, 2017) defines Nijenhuis operators on pre-Lie algebras and gives general constructions and two-dimensional Burgers examples. Gao--Kang--Lü--Yu (arXiv:2308.12121, first public 2023-08-23) treats two-dimensional complex pre-Lie algebras and three-dimensional *associative* algebras, not the present three-dimensional nonassociative family. The 2026 journal revision has the same stated classification scope.

A prior rank-at-most-one scalar-deviation analysis for the **same bilinear product**, interpreted as a left Leibniz algebra, already derives the universal equations in (1) and classifies the stratum \(\operatorname{rank}B\le1\). For an irreducible quadratic action that stratum is exactly \(B=0\), so the rational family \(\mathcal U\) and equation (1) are preexisting coverage rather than independent new contributions. This theorem treats the unrestricted operator locus, in particular the invertible-\(B\) branch \(B\in k[T]^\times\), and establishes the geometric and arithmetic consequences not implied by that restricted-rank theorem.

Two relevant earlier finite-field findings study quadratic splitting of the **two-dimensional** Burgers pre-Lie Nijenhuis locus and two-dimensional automorphism-orbit coincidences. Their result statements and proofs have been compared; neither includes the present algebra with a two-dimensional derived ideal and irreducible action, its four-component geometry, or these extension-field point counts. The underlying philosophy of Galois descent is not claimed as new; the evaluated result is the concrete complete three-dimensional nonassociative classification and its arithmetic-geometric consequences.

## Limitations

No automorphism-conjugacy classification is asserted. No classification is given for nonseparable repeated-eigenvalue actions or noninvertible \(T\). Geometric statements concern the reduced solution variety. The rational decompositions into affine spaces do not imply the original scheme is reduced, and the finite-field experiment is not a substitute for the proof. Searches and inspected publications cannot establish absolute novelty; an unlocated general theorem or another pre-Lie classification may imply the same result. Independent external mathematical review remains unperformed.

## References

1. X. Gao, C. Kang, J. Lü, S. Yu, "Nijenhuis operators on low dimensional pre-Lie algebras and solutions of CYBE", arXiv:2308.12121v1, public 2023-08-23, https://arxiv.org/abs/2308.12121.
2. Q. Wang, C. Bai, J. Liu, Y. Sheng, "Nijenhuis operators on pre-Lie algebras", arXiv:1710.03749v1, public 2017-10-09, https://arxiv.org/abs/1710.03749.
3. X. Zou, X. Gao, C. Kang, J. Lü, "Nijenhuis Operators on 2D Pre-Lie Algebras and 3D Associative Algebras", Axioms 15 (2026), 80, https://doi.org/10.3390/axioms15010080.
4. "Arithmetic splitting of the Burgers pre-Lie Nijenhuis locus", 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-arithmetic-splitting-of-the-burgers-pre-lie-nijenhuis-locus--084219c5b8b0.
5. "Two distinct pre-Lie algebras have the same Nijenhuis orbit space", 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-two-distinct-pre-lie-algebras-have-the-same-nijenhuis-orbit-spac--228605f3382a.
