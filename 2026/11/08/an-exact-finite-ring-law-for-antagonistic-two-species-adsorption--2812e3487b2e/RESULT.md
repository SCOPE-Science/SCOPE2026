# An exact finite-ring law for antagonistic two-species adsorption

## Finding

Consider repeated-proposal random sequential adsorption on the cycle \(C_L\), for any integer \(L\ge3\). Particles have species \(A\) and \(B\). Initially all vertices are empty. At every vertex independently, proposals of each species arrive in a Poisson process of rate \(1/2\). An attempted particle is accepted if its vertex is empty and neither immediate neighbor is occupied by the opposite species. Occupancies are permanent; rejected proposals have no effect. Write \(X_L\) for the number of empty vertices in the terminal configuration, and \(\theta_L=1-\mathbb EX_L/L\) for the expected occupied fraction.

**Theorem.** For every \(L\ge3\),
\[
\boxed{\mathbb EX_L=\frac L2\sum_{k=0}^{L}\frac{(-1)^k}{k!}-\frac{L-1}{2(L-1)!},\qquad
\theta_L=1-\frac12\sum_{k=0}^{L}\frac{(-1)^k}{k!}+\frac{L-1}{2L!}.}
\]
More structurally, let \(a_m\) and \(b_m\) be the expected number of permanently vacant vertices in a segment of \(m\ge1\) initially vacant consecutive sites, with two permanently occupied endpoint neighbors of the **same** species or **opposite** species, respectively, under the identical independent repeated-proposal rule. Then the exact generating functions are
\[
\boxed{\sum_{m\ge1}a_m z^{m-1}=\frac12\left(\frac{e^{-z}}{(1-z)^2}-e^z\right),\qquad
\sum_{m\ge1}b_m z^{m-1}=\frac12\left(\frac{e^{-z}}{(1-z)^2}+e^z\right).}
\]
Consequently the blocked-site fraction \(q_L=\mathbb EX_L/L\) is strictly increasing with \(L\ge3\), since
\[
q_{L+1}-q_L=\frac{L^2-L-1+(-1)^{L+1}}{2(L+1)!}>0,
\]
and the coverage decreases factorially to
\[
\boxed{\lim_{L\to\infty}\theta_L=1-\frac1{2e},\qquad
\theta_L=1-\frac1{2e}+\frac{L-1}{2L!}+O\!\left(\frac1{(L+1)!}\right).}
\]
The limiting density also describes the repeated-proposal process on the infinite line \(\mathbb Z\), by the shielding argument below.

## Assumptions and scope

All rings are simple cycles with \(L\ge3\) vertices, periodic nearest-neighbor interactions, initially vacant sites, permanent acceptance, and independent rate-\(1/2\) Poisson proposal streams for each species at every site. The rates are equal. All expectations are over the complete deposition history. An empty terminal site has neighbors of opposite species, because otherwise it would have a permitted positive-rate proposal and could not remain empty indefinitely. Thus \(X_L\) is the blocked-site count. For the auxiliary segment model, the endpoint sites are already occupied at time zero and never change, while all \(m\) interior sites are initially vacant; the two boundary sites themselves are not counted.

## Proof

**1. Finite absorption and interval shielding.** At any unoccupied site with at least one allowed species, the next allowed attempt arrives at a fixed positive rate. Every accepted deposition decreases the number of empty sites, and there are finitely many sites. A configuration with a permitted deposition cannot remain unchanged forever, so the process almost surely reaches a configuration where every vacant site is blocked. Once a vertex becomes occupied, it shields its two sides from further interactions across that vertex. Hence, after an accepted deposition in an empty segment with fixed occupied endpoints, the remaining vacant pieces evolve independently with their inherited fixed endpoint species.

**2. First-success recurrences.** For one empty site between equal occupied species, it is eventually filled; between opposite species, it is permanently blocked. Therefore \(a_1=0\), \(b_1=1\). For \(m\ge2\), a proposal can be accepted at either end vacant site only in the species of its occupied endpoint neighbor, at rate \(1/2\) each. Every one of the \(m-2\) strictly interior vacant sites admits either species at total rate one. Thus the total rate of **successful** depositions is \(m-1\), independent of the boundary species.

If the first successful deposition occurs at one of the two vacant endpoint sites, the remaining segment has length \(m-1\) and retains the same boundary relationship. If it occurs at position \(i\in\{2,\ldots,m-1\}\), the deposited species is equally likely \(A\) or \(B\); the two remaining pieces have lengths \(i-1\) and \(m-i\), and the conditional expectation for either piece, averaged over the deposited species, is half the sum of its same- and opposite-boundary expectations. Averaging these mutually exclusive events yields
\[
(m-1)a_m=a_{m-1}+\sum_{j=1}^{m-2}(a_j+b_j),\qquad
(m-1)b_m=b_{m-1}+\sum_{j=1}^{m-2}(a_j+b_j).
\]
The empty sum for \(m=2\) is zero. Subtraction and the base values give the exact difference
\[
\boxed{b_m-a_m=\frac{1}{(m-1)!}\quad(m\ge1).}
\]

**3. Solving the generating functions.** Put \(A(z)=\sum_{m\ge1}a_m z^{m-1}\), regarded first as a formal power series. Substituting \(b_m=a_m+1/(m-1)!\) into the first recurrence, summing over \(m\ge2\), and using \(\sum_{m\ge1}z^{m-1}/(m-1)!=e^z\), gives
\[
A'(z)=A(z)+\frac{z}{1-z}\bigl(2A(z)+e^z\bigr),\qquad A(0)=0.
\]
The integrating factor is \(e^z(1-z)^2\), and hence
\[
\frac{d}{dz}\bigl[e^z(1-z)^2 A(z)\bigr]=z(1-z)e^{2z}.
\]
Integrating with the initial condition gives
\[
A(z)=\frac{e^{-z}}{2(1-z)^2}-\frac{e^z}{2},\qquad
B(z)=A(z)+e^z=\frac{e^{-z}}{2(1-z)^2}+\frac{e^z}{2}.
\]
The identities hold as formal series and analytically on \(|z|<1\). Coefficient extraction gives
\[
a_m=\frac12\sum_{k=0}^{m-1}\frac{(-1)^k(m-k)}{k!}-\frac{1}{2(m-1)!}
=\frac{m+1}{2}\sum_{k=0}^{m+1}\frac{(-1)^k}{k!}-\frac1{2(m-1)!}.
\]
The equality of the two finite sums follows by separating the terms \(k=m,m+1\) and shifting the factorial in the weighted sum.

**4. Returning to a ring.** The first accepted deposition on the empty ring occurs at a uniformly random site and has a uniformly random species. It leaves a single interval of \(L-1\) unoccupied sites between two copies of the **same** occupied ring site. Thereafter its total number of permanent vacancies has expectation \(a_{L-1}\). Therefore \(\mathbb EX_L=a_{L-1}\), and the displayed exact ring formula follows by setting \(m=L-1\) in the coefficient formula. Translation invariance gives each site's terminal blocking probability \(q_L=\mathbb EX_L/L\).

**5. Monotonicity and asymptotic limit.** Let \(S_L=\sum_{k=0}^{L}(-1)^k/k!\). Then \(q_L=S_L/2-(L-1)/(2L!)\), and subtraction at consecutive values proves the stated positive increment. The alternating-series remainder satisfies \(|S_L-e^{-1}|\le1/(L+1)!\). Substituting this into the exact formula proves the limit and factorial-error expansion.

**6. Infinite-line interpretation.** Couple the independent proposal processes on increasing cycles with those on \(\mathbb Z\) inside any fixed interval. At each integer site \(j\), write \(T_j\) for its first proposal time, an independent continuous exponential random variable. Whenever \(T_j<\min\{T_{j-1},T_{j+1}\}\), its first proposal is certainly accepted and makes \(j\) a permanent species-fixed shield. On disjoint triples, these events are independent and each has probability \(1/3\). Hence with probability tending to one as \(R\to\infty\), there are such shields strictly to both sides of the origin within distance \(R\). Their acceptance occurs before either adjacent site's first proposal, so interactions outside the two shields cannot affect the origin's terminal state, even before the shields become occupied. The corresponding coupled ring and line outcomes at the origin consequently agree with probability tending to one as the ring size tends to infinity. Bounded convergence of their zero-one terminal vacancy indicators identifies the infinite-line mean coverage with \(\lim_{L\to\infty}\theta_L=1-1/(2e)\).

## Verification

The standalone program `verify_ab_cycle.py` performs independent finite-state continuous-time Markov calculations in exact rational arithmetic (not simulation). It calculates terminal blocked counts by enumerating all successful state transitions of the full cycle, independently computes same/opposite-boundary interval processes, and compares both against the recurrence and closed coefficients. It checks every ring length from \(3\) through \(11\), both boundary types for interval lengths through \(9\), the factorial difference and generating-function coefficients through interval length \(80\), and the strict monotonicity formula at cycle lengths through \(59\). Its latest replay produced 324 exact rational comparisons passed. These finite checks support, but do not replace, the all-size recurrence and infinite-volume shielding proof.

Representative exact values are \(\mathbb EX_4=1/2\), \(\mathbb EX_5=5/6\), \(\mathbb EX_6=13/12\), and \(\mathbb EX_8=353/240\). Reproduce with `python verify_ab_cycle.py` using only the Python standard library.

## Relationship to prior work

Martins, Dickman and Ziff (first public arXiv posting 2022-11-09, Section V, equation (47) in the rendered text) **already proposed the displayed finite-ring coverage formula** based on numerical evidence and found the candidate infinite-line value \(1-1/(2e)\). Neither formula is presented here as newly guessed. The new claim is a general proof, the two boundary-conditioned generating functions, and the resulting sharp monotonic factorial convergence. The authors explicitly described the finite-ring formula as strongly supported rather than proved.

Do Amaral and dos Santos (arXiv:2306.09786, 2023) derive exact coverage in a **different** one-deposition-attempt-per-site model. They explicitly distinguish it from repeated-attempt dynamics; their all-time formula does not yield this repeated-proposal ring law. Penrose and Sudbury (2005) treat random-priority one-species monomer/dimer blocking and annihilation on graphs, not this two-species repeated-proposal system. Other stochastic deposition laws and previously analyzed small complete multipartite graphs overlap only special small-cycle examples, not the all-ring formula or its proof.

## Limitations

The formulas are restricted to exactly equal proposal rates and simple cycles (or their same/opposite-boundary interval reductions). The theorem does not establish biased-rate closed forms, finite-time occupation laws, higher moments, or the full distribution of terminal vacancies. The cited 2022 expression was conjectured before this proof; historical priority of a proof remains subject to independent review, especially a further one-dimensional work announced as forthcoming in that paper but not located in the checked accessible sources. No independent audit is claimed.

## References

1. P. H. L. Martins, R. Dickman and R. M. Ziff, *Percolation in two-species antagonistic random sequential adsorption in two dimensions*, arXiv:2211.04622 (first posted 2022-11-09), Section V, equation (47). https://arxiv.org/abs/2211.04622
2. C. S. do Amaral and D. C. dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site*, arXiv:2306.09786 (first posted 2023-06-16). https://arxiv.org/abs/2306.09786
3. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Annals of Applied Probability 15 (2005), 853–889, arXiv:math/0503519. https://arxiv.org/abs/math/0503519
