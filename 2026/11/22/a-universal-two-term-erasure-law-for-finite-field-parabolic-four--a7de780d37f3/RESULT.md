# A universal two-term erasure law for finite-field parabolic Fourier projections

## Finding

Let \(q\) be an odd prime power, \(\mathbb F_q\) its field, and \(B\subset\mathbb F_q\) a set of \(h\) distinct parameters. Write
\[
P_B=\{(t,t^2):t\in\mathbb F_q\setminus B\}\subset\mathbb F_q^2.
\]
For a nontrivial additive character \(\psi\) of \(\mathbb F_q\), define the one-dimensional deletion spectrum
\[
E_B(a)=\sum_{t\in B}\psi(at),\qquad
D_q(B)=\sum_{a\in\mathbb F_q\setminus\{0\}}|E_B(a)|-h.
\]
Let \(\Pi_{P_B}\) be the Fourier multiplier \(\widehat{\Pi_{P_B}f}=1_{P_B}\widehat f\) on \(\ell^\infty(\mathbb F_q^2)\), using normalized Fourier inversion. Then there is an absolute constant \(C\) such that, whenever \(1\le h<q\) and \(q\ge16h^2\),
\[
\boxed{\left|\|\Pi_{P_B}\|_{\infty\to\infty}
-\left[\frac1q+\left(1-\frac1q\right)\sqrt q
-\frac{3h}{4\sqrt q}+\frac{D_q(B)}{q^2}\right]\right|
\le \frac{C h^4}{q^{3/2}}.}
\]
The bound is uniform in the field, its characteristic, the character, and the positions of the erased points. For every fixed \(h\), the universal leading decrease in the sharp Fourier-algebra/projection norm is \(3h/(4\sqrt q)\). The entire order-\(q^{-1}\) effect is the one-dimensional Fourier \(\ell^1\) profile of the erased parameter set.

For \(B=\{u,v\}\) with \(u\ne v\), and with \(p\) the characteristic of \(\mathbb F_q\), an explicit arithmetic specialization is
\[
\boxed{\|\Pi_{P_B}\|_{\infty\to\infty}
=\frac1q+\left(1-\frac1q\right)\sqrt q
-\frac{3}{2\sqrt q}
+\frac{2}{p\sin(\pi/(2p))}\frac1q
+O(q^{-3/2}).}
\]
The error is absolute in this two-point specialization as \(q\to\infty\), and the coefficient \(2/[p\sin(\pi/(2p))]\) tends to \(4/\pi\) as \(p\to\infty\). Thus the first correction is universal, while the next detects the field characteristic. For one erasure, \(D_q(B)=q-2\). For three or more erasures, \(D_q(B)\) can additionally distinguish the geometry of the deleted parameter set.

## Assumptions and scope

The finite field has odd characteristic; no primality assumption on its order is imposed. The cardinality \(h\) may vary with \(q\) subject to \(q\ge16h^2\). The big-O form is only used with a uniform bound in terms of \(h\), not as a statement about arbitrary macroscopic deletions. The multiplier acts on complex functions, with the group \(\mathbb F_q^2\) carrying counting measure; its convolution kernel uses factor \(q^{-2}\). The sharp operator norm is the \(\ell^1\) mass of that kernel. All statements are deterministic and hold for every choice of the character.

## Proof

**1. Exact operator reduction and the un-erased norm.** Put
\[
G(a,b)=\sum_{t\in\mathbb F_q}\psi(at+bt^2),\qquad
E(a,b)=\sum_{t\in B}\psi(at+bt^2).
\]
Translation invariance and choice of the conjugate sign pattern at one output site give the sharp identity
\[
\|\Pi_{P_B}\|_{\infty\to\infty}
=\frac1{q^2}\sum_{a,b\in\mathbb F_q}|G(a,b)-E(a,b)|.
\]
For \(b=0\), \(G(a,0)=q\mathbf1_{\{a=0\}}\). For \(b\ne0\), completing the square and character orthogonality give \(|G(a,b)|=\sqrt q\). Consequently, the un-erased norm equals
\[
L_q=\frac1q+\left(1-\frac1q\right)\sqrt q.
\]
The entire contribution of the \(b=0\) slice, relative to its un-erased contribution, is *exactly*
\[
\sum_a|G(a,0)-E(a,0)|-q
=\sum_{a\ne0}|E(a,0)|-h=D_q(B),
\]
because \(E(0,0)=h<q\).

**2. The two identities controlling the perturbation.** On \(b\ne0\), put \(\zeta(a,b)=G(a,b)/\sqrt q\) and \(u(a,b)=E(a,b)\overline{\zeta(a,b)}\). Thus \(|\zeta|=1\) and \(|u|\le h\). Character orthogonality proves
\[
\sum_{a,b\ne0}\operatorname{Re}u(a,b)
=\frac{h q(q-1)}{\sqrt q},
\qquad
\sum_{a,b\ne0}\bigl(|u|^2-(\operatorname{Re}u)^2\bigr)
=\frac{h q(q-h)}2.
\]
For the first equality, expand \(E\overline G\) as a sum indexed by one erased parameter and one unrestricted parameter. Summing over \((a,b)\) forces those parameters to agree; removing the \(b=0\) slice leaves \(h q(q-1)\). For the second, orthogonality gives \(\sum_{a,b\ne0}|E|^2=h q(q-1)\). It also gives
\[
\sum_{a,b\ne0} E(a,b)^2\overline{G(a,b)}^2=q^2(h^2-h).
\]
Indeed, equality of both the sum and the sum of squares of two parameters in odd characteristic forces equality of their *unordered* pairs. For two erased parameters there are \(2h^2-h\) such unrestricted pairings. Removing the \(b=0\) contribution \(q^2h^2\) produces the displayed identity. Dividing by \(q\) and using \((\operatorname{Re}u)^2=(|u|^2+\operatorname{Re}(u^2))/2\) completes the second equality.

**3. Uniform control of the cubic term.** Write \(x=\operatorname{Re}u\) and \(y^2=|u|^2\). Since \(q\ge16h^2\), Taylor expansion with an absolute remainder bound gives
\[
|G-E|=\sqrt q-x+\frac{y^2-x^2}{2\sqrt q}
+\frac{x(y^2-x^2)}{2q}
+O\!\left(\frac{h^4}{q^{3/2}}\right).
\]
The cubic sum is smaller than a pointwise bound suggests. The identity \(x(y^2-x^2)=(\operatorname{Re}(u|u|^2)-\operatorname{Re}(u^3))/4\) reduces it to two character correlations. Orthogonality shows
\[
\sum_{a,b\in\mathbb F_q}E|E|^2\overline G=q^2(2h^2-h).
\]
This follows because \(r-s+t=w\) and \(r^2-s^2+t^2=w^2\) imply \((r-s)(t-s)=0\). The omitted \(b=0\) term is \(qh^3\), hence \(\sum_{a,b\ne0}u|u|^2=O(h^3q^{3/2})\). Also
\[
\sum_{a,b\in\mathbb F_q}E^3\overline{G}^3=q^2 N_3,
\]
where \(N_3\) counts two triples with equal sums and equal squared sums, the first lying in \(B^3\). After choosing its three coordinates and one unrestricted coordinate of the second triple, the remaining two solve a quadratic equation; therefore \(N_3\le2h^3q\). Removing the \(b=0\) term \(q^3h^3\) and dividing by \(q^{3/2}\) gives \(\sum_{a,b\ne0}u^3=O(h^3q^{3/2})\). Thus the normalized total cubic contribution is \(O(h^3q^{-3/2})\); the normalized fourth-order Taylor remainder is \(O(h^4q^{-3/2})\).

**4. Assemble the expansion.** Summing the constant, linear, and quadratic terms over \(b\ne0\), dividing by \(q^2\), and adding the exact \(b=0\) contribution yields
\[
\|\Pi_{P_B}\|_{\infty\to\infty}
=L_q+\frac{D_q(B)}{q^2}
-\frac{h(q-1)}{q\sqrt q}
+\frac{h(q-h)}{4q\sqrt q}
+O\!\left(\frac{h^4}{q^{3/2}}\right).
\]
The last two explicit terms equal \(-3h/(4\sqrt q)+O(h^2q^{-3/2})\), proving the theorem.

**5. Two deleted points.** If \(B=\{u,v\}\) with \(u\ne v\), character surjectivity onto the \(p\)-th roots and uniform fiber sizes give
\[
\frac1q\sum_{a\in\mathbb F_q}|E_B(a)|
=\frac2p\sum_{j=0}^{p-1}|\cos(\pi j/p)|
=\frac{2}{p\sin(\pi/(2p))}.
\]
The last equality is a finite cosine sum for odd \(p\). Removing \(a=0\), where \(|E_B(0)|=2\), gives \(D_q(B)=2q/[p\sin(\pi/(2p))]-4\). Substitution proves the specialization.

## Verification

The standalone \(\texttt{verify_erasure.py}\) evaluates the *complete* Fourier kernel by direct finite summation on 45 prime-field configurations and three configurations over the extension field \(\mathbb F_9\). In every case both exact moment identities in Step 2 agree with direct complex summation. The script also computes the two-term approximation and the residual multiplied by \(q^{3/2}\); these are diagnostic finite tests, not a replacement for the uniform proof. No external packages are needed. Execute \(\texttt{python3 verify_erasure.py}\).

## Relationship to prior work

Iosevich, Li and Yu (arXiv:2609.25404, first public 2026-09-21) define the finite Fourier algebra norm and explicitly evaluate the *complete* finite-field parabola by the quadratic Gauss-sum magnitude (Sections 2 and 5). The exact affine-transitive synthesis theorem in Section 4 does not determine punctured-parabola projection norms, because erasures destroy transitivity. Their results motivate measuring precisely how a small deletion changes the otherwise flat nonvertical Fourier magnitudes. Bhowmik, Deodhar and Iosevich (arXiv:2508.12194, first public 2025-08-17) give general finite-group synthesis inequalities and support-based bounds, rather than this two-term expansion. The analysis of incomplete Gauss-sum distributions by Akarsu and Marklof (2013) concerns long incomplete intervals and does not supply this fixed-erasure, fully averaged projection formula. Related sharp finite-field conic erasure studies optimize fourth-power extension norms, not the endpoint Fourier projection norm. No claim of exhaustive bibliographic uniqueness is made.

## Limitations

The theorem is asymptotic with a uniform error bound, **not** an exact closed formula for the finite-size punctured norm. The condition \(q\ge16h^2\) is sufficient to control a Taylor expansion and is not asserted necessary. The result does not cover characteristic two, deletions proportional to the field order, arbitrary curves, or arbitrary Fourier multipliers. The error term may hide finer geometry-dependent effects at order \(q^{-3/2}\). An older equivalent fixed-erasure character-sum expansion is a residual literature risk.

## References

- A. Iosevich, Z. Li, K. Yu, *Spectral synthesis with the complexity parameter in* \(\mathbb Z_N^d\), arXiv:2609.25404 (v1 2026-09-21), https://arxiv.org/abs/2609.25404.
- P. Bhowmik, S. Deodhar, A. Iosevich, *On spectral synthesis in* \(\mathbb Z_N^d\), arXiv:2508.12194 (v1 2025-08-17), https://arxiv.org/abs/2508.12194.
- E. Demirci Akarsu, J. Marklof, *The value distribution of incomplete Gauss sums*, Mathematika 2013, https://www.cambridge.org/core/journals/mathematika/article/abs/value-distribution-of-incomplete-gauss-sums/9FBFB8DBAD3593290570B5E9DBE10991.
