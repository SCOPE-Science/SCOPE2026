# A sharp recovery threshold reverses cross-pathogen covariance in synchronous hypergraph SIS

## Finding

In the synchronous two-pathogen HyCo-SIS process, the sign of the covariance between the two pathogen-carriage indicators at the original co-infected source after two rounds can oppose the sign of the *direct* within-host susceptibility interaction. There is a complete and sharp threshold, valid for every finite hypergraph, including overlapping activated triangles.

Let \(v\) be the unique initially co-infected vertex, and let all other vertices initially carry neither pathogen. For the common per-step recovery probability \(\mu\in(0,1)\), put \(s=1-\mu\). Define the single-pathogen random hazard \(H_v\) and the two quantities

\[
U=1-\mathbb E[e^{-H_v}],\qquad V=1-\mathbb E[e^{-\alpha H_v}],
\]

where the random field in \(H_v\) is specified below and \(\alpha>0\) is the secondary-susceptibility multiplier. If \(X_v^{(a)}(2)\) indicates carriage of pathogen \(a\) by \(v\) after two rounds, then

\[
\boxed{\operatorname{Cov}(X_v^{(1)}(2),X_v^{(2)}(2))
=s(1-s)^2(U-V)[2U-s(2+U-V)].}
\]

If \(v\) has a neighbor and positive pairwise transmission, then \(0<U,V<1\). For \(\alpha\ne1\) the unique sign-change threshold is

\[
\boxed{s_*=\frac{2U}{2+U-V}\in(0,1).}
\]

For \(s<s_*\), covariance has the sign of \(1-\alpha\), and for \(s>s_*\) it has the opposite sign; at \(s=s_*\) it vanishes. At \(\alpha=1\), the two pathogen processes are independent from the deterministic initial state and the covariance vanishes for every time. Thus sufficiently rapid recovery produces **negative** two-step co-carriage association under synergistic secondary susceptibility \(\alpha>1\), and **positive** association under competitive secondary susceptibility \(0<\alpha<1\). The sign reverses again for sufficiently high survival \(s\).

## Assumptions and scope

The underlying contact object is an arbitrary finite loopless hypergraph \(\mathcal H=(\mathcal V,\mathcal E)\). Its pairwise adjacency matrix \(A\) is the binary adjacency matrix of distinct pairwise contacts, including clique edges within each higher-order hyperedge, as in the cited HyCo-SIS model. The dynamics are synchronous: all hazards are computed from the start-of-round state, events for different missing/present pathogens and different vertices are independently sampled conditional on that state, an already-carried pathogen may only recover during its round and may not reinfect in that same round. Both pathogens have the same coefficients \(\beta_1>0\) for pairwise exposure, \(\beta_h\ge0\) for group exposure, \(\gamma\ge0\) for overlap reinforcement, and \(\mu\in(0,1)\) for recovery. The secondary infection multiplier is \(\alpha>0\). Group activation requires at least two other carriers: \(r=2\). All hazards are finite.

Initially, one vertex \(v\) carries both pathogens; all other vertices are susceptible to both. For each \(j\ne v\), let \(Z_j\) be independent Bernoulli variables with probability \(p_j=1-e^{-\beta_1 A_{vj}}\). The random field \(Z\) describes the one-pathogen carrier pattern outside \(v\) at time one. With \(\phi_e(v,Z)=\mathbf1\{\sum_{j\in e\setminus\{v\}}Z_j\ge2\}\), set

\[
H_v(Z)=\beta_1\sum_jA_{vj}Z_j+\beta_h\sum_{\substack{e\ni v\\|e|\ge3}}\phi_e(v,Z)
+\gamma\sum_{\substack{e<f,\ e,f\ni v\\|e|,|f|\ge3}} |(e\cap f)\setminus\{v\}|\,\phi_e(v,Z)\phi_f(v,Z).
\]

Here \(e<f\) is any fixed ordering used only to count each unordered pair once. No assumption about regularity, symmetry or disjointness of hyperedges is needed. The theorem concerns only the original source vertex at the second synchronous update. It is not a statement about prevalence covariances at arbitrary times or under arbitrary initial laws.

## Proof

At time zero only \(v\) carries either pathogen, so no group can have two infected members other than any susceptible target, and no higher-order or overlap transmission acts in the first round. Every neighbor \(j\) independently acquires each pathogen with probability \(p_j\). These acquisitions for the two pathogens, and the survival events of their two copies at \(v\), are all independent. Let \(C_a\) indicate survival of pathogen \(a\) at \(v\) after the first round. Then \(C_1,C_2\) are independent Bernoulli\((s)\); the two external carrier fields \(Z^{(1)},Z^{(2)}\) are independent copies of \(Z\), independent also of \(C_1,C_2\).

At the second update, if \(C_a=1\), pathogen \(a\) survives at \(v\) with probability \(s\), independently of the other pathogen's transition. If \(C_a=0\), its acquisition probability is \(1-e^{-H_v(Z^{(a)})}\) when \(C_{3-a}=0\), and \(1-e^{-\alpha H_v(Z^{(a)})}\) when \(C_{3-a}=1\). Averaging over the field gives respectively \(U\) and \(V\). Because the external fields and second-round events are independent between pathogens given \((C_1,C_2)\), conditional outputs factor.

Writing \(M=\mathbb E X_v^{(1)}(2)=\mathbb E X_v^{(2)}(2)\) and \(J=\mathbb E[X_v^{(1)}(2)X_v^{(2)}(2)]\), conditioning on the four possibilities for \((C_1,C_2)\) yields

\[
M=s^2+(1-s)[(1-s)U+sV],
\qquad J=s^4+2s^2(1-s)V+(1-s)^2U^2.
\]

Expanding and factoring \(J-M^2\) gives the boxed covariance identity. If \(v\) has a neighbor, then \(\Pr(H_v>0)>0\) by positive pairwise transmission, while \(H_v\) remains finite and vanishes when no neighbor is infected. Consequently \(U,V\in(0,1)\); they coincide precisely when \(\alpha=1\). For \(\alpha\ne1\), the bracket is strictly decreasing affine in \(s\), positive at \(s=0\) and negative at \(s=1\) because its endpoint values are \(2U>0\) and \(U+V-2<0\). It therefore has exactly one zero in \((0,1)\), namely \(s_*\). Finally, \(U-V\) has sign \(1-\alpha\), establishing every sign assertion.

For a purely pairwise graph of degree \(d\ge1\) at \(v\), put \(p=1-e^{-\beta_1}\) and \(q=1-e^{-\alpha\beta_1}\). Independence across the \(d\) neighbors gives the further exact specialization

\[
U=1-(1-p^2)^d,\qquad V=1-(1-pq)^d.
\]

Thus the two-step covariance of the initially doubly infected source on any simple graph depends on the graph only through its degree, although later-time correlations need not do so.

## Verification

The standalone standard-library script `verify.py` independently enumerates all first-round two-pathogen states for a four-vertex overlapping-triangle hypergraph, then applies the second-round event rule, and compares the resulting exact-rational marginals and joint probability with the formula. It runs 97 exact-rational cases and exits on any disagreement. This computation is a test of the finite-state formula, not a substitute for the proof above.

A nontrivial higher-order example has hyperedges \(\{0,1,2\}\) and \(\{0,1,3\}\), with \(v=0\), \(\beta_1=\beta_h=\gamma=\log 2\), \(r=2\), and \(\alpha=2\). The eight possible one-pathogen neighbor configurations have integer hazard exponents (in units of \(\log 2\)) \(0,1,1,2,1,3,3,6\). Consequently

\[
U=\frac{319}{512},\qquad V=\frac{25215}{32768},\qquad
s_*=\frac{40832}{60737}.
\]

At survival \(s=1/16\) (recovery \(\mu=15/16\)), the exact covariance is

\[
-\frac{639847670625}{70368744177664}<0
\]

although \(\alpha=2\) makes acquiring a second pathogen more likely at every positive exposure. At survival \(s=3/4\), the same hypergraph and transmission parameters give \(271858551/274877906944>0\). This establishes both sign regimes without removing the triangle or overlap mechanisms.

## Relationship to prior work

Liu and Schaposnik (2026) define the exact synchronous two-pathogen HyCo-SIS rules and examine overlap reinforcement, structural projections, one-step hazards and finite-time co-infection. Their statements do not supply the two-step cross-pathogen covariance identity or the recovery-dependent sign phase diagram. The present result uses those defined rules without modifying them. Hébert-Dufresne, Scarpino and Young (2020) demonstrate that interacting contagions may have macroscopic behaviors indistinguishable from social reinforcement, but their deterministic mean-field equivalence is not the present finite-state, two-step covariance law. Brian (2025) analyzes how pre-/postinfection priority effects change prevalence, including a discrete-time four-state model with a non-reinfecting parasite; that system does not imply the present symmetric pairwise/hypergraph threshold. Conditional-independence and binomial calculations used in the proof are classical and not claimed as novel.

## Limitations

Only one deterministic initial seed, with both pathogens at the same source, is treated. The sign of within-host covariance is not a direct measurement of mechanistic synergy: this theorem shows explicit sign reversal due to discrete synchronous turnover. No clinical, empirical or stationary association claim is made. The exact coefficient depends on the model's strict prohibition of recovery and reinfection in one round. A different update convention may remove or alter the sign boundary. Independence is unconditional at \(\alpha=1\) only because the deterministic two-pathogen initial configuration and all pathogen-specific random events are independent.

## References

1. K. Liu and L. P. Schaposnik, *Higher-Order Co-Infection on Hypergraphs*, arXiv:2610.26072v1 (first public version, 2026-10-19), https://arxiv.org/abs/2610.26072 .
2. L. Hébert-Dufresne, S. V. Scarpino and J.-G. Young, *Macroscopic patterns of interacting contagions are indistinguishable from social reinforcement*, Nature Physics 16 (2020), 426–431, https://doi.org/10.1038/s41567-020-0791-2 .
3. J. I. Brian, *Pre- and postinfection priority effects have contrasting outcomes for parasite prevalence in host populations*, Ecosphere 16 (2025), e70208, https://doi.org/10.1002/ecs2.70208 .
