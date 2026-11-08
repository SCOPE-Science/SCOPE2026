# Exact weighted Lipschitz spread on crown graphs: two partition discrepancies and exceptional pairs

## Finding
For every integer \(n\ge3\), let \(C_n\) have vertices \(A_1,\ldots,A_n,B_1,\ldots,B_n\) and edges \(A_iB_j\) precisely when \(i\ne j\). Give its vertices arbitrary strictly positive probability masses \(a_i=\mu(A_i)\), \(b_i=\mu(B_i)\), with \(\sum_i(a_i+b_i)=1\). Put
\[
\alpha=\sum_i a_i,\qquad \beta=1-\alpha,\qquad
\delta_A=\min_{\varepsilon\in\{-1,1\}^n}\left|\sum_i a_i\varepsilon_i\right|,\qquad
\delta_B=\min_{\varepsilon\in\{-1,1\}^n}\left|\sum_i b_i\varepsilon_i\right|,
\]
and
\[
E_i=\frac14+2(a_i+b_i)-\left(\alpha-\frac12+2(b_i-a_i)\right)^2.
\]
Then the sharp real one-Lipschitz variance, equivalently the squared norm of the centered inclusion of the Lipschitz space modulo constants into \(L^2(\mu)\), is
\[
\boxed{\operatorname{spr}_{\mu}(C_n)
=\max\left\{\alpha-\delta_A^2,\ \beta-\delta_B^2,\ \max_{1\le i\le n} E_i\right\}.}
\]
All maximizing potentials, up to translation and multiplication by \(-1\), are exactly the configurations below whose displayed branch equals this maximum:

1. On the \(A\) side use signs \(\varepsilon_i\in\{-1,1\}\) minimizing \(\left|\sum_i a_i\varepsilon_i\right|\), and set all \(B\) values to zero.
2. On the \(B\) side use signs minimizing \(\left|\sum_i b_i\varepsilon_i\right|\), and set all \(A\) values to zero.
3. For some maximizing index \(i\), set \(f(A_i)=0\), \(f(B_i)=3\), and \(f(A_j)=2\), \(f(B_j)=1\) for all \(j\ne i\).

For the matched-pair symmetric law \(a_i=b_i=q_i/2\), write \(q_i>0\), \(\sum_iq_i=1\), and \(D=\min_{\varepsilon}|\sum_iq_i\varepsilon_i|\). The formula simplifies to
\[
\boxed{\operatorname{spr}_{\mu}(C_n)=\max\left\{\frac14+2\max_iq_i,\ \frac12-\frac{D^2}{4}\right\}.}
\]
The exact boundary between exceptional-pair and discrepancy minimizers is \(8\max_iq_i+D^2=1\), including equality coexistence. With rational masses encoded in binary, deciding whether \(\operatorname{spr}_{\mu}(C_n)\ge1/2\) is NP-complete even under the promised restrictions \(a_i=b_i=q_i/2\) and \(\max_iq_i<1/8\).

## Assumptions and scope
The graph is connected for \(n\ge3\), all edges have length one, the metric is the graph shortest-path distance, and functions are real valued. All \(2n\) probabilities are strictly positive and sum to one. The Lipschitz seminorm is \(\max_{A_iB_j\in E}|f(A_i)-f(B_j)|\); the centered embedding is \(f\mapsto f-\int f\,d\mu\). Variance means \(\int|f-\int f\,d\mu|^2\,d\mu\), without unnormalized counting factors. The NP-completeness statement uses the compact list of rational masses, not a graph expanded to exponential size.

## Proof
**Strict convexity and tight edges.** Modulo constants the unit Lipschitz ball is a compact polytope. Since every mass is positive, the variance is a strictly convex quadratic form on the quotient. Thus every maximizing potential must be a vertex. For an anchored feasible potential \(f\), let its *tight-edge graph* consist of the edges \(uv\) with \(|f(u)-f(v)|=1\). If it is disconnected, shift one nonempty proper tight component by \(+t\) or \(-t\) for sufficiently small \(t>0\). Both perturbations remain feasible; the average of their variances strictly exceeds \(\operatorname{Var}_\mu(f)\) because the positive-mass indicator of that component has nonzero variance. Hence every maximizer has connected tight-edge graph. Along a tight spanning tree all increments equal \(\pm1\), so every potential difference is integral. After translating the minimum to zero, the graph diameter three restricts values to \(\{0,1,2,3\}\).

**Range three.** The minimum and maximum can have difference three only at an omitted pair \(A_i,B_i\). Set \(f(A_i)=0\), \(f(B_i)=3\). For every \(j\ne i\), the edges incident with the exceptional pair force \(f(A_j)\ge2\) and \(f(B_j)\le1\). For any \(j\ne i\), choose \(k\notin\{i,j\}\) (possible since \(n\ge3\)); the edge \(A_jB_k\) then forces \(f(A_j)=2\) and \(f(B_k)=1\). Thus the entire potential is of type 3, or its negative up to translation. Center its values by subtracting \(3/2\): ordinary pairs have values \((1/2,-1/2)\) and the exceptional pair has \((-3/2,3/2)\). The second moment equals \(1/4+2(a_i+b_i)\); the mean equals \(\alpha-1/2+2(b_i-a_i)\). Hence its variance is \(E_i\).

**Range two.** After translating, take only labels \(0,1,2\). If an omitted pair has a gap of two, after sign reversal suppose \(f(A_i)=0\), \(f(B_i)=2\). For all \(j\ne i\) one has \(f(A_j)\in\{1,2\}\) and \(f(B_j)\in\{0,1\}\). Let \(J=\{j\ne i:f(A_j)=2\}\) and \(K=\{j\ne i:f(B_j)=0\}\). The edge \(A_jB_k\) prohibits distinct \(j\in J\) and \(k\in K\); therefore either \(J\) or \(K\) is empty, or \(J=K=\{h\}\). If \(K\) is empty, the tight edges incident with \(B_i\) meet only the \(A_j\)'s labeled one, while those vertices have no tight edges to the other \(B\)'s; \(B_i\)'s tight component is separated from \(A_i\)'s. The case \(J\) empty is symmetric. In the remaining double-exception case, every vertex outside the two exceptional pairs has label one, and tight edges separate into the two noncommunicating sets \(\{A_i,A_h,B_k:k\notin\{i,h\}\}\) and \(\{B_i,B_h,A_k:k\notin\{i,h\}\}\). None can be a vertex. Thus a maximizing range-two potential has no omitted pair with gap two.

Its zero and two labels cannot occur on opposite sides (an actual edge would have gap two, and omitted pairs were just excluded). Accordingly both occur on one side, and every vertex on the other side has value one. Any value one on the varying side has no tight incident edge and prevents tight connectivity. Hence all values there are zero or two; after subtracting one these are precisely the sign configurations of types 1 and 2. Their variances are respectively \(\alpha-(\sum_i a_i\varepsilon_i)^2\) and \(\beta-(\sum_i b_i\varepsilon_i)^2\), giving the two discrepancy terms.

**Range at most one.** If the values are zero and one, tight edges connect only opposite-colored classes. If both kinds of opposite-colored cross pairs occur, their tight subgraphs cannot communicate; if one kind is absent, any vertex not belonging to the other kind is isolated in the tight graph. Connectedness therefore forces all vertices on each side to be constant with opposite values. This is already covered by constant-sign members of types 1 and 2. Constant potentials cannot maximize since the graph has edges and all masses are positive. The three displayed types are feasible, with connected tight graphs, and they exhaust all maximizers. The maximum of their exact variances proves the main formula and equality classification.

**Pair symmetry and complexity.** Under \(a_i=b_i=q_i/2\), direct substitution gives the two-branch expression and the boundary \(8\max_iq_i+D^2=1\). For the promised rational symmetric case with \(\max_iq_i<1/8\), the exceptional-pair term is strictly below \(1/2\); the discrepancy term reaches \(1/2\) exactly when a perfect equal-sum partition of the \(q_i\)'s exists. Given a positive-integer PARTITION instance \(w_1,\ldots,w_m\) of total \(S\), put \(H=S+1\) and append sixteen copies of \(H\). Normalize all weights by \(T=S+16H\) to obtain the \(q_i\)'s. Every \(q_i\le H/T<1/16<1/8\). Any balanced signing of the padded list must assign eight copies of \(H\) to each sign, since an imbalance in their count contributes at least \(H>S\), which cannot be compensated by the original numbers. Thus the padded instance partitions exactly when the original does, proving NP-hardness. Membership in NP follows from a length-\(2n\) integer Lipschitz potential as a polynomially checkable certificate for variance at least \(1/2\), or from a balanced sign vector under the promise. This establishes the stated compact-input NP-completeness. \(\square\)

## Verification
The standalone standard-library program `verify_weighted_crown.py` enumerates all integral, min-normalized feasible potentials taking values in \(\{0,1,2,3\}\) for \(n=3,4,5\). For twelve symmetric and asymmetric rational-mass examples it computes exact rational variances independently of the candidate formula, compares maxima, and verifies every maximizing profile belongs to the predicted families. The admissible potential counts are \(141\), \(495\), and \(1723\), respectively. Running `python3 verify_weighted_crown.py` prints `ALL_ARBITRARY_WEIGHTED_CROWN_CHECKS_OK`. These finite checks are diagnostic; the proof above establishes the universal assertion.

## Relationship to prior work
Graph spread and an integer-maximizer principle occur in Addario-Berry, Janson and McDiarmid's 2009 preprint (citing Alon, Boppana and Spencer). Chen, Davis and Korchevskaia's facet-subgraph theorem describes symmetric edge-polytopal faces in arbitrary graphs. A published crown-graph symmetric-edge-polytope result determines the **uniform Euclidean** inradius and tangent-facet threshold at eight; by polarity, that already covers the **uniform-measure** instance of the present norm. None of those inspected statements provides the arbitrary-positive-measure norm, its two independent weighted subset-discrepancy terms, its exceptional-pair imbalance correction, or the compact weighted-input NP-completeness assertion. The tight-edge classification is a structural tool, not independently claimed as new. A general all-facets description can reduce the remaining computation to finite candidates, so an equivalent weighted optimization or an unindexed treatment remains a substantive originality risk.

## Limitations
The probability weights must be strictly positive; zero masses require separately removing degeneracies. Only crown graphs, real scalars, unit edge lengths, and quadratic \(L^2\) variance are covered. The exact expression contains subset-partition optimizations, which are not asserted to admit a polynomial-time exact algorithm for binary-encoded rational weights. NP-completeness concerns compact weight data, not an exponentially expanded graph, and does not assert strong NP-hardness. Independent mathematical assessment is not performed.

## References
1. L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, first public arXiv version 2009-02-06, arXiv:0902.1156, https://arxiv.org/abs/0902.1156.
2. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, https://arxiv.org/abs/2107.12315.
3. *A sharp Euclidean inradius and tangent-facet transition for crown-graph symmetric edge polytopes*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-euclidean-inradius-and-tangent-facet-transition-for-crow--2cd222e2d952.
4. M. Garey, D. Johnson, *Computers and Intractability*, 1979, the NP-completeness of PARTITION.
