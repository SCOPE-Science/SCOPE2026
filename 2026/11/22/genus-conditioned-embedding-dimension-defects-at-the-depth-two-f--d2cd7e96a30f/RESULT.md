# A fixed-genus total-variation limit for embedding-dimension defects at depth two

## Finding

The result is the density-conditioned convergence in total variation below, including convergence of the conditional mean. The Boolean parametrization and the exact finite and unconditioned formulas are included as context. The formulas for the defect, fixed-genus coefficient, unconditioned mean and unconditioned central limit theorem overlap with the companion record [1] (for its range \(N\ge1\)); no separate novelty or priority is claimed for them.

Fix integers \(m\ge2\) and \(1\le c<m\), put \(F=2m-c\), and write \(N=m-c-1\). Every numerical semigroup with multiplicity \(m\) and Frobenius number \(F\) is uniquely of the form
\[
S_A=\{0,m\}\cup\{m+i:i\in A\}\cup[F+1,\infty),\qquad A\subseteq[N],
\]
where \([N]=\{1,\ldots,N\}\), empty for \(N=0\). Let \(B_A=\{0\}\cup A\), let \(g(S)\) be genus, and let \(e(S)\) be embedding dimension (the number of minimal positive generators). Then
\[
g(S_A)=2m-c-1-|A|,\quad
Q_N(A)=\#\bigl([N+1]\setminus(B_A+B_A)\bigr),\quad
e(S_A)=c+|A|+Q_N(A).
\]
Equivalently, the exact *genus-conditioned embedding-dimension defect* is
\[
e(S_A)-(2m-1-g(S_A))=Q_N(A).
\]
At a fixed admissible genus \(g\), set \(r=2m-c-1-g\), with \(0\le r\le N\). The number of such semigroups is \(\binom Nr\); under the uniform law, \(A\) is a uniformly chosen \(r\)-element subset of \([N]\). The finite conditional mean has the exact coefficient formula
\[
\mathbb E[Q_N\mid |A|=r]=\frac1{\binom Nr}\sum_{j=1}^{N+1}[z^r]
(1+2z)^{t_j}(1+z)^{h_j},
\]
where \(t_j=\lfloor(j-1)/2\rfloor\) and \(h_j=N-2t_j-\mathbf1_{2\mid j}-\mathbf1_{j\le N}\) (these exponents are nonnegative).

For **any** sequence of admissible \(m,c,r\) with \(N=m-c-1\to\infty\) and \(r/N\to p\in(0,1)\), the conditional defect converges in *total variation* to
\[
Q_p=\#\bigl(\mathbb Z_{>0}\setminus(B_p+B_p)\bigr),\qquad
B_p=\{0\}\cup\{j\ge1:X_j=1\},
\]
where \(X_1,X_2,\ldots\) are independent Bernoulli variables with success probability \(p\). Almost surely \(Q_p<\infty\), and the conditional expectations converge to
\[
\boxed{\lim\mathbb E[e(S)-(2m-1-g(S))]=\mathbb E Q_p=\frac{(1-p)(2-p)}{p^2}.}
\]
For unconditioned uniform sampling among all \(2^N\) semigroups with the given \((m,F)\), one additionally has the **exact** formula
\[
\mathbb E[e(S)]=c+\frac N2+3-2\left(\frac34\right)^{\lfloor N/2\rfloor}
\]
and, as \(N\to\infty\),
\[
\frac{e(S)-c-N/2}{\sqrt N/2}\Longrightarrow\mathcal N(0,1).
\]

## Assumptions and scope

All semigroups are cofinite additive submonoids of the nonnegative integers. Their multiplicity is the least positive member; Frobenius number the largest omitted integer; genus the number of omitted nonnegative integers; and embedding dimension the number of irreducible positive elements. For a subset \(B\) of integers, \(B+B=\{b_1+b_2:b_1,b_2\in B\}\). The finite statements hold for all \(m\ge2\), \(1\le c<m\), including \(N=0\). The asymptotic statements require \(N\to\infty\), and the fixed-genus statement requires limiting density strictly between zero and one; no endpoint limit is asserted. For the unconditioned central limit theorem no fixed-\(c\) assumption is required.

## Proof

**1. Parametrization and exact embedding dimension.** We have \(m<F<2m\). Therefore a semigroup of multiplicity \(m\) and Frobenius \(F\) contains \(m\), omits \(F\), contains every integer above \(F\), and may select arbitrary elements among \(m+1,\ldots,F-1\). Since any sum of two positive members is at least \(2m>F\), every selection yields a semigroup, and every such semigroup arises uniquely. There are \(F-(1+|A|)=2m-c-1-|A|\) positive gaps through \(F\).

Every member of \(\{m\}\cup(m+A)\) is irreducible, as is every integer in \([F+1,2m-1]\); this accounts for \(1+|A|+(c-1)=c+|A|\) minimal generators. The element \(2m\) is reducible. For \(1\le j\le N+1\), the element \(2m+j\) is reducible if and only if \(j\in B_A+B_A\), because all positive summands below \(F+1\) are precisely \(m+B_A\), and a summand at least \(F+1\) would make the sum at least \(F+m+1=2m+N+2\). Every integer above \(F+m=2m+N+1\) is reducible by subtracting \(m\). Hence the displayed formula for \(e(S_A)\) follows, including boundary cases.

**2. Finite mean conditioned on genus.** For \(1\le j\le N+1\), the potential positive two-summand representations of \(j\) consist of \(t_j=\lfloor(j-1)/2\rfloor\) disjoint pairs \(\{a,j-a\}\) with distinct positive entries, a central singleton \(j/2\) when \(j\) is even, and the singleton \(j\) when \(j\le N\), corresponding to \(0+j\). Thus \(j\notin B_A+B_A\) precisely when the \(t_j\) pairs each contribute at most one selected element, and the indicated singleton positions are not selected. Each pair contributes polynomial \(1+2z\); the \(h_j\) unconstrained positions contribute \(1+z\). Extracting the coefficient of \(z^r\) and dividing by \(\binom Nr\) gives the exact conditional mean after summing over \(j\).

**3. Conditional limiting law.** Put \(p_N=r/N\to p\in(0,1)\). For every fixed \(K\), the first \(K\) membership indicators of a uniformly selected \(r\)-subset have the hypergeometric distribution. For a specified pattern of \(a\) ones, its probability is \((r)_a(N-r)_{K-a}/(N)_K\to p^a(1-p)^{K-a}\); thus they converge jointly to independent Bernoulli-\(p\) indicators.

To control the moving fringe, choose \(\theta=p/2\), and independently select each position of \([N]\) with probability \(\theta\), producing \(Y\). Couple a uniform \(r\)-subset \(A\) by filling \(Y\) uniformly to size \(r\) when \(|Y|\le r\), and otherwise uniformly retaining \(r\) members of \(Y\). Permutation invariance makes \(A\) uniformly distributed over \(r\)-subsets; on \(\{|Y|\le r\}\), \(Y\subseteq A\). A binomial Chernoff bound gives \(\Pr(|Y|>r)\le e^{-\kappa N}\) for some \(\kappa>0\) and all sufficiently large \(N\). For each \(1\le j\le N+1\), there are \(t_j\) disjoint pairs of positive integers in \([N]\) summing to \(j\). If any pair is contained in \(Y\), it is contained in \(A\). Consequently
\[
\Pr(j\notin B_A+B_A)\le(1-\theta^2)^{t_j}+e^{-\kappa N}.
\]
Summing from \(j=K+1\) to \(N+1\) bounds the expected number of holes beyond \(K\) by \(C_\theta e^{-a_\theta K}+(N+1)e^{-\kappa N}\). The analogous bound for the infinite independent Bernoulli-\(p\) set is geometric, giving almost-sure finiteness of \(Q_p\). For fixed \(K\), the finite truncated hole count through \(K\) converges in total variation to its Bernoulli counterpart, since it depends on only \(K\) indicators. The two tail bounds now imply total-variation convergence of the full counts and convergence of their means.

For odd \(j=2u+1\) with \(u\ge0\), the infinite Bernoulli model has \(\Pr(j\notin B_p+B_p)=(1-p)(1-p^2)^u\). For even \(j=2u\) with \(u\ge1\), the probability is \((1-p)^2(1-p^2)^{u-1}\). Summing these two geometric series yields \(\mathbb E Q_p=(1-p)(2-p)/p^2\).

**4. Unconditioned mean and central limit theorem.** In the uniform subset model, the \(N\) membership bits are independent fair Bernoulli variables. For \(j\le N\), missing-sum probabilities are \(\frac12(\frac34)^{(j-1)/2}\) when \(j\) is odd and \(\frac14(\frac34)^{j/2-1}\) when \(j\) is even. For \(j=N+1\), omit the unavailable \(0+j\) representation, doubling the corresponding probability. Summing the finite geometric series separately for even and odd \(N\) gives \(\mathbb E Q_N=3-2(3/4)^{\lfloor N/2\rfloor}\). The same disjoint-pair estimates show \(Q_N=O_{\mathbb P}(1)\). Because \(|A|\sim\operatorname{Bin}(N,1/2)\), the classical binomial central limit theorem and Slutsky's lemma applied to \(e=c+|A|+Q_N\) give the stated limit.

## Verification

The accompanying standalone `VERIFY.py` exhaustively constructs finite numerical semigroups from their defining subsets for small \(m,c\), independently recomputes their irreducible positive elements, and checks genus and embedding-dimension identities. It also checks the conditional coefficient formula against exhaustive fixed-cardinality sampling and the exact unconditional mean against rational arithmetic. Execute `python3 VERIFY.py`; its success message is `VERIFY_OK`. These finite calculations corroborate, but do not prove, the infinite limiting law; the coupling and geometric-tail argument above do.

## Relationship to prior work

Hernández-Yanes and Rosales (2026) study covarieties with prescribed pseudo-Frobenius numbers, including computational genus and type, and classify certain maximal-embedding-dimension cases. Bras-Amorós and Torra (2026) give exact counts by the triple of Frobenius number, genus and multiplicity but not embedding-dimension distributions. Singhal (2022) counts depth-two numerical semigroups by genus for fixed Frobenius number, and Li (2023) gives broad depth enumerations and maximal-embedding-dimension asymptotics. The parametrization and genus binomial count are background. In [1], put \(\rho=N+1\) and identify its subset \(B\) with \(A\). Its defect \(e+g-2m\) is \(Q_N-1\). Its equations (1), (2), (3) and (6) cover the defect identity, unconditioned finite mean, fixed-genus coefficient and unconditioned Gaussian limit, respectively. Its equation (5) gives a total-variation limit in the unconditioned fair-subset model, not at prescribed genus. The independent missing-sum fringe itself is not a novelty claim; compare the iid random-sumset work of Jambhale–Kaldybayev–Miller–Yao. The distinct statement is convergence in total variation, with convergence of means, **conditional simultaneously on multiplicity, Frobenius number and genus**, for every limiting density \(p\) strictly between zero and one. The companion record is dated the same day; no order of priority is inferred from that date.

## Limitations

The conditional limit excludes \(p=0,1\), where different scaling may occur. This does not establish a new distribution for independent Bernoulli missing-sums outside its semigroup interpretation. No complete finite conditional probability-generating function for the defect is asserted. No claim of exhaustive historical priority is made.

## References

- [1] *Exact joint genus–embedding moments and a boundary law for depth-two numerical semigroups*, companion record dated 2026-11-22, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-exact-joint-genus-embedding-moments-and-a-boundary-law-for-depth--d2845b6b7dea/RESULT.md .
- W. G. Hernández-Yanes and J. C. Rosales, *The covariety of numerical semigroups with some prescribed pseudo-Frobenius numbers*, arXiv:2611.09425v1, first posted 2026-11-06. https://arxiv.org/abs/2611.09425
- M. Bras-Amorós and V. Torra, *Multiparameter counting of numerical semigroups by Frobenius number, genus, and multiplicity*, arXiv:2611.11559v1, first posted 2026-11-08. https://arxiv.org/abs/2611.11559
- D. Singhal, *Distribution of genus among numerical semigroups with fixed Frobenius number*, *Semigroup Forum* 104 (2022), 704–723. https://doi.org/10.1007/s00233-022-10282-6
- S. Li, *Counting numerical semigroups by Frobenius number, multiplicity, and depth*, arXiv:2208.14587. https://arxiv.org/abs/2208.14587
- A. Jambhale, A. Kaldybayev, S. J. Miller, and L. Yao, *Limiting Behavior in Missing Sums of Sumsets*, 2024 manuscript. https://web.williams.edu/Mathematics/sjmiller/public_html/math/papers/MSTD_Jambhale_Kaldybayev_Miller_Yao.pdf
- N. Kaplan and D. Singhal, *The Expected Embedding Dimension, Type and Weight of a Numerical Semigroup*, arXiv preprint. https://arxiv.org/abs/2211.07811
