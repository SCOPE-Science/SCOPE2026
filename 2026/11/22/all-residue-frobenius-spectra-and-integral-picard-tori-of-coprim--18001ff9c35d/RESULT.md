# All-residue Frobenius spectra and integral Picard tori of coprime Chebyshev curves

## Finding
Let \(2\le m<n\) be coprime, let \(q\) be an odd prime power with \(\gcd(q,mn)=1\), and let \(T_j\) denote the first-kind Chebyshev polynomial. Put
\[
C_{m,n}:T_n(X)-T_m(Y)=0\subset\mathbb A^2_{\mathbb F_q},\qquad
\overline C_{m,n}\subset\mathbb P^2_{\mathbb F_q}
\]
for its projective closure, and \(\delta=(m-1)(n-1)/2\). The maximal torus quotient \(\mathcal T_{m,n}\) of \(\operatorname{Pic}^0(\overline C_{m,n})\) and the zeta function of \(C_{m,n}\) are determined for **every** admissible residue of \(q\) modulo \(2mn\), without simultaneous signed congruence assumptions.

Here is a finite, exact recipe with no polynomial factorization. Set \(L=2mn\), and for \(a\in\mathbb Z\) define \(\rho(a)=\min(a\bmod L,(-a)\bmod L)\), with residues chosen in \(\{0,\ldots,L-1\}\). Form the set of unordered two-element labels
\[
\mathscr P_{m,n}=\left\{\left\{\rho(kn+\ell m),\rho(\ell m-kn)\right\}:1\le k<m,\;1\le\ell<n\right\}.
\]
It has exactly \(\delta\) elements. The permutation \(F_q\) sends \(\{a,b\}\) to \(\{\rho(qa),\rho(qb)\}\). For each orbit \(\mathcal O\) of length \(d\), put \(\epsilon(\mathcal O)=+1\) if \(\rho(q^da)=a\) and \(\rho(q^db)=b\); otherwise the two members are interchanged and put \(\epsilon(\mathcal O)=-1\). Let \(a_d\) and \(b_d\) count length-\(d\) positive and negative orbits respectively. Then
\[
\boxed{\mathcal T_{m,n}\cong
\prod_{d\ge1}\left(\operatorname{Res}_{\mathbb F_{q^d}/\mathbb F_q}\mathbb G_m\right)^{a_d}
\times\prod_{d\ge1}\left(\operatorname{Res}_{\mathbb F_{q^d}/\mathbb F_q}R^1_{\mathbb F_{q^{2d}}/\mathbb F_{q^d}}\mathbb G_m\right)^{b_d}.}
\]
This is an isomorphism of tori **over \(\mathbb F_q\)**, not merely an isogeny or a rational-character decomposition. In particular,
\[
\#\mathcal T_{m,n}(\mathbb F_q)=\prod_d(q^d-1)^{a_d}(q^d+1)^{b_d},
\quad
Z(C_{m,n}/\mathbb F_q,t)=\frac{\prod_d(1-t^d)^{a_d}(1+t^d)^{b_d}}{1-qt}.
\]
For every \(r\ge1\),
\[
\#C_{m,n}(\mathbb F_{q^r})=q^r-\sum_{d\mid r}d\left(a_d+(-1)^{r/d}b_d\right).
\]
The zeta function of the projective closure is the displayed affine zeta function divided by \(1-t\).

**A nonsigned example.** For \((m,n,q)=(3,8,7)\), the seven nodes have three negative fixed orbits and two positive orbits of length two. Thus
\[
\mathcal T_{3,8}\cong(R^1_{\mathbb F_{49}/\mathbb F_7}\mathbb G_m)^3
\times(\operatorname{Res}_{\mathbb F_{49}/\mathbb F_7}\mathbb G_m)^2,
\]
\[
Z(C_{3,8}/\mathbb F_7,t)=\frac{(1+t)^3(1-t^2)^2}{1-7t},\quad
\#C_{3,8}(\mathbb F_7)=10,\quad
\#C_{3,8}(\mathbb F_{49})=42,
\]
and \(\#\mathcal T_{3,8}(\mathbb F_7)=1{,}179{,}648\). The node orbit lengths and torus types in this example cannot be obtained from the previously published simultaneous \(\pm1\)-residue formula.

## Assumptions and scope
The Chebyshev recurrence is \(T_0(U)=1\), \(T_1(U)=U\), and \(T_{j+1}(U)=2UT_j(U)-T_{j-1}(U)\). Every finite-field assertion assumes \(q=p^e\) odd and \(p\nmid mn\). The superscript \(R^1\) denotes the norm-one torus, and \(\operatorname{Res}\) denotes Weil restriction. All products have finitely many nonzero exponents, and the label recipe depends only on \(q\bmod2mn\). The projective closure may be singular at infinity; its local one-branch contribution affects the unipotent part of \(\operatorname{Pic}^0\), **not** the claimed maximal torus quotient. No assertion identifies this torus with the whole connected Picard group when an infinity cusp is present.

## Proof
**1. Normalization and node count.** The commutation identity \(T_n\circ T_m=T_m\circ T_n\) gives \(\nu:\mathbb A^1\to C_{m,n}\), \(u\mapsto(T_m(u),T_n(u))\). Over an algebraic closure, \([\overline k(u):\overline k(T_m(u),T_n(u))]\) divides both \(m\) and \(n\), hence equals one. Since \(T_m(U)\) has nonzero leading coefficient, \(u\) is integral over \(\overline k[T_m(u),T_n(u)]\). Moreover, \([\overline k(T_m(u),T_n(u)):\overline k(T_m(u))]=m\), because \([\overline k(u):\overline k(T_m(u))]=m\) and the intermediate index is one. The polynomial \(T_n(X)-T_m(Y)\) has degree \(m\) in \(Y\) and vanishes under this parametrization, so it is its minimal polynomial (up to a nonzero scalar), and hence irreducible. Thus \(\nu\) is the finite birational normalization. Its projective extension has exactly one point over the unique point at infinity, because the source is \(\mathbb P^1\) and the affine normalization is \(\mathbb A^1\).

Take a primitive \(2d\)-th root \(z\) over \(\overline k\). The \(d-1\) distinct critical points of \(T_d\) are \((z^j+z^{-j})/2\), \(1\le j<d\), with critical value \((-1)^j\). This follows from \(T_d((w+w^{-1})/2)=(w^d+w^{-d})/2\), using \(p\nmid2d\). The second derivative at these points is nonzero by \((1-U^2)T_d''(U)-UT_d'(U)+d^2T_d(U)=0\). Consequently the singular locus of \(T_n(X)-T_m(Y)\) consists of the \(\delta\) critical-point pairs of equal parity, and each has two distinct tangents (an ordinary node). These are all affine singularities.

**2. Explicit branch pairs.** Let \(\zeta\) be a primitive \(2mn\)-th root. Write \(u_a=(\zeta^a+\zeta^{-a})/2\), so \(u_a=u_b\) precisely when \(a\equiv\pm b\pmod{2mn}\). For \(1\le k<m\) and \(1\le\ell<n\), set \(A=kn+\ell m\) and \(B=\ell m-kn\). Chebyshev's identity gives
\[
T_m(u_A)=T_m(u_B)=(-1)^k\frac{\zeta^{m^2\ell}+\zeta^{-m^2\ell}}2,
\qquad
T_n(u_A)=T_n(u_B)=(-1)^\ell\frac{\zeta^{n^2k}+\zeta^{-n^2k}}2.
\]
As \(A-B=2kn\) and \(A+B=2\ell m\), the two normalization parameters are distinct. Their image is an ordinary node. The pairs for \((k,\ell)\) and \((m-k,n-\ell)\) are the same unordered branch pair. Every other preimage of every node is covered: a normalization parameter above an affine node is \(u_a\), with \(1\le a<mn\) and neither \(m\) nor \(n\) dividing \(a\); solving the two signed root-of-unity equations in \(T_m(u_a)=T_m(u_b)\) and \(T_n(u_a)=T_n(u_b)\) yields \(A\equiv kn+\ell m\), \(B\equiv\ell m-kn\) up to signs. Equivalently, the \(2\delta\) distinct node-preimages are partitioned into precisely the \(\delta\) displayed unordered pairs. Therefore \(\mathscr P_{m,n}\) is a complete, multiplicity-free node labeling. This argument uses no finite enumeration as a substitute for the universal statement.

**3. Frobenius and the integral torus.** The arithmetic Frobenius sends \(\zeta\mapsto\zeta^q\), hence \(u_a\mapsto u_{qa}\). On a label it permutes the unordered branches exactly by \(F_q\); after returning to a node, either it fixes its two individual branches or exchanges them. Over an algebraic closure, the nodal local unit quotient is \(\mathbb G_m\), with its chosen branch ratio as coordinate. Exchanging branches inverts that coordinate. The one point at infinity is unibranch, so its local unit quotient contributes only unipotent groups; since the normalization is \(\mathbb P^1\), there is no abelian quotient. Thus the character lattice of the maximal torus is **integrally**, not merely after tensoring with \(\mathbb Q\), the direct sum of one rank-one signed permutation lattice for every geometric node. Positive length-\(d\) cycles give the character lattice of \(\operatorname{Res}_{\mathbb F_{q^d}/\mathbb F_q}\mathbb G_m\); negative cycles give the character lattice of \(\operatorname{Res}_{\mathbb F_{q^d}/\mathbb F_q}R^1_{\mathbb F_{q^{2d}}/\mathbb F_{q^d}}\mathbb G_m\). This proves the claimed isomorphism over the base field and the formula for rational torus points.

**4. Point counts.** The normalization \(\mathbb A^1\) has \(q^r\) rational points. A positive node orbit of length \(d\) contributes \(-d\) to the correction when \(d\mid r\); a negative orbit contributes \(-d(-1)^{r/d}\). Indeed a rational node contributes one point, while its two normalization preimages contribute two if they are rational and zero if exchanged. Summing proves the point-count identity. Exponentiating the generating function gives a factor \(1-t^d\) per positive cycle and \(1+t^d\) per negative cycle. The unique rational point at infinity contributes an extra factor \((1-t)^{-1}\) for the projective closure.

## Verification
Run `python3 verify.py` using only the Python standard library. The exact checker constructs the label set independently of the defining-equation point count, asserts its size, double presentation, closure and cycle signs for 1,471 arithmetic configurations, and then compares predicted counts with direct recurrence-based enumeration in 498 prime-field examples. An independently implemented quadratic extension arithmetic checks 162 more field-count examples. It also checks the worked \((3,8,7)\) example over both \(\mathbb F_7\) and \(\mathbb F_{49}\). Output from the packaged program is included as `check_output.txt`. These finite computations corroborate rather than prove the all-degree formula; the normalization, node classification, and signed integral descent are proved above.

## Relationship to prior work
Koseleff–Pecker [1, §2, Propositions 1–2] and Freudenburg–Freudenburg [2, §3, Proposition 3.1] established the geometric rational Chebyshev parametrization and its exact ordinary nodes. Those inputs are not new. An earlier arithmetic result [3] gives the entire affine zeta function **only** under simultaneous signed conditions \(q\equiv\pm1\pmod{2m}\) and \(q\equiv\pm1\pmod{2n}\): its nodes are all fixed and uniformly split/nonsplit. The present theorem handles every unit residue, includes nontrivial node orbits and nonuniform branch splitting, and determines the integral torus isomorphism type. The all-residue theorem restricts to [3] in its signed subfamily but is not implied by that subfamily; for instance \((3,8,7)\) lies outside it. Dimca–Sticlaru [4] study equal-degree (generally reducible) Chebyshev arrangements and Milnor algebras, not this coprime two-degree arithmetic torus. The other same-object published studies [5–6] treat complex dual ramification and real chamber algebras, respectively; neither supplies arithmetic signed orbit factors.

## Limitations
The theorem assumes coprime degrees at least two and an odd finite field of characteristic prime to both degrees. It does not classify bad-characteristic specializations, the unipotent extension at the projective infinity cusp, or the whole non-toric Picard group. The proof is internal and has not undergone an independent mathematical audit. Historical priority could be affected by older finite-field or knot-diagram treatments not located by the recorded searches; novelty claims are limited to the compared statements and inspected materials.

## References
[1] P.-V. Koseleff and D. Pecker, *Chebyshev Knots*, arXiv:0812.1089v1, first posted 2008-12-05; §2 Propositions 1–2. https://arxiv.org/html/0812.1089v2

[2] Gene and Jenna Freudenburg, *Curves Defined by Chebyshev Polynomials*, arXiv:0902.3440v1, first posted 2009-02-19; §3 Proposition 3.1. https://arxiv.org/html/0902.3440v1

[3] *An exact zeta function for nodal Chebyshev curves over finite fields* (2026), published RESULT.md. https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-an-exact-zeta-function-for-nodal-chebyshev-curves-over-finite-fi--0c77de977ec5/RESULT.md

[4] A. Dimca and G. Sticlaru, *Chebyshev curves, free resolutions and rational curve arrangements*, arXiv:1108.0798 (2011), §§1–2. https://arxiv.org/abs/1108.0798

[5] *Simple affine ramification and a cuspidal dual infinity for coprime Chebyshev curves* (2026), published RESULT.md. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-simple-affine-ramification-and-a-cuspidal-dual-infinity-for-copr--29dda6286b6e/RESULT.md

[6] *Degree-one chamber generation for plane Chebyshev arrangements* (2026), published RESULT.md. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-degree-one-chamber-generation-for-plane-chebyshev-arrangements--ac438cd907a2/RESULT.md
