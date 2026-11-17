# Sharp variation–Dobrushin separation for stochastically monotone Markov operators

## Finding
Let \(n\ge 2\), and let \(P\) be an arbitrary stochastic matrix on the ordered set \(\{1,\dots,n\}\) satisfying stochastic monotonicity: for every \(1\le i<n\) and \(1\le k<n\),
\[
\sum_{r>k}P_{ir}\le \sum_{r>k}P_{i+1,r}.
\]
On real signals \(f\in\mathbb R^n\) define the **ordered total variation** and **oscillation**, respectively, by
\[
V(f)=\sum_{i=1}^{n-1}|f_{i+1}-f_i|,
\qquad \operatorname{osc}(f)=\max_i f_i-\min_i f_i.
\]
Write \(\beta(P)\) for the operator seminorm induced by \(V\), and \(\delta(P)\) for the oscillation operator seminorm (the Dobrushin coefficient). For \(1\le k<n\) put \(T_i(k)=\sum_{r>k}P_{ir}\). Then
\[
\boxed{\beta(P)=\max_{1\le k<n}\bigl(T_n(k)-T_1(k)\bigr),
\qquad \beta(P)\le \delta(P)\le\lfloor n/2\rfloor\,\beta(P).}
\]
**Both comparison constants are attained by strictly positive stochastic-monotone matrices in every dimension.** Consequently, \(\beta(P)=\delta(P)\) for every such matrix when \(n=2,3\), while \(n=4\) is the minimum dimension permitting strict separation. The maximum ratio \(\delta(P)/\beta(P)\), for \(\beta(P)>0\), is \(\lfloor n/2\rfloor\), even when all matrix entries are strictly positive.

## Assumptions and scope
All matrices are real \(n\times n\), row-stochastic, nonnegative, and stochastically monotone in the specified linear order. The operator acts on column vectors by \((Pf)_i=\sum_r P_{ir}f_r\). Since \(P\mathbf 1=\mathbf 1\), both induced seminorms are well-defined on the quotient by constants:
\[
\beta(P)=\sup_{V(f)>0}\frac{V(Pf)}{V(f)},\qquad
\delta(P)=\sup_{\operatorname{osc}(f)>0}\frac{\operatorname{osc}(Pf)}{\operatorname{osc}(f)}.
\]
The sharp ratio statement restricts to \(\beta(P)>0\); if \(\beta(P)=0\), both coefficients vanish. No reversibility, irreducibility, common invariant distribution, or tridiagonal transition hypothesis is required.

## Proof
### 1. Exact ordered-variation norm
Set \(d_k=f_{k+1}-f_k\). Every signal decomposes as
\[
f_r=f_1+\sum_{k<r}d_k,
\qquad(Pf)_i=f_1+\sum_{k=1}^{n-1}T_i(k)d_k.
\]
Hence for \(i<n\),
\[
(Pf)_{i+1}-(Pf)_i=\sum_{k=1}^{n-1}a_{ik}d_k,
\quad a_{ik}=T_{i+1}(k)-T_i(k)\ge0.
\]
The induced operator on differences has a nonnegative matrix \(a\). Its \(\ell^1\)-norm is its maximum column sum. By telescoping, \(\sum_i a_{ik}=T_n(k)-T_1(k)\). Therefore \(\beta(P)=\max_k(T_n(k)-T_1(k))\). The step signal \(f_r=\mathbf 1_{\{r>k\}}\) attains the corresponding column sum, so this is an attained exact norm, not merely a bound.

### 2. Upper bound for Dobrushin
For row indices \(i<j\), define
\[
c_k=T_j(k)-T_i(k)\quad(1\le k<n),
\qquad c_0=c_n=0.
\]
Stochastic monotonicity and telescoping give \(0\le c_k\le T_n(k)-T_1(k)\le\beta(P)\). The signed difference of the two rows is \(P_{jr}-P_{ir}=c_{r-1}-c_r\), so
\[
\frac12\sum_{r=1}^n|P_{jr}-P_{ir}|
=\frac12\sum_{r=1}^n|c_r-c_{r-1}|.
\]
The right side is convex in \((c_1,\ldots,c_{n-1})\). Its maximum over the cube \([0,\beta(P)]^{n-1}\) is attained at a vertex, with all entries zero or \(\beta(P)\). With both endpoints fixed at zero, each nonzero contiguous block contributes precisely \(\beta(P)\) to half the total variation; there are at most \(\lfloor n/2\rfloor\) such blocks. Thus each pair of rows has total-variation distance at most \(\lfloor n/2\rfloor\beta(P)\).

For completeness, the Dobrushin identity follows by maximization over signals taking values in \([0,1]\):
\[
\delta(P)=\max_{i<j}\frac12\sum_{r=1}^n|P_{jr}-P_{ir}|.
\]
This finishes the upper bound.

### 3. Lower comparison bound
The pair of endpoint rows has total-variation distance at least the difference on any tail event \(\{k+1,\ldots,n\}\). Consequently
\[
\delta(P)\ge\max_k\bigl(T_n(k)-T_1(k)\bigr)=\beta(P).
\]
This also establishes that \(\beta(P)=0\) implies \(\delta(P)=0\).

### 4. Sharpness, strict positivity, and minimum dimension
Fix \(n\ge2\), put \(m=\lfloor n/2\rfloor\), and let \(u\) and \(v\) be the probability rows uniform on \(\{1,3,\ldots,2m-1\}\) and \(\{2,4,\ldots,2m\}\), respectively. Their tails obey \(T_u(k)\le T_v(k)\) for every cut \(k\): at odd cuts their difference is \(1/m\), and at even cuts it is zero. Their supports are disjoint, so their total-variation distance is \(1\).

For \(s_i=(i-1)/(n-1)\), define \(P^0_{i\cdot}=(1-s_i)u+s_i v\). This row-stochastic matrix is stochastically monotone, and its endpoint rows are \(u,v\). The exact norm formulas give \(\beta(P^0)=1/m\) and \(\delta(P^0)=1\). Let \(J\) be the matrix with every entry \(1/n\). For each \(0<\varepsilon<1\), the matrix \(P^\varepsilon=(1-\varepsilon)P^0+\varepsilon J\) is **strictly positive**, stochastically monotone, and satisfies
\[
\beta(P^\varepsilon)=(1-\varepsilon)/m,
\qquad \delta(P^\varepsilon)=1-\varepsilon.
\]
This attains the upper comparison factor even with strict positivity.

For the lower comparison factor, take \(R^\varepsilon=(1-\varepsilon)I+\varepsilon J\), also strictly positive and stochastically monotone. Since \(R^\varepsilon f=(1-\varepsilon)f+\varepsilon\bar f\mathbf 1\), both seminorms scale by exactly \(1-\varepsilon\): \(\beta(R^\varepsilon)=\delta(R^\varepsilon)=1-\varepsilon\). Finally \(\lfloor n/2\rfloor=1\) for \(n\le3\), while the upper sharp example produces strict separation when \(n\ge4\). This proves every claim.

## Verification
The accompanying standalone Python checker (`checker.py`) uses only standard-library rational arithmetic. It rederives \(\beta\) from ordered tail differences and \(\delta\) from exact row-pair total variation; verifies both sharp constructions with \(n=2,\ldots,32\) and several strictly positive perturbations; and checks 1320 independent mixtures of monotone maps on state spaces of sizes \(2,\ldots,12\). The completed execution reported `ALL_ORDERED_MARKOV_COEFFICIENT_CHECKS_PASS`. These finite checks corroborate but do not replace the above proof, which covers every finite \(n\) and every stochastically monotone matrix.

To reproduce: `python3 checker.py`. No external packages or data are needed.

## Relationship to prior work
Dobrushin's coefficient and its oscillation-norm characterization are classical; see Gaubert–Qu for a general operator-theoretic treatment. Fill–Kahn study finite stochastically monotone kernels and mixing comparisons. Kamihigashi–Stachurski investigate order-sensitive metrics and convergence for monotone Markov chains. The result here compares **two seminorms on functions on an ordered state space**—adjacent-point variation and oscillation—and determines the sharp dimension-dependent ratio under stochastic monotonicity. In particular, the tail-event factor \(\beta(P)\) is not the usual total variation distance between endpoint probability rows; the theorem quantifies exactly how far these can be separated. These comparisons do not claim priority over any result in unindexed literature.

## Limitations
The comparison assumes a *total order* on a *finite* state space and stochastic monotonicity in that order. It does not assert the same factor on arbitrary partially ordered sets, under non-monotone kernels, or for distinct notions of function variation. The sharpness examples need not be reversible. The theorem is a one-step operator statement, not a mixing-time or semigroup theorem. The preceding literature comparison does not constitute an independent originality certification.

## References
1. J. A. Fill and J. Kahn, *Comparison inequalities and fastest-mixing Markov chains*, first public arXiv version 2011-09-28, arXiv:1109.6075, https://arxiv.org/abs/1109.6075.
2. S. Gaubert and Z. Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, arXiv:1307.4649, first posted 2013-07-17, https://arxiv.org/abs/1307.4649.
3. T. Kamihigashi and J. Stachurski, *A Unified Stability Theory for Classical and Monotone Markov Chains*, https://arxiv.org/abs/2410.00472 (later repository version of earlier published work).
4. T. Kamihigashi and J. Stachurski, *Quantitative Convergence Rates for Stochastically Monotone Markov Chains*, https://arxiv.org/abs/2409.19874.
