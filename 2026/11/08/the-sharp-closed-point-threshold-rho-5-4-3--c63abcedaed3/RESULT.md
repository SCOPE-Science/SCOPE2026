# The sharp closed-point threshold \(\rho(5,4)=3\)

## Finding
For a smooth, projective, geometrically integral curve \(X/\mathbb F_5\), write \(B_r(X)\) for the number of its degree-\(r\) closed points. Let \(\rho(5,4)\) be the least positive integer \(R\) such that, for **every** genus-four curve \(X/\mathbb F_5\) and **every** integer \(r\ge R\), one has \(B_r(X)>0\). Then
\[
\boxed{\rho(5,4)=3.}
\]
Sharpness is witnessed by the smooth projective model \(H/\mathbb F_5\) of
\[
H:\qquad y^2=x^9+3x^3+2x.
\]
It has genus four and satisfies \(\#H(\mathbb F_5)=\#H(\mathbb F_{25})=8\), so \(B_2(H)=0\). In fact its eight points over \(\mathbb F_{25}\) are already rational over \(\mathbb F_5\); it is Diophantine-stable for this quadratic extension.

## Assumptions and scope
The base field is precisely \(\mathbb F_5\), and curves are smooth, projective, and geometrically integral of genus exactly four. A closed point of degree \(r\) means a Frobenius orbit of size \(r\). Denote \(N_r(X)=\#X(\mathbb F_{5^r})\); then
\[
N_r(X)=\sum_{d\mid r} d B_d(X).
\]
The claimed threshold concerns **all** genus-four curves over this field, not only hyperelliptic members. Neither the uniqueness nor isomorphism classification of sharpness witnesses is asserted.

## Proof
**1. Smooth genus-four witness.** Put \(f(x)=x^9+3x^3+2x=xA(x^2)\), with \(A(t)=t^4+3t+2\). In characteristic five its derivative is \(f'(x)=4x^8+4x^2+2\). For \(t=x^2\), the identity
\[
f'(x)-4A(t)=2t+4
\]
shows that a common zero of \(f\) and \(f'\) with \(x\ne0\) would have \(t=3\). But \(A(3)=2\ne0\) in \(\mathbb F_5\), and \(f'(0)=2\ne0\). Hence \(f\) is squarefree. Its degree is the odd integer nine, so the smooth projective hyperelliptic model has genus \((9-1)/2=4\) and one rational point at infinity.

**2. Exactly eight points in both fields.** Write \(\mathbb F_{25}=\mathbb F_5[w]/(w^2-2)\). This is a field because two is nonsquare in \(\mathbb F_5\), and the norm of \(a+bw\) is \(a^2-2b^2\). The quadratic character of a nonzero element of \(\mathbb F_{25}\) equals the quadratic character of its norm in \(\mathbb F_5\). Direct substitution of \(f(a+bw)\), reduced using \(w^2=2\), yields the following **complete** norm table, whose rows are \(b=0,1,2,3,4\) and columns \(a=0,1,2,3,4\):
\[
\begin{pmatrix}
0&1&0&0&1\\
3&3&3&3&3\\
3&2&2&2&2\\
3&2&2&2&2\\
3&3&3&3&3
\end{pmatrix}.
\]
Since one is a square and two and three are nonsquares in \(\mathbb F_5\), the corresponding \(\mathbb F_{25}\)-character table has three zero entries, two \(+1\) entries, and twenty \(-1\) entries. The equation \(y^2=f(x)\) therefore has \(3+2\cdot2=7\) affine points over \(\mathbb F_{25}\), plus the point at infinity: \(N_2(H)=8\). Its entries with \(b=0\) show that those points all have coordinates over \(\mathbb F_5\), giving \(N_1(H)=8\). Consequently \(B_2(H)=(N_2(H)-N_1(H))/2=0\), proving \(\rho(5,4)\ge3\).

**3. Degree three on every genus-four curve.** By the Weil bounds, every genus-four \(X/\mathbb F_5\) satisfies
\[
N_r(X)\in[5^r+1-8\cdot5^{r/2},\ 5^r+1+8\cdot5^{r/2}].
\]
Hence
\[
N_3(X)-N_1(X)\ge120-48\sqrt5>0.
\]
Since \(3B_3(X)=N_3(X)-N_1(X)\), every such curve has a degree-three point.

**4. Every degree at least four.** For each positive integer \(d\), the Weil upper bound satisfies
\[
N_d(X)\le5^d+1+8\cdot5^{d/2}<5\cdot5^d;
\]
the strict final inequality already holds at \(d=1\), and its margin increases for larger \(d\). Every proper divisor \(d\) of an integer \(r\ge4\) satisfies \(d\le\lfloor r/2\rfloor\). Therefore
\[
\sum_{\substack{d\mid r\\d<r}}N_d(X)<5\sum_{d=1}^{\lfloor r/2\rfloor}5^d
<\frac{25}{4}5^{r/2}.
\]
Together with the Weil lower bound,
\[
N_r(X)-\sum_{\substack{d\mid r\\d<r}}N_d(X)
>5^{r/2}\left(5^{r/2}-\frac{57}{4}\right)+1>0,
\]
because \(r\ge4\) implies \(5^{r/2}\ge25>57/4\). Finally,
\[
rB_r(X)=N_r(X)-\sum_{\substack{d\mid r\\d<r}}dB_d(X)
\ge N_r(X)-\sum_{\substack{d\mid r\\d<r}}N_d(X)>0.
\]
Thus \(B_r(X)>0\) for all \(r\ge4\). With Steps 2–3 this proves \(\rho(5,4)=3\).

## Verification
Two independently implemented exact-arithmetic programs are provided: `verify_quadratic.py` computes the complete 25-entry norm table and both point counts directly in \(\mathbb F_5[w]/(w^2-2)\), while `verify_extensions.py` uses polynomial-basis finite fields to count the points over extensions of degrees one through four. The latter returns \((N_1,N_2,N_3,N_4)=(8,8,152,592)\) and reconstructs the Hasse–Weil zeta numerator
\[
P_H(T)=(1-2T+5T^2)(1+4T+5T^2)(1-9T^2+25T^4).
\]
This **Weil-polynomial candidate already appears in an earlier published table** (see below). The universal all-degree argument is a proof from the Weil inequalities; finite computations are used only for the explicit sharpness witness and its ancillary zeta numerator.

## Relationship to prior work
Aubry, Herbaut, and Monaldi introduced systematic bounds for \(\rho(q,g)\) and determined its exact values for genera one through three; the genus-four case addressed here is not tabulated there. Lario's public Diophantine-stability table lists **exactly the characteristic polynomial written above** among *candidate* genus-four Weil polynomials for \(\mathbb F_{25}/\mathbb F_5\); the table explicitly distinguishes candidate Weil polynomials from constructed genus-four curves in fields other than \(\mathbb F_2\). The Weil polynomial by itself, or the prediction of Diophantine stability from it, is therefore not presented as new. The extra statements are the explicit realization by the smooth hyperelliptic equation and the resulting proven sharp universal threshold. Related discussions of Diophantine stability by Bars, Lario, and Vrioni provide background but do not establish this exact genus-four conclusion in the material inspected.

## Limitations
This theorem does not classify all genus-four Diophantine-stable curves, nor determine the exact thresholds in other finite fields or genera. Its earlier priority status is subject to an unresolved possibility that an explicit curve with the same stability property was recorded in older, unindexed work. In particular, the complete text of Vrioni's earlier thesis was unavailable for material comparison. The quoted earlier candidate Weil polynomial is not an independent proof that its isogeny class is realized by a genus-four Jacobian. No independent external audit or priority certification has been performed.

## References
1. Y. Aubry, F. Herbaut, J. Monaldi, *Closed points on curves over finite fields*, arXiv:2310.11218 (initial public submission 17 October 2023), https://arxiv.org/abs/2310.11218 ; original full text https://www.i2m.univ-amu.fr/perso/yves.aubry/ArXiv_Aubry_Herbaut_Monaldi_Closed_Points.pdf.
2. J. C. Lario, *Curves over Finite Fields with Diophantine Stability*, public table, https://web.mat.upc.edu/joan.carles.lario/DS.html (genus-four candidate-polynomial list, GF(25)/GF(5) entry with \(N=8\)).
3. F. Bars, J. C. Lario, B. Vrioni, *Diophantine stability for curves over finite fields*, https://mat.uab.cat/~francesc/Diophantine2.pdf (available manuscript).
4. B. Vrioni, *A census for curves and surfaces with Diophantine stability over finite fields* (2021), https://upcommons.upc.edu/entities/publication/6cce8628-d74c-41cb-9c04-b478ee7686be, DOI:10.5821/dissertation-2117-360914; repository abstract inspected, full thesis text not inspected.
