# Finite-field forms, symmetry spectra, and Frobenius cycles of exceptional Chebyshev root divisors

## Finding
Let \(p\) be any odd prime, let \(r,s\geq1\), let \(d=(p^r+1)/2\geq5\), and write \(Q=p^s\). Let \(\varphi_d\) be the monic Dickson–Chebyshev polynomial characterized by \(\varphi_d(t+t^{-1})=t^d+t^{-d}\), and let \(B_d\subset\mathbb P^1_{\mathbb F_Q}\) be its reduced zero divisor. An *arithmetic form* of \(B_d\) is a reduced degree-\(d\) finite étale subscheme of \(\mathbb P^1_{\mathbb F_Q}\) that is projectively equivalent to \(B_d\) over an algebraic closure; two such forms are identified by \(\operatorname{PGL}_2(\mathbb F_Q)\).

Put \(m_+=\gcd(d,Q-1)\) and \(m_-=\gcd(d,Q+1)\). There are exactly
\[
\frac{m_++\gcd(m_+,2)+m_-+\gcd(m_-,2)}{2}
\]
arithmetic forms. They admit unique labels \((\varepsilon,a)\), where \(\varepsilon\in\{+1,-1\}\) and \(0\leq a\leq\lfloor m_\varepsilon/2\rfloor\), with \(m_{+1}=m_+\) and \(m_{-1}=m_-\). The rational projective automorphism group of the form labeled \((\varepsilon,a)\) is
\[
\begin{cases}
D_{m_\varepsilon},&m_\varepsilon\mid2a,\\
C_{m_\varepsilon},&m_\varepsilon\nmid2a.
\end{cases}
\]
Here \(D_m\) denotes the dihedral group of order \(2m\), including \(D_1\cong C_2\) and \(D_2\cong C_2\times C_2\); \(C_m\) is cyclic of order \(m\), including the trivial group \(C_1\).

All Frobenius cycle types, and hence all point counts and zeta functions, are explicit. For a label \((\varepsilon,a)\), put \(k=\varepsilon Q\) and \(b=a+(k-1)/2\), integers. The Frobenius action on its \(d\) geometric points is conjugate to the permutation
\[
j\longmapsto kj+b\pmod d,\qquad j\in\mathbb Z/d\mathbb Z.
\]
For every \(n\geq1\), put \(h_n=\gcd(d,k^n-1)\) and \(u_n=1+k+\cdots+k^{n-1}\). Its number \(N_n\) of \(\mathbb F_{Q^n}\)-points is
\[
N_n=\begin{cases}h_n,&h_n\mid bu_n,\\0,&h_n\nmid bu_n.\end{cases}
\]
If the affine permutation has cycle lengths \(\ell_1,\ldots,\ell_c\), the exact finite-scheme zeta function is \(\prod_i(1-T^{\ell_i})^{-1}\).

For example, in characteristic \(11\) with \(d=6\) and \(Q=11\), the six forms have exactly five different zeta functions:
\[
(1-T^2)^{-3},\quad (1-T)^{-2}(1-T^2)^{-2},\quad (1-T)^{-6},\quad
(1-T^6)^{-1},\quad (1-T^3)^{-2}.
\]
The first occurs for two nonisomorphic forms. Precisely one of the six forms has all six points rational, while another has a single six-cycle.

## Assumptions and scope
The field has odd prime characteristic \(p\). The integer \(d=(p^r+1)/2\) is at least five; in particular \(p\nmid d\). The collection being classified consists of *unlabeled*, reduced divisors with ambient projective equivalence, not abstract finite étale schemes or hyperelliptic curves. The automorphism groups concern the pair \((\mathbb P^1,B)\), not automorphisms of any double cover branched at \(B\). Every formula is valid for all positive integers \(r,s,n\) subject to the stated hypotheses, including even \(d\) and characteristic \(3\).

## Proof
**Geometric stabilizer and rational model.** Tafazolian–Top prove that the geometric stabilizer of this Chebyshev root set is dihedral of order \(2d\) for \(2d=p^r+1\). Its embedding and descent can be made explicit independently: set \(z=(x-2)/(x+2)\) (so \(x=2(1+z)/(1-z)\)). With \(q=p^r\) and \(d=(q+1)/2\), the identity
\[
(1-z)^d\varphi_d\!\left(\frac{2(1+z)}{1-z}\right)=2(1+z^d)
\]
holds in characteristic \(p\). To verify it, adjoin \(u\) with \(u^2=z\), substitute \(t=(1+u)/(1-u)\), multiply the defining identity by \((1-u^2)^d\), and use
\[
(1+u)^{q+1}+(1-u)^{q+1}=2(1+u^{q+1}).
\]
Thus the root divisor is \(z^d=-1\), with no root at \(z=1\) or infinity. Every geometric symmetry is \(z\mapsto\zeta z\) or \(z\mapsto\zeta/z\), with \(\zeta^d=1\). This makes its finite étale stabilizer group scheme over \(\mathbb F_p\) the split semidirect product \(\mu_d\rtimes C_2\), where \(C_2\) acts by inversion ("split" refers to the reflection section; \(\mu_d\) need not be a constant group scheme). Indeed \(p\nmid2d\), and a projective vector field vanishing at three or more distinct points is zero, so the stabilizer scheme has no infinitesimal component.

**Arithmetic forms.** Finite-field Galois descent identifies forms of the pair with \(H^1(\mathbb F_Q,\mu_d\rtimes C_2)\). A twisted projective line is necessarily isomorphic to \(\mathbb P^1\) over a finite field, since \(H^1(\mathbb F_Q,\operatorname{PGL}_2)=1\) (equivalently the finite-field Brauer group is zero). Thus this classification is by actual \(\operatorname{PGL}_2(\mathbb F_Q)\)-orbits of degree-\(d\) divisors.

Choose a primitive \(d\)-th root \(\xi\) in an algebraic closure. Write geometric automorphisms as \((a,\varepsilon)\), meaning \(z\mapsto\xi^a z\) when \(\varepsilon=+1\) and \(z\mapsto\xi^a/z\) when \(\varepsilon=-1\), with product
\[
(a,\varepsilon)(c,\delta)=(a+\varepsilon c,\varepsilon\delta),\qquad
\operatorname{Frob}_Q(a,\varepsilon)=(Qa,\varepsilon).
\]
Every continuous cocycle is specified by its value \((a,\varepsilon)\) at Frobenius. Twisted conjugation by \((c,\delta)\) changes \(a\) to \(\delta(a+(\varepsilon Q-1)c)\) and leaves \(\varepsilon\) unchanged. Therefore the \(\varepsilon\)-sector consists exactly of \((\mathbb Z/m_\varepsilon\mathbb Z)/\{a\sim-a\}\). Its inversion-orbit representatives are \(0,1,\ldots,\lfloor m_\varepsilon/2\rfloor\), establishing the form count.

**Rational stabilizers.** An automorphism \((c,\delta)\) of the geometric pair descends to a twist \((a,\varepsilon)\) precisely when it fixes the cocycle under twisted conjugation. For \(\delta=+1\) the condition is \((\varepsilon Q-1)c=0\pmod d\), giving \(m_\varepsilon\) rotations. For \(\delta=-1\) the condition is \((\varepsilon Q-1)c=-2a\pmod d\), soluble exactly when \(m_\varepsilon\mid2a\), again with \(m_\varepsilon\) solutions. When present, a reflection inverts the rotation subgroup. This proves the stated cyclic-or-dihedral classification.

**Frobenius cycles.** Choose a primitive \(2d\)-th root \(\eta\), let \(\xi=\eta^2\), and label the geometric roots by \(z_j=\eta\xi^j\). The cocycle \((a,\varepsilon)\) replaces ordinary Frobenius by \(z\mapsto\xi^a z^{\varepsilon Q}\); the corresponding label map is \(j\mapsto\varepsilon Qj+a+(\varepsilon Q-1)/2\). Its \(n\)-th power is \(j\mapsto k^n j+bu_n\). A linear congruence \((k^n-1)j=-bu_n\pmod d\) has exactly \(h_n\) solutions if \(h_n\mid bu_n\), otherwise none. The zeta function follows by decomposing this explicit permutation into cycles. These statements hold uniformly even when the twisted ambient projective line is identified with the standard line using a non-rational conjugating matrix.

## Verification
The standalone `checker.py` uses only Python's standard library. Execute `python3 checker.py`. It tests the characteristic-\(p\) polynomial identity for nine eligible prime-power cases, enumerates all twisted-conjugacy classes of the finite dihedral group for a family of field sizes, compares predicted automorphism stabilizers, and independently counts fixed points of the affine Frobenius permutations for extension degrees one through eight. It also checks that the two explicit rational Möbius generators in the other exceptional geometric case generate a group of order six. These finite tests are not used as a substitute for the uniform algebraic proof above.

## Relationship to prior work
Tafazolian and Top (arXiv:2611.05096v1) determine the geometric projective symmetry group of the Chebyshev root set and give its Cayley-coordinate dihedral model. The present result takes that geometric theorem as a premise but classifies every finite-field form of the projective divisor, its rational automorphism group and its complete Frobenius point-count sequence. Their earlier work (arXiv:2505.01216v1) treats the different plane curves given by \(y^d=\varphi_d(x)\), with geometric automorphism groups, rather than finite-field forms of this unordered branch divisor. The Galois-cohomological method of classifying twists is classical, as illustrated by Meagher and Top (2010); no new general cohomological formalism is asserted here.

## Limitations
This is a classification only for the dihedral exceptional degrees \(2d=p^r+1\), not the unrelated exceptional \(S_3\) degrees or ordinary degrees. It says nothing about descent of automorphisms of curves covering \(\mathbb P^1\), nor about Jacobians, and does not construct explicit coefficient equations for every twisted divisor. The use of previously known geometric stabilizer classification means the arithmetic theorem is conditional on that established result. Publication-priority uncertainty remains for any unindexed computation of the same arithmetic forms. No independent mathematical audit has been performed.

## References
1. S. Tafazolian and J. Top, *Projective Symmetries of Chebyshev Polynomials*, arXiv:2611.05096v1 (first posted 3 November 2026), https://arxiv.org/html/2611.05096v1 .
2. S. Tafazolian and J. Top, *Automorphisms of Plane Curves defined from Chebychev polynomials*, arXiv:2505.01216v1 (2 May 2025), https://arxiv.org/html/2505.01216v1 .
3. S. Meagher and J. Top, *Twists of genus three curves over finite fields*, Finite Fields Appl. 16 (2010), 347–368, https://doi.org/10.1016/j.ffa.2010.06.001 .
