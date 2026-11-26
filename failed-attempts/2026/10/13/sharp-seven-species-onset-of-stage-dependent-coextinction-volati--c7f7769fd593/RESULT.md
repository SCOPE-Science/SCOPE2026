# Sharp seven-species onset of stage-dependent coextinction volatility

## Finding

Under uniform primary-species removal without replacement, no single seven-species network need maximize the **variance** of secondary extinctions at all removal stages, even when every secondary species has the same degree. This incompatibility first occurs with four primary and three secondary species, each secondary species connected to exactly two primary species. No smaller nonisolated bipartite system has an analogous incompatibility when the secondary-degree multiset is fixed.

More precisely, for a fixed feasible primary/secondary size and secondary-degree multiset, define a *common volatility maximizer* as one incidence network that simultaneously maximizes the variance of the number of secondary extinctions for every possible number of primary survivors. Every profile with at most six total species has one. At seven total species the **unique failing profile**, with guild roles fixed, is four primary species and three secondary species of degrees \((2,2,2)\).

In the exceptional profile there are exactly three isomorphism types, obtained by interpreting the three secondary neighborhoods as edges of a multigraph on four primary vertices. They are a three-edge star, a four-vertex path, and a doubled edge disjoint from a single edge. Writing \((V_1,V_2,V_3)\) for variances after one, two, or three primary species survive, these types have respectively
\[
(3/4,1/4,0),\qquad(1/4,1/4,0),\qquad(1/4,7/12,0).
\]
Thus the star uniquely maximizes volatility at the one-survivor stage and the doubled-edge configuration uniquely maximizes it at the two-survivor stage. Each type has the same stagewise mean extinction counts \((3/2,1/2,0)\); expectation alone cannot detect this reversal.

## Assumptions and scope

Let \(P\) contain \(m\ge1\) primary species and \(S\) contain \(n\ge1\) secondary species. A network is a simple bipartite graph with every species incident to at least one interaction. For each \(j\in S\), let \(N_j\subseteq P\) be its nonempty set of interaction partners; the unordered multiset \(\{|N_j|:j\in S\}\) is held fixed. The remaining primary species form a uniformly selected subset \(T\subseteq P\) of size \(t\), where \(0\le t\le m\). Secondary species \(j\) disappears exactly when \(T\cap N_j=\varnothing\). Define
\[
X_t=\sum_{j\in S}\mathbf1_{\{T\cap N_j=\varnothing\}},\qquad V_t(G)=\operatorname{Var}(X_t).
\]
Primary extinctions are exogenous; no rewiring, weighted dependency, population dynamics or feedback is assumed. All graphs with fixed \((m,n,\{|N_j|\})\) and no isolated primary species are competitors, up to arbitrary relabeling within either guild. A common volatility maximizer must optimize every \(V_t\), not merely their sum.

## Proof

**Moment identity.** For a nonempty \(U\subseteq P\) define
\[
p_t(U)=\frac{\binom{m-|U|}{t}}{\binom mt},
\]
interpreting the numerator as zero if \(t>m-|U|\). Because exactly \(t\) surviving primary species are sampled without replacement, \(p_t(U)\) is the probability that none belongs to \(U\). Hence linearity and expansion of the square give the exact identities
\[
\mathbb E X_t=\sum_j p_t(N_j),\quad
V_t(G)=\sum_{i,j}p_t(N_i\cup N_j)-\left(\sum_j p_t(N_j)\right)^2.
\]
In particular, for a prescribed secondary-degree multiset, \(\mathbb E X_t\) is *independent of the network topology*. The same identities provide one calculation of every candidate variance, separate from a direct enumeration of survivor sets.

**Exhaustive minimality certificate.** Any graph with at most seven total vertices is described, after secondary-species relabeling, by an integer profile \(1\le d_1\le\cdots\le d_n\le m\) and an ordered tuple of distinct allowed primary neighborhoods for each secondary species (repeated neighborhoods are allowed, distinct incidence entries remain binary). Enumerate each tuple in
\[
\prod_{j=1}^n\binom{[m]}{d_j}
\]
and retain it precisely when the union of its neighborhoods equals \([m]\). Every nonisolated simple bipartite graph occurs in this enumeration after secondary relabeling, and the common-maximizer property is relabel-invariant. For each feasible profile, compute \(\max_G V_t(G)\) at each \(t\), then test whether one eligible \(G\) simultaneously meets all the maxima. The accompanying pure-Python program `verify_stage.py` performs the full finite enumeration, and independently compares direct survivor-set moments against the pair-union formula for each candidate. Through total order seven it checks exactly 97 feasible secondary-degree-multiset profiles and 1,600 incidence matrices with nondecreasing secondary degrees. Exactly one profile fails the common-maximizer test: \((m,n,\mathbf d)=(4,3,(2,2,2))\). In particular every feasible profile with at most six total species passes. These finite exhaustive checks are the certificate for the claimed *finite* minimality, not a proposed proof about larger system sizes.

**Structural classification at the first obstruction.** For the failing profile, interpret each two-element neighborhood as an undirected edge on the four primary species; because no primary species is isolated, the three-edge *multigraph* covers all four vertices. If the edges are pairwise distinct, the resulting ordinary simple graph is a tree on four vertices, so it is a star or a path. If one edge repeats, the third must be disjoint from it to cover all four vertices. Three copies of a single edge cannot cover four vertices. These are exactly the three classes. Directly evaluating the six possible survivor pairs at \(t=2\), and four possible survivors at \(t=1\), gives the variance vectors in the Finding. The program separately enumerates all 114 incidence matrices, with labeled-type counts \(24\), \(72\) and \(18\) for star, path and disjoint-double-edge configurations. Therefore the maximum variance at \(t=1\) equals \(3/4\), attained only by stars, whereas at \(t=2\) it equals \(7/12\), attained only by disjoint-double-edge configurations. No graph can maximize both, proving the obstruction. The formula for \(\mathbb E X_t\) above shows that the three configurations nonetheless have identical means at each stage.

## Verification

Run `python verify_stage.py` in a Python 3.10 or newer standard-library environment. It independently computes \(\mathbb E X_t\) and \(V_t\) via exact fractions from direct enumeration of all \(\binom mt\) survivor sets, compares them with the neighborhood-union moment identity for every enumerated graph and stage, and evaluates simultaneous maxima for every feasible degree profile. It asserts that the sole failing profile is \((4,3,(2,2,2))\), then independently checks the three multigraph types, exact incidence counts and all stated variance vectors. A successful execution prints `VERIFY_OK`. No floating-point tolerance, sampling, or external datasets enter the certificate. The all-size mean and variance identity follows by the separate two-line indicator calculation above; the sharp threshold itself concerns only networks through total order seven.

## Relationship to prior work

The random primary-extinction and loss-of-all-partners rule follows the ecological knockout-network tradition of Memmott, Waser and Price (2004). Burgos and collaborators (2006 preprint) study nestedness and robustness, not the present fixed-stage variance-optimal network classification. Bane, James and colleagues (2018) investigate full-sequence robustness *distributions* and identify network heterogeneity as an important driver of their spread; their variable is the integrated robustness score over an extinction sequence, not the conditional single-stage secondary-extinction variance optimized here. Jones, Zurell and Wiesner (2024) supply analytic **mean** secondary-extinction predictions, and explicitly identify prediction of variance or standard deviation in extinction curves as a further problem. The expectation-only result in that paper cannot distinguish the present equal-degree configurations. Standard probability identities for joint absence or comonotonic random variables do not themselves establish the first feasible guild size and stage-incompatible topology classification when neither guild may contain isolated vertices.

## Limitations

The classification covers all feasible nonisolated profiles with \(m+n\le7\), but it does not classify obstructions in larger systems or model demographic feedback, weighted interactions, heterogeneous extinction risk, resampling, dependent primary removal or alternate secondary-extinction thresholds. Since both guilds are distinguished, transposing the incidence matrix changes the sampling problem. Larger ecological systems and dynamical extinctions may behave differently. The analysis is an exact combinatorial statement about a stipulated ecological null model, not an empirical ecological prediction. No independent audit has been carried out.

## References

1. Memmott, J., Waser, N. M. and Price, M. V. (2004). *Tolerance of pollination networks to species extinctions*. Proceedings of the Royal Society B. DOI: 10.1098/rspb.2004.2909. First publicly available online December 6, 2004.
2. Burgos, E. et al. (2006). *Why Nestedness in Mutualistic Networks?* arXiv:q-bio/0609005, first submitted September 5, 2006.
3. Bane, M. S. et al. (2018). *Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness*. Ecology and Evolution. DOI: 10.1002/ece3.4529.
4. Jones, C., Zurell, D. and Wiesner, K. (2024). *Novel Analytic Methods for Predicting Extinctions in Ecological Networks*. Ecological Monographs. DOI: 10.1002/ecm.1601.
