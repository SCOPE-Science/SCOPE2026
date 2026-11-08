# Idempotent averaging projections on quadratic Gorenstein local algebras

## Finding

Let \(k\) be any field, \(m\geq 2\), and \((V,B)\) a nondegenerate symmetric bilinear space of dimension \(m\). Form the commutative associative unital algebra
\[
 A_B=k1\oplus V\oplus kz,\qquad uv=B(u,v)z,\qquad zV=z^2=0.
\]
Its radical is \(J=V\oplus kz\), with \(J^2=kz\), \(J^3=0\), and its socle is \(kz\). Its Hilbert function is \((1,m,1)\).

An averaging projection is a \(k\)-linear map \(P:A_B\to A_B\) obeying both
\[
 P^2=P,\qquad P(xP(y))=P(x)P(y)\quad(x,y\in A_B).
\]
Every nonzero such \(P\) satisfies \(P(1)=1\), and exactly the following four mutually exclusive families occur. In each case set \(W=\operatorname{im}(P)\cap J\).

1. **Scalar-image family.** \(W=0\): any \(\alpha\in J^*\) gives \(P(1)=1\) and \(P(j)=\alpha(j)1\) for \(j\in J\). Its rank is \(1\).

2. **Socle-containing family.** \(z\in W\): choose a nondegenerate subspace \(U\leq V\) of dimension \(r\), \(0\leq r\leq m\), and an arbitrary \(h:U^\perp\to k\). Write \(V=U\oplus U^\perp\); then \(P\) projects along \(\{t+h(t)z:t\in U^\perp\}\) onto \(k1\oplus U\oplus kz\). Its rank is \(r+2\).

3. **Exceptional isotropic-line family.** \(\dim W=1\), \(z\notin W\): choose an isotropic line \(ku\leq V\), a lift \(w=u+cz\) with \(c\in k\), and \(\beta\in k\). Choose \(\gamma\in J^*\) satisfying \(\gamma(w)=1\) and \(\gamma(z)=\beta\). Then
\[
 P(1)=1,\qquad P(j)=\beta B(u,j_V)1+\gamma(j)w\quad(j\in J).
\]
Here \(j_V\) is the \(V\)-coordinate. Its rank is \(2\); in particular \(P(z)=\beta w\). The \(\beta\neq0\) subfamily does not preserve the radical \(J\). The parametrization is unique after one nonzero representative \(u\) has been fixed on each isotropic line.

4. **Higher isotropic family.** \(\dim W=r\geq2\), \(z\notin W\): choose a totally \(B\)-isotropic \(r\)-subspace \(U\leq V\), a form \(\ell\in U^*\), and a complementary subspace \(T\leq V\) with \(V=U\oplus T\). Then \(P\) projects along \(kz\oplus T\) onto
\[
 k1\oplus\{u+\ell(u)z:u\in U\}.
\]
Its rank is \(r+1\). The totally isotropic dimension necessarily satisfies \(r\leq\lfloor m/2\rfloor\).

The zero projection is the only additional averaging projection. In particular, **every averaging projection of rank at least \(3\) preserves the radical**, and non-radical-preserving projections can occur only in ranks \(1\) and \(2\). At rank \(2\), such operators exist exactly when \((V,B)\) has an isotropic line.

**Complete finite-field rank polynomial.** Put \(k=\mathbb F_q\) (any characteristic). Let \(\mathsf N_r(B)\) be the number of nondegenerate \(r\)-subspaces of \(V\), with \(\mathsf N_0=\mathsf N_m=1\). Let \(\mathsf I_r(B)\) be the number of totally \(B\)-isotropic \(r\)-subspaces, with \(\mathsf I_0=1\) and \(\mathsf I_r=0\) for \(r>\lfloor m/2\rfloor\). Then the number of labeled averaging projections by linear rank is exactly the coefficient polynomial
\[
\boxed{\begin{aligned}
\mathcal A_{B,q}(T)={}&1+q^{m+1}T+
\sum_{r=0}^{m}\mathsf N_r(B)q^{m-r}T^{r+2}\\
&+\mathsf I_1(B)q^{m+1}T^2
+\sum_{r=2}^{\lfloor m/2\rfloor}\mathsf I_r(B)q^{r(m-r+1)}T^{r+1}.
\end{aligned}}
\]
The number of non-radical-preserving averaging projections is exactly
\[
(q^{m+1}-1)+(q-1)q^m\mathsf I_1(B).
\]
These are complete finite sums over classical bilinear subspaces. In odd characteristic the subspace counts also have the explicit product formulas below, so no subspace enumeration is needed.

For odd \(q\), let \(\chi\) be the quadratic character of \(\mathbb F_q^\times\), and put \(\delta=\chi(\det B)\) and \(\tau=\chi(-1)\). Define
\[
\begin{aligned}
 o_0(\eta)&=1,\\
 o_{2h+1}(\eta)&=2q^{h^2}\prod_{i=1}^{h}(q^{2i}-1),\\
 o_{2h}(\eta)&=2q^{h(h-1)}(q^h-\tau^h\eta)\prod_{i=1}^{h-1}(q^{2i}-1)\quad(h\geq1).
\end{aligned}
\]
For \(1\leq r<m\),
\[
\mathsf N_r(B)=\sum_{\eta\in\{1,-1\}}
\frac{o_m(\delta)}{o_r(\eta)o_{m-r}(\delta\eta)}.
\]
Next define for each \(s\geq1\)
\[
\nu_s(\eta)=\begin{cases}
q^{s-1}-1,&s\text{ odd},\\
q^{s-1}-1+(q-1)q^{s/2-1}\tau^{s/2}\eta,&s\text{ even}.
\end{cases}
\]
For \(1\leq r\leq\lfloor m/2\rfloor\),
\[
\mathsf I_r(B)=\frac{\prod_{j=0}^{r-1}\nu_{m-2j}(\delta\tau^j)}{\prod_{i=1}^{r}(q^i-1)}.
\]

## Assumptions and scope

All constructions are **labeled linear operators**, not similarity classes. The classification and the subspace-count polynomial hold for every field and every nondegenerate symmetric bilinear form, including characteristic \(2\); the orthogonal-group product formulas are asserted only for odd \(q\). A totally isotropic subspace means \(B(u,v)=0\) for **all** pairs in that subspace (not merely \(B(u,u)=0\) in characteristic \(2\)). No algebraically closedness or positivity assumption is made.

## Proof

**Step 1: decomposition and unitality.** An idempotent linear \(P\) is averaging precisely when \(S=\operatorname{im}P\) is a subalgebra and \(K=\ker P\) is an \(S\)-submodule: \(A_B=S\oplus K\) as vector spaces, \(SS\subseteq S\), \(SK\subseteq K\). Indeed substituting image and kernel elements proves necessity; expanding \(x=s+k\), \(y=s'+k'\) proves sufficiency. Suppose \(P\neq0\). If \(S\subset J\), then \(a=1-P(1)\in K\) is a unit. For \(s\in S\), both \(sa=s-sP(1)\in S\) and \(sa\in K\); hence \(sa=0\), forcing \(S=0\), a contradiction. Therefore \(S\) contains an element \(b\) of nonzero scalar part. This element is a unit; as \(A_B\) is finite-dimensional, its inverse is a polynomial in \(b\) with zero constant term (by its polynomial relation with invertible constant), so \(1\in S\), and consequently \(P(1)=1\). Thus \(S=k1\oplus W\) for the radical subalgebra \(W=S\cap J\).

**Step 2: distinguish the position of the socle.** Let \(\pi:J\to V\) be reduction modulo \(kz\). If \(z\in W\), then \(W=U\oplus kz\), where \(U=\pi(W)\), and \(P(z)=z\). For any \(j\in J\), \(0=P(zj)=zP(j)\) forces the scalar coordinate of \(P(j)\) to vanish. Hence \(P(J)\subset W\), and \(K\subset J\). The projection \(T=\pi(K)\) complements \(U\) in \(V\). The submodule condition \(WK\subset K\) forces \(B(U,T)=0\), since every product here is a scalar multiple of \(z\in W\) and \(W\cap K=0\). By dimension, \(T=U^\perp\) and \(U\) is nondegenerate. Conversely every such \(U\), together with every graph \(K=\{t+h(t)z\}\), satisfies all conditions. This is family 2.

Now assume \(z\notin W\). The projection \(\pi|_W\) is injective. As \(W^2\subset W\) while \(W^2\subset kz\), we have \(W^2=0\), and \(U=\pi(W)\) is totally isotropic. Moreover \(W\) is uniquely the graph of a functional \(\ell:U\to k\). The case \(U=0\) gives \(S=k1\) and every linear functional \(\alpha:J\to k\) defines an averaging projection, proving family 1.

For \(r=\dim W\geq1\), write \(P(z)=a1+v\) with \(v\in W\). From \(0=P(wz)=wP(z)=aw\) for nonzero \(w\in W\), we get \(a=0\). For \(j\in J\), write \(P(j)=\alpha(j)1+w_j\). The \(S\)-linearity identity \(P(wj)=wP(j)\) becomes
\[
\alpha(j)w=B(\pi w,j_V)v\qquad(w\in W,\ j\in J).
\]
If \(r\geq2\), the right side, as a linear operator of \(w\), has rank at most one, whereas a nonzero scalar multiple of the identity has rank \(r\). Therefore \(\alpha=0\). Since \(B\) is nondegenerate and \(U\neq0\), the same equation forces \(v=0\). Thus \(P(J)=W\), \(P(z)=0\) and \(K=kz\oplus T\) for an arbitrary complement \(T\) of \(U\) in \(V\). This is family 4, and its converse follows because \(W^2=0\) and \(WK\subset kz\subset K\).

Finally, if \(r=1\), take \(w=u+cz\) spanning \(W\), with \(u\neq0\), \(B(u,u)=0\). Write \(v=\beta w\) and \(P(j)=\alpha(j)1+\gamma(j)w\). The last displayed equation becomes \(\alpha(j)=\beta B(u,j_V)\). The constraints \(P(w)=w\) and \(P(z)=\beta w\) are exactly \(\gamma(w)=1\) and \(\gamma(z)=\beta\). Conversely these conditions imply \(P^2=P\), \(P(1)=1\), and \(P(wj)=wP(j)\) for all \(j\), proving family 3. The four cases and zero exhaust all operators.

**Step 3: counting.** For family 1 there are \(q^{m+1}\) choices of \(\alpha\). For fixed nondegenerate \(U\) of dimension \(r\), family 2 has \(q^{m-r}\) possible forms \(h\). For each isotropic line \(U\), fixing a generator \(u\), family 3 has \(q\) lifts \(w=u+cz\), \(q\) values of \(\beta\), and \(q^{m-1}\) functionals \(\gamma\) with two independent prescribed values: hence \(q^{m+1}\) maps. For family 4 and fixed isotropic \(r\)-space \(U\), there are \(q^r\) functionals \(\ell\) and \(q^{r(m-r)}\) complementary subspaces \(T\), giving \(q^{r(m-r+1)}\). Distinct data give distinct maps. Adding the zero map proves the complete rank polynomial. The only cases with a scalar component in \(P(J)\) are family 1 with \(\alpha\neq0\) and family 3 with \(\beta\neq0\), which proves the defect count and the rank rigidity.

**Step 4: odd-field product counts.** Over odd \(q\), Witt extension gives a transitive action of the full orthogonal group on nondegenerate \(r\)-spaces with each prescribed determinant square class \(\eta\); stabilizers have orders \(o_r(\eta)o_{m-r}(\delta\eta)\). The displayed formula for \(\mathsf N_r\) follows by orbit-stabilizer. The number of nonzero isotropic vectors in a nondegenerate \(s\)-space of determinant character \(\eta\) is exactly \(\nu_s(\eta)\), by the elementary quadratic Gauss sum. Choosing an ordered basis for a totally isotropic \(r\)-space successively gives \(q^{r(r-1)/2}\prod_{j=0}^{r-1}\nu_{m-2j}(\delta\tau^j)\) possibilities: at stage \(j\), remove \(j\) hyperbolic planes, whose determinants multiply the remaining discriminant by \(\tau^j\), and lift each quotient vector in \(q^j\) ways. Dividing by \(|\operatorname{GL}_r(\mathbb F_q)|=q^{r(r-1)/2}\prod_{i=1}^{r}(q^i-1)\) proves the formula for \(\mathsf I_r\).

## Verification

A standalone, original-identity exhaustive checker is supplied as `checks/exhaustive.cpp`. Compile with `g++ -std=c++17 -O3 checks/exhaustive.cpp -o exhaustive`. Then run `./exhaustive 2 2 0 full`, `./exhaustive 2 2 0`, `./exhaustive 3 2 0`, `./exhaustive 3 2 1`, and `./exhaustive 2 3 1`. Form code `0` denotes the hyperbolic \(2\)-plane; code `1` denotes the diagonal identity Gram matrix. The optional `full` tests all linear maps (not only unital maps) in the first configuration. The checker directly tests \(P^2=P\) and \(P(xP(y))=P(x)P(y)\) on all pairs of algebra basis elements, independently of the classification. The stored counts include the zero operator for the `full` case and omit it for the unital-only cases.

A separate script, `checks/finite_counts.py`, enumerates bilinear subspaces in reduced row-echelon form and, for odd \(q\), cross-checks the orthogonal-group product counts. It reproduces the full rank polynomials and checks an additional \(\mathbb F_3\), dimension-\(3\) example. Complete recorded output is in `checks/verification_output.txt`. In particular, for \(m=2\) over \(\mathbb F_3\), the hyperbolic and anisotropic forms have respective rank profiles \((1,27,63,6,1)\) and \((1,27,9,12,1)\); thus the same dimension and field can have sharply different averaging spectra.

## Relationship to prior work

Guo and Pei, arXiv:1401.7386, Proposition 2.3, already establish the general image-subalgebra/kernel-submodule criterion for idempotent averaging operators; the derivation above credits and uses it. Their principal enumeration concerns free averaging words and Schröder numbers, not the individual projections of a finite-dimensional Gorenstein local algebra. Cao, arXiv:1401.7389, supplies the general algebraic averaging framework, free constructions and Lie structures, but does not provide the orthogonal/isotropic classification or the exact finite-field rank polynomial here. The result is a **specific classification and arithmetic census**, not a new averaging identity or a reproof of those authors' general criterion. The local Gorenstein terminology and bilinear-form model are standard and are not claimed novel.

## Limitations

The claims concern **idempotent** averaging operators on the displayed \((1,m,1)\) algebra, not general averaging maps, noncommutative algebras, automorphism-conjugacy orbits, or nonreduced equation schemes. Odd-characteristic orthogonal product formulas are not asserted for even \(q\); the main subspace-count polynomial is valid for even \(q\) as well. Exhaustive tests cover only the stated small prime fields, not all finite fields or dimensions. Unidentified broader classifications might imply the result; historical priority and independent mathematical validation are not established.

## References

1. L. Guo and J. Pei, *Averaging algebras, Schröder numbers, rooted trees and operads*, arXiv:1401.7386, initially public 2014-01-29; especially Section 2, Proposition 2.3, and Section 3. https://arxiv.org/abs/1401.7386
2. W. Cao, *An Algebraic Study of Averaging Operators*, arXiv:1401.7389, initially public 2014-01-29; especially Sections 1–2 and 4. https://arxiv.org/abs/1401.7389
3. J. Jelisiejew, *Classifying local Artinian Gorenstein algebras*, arXiv:1511.08007 (background on the general local Gorenstein classification problem). https://arxiv.org/abs/1511.08007
