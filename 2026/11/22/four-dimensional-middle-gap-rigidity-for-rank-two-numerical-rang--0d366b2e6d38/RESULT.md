# Four-dimensional middle-gap rigidity for rank-two numerical ranges

## Finding

**Theorem (exact middle-gap rigidity).** Let \(A\in M_4(\mathbb C)\) be arbitrary and, for each real \(\theta\), set
\[
H(\theta)=\operatorname{Re}(e^{-i\theta}A)
=\frac{e^{-i\theta}A+e^{i\theta}A^*}{2},
\]
with its four real eigenvalues, counted with multiplicities, ordered as
\(\lambda_1(\theta)\ge\lambda_2(\theta)\ge\lambda_3(\theta)\ge\lambda_4(\theta)\).
Suppose there is a fixed \(d>0\) such that for **every** \(\theta\in\mathbb R\),
\[
\lambda_2(\theta)-\lambda_3(\theta)=d.
\]
Then there is a unique \(c\in\mathbb C\) such that for every real \(\theta\),
\[
\boxed{\lambda_2(\theta)=\operatorname{Re}(e^{-i\theta}c)+d/2,\qquad
\lambda_3(\theta)=\operatorname{Re}(e^{-i\theta}c)-d/2.}
\]
In particular, the rank-two numerical range
\[
\Lambda_2(A)=\{z\in\mathbb C:\;V^*AV=zI_2\text{ for some }V\in M_{4,2}(\mathbb C),\ V^*V=I_2\}
\]
is exactly the closed disk
\[
\boxed{\Lambda_2(A)=\{z\in\mathbb C:|z-c|\le d/2\}.}
\]
Moreover, writing \(X=\operatorname{Re}A\), \(Y=\operatorname{Im}A\) and \(c=\alpha+i\beta\), the polynomial
\[
\det(tI_4-xX-yY)\in\mathbb R[x,y,t]
\]
is divisible by the *circular quadratic*
\[
\boxed{(t-\alpha x-\beta y)^2-\frac{d^2}{4}(x^2+y^2).}
\]
These conclusions need no normality, reducibility, simplicity, or genericity hypothesis on \(A\).

The hypothesis is nonvacuous: for any \(c\in\mathbb C\) and \(d>0\), the block diagonal matrix consisting of two copies of \(\begin{psmallmatrix}c&d\\0&c\end{psmallmatrix}\) has middle eigenvalues \(\operatorname{Re}(e^{-i\theta}c)\pm d/2\) for all directions. The theorem does **not** claim that every circular rank-two numerical range has constant raw middle gap.

## Assumptions and scope

The matrix size is exactly four, and the hypothesis concerns the **raw ordered spectral gap** of the Hermitian pencil, not the actual directional width of \(\Lambda_2(A)\). For higher-rank numerical ranges the two quantities are different in general: the inequalities defining the range need not all be active. The gap \(d\) is strictly positive and uniform in every direction; no conclusion is asserted for a varying gap or the degenerate case \(d=0\). All identities are exact in finite-dimensional complex linear algebra.

## Proof

**1. An algebraic common divisor.** Introduce a Laurent variable \(z\) and the field and ring
\[
R=\mathbb C[z,z^{-1}],\qquad K=\mathbb C(z),\qquad
\mathcal H(z)=\tfrac12(z^{-1}A+zA^*),
\]
and put \(Q(t,z)=\det(tI_4-\mathcal H(z))\in R[t]\). Both \(Q(t,z)\) and \(Q(t+d,z)\) are monic polynomials of degree four in \(t\).
For each \(|z|=1\), the number \(\lambda_3\) is a root of the first polynomial and \(\lambda_3+d=\lambda_2\) is a root of the second. Hence their Sylvester resultant, a Laurent polynomial in \(z\), vanishes at every unit-modulus \(z\). It is identically zero. Therefore the monic greatest common divisor
\[
g(t,z)=\gcd_{K[t]}(Q(t,z),Q(t+d,z))
=t^k+\gamma_{k-1}(z)t^{k-1}+\cdots
\]
has some fixed degree \(1\le k\le4\) and coefficients in \(K\).

**2. All common-divisor roots have a discrete location relative to the middle gap.** Write \(Q=gu\), \(Q(t+d,z)=gv\) over \(K[t]\). Outside a finite set of unit-modulus values at which coefficients of these factorizations have poles, their specializations are valid monic factorizations. Thus every root \(r\) of the specialized polynomial \(g\), counted with multiplicity, satisfies \(r,r+d\in\sigma(\mathcal H(z))\). It cannot be \(\lambda_1\), because \(r+d\) would exceed the maximum eigenvalue. If \(r=\lambda_3\), its value is known. If \(r=\lambda_2\), it equals \(\lambda_3+d\). If \(r=\lambda_4\), then \(r+d\) is one of \(\lambda_1,\lambda_2,\lambda_3\); because \(r\le\lambda_3\) and \(\lambda_2=\lambda_3+d\), this forces \(r\in\{\lambda_3-d,\lambda_3\}\). Consequently, every root belongs to
\[
\{\lambda_3-d,\lambda_3,\lambda_3+d\}.
\]
This elementary four-eigenvalue restriction is the key difference from higher dimensions: additional interior eigenvalues may support a second, unrelated pair separated by \(d\).

Set \(s(z)=-\gamma_{k-1}(z)/k\), the mean of the roots of \(g\). On any connected pole-free open arc, \(s(e^{i\theta})-\lambda_3(\theta)\) is continuous and takes values in the finite set \(\{jd/k:-k\le j\le k,\ j\in\mathbb Z\}\). It is therefore constant on that arc. Fix such an arc and call the constant \(\delta\). The rational function \(a(z)=s(z)-\delta\in K\) then equals \(\lambda_3\) throughout that arc. Therefore the rational functions \(Q(a(z),z)\) and \(Q(a(z)+d,z)\) vanish at infinitely many points and vanish identically in \(K\):
\[
Q(a(z),z)=Q(a(z)+d,z)=0.
\]

**3. The rational root is a first-degree Laurent polynomial.** Since \(a\in K\) is a root of monic \(Q\in R[t]\), it lies in \(R\). For completeness, write \(a=B/C\) in lowest terms with \(B,C\in\mathbb C[z]\). Multiplying \(Q(B/C,z)=0\) by \(C^4\) and a suitable power of \(z\) shows that every nonzero root of \(C\) must also be a root of \(B\), impossible. Hence \(C\) is a monomial times a nonzero constant, so \(a\in R\).

Writing
\(Q(t,z)=t^4+\sum_{j=1}^{4}q_j(z)t^{4-j}\), each \(q_j\) has Laurent exponents between \(-j\) and \(j\), as follows from its expression as sums of \(j\)-by-\(j\) principal minors of \(\mathcal H(z)\). If the highest nonzero Laurent exponent of \(a\) were \(m>1\), the term \(a^4\) in \(Q(a,z)\) would have a nonzero coefficient at exponent \(4m\), whereas each \(q_j a^{4-j}\) has exponent at most \(j+(4-j)m<4m\); impossible. Similarly, the lowest exponent cannot be less than \(-1\). Therefore
\[
a(z)=b_{-1}z^{-1}+b_0+b_1z.
\]

**4. No eigenvalue-branch switching.** The two rational identities above show that, on the *entire* unit circle, both \(a(e^{i\theta})\) and \(a(e^{i\theta})+d\) are real eigenvalues of \(H(\theta)\). Consider the closed set \(E=\{\theta\pmod{2\pi}:a(e^{i\theta})=\lambda_3(\theta)\}\), which contains the chosen open arc. It is also open: at a point of \(E\), by continuity, on a small neighborhood \(|a-\lambda_3|<d/2\). If \(a>\lambda_3\), then \(a\) would be an eigenvalue strictly inside the forbidden interval \((\lambda_3,\lambda_2)\). If \(a<\lambda_3\), then \(a+d\) would be an eigenvalue in the same forbidden interval. Both are impossible. Since the circle is connected, \(E\) is the whole circle. Therefore \(a=\lambda_3\) and \(a+d=\lambda_2\) globally. This step rules out the otherwise possible danger of switching spectral branches at isolated degeneracies.

**5. Antipodal symmetry and disk geometry.** The relation \(H(\theta+\pi)=-H(\theta)\) gives \(\lambda_3(\theta+\pi)=-\lambda_2(\theta)=-\lambda_3(\theta)-d\). Substituting the Laurent formula for \(a\), this shows \(b_0=-d/2\). The function \(a(e^{i\theta})\) is real everywhere, so \(b_{-1}=\overline{b_1}\). Hence, for the unique \(c=2b_{-1}\),
\[
\lambda_3(\theta)=\operatorname{Re}(e^{-i\theta}c)-d/2,
\qquad\lambda_2(\theta)=\operatorname{Re}(e^{-i\theta}c)+d/2.
\]
The Li–Sze half-plane representation of the rank-two numerical range now gives
\[
\Lambda_2(A)=\bigcap_{\theta\in[0,2\pi)}
\{w\in\mathbb C:\operatorname{Re}(e^{-i\theta}w)\le\lambda_2(\theta)\}
=\overline{B}(c,d/2).
\]
Finally the two roots \(\operatorname{Re}(e^{-i\theta}c)\pm d/2\) of \(Q\) show, after replacing \((\cos\theta,\sin\theta)\) by an arbitrary nonzero real \((x,y)\) and rescaling, that the claimed circular quadratic divides the homogeneous characteristic polynomial over \(\mathbb R[x,y,t]\). Indeed polynomial division by the proposed monic quadratic has a remainder linear in \(t\); the two distinct roots annihilate that remainder for every \((x,y)\ne(0,0)\), so both remainder coefficients vanish identically. This completes the proof.

## Verification

The proof uses only exact polynomial/resultant identities, ordered Hermitian eigenvalues, and a standard half-plane formula. Its crucial finite-dimensional comparison is explicit: for a four-eigenvalue spectrum with positive middle gap \(d\), every pair of eigenvalues at separation \(d\) begins at one of just three positions relative to \(\lambda_3\). The proof of global equality additionally handles multiplicities, isolated crossings and poles of rational factors. No numerical search or finite enumeration is used to certify the theorem.

For a direct nonvacuous witness, take \(A=J_d\oplus J_d\) with \(J_d=\begin{psmallmatrix}0&d\\0&0\end{psmallmatrix}\). Its Hermitian pencil has eigenvalues \(d/2,d/2,-d/2,-d/2\) in every direction; thus \(\Lambda_2(A)=\overline B(0,d/2)\), and its determinant pencil is \((t^2-(d^2/4)(x^2+y^2))^2\).

## Relationship to prior work

Muyan Jiang, *A proof of the constant-width numerical range conjecture* (arXiv:2611.13461v1, first public version 10 November 2026), proves disk rigidity when the **extreme** eigenvalue gap \(\lambda_1-\lambda_n\) of a finite Hermitian pencil is direction-independent. His resultant and rational-root argument motivates steps 1 and 3, which are explicitly credited rather than claimed anew. The new issue is the **middle** gap: the gcd may have several roots at different eigenvalue positions, and the proof above uses the four-eigenvalue discrete-offset restriction and the no-switching argument to recover the middle ordered eigenvalues.

Chien, Li and Nakazato, *The diameter and width of higher rank numerical ranges* (published online 3 January 2020; journal volume 2021), give the Li–Sze framework and a six-dimensional example with \(\lambda_2-\lambda_5\) constant in direction but noncircular rank-two numerical range. That example shows why arbitrary-dimensional extrapolation from the current claim is false. Pei Yuan Wu's *Numerical ranges as circular discs* (2011) addresses ordinary numerical ranges and circular arcs, not the four-dimensional middle gap. A previous exact computation for direct sums of two Jordan blocks treats a special family and does not imply the present universal assertion for all complex four-by-four matrices.

## Limitations

Only the forward implication from a **constant positive middle spectral gap** is proved; the actual geometric width of a rank-two numerical range need not equal that gap. The result does not solve the general constant-width conjecture for higher-rank numerical ranges, does not extend to all matrix sizes, and does not classify matrices up to unitary similarity. The determinant factor follows from, but is not asserted to characterize, the spectral-gap hypothesis. Bibliographic searches do not exclude every older implicit algebraic formulation. Independent mathematical validation has not been performed.

## References

1. M. Jiang, *A proof of the constant-width numerical range conjecture*, arXiv:2611.13461v1 (10 November 2026), https://arxiv.org/html/2611.13461v1.
2. M.-T. Chien, C.-K. Li, H. Nakazato, *The diameter and width of higher rank numerical ranges*, Linear and Multilinear Algebra **69** (2021), 871–887, https://cklixx.people.wm.edu/diameter.pdf, DOI:10.1080/03081087.2019.1710105.
3. P. Y. Wu, *Numerical ranges as circular discs*, Applied Mathematics Letters **24** (2011), 2115–2117, DOI:10.1016/j.aml.2011.06.010, https://ir.lib.nycu.edu.tw/server/api/core/bitstreams/59e3168b-f81b-4ba8-b814-9e513a064ab3/content.
4. C.-K. Li and N.-S. Sze, *Canonical forms, higher rank numerical ranges, totally isotropic subspaces, and matrix equations*, Proceedings of the American Mathematical Society **136** (2008), 3013–3023 (half-plane characterization, as quoted in Reference 2).
