# Quartic Frobenius symmetry in an elementary abelian cover of the Hermitian curve

## Finding
For every odd prime power \(q\), let \(X_q/\mathbb F_q\) be the smooth projective normalization of the plane curve
\[
(x+x^{q^2})^{q+1}+(y+y^{q^2})^{q+1}+1=0,
\]
and let \(H_q/\mathbb F_q\) be the smooth Hermitian curve \(u^{q+1}+v^{q+1}+1=0\). Denote the reciprocal Weil numerators by \(P_X(T)\) and \(P_H(T)\), respectively. Write \(g_X=1+q^2(q+1)(q^3-2)/2\) and \(g_H=q(q-1)/2\).

**Theorem.** For every positive integer \(m\) not divisible by \(4\),
\[
\#X_q(\mathbb F_{q^m})=\#H_q(\mathbb F_{q^m})=
\begin{cases}
q^m+1,&m\text{ odd},\\
q^m+1-q(q-1)(-q)^{m/2},&m\equiv2\pmod4.
\end{cases}
\]
Moreover, there is an integral polynomial \(Q_q(S)\in\mathbb Z[S]\) of degree \((g_X-g_H)/2\) such that
\[
P_X(T)=(1+qT^2)^{g_H}\,Q_q(T^4),\qquad
Q_q(S)=1+\frac{(q^2-1)(q^5+1)}4 S+O(S^2).
\]
Thus every Frobenius trace on the complementary abelian variety vanishes in degrees not divisible by \(4\). This is a statement about Weil numerators, not a determination of the full polynomial \(Q_q\).

The reduced support \(D_q\) of the pullback of the line at infinity to \(X_q\), which is a distinguished Weierstrass-point locus, has exactly \(q^2(q+1)\) geometric points. Put \(e_q=2\) if \(q\equiv1\pmod4\), and \(e_q=0\) if \(q\equiv3\pmod4\). Its Frobenius cycle type is
\[
1^{e_q}\,2^{(q+1-e_q)/2}\,4^{(q+1)(q^2-1)/4},
\]
so its finite-étale zeta function is
\[
Z(D_q,T)=\frac{1}{(1-T)^{e_q}(1-T^2)^{(q+1-e_q)/2}(1-T^4)^{(q+1)(q^2-1)/4}}.
\]

## Assumptions and scope
Here \(q=p^a\) is an arbitrary odd prime power, \(p\ge3\), \(a\ge1\). The named curve \(X_q\) is the **normalization** of a singular plane model, and all point counts refer to its smooth projective model. The morphism and all Frobenius actions are defined over \(\mathbb F_q\). The genus, ordinary singularity description, and the point count in extension degree \(4\) are the established inputs from Borges–Fukasawa (2020/2022); the first-public arXiv version dates to 10 September 2020. This theorem does not assert a full closed form for \(Q_q\), or extend the result to even characteristic.

## Proof
**1. The affine covering and its bijective degrees.** Set \(L(t)=t+t^{q^2}\). The map
\[
\pi:X_q\longrightarrow H_q,\qquad (x,y)\longmapsto(L(x),L(y))
\]
is nonconstant and separable (\(L'(t)=1\)) and extends uniquely from the smooth affine model to the projective normalizations. Over an algebraic closure, it has degree \(q^4\), with translations by \(\ker L\) in each coordinate as its deck group. If \(4\nmid m\), the only root of \(L(t)\) in \(\mathbb F_{q^m}\) is zero: indeed \(t^{q^2}=-t\) entails \(t^{q^4}=t\), while a root in \(\mathbb F_{q^{\gcd(m,4)}}\) must lie in \(\mathbb F_q\) or \(\mathbb F_{q^2}\), where it satisfies \(2t=0\). Thus \(L\) permutes \(\mathbb F_{q^m}\). Consequently the affine rational point sets of \(X_q\) and \(H_q\) have equal cardinalities in every such degree.

**2. The branches at infinity.** The projective singular model of \(X_q\) has exactly \(q+1\) ordinary singularities at infinity, labeled \((\alpha:1:0)\) with \(\alpha^{q+1}=-1\). By the local tangent computation in Borges–Fukasawa, each has \(q^2\) distinct branches with tangents \(X-\alpha Y-\beta Z=0\), indexed by \(\beta\in\ker L\). Hence geometric points of \(D_q\) are canonically labeled by the pairs \((\alpha,\beta)\) with \(\alpha^{q+1}=-1\), \(\beta^{q^2}+\beta=0\), and their arithmetic Frobenius sends \((\alpha,\beta)\) to \((\alpha^q,\beta^q)\). Here \(\alpha\in\mathbb F_{q^2}\) and \(\beta\in\mathbb F_{q^4}\). If \(4\nmid m\), a rational branch requires \(\beta=0\). Thus the rational branches at infinity of \(X_q\) are in bijection with the rational points at infinity of \(H_q\), labeled by the same \(\alpha\). Combined with Step 1, this proves \(\#X_q(\mathbb F_{q^m})=\#H_q(\mathbb F_{q^m})\) for every \(4\nmid m\).

**3. The Hermitian counts.** The curve \(H_q\) is a nonsingular plane curve of genus \(g_H=q(q-1)/2\). At \(\mathbb F_q\)-points its equation is a nonsingular ternary quadratic form, so it has \(q+1\) rational points. Over \(\mathbb F_{q^2}\) it is the Hermitian maximal curve with \(q^3+1\) points. Equality in the Hasse–Weil bound over \(\mathbb F_{q^2}\) forces all reciprocal zeros to square to \(-q\). The zero trace at the first extension forces equal multiplicities of the two square roots, and therefore \(P_H(T)=(1+qT^2)^{g_H}\). The displayed piecewise formula follows by summing their powers.

**4. The quartic Weil factor.** The nonconstant separable morphism \(X_q\to H_q\) induces an abelian subvariety of \(\operatorname{Jac}(X_q)\) isogenous over \(\mathbb F_q\) to \(\operatorname{Jac}(H_q)\). By Poincaré complete reducibility over \(\mathbb F_q\), there is a complementary abelian variety whose integral Weil numerator \(R_q(T)\) satisfies \(P_X(T)=P_H(T)R_q(T)\). For smooth projective curves over finite fields,
\[
\log R_q(T)=\sum_{m\ge1}\bigl(\#X_q(\mathbb F_{q^m})-\#H_q(\mathbb F_{q^m})\bigr)\frac{T^m}{m}.
\]
Step 2 makes every coefficient with exponent not divisible by \(4\) zero. Therefore \(R_q(T)\), being a polynomial with constant term \(1\), is invariant under multiplication of \(T\) by a primitive fourth root of unity, so \(R_q(T)=Q_q(T^4)\) for \(Q_q\in\mathbb Z[S]\). Degree comparison yields \(\deg Q_q=(g_X-g_H)/2\).

**5. First nonzero coefficient.** Borges–Fukasawa's exact count for this normalized model is \(\#X_q(\mathbb F_{q^4})=q^7-q^5+q^3+q^2\); Step 3 gives \(\#H_q(\mathbb F_{q^4})=q^3+1\). Their difference is \((q^2-1)(q^5+1)\). The coefficient of \(T^4\) in \(\log R_q(T)\) is therefore \((q^2-1)(q^5+1)/4\), also the coefficient of \(S\) in \(Q_q(S)\).

**6. The finite boundary spectrum.** For \(\beta=0\), Frobenius on \(\alpha\) fixes exactly \(e_q\) labels and pairs the other \(q+1-e_q\). Every nonzero \(\beta\) has Frobenius order exactly \(4\), since its second power satisfies \(\beta^{q^2}=-\beta\ne\beta\). The \((q+1)(q^2-1)\) nonzero-\(\beta\) pairs accordingly form \((q+1)(q^2-1)/4\) four-cycles. This proves the full boundary zeta formula.

## Verification
The standalone script `verify.py` computes exact polynomial-quotient finite fields, implements Frobenius and the linearized map, enumerates both affine curves and their infinity labels, and tests the predicted formulas. `samples.csv` is the output of `python verify.py`; all rows are exact arithmetic, not randomized experiments. In particular, \(\#X_3(\mathbb F_{81})=1980\), \(\#H_3(\mathbb F_{81})=28\), \(\#X_5(\mathbb F_{625})=75150\) and \(\#H_5(\mathbb F_{625})=126\). These checks are supporting examples: the proof of the universal statements is Steps 1–6, not interpolation from the tested fields.

## Relationship to prior work
Fukasawa (2013/2016) introduced the broader separated-linearized-variable plane-curve family and established its irreducibility and genus framework. Borges–Fukasawa (2020/2022) studied the chosen elementary abelian cover and proved its geometric singularity/branch structure, automorphisms, distinguished Weierstrass locus, and exact degree-four point count. Those prior results are premises, not new claims here. The additional arithmetic assertion is the all-extension vanishing outside multiples of four, the integral quartic support of the complementary Weil factor, its first nonzero coefficient, and the full degree-one/two/four Frobenius splitting of the distinguished boundary locus. The examined primary results do not explicitly give these full arithmetic assertions; an equivalent unindexed computation is a historical-priority risk.

## Limitations
This identifies only a constrained factorization and one coefficient of the complementary Weil numerator, not its remaining coefficients or the full zeta function. The quotient morphism has wild degree, but separability and the abelian-variety isogeny decomposition suffice for the stated conclusion. This same-author mathematical review is not independent verification. Characteristic two is excluded because the kernel-field argument changes.

## References
- H. Borges and S. Fukasawa, *An elementary abelian p-cover of the Hermitian curve with many automorphisms*, arXiv:2009.04716 (first posted 2020-09-10; version 3 posted 2022-02-08), *Mathematische Zeitschrift* 302 (2022), 695–706. https://arxiv.org/abs/2009.04716. Especially Theorems 1–2 and Remark 2.
- S. Fukasawa, *A family of plane curves with two or more Galois points in positive characteristic*, arXiv:1308.1490 (first posted 2013-08-07), in *Contemporary Developments in Finite Fields and Applications*, 2016, pp. 62–73. https://arxiv.org/abs/1308.1490.
- J. W. P. Hirschfeld, G. Korchmáros and F. Torres, *Algebraic Curves over a Finite Field*, Princeton University Press, 2008 (standard Hermitian-curve facts).
