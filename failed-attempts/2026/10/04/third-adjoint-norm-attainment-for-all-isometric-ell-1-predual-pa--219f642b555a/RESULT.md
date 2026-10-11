# Third-adjoint norm attainment for all isometric \(\ell_1\)-predual pairs
## Finding
Let \(\Gamma\) and \(\Delta\) be arbitrary index sets. If \(X\) and \(Y\) are real Banach spaces with \(X^*\) linearly isometric to \(\ell_1(\Gamma)\) and \(Y^*\) linearly isometric to \(\ell_1(\Delta)\), then
\[
\operatorname{NA}_3(X,Y)=\mathcal L(X,Y).
\]
Thus every bounded \(T:X\to Y\) has a norm-attaining third adjoint \(T^{***}:Y^{***}\to X^{***}\). The uniform depth bound is sharp within the class: \(c^*\) is linearly isometric to \(\ell_1\), but
\[
\operatorname{NA}_2(c,c)\ne\mathcal L(c,c)
\quad\text{and}\quad
\operatorname{NA}_3(c,c)=\mathcal L(c,c).
\]

## Assumptions and scope
All spaces are real. “Linearly isometric to \(\ell_1(\Gamma)\)” means that there is a surjective linear isometry onto the indicated \(\ell_1\)-space. No separability or countability is assumed for \(\Gamma\) or \(\Delta\). The claim concerns third-adjoint norm attainment; it does not assert universal second-adjoint norm attainment for arbitrary \(\ell_1\)-preduals.

For a bounded operator \(S:E\to F\), membership in \(\operatorname{NA}_k(E,F)\) means that the \(k\)-th adjoint of \(S\) attains its operator norm.

## Proof
We first obtain an off-diagonal consequence of the published \(\ell_1(\Lambda)\) endomorphism theorem.

Let \(R:\ell_1(\Delta)\to\ell_1(\Gamma)\) be bounded. Put \(\Lambda=\Delta\sqcup\Gamma\), so
\[
\ell_1(\Lambda)=\ell_1(\Delta)\oplus_1\ell_1(\Gamma).
\]
Define
\[
A(d,g)=(0,Rd).
\]
Then \(\|A\|=\|R\|\). If \(\Lambda\) is infinite, Remark 3.20 of Dantas--Jung--Martín gives
\[
\mathcal L(\ell_1(\Lambda),\ell_1(\Lambda))
=
\operatorname{NA}_2(\ell_1(\Lambda),\ell_1(\Lambda)),
\]
so \(A^{**}\) attains its norm. If \(\Lambda\) is finite, the same conclusion is immediate from finite dimensionality.

Using
\[
(\ell_1(\Delta)\oplus_1\ell_1(\Gamma))^{**}
=
\ell_1(\Delta)^{**}\oplus_1\ell_1(\Gamma)^{**},
\]
we have
\[
A^{**}(d^{**},g^{**})=(0,R^{**}d^{**}).
\]
Assume \(R\ne0\), and choose \((d^{**},g^{**})\) in the unit sphere at which \(A^{**}\) attains its norm. Then
\[
\|R\|
=\|A\|
=\|A^{**}(d^{**},g^{**})\|
=\|R^{**}d^{**}\|
\le \|R\|\,\|d^{**}\|
\le \|R\|.
\]
Hence \(\|d^{**}\|=1\), and \(R^{**}\) attains \(\|R\|\). The case \(R=0\) is trivial. Therefore
\[
\mathcal L(\ell_1(\Delta),\ell_1(\Gamma))
=
\operatorname{NA}_2(\ell_1(\Delta),\ell_1(\Gamma))
\]
for arbitrary \(\Gamma,\Delta\).

Now choose surjective linear isometries
\[
U:Y^*\to\ell_1(\Delta),
\qquad
V:X^*\to\ell_1(\Gamma).
\]
For \(T:X\to Y\), define
\[
R=VT^*U^{-1}:\ell_1(\Delta)\to\ell_1(\Gamma).
\]
By the previous paragraph, \(R^{**}\) attains its norm. Functoriality of the bidual gives
\[
R^{**}
=
V^{**}T^{***}(U^{-1})^{**}.
\]
Both \(V^{**}\) and \((U^{-1})^{**}\) are surjective linear isometries. Therefore norm attainment of \(R^{**}\) transfers to \(T^{***}\). Since \(\|T^{***}\|=\|T\|\), every \(T\) belongs to \(\operatorname{NA}_3(X,Y)\).

Sharpness follows from Corollary 3.19 of the same paper: \(c^*\) is linearly isometric to \(\ell_1\), while \(\operatorname{NA}_2(c,c)\ne\mathcal L(c,c)\) and \(\operatorname{NA}_3(c,c)=\mathcal L(c,c)\).

## Verification
The proof was checked at the level of maps, domains, codomains, adjoint parity, and norms. In particular, for \(T:X\to Y\), the third adjoint has direction \(T^{***}:Y^{***}\to X^{***}\). The block operator \(A\) has exactly the same norm as \(R\), and the \(\ell_1\)-sum norm forces the norm-attaining point of \(A^{**}\) to have first coordinate of norm \(1\) whenever \(R\ne0\). The isometric conjugacy step preserves both the operator norm and norm attainment.

No finite experiment or numerical certificate is used.

## Relationship to prior work
Dantas, Jung and Martín prove \(\mathcal L(\ell_1,\ell_1)=\operatorname{NA}_2(\ell_1,\ell_1)\) in Theorem 3.17 and state in Remark 3.20 that the proof routinely extends to \(\ell_1(\Gamma)\) for every infinite index set \(\Gamma\). Their Corollary 3.19 proves the sharp separation on \(c\): universal third-adjoint norm attainment holds there while universal second-adjoint norm attainment fails.

The paper also classifies universal second-adjoint norm attainment for a particular family of \(\ell_1\)-preduals \(W_\alpha\). The present statement is different: it gives a uniform third-adjoint conclusion for every pair of isometric \(\ell_1\)-preduals, with arbitrary and possibly different index sets. The off-diagonal \(\ell_1(\Delta)\to\ell_1(\Gamma)\) step follows by embedding the operator as one block of an endomorphism on the \(\ell_1\)-sum.

Targeted searches for the cross-cardinality second-adjoint statement and for universal third-adjoint norm attainment across arbitrary isometric \(\ell_1\)-predual pairs did not locate a covering statement.

## Limitations
The theorem requires isometric, not merely isomorphic, \(\ell_1\)-duals. It does not improve second-adjoint norm attainment for those \(\ell_1\)-preduals where that property fails. The argument is a short structural consequence of a very recent theorem, so an equivalent formulation may exist in unindexed or differently worded literature.

## References
1. Sheldon Dantas, Mingu Jung, Miguel Martín, *On operators whose adjoints or second adjoints attain their norms*, arXiv:2609.00794v1, first submitted 2026-09-01. See Theorem 3.17, Corollary 3.19, and Remark 3.20.
