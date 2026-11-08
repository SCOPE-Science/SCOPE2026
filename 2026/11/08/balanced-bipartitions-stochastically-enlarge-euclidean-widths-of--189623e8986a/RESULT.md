# Balanced bipartitions stochastically enlarge Euclidean widths of symmetric edge polytopes

## Finding
For every integer \(n\ge4\) and \(1\le p\le\lfloor n/2\rfloor\), put \(q=n-p\). Let \(A\sqcup B=[n]\), with \(|A|=p\), and let
\[
Q_{p,q}=\operatorname{conv}\{\pm(e_i-e_j):i\in A,\ j\in B\}
\subset H=\{x\in\mathbb R^n:\sum_i x_i=0\}.
\]
For a Haar-uniform unit vector \(U\) in \(H\), write \(W_{p,q}=h_{Q_{p,q}}(U)+h_{Q_{p,q}}(-U)\) for the Euclidean directional width. For each integer \(1\le p<\lfloor n/2\rfloor\) and every real \(w\),
\[
\Pr\{W_{p+1,q-1}\le w\}\le \Pr\{W_{p,q}\le w\}.
\]
Consequently, for every real \(r>0\),
\[
\mathbb E W_{p+1,q-1}^{r}>\mathbb E W_{p,q}^{r}.
\]
In particular, among complete-bipartite symmetric edge polytopes of fixed graph order \(n\), the balanced partition uniquely maximizes the mean Euclidean width, up to exchanging the two part sizes. The star partition uniquely minimizes it.

More precisely, for \(t\ge0\) and any vector \(u\in H\), form the graph \(F_t(u)\) on \([n]\) with an edge \(ij\) exactly when \(|u_i-u_j|>t\). If this graph has edges, its unique nontrivial connected component has vertex count \(s_t(u)\ge2\); otherwise put \(s_t(u)=0\). Then the entire directional-width distribution obeys
\[
\Pr\{W_{p,q}\le2t\}=
\mathbb E_U\!\left[\mathbf1_{\{s_t(U)=0\}}+
\mathbf1_{\{s_t(U)\ge2\}}
\frac{\binom p{s_t(U)}+\binom q{s_t(U)}}{\binom n{s_t(U)}}\right],
\]
with \(\binom as=0\) when \(s>a\). This identity is a conditional finite-counting formula, not an asserted closed elementary expression for the spherical integral.

## Assumptions and scope
All vectors use the inherited Euclidean metric of the zero-sum subspace \(H\). The random direction is uniform on its unit sphere, not uniform in the polytope, and the width is the full two-sided projection length. The graph \(K_{p,q}\) has at least one vertex in each part; \(n\) is fixed when comparing partitions. The strict statement concerns all positive real moments and mean width, not strict CDF ordering at every threshold.

## Proof
**Support function and exchangeability.** By the definition of the convex hull,
\[
W_{p,q}(u)=2\max_{i\in A,j\in B}|u_i-u_j|.
\]
The law of \(U\) is invariant under every coordinate permutation. Thus, conditional on the unordered coordinate values, assigning the indices in \(A\) to \(p\) of these values is equivalent to selecting a uniformly random \(p\)-subset of \([n]\).

**A one-component lemma.** Fix any \(z_1,\ldots,z_n\in\mathbb R\) and \(t\ge0\). The graph with edges \(ij\) whenever \(|z_i-z_j|>t\) has at most one component containing an edge. Indeed, take any two edges, order their endpoint values as \(a<b\) and \(c<d\), and assume \(a\le c\). Since \(d-c>t\), we have \(d-a>t\). The edge between the indices whose values are \(a\) and \(d\) joins the original two edges (unless they already share a vertex). Hence all edges lie in one component; every other vertex is isolated. This argument also permits coincident coordinate values.

**Conditional distribution.** A bipartition has \(\max_{i\in A,j\notin A}|z_i-z_j|\le t\) precisely when no edge of the preceding graph crosses the partition. If the graph has no edges, this is automatic. Otherwise, its unique nontrivial component of size \(s\) must be monochromatic. Out of the \(\binom np\) possible \(p\)-subsets, exactly \(\binom{n-s}{p-s}+\binom{n-s}p\) place all \(s\) vertices in \(A\) or all in its complement. By the elementary binomial identities,
\[
\Pr\{\max_{i\in A,j\notin A}|z_i-z_j|\le t\mid z\}
=\frac{\binom ps+\binom qs}{\binom ns}.
\]
Averaging over spherical directions gives the asserted formula.

**Sharp monotonicity.** For \(p<\lfloor n/2\rfloor\), so \(q\ge p+2\), the difference of the conditional fractions at consecutive part sizes is
\[
\frac{\binom{p+1}s+\binom{q-1}s-\binom ps-\binom qs}{\binom ns}
=\frac{\binom p{s-1}-\binom{q-1}{s-1}}{\binom ns}\le0
\]
for every \(s\ge2\), since \(q-1>p\). The no-edge case has equal probabilities. After averaging, this proves first-order stochastic dominance.

**Strictness.** A Haar-uniform \(U\) has distinct coordinates almost surely. Fix any vector with distinct ordered values \(z_{(1)}<\cdots<z_{(n)}\). The interval
\[
I=\big(\max\{z_{(n)}-z_{(2)},\ z_{(n-1)}-z_{(1)}\},\ z_{(n)}-z_{(1)}\big)
\]
is nonempty. For every \(t\in I\), the far-pair graph has exactly one edge, between the extreme coordinates, and so \(s_t=2\). As \(q-1>p\), the preceding binomial difference is strictly negative for \(s=2\). Therefore, for every distinct-coordinate vector, the conditional width distribution for \((p+1,q-1)\) strictly dominates that for \((p,q)\) on an interval of positive length. Since for any \(r>0\)
\[
\mathbb E W^r=r\int_0^{2\sqrt2}w^{r-1}\Pr\{W>w\}\,dw
\]
(the bound \(W\le2\sqrt2\) holds on the unit sphere), Tonelli's theorem and the strictly positive conditional integrals give the strict moment inequality. Repeating adjacent transfers proves uniqueness of the balanced maximizer and star minimizer among part sizes.

## Verification
The standalone `verify.py` independently enumerates the bipartitions of 20 deterministic real-coordinate configurations in dimensions \(3\) through \(7\), checking the binomial conditional distribution for six thresholds per configuration and checking monotonicity for every eligible partition size. It also verifies the \(s=2\) strict interval in eleven more dimensions (\(4\) through \(14\)). The checker outputs `BALANCED_BIPARTITE_WIDTH_CHECKS_PASSED` when successful. It verifies finite instances only; the proof above gives the all-dimensional result.

## Relationship to prior work
The symmetric edge polytope construction and the complete-bipartite family appear in Higashitani--Jochemko--Michałek (2018), which determines facet structure and Ehrhart \(h^*\)-polynomials, not directional-width probability laws. Chen--Davis--Korchevskaia (2021) describes face/facet subgraphs of symmetric edge polytopes and does not imply an ordering of randomly oriented widths. Ohsugi--Tsuchiya (2020) develops matching-polynomial and lattice-volume invariants, rather than the Euclidean width distribution. The observed balance law is a metric and stochastic comparison for different nonnested polytopes, not a corollary of their \(h^*\)-polynomials or facet counts.

## Limitations
The distribution formula involves averaging a piecewise-constant binomial statistic over the sphere; a closed elementary probability density is not supplied. The result does not assert a pointwise support-function ordering, since the polytopes at differing part sizes are not nested in a fixed realization. Strictness applies to positive moments; the weak CDF ordering may have equality at particular thresholds. Historical priority cannot be guaranteed by a finite literature search; potential equivalent formulations under random-cut or extremal-distance terminology remain a risk.

## References
- A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (20 July 2018), Sections 2--4, especially Proposition 3.4 and Theorem 4.1.
- T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315v1 (26 July 2021), Sections 3--4.
- H. Ohsugi, A. Tsuchiya, *Symmetric edge polytopes and matching generating polynomials*, arXiv:2008.08621v1 (19 August 2020), Sections 1--2.
