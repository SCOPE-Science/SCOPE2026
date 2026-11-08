# Exact local instability and the binary optimizer bifurcation for expiring coupon entry rates

## Finding

The principal result is an exact local stability test at the uniform probability vector for **every finite alphabet and window**, together with the complete global optimizer classification for **two types**. The stability coefficient is the explicit finite word-count expression (9); for each fixed number of types it is eventually positive, so the uniform law becomes a strict *local minimum* of stationary new-completion intensity. In the two-type case a unique balanced optimum at \(M=2,3\) splits into exactly two unequal global optima at the sharp threshold \(M=4\). The weighted entrance formula (1), the shortest-window product (2), and the rare-symbol comparison (4) are supporting identities and contextual benchmarks rather than independent novelty claims.

More precisely, for \(n\ge2\), \(M\ge n\), and positive probabilities \(\mathbf p=(p_1,\ldots,p_n)\) summing to one, define the stationary entrance frequency \(\mu_{n,M}(\mathbf p)\) as in the next section. Then

\[
\mu_{n,M}(\mathbf p)
=\sum_{i=1}^{n}p_i(1-p_i)
\sum_{B\subseteq[n]\setminus\{i\}}
(-1)^{n-1-|B|}\left(\sum_{j\in B}p_j\right)^{M-1}.
\tag{1}
\]

At \(M=n\), the exact expression simplifies to

\[
\mu_{n,n}(\mathbf p)=(n-1)(n-1)!\prod_{i=1}^{n}p_i,
\tag{2}
\]

which is uniquely maximized by \(p_i=1/n\). For each fixed \(n\ge2\), however, uniform sampling is a strict local minimum for all sufficiently large \(M\). Furthermore, the explicit unequal law

\[
p_1=1/M,\qquad p_2=\cdots=p_n=(1-1/M)/(n-1)
\tag{3}
\]

satisfies

\[
\mu_{n,M}(\mathbf p)\sim 1/(eM),\qquad
\mu_{n,M}(\mathbf u)\sim(1-1/n)^M,
\tag{4}
\]

where \(\mathbf u\) is uniform. The first equivalence is a constructive lower bound for nonuniform flux, **not** an assertion that it is the global maximum for \(n\ge3\).

For \(n=2\), write \(\mathbf p=(p,1-p)\). Then, for every integer \(M\ge2\),

\[
\mu_{2,M}(p)=p(1-p)^M+(1-p)p^M.
\tag{5}
\]

For \(M=2,3\) its unique maximizer is \(p=1/2\). For every \(M\ge4\), the only global maximizers are \(p_M\) and \(1-p_M\), where \(0<p_M<1/2\), and \(t_M=p_M/(1-p_M)\) is the unique root in \((0,1)\) of

\[
1-Mt+Mt^{M-1}-t^M=0.
\tag{6}
\]

In particular,

\[
p_4=(1-1/\sqrt3)/2,\quad
\max_{0<p<1}\mu_{2,4}(p)=1/12,
\quad\mu_{2,4}(1/2)=1/16.
\tag{7}
\]

The maximizing rare-type probability and flux have the asymptotics

\[
p_M=\frac1{M+1}+O((2/M)^{M-1}),\qquad
\max_p\mu_{2,M}(p)\sim\frac1{eM}.
\tag{8}
\]

The **new** mathematical assertion is the explicit all-alphabet Hessian criterion and its eventual positive sign, jointly with the sharp finite-window binary global optimizer bifurcation. The general weighted inclusion–exclusion formula, short-window AM–GM observation, and existence of large-window asymmetric improvements follow directly from known entrance-counting mechanisms; prior work already determines the more powerful fixed-alphabet large-window global asymptotic optimum and a sharp three-type example. No novel global large-window asymptotic optimum is claimed here.

## Assumptions and scope

Let \((X_t)_{t\in\mathbb Z}\) be independent with \(\Pr(X_t=i)=p_i>0\), \(i\in[n]\), and \(\sum_i p_i=1\). Define the window \(W_t=(X_{t-M+1},\ldots,X_t)\), and let \(A_t\) mean that \(W_t\) contains every label in \([n]\). The entrance event is \(E_t=A_t\cap A_{t-1}^{\mathrm c}\), and \(\mu_{n,M}(\mathbf p)=\Pr(E_t)\). This is a **stationary recurrence frequency**, not the probability that a window covers all types and not the reciprocal of the initial mean completion time. It equals the reciprocal of the expected separation between successive entrances when conditioned on an entrance in the stationary finite-state process.

All probability vectors in the main optimization are strictly positive. The endpoint \(M=n\) includes every \(n\ge2\); the local-curvature derivation below uses \(M\ge\max\{n,3\}\). All asymptotic statements hold for each **fixed** \(n\) as integer \(M\to\infty\). Constants implicit in those asymptotics may depend on \(n\).

## Proof

**Weighted entrance identity.** Put \(B_t=(X_{t-M+1},\ldots,X_{t-1})\), the common block of \(M-1\) symbols. For an entrance, exactly one type \(i\) is missing from \(B_t\); the block contains all other \(n-1\) types, \(X_t=i\), and \(X_{t-M}\ne i\). These are also sufficient. The three independent conditions have probabilities \(p_i\), \(1-p_i\), and the probability that \(B_t\) contains all types except \(i\) but no \(i\). Inclusion–exclusion on missing types in \(B_t\) gives the inner subset sum in (1). The events for different \(i\) are disjoint, proving (1). If \(M=n\), the common block contains each other type exactly once; summation gives (2). The arithmetic–geometric mean inequality gives its unique maximizer.

**Contextual long-window comparison (not a new global asymptotic optimality claim).** For the vector (3), the contribution from the rare type \(i=1\) is

\[
\frac1M\left(1-\frac1M\right)^M C_{n-1,M-1},
\]

where \(C_{k,s}\) is the probability that \(s\) independent uniform draws from \(k\) labels cover all \(k\). For each fixed \(n\), \(C_{n-1,M-1}\to1\). Every remaining term is at most \(p_i(1-p_i)^M\) and is exponentially small for fixed \(n\). Thus the total is asymptotic to \(1/(eM)\). At uniform probabilities, (1) reduces to Long's uniform flux

\[
\mu_{n,M}(\mathbf u)
=\left(1-\frac1n\right)^M C_{n-1,M-1}
\sim\left(1-\frac1n\right)^M.
\]

Hence unequal sampling has a strictly greater flux for every sufficiently large \(M\), with the ratio diverging exponentially.

**Strict local minimality for every fixed number of types.** Fix \(n\), put \(r=M-1\), \(k=n-1\), \(u=1/n\), and write

\[
H_{s,k,h}:=\sum_{j=0}^{h}(-1)^j\binom hj(k-j)^s
\]

for the number of words of length \(s\) from an alphabet of size \(k\) containing each of \(h\) prescribed symbols. For \(M\ge\max\{n,3\}\), set

\[
Q=\frac{H_{r,k,k}}{n^r},\quad
A=\frac{rH_{r-1,k,k-1}}{n^{r-1}},\quad
B=\frac{r(r-1)H_{r-2,k,k-1}}{n^{r-2}},\quad
C=\frac{r(r-1)H_{r-2,k,k-2}}{n^{r-2}}.
\]

Differentiating the polynomial (1) along \(\mathbf p(x)=(u+x,u-x,u,\ldots,u)\) yields

\[
\mu_{n,M}(\mathbf p(x))
=\mu_{n,M}(\mathbf u)+\kappa_{n,M}x^2+O(x^4),
\quad
\kappa_{n,M}=-2Q+u(1-u)((n-1)B-(n-2)C)-2(1-2u)A.
\tag{9}
\]

The remainder is even because swapping the first two symbols changes \(x\) to \(-x\). Inclusion–exclusion implies, with \(a=(n-1)/n\) and fixed \(n\),

\[
Q=a^r(1+o(1)),\quad
A=ra^{r-1}(1+o(1)),\quad
B=r(r-1)a^{r-2}(1+o(1)),\quad
C=r(r-1)a^{r-2}(1+o(1)).
\]

The errors in these estimates decay exponentially relative to their displayed terms, since missing one prescribed symbol reduces the alphabet size. Consequently

\[
\kappa_{n,M}\sim\frac{n-1}{n^2}(M-1)(M-2)
\left(\frac{n-1}{n}\right)^{M-3}>0.
\tag{10}
\]

At a permutation-symmetric point the Hessian has one common diagonal entry and one common off-diagonal entry. Formula (9) is exactly their difference, hence its quadratic form on the tangent space \(\sum_i v_i=0\) is \(\kappa_{n,M}\sum_i v_i^2\). This is strictly positive for sufficiently large \(M\), proving strict local minimality of uniform sampling on the probability simplex.

**Sharp two-type global classification.** For \(n=2\), an entrance is precisely a monochromatic preceding window of length \(M\) followed by the opposite type. Equation (5) follows. By symmetry, analyze \(0<p\le1/2\) and let \(t=p/(1-p)\in(0,1]\). Then

\[
\mu_{2,M}(p)=\frac{t+t^M}{(1+t)^{M+1}},\qquad
\operatorname{sgn}\frac{d\mu}{dt}=
\operatorname{sgn}F_M(t),
\quad F_M(t)=1-Mt+Mt^{M-1}-t^M.
\]

For \(M=2\), \(F_M(t)=1-t^2>0\) on \((0,1)\); for \(M=3\), \(F_M(t)=(1-t)^3>0\) there. Thus \(p=1/2\) is the unique maximum. For \(M\ge4\),

\[
F_M'(t)=M\bigl(-1+t^{M-2}(M-1-t)\bigr).
\]

The factor \(t^{M-2}(M-1-t)\) increases strictly from \(0\) to \(M-2>1\) on \((0,1)\). Hence \(F_M\) first strictly decreases and then strictly increases; since \(F_M(0)=1\), \(F_M(1)=0\), and \(F_M\) is negative just left of \(1\), it has exactly one root in \((0,1)\). The derivative changes from positive to negative at that root. This proves the two and only two global maxima and shows the balanced point is a strict local minimum.

For \(M=4\), polynomial factorization gives \(p_4=(1-1/\sqrt3)/2\) and (7). Finally, \(F_M(1/M)>0\) and \(F_M(2/M)<0\) for every \(M\ge4\), so \(1/M<t_M<2/M\). The root equation rearranges to

\[
0<t_M-1/M=t_M^{M-1}(1-t_M/M)\le(2/M)^{M-1}.
\]

Since \(p_M=t_M/(1+t_M)\), this yields the first assertion of (8). Substitution into (5) gives its second assertion. The binomial expansions involved here are exact, not finite-size numerical extrapolations.

**Initial waiting versus stationary recurrence.** With two types and \(M\ge2\), first completion from an empty history is the first time the initial monochromatic run changes type. Conditioning on its initial type gives

\[
\mathbb E T_{\rm first}=1+\frac{p}{1-p}+\frac{1-p}{p}.
\]

Unlike stationary entrance flux for \(M\ge4\), this initial mean is uniquely minimized by \(p=1/2\). Thus the sampling design that speeds up recurrent new entries can make completion from an empty start slower.

## Verification

Run `python3 verify.py` using Python's standard library. The supplied checker performs **425 exact-rational assertions**, including exhaustive weighted enumeration of all relevant length-\(M+1\) words in small instances, independent evaluations of the inclusion–exclusion formula, recovery of the published uniform Stirling-number formula, independent quadratic-coefficient versus symbolic-curvature comparisons, exact algebra at \(M=4\), root-sign brackets, and explicit unequal-versus-uniform comparisons. The analytical proof—not the finite tests—establishes all quantifiers and asymptotics.

## Relationship to prior work

Long (2026), Theorem 3.1, proves the uniform-probability flux \((n-1)(n-1)!S(M-1,n-1)/n^M\) and studies subcritical rare-entry limits as the number of types grows. Weighted inclusion–exclusion is a direct extension of that mechanism and is **not by itself asserted as a deep novelty**. The substantive claims concern the **exact tangent Hessian sign-test at every alphabet size** and the **sharp binary global optimizer phase boundary**. Earlier mathematical findings already provide a fixed-alphabet global long-window optimum and a three-type exact finite phase example; those results dominate the elementary rare-symbol comparison and are not claimed anew. Neither their stated global asymptotic optimizer nor the three-type threshold implies the present local Hessian criterion for arbitrary alphabet size or the complete binary finite-window classification. The paper's inspected text does not state these optimizer conclusions. Chang and Ross (2007) treat a monotone multiple-subset collection time with unequal probabilities; its publicly available abstract describes a different stopping event and does not resolve this entrance-rate optimization. General binary-run pattern probabilities remain a potential source of equivalent formulations.

## Limitations

This work gives stationary entrance frequencies, not an arbitrary-parameter first-passage distribution or an exponential-limit theorem under biased sampling. The exact global optimizer classification is for two types only. For more types, the long-window construction supplies a lower bound and local instability of uniform, not a complete global phase diagram. No independent audit has been performed. Historical-priority assessment is conditional on the inspected primary text, accessible records, and searches; older symbolic-run optimization work may cover equivalent formulas or special cases.

## References

1. Christopher D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298v1, first posted 2026-04-29. https://arxiv.org/html/2604.26298v1
2. Kuang-Chao Chang and Sheldon M. Ross, *The Multiple Subset Coupon Collecting Problem*, *Probability in the Engineering and Informational Sciences* **21** (2007), 435–440. https://doi.org/10.1017/S026996480700006X (public abstract inspected; article text not available for verification).
