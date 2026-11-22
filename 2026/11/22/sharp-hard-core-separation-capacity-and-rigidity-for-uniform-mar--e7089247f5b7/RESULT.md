# Sharp hard-core separation capacity and rigidity for uniform-marginal couplings

## Finding

For every integer \(n\geq 2\), fix an arbitrary dependence law on \(U_1,\ldots,U_n\) with each \(U_i\sim\operatorname{Unif}[0,1]\), and define the minimal pairwise separation
\[
S=\min_{1\le i<j\le n}|U_i-U_j|.
\]
For every real \(r\geq0\), the largest possible survival probability over *all* copulas is the attained sharp value
\[
\boxed{\sup\Pr\{S\ge r\}=\max\bigl\{0,\min\{1,n[1-(n-1)r]\}\bigr\}.}
\]
The critical interval is \(1/n<r<1/(n-1)\). In this interval, write \(a=1-(n-1)r\), \(q=na\), and \(B_j=[(j-1)r,(j-1)r+a]\). Every maximizing law has the following *necessary* structure: with probability \(q\), the unordered observations form the exact arithmetic progression
\[
\{T,T+r,\ldots,T+(n-1)r\},\qquad T\sim\operatorname{Unif}[0,a],
\]
and, with the complementary probability, **all** coordinates lie in \(H=[0,1]\setminus\bigcup_{j=1}^nB_j\). Conditional on failure, each individual coordinate is uniform on \(H\). Conditional on the common offset \(T\) in the success branch, each label occupies each progression position with probability \(1/n\) for almost every offset. Conversely, these properties characterize all maximizing laws; the labels can be coupled in any way satisfying those one-label assignment probabilities, and the failure coordinates can have any coupling of the uniform law on \(H\).

A direct consequence is incompatibility of tail optimizers: if \(1/n<r<s<1/(n-1)\), **every** law maximizing \(\Pr\{S\ge r\}\) has \(\Pr\{S\ge s\}=0\), although the sharp probability at threshold \(s\) is strictly positive. In particular no single copula stochastically maximizes \(S\) at all thresholds.

## Assumptions and scope

The integer \(n\) is fixed and at least two. Marginal distributions are exactly standard uniform on the closed interval \([0,1]\). No independence, density, exchangeability, smoothness, or symmetry of the copula is assumed. All probability events use weak separation \(S\ge r\); the precise boundary convention matters at \(r=1/(n-1)\) and is settled by atomless marginal laws. The supremum runs over all Borel probability laws on \([0,1]^n\) with the stated marginals, including singular copulas. For \(r=0\), the optimum is one, and for \(r>1/(n-1)\), the event is deterministically empty. The rigidity and optimizer incompatibility statements concern only the open critical interval.

## Proof

**1. Deterministic geometric constraint.** Let \(V_1\le\cdots\le V_n\) denote the ordered observations. On \(E_r=\{S\ge r\}\), consecutive differences are at least \(r\); hence for each \(j\),
\[
(j-1)r\le V_j\le1-(n-j)r=(j-1)r+a,
\qquad a=1-(n-1)r.
\]
For \(r>1/(n-1)\), this is impossible. At \(r=1/(n-1)\), the only possible ordered configuration is \(V_1=0,V_j=(j-1)r,V_n=1\). That event is contained in \(\bigcup_i\{U_i=0\}\), which has probability zero by atomlessness. Consequently the sharp value is zero for \(r\ge1/(n-1)\).

**2. Upper bound in the critical interval.** Assume \(1/n<r<1/(n-1)\). Then \(0<a<r\), so the bands \(B_j=[(j-1)r,(j-1)r+a]\) are pairwise disjoint. On \(E_r\), exactly one coordinate lies in each band; in particular, at least one coordinate belongs to \(B_1=[0,a]\). Since each marginal is uniform,
\[
\Pr(E_r)\le\Pr\{\exists i:U_i\in B_1\}
\le\sum_{i=1}^n\Pr\{U_i\in B_1\}=na=q.
\]
For \(0\le r\le1/n\), the trivial upper bound one suffices.

**3. Simultaneous sharpness with exact marginal verification.** In the critical interval, select the success branch with probability \(q=na\). In that branch, draw \(T\sim\operatorname{Unif}[0,a]\), choose an independent uniformly random permutation \(\pi\) of \(\{0,\ldots,n-1\}\), and set \(U_i=T+\pi(i)r\). The sample has separation exactly \(r\). On the failure branch, draw \(W\sim\operatorname{Unif}(H)\) and set \(U_1=\cdots=U_n=W\), so its separation is zero. The total Lebesgue measure of the bands is \(na=q\) and that of \(H\) is \(1-q>0\). For any Borel subset \(C\subseteq B_j\),
\[
\Pr\{U_i\in C\}=q\frac1n\frac{|C|}{a}=|C|,
\]
while for \(C\subseteq H\),
\[
\Pr\{U_i\in C\}=(1-q)\frac{|C|}{1-q}=|C|.
\]
These two identities cover the interval up to their disjoint boundaries, which have zero marginal probability. Thus every coordinate has exactly the standard-uniform law and the event has probability \(q\). For \(r\le1/n\), use \(T\sim\operatorname{Unif}[0,1/n]\) and a uniformly random permutation of \(T,T+1/n,\ldots,T+(n-1)/n\). All marginals are uniform and the sample separation is \(1/n\ge r\); hence the upper bound one is sharp.

**4. Rigidity of all critical-interval optimizers.** Consider any law attaining \(\Pr(E_r)=q\). On \(E_r\) exactly one point lies in each \(B_j\). Therefore, for each \(j\),
\[
\sum_{i=1}^n\Pr\{U_i\in B_j,E_r\}=q
=\sum_{i=1}^n\Pr\{U_i\in B_j\},
\]
which implies \(\Pr\{U_i\in B_j,E_r^c\}=0\) for every \(i,j\). For every Borel \(C\subseteq B_j\), since no failure observation hits \(B_j\),
\[
\Pr\{V_j\in C,E_r\}=\sum_{i=1}^n\Pr\{U_i\in C,E_r\}
=\sum_{i=1}^n\Pr\{U_i\in C\}=n|C|.
\]
Dividing by \(q=na\) shows \(V_j\mid E_r\sim\operatorname{Unif}(B_j)\). The offsets \(T_j=V_j-(j-1)r\) therefore all have the same uniform distribution on \([0,a]\) conditional on \(E_r\). But the gap constraints give \(T_1\le T_2\le\cdots\le T_n\) almost surely. Since all offsets have equal finite expectations, \(\mathbb E[T_n-T_1\mid E_r]=0\) and hence \(T_1=\cdots=T_n=T\) almost surely on \(E_r\). This is the stated rigid arithmetic progression, including its exact offset law.

Each label has unconditional density one on each band and zero band mass in the failure branch, so conditional on \(T=t,E_r\) the probability of that label taking position \(j\) is \(1/n\) for Lebesgue-almost every \(t\in[0,a]\). On failure, all coordinates lie in \(H\); their unconditional density there is one, and \(\Pr(E_r^c)=1-q\), so their conditional marginals are uniform on \(H\). The converse follows by reversing the marginal-density calculation in Step 3; moreover, an \(n\)-point \(r\)-separated configuration cannot have all its coordinates in \(H\), because Step 1 would require one point in each \(B_j\). This proves the complete optimizer description.

**5. Incompatibility across distinct thresholds.** Suppose \(1/n<r<s<1/(n-1)\). Under *any* \(r\)-maximizer, the event \(E_r\) consists of arithmetic progressions with every consecutive gap exactly \(r\), by Step 4. Thus \(E_s\subseteq E_r\) has probability zero. Yet Step 3 at threshold \(s\) supplies an admissible coupling with \(\Pr(E_s)=n[1-(n-1)s]>0\). Therefore a common maximizer for both thresholds cannot exist, proving the last assertion.

## Verification

The accompanying standalone \(\texttt{checker.py}\) uses exact rational arithmetic. It verifies threshold endpoint values, band geometry and disjointness, union/complement measures, both branches' marginal densities, and the positivity of an incompatible larger-threshold optimum for \(n\) from two through eighteen and eighteen rational interior thresholds per \(n\). Reproduce with \(\texttt{python checker.py}\). The checker returns 3128 passed assertions. The infinite-dimensional statements and uniqueness consequences rest on the proofs above, not finite testing.

As a concrete instance, \(n=3\) and \(r=2/5\) give \(a=1/5\), \(q=3/5\), three bands \([0,1/5]\), \([2/5,3/5]\), and \([4/5,1]\); the surviving configurations are uniformly shifted length-three arithmetic progressions at gap \(2/5\). Any maximizing law at \(2/5\) has zero probability of a strictly larger minimum gap, even though positive sharp probability remains until \(r=1/2\).

## Relationship to prior work

Cattaneo, Masini, and Underwood (arXiv:2502.07699v1, 2025) give sharp arbitrary-copula anti-concentration bounds for a *maximum statistic*, using restrictions on diagonal sections of copulas. Their event constrains a single maximum to an interval; it does not impose all \(\binom n2\) pairwise separation constraints or classify conditional gap rigidity. The present extremal event concerns the minimum distance among all coordinates and supplies an explicit multivariate feasibility construction and all equality cases.

Cunden, Cuppone, Gramegna, and Vivo (arXiv:2606.04837v1, June 3, 2026) analyze the maximal minimal spacing obtainable by *selecting a subset of an existing random point configuration* whose initial spacings are independently distributed. This selection/renewal model does not optimize the joint distribution of a prescribed number of uniform-marginal coordinates and therefore has neither the same optimization domain nor the present equality cases. More general copula, marginal-compatibility and optimal-transport theory supplies a framework, but its existence principles alone do not state the explicit sharp capacity, rigidity or incompatible-threshold conclusion. These comparisons do not establish historical uniqueness.

## Limitations

The theorem applies specifically to *standard-uniform* one-dimensional marginals; nonlinear transformations to a nonuniform common marginal do not preserve Euclidean separation. It concerns all unrestricted copulas, including singular ones, not an independent or smoothly-density-constrained model. The rigid optimizer structure is asserted only on the open critical interval. There is no claim that a single optimal copula exists simultaneously for all thresholds, and the theorem proves the contrary there. Independent expert mathematical validation and a conclusive historical-priority determination have not been performed.

## References

1. M. D. Cattaneo, R. P. Masini, W. G. Underwood, *Sharp Anti-Concentration Inequalities for Extremum Statistics via Copulas*, arXiv:2502.07699v1, publicly submitted February 11, 2025. https://arxiv.org/html/2502.07699v1
2. F. D. Cunden, N. Cuppone, G. Gramegna, P. Vivo, *Maximal Minimal Spacing for Random Points*, arXiv:2606.04837v1, publicly submitted June 3, 2026; subsequently Journal of Statistical Physics 193, article 118 (2026). https://arxiv.org/abs/2606.04837
3. H. Joe, *Dependence Modeling with Copulas*, CRC Press, 2014; background definitions and extremal-coupling terminology (not a specific priority claim).
