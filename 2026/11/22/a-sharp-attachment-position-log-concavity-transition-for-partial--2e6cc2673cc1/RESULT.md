# A sharp attachment-position log-concavity transition for partial Petrial polynomials of four-vertex branches

## Finding
For every integer \(m\ge1\), let \(T_m^{\mathrm{end}}\) and \(T_m^{\mathrm{int}}\) be obtained by taking \(m\) disjoint copies of the four-vertex path and connecting a new common hub to, respectively, an endpoint or a next-to-end vertex in each copy. Both trees have \(4m+1\) vertices and the same number of attached paths.

Define \(P_G^\times(z)=\sum_{F\subseteq V(G)}z^{\operatorname{rank}_{\mathbb F_2}(A_G+\operatorname{diag}(1_F))}\). Then
\[
P_{T_m^{\mathrm{int}}}^{\times}(z)=z^{3m}\left[(1+z)(2+11z)^m+2z^2\bigl((5+11z)^m-(2+11z)^m\bigr)\right],
\]
\[
P_{T_m^{\mathrm{end}}}^{\times}(z)=z^{3m}\left[(1+z)(11z)^m+2z^2\bigl((5+11z)^m-(11z)^m\bigr)\right].
\]
The sequence of nonzero coefficients of the endpoint-rooted polynomial is log-concave at every \(m\), strictly so whenever there are at least three coefficients. The internally rooted polynomial is strictly log-concave for \(1\le m\le6\), and is not log-concave for any \(m\ge7\). The sharp first failing tree has \(29\) vertices; its first three nonzero coefficients are \(128,5056,242234\), whose log-concavity defect is \(-5442816\).

## Assumptions and scope
Graphs are finite, simple and unweighted. The root in each copy of the four-vertex path is either its first vertex (endpoint case) or second vertex (internal case); the other endpoint/internal choice is isomorphic. Polynomial exponents are **matrix ranks**, not coranks, and all computations are over the two-element field. Log-concavity compares consecutive nonzero coefficients, with no unlisted zeros in their support. For one or two coefficients the condition holds vacuously. The theorem concerns these two tree families only; it is not a minimum-order classification among all trees.

## Proof
**1. Rooted path data.** For a rooted graph \((H,c)\) with every binary diagonal perturbation of corank at most one, let \(a\) be the number of invertible perturbations, \(b\) the number of singular perturbations whose one-dimensional kernel vanishes at \(c\), and \(\gamma\) the number whose kernel does not vanish at \(c\). For \(H=P_4\), the path recurrence \(P_{P_s}^\times(z)=zP_{P_{s-1}}^\times(z)+2z^2P_{P_{s-2}}^\times(z)\) gives \(P_{P_4}^\times(z)=5z^3+11z^4\), hence \(a=11\) and \(b+\gamma=5\). There is no corank at least two because a kernel vector of a perturbed path is determined by its initial coordinate via successive row equations.

Every nonzero kernel vector of a perturbed path has nonzero endpoint coordinates, so an endpoint root gives \((a,b,\gamma)=(11,0,5)\). For an internal root splitting the remaining path into arms of lengths one and two, a kernel with root coordinate one exists exactly when both perturbed arm matrices are invertible; there is one such perturbation on \(P_1\) and three on \(P_2\). Thus \(\gamma=3\), \(b=2\), and \((a,b,\gamma)=(11,2,3)\). These counts also follow from the Jacobsthal identities in Feng and Yan [1, Corollary 14].

**2. Complete rank polynomials.** Feng and Yan's rooted-attachment identity [1, Lemma 2, Corollary 3] is
\[
C_{T_m}(t)=(1+t)(a+bt)^m+\frac{2}{t}\left[(a+(b+\gamma)t)^m-(a+bt)^m\right],
\]
where \(C_G(t)=\sum_F t^{|V(G)|-\operatorname{rank}(A_G+\operatorname{diag}(1_F))}\). For completeness, its kernel argument splits branch choices into (i) all branch kernels vanishing at their roots, contributing corank exponents \(K,K+1\) for the two hub diagonal choices, and (ii) at least one kernel visible at its root, contributing corank \(K-1\) twice. The displayed identity follows by summing the respective products. Substitute the two triples above and reverse coefficients by \(P_G^\times(z)=z^{|V(G)|}C_G(z^{-1})\), obtaining the two stated formulas.

**3. Internal-root threshold.** Remove the common shift \(z^{3m}\) and denote the remaining coefficients by \(q_{m,j}\). Binomial extraction gives
\[
q_{m,0}=2^m,\qquad q_{m,1}=2^{m-1}(2+11m),
\]
\[
q_{m,2}=121\binom m2 2^{m-2}+11m2^{m-1}+2(5^m-2^m).
\]
The first defect is exactly
\[
q_{m,1}^2-q_{m,0}q_{m,2}
=2^{2m-3}\left[121m^2+165m+24-16\left(\tfrac52\right)^m\right].
\]
At \(m=7\) it equals \(-5442816\). If \(f(m)=121m^2+165m+24\), then for \(m\ge7\), \(f(m+1)/f(m)\le((m+1)/m)^2\le(8/7)^2<5/2\), since \(f\) has positive coefficients. Therefore once \(16(5/2)^m>f(m)\) holds at seven it persists at every larger integer. For each \(1\le m\le6\), direct integer substitution into the polynomial gives, respectively, the minimum of all applicable interior defects
\[
135,\ 1476,\ 10864,\ 63840,\ 295872,\ 749440.
\]
Each is strictly positive, completing the sharp classification (with all finite coefficient arrays reproduced in the verification file).

**4. Endpoint-rooted log-concavity.** For \(m\ge2\), after removing \(z^{3m}\), reversing the positive coefficient sequence, and dividing every coefficient by \(11^m\), the sequence becomes
\[
c_j=2\binom mj\left(\frac5{11}\right)^j+\mathbf1_{\{j=1\}}+\mathbf1_{\{j=2\}},\qquad 1\le j\le m.
\]
For all \(4\le j\le m-1\), the adjacent triple consists solely of positively scaled binomial coefficients, so \(c_j^2>c_{j-1}c_{j+1}\). For the remaining possible interior indices, exact expansion gives
\[
c_2^2-c_1c_3=\frac{625m^4-1375m^3+21650m^2-20900m+43923}{43923},
\]
\[
c_3^2-c_2c_4=\frac{625m(m-1)(m-2)(25m^3-388m+1089)}{63776196}.
\]
When \(m\ge4\), writing \(t=m-4\ge0\), the first numerator becomes \(625t^4+8625t^3+65150t^2+246300t+378723\), strictly positive; and the last cubic becomes \(25t^3+300t^2+812t+1137\), also strictly positive. The cases \(m=1,2\) have fewer than three coefficients and are vacuous. For \(m=3\), the endpoint coefficients are \((250,2981,4961)\) in increasing degree, with a positive sole defect. Reversal and positive scaling preserve log-concavity. This proves the endpoint result for all integers \(m\ge1\).

## Verification
The included standalone `verify_petrial_p4.py` directly enumerates all binary diagonal perturbations of both tree families for \(m=1,2,3\) and independently compares exact rank-count histograms to the claimed formulas. It also calculates all integer coefficient defects through \(m=100\), checks the first-defect identity and the 29-vertex boundary values. All checks returned `VERIFY_OK`. Finite enumeration corroborates but does not establish the unbounded conclusions; those follow from the inequalities in the proof. To reproduce, run `python3 verify_petrial_p4.py` with the Python 3 standard library; no external input data are required.

## Relationship to prior work
Feng and Yan [1] defined and proved the repeated-root attachment formula used explicitly here, proved exact log-concavity for a different family with five-vertex path branches rooted in the middle, and established only **eventual** failure for every internally rooted path [1, Theorem 13 and Corollary 14]. The present contribution is the exact first failure for four-vertex internally rooted branches and the opposing **all-order positive result** for endpoint-rooted branches, with closed polynomials. The attachment identity and general eventual-failure conclusion are **not claimed as new**. Deng and Zhang [2] characterized trees with two or three nonzero terms; that result does not give this many-coefficient phase transition.

## Limitations
No assertion is made that \(29\) is the smallest tree order at which the polynomial fails log-concavity, or that the two families exhaust all trees built from four-vertex paths by other gluings. Independent mathematical validation remains outstanding. Published or unindexed overlapping special cases might exist beyond the inspected source scope.

## References
[1] Ruiqing Feng and Qi Yan, *Strict unimodality without log-concavity for partial Petrial polynomials*, arXiv:2611.07503v1, first submitted 2026-11-05, https://arxiv.org/abs/2611.07503. See Lemma 2, Corollary 3, Theorem 13, Corollary 14, and the proof around pp. 5–8 and 24–26.

[2] Qingying Deng and Chaoyang Zhang, *A Characterization of Trees with Trinomial Partial Petrial Polynomials*, arXiv:2608.01748v1, first submitted 2026-08-03, https://arxiv.org/abs/2608.01748.
