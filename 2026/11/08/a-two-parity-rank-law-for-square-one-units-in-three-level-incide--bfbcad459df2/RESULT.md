# A two-parity rank law for square-one units in three-level incidence algebras

## Finding
Let \(n\geq1\), \(q=2^f\) with \(f\geq1\), and let \(P_n\) be the finite poset formed from three antichains \(X,Y,Z\), each of cardinality \(n\), with every element of \(X\) below every element of \(Y\) and every element of \(Y\) below every element of \(Z\). Write \(I_n=I(P_n,\mathbb F_q)\) for the incidence algebra. A *square-one unit* is a unit \(u\in I_n\) satisfying \(u^2=1\); the identity is included.

Every square-one unit has a unique block expression
\[
u=1+\begin{pmatrix}0&A&C\\0&0&B\\0&0&0\end{pmatrix},\qquad A,B,C\in M_n(\mathbb F_q),\quad AB=0.
\]
Here the diagonal block of the displayed nilpotent element is zero, and the identity has diagonal blocks equal to identity matrices. (These blocks describe comparable pairs, not arbitrary entries inside an antichain.) Define \(R_n(u)=\operatorname{rank} A\). For every \(0\leq r\leq n\), its exact multiplicity is
\[
T_{n,r}(q)=q^{n^2+n(n-r)}\binom{n}{r}_q\prod_{i=0}^{r-1}(q^n-q^i).
\]
Here \(\binom{n}{r}_q\) denotes the Gaussian binomial coefficient, and empty products are one. In particular the total number of square-one units is \(T_n(q)=\sum_{r=0}^n T_{n,r}(q)\).

Put \(D_s(q)=\prod_{i=1}^{s}(1-q^{-i})\), \(D_\infty(q)=\prod_{i\geq1}(1-q^{-i})>0\), and
\[
\Theta_{q,0}=\sum_{j\in\mathbb Z}q^{-j^2},\qquad
\Theta_{q,1}=\sum_{j\in\mathbb Z}q^{-j(j-1)}.
\]
For \(\varepsilon\in\{0,1\}\) and \(n\equiv\varepsilon\pmod2\), as \(n\to\infty\) through that parity,
\[
T_n(q)=\frac{q^{2n^2+\lfloor n^2/4\rfloor}}{D_\infty(q)}
\left(\Theta_{q,\varepsilon}+O_q(q^{-n/2})\right).
\]
If \(u\) is uniform among these units, then for each fixed integer \(j\), along even \(n=2m\),
\[
\Pr(R_n=m+j)=\frac{q^{-j^2}}{\Theta_{q,0}}+O_q(q^{-n/2}),
\]
and along odd \(n=2m+1\),
\[
\Pr(R_n=m+j)=\frac{q^{-j(j-1)}}{\Theta_{q,1}}+O_q(q^{-n/2}).
\]
The entire centered laws converge in total variation with error \(O_q(q^{-n/2})\). Thus \(R_n/n\to1/2\) in probability, although its centered fluctuations remain nondegenerate and parity-dependent.

Furthermore, interpreting \(B\) and \(A\) as consecutive maps of the length-two complex \(\mathbb F_q^n\xrightarrow{B}\mathbb F_q^n\xrightarrow{A}\mathbb F_q^n\), its middle homology vanishes with probability \(1-O_q(q^{-n/2})\) under the **uniform measure on all admissible pairs** \((A,B)\) with \(AB=0\). This uniform-pair measure is *not* the sequential measure that first chooses \(A\) uniformly among all matrices and then chooses \(B\) uniformly subject to \(AB=0\).

## Assumptions and scope
The partial order includes all transitive comparabilities between \(X\) and \(Z\). The field has characteristic two, though the finite-field matrix counting steps are valid in any characteristic. The limit holds for fixed \(q\), not for joint growth of \(q\) and \(n\). The formula counts solutions of \(u^2=1\) including \(u=1\), not only group elements of exact order two. Rank means the displayed \(X\)-to-\(Y\) block rank; it is not the rank of \(u\), which is always invertible.

## Proof
**1. Reduction to two consecutive matrices.** The incidence algebra has exactly the diagonal coordinates, the \(X\)-to-\(Y\) coordinates, the \(Y\)-to-\(Z\) coordinates, and the \(X\)-to-\(Z\) coordinates. A square-one element has diagonal coefficients \(a\) satisfying \(a^2=1\). Since \(\mathbb F_q\) is a field of characteristic two, \((a+1)^2=0\) implies \(a=1\). Hence \(u=1+N\) with \(N\) in the radical; \((1+N)^2=1+N^2\). Multiplication of the three block coordinates gives \(N^2\) equal to the \(X\)-to-\(Z\) block \(AB\), and no other nonzero blocks. Thus \(u^2=1\) if and only if \(AB=0\). The block \(C\) is unrestricted, yielding \(q^{n^2}\) choices.

**2. Rank enumeration.** To choose rank-\(r\) matrices \(A:\mathbb F_q^n\to\mathbb F_q^n\), choose an \(r\)-dimensional image (\(\binom{n}{r}_q\) choices), then choose a surjection to that image (\(\prod_{i=0}^{r-1}(q^n-q^i)\) choices). For any such \(A\), \(\dim\ker A=n-r\), and \(AB=0\) means all \(n\) columns of \(B\) lie in \(\ker A\), giving exactly \(q^{n(n-r)}\) choices. Multiplying proves the rank formula. In terms of the finite products,
\[
T_{n,r}(q)=q^{2n^2+r(n-r)}\frac{D_n(q)^2}{D_r(q)D_{n-r}(q)^2}.
\]
No approximation is used here.

**3. Sharp sum and centered law.** Write \(n=2m+\varepsilon\) and \(r=m+j\). Then \(r(n-r)=\lfloor n^2/4\rfloor-j^2\) for \(\varepsilon=0\), while \(r(n-r)=\lfloor n^2/4\rfloor-j(j-1)\) for \(\varepsilon=1\). For every fixed \(j\), as \(m\to\infty\), the product ratio \(D_n(q)^2/(D_r(q)D_{n-r}(q)^2)\) tends to \(1/D_\infty(q)\). For all admissible \(r\), it is bounded above by a constant depending only on \(q\), because \(D_s(q)\ge D_\infty(q)>0\). Hence dominated convergence against the summable Gaussian tails proves the sharp leading constants and the centered probability limits.

For the stated error, note \(|D_s(q)-D_\infty(q)|\le C_q q^{-s}\). Where \(r\) and \(n-r\) are at least \(n/2-|j|-1\), the ratio differs from \(1/D_\infty(q)\) by at most \(C_q q^{-n/2+|j|+1}\). Multiplying by \(q^{-j^2}\) or \(q^{-j(j-1)}\) and summing over \(j\) yields \(O_q(q^{-n/2})\), since all exponentially tilted Gaussian series converge. Far-tail terms outside the valid rank window are superexponentially small. Dividing by the sharp total count yields the asserted total-variation bound and the fixed-\(j\) estimates.

**4. Exactness of the associated complex.** Conditioned on \(A\) of rank \(r\), the map \(B:\mathbb F_q^n\to\ker A\) is uniform. Its probability of surjectivity is
\[
\prod_{i=0}^{n-r-1}(1-q^{i-n}).
\]
The failure probability is at most \(\sum_{i=0}^{n-r-1}q^{i-n}\le(q-1)^{-1}q^{-r}\). The centered rank law, together with its Gaussian tail bound, gives \(\mathbb E[q^{-R_n}]=O_q(q^{-n/2})\). Therefore \(\Pr(\operatorname{im}B\ne\ker A)=O_q(q^{-n/2})\), as claimed.

## Verification
Run `python3 verify.py` with Python 3.10 or newer. The verifier exhaustively enumerates \(A,B\) with \(AB=0\) over \(\mathbb F_2\) for \(n=1,2,3\), and over \(\mathbb F_4\) for \(n=2\) using the polynomial basis with defining relation \(t^2+t+1=0\). It independently counts rank multiplicities before multiplying by the free \(C\)-block choices. For binary \(n=2\), the rank spectrum is \((256,576,96)\), totaling \(928\). For binary \(n=3\), it is \((262144,1605632,1204224,86016)\), totaling \(3158016\). For \(n=2\) over \(\mathbb F_4\), it is \((65536,307200,46080)\), totaling \(418816\). Arithmetic checks demonstrate convergence of the sharp normalizing constant. Finite tests corroborate but do not substitute for the proof of the infinite statements.

## Relationship to prior work
Gargate and Gargate (2019), *Involutions on Incidence Algebras of Finite Posets*, count square-one elements in incidence algebras under the explicit restriction that the field characteristic differs from two. Their semisimple diagonal method does not apply to the unipotent square-one locus here. Their 2020 work on potent elements also assumes that characteristic does not divide the relevant exponents; these characteristic-two square-one equations are not covered.

Catanzaro and Zabka (2019), *A Model for Random Chain Complexes*, analyze a model that selects consecutive maps sequentially, choosing each next matrix uniformly within the kernel allowed by its predecessor. For fixed \(n\), their conditional rank laws and large-field asymptotics concern a different measure: under sequential sampling the first \(n\)-by-\(n\) differential has rank \(n-O_{\Pr}(1)\) for fixed \(q\) as \(n\to\infty\), whereas under uniform sampling of the entire space \(AB=0\), its rank concentrates near \(n/2\). (Its invertibility probability under sequential sampling approaches the positive constant \(D_\infty(q)\), not one.) The matrix-rank counting lemma in their paper is classical and is used here without novelty claims.

Ginzburg and Pasechnik (2016) study uniformly distributed *ungraded* square-zero operators; their formula is not a rank-law for a fixed three-term graded model. Ababneh and Kahle (2026) prove almost-sure statements over the real numbers for rank strata of graded complexes, not discrete rank probabilities over fixed finite fields. The 1981 variety-of-complexes perspective provides relevant structural background. The novelty asserted here is specifically the characteristic-two incidence-algebra interpretation, its exact uniform-pair multiplicities, and the parity-dependent fixed-field asymptotic distribution and homological consequence; it is not a claim to invent the Gaussian matrix-rank formula.

## Limitations
No classification of conjugacy classes of square-one units is claimed. The asymptotic is for complete three-level posets with equal level cardinalities, not arbitrary height-three posets or arbitrary graded complexes. Independence of this result from all possible older enumeration treatments is not established. The literature comparison identified directly relevant prior finite-field chain-complex counting, and potential encompassing treatments of varieties of complexes remain an originality risk. Independent validation has not been performed.

## References
1. M. J. Catanzaro and M. J. Zabka, *A Model for Random Chain Complexes*, arXiv:1901.00964 (first public 2019-01-04), https://arxiv.org/abs/1901.00964.
2. I. Gargate and M. Gargate, *Involutions on Incidence Algebras of Finite Posets*, arXiv:1907.06805 (first public 2019-07-16), https://arxiv.org/abs/1907.06805.
3. I. Gargate and M. Gargate, *\((k+1)\)-potent Matrices in triangular matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243 (first public 2020-08-30), https://arxiv.org/abs/2009.04243.
4. V. L. Ginzburg and D. V. Pasechnik, *Random Chain Complexes*, arXiv:1602.08538 (first public 2016-02-27), https://arxiv.org/abs/1602.08538.
5. A. Ababneh and M. Kahle, *Random chain complexes of real vector spaces*, arXiv:2602.10783 (first public 2026-02-11), https://arxiv.org/html/2602.10783v1.
