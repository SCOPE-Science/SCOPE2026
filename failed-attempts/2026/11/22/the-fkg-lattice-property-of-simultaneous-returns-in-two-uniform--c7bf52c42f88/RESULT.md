# The FKG lattice property of simultaneous returns in two uniform Dyck paths

## Finding

**Theorem.** Let \(n\ge2\) and independently sample two uniformly random Dyck paths of semilength \(n\). Let \(S_n\subseteq\{1,\ldots,n-1\}\) consist of those \(j\) for which **both** paths have height zero immediately after step \(2j\). Then the complete law of \(S_n\), regarded as a strictly positive probability measure \(\mu_n\) on the Boolean lattice of subsets of \(\{1,\ldots,n-1\}\), satisfies
\[
\mu_n(A\cup B)\,\mu_n(A\cap B)\ge\mu_n(A)\,\mu_n(B)
\qquad\text{for every }A,B\subseteq\{1,\ldots,n-1\}.
\]
Consequently all coordinatewise increasing real functions \(f,g\) of the simultaneous-return set are positively associated:
\[
\operatorname{Cov}(f(S_n),g(S_n))\ge0.
\]
The same conclusions hold if the probability of each return set \(S\) is multiplied by an arbitrary positive product of individual weights \(\prod_{j\in S}t_j\), with \(t_j>0\), and then renormalized. For distinct \(1\le i<j\le n-1\), the covariance of their common-return indicators is strictly positive.

## Assumptions and scope

A Dyck path of semilength \(n\) has \(n\) steps \(+1\), \(n\) steps \(-1\), begins and ends at zero, and has nonnegative partial heights. The two paths are independent and each is uniform among the \(C_n=\binom{2n}{n}/(n+1)\) possibilities. Only simultaneous *interior* zero returns count; time zero and time \(2n\) are excluded. A measure is positively associated if all its increasing-observable covariances are nonnegative. This statement concerns independent Catalan excursions, not arbitrary correlated excursions or height-inhomogeneous step weights.

## Proof

**1. Exact law of the common-return set.** Put \(a_m=C_m^2\), \(A(z)=\sum_{m\ge0}a_mz^m\), and define \(B(z)=1-1/A(z)=\sum_{m\ge1}b_mz^m\). Cutting an ordered pair of Dyck paths at **all** simultaneous returns uniquely decomposes the pair into positive-length blocks without any interior simultaneous return. Thus \(b_m\) is exactly the nonnegative integer number of blocks of semilength \(m\); it is positive because two individually irreducible paths give a block. If \(S=\{s_1<\cdots<s_r\}\), write \(s_0=0\), \(s_{r+1}=n\). Concatenation of blocks gives the exact probability
\[
\mu_n(S)=\frac{\prod_{i=0}^{r}b_{s_{i+1}-s_i}}{C_n^2}.
\tag{1}
\]
There are no unaccounted cuts because each block is by definition without an interior *common* return.

**2. Strict log-convexity of block counts.** Let \(Y\) have density \(\frac{1}{2\pi}\sqrt{(4-y)/y}\) on \((0,4)\). A beta-integral shows \(\mathbb EY^m=C_m\). For independent copies \(Y_1,Y_2\), the nonnegative bounded variable \(X=Y_1Y_2\) has moments \(\mathbb EX^m=a_m\). On \(L^2(X)\), let \(e=1\), let \(P\) be orthogonal projection onto \(e^\perp\), let \(M\) multiply by \(X\), and set \(v=PM e\), \(T=PMP\) on \(e^\perp\). The operator \(T\) is bounded and positive. Schur complementation of the top-left entry of \((I-zM)^{-1}\) gives, for sufficiently small \(|z|\),
\[
\frac1{A(z)}=1-za_1-z^2\langle v,(I-zT)^{-1}v\rangle,
\qquad B(z)=za_1+z^2\langle v,(I-zT)^{-1}v\rangle.
\]
Hence \(b_1=a_1\), and \(b_{m+2}=\langle v,T^mv\rangle\) for every \(m\ge0\). Positivity of \(T\) and Cauchy–Schwarz make the sequence \((b_m)_{m\ge2}\) log-convex:
\(b_{k-1}b_{k+1}\ge b_k^2\) for all \(k\ge3\). The missing first inequality follows exactly from
\[
b_1b_3-b_2^2=a_1a_3-a_2^2=25-16=9>0.
\]
Thus \((b_m)_{m\ge1}\) is positive and log-convex. The argument is all-order, not based on finite enumeration.

**3. The lattice condition.** Consider a return set \(S\) and two missing indices \(i<j\). If they fall into different gaps between consecutive cuts of \(S\), then
\(\mu_n(S\cup\{i,j\})\mu_n(S)=\mu_n(S\cup\{i\})\mu_n(S\cup\{j\})\).
If both lie in the same gap \((u,v)\), set \(L=v-u\), \(x=i-u\), \(y=j-u\), with \(0<x<y<L\). Formula (1) gives the four-cell ratio
\[
\frac{\mu_n(S\cup\{i,j\})\mu_n(S)}{\mu_n(S\cup\{i\})\mu_n(S\cup\{j\})}
=\frac{b_{y-x}b_L}{b_{L-x}b_y}\ge1.
\]
Indeed the numerator subscripts and denominator subscripts have equal sum, while the numerator has the wider-spread pair; log-convexity establishes the inequality. These elementary squares imply log-supermodularity for arbitrary \(A,B\) by successive additions. The finite FKG lattice theorem then gives positive association. Multiplication by \(\prod_{j\in S}t_j\) cancels in every four-cell ratio, proving the stated inhomogeneous pinning robustness.

**4. Strict pairwise correlations.** For \(i<j\), forcing individual returns in each independent path yields
\[
\mathbb P(i,j\in S_n)=\left(\frac{C_iC_{j-i}C_{n-j}}{C_n}\right)^2,
\quad \mathbb P(i\in S_n)=\left(\frac{C_iC_{n-i}}{C_n}\right)^2.
\]
The joint-to-product ratio is \(\bigl(C_{j-i}C_n/(C_jC_{n-i})\bigr)^2>1\), by strict log-convexity of Catalan numbers and \(0<i<j<n\). Hence the two distinct contact indicators have strictly positive covariance.

## Verification

Run `python3 verify.py` alongside this file with the standard Python library. The checker independently enumerates both Dyck paths for semilengths \(2\) through \(8\), up to \(2{,}044{,}900\) ordered pairs, constructs their actual simultaneous-return sets, and checks the complete block-product probability law and every elementary FKG square with exact integers. It verifies 1,340 assertions, as well as block-count positivity and log-convexity. These finite tests are not the proof of the general theorem; the spectral argument and the FKG lattice argument above are.

## Relationship to prior work

First-return decomposition, Catalan enumeration and one-path contact statistics are classical. Mortimer and Prellberg (2012) give a Dyck-path bijection preserving contacts; Barnabei, Bonetti and Silimbani (2013) examine pairs of Dyck paths in connection with pattern-avoiding permutations. Fukuda and Nechita (2016) enumerate meandric systems via paired noncrossing matchings; Janson and Thévenin (2024) study counts of fixed loop shapes. All these supply natural adjacent models and combinatorial interpretations, but their inspected statements do not assert the **full FKG lattice condition for the exact set of simultaneous zero returns**, nor an all-order log-convexity certificate for its no-common-return block sequence.

The general FKG implication from log-supermodular weights is classical and is not claimed as new. The specialization hinges on the new block-weight identification and its all-order positivity proof. General subcritical-sequence results in Flajolet and Sedgewick supply negative-binomial laws for component counts; no such generic counting limit is claimed as novel here. Two independent Dyck paths can alternatively be viewed as the upper and lower noncrossing matchings of a meandric system; the statistic here counts separating **simultaneous return cuts**, not its loop components or the established irreducible-meander substitution statistic. Related historical formulations using Boolean cumulants or renewal pinning models might imply the result, and this is the main residual priority risk.

## Limitations

The theorem establishes the positive-association property for the complete contact configuration, not independence of contacts, a Gaussian limit, or a law for individual meander-loop components. The classical FKG theorem and positive-compression spectral identities are used in the proof. Historical priority for this exact probabilistic application has not been independently audited; equivalent statements may appear under renewal-set, noncrossing-matching or Boolean-cumulant terminology.

## References

1. P. R. G. Mortimer and T. Prellberg, *A Bijection on Bilateral Dyck Paths*, arXiv:1208.3061v1 (2012-08-15), https://arxiv.org/abs/1208.3061.
2. M. Barnabei, F. Bonetti and M. Silimbani, *Permutations and Pairs of Dyck Paths*, International Scholarly Research Notices, first published 2013-01-13, https://doi.org/10.1155/2013/107454.
3. M. Fukuda and I. Nechita, *Enumerating meandric systems with large number of loops*, arXiv:1609.02756 (2016-09), https://arxiv.org/abs/1609.02756.
4. S. Janson and P. Thévenin, *Central limit theorem for components in meandric systems through high moments*, Combinatorics, Probability and Computing 33 (2024), 597–610, https://doi.org/10.1017/S0963548324000117.
5. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), Chapter IX, https://algo.inria.fr/flajolet/Publications/book.html.
