# A two-vertex averaging Reynolds operator ring has a repeating simple-module syzygy

## Finding

Let \(k\) be any field with \(\operatorname{char}k\ne2\), let \(R=k\times k\) with coordinatewise multiplication, and define
\[
P(a,b)=\left(\frac{a+b}{2},\frac{a+b}{2}\right).
\]
This is the idempotent classical Reynolds operator projecting onto the diagonal subalgebra \(A=k(1,1)\). Its operator ring satisfies
\[
\mathcal U_{R,P}\cong B=\begin{pmatrix}k[t]&tk[t]\\tk[t]&k[t]\end{pmatrix}.
\]
Put \(O=k[t]_{(t)}\) and \(\Lambda=B\otimes_{k[t]}O=\begin{pmatrix}O&tO\\tO&O\end{pmatrix}\). If \(J=tM_2(O)\), \(e_1=E_{11}\), and \(S_1=\Lambda e_1/J e_1\), then
\[
\Omega^n_\Lambda(S_1)\cong Je_1\quad(n\ge1),
\]
where \(Je_1\) is not projective. Consequently \(\operatorname{pd}_\Lambda S_1=\infty\) and \(\operatorname{gl.dim}\mathcal U_{R,P}=\infty\).

## Assumptions and scope

All algebras are unital. The field restriction is needed for the averaging projection and for the rescaling of positive-degree components by powers of \(2\). The ring \(\mathcal U_{R,P}\) is the associative operator ring representing modules over the Reynolds algebra \((R,P)\), as defined in the cited primary source. The result concerns this one proper projection; it does not classify operator rings for other finite-dimensional algebras or other Reynolds operators.

## Proof

The map \(P\) is idempotent and fixes \((1,1)\). Writing \(s=(a+b)/2\) and \(u=(c+d)/2\), one has
\[
P(a,b)P(c,d)=(su,su)=P((a,b)P(c,d))=P(P(a,b)(c,d)),
\]
so the averaging identity, and hence the classical Reynolds identity of weight \(-1\), holds.

The graded presentation of the operator ring for an idempotent classical Reynolds operator fixing the identity gives degree zero \(R\), positive-degree pieces \((R\otimes_A R)t^n\), and multiplication
\[
(r\otimes s)t^m(u\otimes v)t^n=(r\otimes P(su)v)t^{m+n}\quad(m,n\ge1).
\]
For the coordinate idempotents \(e_1=(1,0)\) and \(e_2=(0,1)\), \(P(e_j e_i)=\delta_{ij}(1,1)/2\). Thus
\[
((e_i\otimes e_j)t^m)((e_k\otimes e_l)t^n)=\frac{\delta_{jk}}2(e_i\otimes e_l)t^{m+n}.
\]
Send degree-zero \(e_i\) to \(E_{ii}\) and send \((e_i\otimes e_j)t^n\) to \(2^{n-1}E_{ij}t^n\) for \(n\ge1\). The displayed multiplication shows that this is a graded algebra isomorphism onto \(B\): the degree-zero part is the diagonal constant matrices, and every positive-degree part is \(M_2(k)t^n\). Therefore \(B\) has exactly the matrix description claimed above.

Localize at the multiplicative set \(k[t]\setminus(t)\). The resulting ring is \(\Lambda=\begin{pmatrix}O&tO\\tO&O\end{pmatrix}\), where \(O=k[t]_{(t)}\) is a discrete valuation ring. Its Jacobson radical is \(J=tM_2(O)\): every element of \(J\) has a complement invertible in \(\Lambda\), while \(\Lambda/J\cong k\times k\) is semisimple. The indecomposable projectives are \(P_i=\Lambda e_i\), and \(Je_1/J^2e_1\cong S_1\oplus S_2\), with \(S_i=\Lambda e_i/Je_i\).

Consider the map
\[
\pi:P_1\oplus P_2\longrightarrow Je_1,\qquad (x,y)\longmapsto x(te_1)+y(tE_{21}).
\]
Its image is \(tP_1+P_2(tE_{21})=Je_1\). On tops, the two summands map to the two independent coordinates of \(Je_1/J^2e_1\), so \(\pi\) is the projective cover. Writing \(x=(a,tc)^T\) and \(y=(tb,d)^T\), the kernel equations are \(a=-tb\) and \(d=-tc\). Hence
\[
\ker\pi=\{(z,-z):z\in tO^2\}\cong Je_1
\]
as left \(\Lambda\)-modules. This kernel is nonzero, so the projective cover of \(Je_1\) is not an isomorphism; in particular \(Je_1\) is not projective. The same projective cover and kernel calculation repeats at every step. Since \(\Omega(S_1)=Je_1\), induction gives \(\Omega^n(S_1)\cong Je_1\) for every \(n\ge1\), proving \(\operatorname{pd}_\Lambda S_1=\infty\).

Finally, if \(\mathcal U_{R,P}\cong B\) had finite global dimension, localizing a finite projective resolution of any \(\Lambda\)-module over the central multiplicative set would give a projective resolution of the same length over \(\Lambda\), because that set acts invertibly on every \(\Lambda\)-module. This would force \(\operatorname{gl.dim}\Lambda<\infty\), contradicting the infinite projective dimension just established. Thus \(\operatorname{gl.dim}\mathcal U_{R,P}=\infty\).

## Verification

The multiplication check is exact in every positive degree: the coefficient on either side of the proposed matrix isomorphism is \(\delta_{jk}2^{m+n-2}\). The radical quotient is \(k\times k\), and the projective-cover map induces an isomorphism on tops. The kernel equations explicitly identify the next syzygy with the same nonprojective module. No finite enumeration or numerical experiment is used as a substitute for the proof.

## Relationship to prior work

The primary Reynolds-operator paper gives the general graded description of this operator ring for idempotent classical Reynolds operators fixing the identity (Theorem 4.7) and compute global dimension for the identity and zero operators on the one-dimensional algebra \(k\) (Proposition 6.12). The present calculation specializes their description to the proper diagonal projection on \(k\times k\) and adds an explicit matrix-order realization and a repeating simple-module syzygy. Jategaonkar's work on tiled orders over discrete valuation rings supplies broader context for global-dimension questions; the proof here uses the displayed projective cover directly and does not rely on a classification theorem for tiled orders.

## Limitations

The construction requires \(\operatorname{char}k\ne2\). It proves infinite global dimension for this specific operator ring and the stated local syzygy pattern; it gives no classification for other projections. The older tiled-order literature is broader than the exact calculation made here, and priority for this precise application is not settled by an abstract-level comparison alone.

## References

1. *Modules and Operator Rings of Reynolds Algebras*, arXiv:2610.21829v1 (2026), especially Theorem 4.7 and Proposition 6.12. https://arxiv.org/abs/2610.21829
2. V. A. Jategaonkar, *Global dimension of tiled orders over a discrete valuation ring*, Transactions of the American Mathematical Society 196 (1974), 313–330. https://doi.org/10.1090/S0002-9947-1974-0349729-3
