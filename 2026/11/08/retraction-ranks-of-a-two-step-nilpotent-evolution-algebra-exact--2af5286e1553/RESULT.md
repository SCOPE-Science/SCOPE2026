# Retraction ranks of a two-step nilpotent evolution algebra: exact census and logarithmic Gaussian drift

## Finding
For a prime power \(q\) and integer \(n\geq1\), let \(E_n(q)\) be the \(2n\)-dimensional algebra over \(\mathbb F_q\) with basis \(e_1,\ldots,e_n,f_1,\ldots,f_n\) and products \(e_i^2=f_i\), all other products of basic vectors being zero. This is an evolution algebra and a commutative associative nilpotent algebra. A *retraction* is an algebra endomorphism \(P:E_n(q)\to E_n(q)\) with \(P^2=P\), where the superscript denotes composition.

For every \(0\le r\le n\), the number of retractions of image dimension \(2r\) is exactly
\[
N_{n,r}(q)=\binom nr\bigl(1+r(q-1)\bigr)^{n-r}q^{2r(n-r)}.
\]
There are no retractions of odd image dimension. Each image is isomorphic, as an algebra, to \(E_r(q)\), with \(E_0(q)=0\). In particular, the zero map and identity are the only retractions of image dimensions \(0\) and \(2n\), respectively.

For fixed \(q\), choose a retraction uniformly and denote half its image dimension by \(R_n\). Define
\[
c_n=\frac{(q-1)n}{2},\qquad b_n=1-\ln c_n,\qquad
\mu_n=\frac n2+\frac{b_n}{4\ln q},
\]
and the integer-valued discrete Gaussian
\[
G_{n,q}(r)=\frac{q^{-2(r-\mu_n)^2}}{\Theta_q(\mu_n)},
\qquad\Theta_q(u)=\sum_{j\in\mathbb Z}q^{-2(j-u)^2}.
\]
Then
\[
\bigl\|\mathcal L(R_n)-G_{n,q}\bigr\|_{\mathrm{TV}}\longrightarrow0
\quad(n\to\infty),
\]
where the finite-support law of \(R_n\) is extended by zero to all integers. Thus
\[
R_n=\frac n2-\frac{\ln n}{4\ln q}+O_{\mathsf P}(1),
\qquad \frac{R_n}{n}\xrightarrow{\mathsf P}\frac12.
\]
The shift of order \(\ln n\) distinguishes this law from Gaussian rank laws centered at an exactly linear function of dimension.

Moreover, writing \(N_n(q)=\sum_{r=0}^nN_{n,r}(q)\), one has the sharp moving-theta asymptotic
\[
N_n(q)\sim K_n(q)\Theta_q(\mu_n),\qquad
K_n(q)=\frac{2^n c_n^{n/2}q^{n^2/2}}{\sqrt{\pi n/2}}
\exp\!\left(\frac1{q-1}+\frac{b_n^2}{8\ln q}\right).
\]
Here \(\sim\) means that the ratio tends to one with \(q\) fixed; no uniformity in growing \(q\) is claimed.

## Assumptions and scope
The field has any prime-power cardinality \(q\ge2\), including characteristic two. The algebra is specified by its multiplication table, so neither associativity beyond that table nor an algebra identity is tacitly imposed. The word *idempotent* refers to composition of endomorphisms, not an algebra element satisfying \(x^2=x\). The integer \(r\) counts the image rank induced on \(E_n/E_n^2\), and the actual algebra-image dimension is \(2r\). The asymptotic limit holds for \(n\to\infty\) and each fixed \(q\).

## Proof
Let \(U=\langle e_1,\ldots,e_n\rangle\) and \(F=\langle f_1,\ldots,f_n\rangle=E_n^2=\operatorname{Ann}(E_n)\). An algebra endomorphism \(P\) must carry \(F\) into \(F\). With respect to \(U\oplus F\), it has a block matrix
\[
P=\begin{pmatrix}A&0\\C&B\end{pmatrix}.
\]
Since \(P(f_i)=P(e_i)^2\), the entries of \(B\) are exactly \(B_{ji}=A_{ji}^2\), the entrywise square \(B=A^{[2]}\). Since \(e_ie_j=0\) for \(i\ne j\) and the \(f_j\) are independent, multiplication preservation additionally requires
\[
A_{ji}A_{jk}=0\quad\text{for every row }j\text{ and columns }i\ne k.
\]
Thus each row of \(A\) contains at most one nonzero entry. Conversely, this condition with \(B=A^{[2]}\) is sufficient for multiplication preservation, with \(C\) arbitrary before imposing idempotence.

The condition \(P^2=P\) becomes
\[
A^2=A,\qquad B^2=B,\qquad CA+BC=C.
\]
Since \(A\) is row-sparse, \((A^2)^{[2]}=(A^{[2]})^2\), so \(A^2=A\) implies \(B^2=B\). For a nonzero row \(j\), let \(\phi(j)\) be its unique nonzero column and \(a_j=A_{j,\phi(j)}\). Its row in \(A^2\) is \(a_j\) times row \(\phi(j)\). Equality with row \(j\) forces \(\phi(j)\) to be a fixed point with \(A_{\phi(j),\phi(j)}=1\). Hence \(A\) is uniquely described by a set \(S\) of \(r\) roots with diagonal entries one, and, for each nonroot row, either a zero row or one nonzero scalar in one of the columns indexed by \(S\). Its rank is \(r\). There are
\[
\binom nr\bigl(1+r(q-1)\bigr)^{n-r}
\]
such matrices. This description also proves the converse: every resulting \(A\) is row-sparse and idempotent.

The matrix \(B=A^{[2]}\) has rank \(r\), as entrywise squaring is a field automorphism and commutes with the unique-root row-sparse pattern. Decompose the source of \(C\) as \(\operatorname{im}A\oplus\ker A\) and its target as \(\operatorname{im}B\oplus\ker B\). The equation \(CA+BC=C\) forces the \(\operatorname{im}A\to\operatorname{im}B\) and \(\ker A\to\ker B\) blocks to be zero; the two opposite blocks are unrestricted. Thus the solution space for \(C\) has dimension \(2r(n-r)\). This yields exactly \(q^{2r(n-r)}\) choices, proving the enumeration.

The same block equation shows \(C(\ker A)\subseteq\operatorname{im}B\). Hence the image of \(P\) has dimension \(r+r=2r\). For each root \(i\in S\), the vectors \(v_i=P(e_i)\) have disjoint supports in their \(e\)-components, so \(v_iv_j=0\) for distinct roots; their squares \(v_i^2=P(f_i)\) are linearly independent, nonzero and annihilate the image. The \(2r\) vectors \(v_i,v_i^2\) form an algebra basis of \(\operatorname{im}P\), exhibiting \(\operatorname{im}P\cong E_r(q)\).

For the asymptotic claim, write \(w_{n,r}=N_{n,r}(q)\), and regard the logarithm of the positive weights as a function of the integer \(r\). The logarithm of the binomial coefficient is discretely concave; \((n-r)\ln(1+(q-1)r)\) is concave on \([0,n]\); and \(2r(n-r)\ln q\) has constant second discrete difference \(-4\ln q\). Therefore
\[
\frac{w_{n,r-1}w_{n,r+1}}{w_{n,r}^2}\le q^{-4}
\qquad(1\le r<n).
\]
This strong log-concavity controls the tails uniformly around the mode.

For \(r=n/2+s\), with \(|s|=O(\ln n)\), Stirling's formula and Taylor expansion give uniformly
\[
\ln w_{n,r}=H_n-2s^2\ln q+b_ns+o(1),
\]
where
\[
H_n=\frac{n^2}{2}\ln q+n\ln2-\frac12\ln(\pi n/2)
+\frac n2\ln c_n+\frac1{q-1}.
\]
Completing the square yields
\[
\ln w_{n,r}=\ln K_n(q)-2(r-\mu_n)^2\ln q+o(1)
\]
uniformly when \(|r-\mu_n|\) is bounded (indeed on every fixed bounded window). The adjacent-ratio expansion places a mode within bounded distance of \(\mu_n\); the displayed strong log-concavity bounds the remaining tails by a summable discrete-Gaussian envelope. Finite-window convergence followed by tail truncation proves total-variation convergence. Summing the same approximation with the same tail bound proves \(N_n(q)\sim K_n(q)\Theta_q(\mu_n)\). The logarithmic drift and the law of large numbers follow immediately.

## Verification
The standalone `verify.py` enumerates all images of the generating vectors and checks the algebra-homomorphism equations and idempotence directly, independently of the root-counting argument. It matches the full rank census for \((n,q)=(1,2),(2,2),(3,2),(2,3),(2,4)\), implementing \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). In particular the counts by \(r\) are \((1,16,1)\) at \((n,q)=(2,2)\), \((1,192,144,1)\) at \((3,2)\), and \((1,128,1)\) at \((2,4)\). It also computes the exact finite \(n\) distribution and its moving-Gaussian approximation for several fixed fields and \(n\le1000\). Execution completed with `VERIFY_OK`. These finite checks are corroboration, not an infinite proof.

Reproduce with `python verify.py`, using Python 3.9 or later and no third-party packages.

## Relationship to prior work
Elduque and Labra (2016) establish structural nilpotent evolution-algebra decompositions and explicitly identify direct sums of two-dimensional nilpotent ideals in their Corollary 2.6; this decomposition is prior work, not the present contribution. Omirov, Rozikov and Velasco (2017) develop large nilpotent evolution-algebra families and their type classification. Boudi, Cabrera Casado and Siles Molina (2020) investigate natural families, algebra homomorphisms and evolution rank. The 2026 survey of Kaygorodov, Martín González and Viruel provides a broad account of evolution-algebra structure, automorphisms and idempotent **elements**. These sources motivate the object but, in the inspected material, do not give the rank census of idempotent **endomorphisms** or the logarithmically drifting discrete-Gaussian law. Sen (2019) counts idempotent set maps via height-one rooted forests; this supplies a combinatorial precursor to the weighted root patterns of the quotient block but does not count the independent linear extension block. Ordinary idempotent partial-function counting is therefore an ingredient of the proof, not a separate claimed discovery. Results on perfect or maximal-nilindex evolution algebras and free nilpotent Lie retractions concern non-equivalent objects or invariants.

## Limitations
This result covers the particular direct sum of the smallest nonzero nilpotent evolution algebra, not arbitrary evolution algebras. It counts labeled, field-linear endomorphisms rather than isomorphism classes or maps modulo automorphisms. The asymptotic fixes the field order. The centered discrete Gaussian moves with \(n\); an unconditional fixed limiting distribution is not asserted. Search and comparison do not establish absolute publication priority; an unidentified general theorem on weighted partial transformations or algebra retractions could imply parts of the count. Independent review is not included.

## References
- B. A. Omirov, U. A. Rozikov and M. V. Velasco, *A class of nilpotent evolution algebras*, arXiv:1711.05030, first posted 2017-11-14. https://arxiv.org/abs/1711.05030
- A. Elduque and A. Labra, *On nilpotent evolution algebras*, arXiv:1602.01590, first posted 2016-02-04; particularly Corollary 2.6. https://arxiv.org/abs/1602.01590
- N. Boudi, Y. Cabrera Casado and M. Siles Molina, *Natural families in evolution algebras*, arXiv:2006.14460, first posted 2020-06-25. https://arxiv.org/abs/2006.14460
- I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248, first posted 2026-10-15. https://arxiv.org/abs/2610.22248
- E. Sen, *Exceptional Sequences and Idempotent Functions*, arXiv:1909.05887, first posted 2019-09-12. https://arxiv.org/abs/1909.05887
