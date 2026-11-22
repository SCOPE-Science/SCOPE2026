# Two-sided averaging projections on nonsymmetric bilinear-product algebras: an exact rank census

## Finding
Let \(q\) be a prime power, \(k=\mathbb F_q\), \(n\ge2\), and \(a\in k^\times\) satisfy \(a^2\ne1\). On the nonunital associative algebra
\[
 A_{n,a}=k^n\oplus k^n\oplus kz,\qquad
 (x,y,s)(x',y',s')=(0,0,x\cdot y'+a\,y\cdot x'),
\]
count all **two-sided averaging projections**: linear maps \(P:A_{n,a}\to A_{n,a}\) satisfying
\[
 P^2=P,\qquad P(u)P(v)=P(P(u)v)=P(uP(v))
 \quad\text{for every }u,v\in A_{n,a}.
\]
Their complete linear-rank polynomial is
\[
 \boxed{\mathcal A_{n,q}(T)=
 \sum_{r=0}^{n}I_{n,r}(q)q^{r(2n-r+1)}T^r
 +\sum_{j=0}^{n}{n\brack j}_q q^{j(n-j)+2(n-j)}T^{2j+1}.}
\]
Here \({m\brack r}_q=\prod_{i=0}^{r-1}(q^{m-i}-1)/(q^{r-i}-1)\), with value zero if \(r\notin\{0,\dots,m\}\); \(g_d(q)=\prod_{i=0}^{d-1}(q^d-q^i)\), with \(g_0(q)=1\); and
\[
 I_{n,r}(q)=\sum_{\substack{0\le s\le n,\ 0\le t\le n-s\\
 0\le d=s+t-r\le\min(s,t)}}
 {n\brack s}_q{n-s\brack t}_q
 {s\brack d}_q{t\brack d}_q g_d(q).
\]
The rank support is **exactly**
\[
 \{0,1,\ldots,n\}\ \cup\ \{1,3,5,\ldots,2n+1\}.
\]
The first sum is the **already established retraction contribution** for this same algebra, together with all projections killing the socle. The new contribution is the second sum, classifying the socle-fixing averaging projections. In particular, all the nonidentity operators in that branch have odd rank, and no even rank strictly larger than \(n\) occurs. At \(q=5\), \(n=2\), \(a=2\), the polynomial is
\[
 1+23125T+125000T^2+750T^3+T^5.
\]
Thus there are exactly \(750\) rank-three averaging projections, none of which are algebra endomorphisms, and no rank-four ones. The retraction polynomial for this example, previously established, is \(1+22500T+125000T^2+T^5\).

## Assumptions and scope
The coefficient \(a\) is a fixed nonzero field element with \(a^2\ne1\); this condition excludes \(q=2\) and \(q=3\), but is attainable for other finite fields, including characteristic two. The algebra is associative because every triple product vanishes; it is noncommutative under this assumption. All maps are labeled \(k\)-linear operators, and rank means linear rank on the full \((2n+1)\)-dimensional space. The averaging identity is **two-sided**; classifying only left averaging operators would be a different problem. A projection need not be an algebra endomorphism.

## Proof
Write \(V=k^n\oplus k^n\), and set \(B((x,y),(x',y'))=x\cdot y'+a\,y\cdot x'\); this pairing is nondegenerate. The multiplication is \((v+sz)(w+tz)=B(v,w)z\) and \(zA_{n,a}=A_{n,a}z=0\).

**1. The socle line is preserved.** For a two-sided averaging projection \(P\), write \(P(z)=h+bz\) for \(h\in V\). The identity \(P(P(z)v)=P(z)P(v)\) and \(P(zP(v))=P(z)P(v)\) imply \(P(P(z)v)=0\) for every \(v\in V\). But \(P(z)v=B(h,v)z\), so \(B(h,v)P(z)=0\) for every \(v\). If \(P(z)\ne0\), nondegeneracy forces \(h=0\); if \(P(z)=0\) this holds already. Consequently \(P(z)=bz\) and idempotence gives \(b^2=b\), i.e. \(b\in\{0,1\}\).

**2. Socle-killing family.** If \(P(z)=0\), write \(P(v)=Qv+f(v)z\). Idempotence is equivalent to \(Q^2=Q\) and \(fQ=f\), while the two-sided averaging identity is equivalent to \(B(Qv,Qw)=0\) for all \(v,w\). Thus \(U=\operatorname{im}Q\) is a totally \(B\)-isotropic subspace, \(Q\) is any projection onto \(U\), and \(f\) is an arbitrary functional on \(U\) pulled back through \(Q\). For each such \(r\)-space \(U\), there are \(q^{r(2n-r)}\) complementary kernels and \(q^r\) functionals; hence the contribution is \(I_{n,r}(q)q^{r(2n-r+1)}\). Every such projection also preserves multiplication and is a retraction. This entire first polynomial summand is known from the earlier retraction census; its derivation is supplied to make the proof self-contained, not asserted as original.

To evaluate \(I_{n,r}(q)\), let \(X,Y\le k^n\) be the coordinate images of \(U\). For \(u=(x,y),v=(x',y')\in U\), put \(c=x\cdot y'\), \(d=x'\cdot y\). Both \(B(u,v)=c+ad\) and \(B(v,u)=d+ac\) vanish; since \(1-a^2\ne0\), we get \(c=d=0\), hence \(X\perp Y\). Conversely a subdirect subspace \(U\le X\oplus Y\) is totally isotropic when \(X\perp Y\). If \(\dim X=s\), \(\dim Y=t\), and \(\dim U=r\), the vector-space Goursat description uses an isomorphism between two \(d=s+t-r\)-dimensional quotients. There are \({n\brack s}_q{n-s\brack t}_q\) orthogonal choices of \((X,Y)\) and \({s\brack d}_q{t\brack d}_q g_d(q)\) such subdirect subspaces. This proves the formula and the upper bound \(r\le n\). The positive counts for every \(0\le r\le n\) follow by taking \(U\) in the first coordinate summand.

**3. Socle-fixing family (new census).** If \(P(z)=z\), again write \(P(v)=Qv+f(v)z\). Idempotence is equivalent to \(Q^2=Q\), \(fQ=0\). The three expressions of the averaging identity are, respectively, \(B(Qv,Qw)z\), \(B(Qv,w)z\), and \(B(v,Qw)z\). Therefore, using idempotence, averaging is equivalent to \(Q\) being self-adjoint for the bilinear form \(B\), i.e.
\[
 B(Qv,w)=B(v,Qw)\quad\text{for every }v,w\in V.
\]
In the coordinate splitting \(V=k^n\oplus k^n\), the Gram matrix is
\[
 M=\begin{pmatrix}0&I\\aI&0\end{pmatrix}.
\]
Write \(Q=\begin{psmallmatrix} A&C\\D&E\end{psmallmatrix}\). The equation \(Q^{\mathsf T}M=MQ\), together with \(a^2\ne1\), forces \(C=D=0\) and \(E=A^{\mathsf T}\). The idempotence of \(Q\) is exactly \(A^2=A\). Thus every socle-fixing averaging projection is uniquely specified by
\[
 Q=\operatorname{diag}(A,A^{\mathsf T}),\qquad A^2=A,
 \qquad fQ=0.
\]
If \(\operatorname{rank}A=j\), then \(\operatorname{rank}Q=2j\), the linear rank of \(P\) is \(2j+1\), and \(\dim\ker Q=2(n-j)\). The number of rank-\(j\) idempotents on \(k^n\) equals \({n\brack j}_q q^{j(n-j)}\): select their image and complementary kernel. For each such \(A\), the functionals \(f\) with \(fQ=0\) number \(q^{2(n-j)}\). This establishes the second sum. Every listed count is positive. The branches are disjoint since their actions on \(z\) differ, completing the proof of both the polynomial and exact rank support.

**4. Relation to retractions.** An algebra endomorphism with \(P(z)=z\) must have \(B(Qv,Qw)=B(v,w)\) for all \(v,w\). Since \(Q\) is self-adjoint idempotent and \(B\) is nondegenerate, this forces \(Q=I\), then \(f=0\). Thus within the new socle-fixing family only the identity is also an endomorphism. The other \(\sum_{j=0}^{n-1}{n\brack j}_q q^{j(n-j)+2(n-j)}\) operators are genuinely averaging projections but not retractions.

## Verification
The standalone scripts `verify_counts.py` (Python standard library) and `exhaust.cpp` (C++17) supply independent checks. `verify_counts.py` enumerates reduced-row-echelon subspaces, tests the two-sided isotropy equations directly for \((q,n,a)=(5,1,2),(5,2,2),(7,1,2)\), and compares their counts with the Goursat sum. It independently enumerates idempotent two-by-two matrices at \(q=5\), giving rank frequencies \((1,30,1)\), and checks the complete rank formula at \(q=5\), \(n=2\).

Compile `exhaust.cpp` with `g++ -O3 -std=c++17 exhaust.cpp -o exhaust` and execute `./exhaust`; it enumerates **all** three-by-three matrices over \(\mathbb F_5\) and \(\mathbb F_7\) for \(n=1\) and tests the original multiplication-based identities and idempotence, without using the normal forms. The rank profiles are \((1,75,0,1)\) and \((1,147,0,1)\), respectively. These finite tests check computations only; the all-dimension result rests on the symbolic proof.

## Relationship to prior work
The precise general criterion that an idempotent averaging operator has subalgebra image and stable kernel is established by L. Guo and J. Pei (2014), Proposition 2.3. The present proof uses that standard framework rather than claiming it new. Braiek, Chtioui and Mabrouk (2024) develop anti-Leibniz and averaging structures; because all triple products vanish, the displayed algebra belongs to the natural two-step setting, but their inspected framework does not provide the present nonsymmetric finite-field projection census.

A **very close published antecedent**, *Complete retraction-rank spectra of split bilinear-product algebras over finite fields*, already treats precisely the same \(A_{n,a}\) and proves the first summand above, including the Goursat isotropic count and the isolated identity endomorphism. It decisively covers the entire retraction subfamily. The present finding therefore claims novelty only for the additional socle-fixing **non-endomorphism averaging** branch, its exact enumeration, and the resulting full averaging rank support. Another published result on idempotent averaging projections of **unital commutative** quadratic Gorenstein local algebras studies a distinct bilinear multiplication and does not subsume this nonunital nonsymmetric branch. Generic symplectic Heisenberg retractions and splitting Rota–Baxter projections likewise do not imply the stated two-sided averaging counts.

## Limitations
The algebra must have a nondegenerate nonsymmetric pairing of the exact specified type and \(a^2\ne1\). In particular neither symmetric nor alternating phase is addressed. The theorem does not cover non-idempotent averaging operators, singular bilinear pairings, classification of automorphism-conjugacy orbits, or non-reduced equation schemes. The retraction term is prior work; an unidentified broader theorem about self-adjoint projections could imply the elementary socle-fixing classification, so originality and publication priority remain provisional. No independent mathematical audit has been performed. Finite checks do not establish the general theorem by themselves.

## References
1. S. Braiek, T. Chtioui, S. Mabrouk, *Anti-Leibniz algebras: A non-commutative version of mock-Lie algebra* (2024), arXiv:2409.17184, https://arxiv.org/abs/2409.17184.
2. L. Guo and J. Pei, *Averaging algebras, Schröder numbers, rooted trees and operads* (2014), arXiv:1401.7386, https://arxiv.org/abs/1401.7386.
3. W. Cao, *An Algebraic Study of Averaging Operators* (2014), arXiv:1401.7389, https://arxiv.org/abs/1401.7389.
4. *Complete retraction-rank spectra of split bilinear-product algebras over finite fields* (2026), public full text: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-retraction-rank-spectra-of-split-bilinear-product-algeb--7bb1168c556c.
5. *Idempotent averaging projections on quadratic Gorenstein local algebras* (2026), public full text: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-idempotent-averaging-projections-on-quadratic-gorenstein-local-a--4c6e9f9c7511.
