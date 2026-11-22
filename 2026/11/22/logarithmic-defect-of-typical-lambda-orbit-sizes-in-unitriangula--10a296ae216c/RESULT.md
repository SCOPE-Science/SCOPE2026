# Logarithmic defect of typical lambda-orbit sizes in unitriangular radical braces

## Finding

Let \(q\) be any prime power and \(n\ge2\). Give the strictly upper-triangular matrix algebra \(A_n=\operatorname{NT}_n(\mathbb F_q)\) its radical two-sided brace structure \(a\circ b=a+b+ab\). Its lambda action is \(\lambda_a(b)=b+ab\). The main finding is a uniform quantitative law for the size of a **uniformly sampled lambda-orbit point**: the orbit exponent has a negative, order-\(n\log_q n\) correction to its quadratic maximum, with expected absolute error bounded linearly in \(n\). A positive rank-defect transfer is included as a self-contained proof device and finite check, not asserted as a newly discovered group action or a previously unknown enumerative invariant.

For \(N=n-2\) and \(M=N(N+1)/2\), every fixed prime power \(q\) admits a constant \(C_q\) such that a uniformly chosen \(B\in A_n\) satisfies

\[
\boxed{\mathbb E\left|\log_q|\Lambda(B)|-\left(M-N\log_q N\right)\right|\le C_q n,\qquad n\ge3.}
\]

Thus \(\log_q|\Lambda(B)|=n^2/2-n\log_q n+O_{\mathsf P,q}(n)\). The statement is about the **integrated suffix-rank statistic**, not the distribution of the rank of a single random triangular matrix.

**Exact transfer used in the proof.** Initialize \(H_0(0,0)=1\), with all other entries zero. For \(m=0,1,\ldots,N-1\), take every nonzero \(H_m(d,s)\) and make both updates

\[
\begin{aligned}
H_{m+1}(d,s+d)&\mathrel{+}=H_m(d,s)\big(q^{m+1}-q^{m-d}\big),\\
H_{m+1}(d+1,s+d+1)&\mathrel{+}=H_m(d,s)q^{m-d}.
\end{aligned}
\]

For each \(0\le\ell\le M\), the number of points on lambda-orbits of cardinality \(q^\ell\) is

\[
E_{n,q}(\ell)=q^{n-1}\sum_{d=0}^{N}H_N(d,M-\ell),
\]

and the number of **distinct** such orbits is exactly

\[
\boxed{\mathcal O_{n,q}(\ell)=q^{n-1-\ell}\sum_{d=0}^{N}H_N(d,M-\ell).}
\]

In particular, exactly \(q^{n-1}\) points have singleton orbit, the largest orbit has length \(q^M\), and exactly \(q(q-1)^{n-2}\) distinct orbits have this maximum size. These formulas include \(n=2\), when all \(q\) orbits are singletons.

There is also a uniform typical-size law. If \(B\) is uniformly sampled from \(A_n\), then for every fixed prime power \(q\), with a constant \(C_q\) independent of \(n\),

\[
\mathbb E\left|\log_q|\Lambda(B)|-\left(\frac{(n-2)(n-1)}2-(n-2)\log_q(n-2)\right)\right|\le C_q n
\]

for \(n\ge3\). In particular, as \(n\to\infty\) with \(q\) fixed,

\[
\log_q|\Lambda(B)|=\frac{n^2}{2}-n\log_q n+O_{\mathsf P,q}(n).
\]

The distinct mathematical assertion assessed here is the quantified n-logarithm typical-orbit law. The transfer is presented for transparent independent verification and does not claim a novelty independent of the extensive earlier unitriangular left-orbit and template literature.

## Assumptions and scope

\(q\) is a prime power and all ranks and operations are over \(\mathbb F_q\). The base algebra consists of **strictly** upper-triangular matrices. The two-sided brace operations are ordinary vector addition and \(a\circ b=a+b+ab\); its circle group is canonically the upper unitriangular group under \(a\mapsto I+a\). Lambda-orbits are under the **whole** circle group. Indices are 1-based. For \(n=2\), \(N=M=0\), the transfer has no steps. The probability statement concerns a uniformly chosen element of this additive set; no independent uniform distribution on the orbit *set* is claimed. The displayed expected-deviation bound is for fixed \(q\) and a \(q\)-dependent constant; it does not assert a uniform bound for fields whose orders tend to infinity.

## Proof

**Orbit size as a sum of suffix ranks.** For a fixed \(b\in A_n\), the orbit is the affine set \(b+A_nb\), because \(\lambda_a(b)=(I+a)b\) and \(I+A_n\) is the entire circle group. In the \(i\)-th row, the product \(ab\) is an arbitrary linear combination of the rows of \(b\) below row \(i\); its nonzero coordinates lie strictly right of column \(i\). The coefficients \(a_{ik}\), as \(i\) varies, are independent. Therefore

\[
\dim_{\mathbb F_q}A_nb=\sum_{i=1}^{n-2}\operatorname{rank}(b_{i+1},\ldots,b_{n-1}),
\]

where \(\operatorname{rank}(b_{i+1},\ldots,b_{n-1})\) means the rank of those rows as vectors of length \(n\). This shows every orbit is an affine space, hence has size a power of \(q\).

**Rank-defect transfer.** Inspect the last \(m\) potentially nonzero rows of \(b\), beginning with row \(n-1\) and moving upward, for \(m=0,\ldots,N\). Their nonzero coordinates fit in the last \(m+1\) columns. Write their rank \(R_m=m-D_m\), with \(D_0=0\). When the next row is appended above, it contributes \(m+1\) independent uniform field coordinates. The previous span has dimension \(m-D_m\), embedded in a space of dimension \(m+1\); thus the new row belongs to this span in exactly \(q^{m-D_m}\) of the \(q^{m+1}\) choices. In that case the rank does not increase, so the defect increases by 1; otherwise the defect stays constant. The cumulative defect sum changes by the new defect. These two cases give exactly the two claimed updates for \(H_m(d,s)\). The original matrix's first row, containing \(n-1\) entries, is unconstrained in this transfer, yielding the factor \(q^{n-1}\).

The orbit-size exponent is the sum of all suffix ranks:

\[
\log_q|\Lambda(b)|=\sum_{m=1}^{N}R_m=M-\sum_{m=1}^{N}D_m.
\]

Hence the coefficient formula counts each point of given exponent exactly once. Every such orbit has \(q^\ell\) points, so division yields the number of distinct orbits; the division is exact because these are disjoint group-action orbits.

**Extremes.** The exponent vanishes exactly when all last \(N\) rows are zero. Only the unrestricted first row remains: \(q^{n-1}\) singleton orbits. The exponent equals \(M\) exactly when the defects all vanish; at the transition from \(m\) to \(m+1\) this permits \(q^{m+1}-q^m=q^m(q-1)\) rows. Thus there are \(q^{n-1}\,q^{N(N-1)/2}(q-1)^N\) maximal-orbit points. Dividing by \(q^M\), and using \(n-1=N+1\), gives exactly \(q(q-1)^N\) maximal orbits.

**Typical exponent.** For uniform \(b\), the defect chain evolves as

\[
\Pr(D_{m+1}=d+1\mid D_m=d)=q^{-d-1},\quad
\Pr(D_{m+1}=d\mid D_m=d)=1-q^{-d-1}.
\]

Equivalently, the holding time in state \(d\) before the next defect increment is a geometric random variable of success probability \(q^{-d-1}\); these holding times may be constructed independently. Let \(T_k\) be the time of the \(k\)-th increment, so \(\mathbb E T_k=q(q^k-1)/(q-1)\). For \(m\ge1\), write \(h=\lfloor\log_q m\rfloor\). For every integer \(u\ge1\), the event \(D_m\ge h+u\) implies that the last required holding time was completed by time \(m\). This gives \(\Pr(D_m\ge h+u)\le m q^{-(h+u)}\le q^{1-u}\). Similarly, \(D_m\le h-u\) implies \(T_{h-u+1}>m\), and Markov's inequality gives \(\Pr(D_m\le h-u)\le q^{2-u}/(q-1)\) when the event is possible. Summing these geometric tail bounds proves \(\mathbb E|D_m-\lfloor\log_q m\rfloor|\le K_q\) with \(K_q\) independent of \(m\). Since \(\sum_{m=1}^{N}\lfloor\log_q m\rfloor=N\log_q N+O(N)\), the triangle inequality gives

\[
\mathbb E\left|\sum_{m=1}^{N}D_m-N\log_q N\right|\le C_q N.
\]

Substituting the exponent identity gives the claimed \(L^1\) bound and the probabilistic statement by Markov's inequality. This is an infinite-size argument; finite enumeration alone is not being used to infer it.

## Verification

The accompanying standard-library program `verify.py` implements the transfer with exact integers and independently enumerates **actual** lambda-action orbit partitions via matrix multiplication for \((n,q)=(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(4,3)\). Both the point multiplicities and the orbit multiplicities agree. It also checks exact total-element counts and divisibility for each \(2\le n\le21\) and \(q\in\{2,3,4,5,7\}\). The program is a finite cross-check of the independent proof, not an assertion of exhaustive testing of all dimensions or fields.

For example, \(n=4,q=2\) has \(8,12,4,2\) distinct lambda-orbits of respective sizes \(1,2,4,8\); \(n=5,q=2\) has \(16,56,24,44,12,4,2\) orbits of respective sizes \(1,2,4,8,16,32,64\).

## Relationship to prior work

Properzi and Van Antwerpen [1] study common-divisor graphs of lambda-orbits of arbitrary finite skew braces, and introduce the numerical orbit-length invariant; their general graph bounds do not give the all-size multiplicities for the unitriangular radical family. Yan [2] explicitly uses the left action of the upper unitriangular group on strictly upper-triangular matrices by row operations, and develops double-orbit template and character machinery. Therefore the underlying action, the row-operation interpretation, and orbit–stabilizer principles are **not** claimed to be new. The distinct claim assessed here is the **quantitative typical integrated-suffix-rank law** for lambda-orbit logarithms. The transfer and extremal counts are displayed as proof tools and concrete specializations, not as independently established historical firsts. Van Peski [3] studies the terminal rank and logarithmic rank defect of a random strictly triangular matrix; the statistic here is instead the **sum of ranks of all trailing row blocks**, which controls lambda-orbit sizes. The random-rank argument leverages a related mechanism but is stated and proved separately.

## Limitations

The theorem concerns the uniform-point size of lambda-orbits in this radical-brace family, not arbitrary skew braces or conjugacy/coadjoint orbits. The dimension-by-dimension transfer is an explicit computation used for verification, not a claim of historical first occurrence. The \(O_q(n)\) fluctuation bound does not identify any centered limiting law. Earlier unitriangular orbit literature may contain an equivalent enumeration hidden in a more general form; the evidence inspected does not establish this, but historical priority is not independently certified. The quantitative rank law is proved for fixed \(q\), and no uniform double limit in \(n\) and \(q\) is asserted.

## References

[1] S. Properzi and A. Van Antwerpen, *Common divisor graphs for skew braces*, first arXiv posting 21 June 2023, arXiv:2306.12415, https://arxiv.org/abs/2306.12415 .

[2] N. Yan, *Representations of Finite Unipotent Linear Groups by the Method of Clusters*, arXiv:1004.2674 (2010), especially Section 3.1 on upper unitriangular left multiplication and row operations, https://arxiv.org/abs/1004.2674 .

[3] R. Van Peski, *The rank of a random triangular matrix over \(\mathbb F_q\)*, first arXiv posting 28 July 2024, arXiv:2407.19578, especially the logarithmic rank-defect theorem, https://arxiv.org/abs/2407.19578 .
