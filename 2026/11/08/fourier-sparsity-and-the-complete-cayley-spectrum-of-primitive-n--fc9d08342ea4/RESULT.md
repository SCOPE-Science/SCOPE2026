# Fourier sparsity and the complete Cayley spectrum of primitive nilpotent matrices over odd prime-power rings

## Finding

Let \(p\) be any odd prime and \(k\ge2\). Put \(R=\mathbb Z/p^k\mathbb Z\) and
\[
\mathcal N_{p,k}=\{G E_{12}G^{-1}:G\in\operatorname{GL}_2(R)\}\subset M_2(R),
\qquad E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]
Equivalently, \(\mathcal N_{p,k}\) is the set of square-zero matrices that remain nonzero modulo \(p\). The unnormalized Cayley convolution
\[
(Tf)(Y)=\sum_{X\in\mathcal N_{p,k}}f(Y-X)
\]
on the additive group \(M_2(R)\) has the **entire real, integral eigenvalue multiset** specified below, with exact multiplicities. In particular, its complex rank is
\[
\boxed{\operatorname{rank}T=p^k\left[p^3+(p^2-1)\sum_{m=2}^k w_m p^{2m-2}\right],\qquad
 w_m=\begin{cases}p,&m\text{ even},\\p-1,&m\text{ odd}.\end{cases}}
\]
The graph has \(p^{4k}\) vertices and degree \((p^2-1)p^{2k-2}\). At the first nonfield level \(k=2\), its adjacency rank is **exactly \(p^7\)**, so precisely the proportion \(1-1/p\) of its eigenvalues vanish. For every fixed odd prime \(p\), the nonzero spectral fraction is \(\asymp_p p^{-k}\) as \(k\to\infty\), a persistent arithmetic Fourier-sparsity phenomenon.

## Assumptions and scope

Characters are indexed by \(A\in M_2(R)\):
\[
\chi_A(Y)=\exp\!\left(\frac{2\pi i\,\operatorname{tr}(AY)}{p^k}\right),\qquad
\lambda(A)=\sum_{X\in\mathcal N_{p,k}}\chi_A(X).
\]
This trace pairing is perfect on the additive matrix group. Write
\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
q_A(x,y)=c x^2+(d-a)xy-b y^2.
\]
Define its **content valuation** \(t\in\{0,\dots,k\}\) as the minimum of the truncated \(p\)-adic valuations of \(c,d-a,b\). In particular, \(t=k\) exactly when \(A\) is scalar. For \(t<k\), put \(m=k-t\) and let \(q'=p^{-t}q_A\) over \(\mathbb Z/p^m\mathbb Z\), a primitive binary quadratic form. If \(q'=\alpha x^2+\beta xy+\gamma y^2\), let \(\Delta=\beta^2-4\alpha\gamma\pmod{p^m}\) and \(v=\min(v_p(\Delta),m)\). Let \(\eta\) be the quadratic character on \(\mathbb F_p^\times\) extended by \(\eta(0)=0\).

The eigenvalue is given **pointwise for every frequency** by these exhaustive rules:

* If \(t=k\), then \(\lambda(A)=(p^2-1)p^{2k-2}\).
* If \(t=k-1\), so \(m=1\), then
  \[\lambda(A)=p^{2k-2}\bigl[p(1+\eta(\Delta))-(p+1)\bigr].\]
* If \(m=2h\ge2\), then
  \[
  \lambda(A)=\begin{cases}
  (p-1)p^{k+t+h-1},&v=m,\\
  -p^{k+t+h-1},&v=m-1,\\
  0,&v<m-1.
  \end{cases}
  \]
* If \(m=2h+1\ge3\), then
  \[
  \lambda(A)=\begin{cases}
  p^{k+t+h}\eta(\Delta/p^{m-1}),&v=m-1,\\
  0,&v\ne m-1.
  \end{cases}
  \]
In the last case the character is applied to the nonzero residue of \(\Delta/p^{m-1}\). All divisibility and valuations use representatives only in the indicated residue rings.

**Exact multiplicities.** The following is a *multiset prescription*: when numerical eigenvalues from different rows coincide, **add** their displayed multiplicities. At \(t=k\), the eigenvalue \((p^2-1)p^{2k-2}\) has multiplicity \(p^k\). At \(m=1\) the three values have multiplicities
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
-(p+1)p^{2k-2}&\tfrac12p^{k+1}(p-1)^2\\
-p^{2k-2}&p^k(p^2-1)\\
(p-1)p^{2k-2}&\tfrac12p^{k+1}(p^2-1)
\end{array}
\]
For each \(m\in\{2,\dots,k\}\), let \(t=k-m\) and \(H_m=(p^2-1)p^{2m-2}\). If \(m=2h\) is even, append
\[
\begin{array}{c|c}
(p-1)p^{k+t+h-1}&p^kH_m\\
-p^{k+t+h-1}&p^k(p-1)H_m
\end{array}
\]
while if \(m=2h+1\ge3\) is odd, append
\[
\begin{array}{c|c}
p^{k+t+h}&\tfrac12p^k(p-1)H_m\\
-p^{k+t+h}&\tfrac12p^k(p-1)H_m.
\end{array}
\]
Every other eigenvalue is zero; its multiplicity is \(p^{4k}-\operatorname{rank}T\). These tables include the trivial character, repeated scalar-frequency eigenvalues, and all collisions across valuation layers.

## Proof

**1. Nilpotent orbit and degree.** Every matrix \(X\) with \(X^2=0\) and nonzero reduction modulo \(p\) is conjugate to \(E_{12}\). Indeed, choose \(v\) with \(u=Xv\) primitive. Then \(Xu=0\); the reductions of \(u,v\) are independent, so \((u,v)\) is a basis in which \(X\) is the standard nilpotent Jordan block. Let \(J(x,y)=(-y,x)\). A nilpotent in the orbit is uniquely \(s u(Ju)^{\mathsf T}\) for a projective line \(Ru\in\mathbb P^1(R)\) and a unit coefficient \(s\in R^\times\), after fixing one generator for every projective line. Changing generator scales \(s\) bijectively, so the parametrization is intrinsic. The projective line has \(p^{k-1}(p+1)\) points and \(|R^\times|=(p-1)p^{k-1}\), giving degree \((p^2-1)p^{2k-2}\). Since \(-s\) is a unit, the set is symmetric: \(\mathcal N_{p,k}=-\mathcal N_{p,k}\).

**2. Ramanujan reduction.** The trace identity
\[
\operatorname{tr}\bigl(A\,s u(Ju)^{\mathsf T}\bigr)=s(Ju)^{\mathsf T}Au=sq_A(u)
\]
reduces each projective direction to the unit Ramanujan sum
\[
\sum_{s\in R^\times}\exp\!\left(\frac{2\pi i s z}{p^k}\right)
=\begin{cases}(p-1)p^{k-1},&z\equiv0\pmod{p^k},\\
-p^{k-1},&v_p(z)=k-1,\\0,&v_p(z)<k-1.\end{cases}
\]
Let \(Z_j(q_A)\) count projective zeros of \(q_A\) modulo \(p^j\). Each projective line over \(p^{k-1}\) has exactly \(p\) lifts to level \(k\). Thus
\[
\lambda(A)=p^k\bigl(Z_k(q_A)-Z_{k-1}(q_A)\bigr).\tag{1}
\]
Here \(Z_j\) always means a count over \(\mathbb P^1(\mathbb Z/p^j\mathbb Z)\), not an affine root count. If \(q_A=0\), (1) gives the stated orbit degree. If its content is \(t=k-1\), write \(Z_1(q')=z\); then \(Z_k=p^{k-1}z\) and \(Z_{k-1}=p^{k-2}(p+1)\), giving \(p^{2k-2}[pz-(p+1)]\). In general \(t\le k-2\) gives
\[
\lambda(A)=p^{k+t}\bigl(Z_m(q')-Z_{m-1}(q')\bigr),\qquad m=k-t.\tag{2}
\]

**3. Root lifting and discriminants.** Because \(p\) is odd, a primitive quadratic form modulo \(p\) has respectively zero, one, or two projective roots according as its discriminant is a nonsquare, zero, or a nonzero square. In the latter two-simple-root case each root lifts uniquely, so \(Z_m-Z_{m-1}=0\) for all \(m\ge2\). In the nonsquare case both are zero. In the double-root case a coordinate change puts the unique root in an affine chart with one quadratic coefficient a unit. Completing the square identifies \(Z_j(q')\), for every \(j\ge1\), with the number of square roots of \(\Delta\pmod{p^j}\); multiplying \(\Delta\) by a unit square does not change the count.

For any \(D\pmod{p^m}\), the equation \(x^2=D\pmod{p^m}\) has \(p^{\lfloor m/2\rfloor}\) roots if \(D\equiv0\), has zero roots when \(0\le v_p(D)<m\) is odd, and, when \(v_p(D)=2h<m\), has either \(2p^h\) or zero roots according to whether the unit part is respectively a square or a nonsquare modulo \(p\). These are exact: divide by \(p^{2h}\), use Hensel lifting of the two simple roots, and count the \(p^h\) lifts. Subtracting the root numbers at adjacent levels \(m,m-1\) yields exactly the even- and odd-\(m\) eigenvalue cases above, including the negative boundary jumps. This establishes every pointwise eigenvalue, not just its possible magnitudes.

**4. Multiplicities.** The linear map \(A\mapsto q_A\) from \(M_2(R)\) onto the three coefficients of a binary quadratic form is surjective, and every fiber consists of \(p^k\) scalar translates. For \(m=1\), direct counting of \((\alpha,\beta,\gamma)\ne(0,0,0)\) with \(\Delta=\beta^2-4\alpha\gamma\) gives \(p(p-1)^2/2\) nonsquare-discriminant forms, \(p^2-1\) zero-discriminant forms, and \(p(p^2-1)/2\) split-discriminant forms. This gives the three multiplicities at \(m=1\).

For \(m\ge2\), every primitive quadratic form whose discriminant vanishes modulo \(p\) has a unit coefficient \(\alpha\) or \(\gamma\). Hence the discriminant map has a unit partial derivative \(-4\alpha\) or \(-4\gamma\); it is a smooth, uniformly lifting map over the \(p\)-adic digits. There are \(p^2-1\) nonzero mod-\(p\) forms of discriminant zero. Therefore, **for each fixed prescribed residue** \(\Delta\in p(\mathbb Z/p^m\mathbb Z)\), the number of primitive coefficient triples is exactly
\[
H_m=(p^2-1)p^{2m-2}.
\]
The even-level nonzero cases comprise one residue \(\Delta=0\) and \(p-1\) residues of valuation \(m-1\). The odd-level cases comprise the \((p-1)/2\) square-unit and \((p-1)/2\) nonsquare-unit residues of valuation \(m-1\). Multiplying these counts by the free \(p^k\) scalar frequencies proves all multiplicities and the rank sum. Fourier diagonalization of additive convolution establishes the matrix/operator interpretation.

**5. Fourier-sparsity consequence.** Summing the nonzero frequencies by level yields precisely the displayed rank formula. At \(k=2\) its bracket reduces to \(p^5\), so the rank is \(p^7\). For fixed \(p\), the geometric ratio between the contributions at levels two apart is \(p^4\), hence the rank is bounded above and below by positive \(p\)-dependent constants times \(p^{3k}\). The ambient dimension is \(p^{4k}\), establishing nonzero spectral fraction \(\asymp_p p^{-k}\).

## Verification

The independent integer checker `verify.py` evaluates the pointwise discriminant/valuation formula at **every** matrix frequency for \((p,k)=(3,2),(3,3),(5,2)\), comparing histograms against the separate closed multiplicity prescription. It checks that the eigenvalue sum is zero (the orbit excludes zero), and the Parseval square sum is \(p^{4k}|\mathcal N_{p,k}|\). An entirely separate enumeration constructs the nilpotent matrices from projective directions and unit parameters, then directly sums complex characters over the orbit; it checks all \(3^8\) frequencies at \((p,k)=(3,2)\) and selected fixed-seed frequencies at \((5,2),(3,3),(3,4),(5,3)\). Run `python3 verify.py` with only the standard library. Success prints `PRIMITIVE_NILPOTENT_LOCAL_SPECTRUM_PASS`. These computations test the formulas but are not the proof of the all-prime, all-depth claim.

## Relationship to prior work

DeBacker and Sally [1, Appendix A] compute Fourier transforms of nilpotent orbital integrals for the **continuous** \(p\)-adic group \(\operatorname{SL}_2\). Spice [2, §1] cites this fact and develops transforms of semisimple orbital integrals in the same local-field setting. Their integral distributions and orbit normalizations are not the discrete additive Cayley operator on \(M_2(\mathbb Z/p^k\mathbb Z)\), nor do the inspected statements provide the present exact finite-depth eigenvalue multiplicities. A specialization/averaging of their theory could possibly imply this result; it has not been excluded categorically. Evdokimov and Ponomarenko [3] analyze general ring cyclotomic schemes and normality/automorphisms, not the present explicit primitive nilpotent orbit spectrum. Li and Hu [4] evaluate matrix-group Gauss sums over **fields**, not the nilpotent orbit over composite prime-power rings. Harris [5] treats continuous real nilpotent coadjoint-orbit Fourier transforms. A related finite-field compressed nilpotent Fourier-matrix calculation concerns a different operator (both Fourier indices restricted to the orbit) and is not equivalent to this full ambient Cayley spectrum.

## Limitations

The theorem requires \(p\) odd and \(k\ge2\), concerns the primitive regular nilpotent orbit only, and computes the unnormalized additive Cayley spectrum. It does not cover nonprimitive square-zero matrices, \(p=2\), all nilpotent matrix sizes, or weighted Fourier-restriction norms. Although relevant primary manuscripts were inspected, the literature comparison is bounded: general continuous \(p\)-adic nilpotent orbital Fourier theory could yield a dominating statement after a nontrivial finite-shell specialization. The multiplicities and rank have not undergone independent specialist audit.

## References

1. S. DeBacker and P. J. Sally Jr., *Germs, characters, and the Fourier transforms of nilpotent orbits*, Appendix A. Public author manuscript: https://websites.umich.edu/~smdbackr/MATH/germs.pdf (continuous \(p\)-adic orbit integrals; publication priority not asserted from the PDF timestamp).
2. L. Spice, *Fourier transforms of semisimple orbital integrals on the Lie algebra of SL2*, arXiv:1008.1592v1, first public 9 August 2010. https://arxiv.org/abs/1008.1592.
3. S. Evdokimov and I. Ponomarenko, *Normal cyclotomic schemes over a finite commutative ring*, arXiv:math/0608469v1, first public 18 August 2006. https://arxiv.org/abs/math/0608469.
4. Y. Li and S. Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513v1, first public 23 May 2011. https://arxiv.org/abs/1105.4513.
5. B. Harris, *Fourier transforms of nilpotent, coadjoint orbits for GL(n,R)*, arXiv:1209.4122v1, first public 18 September 2012. https://arxiv.org/abs/1209.4122.
