# A sharp five-site covariance reversal and a parity threshold on hard-core fan graphs

## Finding

Let \(F_n=K_1\vee P_n\), with \(n\ge4\), denote the fan consisting of a path of \(n\) vertices and a hub adjacent to every path vertex. In the homogeneous hard-core lattice gas with activity \(z>0\), write \(X_1,X_n\in\{0,1\}\) for the path-endpoint occupations, and let \(I_m(z)\) denote the independence polynomial of the path on \(m\) vertices, with \(I_0(z)=1\), \(I_1(z)=1+z\).

**Theorem.** For every integer \(n\ge4\) and all real \(z>0\),

\[
\operatorname{Cov}(X_1,X_n)=\frac{z^3\bigl(I_{n-4}(z)+(-1)^{n-1}z^{n-3}\bigr)}{\bigl(I_n(z)+z\bigr)^2}.
\]

For every odd \(n\ge5\), the covariance is strictly positive at every activity. For every even \(n\ge4\), a unique \(z_n>0\) makes the covariance vanish; the covariance is positive for \(0<z<z_n\) and negative for \(z>z_n\). These thresholds strictly increase along even \(n\), satisfy \(z_4=1\) and \(1<z_n<2\) for even \(n\ge6\), and obey

\[
z_n=2-\frac{3\log(3/2)}{n}+O(n^{-2}) \quad\text{as even }n\to\infty.
\]

Among **all finite simple graphs with at most five vertices**, an occupation-covariance sign reversal as the *common positive* activity varies occurs first at five vertices; up to graph isomorphism and exchanging the marked vertices, the unique five-vertex example is the two path endpoints of \(F_4\). There

\[
\operatorname{Cov}(X_1,X_4)=\frac{z^3(1-z)}{(1+5z+3z^2)^2}.
\]

Consequently the five-vertex crossing is exactly at \(z=1\), with no sign-changing pair on any graph of at most four vertices.

## Assumptions and scope

Graphs are finite, simple and unweighted. For a graph \(G\), its independent sets \(S\) have probabilities proportional to \(z^{|S|}\) with one common \(z>0\). Occupation variables are binary indicators of membership in the sampled independent set; covariance is the **ordinary unconditioned two-site covariance**, not an inverse-covariance or conditional correlation. The fan \(F_n\) has \(n+1\) total vertices. A sign reversal means the covariance takes both positive and negative values at strictly positive activities. The minimality statement ranges over every labeled graph, including disconnected graphs, and each unordered pair of distinct vertices.

## Proof

**1. Exact endpoint identity.** The independence polynomials of paths obey \(I_0=1\), \(I_1=1+z\), and \(I_m=I_{m-1}+zI_{m-2}\) for \(m\ge2\), by conditioning on the last site. A hub-occupied state excludes every path site. Hence the fan partition polynomial is \(Z_n=I_n+z\). Fixing either endpoint occupied leaves a path of length \(n-2\), so its unnormalized occupation probability is \(zI_{n-2}\). Fixing both endpoints occupied leaves a path of length \(n-4\), so the joint numerator is \(z^2I_{n-4}\). It follows without approximation that

\[
Z_n^2\operatorname{Cov}(X_1,X_n)
=z^2\bigl[I_{n-4}(I_n+z)-I_{n-2}^2\bigr].
\]

**2. Continuant identity.** For \(z>0\), set \(a=(1+\sqrt{1+4z})/2\), \(b=(1-\sqrt{1+4z})/2\), and \(\Delta=a-b\). Solving the path recurrence gives \(I_m=(a^{m+2}-b^{m+2})/\Delta\). Since \(a+b=1\) and \(ab=-z\), direct multiplication yields

\[
I_{n-4}I_n-I_{n-2}^2=-(-z)^{n-2}=(-1)^{n-1}z^{n-2}.
\]

Substitution proves the displayed covariance formula for all \(n\ge4\), including both boundary cases \(n=4,5\).

**3. Signs and unique threshold.** At odd \(n\), every term in \(I_{n-4}+z^{n-3}\) is nonnegative and its constant term is one, so covariance is positive. At even \(n\), the sign is that of \(I_{n-4}-z^{n-3}\). The polynomial \(I_{n-4}\) has nonnegative coefficients, constant term one, and degree \((n-4)/2<n-3\); consequently \(I_{n-4}-z^{n-3}\) has exactly one sign change in its ordered coefficient sequence and has opposite signs at zero and infinity. Descartes' rule plus the intermediate-value theorem give exactly one positive root and the claimed signs.

**4. Monotonic thresholds.** At \(z=1\), \(I_{n-4}(1)\ge1\), with equality for even \(n=4\) only. At \(z=2\), the recurrence gives \(I_{n-4}(2)=(2^{n-2}-1)/3<2^{n-3}\), so \(z_4=1\) and \(z_n\in(1,2)\) for every even \(n\ge6\). For even \(m\ge0\), write \(B=-b>0\); then

\[
\frac{I_{m+2}}{I_m}=
\frac{a^{m+4}-B^{m+4}}{a^{m+2}-B^{m+2}}>a^2>z^2
\qquad (0<z<2),
\]

where the first strict inequality holds because \(a>B>0\), and the second because \(a>z\) exactly when \(z<2\). Thus \(I_{n-2}/z^{n-1}>I_{n-4}/z^{n-3}\) for every even \(n\) and \(0<z<2\). Each ratio is strictly decreasing in \(z\) because all powers of \(z\) in the numerator are strictly below the denominator power. Therefore the next even root lies strictly to the right of the preceding one. For each fixed \(z<2\), the same characteristic-root expression gives \(I_{n-4}(z)/z^{n-3}\to\infty\) along even \(n\), so the increasing roots converge to \(2\).

**5. Sharp approach to two.** With even \(n\), the root relation and the characteristic-root expression imply

\[
(n-3)\log\frac{a(z_n)}{z_n}
=\log\frac{\Delta(z_n)}{a(z_n)}-\log\left(1-\left(\frac{-b(z_n)}{a(z_n)}\right)^{n-2}\right).
\]

As \(z_n\to2\), the right side equals \(\log(3/2)+O(2-z_n)+O(2^{-n})\), while \(\log(a(z)/z)=(2-z)/3+O((2-z)^2)\) near \(2\). First this yields \(2-z_n=O(n^{-1})\), and then substitution gives \(2-z_n=3\log(3/2)/n+O(n^{-2})\). The uniform bounds follow from smoothness of the characteristic roots in a neighborhood of \(2\), and from the exponentially small ratio \((-b)/a\) there.

**6. Sharp five-site minimum.** For every graph \(G\) of order \(1\) through \(5\), every unordered vertex pair \(u,v\), and every independent set \(S\), let \(Z(z)=\sum_Sz^{|S|}\), \(A_u(z)=\sum_{S\ni u}z^{|S|}\), and \(B_{uv}(z)=\sum_{S\ni u,v}z^{|S|}\). Then

\[
Z(z)^2\operatorname{Cov}(X_u,X_v)=B_{uv}(z)Z(z)-A_u(z)A_v(z).
\]

The attached complete exact-arithmetic checker `verify.py` enumerates *every* one of \(2^{\binom m2}\) labeled graphs at each order \(1\le m\le5\), their entire independent-set collections, and all unordered vertex pairs. Its fully exhaustive coefficient certificate establishes: for the 10,650 pairs across the 1,099 graphs, the covariance numerator either has coefficients all of one weak sign or is, for exactly 60 labeled pairs, \(z^3-z^4\). The 60 exceptional cases are precisely the different labelings of \(K_1\vee P_4\) with its two path endpoints marked (automorphism group of size two). Because a polynomial with coefficients of one weak sign cannot reverse on \(z>0\), this exhaustive finite classification proves minimality and uniqueness without relying on numerical sampling. For the fan \(F_4\), the all-size identity gives the same numerator and \(Z_4=1+5z+3z^2\), confirming the exact crossing.

## Verification

Execute `python3 verify.py` with Python 3.9 or newer; it uses only the standard library. The program constructs all possible edge masks and all independent subsets explicitly, independently computes coefficient convolutions for covariance numerators, checks that no other graph/pair has both positive and negative coefficients, and verifies the complete symmetry classification of the 60 labeled exceptional graphs. Its additional finite-path checks cover \(4\le n\le11\); these are independent checks of the infinite-family identity, **not** substitutes for the analytical recurrence/Cassini proof. It reports `PASS labelled_graphs=1099 vertex_pairs=10650 unique_exceptional_labelled_graphs=60` and `PASS fan_cassini_identity n=4..11`.

## Relationship to prior work

The independent-set-polynomial formulation and vertex-deletion recursion are classical; Scott and Sokal's 2003 arXiv preprint (notably its Section 3.1) gives the general hard-core partition formalism. The path recurrence is likewise standard. The new statement here is the combined exact *marked-pair* covariance identity on fans, parity-dependent single threshold and asymptotic, and the sharp minimum/uniqueness among all graphs on at most five vertices. These are not claimed as new partition-function recurrences. Existing research on dissociation polynomials of fan graphs concerns a different admissible-set family; work on fixed-size independent-set covariances of paths and cycles concerns canonical sampling rather than the present common-fugacity fan gas. No proof of historical priority is claimed.

## Limitations

The result concerns path endpoints only, not all vertex pairs on larger fans. It treats uniform positive activity and excludes arbitrary site-specific fugacities. The five-vertex minimality classification is exhaustive only through five vertices and is not a classification of all larger graphs displaying a reversal. The limiting value of the thresholds is an activity crossover, not an infinite-volume thermodynamic phase transition. The literature comparison is bounded and does not establish historical priority; independent validation has not been performed.

## References

- A. D. Scott and A. D. Sokal, *The Repulsive Lattice Gas, the Independent-Set Polynomial, and the Lovász Local Lemma*, arXiv:cond-mat/0309352, first publicly posted 2003-09-15, https://arxiv.org/abs/cond-mat/0309352 (especially Sections 3.1 and 3.3).
- J. I. Brown, C. A. Hickman and R. J. Nowakowski, *On the Location of Roots of Independence Polynomials*, J. Algebraic Combinatorics 19 (2004), 273–282, DOI:10.1023/B:JACO.0000030703.39946.70 (general background on independence polynomials, not a claim of the present covariance theorem).
- published-finding corpus public research records, *Dissociation polynomial and extremal coefficients of fan graphs* (2026-10-04) and *Canonical hard-core path and cycle correlations have distinct square-root thresholds* (2026-10-25), as comparison targets for different invariants and ensembles; their publicly indexed summaries were used, and full text was unavailable in the attempted retrieval.
