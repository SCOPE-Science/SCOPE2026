# An almost-ordinary Prym on every smooth symmetric minimal filling curve over \(\mathbb F_3\)

## Finding
Let \(k=\mathbb F_3\), and let
\[
E(U,V)=U^3V-UV^3,\qquad
A(U,V)=U^4+UV^3+2V^4.
\]
On \(\mathbb P^1_k\times\mathbb P^1_k\), with homogeneous coordinates \(([X_0:X_1],[Y_0:Y_1])\), define
\[
C:\quad F=A(Y_0,Y_1)E(X_0,X_1)+A(X_0,X_1)E(Y_0,Y_1)=0.
\]
The curve is smooth, geometrically integral, has bidegree \((4,4)\) and genus \(9\), and contains all \(16\) rational points of the ambient surface. Let \(\iota(X,Y)=(Y,X)\). Its quotient \(Q=C/\langle\iota\rangle\) is the smooth genus-three plane quartic
\[
G(S,T,U)=2S^3U-S^3T+S^2TU+SU^3+ST^3+TU^3+T^2U^2=0,
\]
where \(T=X_0Y_0\), \(S=X_0Y_1+X_1Y_0\), and \(U=X_1Y_1\). The double cover \(C\to Q\) is branched at exactly eight distinct geometric points. Its Prym \(P=\ker(\operatorname{Nm}:J(C)\to J(Q))^0\) has dimension \(6\).

The complete arithmetic conclusion in characteristic \(3\) is
\[
\boxed{(f_3(J(C)),a(J(C)))=(8,1),\quad
(f_3(J(Q)),a(J(Q)))=(3,0),\quad
(f_3(P),a(P))=(5,1).}
\]
Here \(f_3\) denotes \(3\)-rank and \(a(B)=\dim_{\bar k}\operatorname{Hom}(\alpha_3,B[3])\) is the \(a\)-number. In particular, the quotient Jacobian is ordinary while the Prym is almost ordinary.

More generally, for any nonzero binary quartic \(B\in k[U,V]_4\), define the *symmetric minimal filling member*
\[
C_B:\quad B(Y)E(X)+B(X)E(Y)=0.
\]
**Every geometrically smooth member \(C_B\) has the same three pairs of arithmetic invariants stated above** (with its own quotient and Prym). Up to scalar, there are exactly six smooth choices of \(B\) over \(k\), and all are equivalent under the diagonal \(\operatorname{PGL}_2(k)\)-action. The count and symmetry construction are background to the arithmetic finding, not claimed as novel.

## Assumptions and scope
All curves and abelian varieties are over \(k=\mathbb F_3\), and smoothness and rank statements are geometric, after base change to an algebraic closure. Quotients and Pryms refer to the factor-exchange involution, which is tame because the characteristic is not two. The six choices of \(B\) are counted as projective coefficient classes (the first nonzero coefficient normalized to one), not as six isomorphism classes. A smooth bidegree-\((4,4)\) divisor is geometrically connected and integral and has arithmetic genus \((4-1)(4-1)=9\).

## Proof
**Smoothness, filling, and completeness of the symmetric family.** Since \(E\) vanishes at each of the four points of \(\mathbb P^1(k)\), every \(C_B\) contains all sixteen rational pairs. If \(B\) has a rational zero \(u\), then at the diagonal point \((u,u)\) both \(F\) and its local first derivatives vanish; thus no such \(C_B\) is smooth. There are exactly twenty-four projectively normalized quartics with no rational zero. For the displayed \(A\), the ideal \((F,\partial F/\partial x,\partial F/\partial y)\) on **each** of the four standard product affine charts has reduced Gröbner basis \((1)\) over \(k\). The same four-chart test for all twenty-four root-free quartics leaves precisely the six coefficient tuples
\[
(1,0,0,1,2),\ (1,0,0,2,2),\ (1,1,0,0,2),\ (1,1,0,2,1),\ (1,2,0,0,2),\ (1,2,0,1,1),
\]
relative to the monomials \(U^{4-i}V^i\). These six form a single orbit under the twenty-four-element diagonal \(\operatorname{PGL}_2(k)\); the representative stabilizer has order four. The exact polynomial identities, finite exhaustive candidate space, and unit-ideal certificates are reconstructed by `verify_geometry.py`. A diagonal coordinate change sends \(E\) to its determinant multiple, *the same multiplier in both summands*, and hence preserves the symmetric family up to scalar. Consequently all smooth symmetric members are isomorphic over \(k\) to the displayed \(C\), compatibly with factor exchange. They share the sought arithmetic invariants.

**Quotient and branch.** The symmetric square \(\operatorname{Sym}^2(\mathbb P^1)\) is \(\mathbb P^2\), with the stated quotient coordinates. Direct substitution yields the polynomial identity \(G(S,T,U)=F(X,Y)\) in characteristic \(3\). The three affine-chart ideals \((G,G_s,G_t)\) all have Gröbner basis \((1)\), so \(Q=V(G)\) is a smooth plane quartic, of genus three. The branch locus is the intersection with the diagonal, where the equation becomes \(2A(U,V)E(U,V)=0\). The four roots of \(E\) are the rational points of \(\mathbb P^1\); the binary quartic \(A\) is separable and has no common root with \(E\), so there are exactly eight distinct ramification points. Riemann–Hurwitz gives \(2(9)-2=2(2(3)-2)+8\), consistent with the two genera. It follows that the Prym has dimension \(9-3=6\).

**Exact Frobenius coefficient calculation on \(C\).** The standard divisor sequence identifies
\[
H^1(C,\mathcal O_C)\cong H^2(\mathbb P^1\times\mathbb P^1,\mathcal O(-4,-4)),
\]
of dimension nine, with Čech monomial basis indexed by \((i,j)\in\{1,2,3\}^2\). Frobenius is represented over \(k\) by the matrix
\[
H_{(r,s),(i,j)}=
[X_0^{3i-r}X_1^{3(4-i)-(4-r)}Y_0^{3j-s}Y_1^{3(4-j)-(4-s)}]F^2\pmod3.
\]
An exponent below zero gives coefficient zero. The extraction performed in `verify_hasse.py` produces, in lexicographic index order,
\[
H=\begin{pmatrix}
1&1&1&1&2&0&1&0&0\\
2&0&1&1&0&1&0&1&0\\
1&2&1&0&2&2&0&0&1\\
2&1&0&0&0&1&1&1&0\\
2&0&2&0&1&2&2&2&2\\
0&1&1&1&1&1&0&1&0\\
1&0&0&2&2&0&1&2&1\\
0&1&0&1&1&1&1&1&0\\
0&0&1&0&2&0&1&0&0
\end{pmatrix}.
\]
Its leading principal \(8\times8\) minor equals \(1\) modulo \(3\), its determinant is zero, and its characteristic polynomial over \(k\) is
\[
\chi_H(z)=z(z-1)^2(z^2+1)(z^2+z-1)^2.
\]
The zero eigenvalue has algebraic multiplicity one, so \(\operatorname{rank}(H^n)=8\) for every integer \(n\ge1\). Since the coefficient field is \(\mathbb F_3\), the Frobenius semilinearity causes no additional twists in matrix products. Thus the stable Frobenius rank, and hence the Jacobian \(3\)-rank, is eight, while the Cartier \(a\)-number is \(9-\operatorname{rank}H=1\).

**The ordinary quotient and the Prym.** For the plane quartic use the basis indexed by \((2,1,1),(1,2,1),(1,1,2)\). Its Hasse–Witt matrix is obtained from coefficients
\[
(H_Q)_{\beta,\alpha}=[S^{3\alpha_1-\beta_1}T^{3\alpha_2-\beta_2}U^{3\alpha_3-\beta_3}]G^2\pmod3
\]
and is exactly
\[
H_Q=\begin{pmatrix}1&2&2\\1&0&0\\1&0&2\end{pmatrix},\qquad \det H_Q=2\ne0\pmod3.
\]
Hence \(J(Q)\) is ordinary, with \(3\)-rank three and \(a\)-number zero. The norm/pullback Prym decomposition gives a \(2\)-power-degree isogeny \(J(Q)\times P\to J(C)\). Since \(2\) is prime to the characteristic, this induces an isomorphism on \(3\)-divisible groups. Consequently \(3\)-ranks and \(a\)-numbers add, giving \(f_3(P)=8-3=5\) and \(a(P)=1-0=1\).

## Verification
The self-contained scripts `verify_geometry.py` and `verify_hasse.py` use exact symbolic arithmetic over \(\mathbb F_3\), reconstruct the equations from their definitions, and verify the quotient pullback identity, smoothness ideals, eight branch points, the full twenty-four/six candidate census, diagonal orbit, both complete Hasse–Witt matrices, nonzero minors, and Frobenius characteristic polynomial. Run with Python 3 and SymPy, invoking each script from its directory. Exact Gröbner-basis reduction to \((1)\) rules out *geometric* common zeros in the corresponding affine chart, not just rational ones. The rank formula for the Prym follows mathematically from the prime-to-three isogeny, not a finite sample.

## Relationship to prior work
Homma and Kim, *Filling curves for \(\mathbb P^1\times\mathbb P^1\)* (arXiv:2203.11595, first public March 22, 2022), established the minimal filling bidegree and existence of smooth examples. Ahammed, Campbell, and Moon, *Minimal algebraic space filling curves on the product of projective lines* (arXiv:2512.02796, December 2025), studied the symmetric construction and the \(q=3\) smoothness orbits. Their established existence, smoothness classification, and orbit counts are used as context, not novelty. The arithmetic statement here is the exact Hasse–Witt rank and stable rank of a genus-nine curve, the explicit genus-three quotient and its ordinarity, and the almost-ordinary Prym; neither inspected primary source states those conclusions. Standard quotient, divisor-cohomology and Prym decomposition theorems are used in the proof.

## Limitations
This is the arithmetic classification of the *symmetric subfamily* in characteristic three, not of all nonsymmetric filling curves or all characteristics. No full Newton polygon, complete zeta function, or integral geometric endomorphism ring is claimed. The originality comparison covers the identified primary work and mathematical-result searches, not every unpublished or historically unindexed computation. The status is self-review only; no independent validation or independent historical-priority certification has been performed.

## References
1. M. Homma and S. J. Kim, *Filling curves for \(\mathbb P^1\times\mathbb P^1\)*, arXiv:2203.11595 (2022), especially Theorem 3.3. https://arxiv.org/abs/2203.11595
2. M. Ahammed, M. Campbell and H.-B. Moon, *Minimal algebraic space filling curves on the product of projective lines*, arXiv:2512.02796 (2025), Sections 4.1 and 6. https://arxiv.org/abs/2512.02796
3. Standard facts: Riemann–Hurwitz, Frobenius on Čech cohomology of hypersurface divisors, and Prym decomposition for tame degree-two covers.
