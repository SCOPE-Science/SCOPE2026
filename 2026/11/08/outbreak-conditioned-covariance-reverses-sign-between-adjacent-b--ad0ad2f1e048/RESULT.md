# Outbreak-conditioned covariance reverses sign between adjacent but not distant sites on a three-vertex path

## Finding

In the independently imported and independently transmitted bond-outbreak model on a three-vertex contact path, conditioning on the existence of an imported infection creates two inequivalent pair-association regimes. For every nontrivial importation probability, adjacent final-infection indicators change their conditional covariance sign at exactly one transmissibility, whereas the two endpoints remain strictly anticorrelated at all nonperfect transmissibilities. Both unconditioned pairs are nonnegatively correlated.

Write \(t=1-q\), \(z=1-t^3\), and
\[
F_t(p)=-t+(2+t-t^2)p+(t^2+2t-1)p^2-t(1-t)p^3.
\]
For \(q\in(0,1)\) and \(p\in[0,1]\), the exact identities are
\[
z^2\operatorname{Cov}(X_0,X_1\mid S)=q^2t^2(1-p)F_t(p),
\]
\[
z^2\operatorname{Cov}(X_0,X_2\mid S)=-q^2t^3(1-p)^2[1+2p(1+t)+tp^2].
\]
The polynomial \(F_t\) has exactly one root \(p_*(q)\in(0,1)\). The adjacent covariance is negative before the root, positive after it until \(p=1\), and zero exactly at the root and at \(p=1\). The endpoint covariance is strictly negative for \(0\le p<1\), and zero only at \(p=1\). As \(q\downarrow0\), \(p_*(q)\to(\sqrt3-1)/2\); as \(q\uparrow1\), \(p_*(q)\sim(1-q)/2\). For \(q=1/2\), the root is approximately \(0.218089980704572\).

With only two vertices and a single open-edge indicator, the corresponding conditional covariance is \(-q^2(1-q)^2(1-p)^2/[1-(1-q)^2]^2\), so a conditional sign reversal first becomes possible on a three-vertex path.

## Assumptions and scope

Let the contact graph be the simple undirected path \(0-1-2\). All five Bernoulli input variables are mutually independent: three imported-infection seed bits with common success probability \(q\in(0,1)\), and the two edge-opening bits with common success probability \(p\in[0,1]\). Each vertex eventually becomes infected exactly when connected by open edges to at least one initially seeded vertex, including itself. The observable \(X_i\in\{0,1\}\) denotes ever infected, not currently infectious. The conditioning event \(S\) is at least one seed; because there are no other infection sources, it is equivalently the event that an outbreak occurs at all. Its probability \(z=1-(1-q)^3\) is positive. All covariance comparisons are ordinary conditional covariances \(\operatorname{Cov}(X_i,X_j\mid S)\).

## Proof

Set \(t=1-q\). Enumerate the edge states. A vertex is uninfected if its entire open-edge component has no seeds. The two endpoint and center noninfection probabilities are respectively
\[
A=t(1-p)+p(1-p)t^2+p^2t^3,
\]
\[
B=t(1-p)^2+2p(1-p)t^2+p^2t^3.
\]
The noninfection joint probabilities for adjacent vertices and the two endpoints are
\[
C_{01}=t^2(1-p+pt),\qquad C_{02}=t^2[(1-p)^2+(2p-p^2)t].
\]
These formulas can also be reconstructed by independently inspecting the four edge states. In particular, for \(C_{01}\), the two vertices are either disconnected from vertex \(2\) or in one component with it, resulting in the stated factor.

Whenever \(X_i=1\), the conditioning event \(S\) necessarily holds. Hence \(\Pr(X_i=1\mid S)=(1-\Pr(X_i=0))/z\), and similarly \(\Pr(X_i=X_j=1\mid S)=[1-\Pr(X_i=0)-\Pr(X_j=0)+\Pr(X_i=X_j=0)]/z\). Thus
\[
z^2\operatorname{Cov}(X_0,X_1\mid S)=z(1-A-B+C_{01})-(1-A)(1-B),
\]
\[
z^2\operatorname{Cov}(X_0,X_2\mid S)=z(1-2A+C_{02})-(1-A)^2.
\]
Substitution and polynomial expansion give exactly the two factorizations in the finding. Each factor external to \(F_t\) in the adjacent expression is strictly positive for \(p<1\). Every factor in the endpoint expression is strictly positive except its explicit minus sign, proving unconditional-in-parameter endpoint anticorrelation.

For \(0<t<1\), one has \(F_t(0)=-t<0\) and \(F_t(1)=1+t+t^2>0\). Its derivative has the positive Bernstein-form representation
\[
F'_t(p)=(2+t-t^2)(1-p)^2+2(1+3t)p(1-p)+2t(1+2t)p^2.
\]
The three coefficients are strictly positive, so \(F'_t(p)>0\) for every \(0\le p\le1\). The intermediate value theorem and strict monotonicity give precisely one root and the stated signs. As \(t\uparrow1\), continuity and uniqueness give the limit from \(-1+2p+2p^2=0\). As \(t\downarrow0\), the root must tend to zero, and substituting \(p=O(t)\) into \(F_t(p)=0\) gives \(p=t/2+O(t^2)\).

For a two-vertex graph, the analogous direct computation has conditional covariance numerator \(-q^2t^2(1-p)^2\), and denominator \((1-t^2)^2\), proving minimality of the sign reversal in this path family. Finally each \(X_i\) is increasing in all five independent Bernoulli input variables. The elementary product-measure positive-association inequality therefore gives \(\operatorname{Cov}(X_i,X_j)\ge0\) without conditioning, completing the contrast.

## Verification

The supplied `verify.py` runs independently enumerated exact-rational probabilities for all \(8\) seed states and \(4\) edge states, checks the marginal and joint formulas and factorizations against enumerations, verifies both conditional covariance numerators, and tests the strictly positive derivative representation on finite grids. Run `python verify.py` using standard-library Python; this produces `PASS: 21825 ...` on the supplied version. The proof of the all-parameter result is analytical; no finite grid is used as an exhaustive argument over real parameters.

## Relationship to prior work

Moore and Newman (2000) use bond percolation as a basic epidemic model but do not give this exact conditional pair-association phase diagram. Cator and Van Mieghem (2014), particularly their definitions and positive-association arguments, examine unconditioned same-time infection-state correlations from prescribed initial states. Their conclusion does not imply the sign of final-ever-infection covariance after selection on a nonempty random imported-seed set. Rodríguez, Roldán-Correa and Valencia (2018) analyze limitations of the 2014 argument for time-dependent SIR infectious-state indicators and provide a small-graph counterexample; their target is distinct from the present final-ever-infection and outbreak-conditioned model. General positive association for the unconditioned process does not survive conditioning automatically.

## Limitations

This is a minimal finite-graph benchmark with homogeneous, independently seeded importations and independently open undirected edges. Neither a claim about all graphs nor a claim about Markovian finite-time infectious states is made. The transition is not a statement about epidemic persistence in an infinite population. Primary comparisons cover the relevant accessible full text and focused searches; a historical-priority risk remains for unindexed older treatments of conditional reliability and epidemic covariance, and independent audit has not been performed.

## References

- C. Moore and M. E. J. Newman, “Epidemics and percolation in small-world networks,” *Physical Review E* 61, 5678 (2000). https://doi.org/10.1103/PhysRevE.61.5678
- E. Cator and P. Van Mieghem, “Nodal infection in Markovian susceptible-infected-susceptible and susceptible-infected-removed epidemics on networks are non-negatively correlated,” *Physical Review E* 89, 052802 (2014). https://doi.org/10.1103/PhysRevE.89.052802
- P. M. Rodríguez, A. Roldán-Correa, and L. A. Valencia, “Comment on 'Nodal infection ...'”, preprint first public 18 July 2018, https://arxiv.org/abs/1807.06909
