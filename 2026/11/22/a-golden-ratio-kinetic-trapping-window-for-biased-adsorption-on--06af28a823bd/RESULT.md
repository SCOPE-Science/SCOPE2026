# A golden-ratio kinetic trapping window for biased adsorption on two-subset Kneser networks

## Finding

Let \(N\ge5\), designate a point \(0\) in an \(N\)-point set, and form the two-subset Kneser graph \(KG(N,2)\): vertices are unordered pairs of points, and two such vertices are adjacent exactly when the pairs are disjoint. Run irreversible monomer adsorption with nearest-neighbor exclusion on this graph. Every unoccupied, unblocked site representing \(\{0,a\}\) attempts adsorption at rate \(w>0\); each other site attempts at rate one. All site clocks are independent. Let \(X_{N,w}\) be the number of occupied sites at jamming.

Every jammed configuration is either a full star of \(N-1\) pairs meeting one point, or the three sides of a triangle. Write \(p_N(w)\) for the probability of the triangular jam. Then

\[
\begin{aligned}
p_N(w)={}&\frac{2w}{N-2+2w}\left[\frac{w}{(w+1)(1+(N-3)w)}+\frac{w}{(w+1)(w+N-3)}\right]\\
&+\frac{N-2}{N-2+2w}\frac{w^2+N-3}{(w+N-3)^2}.
\end{aligned}
\]

Consequently \(\Pr(X_{N,w}=3)=p_N(w)\) and \(\Pr(X_{N,w}=N-1)=1-p_N(w)\), with
\[
\mathbb E X_{N,w}=N-1-(N-4)p_N(w),\qquad
\operatorname{Var}(X_{N,w})=(N-4)^2p_N(w)(1-p_N(w)).
\]
For the unbiased process, \(p_N(1)=1/(N-2)\), so the occupancy variance is asymptotic to \(N\).

For any positive sequence \(w_N\) with \(w_N/N\to c\in(0,\infty)\),
\[
 p_N(w_N)\longrightarrow f(c):=\frac{c^2}{(1+2c)(1+c)^2},
\]
whereas \(p_N(w_N)\to0\) if \(w_N/N\to0\) or \(w_N/N\to\infty\). Thus a linear rate bias is the only scale yielding nonzero limiting triangular trapping probability. The limiting normalized occupancy has a two-point law: \(X_{N,w_N}/N\) converges to one with probability \(1-f(c)\) and zero with probability \(f(c)\). Its variance divided by \(N^2\) converges to \(f(c)(1-f(c))\).

The function \(f\) has a unique positive global maximum at the golden ratio \(c_*= (1+\sqrt5)/2\), where
\[
 f(c_*)=\frac{5\sqrt5-11}{2}.
\]
Moreover, for any choice of finite-size maximizers of \(p_N(w)\) over positive \(w\) at all sufficiently large \(N\), their ratios to \(N\) converge to \(c_*\).

## Assumptions and scope

The substrate is exactly \(KG(N,2)\), \(N\ge5\). Incompatibility means disjoint underlying two-subsets, not intersecting ones. A successful deposition is permanent, and blocked sites never become eligible again. Each site's attempt process is independent exponential/Poisson with the stated constant rate. \(w\) may depend on \(N\); all limits concern the terminal random variable and not a finite observation time. Star and triangle are disjoint terminal types because \(N-1>3\).

## Proof

**1. Terminal geometry.** A feasible occupied set corresponds to a pairwise-intersecting family of distinct edges of \(K_N\). The first two accepted edges share exactly one underlying endpoint, say \(ab\) and \(ac\). Every further eligible edge must either be an edge \(ax\) of their common star, or the unique closure edge \(bc\). If \(bc\) wins the next race, the three edges form a maximal triangle and all other edges are blocked. If an edge \(ax\) with \(x\notin\{b,c\}\) wins, then \(bc\) is blocked, and every further accepted edge contains \(a\). All \(N-1\) star edges eventually arrive, since all rates are positive. This exhausts the terminal types.

**2. Three accepted-edge races.** Classify an edge as S if it contains the distinguished point \(0\), and O otherwise. The first accepted edge is S with probability \(s=2w/(N-2+2w)\), because the \(N-1\) S edges have rate \(w\) and the \(\binom{N-1}{2}\) O edges have rate one. After the first edge, the second accepted edge must intersect it. Conditional probabilities for the second type and, given it, probability that the next accepted edge closes a triangle are:

| First type | Second type | Conditional second probability | Conditional closing probability |
|---|---|---|---|
| S | S | \(w/(w+1)\) | \(1/(1+(N-3)w)\) |
| S | O | \(1/(w+1)\) | \(w/(w+N-3)\) |
| O | S | \(w/(w+N-3)\) | \(w/(w+N-3)\) |
| O | O | \((N-3)/(w+N-3)\) | \(1/(w+N-3)\) |

The closure rates are one or \(w\), while the competing star extension rates are respectively \((N-3)w\), \(N-3\), \(N-3\), and \(w+N-4\). Every entry follows by adding the rates of still-eligible sites. Conditioning on the two first-edge types gives exactly the displayed formula for \(p_N(w)\). The two-point occupancy law and its moments follow immediately.

**3. Scaling window.** Substitute \(w=w_N\) into the exact formula. If \(w_N/N\to c\in(0,\infty)\), the first-S probability tends to \(2c/(1+2c)\) and its bracketed triangular contribution tends to zero. The first-O probability tends to \(1/(1+2c)\) and its triangular closure factor tends to \(c^2/(1+c)^2\), proving \(f(c)\). If \(w_N/N\to0\), the first-S contribution is bounded by the first-S probability, which tends to zero, and the first-O closure factor tends to zero. If \(w_N/N\to\infty\), the first-O contribution is bounded by its vanishing first-O probability; the two first-S closure probabilities both vanish. Therefore no other scale has a positive limiting triangle mass. Since \(X_{N,w}\in\{3,N-1\}\), the normalized law and variance statements follow.

**4. Optimal window.** For \(c>0\),
\[
\frac{f'(c)}{f(c)}=\frac{2(1+c-c^2)}{c(1+c)(1+2c)}.
\]
It changes sign exactly at \(c_*=(1+\sqrt5)/2\), proving the unique global maximum and its exact value. Each fixed-size \(p_N\) is continuous for \(w>0\), tends to \(1/(N-3)\) as \(w\downarrow0\), and tends to zero as \(w\to\infty\). For large \(N\), \(p_N(c_*N)\to f(c_*)>0\) exceeds the left boundary value, so a positive maximizer exists. Along a sequence of maximizing rates, no subsequence can have \(w_N/N\to0\) or infinity, since those yield limiting probability zero. Each convergent positive finite subsequence must maximize \(f\), hence tends to \(c_*\). This establishes the last assertion.

## Verification

`verify_exact.py` reconstructs the full feasible-state Markov race independently, using exact rational arithmetic, for \(N=5,6,7\) and five positive rates each. It checks the triangle probability against the stated formula without relying on the first/second-edge case table. `verify_symbolic.py` uses symbolic algebra to confirm the unbiased identity, the finite formula's asymptotic scaling and the derivative/fixed-point identities. Exact finite checks are supporting reproducibility and are not substitutes for Steps 1–4, which prove the all-\(N\) theorem.

## Relationship to prior work

The irreversible graph-adsorption model is classical; see Pippenger (1989) and Evans (1993). The correspondence between random greedy maximal independent sets and adsorption is also treated in full by Krivelevich, Mészáros, Michaeli and Shikhelman (2023 first-public version). Extremal intersecting-family theory, including the Erdős–Ko–Rado and Hilton–Milner results, already identifies structural extremizers and the nonstar family scale; none of that deterministic extremal theory is claimed as new. The new object evaluated here is the rate-biased terminal *probability* on \(KG(N,2)\), its exact singular linear-bias scaling, and its finite-size optimizer limit. The cited locally convergent-graph greedy algorithms framework does not directly calculate this dense, one-marked-point, inhomogeneous-rate law.

## Limitations

No claim is made for \(KG(N,k)\) with \(k\ge3\), for reversible adsorption, for other rate profiles, or for finite-time occupation kinetics. An inaccessible relevant 1989 full paper and possible unindexed exact calculations remain historical-priority risks.

## References

- N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM Journal on Discrete Mathematics* **2** (1989), 393–401, DOI: https://doi.org/10.1137/0402034. Earlier issue month established; exact first public day not inferred.
- J. W. Evans, “Random and cooperative sequential adsorption,” *Reviews of Modern Physics* **65** (1993), 1281–1329, published 1993-10-01, DOI: https://doi.org/10.1103/RevModPhys.65.1281.
- M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, “Greedy maximal independent sets via local limits,” first published 2023-12-18, DOI: https://doi.org/10.1002/rsa.21200.
- P. Frankl and A. Kupavskii, “Improved bounds on the maximum diversity of intersecting families,” *European Journal of Combinatorics* **118** (2024), 103885, DOI: https://doi.org/10.1016/j.ejc.2023.103885.
