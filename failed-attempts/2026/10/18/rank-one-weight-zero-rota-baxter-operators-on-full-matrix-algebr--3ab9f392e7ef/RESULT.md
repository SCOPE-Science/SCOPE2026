# Rank-one weight-zero Rota–Baxter operators on full matrix algebras: normal forms and finite-field enumeration

## Finding
Let \(K\) be any field, \(n\geq 2\), and \(A=M_n(K)\). The **rank** of an operator \(R:A\to A\) means its rank as a \(K\)-linear map on the \(n^2\)-dimensional matrix space, not the rank of a matrix in its image. Every nonzero rank-one weight-zero Rota–Baxter operator on \(A\) is exactly one of the following two types:

**Nilpotent-image type.**
\[
 R(X)=\operatorname{tr}(VX)U,\qquad
 0\ne U\in A,\quad U^2=0,\quad 0\ne V\in A,\quad UV=VU=0.
\]
Here \((U,V)\) and \((cU,c^{-1}V)\), for \(c\in K^\times\), determine the same operator; this is the only duplication among such pairs.

**Idempotent-image type.**
\[
 R(X)=\operatorname{tr}(VX)P,\qquad
 P^2=P,\quad 1\leq\operatorname{rank}P\leq n-1,
\]
where \(V\ne0\) satisfies **exactly one** of the two orientations
\[
 (PV=0,\ VP=V),\qquad (PV=V,\ VP=0).
\]
Here the pair \((P,V)\) is uniquely determined by the operator. Both types satisfy \(R^2=0\) as **linear endomorphisms of \(A\)**, even though the image of an idempotent-image operator need not consist of square-zero matrices.

For every prime power \(q\), the number of such nonzero operators over \(\mathbb F_q\) is \(N_n(q)=N_{\mathrm{nil}}+N_{\mathrm{id}}\), with
\[
 N_{\mathrm{nil}}=\sum_{r=1}^{\lfloor n/2\rfloor}
 {n\brack r}_q{n-r\brack r}_q
 \left(\prod_{j=0}^{r-1}(q^r-q^j)\right)
 \frac{q^{(n-r)^2}-1}{q-1},
\]
\[
 N_{\mathrm{id}}=2\sum_{r=1}^{n-1}{n\brack r}_q
 q^{r(n-r)}\left(q^{r(n-r)}-1\right),
\]
where \({a\brack b}_q\) denotes the Gaussian binomial coefficient. The nilpotent summation index \(r\) is the matrix rank of \(U\); the idempotent index is the rank of \(P\). In particular,
\[
 N_2(q)=(2q+1)(q^2-1),\qquad N_2(2)=15,\quad N_2(3)=56,\quad N_3(2)=651.
\]

## Assumptions and scope
The algebra is associative, unital and the full matrix algebra \(M_n(K)\) with \(n\ge 2\). There is no restriction on the characteristic of \(K\). The weight-zero Rota–Baxter identity is, for every \(X,Y\in M_n(K)\),
\[
 R(X)R(Y)=R\bigl(R(X)Y+XR(Y)\bigr).
\]
The classification concerns precisely nonzero rank-one linear operators, not operators of arbitrary rank. The counts require a finite field \(K=\mathbb F_q\) with prime-power order \(q\); the structural classification holds over arbitrary fields. The zero operator is excluded throughout the displayed enumeration.

## Proof
**1. Reduction to a matrix coefficient.** By nondegeneracy of the ordinary trace pairing on matrices over every field, any nonzero rank-one linear operator uniquely admits a representation \(R(X)=\varphi(X)U\) with \(U\ne0\) and \(\varphi(X)=\operatorname{tr}(VX)\), \(V\ne0\), up to simultaneous reciprocal nonzero scaling. Choose \(Z\) with \(\varphi(Z)=1\). Substituting \((Z,Z)\) in the Rota–Baxter identity gives \(U^2=\lambda U\), for \(\lambda=\varphi(UZ)+\varphi(ZU)\).

Define linear forms \(\alpha(Y)=\varphi(UY)\) and \(\beta(X)=\varphi(XU)\). Substituting \((Z,Y)\) and \((X,Z)\) gives, with \(a=\alpha(Z)\), \(b=\beta(Z)\),
\[
 \lambda=a+b,\qquad \alpha=a\varphi,\qquad \beta=b\varphi.
\]
The trace pairing then gives \(VU=aV\), \(UV=bV\). Multiplying once by \(U\) and using \(U^2=\lambda U\) gives
\[
 a(a-\lambda)=0,\qquad b(b-\lambda)=0.
\]
If \(\lambda=0\), then \(a=b=0\), obtaining exactly the nilpotent-image conditions. If \(\lambda\ne0\), then \(a,b\in\{0,\lambda\}\) and \(a+b=\lambda\); hence exactly one equals \(\lambda\). Put \(P=\lambda^{-1}U\) and absorb \(\lambda\) into the trace coefficient to obtain the two idempotent orientations. A nonzero idempotent \(P\) cannot be the identity: either orientation with \(P=I\) would force \(V=0\).

**2. Sufficiency and uniqueness.** Conversely, in either normal form, \(U^2=\lambda U\), \(VU=aV\), \(UV=bV\), and \(a+b=\lambda\). Therefore
\[
 \begin{aligned}
 R(X)R(Y)&=\varphi(X)\varphi(Y)\lambda U,\\
 R\bigl(R(X)Y+XR(Y)\bigr)&=
 [\varphi(X)a\varphi(Y)+\varphi(Y)b\varphi(X)]U,
 \end{aligned}
\]
which are equal for all \(X,Y\). In the nilpotent type \(\varphi(U)=\operatorname{tr}(VU)=0\); in the idempotent type \(\varphi(P)=\operatorname{tr}(VP)=0\) from either orientation. Thus \(R^2=0\). A nonzero line spanned by a square-zero matrix contains no nonzero idempotent; the two types are disjoint. In the idempotent type the unique nonzero idempotent on the image line is \(P\), fixing the normalization of \(V\). In the nilpotent type the only redundancy is reciprocal scalar scaling.

**3. Enumerating square-zero image matrices.** Over \(\mathbb F_q\), a square-zero matrix \(U\) of matrix rank \(r\) exists precisely for \(1\le r\le\lfloor n/2\rfloor\). Choose the \(r\)-space \(\operatorname{im}U\), the \((n-r)\)-space \(\ker U\) containing it, and the induced isomorphism \(K^n/\ker U\to\operatorname{im}U\). The respective counts are
\[
 {n\brack r}_q,\quad {n-r\brack r}_q,\quad |\operatorname{GL}_r(\mathbb F_q)|.
\]
For fixed \(U\), the equations \(UV=VU=0\) say exactly that \(V\) factors through \(K^n/\operatorname{im}U\) into \(\ker U\); the space of such \(V\)'s has dimension \((n-r)^2\). Excluding zero and dividing by the free \((q-1)\)-element rescaling action gives \(N_{\mathrm{nil}}\).

**4. Enumerating idempotent images.** Every rank-\(r\) idempotent is projection onto an \(r\)-space along a complementary \((n-r)\)-space, giving \({n\brack r}_q q^{r(n-r)}\) possibilities. For any such \(P\), each orientation constrains \(V\) to one off-diagonal block of dimension \(r(n-r)\). The two blocks meet only in zero, yielding \(2(q^{r(n-r)}-1)\) nonzero choices. Every pair gives a distinct operator, establishing \(N_{\mathrm{id}}\) and the stated totals.

## Verification
The standalone `verify.py` uses only the Python standard library. Running `python verify.py` enumerates every nonzero pair of matrices \((U,V)\) in three prime-field configurations; it evaluates the **original** Rota–Baxter polynomial on all ordered pairs of matrix units (hence on all input pairs by bilinearity), compares the outcome with both proposed families, deduplicates operators as full linear maps, and compares counts and square-zero compositions. Its exact outputs are:

```
PASS n=2 q=2: nilpotent-image=3, idempotent-image=12, total=15; witnesses=15
PASS n=2 q=3: nilpotent-image=8, idempotent-image=48, total=56; witnesses=112
PASS n=3 q=2: nilpotent-image=315, idempotent-image=336, total=651; witnesses=651
```

These checks are exhaustive only for the indicated three prime fields and dimensions. The proof above, not finite sampling, establishes the arbitrary-field classification and every-prime-power formulas.

## Relationship to prior work
Gubarev, *Extremal Rota–Baxter operators on matrix algebras* (arXiv:2609.05647, first public September 4, 2026), classifies the **opposite extreme** of maximum possible minimal-polynomial degree for operators on full matrix algebras over characteristic-zero fields. The operators here all satisfy \(R^2=0\), so the extremal classification with minimum-polynomial degree \(2n-1\) does not imply this classification for \(n\ge2\).

Benito, Gubarev and Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras* (arXiv:1801.07037), §5.1, Theorem 6, already classifies weight-zero operators on \(M_2\) over algebraically closed fields of characteristic other than two, up to equivalences. Its rank-one classes correspond to the two image types exhibited here in dimension two. The present theorem includes that known small case as a boundary, but gives uniform normal forms for **all** \(n\), all characteristics, and exact counts over finite fields; these are not consequences of the quoted dimension-two theorem without further work. A related published enumeration for the exterior algebra over \(\mathbb F_2\) concerns a different underlying algebra and does not imply the result here.

## Limitations
No classification of higher operator ranks, conjugacy orbits, or other weights is claimed. No independent expert or formal-proof audit has been performed. The novelty assessment is literature-based, not a proof of worldwide priority; equivalents through associative Yang–Baxter tensors, rank-one operator varieties, or hard-to-index literature remain a genuine search risk. Exhaustive computer checks cover only three small prime-field instances, not every finite field.

## References
1. V. Gubarev, *Extremal Rota–Baxter operators on matrix algebras*, arXiv:2609.05647 (2026), https://arxiv.org/abs/2609.05647.
2. P. Benito, V. Gubarev, A. Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras*, arXiv:1801.07037 (2018), §5.1, https://arxiv.org/abs/1801.07037.
3. *Weight-zero Rota–Baxter operators on the four-dimensional exterior algebra over \(\mathbb F_2\)*, publicly indexed result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-weight-zero-rota-baxter-operators-on-the-four-dimensional-exteri--6ed2dc859a4a.
