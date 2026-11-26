# The reduced restricted nullcone of the two-variable characteristic-two Witt derivation algebra

## Finding
Let \(k\) be any field of characteristic \(2\) and let
\[
A=k[x,y]/(x^2,y^2),\qquad W=\operatorname{Der}_k(A).
\]
Here \(W\) is an eight-dimensional restricted Lie algebra with restricted square \(D^{[2]}=D\circ D\). Give the closed subset
\[
\mathcal Z(k)=\{D\in W:D^2=0\}
\]
its reduced algebraic-variety structure over \(k\). Then \(\mathcal Z\) is **geometrically irreducible, rational and four-dimensional**. Its open locus on which at least one of \(D(x),D(y)\) has nonzero constant coefficient is isomorphic over \(k\) to \((\mathbb A^2\setminus\{0\})\times\mathbb A^2\).

If \(k=\mathbb F_q\), with \(q=2^e\) and \(e\ge1\), the exact rank distribution for the underlying \(k\)-linear endomorphism \(D:A\to A\) is
\[
\begin{aligned}
\#\{D\in\mathcal Z(k):\operatorname{rank}D=0\}&=1,\\
\#\{D\in\mathcal Z(k):\operatorname{rank}D=1\}&=q^3+q^2-q-1,\\
\#\{D\in\mathcal Z(k):\operatorname{rank}D=2\}&=q^4-q^2.
\end{aligned}
\]
In particular,
\[
\boxed{\#\mathcal Z(\mathbb F_q)=q^4+q^3-q.}
\]
No assertion about reducedness, radicality, normality, or singularities of the **scheme** cut out by the coordinate equations for \(D^2\) is intended.

## Assumptions and scope
The characteristic-two hypothesis is essential to the computation: the composition square of a derivation is again a derivation because the Leibniz cross term vanishes. The ring \(A\) has basis \((1,x,y,xy)\). Every \(k\)-derivation is uniquely determined by arbitrary images of \(x\) and \(y\), since the derivatives of their defining square relations vanish. Thus \(\dim_k W=8\), and its restricted \(2\)-power is ordinary composition. The geometric statement holds over any field of characteristic \(2\), including nonperfect fields, after extension to an algebraic closure. The numerical formulas apply to every finite field of characteristic \(2\); rank means ordinary linear rank on the four-dimensional algebra \(A\).

Write \(z=(x,y)^T\) and uniquely express
\[
D(z)=v+Bz+cxy,\qquad v,c\in k^2,\ B\in M_2(k).
\]
Write \(\lambda_v=(v_2,v_1)\) for a row vector, so \(\lambda_v v=0\) in characteristic two.

## Proof
**1. Equations.** Applying Leibniz to \(xy\) gives
\[
D(xy)=v_1y+v_2x+\operatorname{tr}(B)xy.
\]
Consequently
\[
D^2(z)=Bv+\bigl(B^2+c\lambda_v\bigr)z+
\bigl(B+\operatorname{tr}(B)I_2\bigr)c\,xy.
\]
As \(D^2\) is a derivation in characteristic two, it vanishes on all of \(A\) exactly when it vanishes on both generators. The defining conditions are therefore precisely
\[
Bv=0,\qquad B^2+c\lambda_v=0,\qquad
\bigl(B+\operatorname{tr}(B)I_2\bigr)c=0.\tag{1}
\]

**2. Nonzero constant term.** Suppose \(v\ne0\). Since the one-dimensional annihilator of \(v\) in \((k^2)^*\) is spanned by the nonzero row \(\lambda_v\), the first equation of (1) says uniquely that \(B=u\lambda_v\) for some \(u\in k^2\). Put \(a=\lambda_v u\). Then \(B^2=a u\lambda_v\) and \(\operatorname{tr}(B)=a\). The second equation of (1) forces \(c=au\). The third equation follows since
\[
(B+aI_2)(au)=a(au)+a^2u=0.
\]
Conversely, every \((v,u)\) with \(v\ne0\) yields a solution by
\[
(v,u)\longmapsto (v,\ B=u\lambda_v,\ c=(\lambda_vu)u).\tag{2}
\]
This is an isomorphism onto the open subset \(U\subset\mathcal Z\): on each open chart \(v_1\ne0\) or \(v_2\ne0\), one recovers \(u\) regularly by dividing the appropriate column of \(B\) by the corresponding nonzero coordinate of \(\lambda_v\). Hence \(U\cong(\mathbb A^2\setminus\{0\})\times\mathbb A^2\), a smooth irreducible rational variety of dimension four.

**3. Zero constant term.** If \(v=0\), equations (1) become \(B^2=0\) and \(Bc=0\): a square-zero \(2\times2\) matrix has trace zero. The nonzero such matrices have rank one, with image equal to kernel, and they number \((q+1)(q-1)=q^2-1\) over \(\mathbb F_q\): choose their common image/kernel line and then a nonzero map from the quotient line back to it. Each permits \(q\) values of \(c\). The zero matrix permits \(q^2\) values, giving
\[
\#\{(v,B,c)\in\mathcal Z(\mathbb F_q):v=0\}=
(q^2-1)q+q^2=q^3+q^2-q.\tag{3}
\]
Together with the \((q^2-1)q^2\) solutions (2) for nonzero \(v\), this proves the total point count.

**4. Geometric irreducibility.** It remains to show that all solutions with \(v=0\), over an algebraic closure \(K\) of \(k\), lie in the closure of \(U_K\). If \(B_0\ne0\), write \(B_0=\alpha w\lambda_w\) where \(w\ne0\), \(\alpha\ne0\), and \(c_0=\beta w\). This is possible because every nonzero square-zero \(2\times2\) matrix has image and kernel equal to \(Kw\). Choose \(b\in K^2\) with \(\lambda_w b=\beta/\alpha\). In parametrization (2), for \(t\ne0\), set
\[
v(t)=tw,\qquad u(t)=\alpha t^{-1}w+b.
\]
The resulting triples have polynomial limits
\[
B(t)=\alpha w\lambda_w+t b\lambda_w\to B_0,
\qquad c(t)=\beta w+t(\lambda_w b)b\to c_0.
\]
If \(B_0=0\) and \(c_0\ne0\), choose \(w\in K^2\) with \(\lambda_w c_0=1\) and put \(v(t)=t^2w\), \(u(t)=t^{-1}c_0\). Formula (2) yields \(B(t)=t c_0\lambda_w\to0\) and \(c(t)=c_0\). The origin is approached by \(v(t)=tw\), \(u(t)=0\). All displayed \((v(t),B(t),c(t))\) extend polynomially through \(t=0\). Thus \(\mathcal Z_K=\overline{U_K}\), proving geometric irreducibility and dimension four. Rationality follows from the dense parametrized open subset.

**5. Rank stratification.** For any square-zero endomorphism of the four-dimensional \(A\), the rank is at most two. If \(v\ne0\), some image \(D(x)\) or \(D(y)\) has nonzero constant coefficient, whereas \(D(xy)=v_1y+v_2x+\operatorname{tr}(B)xy\) has nonzero linear part and zero constant coefficient, so the rank is two. If \(v=0\), then \(D(xy)=0\). For \(B\ne0\), the condition \(Bc=0\) places \(c\) in \(\ker B=\operatorname{im}B\), so the augmented \(2\times3\) coefficient matrix \([B\mid c]\) has rank one; for \(B=0\), the rank is one if \(c\ne0\) and zero otherwise. Equations (2) and (3) now give the three rank counts above. This completes the proof.

## Verification
The included standalone `verify.py` enumerates all eight coefficients of a derivation over \(\mathbb F_2\) and \(\mathbb F_4\), forms its actual \(4\times4\) matrix via Leibniz multiplication on \((1,x,y,xy)\), squares this matrix by finite-field matrix multiplication, and directly computes its rank by Gaussian elimination. It does not use the coordinate conditions (1) to determine acceptance. It reproduced
\[
\begin{array}{c|ccc|c}
q&\text{rank }0&\text{rank }1&\text{rank }2&\text{total}\\\hline
2&1&9&12&22\\
4&1&75&240&316
\end{array}
\]
and printed `VERIFY_OK`. These finite calculations test, but do not replace, the arbitrary-field algebraic and geometric proof.

## Relationship to prior work
Premet's 1992 paper studies invariant functions and the **full nilpotent cone** of Cartan-type \(W_n\), under the explicit assumption that the characteristic exceeds two. His 2014 paper studies regular derivations and invariant-theoretic fibers of \(\operatorname{Der}(k[X_1,\ldots,X_n]/(X_i^p))\), again explicitly in characteristic \(p>2\). Neither result determines the reduced restricted square-zero locus in characteristic two or its finite-field point counts. The present locus \(\{D:D^{[2]}=0\}\) is also strictly narrower than a full nilpotent cone defined by some sufficiently large power vanishing. Comparisons to finite-field square-zero derivations of other Lie algebras and to Poisson-bracket classifications on the same four-dimensional associative algebra concern different operators or equivalence problems, so neither implication is available. Novelty is asserted only relative to the material actually located and inspected.

## Limitations
The result treats exactly two truncated variables, all fields of characteristic two, and the reduced underlying geometric locus. It does not claim a classification for three or more variables, full automorphism-conjugacy orbits, singularities, scheme-theoretic radicality, or the structure of the full nilpotent cone. No independence or external mathematical audit has been performed. A specialized earlier result about height-one vector-field varieties might potentially imply the point count; available searches did not resolve every such possibility.

## References
1. A. Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426v1 (first public version 2014-05-10); version 3 (2014-07-22), especially introduction and §§2–4. https://arxiv.org/html/1405.2426v3
2. A. A. Premet, *The theorem on restriction of invariants, and nilpotent elements in* \(W_n\), Mathematics of the USSR-Sbornik **73** (1992), 135–159, doi:10.1070/SM1992v073n01ABEH002538. https://www.mathnet.ru/eng/sm1322
