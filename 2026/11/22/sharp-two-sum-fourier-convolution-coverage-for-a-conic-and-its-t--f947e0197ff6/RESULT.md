# Sharp two-sum Fourier-convolution coverage for a conic and its tangent

## Finding

For every odd prime power \(q\), choose a nonsquare \(d\in\mathbb F_q^\times\). In the additive group \(G=\mathbb F_q^2\), consider the anisotropic conic and one tangent line
\[
C=\{(u,v):u^2-dv^2=1\},\qquad L=\{(1,v):v\in\mathbb F_q\},\qquad S=C\cup L.
\]
Here \(L\) is tangent to \(C\) at \((1,0)\), and \(|S|=2q\). Let \(\chi\) be the quadratic character of \(\mathbb F_q\), extended by \(\chi(0)=0\). Define
\[
A=\{a\in\mathbb F_q:\chi(a(a-2))=1\},\qquad
H_a(b)=(a^2-db^2)(a^2-db^2-4).
\]
The exact zero locus of the unnormalized additive convolution \(\mathbf1_S*\mathbf1_S\) is
\[
\boxed{\{(a,b)\in G:(\mathbf1_S*\mathbf1_S)(a,b)=0\}
=\{(a,b):a\in A,\ \chi(H_a(b))=1\}.}
\]
In particular, with \(M_q=q^2-|S+S|\), one has \(|A|=(q-3)/2\) and the explicit uniform estimate
\[
\boxed{\left|M_q-\frac{q(q-3)}4\right|
\le\frac{q-3}{2}\left(\sqrt q+\frac32\right).}
\]
Thus \(|S+S|/q^2=3/4+O(q^{-1/2})\), and there is a sharp finite coverage threshold:
\[
\boxed{S+S=G\quad\Longleftrightarrow\quad q\in\{3,5\}.}
\]
For the first two failure orders, \(M_7=4\) and \(M_9=12\). Every nonsingular anisotropic affine conic and any of its rational tangent lines have the same sumset cardinality after an affine coordinate change.

The result is Fourier-analytic: for the unitary transform \(\widehat f(\xi)=q^{-1}\sum_{x\in G}f(x)\psi(-\langle x,\xi\rangle)\) (with any fixed nontrivial additive character composed with the field trace), \(\widehat{\mathbf1_S*\mathbf1_S}=q\widehat{\mathbf1_S}^{\,2}\). The displayed locus is therefore the *entire* zero set of the inverse Fourier transform of the squared indicator spectrum, not just a numerical lower bound on its support.

## Assumptions and scope

All field characteristics are odd; \(q\) may be a nonprime prime power. A chosen nonsquare \(d\) gives the anisotropic norm \(N(a,b)=a^2-db^2\). Convolutions are unnormalized, so \((f*g)(z)=\sum_{x\in G}f(x)g(z-x)\). Additive sums are ordered when counted by a convolution and unordered when interpreted as a support set. The general estimate is uniform in \(q\) and \(d\). The elliptic-trace formulas below have no restriction on the characteristic other than oddness.

## Proof

**1. Exact pair-convolution formula.** Write \(e=(1,0)\), \(n=N(a,b)\), and \(r_{XY}=\mathbf1_X*\mathbf1_Y\). The three elementary convolutions are
\[
r_{CC}(a,b)=\begin{cases}q+1,&(a,b)=(0,0),\\1-\chi(n(n-4)),&(a,b)\ne(0,0),\end{cases}
\qquad
r_{CL}(a,b)=1-\chi(a(a-2)),\qquad
r_{LL}(a,b)=q\mathbf1_{a=2}.
\]
For the first, if \(s=(a,b)\ne0\), write the two conic summands as \(s/2\pm v\). Equality of their norms to one forces the polar inner product of \(s\) and \(v\) to vanish. Since \(N(s)\ne0\) (anisotropy), the orthogonal line is parametrized by \(v=t(db,a)\), whose norm is \(-d\,n\,t^2\). The equation becomes \(t^2=(n-4)/(4dn)\), giving \(1-\chi(n(n-4))\) solutions because \(\chi(d)=-1\). At the zero sum, the ordered pairs are \((x,-x)\) for all \(x\in C\), giving \(q+1\). For \(r_{CL}\), the conic summand must have first coordinate \(a-1\); the remaining equation \(dv^2=a(a-2)\) has exactly \(1-\chi(a(a-2))\) solutions. The line is a coset of a one-dimensional additive subgroup, so its self-convolution is \(q\) on the coset with first coordinate \(2\).

Since \(C\cap L=\{e\}\), \(\mathbf1_S=\mathbf1_C+\mathbf1_L-\delta_e\), and hence
\[
(\mathbf1_S*\mathbf1_S)(s)=r_{CC}(s)+2r_{CL}(s)
+(q-2)\mathbf1_{s_1=2}-2\mathbf1_C(s-e)+\mathbf1_{s=2e}.
\]
If \(\chi(a(a-2))\ne1\), at least one genuine mixed \(C+L\) representation exists, so the convolution is positive. If \(\chi(a(a-2))=1\), then \(a\notin\{0,2\}\), no mixed representation exists, and the intersection correction also vanishes: otherwise \(s=e+x\) with \(x\in C\) would be a mixed representation. Thus the convolution equals \(r_{CC}(s)\) in this case, and is zero exactly when \(\chi(n(n-4))=1\). This proves the boxed pointwise criterion, including its sign.

**2. Exact elliptic character formula.** The standard distinct-root quadratic-character identity gives \(\sum_a\chi(a(a-2))=-1\). Since two inputs give zero, it follows that \(|A|=(q-3)/2\). For \(a\in A\), define \(Z_a=\#\{b:H_a(b)=0\}\) and \(B_a=\sum_b\chi(H_a(b))\). Splitting values into \(-1,0,+1\) yields the exact count
\[
\boxed{M_q=\frac12\sum_{a\in A}(q-Z_a+B_a).}
\]
For \(a\ne-2\), the quartic \(H_a(b)\) is squarefree over an algebraic closure: \(a\notin\{0,2,-2\}\) and the two quadratic factors have disjoint roots. Its leading coefficient is \(d^2\), a square, so the smooth genus-one model \(E_a:y^2=H_a(b)\) has exactly two rational points at infinity. Writing \(t_a=q+1-\#E_a(\mathbb F_q)\), we have
\[
Z_a=1-\chi(a^2-4)\in\{0,2\},\qquad B_a=-1-t_a,\qquad |t_a|\le2\sqrt q.
\]
Consequently the exact fiber count is \((q-1-Z_a-t_a)/2\). If \(a=-2\), then \(a\in A\) precisely when \(\chi(2)=1\); the quartic has a double root at zero and must not be treated as genus one. Directly applying \(\sum_b\chi(4-db^2)=-\chi(-d)\) gives \(Z_{-2}=1\) and \(B_{-2}=-1+\chi(-1)\), hence \((q-2+\chi(-1))/2\) holes on this fiber. This also establishes an elliptic-trace evaluation with the unique singular-fiber correction.

**3. Density and the sharp threshold.** For every regular \(a\in A\), Hasse's bound and \(Z_a\le2\) yield
\[
\left|\frac{q-Z_a+B_a}{2}-\frac q2\right|
\le\sqrt q+\frac32.
\]
The exceptional \(a=-2\), when present, satisfies the same inequality by its explicit formula. Summing over \(|A|=(q-3)/2\) proves the uniform estimate.

For \(q\ge11\), there is a regular \(a\in A\), since \(|A|\ge4\) and at most one element is singular. Its number of missing sums is at least \((q-3-2\sqrt q)/2>0\). For the four smaller odd prime-power orders, exact field arithmetic gives the following fiber data, displayed as \((a,\#\{b:\chi(H_a(b))=1\})\): at \(q=3\), \(A\) is empty; at \(q=5\) with \(d=2\), the data are \((1,0)\); at \(q=7\) with \(d=3\), they are \((4,2),(5,2)\); and at \(q=9\) with \(\mathbb F_9=\mathbb F_3[\alpha]/(\alpha^2+1)\) and \(d=1+\alpha\), they are \((1,4),(1+\alpha,4),(1+2\alpha,4)\). The last entries use literal field elements, not integer reduction modulo nine. Each finite case is exhaustively reproducible by the standalone checker; the all-degree conclusion for \(q\ge11\) is the preceding proof, not finite extrapolation. These data establish the claimed exact threshold.

**4. Affine-conic invariance.** Every nonsingular affine conic with anisotropic quadratic part and a rational point can be centered and linearly transformed to \(N=1\), as its binary anisotropic quadratic form is a scalar multiple of the quadratic extension norm. Multiplication by a norm-one element moves the chosen rational tangency point to \((1,0)\). Such affine changes preserve cardinalities of sumsets (a translation translates the twofold sumset by twice its vector), so the same count holds for any rational tangent.

## Verification

A standalone Python program `conic_tangent_checker.py` independently constructs the field arithmetic, conic, tangent line, every ordered two-sum multiplicity and every predicted character value. It tests all \(q^2\) targets over \(q=3,5,7,9,11,13,17,19,25,27,49,81\), checking the convolution formula, exact zero locus, trace inequalities and sum counts. It reports missing counts \(0,0,4,12,14,26,50,76,112,138,514,1530\), respectively. The program is finite evidence only; the universal theorem is proved in the preceding section. No external certificate or independent verification is asserted.

## Relationship to prior work

Shi, Li, Xia, Helleseth and Özbudak study additive decompositions of the norm-one torus in characteristic three, including the torus-only two-summand criterion; that criterion is a relevant component, but their result does not include adding a tangent line or the resulting two-sum holes. Iosevich, Li and Yu relate finite Fourier synthesis to additive energy, doubling and Fourier moments, and analyze spheres and paraboloids, not this tangent-augmented anisotropic conic. Related published torus-only odd-characteristic additive-length and conic extension results also supply ingredients, but do not state the pointwise zero characterization, elliptic fiber formula, or sharp coverage threshold for this union. The novelty claim concerns the combined support and exact threshold, not the classical torus chord count or Hasse's theorem.

## Limitations

This result treats odd fields and anisotropic conics, not characteristic two or hyperbolic/split conics. The elliptic trace formula is explicit as a finite sum of traces, not simplified to one elementary polynomial in \(q\); the density estimate is uniform but its error exponent is not asserted optimal. The finite checks do not constitute an infinite-field proof. While no exact equivalent was identified in the inspected sources, older results on conic-plus-subspace sumsets or general character-sum families could imply some or all of the theorem; the bibliographic survey is not exhaustive.

## References

- Minjia Shi, Shitao Li, Yuhong Xia, Tor Helleseth and Ferruh Özbudak, *Norm-One Torus Decompositions and Decoding of Gashkov-Sidel'nikov Codes*, arXiv:2609.20402v1, first posted 2026-09-17, https://arxiv.org/abs/2609.20402. Especially Section 2.1 and Theorem 1.3.
- Alex Iosevich, Zhihe Li and Ke Yu, *Spectral synthesis with the complexity parameter in* \(\mathbb Z_N^d\), arXiv:2609.25404v1, first posted 2026-09-21, https://arxiv.org/html/2609.25404v2. Especially Sections 5.2 and 8.2.
- Hasse's elliptic curve point-count bound, in its standard form \(|q+1-\#E(\mathbb F_q)|\le2\sqrt q\) for smooth genus-one curves with a rational point.
