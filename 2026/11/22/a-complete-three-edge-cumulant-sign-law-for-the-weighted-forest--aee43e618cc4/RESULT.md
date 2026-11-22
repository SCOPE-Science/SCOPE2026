# A complete three-edge cumulant sign law for the weighted forest gas on theta networks

## Finding

**Theorem.** Let \(G\) consist of \(k\ge2\) internally vertex-disjoint paths \(P_1,\ldots,P_k\) joining two common vertices, each with at least two edges. Give each edge \(e\) an arbitrary finite activity \(t_e>0\). Choose \(A\subseteq E(G)\) with probability proportional to \(\prod_{e\in A}t_e\), conditioned on \(A\) being acyclic; write \(X_e=\mathbf1_{\{e\in A\}}\). For every three *distinct* edges, the joint third cumulant is strictly positive if and only if they lie on three different paths. Otherwise it is strictly negative.

In particular, out of the \(\binom{\sum_i L_i}{3}\) triples, exactly \(\sum_{i<j<\ell} L_iL_jL_\ell\) have positive cumulant, for **every** choice of positive edge activities. Thus the two-path cycle supports no positive distinct-edge third cumulants, whereas every graph with at least three such paths supports some. Equivalently, these cumulants are the three-edge nonlinear susceptibilities \(\partial_{\log t_e}\partial_{\log t_f}\partial_{\log t_g}\log Z_G\), where \(Z_G=\sum_{A\text{ forest}}\prod_{h\in A}t_h\). All assertions concern finite graphs and finite strictly positive edge activities.

## Assumptions and scope

A *spanning forest* means any acyclic spanning edge subset, including the empty forest; it does not mean a spanning tree. Path interiors are mutually disjoint, and no path is a single edge (so that the graph is simple). Set

\[
b_e=\frac{t_e}{1+t_e},\quad p_i=\prod_{e\in P_i}b_e,\quad R_i=\frac{p_i}{1-p_i},\quad \pi_i=\frac{R_i}{1+\sum_hR_h},\quad d_e=\frac{1-b_e}{1-p_i}\quad(e\in P_i).
\]

All quantities \(b_e,p_i,\pi_i,d_e\) are strictly positive, with \(b_e,p_i<1\) and \(0<\pi_i<p_i\). For three distinct edges \(e,f,g\), define

\[
\kappa_3(e,f,g)=\mathbb E[X_eX_fX_g]-\mathbb E[X_eX_f]\mathbb E[X_g]-\mathbb E[X_eX_g]\mathbb E[X_f]-\mathbb E[X_fX_g]\mathbb E[X_e]+2\mathbb E[X_e]\mathbb E[X_f]\mathbb E[X_g].
\]

The following closed forms are the complete classification:

1. If \(e\in P_i,f\in P_j,g\in P_\ell\) with \(i,j,\ell\) all distinct, then
\[
\kappa_3(e,f,g)=2\pi_i\pi_j\pi_\ell d_e d_f d_g>0.
\]
2. If \(e,f\in P_i\) and \(g\in P_j\) with \(i\ne j\), then
\[
\kappa_3(e,f,g)=\pi_i\pi_j(2\pi_i-1-p_i)d_e d_f d_g<0.
\]
3. If all three edges belong to \(P_i\), put \(S_i=\sum_{j\ne i}R_j>0\) and \(r_i=p_iS_i/(1+S_i)\). Then
\[
\kappa_3(e,f,g)=-\frac{r_i(1+r_i)}{(1-r_i)^3}(1-b_e)(1-b_f)(1-b_g)<0.
\]

## Proof

**1. Conditional Bernoulli representation.** Independently include each edge with Bernoulli probability \(b_e\). The resulting mass of an edge set differs from \(\prod_{e\in A}t_e\) only by the constant \(\prod_e(1+t_e)^{-1}\). Define \(Y_i=\prod_{e\in P_i}X_e\), the event that path \(i\) is complete. Every cycle in this graph is the union of two complete terminal-to-terminal paths. Consequently the edge set is a forest exactly when \(\sum_iY_i\le1\). Prior to conditioning, the \(Y_i\) are independent Bernoulli variables of means \(p_i\). The probability of the conditioning event is

\[
Z_0=\prod_i(1-p_i)\left(1+\sum_iR_i\right)>0.
\]

Conditionally, \(\mathbb P(Y_i=1)=\pi_i\), and for distinct \(i,j\), \(Y_iY_j=0\). Given the full vector of path-completion indicators, the edge configurations on different paths remain independent. Also \(\pi_i=R_i/(1+\sum_hR_h)<R_i/(1+R_i)=p_i\), since at least one other path has positive completion probability.

**2. Distinct paths.** For \(e\in P_i\), the conditional mean of \(X_e\) given \(Y_i\) is

\[
\mathbb E[X_e\mid Y_i]=\frac{b_e-p_i}{1-p_i}+d_eY_i.
\]

If three edges are on different paths, their conditional cross-products factor. Hence their third cumulant equals \(d_e d_f d_g\kappa_3(Y_i,Y_j,Y_\ell)\). Three distinct completion events are mutually exclusive, and direct substitution into the cumulant definition gives \(\kappa_3(Y_i,Y_j,Y_\ell)=2\pi_i\pi_j\pi_\ell\). This proves the first formula and strict positivity.

**3. Two edges on one path.** For distinct \(e,f\in P_i\), conditional on \(Y_i=0\),

\[
\mathbb E[X_eX_f\mid Y_i=0]=\frac{b_eb_f-p_i}{1-p_i}.
\]

For \(g\in P_j\), \(j\ne i\), compute the third cumulant using

\[
\kappa_3(e,f,g)=\operatorname{Cov}(X_eX_f,X_g)-\mathbb E[X_e]\operatorname{Cov}(X_f,X_g)-\mathbb E[X_f]\operatorname{Cov}(X_e,X_g).
\]

Conditioning on the mutually exclusive completion variables yields, respectively,

\[
\operatorname{Cov}(X_eX_f,X_g)= -\pi_i\pi_j d_g\left(1-\frac{b_eb_f-p_i}{1-p_i}\right),\qquad \operatorname{Cov}(X_e,X_g)=-\pi_i\pi_jd_e d_g,
\]

and the analogous formula with \(e\) replaced by \(f\). Substitution of \(\mathbb E[X_e]=1-(1-\pi_i)d_e\), followed by cancellation, gives the second displayed exact formula. Its sign is negative because \(2\pi_i-1-p_i< p_i-1<0\).

**4. Three edges on one path.** Let \(S_i=\sum_{j\ne i}R_j\) and \(C_i=1/(1+S_i)\), the probability that all other paths are incomplete conditional on at most one of them being complete. Conditioned on the forest event, the distribution of edges in \(P_i\) is the ordinary product Bernoulli law with the all-present configuration's weight multiplied by \(C_i\). Setting \(r_i=p_i(1-C_i)\), the joint probability-generating function of its edge indicators is

\[
F_i(\mathbf z)=\frac{\prod_{e\in P_i}(1-b_e+b_ez_e)-r_i\prod_{e\in P_i}z_e}{1-r_i}.
\]

Because all three edge indices are distinct, differentiating \(\log F_i\) once in each of \(z_e,z_f,z_g\) and evaluating at all \(z=1\) gives their ordinary joint third cumulant. Factor out the product Bernoulli generating function. The only mixed derivative comes from

\[
\log\left(1-r_i\prod_{h\in P_i}\frac{z_h}{1-b_h+b_hz_h}\right).
\]

A direct third derivative gives \(-r_i(1+r_i)(1-b_e)(1-b_f)(1-b_g)/(1-r_i)^3\). Since \(0<r_i<p_i<1\), this is strictly negative.

Every three-edge choice falls into exactly one of these cases, completing the proof and the counting formula.

## Verification

The accompanying standalone Python 3 program, `verify_theta_cumulants.py`, independently constructs each graph and checks the forest condition by a disjoint-set cycle detector. It then enumerates all edge subsets with exact rational probabilities, computes the third cumulant directly from moments, and compares every triple with its corresponding closed formula and strict sign. Seven test networks with arm lengths \((2,2),(3,4),(2,2,2),(3,3,2),(2,3,4),(2,2,2,2),(3,3,3,2)\) verify **420 distinct triples**. All calculations use arbitrary-precision rational arithmetic, not rounded floating-point approximations. This finite verification tests the proof but is not itself the argument for all lengths or weights.

## Relationship to prior work

Jacobsen, Salas, and Sokal identify the weighted spanning-forest partition model as a statistical-mechanical Potts limit and analyze lattice partition-function behavior, not the present theta-network third cumulants. Erickson's exact series-parallel result establishes the weighted two-edge Rayleigh inequality, but that is a **second-order** statement. The present sign-sensitive **third-order** cumulant has opposite signs depending on whether the edges occupy one, two or three arms; second-order negative correlation cannot determine this sign pattern. The more recent work of Çiçeksiz and Ravichandran likewise analyzes two-edge Rayleigh differences and connectivity correlations; it supplies no claim implying the formula above. The conclusion is limited to the source text examined and does not establish universal historical priority.

## Limitations

This is a complete sign classification only for distinct edge indicators in a finite simple generalized theta host and arbitrary fixed finite positive activities. It does not extend as stated to arbitrary series-parallel graphs, arbitrary cycles coupled through articulation points, general connectedness indicators, higher-order cumulants, or the uniform **spanning-tree-only** measure. No infinite-volume critical phenomenon is claimed. An equivalent earlier unindexed argument cannot be ruled out by database searches. Independent external scientific validation has not been performed.

## References

1. J. L. Jacobsen, J. Salas, A. D. Sokal, “Spanning forests and the \(q\)-state Potts model in the limit \(q\to0\),” arXiv:cond-mat/0401026, first posted 2004-01-04, https://arxiv.org/abs/cond-mat/0401026.
2. A. Erickson, “Sums of squares and negative correlation for spanning forests of series parallel graphs,” arXiv:1008.3660, first posted 2010-08-21, https://arxiv.org/abs/1008.3660.
3. R. A. Çiçeksiz, M. Ravichandran, “Negative Correlations for Forests and the \(q<1\) Random Cluster Model,” arXiv:2610.00549, first posted 2026-09-30, https://arxiv.org/abs/2610.00549.
