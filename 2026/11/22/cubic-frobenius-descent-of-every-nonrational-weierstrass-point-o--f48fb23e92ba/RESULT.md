# Cubic Frobenius descent of every nonrational Weierstrass point on the genus-19 maximal curve over \(\mathbb F_{121}\)

## Finding
Let \(X\) be the smooth projective model of
\[
 y^{12}+x^8+x^4=0
\]
over \(k=\mathbb F_{121}\). Write \(W\) for the *reduced geometric support* of the Weierstrass locus: a geometric point belongs to \(W\) when its gap sequence differs from the generic gap sequence. Then \(W\) has exactly \(828\) geometric points. Arithmetic Frobenius over \(k\) has cycle type
\[
\boxed{1^{540}\,3^{96}}.
\]
In particular every non-\(k\)-rational Weierstrass point has **exact residue degree three**, and all such points first become rational over \(\mathbb F_{11^6}\), not over any quadratic extension of \(k\). The zeta function of the reduced zero-dimensional \(k\)-scheme \(W\) is
\[
 \boxed{Z(W,T)=\frac{1}{(1-T)^{540}(1-T^3)^{96}}}.
\]
Equivalently, for every positive integer \(n\),
\[
 \#W(\mathbb F_{121^n})=540+288\,\mathbf 1_{3\mid n}.
\]
This result concerns the reduced support; no assertion about scheme-theoretic Weierstrass weights or a canonical Wronskian scheme is made.

## Assumptions and scope
The field has characteristic \(11\), the curve is the *smooth projective normalization* of the displayed affine model, and Frobenius is the \(121\)-power map. The genus is \(g=(11^2-11+4)/6=19\); the curve is maximal over \(\mathbb F_{121}\). The cited Beelen--Montanucci--Vicino classification (arXiv:2303.00376, Lemma 3.11, Theorems 4.6 and 5.2, Proposition 5.4) gives exactly \(540\) rational Weierstrass points and precisely \(288\) additional geometric Weierstrass points, characterized by \(\mathcal P\)-order \(2\). These published counts and the characterization are inputs, not new conclusions.

## Proof
Put \(m=4\) and \(\alpha=a^4/(1+a^4)\) at the affine point \((a,b)\). By the cited classification, a nonrational Weierstrass point occurs precisely when
\[
 B=\frac{\alpha+\omega}{\alpha+\omega^2}
\]
is a **primitive ninth root of unity**, where \(\omega\) is a primitive cube root of unity in \(k\). There are \(\varphi(9)=6\) choices for \(B\), and each gives four choices for \(a\) and twelve for \(b\), so there are \(6\cdot4\cdot12=288\) points. The equations relating these quantities are
\[
 \alpha=\frac{B\omega^2-\omega}{1-B},\qquad
 z:=a^4=\frac{\alpha}{1-\alpha},\qquad
 b^{12}=v:=-z(z+1).
\]
None of the denominators vanishes for primitive ninth roots, and \(z,v\ne0\).

Let \(K=\mathbb F_{11}[t]/(t^6+t^3+1)\), with \(\beta=t\bmod(t^6+t^3+1)\) and \(\omega=\beta^3\). The ninth cyclotomic polynomial is irreducible over \(\mathbb F_{11}\), because the multiplicative order of \(11\) modulo \(9\) equals \(6\). Thus \(K\cong\mathbb F_{11^6}\), and \(\beta\) is a primitive ninth root. The six possible \(B\) are \(\beta^j\) for \(j\in\{1,2,4,5,7,8\}\). The \(121\)-power map sends \(j\) to \(4j\bmod9\), producing two three-cycles \((1,4,7)\) and \((2,8,5)\).

We must show that each of the four roots of \(a^4=z\) and twelve roots of \(b^{12}=v\) is defined over \(K\), **not merely that the auxiliary ratio is**. For the two Frobenius representatives \(B=\beta\) and \(B=\beta^2\), reduction modulo \(t^6+t^3+1\) gives, respectively,
\[
\begin{aligned}
 z_1&=-\beta+\beta^2+\beta^5,&
 v_1&=9+2\beta+9\beta^2+\beta^4+10\beta^5,\\
 z_2&=10+\beta^4+\beta^5,&
 v_2&=9+10\beta+\beta^2+\beta^4+2\beta^5.
\end{aligned}
\]
Exact polynomial modular exponentiation gives, for \(j=1,2\),
\[
 z_j^{442890}=1,\qquad v_j^{147630}=1
 \quad\text{in }K.
\]
These identities are finite algebraic certificates, reproduced by the attached standalone checker. Since the multiplicative group of \(K\) is cyclic of order \(11^6-1=1771560\), the first identity is **equivalent** to \(z_j\) being a fourth power; the second is equivalent to \(v_j\) being a twelfth power. Frobenius conjugation supplies the identities for the other four primitive ninth roots. Both \(\mu_4\) and \(\mu_{12}\) are already contained in \(\mathbb F_{121}\), so **all** four and twelve roots respectively lie in \(K\).

Conversely, the ratio \(B\) uniquely determines \(\alpha\), and \(\alpha\) uniquely determines \(z=a^4\). Since \(B\) has residue degree three over \(k\), so does \(z\); hence every associated point \((a,b)\) has residue degree at least three. Its coordinates lie in \(K\), giving degree exactly three. Thus the \(288\) nonrational points form \(288/3=96\) Frobenius orbits. The other \(540\) Weierstrass points are rational by the published classification, yielding the asserted decomposition and zeta function.

## Verification
Run `python3 verify_weierstrass.py` using only Python's standard library. The verifier constructs the quotient field with exact coefficient arithmetic, checks the cyclotomic relation, all six rational expressions, the two power tests for every primitive ninth root, their exact Frobenius periods, and both cardinalities. Its concluding line is `WEIERSTRASS_SUPPORT_540_RATIONAL_96_CUBIC_VERIFIED`. A second independent check using symbolic polynomial arithmetic reproduced the two representative modular exponent identities. The proof uses the cited published classification for the exhaustiveness of the Weierstrass locus and direct finite-field calculations for its Frobenius descent; it does not infer exhaustiveness from a bounded point census.

## Relationship to prior work
Beelen, Montanucci and Vicino classify the Weierstrass semigroups of this entire maximal-curve family and establish the \(288\) nonrational Weierstrass points at \(q=11\). This result takes their *exact* classification as a premise. Its additional arithmetic statement specifies the first field of definition of **every** exceptional point, the full Frobenius orbit decomposition, and the zeta function of the **reduced Weierstrass support**. Their Lemma 3.11 counts geometric points but does not, on its own, establish that both Kummer coordinates have solutions over the cubic extension. The explicit fourth- and twelfth-power tests provide that additional step. No claim is made that the published semigroup theorem or the known existence of nonrational Weierstrass points is new.

## Limitations
This statement is for the single natural first-exceptional parameter \(q=11\), not for all \(q\equiv2\pmod3\). It concerns the reduced support rather than multiplicities of a Weierstrass divisor. The count and characterization rely on the published complete Weierstrass-semigroup classification. The field computation is exact, but a separately conducted mathematical review and a complete historical-priority audit have not been performed. A later revision or obscure computation might contain the same Frobenius degrees.

## References
1. P. Beelen, M. Montanucci, L. Vicino, *Weierstrass semigroups and automorphism group of a maximal curve with the third largest genus*, arXiv:2303.00376v1 (1 March 2023), especially Lemma 3.11, Theorems 4.6 and 5.2, Proposition 5.4. https://arxiv.org/pdf/2303.00376
2. P. Beelen, M. Montanucci, L. Vicino, *Finite Fields and Their Applications* **92** (2023), article 102300, https://doi.org/10.1016/j.ffa.2023.102300.
