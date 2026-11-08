# A two-scale covariance sign diagram for random-source epidemics on stars

## Finding

In a single-seed independent-bond epidemic on a star with \(k\ge 2\) leaves, a uniformly random index case, and common edge transmissibility \(p\in[0,1]\), let \(X_v\) indicate whether vertex \(v\) has **ever been infected** by the end of the outbreak. Write \(H\) for the hub and \(L_1,L_2\) for distinct leaves. Then, for every integer \(k\ge2\),

\[
\operatorname{Cov}(X_H,X_{L_1})=\frac{1-p}{(k+1)^2}\bigl[k(k-1)p^2+kp-1\bigr],
\]
\[
\operatorname{Cov}(X_{L_1},X_{L_2})=\frac{1-p}{(k+1)^2}\bigl[(k-1)^2p^3+(k+1)p^2-3p-1\bigr].
\]

For \(k\ge3\), the hub–leaf covariance changes sign at exactly one threshold \(r_k\), and the leaf–leaf covariance changes sign at exactly one strictly greater threshold \(s_k\). Thus there are exactly three open regimes:

- \(0<p<r_k\): both pair types have negative covariance;
- \(r_k<p<s_k\): hub–leaf covariance is positive, but leaf–leaf covariance remains negative;
- \(s_k<p<1\): both pair types have positive covariance.

At each threshold the corresponding covariance is zero; at \(p=1\), both are zero. For \(k=2\), the hub–leaf covariance still has a unique interior sign change but the leaf–leaf covariance remains strictly negative throughout \(0\le p<1\). The two thresholds have **different large-degree scales**:

\[
r_k\sim\frac{\sqrt5-1}{2k},\qquad s_k\sim k^{-2/3}\quad(k\to\infty).
\]

When \(k=1\), the sole pair has covariance \(-(1-p)^2/4\), so it remains negative for \(0\le p<1\).

## Assumptions and scope

Fix an integer \(k\ge1\). The contact network is the undirected star with hub \(H\) and leaves \(L_1,\ldots,L_k\). A seed \(S\) is chosen uniformly from the \(k+1\) vertices, independently of the contact successes. Every edge is independently open with the **same** probability \(p\). The infected set is exactly the connected component containing \(S\) in the retained-edge graph. This is the one-generation-per-infection, independent-contact Reed–Frost final-outbreak model on a tree; it is not the full continuous-time SIR model with random, shared infectious periods, where a hub's outgoing contact outcomes may be dependent. Indicators record **ever infected**, not the infectious state at a finite time.

All probabilities and covariances below are unconditional over both the seed and edge states. The conclusions cover every integer \(k\ge1\) and every \(p\in[0,1]\), with stated degeneracies at endpoints.

## Proof

Put \(n=k+1\). The single-vertex and pair probabilities are computed by disjoint seed cases; each probability of a required path is a product of its independent open-edge probabilities. For \(k\ge2\),

\[
\begin{aligned}
\Pr(X_H=1)&=\frac{1+kp}{n},\\
\Pr(X_{L_1}=1)&=\frac{1+p+(k-1)p^2}{n},\\
\Pr(X_H=X_{L_1}=1)&=\frac{2p+(k-1)p^2}{n},\\
\Pr(X_{L_1}=X_{L_2}=1)&=\frac{3p^2+(k-2)p^3}{n}.
\end{aligned}
\]

The last identity partitions the seed among the hub (two edges required), the two designated leaves (two edges required), and the other \(k-2\) leaves (three edges required). Subtracting products of the preceding marginals, then factoring, proves the two covariance formulas. For \(k=1\), the two-vertex probability is \(\Pr(X_H=X_{L_1}=1)=p\), while both marginals equal \((1+p)/2\), giving \(-(1-p)^2/4\).

Define

\[
A_k(p)=k(k-1)p^2+kp-1,\qquad
B_k(p)=(k-1)^2p^3+(k+1)p^2-3p-1.
\]

For \(k\ge2\), \(A_k(0)=-1\), \(A_k(1)=k^2-1>0\), and \(A'_k(p)=2k(k-1)p+k>0\) for \(p\ge0\); therefore \(A_k\) has exactly one zero \(r_k\in(0,1)\), namely

\[
r_k=\frac{\sqrt{5-4/k}-1}{2(k-1)}.
\]

When \(k=2\), direct factorization gives \(B_2(p)=(p-1)(p^2+4p+1)<0\) for \(0\le p<1\). When \(k\ge3\), \(B_k(0)=-1\), \(B_k'(0)=-3\), \(B_k''(p)=6(k-1)^2p+2(k+1)>0\) for \(p\ge0\), and \(B_k(1)=(k-2)(k+1)>0\). Thus \(B_k\) first decreases and then increases, crossing zero exactly once in \((0,1)\). Call this zero \(s_k\).

The roots are strictly ordered: direct polynomial subtraction yields, for \(k\ge2\),

\[
B_k(p)-\frac{k-1}{k}pA_k(p)=2p^2-\left(2+\frac1k\right)p-1<0\qquad(0\le p\le1).
\]

The right-hand side is convex in \(p\); its maximum over \([0,1]\) occurs at an endpoint, where the values are \(-1\) and \(-1/k\). Consequently \(B_k(r_k)<0\). For \(k\ge3\), since \(B_k\) changes from negative to positive only at \(s_k\), it follows that \(r_k<s_k\). Multiplication by the strictly positive factor \((1-p)/n^2\) for \(p<1\) establishes the complete sign diagram.

The explicit formula for \(r_k\) gives \(k r_k\to(\sqrt5-1)/2\). For the other scale, substitute \(p=c k^{-2/3}\), with any fixed \(c>0\), into \(B_k\):

\[
B_k(ck^{-2/3})=c^3-1+O_c(k^{-1/3}).
\]

For every fixed \(0<c_-<1<c_+\), the expression is eventually negative at \(c_-k^{-2/3}\) and positive at \(c_+k^{-2/3}\); uniqueness of the positive zero and arbitrariness of these brackets imply \(k^{2/3}s_k\to1\).

For completeness, at \(p=0\) exactly one vertex (the seed) is infected, giving covariance \(-1/(k+1)^2\) for every distinct pair. At \(p=1\) every vertex is infected with certainty, giving covariance zero. For fixed \(p\in(0,1)\), the formulas additionally imply

\[
\lim_{k\to\infty}\operatorname{Cov}(X_H,X_{L_1})=p^2(1-p),\qquad
\lim_{k\to\infty}\operatorname{Cov}(X_{L_1},X_{L_2})=p^3(1-p).
\]

## Verification

Run `python3 verify_star_covariance.py` using Python's standard library. It independently enumerates all choices of seed and every retained-edge configuration on stars with \(1\le k\le9\) for eight exact rational or endpoint contact probabilities, finds connected components by graph traversal, and compares marginals, joint probabilities, and covariances with the closed formulas. It also checks the exact polynomial comparison on a broad rational grid and separately performs numerical threshold-asymptotic diagnostics. The packaged run passed \(5{,}503\) exact assertions and \(12\) numerical diagnostics. The analytical proof, not this finite enumeration, establishes all integer sizes and continuum parameters.

For a four-vertex star (\(k=3\)) at \(p=1/2\), the hub–leaf covariance equals \(1/16\) while the leaf–leaf covariance equals \(-1/32\). At \(p=3/4\), these become \(37/512\) and \(11/1024\), respectively. These exact witnesses distinguish the intermediate and positive-positive regimes.

## Relationship to prior work

The outbreak–percolation correspondence is classical. Kenah and Robins (2007) analyze epidemic percolation networks, including the role of a single imported infection, and Sharkey et al. (2013 online) derive exact tree-network SIR moment equations. These frameworks motivate the finite-star problem and provide more general background; neither of the inspected texts states the two explicit unconditional **final-infection covariance** polynomials, their ordered sign transitions, or their distinct degree exponents.

Schwartz and Stone (2013) give an exact **SIS** analysis of star networks, focusing on endemic states and thresholds, rather than the final infected set with a uniformly random source. The Cator–Van Mieghem (2014) covariance claim and the Rodríguez–Roldán-Correa–Valencia (2018) discussion concern **infection state at a specified time**, not the eventual-ever-infected indicators here. The latter provides a fixed-time two-node counterexample, which is not this all-degree sign classification. This comparison distinguishes mathematical statements and makes no priority claim beyond inspected material.

## Limitations

The results are exact for one uniformly chosen index case, independent homogeneous edge successes, and an undirected star. They do not extend without additional analysis to multiple simultaneous imported infections, heterogeneous edge probabilities, arbitrary graphs, or continuous-time SIR models with shared random infectious periods. Negative covariance here is not a causal inhibitory effect; uncertainty about the exclusive initial seed is itself a source of dependence. These are model benchmarks, not empirical epidemiological estimates. A historically earlier equivalent star-specific calculation could remain undiscovered.

## References

- Kenah, E. and Robins, J. M. (2007), *Network-based analysis of stochastic SIR epidemic models with random and proportionate mixing*, Journal of Theoretical Biology, DOI: 10.1016/j.jtbi.2007.09.011. Open author manuscript: https://pmc.ncbi.nlm.nih.gov/articles/PMC2186204/
- Sharkey, K. J., Kiss, I. Z., Wilkinson, R. R. and Simon, P. L. (first published 18 December 2013), *Exact Equations for SIR Epidemics on Tree Graphs*, Bulletin of Mathematical Biology, DOI: 10.1007/s11538-013-9923-5. https://link.springer.com/article/10.1007/s11538-013-9923-5
- Schwartz, N. and Stone, L. (2013), *Exact epidemic analysis for the star topology*, Physical Review E, DOI: 10.1103/PhysRevE.87.042815. https://pubmed.ncbi.nlm.nih.gov/23679481/
- Cator, E. and Van Mieghem, P. (2014), *Nodal infection in Markovian susceptible-infected-susceptible and susceptible-infected-removed epidemics on networks are non-negatively correlated*, Physical Review E, DOI: 10.1103/PhysRevE.89.052802. https://doi.org/10.1103/PhysRevE.89.052802
- Rodríguez, P. M., Roldán-Correa, A. and Valencia, L. A. (2018), *Comment on “Nodal infection...”*, arXiv:1807.06909. https://arxiv.org/abs/1807.06909
