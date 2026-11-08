# Convex-order balancing law for fixed points in random mappings with prescribed indegrees

## Finding
For every integer \(n\ge2\), condition a uniformly random function \(f:[n]\to[n]\) on its entire labeled indegree vector \(\boldsymbol d=(d_1,\ldots,d_n)\) with nonnegative integral coordinates summing to \(n\). Write \(F_{\boldsymbol d}=\#\{i:f(i)=i\}\) for the number of self-loops. Whenever \(\boldsymbol d\) majorizes \(\boldsymbol e\),
\[
F_{\boldsymbol d}\preceq_{\mathrm{cx}}F_{\boldsymbol e},
\]
meaning that every real convex function \(\varphi\) on \([0,n]\) has \(\mathbb E\varphi(F_{\boldsymbol d})\le\mathbb E\varphi(F_{\boldsymbol e})\). The inequality for every strictly convex \(\varphi\) is strict unless \(\boldsymbol d\) and \(\boldsymbol e\) have the same coordinates up to permutation.

There is an exact one-step law, not just an ordering. Suppose two coordinates are \(a,b\), with \(a\ge b+2\), and replace them with \(a-1,b+1\). Let \(Y\) count position-label matches among the remaining \(n-2\) named positions when the available letters comprise their original prescribed target multiplicities plus \(a+b-2\) copies of one auxiliary symbol that matches none of those positions. Then for every integer \(t\),
\[
\mathbb E[(F_{\boldsymbol e}-t)_+]-\mathbb E[(F_{\boldsymbol d}-t)_+]
=\frac{a-b-1}{n(n-1)}\Pr\{Y=t-1\}.
\]
The right side is nonnegative. In particular,
\[
1\equiv F_{(n,0,\ldots,0)}\preceq_{\mathrm{cx}}F_{\boldsymbol d}
\preceq_{\mathrm{cx}} F_{(1,\ldots,1)},
\]
where the rightmost law is the usual rencontres fixed-point distribution of a uniform permutation. These two extremal laws are attained only at the indicated indegree multisets.

## Assumptions and scope
All \(n\) positions and all \(n\) target labels are distinct and numbered \(1,\ldots,n\), even when some target multiplicities vanish. There are precisely \(n!/\prod_i d_i!\) admissible functions, taken uniformly. An indegree coordinate \(d_i\) counts the number of sources mapping to target \(i\); a fixed point is the single event \(f(i)=i\), not a match to a block of \(d_i\) reference positions.

Majorization means that, after arranging both degree vectors in nonincreasing order, the first \(s\) coordinates of \(\boldsymbol d\) sum to at least the first \(s\) coordinates of \(\boldsymbol e\) for all \(1\le s<n\), with equal total sum. The positive part is \((x)_+=\max(x,0)\), and \(\preceq_{\mathrm{cx}}\) denotes the finite-support convex order. Empty products are one; \(e_r\) denotes the elementary symmetric polynomial of degree \(r\), with \(e_0=1\) and \(e_r=0\) for negative degrees or degrees exceeding the number of variables.

## Proof
**Exact generating function.** For a subset \(S\) of \(r\) source positions, all events \(f(i)=i\), \(i\in S\), occur with probability \(\prod_{i\in S}d_i/(n)_{\underline r}\), where \((n)_{\underline r}=n(n-1)\cdots(n-r+1)\). Counting subsets gives
\[
\mathbb E\binom{F_{\boldsymbol d}}r=\frac{e_r(\boldsymbol d)}{(n)_{\underline r}},\qquad
G_{\boldsymbol d}(z):=\mathbb E z^{F_{\boldsymbol d}}
=\sum_{r=0}^n\frac{e_r(\boldsymbol d)}{(n)_{\underline r}}(z-1)^r.
\]
The derivation includes \(r=0\) and \(r=n\), and zero multiplicities pose no exception.

**One balancing transfer.** Write \(\boldsymbol c\) for the \(n-2\) untouched coordinates. The identity
\[
e_r(a,b,\boldsymbol c)=e_r(\boldsymbol c)+(a+b)e_{r-1}(\boldsymbol c)+ab e_{r-2}(\boldsymbol c)
\]
shows that replacing \((a,b)\) by \((a-1,b+1)\) changes \(e_r\) by exactly \((a-b-1)e_{r-2}(\boldsymbol c)\). Therefore,
\[
G_{\boldsymbol e}(z)-G_{\boldsymbol d}(z)
=\frac{a-b-1}{n(n-1)}(z-1)^2
\sum_{s=0}^{n-2}\frac{e_s(\boldsymbol c)}{(n-2)_{\underline s}}(z-1)^s.
\]
Since \(a+b\ge2\), the total multiplicity \(a+b-2\) of an anonymous filler symbol is nonnegative, and \(\sum c_i+(a+b-2)=n-2\). Apply the preceding match-count calculation to the \(n-2\) untouched named positions and this filler symbol. The last sum is precisely the probability generating function \(\mathbb E z^Y\). Thus for any real function \(\varphi\) on \(\{0,\ldots,n\}\), coefficient comparison yields
\[
\mathbb E\varphi(F_{\boldsymbol e})-\mathbb E\varphi(F_{\boldsymbol d})
=\frac{a-b-1}{n(n-1)}\mathbb E\bigl[\varphi(Y+2)-2\varphi(Y+1)+\varphi(Y)\bigr].
\]
Choosing \(\varphi(x)=(x-t)_+\) produces the stated stop-loss formula. Every convex \(\varphi\) has a nonnegative second forward difference; every strictly convex \(\varphi\) has a positive difference at every integer, so a strict transfer gives strict inequality. The auxiliary \(Y\) is always supported on \(0,\ldots,n-2\).

**General majorization and endpoints.** Any two nonnegative integer vectors of equal sum satisfying majorization are connected, up to permutations, by finitely many unit transfers from a coordinate at least two greater than another. The law above depends only on the elementary symmetric polynomials and hence is invariant under coordinate permutations. Compose the one-step inequalities. The degree vectors \((n,0,\ldots,0)\) and \((1,\ldots,1)\) respectively majorize every admissible vector and are majorized by every admissible vector. Strictness follows from a transfer unless the endpoint degree multisets coincide.

**Moments.** The first two factorial moments of the generating function give
\[
\mathbb EF_{\boldsymbol d}=\frac{\sum_i d_i}{n}=1,
\qquad
\operatorname{Var}(F_{\boldsymbol d})=\frac{n^2-\sum_i d_i^2}{n(n-1)}.
\]
The bottom degree multiset forces one fixed point because every arrow points to one label; the top degree multiset forces a uniform bijection. This proves all assertions for every \(n\ge2\).

## Verification
Run `python3 check.py` in the directory containing this file. It uses only Python's standard library and exact integer/fraction arithmetic. It exhaustively enumerates the \(636\) admissible labeled degree vectors across orders \(2\) through \(6\), verifies their full fixed-point distributions and moment identities, and checks \(3{,}158\) strict balancing comparisons via both exact coefficient differences and stop-loss inequalities. The exact checks are finite corroboration; the proof above supplies the all-order result.

For example, at \(n=4\), balancing the pair \((3,1)\) to \((2,2)\) with both remaining multiplicities zero changes the three probabilities for \(F=0,1,2\) by \((1/12,-1/6,1/12)\). The local stop-loss increase at threshold \(1\) is \(1/12\), matching the formula with \(Y=0\) surely.

## Relationship to prior work
Hansen and Jaworski's 2007-on-line study introduces random mappings with exchangeable prescribed indegrees and gives laws for the cyclic population, components and component sizes; its conditional mapping model is the present sampling model, while its stated structural distributions are different from a convex-order comparison of self-loop counts across specified degree vectors. Their subsequent local-properties paper studies predecessors, successors and related root statistics. Stark's 2026 study of fixed points in multiset permutations defines agreement with a sorted multiset's reference word, where a symbol with multiplicity \(a_i\) occupies \(a_i\) reference positions: that is not the present definition with exactly one named position corresponding to each target. Its fixed-point mean \(\sum_i a_i^2/n\) highlights the distinction from the invariant mean \(1\) proved here.

The central claim is the full majorization-to-convex-order theorem with its exact transfer identity; elementary symmetric factorial-moment enumeration is used as the proof mechanism, not separately claimed as an original combinatorial construction.

## Limitations
The statement is conditional on a complete deterministic indegree sequence and on uniform sampling among compatible mappings. It does not apply without modification to a biased allocation among sources, to self-maps prohibited from having loops, or to a multiset reference word with repeated target positions. Convex order does not assert independence of fixed-point count and indegree vector, nor does it imply first-order stochastic domination. The theorem is an all-order finite-law result; no asymptotic rates or numerical parameter estimates are asserted. The possibility of a historical equivalent hidden in broader multiset-matching literature remains a scientific priority risk.

## References
- Jennie C. Hansen and Jerzy Jaworski, *Random mappings with exchangeable in-degrees*, Random Structures & Algorithms 33 (2008), 105–126; first online 4 September 2007. DOI: https://doi.org/10.1002/rsa.20187.
- Jennie C. Hansen and Jerzy Jaworski, *Local properties of random mappings with exchangeable in-degrees*, Advances in Applied Probability 40 (2008), 183–205. DOI: https://doi.org/10.1239/aap/1208358892.
- Dudley Stark, *Poisson approximations of the number of fixed points in random multiset permutations* (2026). https://arxiv.org/abs/2608.00710.
