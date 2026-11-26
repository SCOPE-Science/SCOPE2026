# The characteristic-two chordal cubic has a non-split canonical singular ribbon

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). In \(\mathbb P^4_k\) with homogeneous coordinates \([x_0:x_1:x_2:x_3:x_4]\), put
\[
X=V(F),\qquad
F=\det\begin{pmatrix}x_0&x_1&x_2\\x_1&x_2&x_3\\x_2&x_3&x_4\end{pmatrix}.
\]
This is the coefficientwise characteristic-two realization of the classical chordal cubic, namely the secant cubic of the rational normal quartic. Let \(J=\operatorname{Sing}(X)\) be the **scheme-theoretic** Jacobian singular locus, not just its reduction.

**Theorem.** The scheme \(J\) is a non-split ribbon supported on the rational normal quartic \(C\cong\mathbb P^1\). More precisely,
\[
J=V(q_0,q_2,q_4),\quad
q_0=x_2x_4+x_3^2,\quad q_2=x_0x_4+x_2^2,\quad q_4=x_0x_2+x_1^2.
\]
The three quadrics form a regular sequence: \(J\) is a projective complete intersection of type \((2,2,2)\), with degree \(8\), arithmetic genus \(5\), and dualizing line bundle \(\omega_J\cong\mathcal O_J(1)\). The nilradical \(\mathcal N\) has
\[
\mathcal N^2=0,\qquad \mathcal N\cong\mathcal O_{\mathbb P^1}(-6),
\]
and the square-zero extension \(\mathcal O_J\to\mathcal O_C\) has **no algebra section**. Thus \(J\) is not isomorphic, even abstractly, to the split ribbon \(\underline{\operatorname{Spec}}_C(\mathcal O_C\oplus\mathcal O_C(-6))\). Its Hilbert polynomial in the given projective embedding is \(8n-4\), and the embedding is given by the complete canonical system.

## Assumptions and scope
The field is arbitrary algebraically closed of characteristic exactly \(2\). The cubic is defined by the displayed coefficientwise Hankel determinant; no divisibility or genericity conditions on parameters arise. The word *singular locus* denotes the closed subscheme cut out by the equation and all partial derivatives in projective space. A ribbon means a double structure on a smooth curve with invertible square-zero nilradical. Non-split means that the reduction morphism has no scheme-theoretic retraction, or equivalently that the quotient of structure sheaves has no multiplicative section.

## Proof
**1. The exact Jacobian ideal.** In characteristic two the determinant is
\[
F=x_0x_2x_4+x_0x_3^2+x_1^2x_4+x_2^3.
\]
Its five partial derivatives, ordered by coordinate, are \((q_0,0,q_2,0,q_4)\). Euler's identity gives
\[
F=x_0q_0+x_2q_2+x_4q_4,
\]
so the projective Jacobian ideal is exactly \((q_0,q_2,q_4)\).

**2. Two exhaustive affine charts.** No projective geometric point of \(J\) has both \(x_0=x_4=0\): the three quadrics would successively force \(x_2=x_3=x_1=0\). On \(x_0=1\), put \(t=x_1\) and \(u=x_3+t^3\). The equations yield \(x_2=t^2\), \(x_4=t^4\) and \(u^2=0\); hence
\[
J\cap\{x_0\ne0\}\cong\operatorname{Spec}k[t,u]/(u^2),\quad
[x_0:x_1:x_2:x_3:x_4]=[1:t:t^2:t^3+u:t^4].
\]
Similarly, on \(x_4=1\), put \(s=x_3\) and \(v=x_1+s^3\). Then
\[
J\cap\{x_4\ne0\}\cong\operatorname{Spec}k[s,v]/(v^2),\quad
[x_0:x_1:x_2:x_3:x_4]=[s^4:s^3+v:s^2:s:1].
\]
These presentations are isomorphisms of rings, not merely equations on closed points. Setting the square-zero coordinates to zero gives precisely the degree-four Veronese curve on both charts. Thus the reduction of \(J\) is \(C=\nu_4(\mathbb P^1)\), and \(J\) is a ribbon.

**3. Global gluing.** On the overlap \(t\ne0\), the first chart has \(x_4=t^4\). Dividing by \(x_4\) and using \(u^2=0\) gives the exact transitions
\[
s=t^{-1}+t^{-4}u,\qquad v=t^{-6}u.
\]
The second identity identifies the line-bundle transition of the nilradical as that of \(\mathcal O_{\mathbb P^1}(-6)\).

**4. The extension does not split.** Suppose a scheme-theoretic retraction \(J\to C\) existed. Its induced algebra section would lift the standard coordinates to \(t+f(t)u\) on the first chart and \(s+g(s)v\) on the second, for polynomials \(f\in k[t]\), \(g\in k[s]\). Their compatibility with \(s=t^{-1}\) on \(C\), using the transitions, requires
\[
t^{-4}+t^{-6}g(t^{-1})=t^{-2}f(t),\quad\text{hence}\quad
t^2+g(t^{-1})=t^4f(t).
\]
The Laurent coefficient of \(t^2\) on the left is \(1\), whereas the right has only degrees at least \(4\). This contradiction proves nonsplitting. Concretely the obstruction is represented by the nonzero class of \(t^2\) in \(k[t,t^{-1}]/(k[t^{-1}]+t^4k[t])\).

**5. Complete-intersection and canonical invariants.** Since the common reduced support is the quartic curve of dimension \(1\) in \(\mathbb P^4\), the three homogeneous quadrics have codimension \(3\). In the Cohen--Macaulay polynomial ring they form a regular sequence. Thus \(J\) is a complete intersection of type \((2,2,2)\), with degree \(2\cdot2\cdot2=8\), and adjunction gives \(\omega_J=\mathcal O_J(2+2+2-5)=\mathcal O_J(1)\). The short exact sequence
\[
0\to\mathcal O_{\mathbb P^1}(-6)\to\mathcal O_J\to\mathcal O_{\mathbb P^1}\to0
\]
shows \(\chi(\mathcal O_J)=(-5)+1=-4\), hence \(p_a(J)=5\). Twisting by \(\mathcal O_J(n)\), which restricts to \(\mathcal O_{\mathbb P^1}(4n)\), gives Hilbert polynomial \((4n-5)+(4n+1)=8n-4\). The regular sequence has no linear equations, and the complete-intersection resolution gives \(h^0(J,\mathcal O_J(1))=5\); the given embedding is the complete canonical embedding.

## Verification
The included `verification/verify.py` uses only the Python standard library and exact arithmetic over \(\mathbb F_2\). It independently expands the determinant and all derivatives, checks Euler containment, verifies the two local coordinate descriptions and Laurent transition, certifies the impossible Laurent-degree gap used in the nonsplitting proof, and checks the complete-intersection Hilbert polynomial. Execute `python3 verification/verify.py`. The observed output is stored in `verification/output.txt`. The abstract regular-sequence argument and impossibility for polynomials of all degrees are proved above, not inferred from finite tests.

## Relationship to prior work
Kanev (arXiv:math/9804141, first posted April 30, 1998) studies chordal Veronese varieties and catalecticant equations, explicitly under characteristic-zero hypotheses. Raicu (arXiv:1011.1564, first posted November 6, 2010) displays this precise Hankel matrix and secant cubic, and proves higher-dimensional catalecticant ideal identities in characteristic zero. Casalaina-Martin--Laza (arXiv:0710.5329) describe the chordal cubic as a degeneration of complex cubic threefolds. Bayer--Eisenbud develop the general theory and canonical embeddings of ribbons. None of these cited statements gives this characteristic-two Jacobian ideal, its nilradical transition, or its nonsplitting. The canonical-ribbon framework and the chordal cubic itself are established prior work; the finding is their explicit scheme-theoretic connection in characteristic two.

## Limitations
The result concerns the specified cubic hypersurface and its intrinsic Jacobian singular scheme, not every determinantal cubic or an arbitrary embedded ribbon. The proof does not classify deformations or embedded Hilbert components. Primary literature checked is strongly relevant but does not exhaust historical sources; the priority assessment is provisional. Verification code checks algebraic identities and finite Hilbert-function values, while general facts are established by the mathematical argument. No independent mathematical audit has been performed.

## References
1. V. Kanev, *Chordal varieties of Veronese varieties and catalecticant matrices*, arXiv:math/9804141v1 (1998-04-30), https://arxiv.org/abs/math/9804141.
2. C. Raicu, *3x3 Minors of Catalecticants*, arXiv:1011.1564v1 (2010-11-06), https://arxiv.org/abs/1011.1564.
3. S. Casalaina-Martin and R. Laza, *The moduli space of cubic threefolds via degenerations of the intermediate Jacobian*, arXiv:0710.5329v1 (2007-10-29), https://arxiv.org/abs/0710.5329.
4. D. Bayer and D. Eisenbud, *Ribbons and Their Canonical Embeddings*, Trans. Amer. Math. Soc. 347 (1995), DOI:10.2307/2154871; open manuscript https://www.math.columbia.edu/~bayer/papers/Ribbons_BE95.pdf.
