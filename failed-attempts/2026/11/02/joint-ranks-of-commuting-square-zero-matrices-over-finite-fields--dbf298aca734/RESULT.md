# Joint ranks of commuting square-zero matrices over finite fields

## Finding

Let \(q\) be any prime power, let \(r\geq1\), and fix a matrix \(A\in M_{2r}(\mathbb F_q)\) with \(A^2=0\) and \(\operatorname{rank} A=r\). Such matrices form one similarity class. For integers \(k,b\), set
\[
N_{q,r}(k,b)=\#\{B\in M_{2r}(\mathbb F_q):B^2=0,\ AB=BA,\ \operatorname{rank}(AB)=k,\ \operatorname{rank}B=b\}.
\]
Define the Gaussian coefficient \({m\brack j}_q=\prod_{i=0}^{j-1}(q^m-q^i)/(q^j-q^i)\), with the empty product equal to \(1\), and \(G_j(q)=\prod_{i=0}^{j-1}(q^j-q^i)=|\mathrm{GL}_j(\mathbb F_q)|\), with \(G_0(q)=1\). Let
\[
R_{s,h}(q)={s\brack h}_q\prod_{i=0}^{h-1}(q^s-q^i),
\]
which counts the rank-\(h\) elements of \(M_s(\mathbb F_q)\), including \(R_{0,0}=1\).

**Theorem (complete joint-rank census).** The number \(N_{q,r}(k,b)\) is zero unless
\[
0\leq k\leq\lfloor r/2\rfloor,\qquad b=2k+h,\qquad 0\leq h\leq r-2k.
\]
For each such \(k,h\) it is exactly
\[
\boxed{N_{q,r}(k,2k+h)
={r\brack k}_q\,{r-k\brack k}_q\,G_k(q)\,
q^{2k(r-k)}R_{r-2k,h}(q).}
\]
Every permitted pair occurs. This simultaneously classifies the ranks of the second square-zero operator and its product with a fixed maximal-rank square-zero operator, with exact multiplicities over every finite field.

**Asymptotic equidistribution.** Fix \(r\). Among matrices \(B\) chosen uniformly subject to \(B^2=0\) and \(AB=BA\), the probability that \(\operatorname{rank}B=r\) tends to \(1\) as \(q\to\infty\) through prime powers. Moreover, the conditional distribution of \(\operatorname{rank}(AB)\) converges to the uniform distribution on \(\{0,1,\ldots,\lfloor r/2\rfloor\}\), whether or not one also conditions on \(\operatorname{rank}B=r\). Explicitly, for every allowed \(k\),
\[
\Pr(\operatorname{rank}(AB)=k\mid B^2=0,AB=BA)
\longrightarrow\frac1{\lfloor r/2\rfloor+1}.
\]

## Assumptions and scope

All ranks and equalities are over \(\mathbb F_q\); the characteristic is arbitrary, including \(2\). The first matrix \(A\) is fixed rather than sampled and must have the largest possible rank for a square-zero matrix in even dimension. No invertibility of \(B\) is assumed or possible unless the underlying space is zero; here \(r\geq1\). Counts concern actual matrices \(B\), not simultaneous similarity classes of pairs. The group order and Gaussian coefficients use the standard nonnegative-integer conventions, including dimension zero.

## Proof

**1. Centralizer coordinates.** Because \(A^2=0\) and \(\operatorname{rank} A=r\), its kernel equals its image, and a suitable basis makes
\[
A=\begin{pmatrix}0&I_r\\0&0\end{pmatrix}.
\]
For an arbitrary \(2r\)-by-\(2r\) block matrix \(B\), direct comparison of \(AB\) and \(BA\) gives the unique form
\[
B=\begin{pmatrix}P&Y\\0&P\end{pmatrix},\qquad P,Y\in M_r(\mathbb F_q).
\]
Then
\[
B^2=0\quad\Longleftrightarrow\quad P^2=0\ \text{and}\ PY+YP=0,
\]
and \(AB=\begin{pmatrix}0&P\\0&0\end{pmatrix}\), hence \(\operatorname{rank}(AB)=\operatorname{rank}P\). The equation remains valid in characteristic \(2\); no division by two is used.

**2. The free block controlling the other rank.** Fix a square-zero \(P\) of rank \(k\). Its image lies in its kernel, so \(2k\leq r\). Set \(s=r-2k\). There is an ordered decomposition \(\mathbb F_q^r=U\oplus H\oplus T\) with dimensions \(k,s,k\), for which
\[
P=\begin{pmatrix}0&0&I_k\\0&0&0\\0&0&0\end{pmatrix}.
\]
Write \(Y\) in this three-block decomposition. Multiplying out \(PY+YP=0\) shows that its entire solution space has exactly the form
\[
Y=\begin{pmatrix}C&D&E\\0&Q&F\\0&0&-C\end{pmatrix},
\]
where \(C\in M_k\), \(D\in M_{k\times s}\), \(E\in M_k\), \(F\in M_{s\times k}\), and \(Q\in M_s\) are arbitrary. Thus for each fixed \(Q\), precisely \(q^{2k^2+2ks}=q^{2k(r-k)}\) matrices \(Y\) are allowed.

To determine the rank of \(B\), view it as the map \((x,y)\mapsto(Px+Yy,Py)\) on \(\mathbb F_q^r\oplus\mathbb F_q^r\). Its bottom projection has image of dimension \(k\). Inside the kernel of that projection the attainable upper coordinates are \(\operatorname{im}P+Y(\ker P)\). In the displayed decomposition, \(\ker P=U\oplus H\), \(Y(U)\subseteq U\), and the image of \(Y(H)\) modulo \(U\) is precisely \(Q(H)\). Hence
\[
\operatorname{rank}B=k+(k+\operatorname{rank}Q)=2k+\operatorname{rank}Q.
\]
In particular \(b=2k+h\) with \(0\leq h\leq s\), and each \(h\) is attainable.

**3. Counting the first block.** A rank-\(k\) square-zero matrix \(P\) is uniquely specified by its \(k\)-dimensional image \(U\), its \((r-k)\)-dimensional kernel \(K\supseteq U\), and the induced isomorphism \(\mathbb F_q^r/K\to U\). These choices number
\[
{r\brack k}_q\,{r-k\brack k}_q\,G_k(q).
\]
For each such \(P\), Step 2 gives \(q^{2k(r-k)}\) choices of \(Y\) for every fixed \(Q\). Finally, the number of \(s\)-by-\(s\) matrices \(Q\) of rank \(h\) is \(R_{s,h}(q)\): first choose an \(h\)-dimensional image and then a surjection from \(\mathbb F_q^s\) to that image. Multiplication of these independent exact counts proves the formula and completeness.

**4. Asymptotic equidistribution.** For fixed integers in range, Gaussian coefficients, invertible-matrix counts, and rank-\(h\) counts are monic polynomials in \(q\) with degrees \(k(r-k)\), \(k(r-2k)\), \(k^2\), and \(h(2s-h)\), respectively. The degree of the displayed count is therefore
\[
4k(r-k)+h(2s-h)=r^2-(s-h)^2.
\]
Exactly the terms with \(h=s\), equivalent to \(\operatorname{rank}B=r\), have the maximum degree \(r^2\). For every \(k\in\{0,\ldots,\lfloor r/2\rfloor\}\), there is precisely one such term, with leading coefficient \(1\); all other terms have strictly lower degree. Summing the finitely many terms proves both concentration on rank \(r\) and the stated uniform limit for the product rank. No uniformity in \(r\) as \(q\) grows is asserted.

## Verification

The included standalone `verify.py` directly enumerates \(P,Y\) over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), checks the identities \(AB=BA\) and \(B^2=0\) on complete block matrices, independently row-reduces \(AB\) and \(B\), and compares every joint-rank multiplicity to the closed formula. It uses \(\mathbb F_4=\mathbb F_2[z]/(z^2+z+1)\). Run `python verify.py` with a Python 3 interpreter; no external packages are needed.

The five exhaustive parameter instances were \((q,r)=(2,1),(2,2),(3,2),(4,2),(2,3)\). The corresponding totals of admissible \(B\) were respectively \(2,28,153,496,1184\), with every individual stratum matching the formula. These checks confirm the implementation and low-dimensional cases, but the preceding proof, rather than finite enumeration, establishes the theorem in all dimensions and finite fields.

## Relationship to prior work

Košir's 2026 survey of commuting nilpotent Jordan types focuses on which pairs of Jordan partitions occur; it explicitly works over infinite fields for its general survey. Kokol Bukovšek, Košir, Novak, and Oblak (2007), Proposition 2.2 and Theorem 2.3, characterize which square-zero matrices are products of commuting square-zero factors; their sharp bound \(\operatorname{rank}(AB)\leq r/2\) agrees with the present support, but does not specify the number of compatible factors of each individual rank. Mohammadian (2012) generalizes rank bounds under weaker hypotheses; that does not supply the joint frequencies. Bogdanić et al. (2024) classify possible Jordan types in the centralizer of a matrix with two equal Jordan blocks, not finite-field joint-rank multiplicities for a fixed maximal-rank square-zero matrix with arbitrarily many blocks.

The new assertion is the full family of finite-field joint counts and the uniform product-rank limit, **not** the existence bound, the block-centralizer form, or the standard Gaussian coefficients. An equivalent enumeration elsewhere in the extensive matrix-pair literature remains possible.

## Limitations

No claim is made about pairs with \(A\) of nonmaximal square-zero rank, about nilpotent matrices of index greater than two, or about counts of conjugacy orbits. The limiting law is for fixed \(r\) and increasing field size. Earlier work may encode equivalent information in a different representation-theoretic language. This result has undergone only self-review, not independent validation.

## References

1. T. Košir, *Jordan types for pairs of commuting nilpotent matrices: A survey*, arXiv:2606.02026v1 (2026-06-01), https://arxiv.org/abs/2606.02026.
2. D. Kokol Bukovšek, T. Košir, N. Novak and P. Oblak, *Products of Commuting Nilpotent Operators*, Electronic Journal of Linear Algebra 16 (2007), 237–247, DOI:10.13001/1081-3810.1199; author's copy https://users.fmf.uni-lj.si/kosir/papers/produkti.pdf.
3. A. Mohammadian, *Sums and Products of Square-Zero Matrices*, Communications in Algebra 40 (2012), 4568–4574, DOI:10.1080/00927872.2011.613423.
4. D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak and K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, Linear Algebra and its Applications (2024), DOI:10.1016/j.laa.2024.03.008, arXiv:2212.08425.
