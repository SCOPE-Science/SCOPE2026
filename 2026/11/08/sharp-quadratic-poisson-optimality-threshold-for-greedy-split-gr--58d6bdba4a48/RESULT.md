# Sharp quadratic Poisson optimality threshold for greedy split-graph matchings

## Finding

Let \(a\ge 2\), \(b\ge a\), and let \(G_{a,b}=K_a\vee\overline K_b\) be a labeled complete split graph. Repeatedly choose a uniformly random currently feasible edge, add it to a matching, and delete its endpoints. Write \(M_{a,b}\) for the final matching, and \(D_{a,b}=a-|M_{a,b}|\) for its additive deficit from the maximum matching size \(a\). Let \(U_{a,b}\) be the uniform law on the maximum matchings, each of which is a cross-part injection.

**Exact finite law.** The probability of optimality and the total variation distance of the *entire matching laws* are
\[
\Pr(D_{a,b}=0)=\prod_{x=1}^a\frac{2(b-a+x)}{2(b-a+x)+x-1},\qquad
 d_{\rm TV}(\mathcal L(M_{a,b}),U_{a,b})=1-\Pr(D_{a,b}=0).
\]
The conditional law of \(M_{a,b}\) given \(D_{a,b}=0\) is exactly \(U_{a,b}\). The deficit counts precisely the number of clique-internal edges selected.

**Explicit Poisson approximation.** For every \(b\ge4a\), with \(\lambda_{a,b}=a(a-1)/(4b)\),
\[
 d_{\rm TV}\bigl(\mathcal L(D_{a,b}),\operatorname{Pois}(\lambda_{a,b})\bigr)
 \le \frac{a(a-1)(14a-5)}{24b^2}\le \frac{7a^3}{12b^2}.
\]
Consequently, if \(a\to\infty\) and \(a^2/b\to\theta\in[0,\infty)\), then \(D_{a,b}\) converges in total variation to \(\operatorname{Pois}(\theta/4)\), and \(\Pr(D_{a,b}=0)\to e^{-\theta/4}\). More generally, for all sequences \(b\ge a\), the exact-optimality probability tends to \(1\) when \(b/a^2\to\infty\), to \(e^{-1/(4c)}\) when \(b/a^2\to c\in(0,\infty)\), and to \(0\) when \(b/a^2\to0\). Thus \(b\asymp a^2\) is the sharp transition for exact maximum matching and for approximation of the entire matching law by uniform injections.

## Assumptions and scope

All graph edges have unit weight. At each step the choice is uniform **among feasible edges**, not uniform among vertices. The process stops when no edge remains. The two graph parts are labeled, and \(a,b\) are integers with \(2\le a\le b\). The total variation convention is \(d_{\rm TV}(P,Q)=\sup_E|P(E)-Q(E)|\). Poisson variables are supported on nonnegative integers. The asymptotic statements require \(a\to\infty\) and use no unstated relationship between the two part sizes beyond those specified.

## Proof

**1. Exact state recursion and deficit identity.** Suppose \(x\) clique vertices and \(y\) independent-set vertices remain. Of the \(\binom{x}{2}+xy\) feasible edges, \(\binom{x}{2}\) are internal and \(xy\) are cross-part edges. An internal choice removes two clique vertices, whereas a cross choice removes one vertex from each part. Because \(b\ge a\), while \(x>0\) a cross edge exists: after \(k\) internal selections, the number of cross selections is \(a-x-2k\), and therefore \(y=b-a+x+2k\ge x\). At termination all clique vertices have been removed, so with \(k\) internal selections the matching has \(k+(a-2k)=a-k\) edges. Hence \(D_{a,b}=k\), and the maximum matching size is \(a\).

**2. The optimality product and full-law distance.** If no internal edge is ever selected, the process visits clique sizes \(a,a-1,\dots,1\), with independent-set size \(b-a+x\) at size \(x\). The conditional probability of a cross edge is
\[
 \frac{2(b-a+x)}{2(b-a+x)+x-1}.
\]
Multiplying proves the product. All full cross-part injections are equally likely conditional on this event, by exchangeability of the vertex labels under every cross choice. Every maximum matching is an injection, and any matching containing an internal edge is nonmaximum. Therefore if \(p\) is the displayed product, \(\mathcal L(M_{a,b})=pU_{a,b}+(1-p)R\), where \(R\) is supported on matchings disjoint from the support of \(U_{a,b}\). This proves the asserted exact total variation distance.

**3. Explicit coupling to rare independent Bernoulli choices.** Index states by remaining clique count \(x\), and let \(k\) be the number of previous internal selections. At a visited state \(x\) the internal-edge probability is
\[
 p_{x,k}=\frac{x-1}{D_{x,k}},\qquad D_{x,k}=2b-2a+3x+4k-1,
\]
with \(0\le k\le(a-x)/2\). An internal choice jumps from \(x\) to \(x-2\), whereas a cross choice moves to \(x-1\). Construct this process using independent uniforms \(V_1,\ldots,V_a\): at visited \(x\), select an internal edge exactly when \(V_x\le p_{x,k}\). Independently of the labels of subsequent chosen endpoints, this reproduces the part-count law. In the same probability space define independent \(Y_x=\mathbf 1\{V_x\le q_x\}\), where \(q_x=(x-1)/(2b)\), and let \(S=\sum_{x=1}^aY_x\).

If \(b\ge4a\), the state constraint gives
\[
 D_{x,k}\ge\tfrac32 b,\qquad |D_{x,k}-2b|\le2a,\qquad
 |p_{x,k}-q_x|\le\frac{2a(x-1)}{3b^2}.
\]
The total probability of a disagreement at *visited* states is at most \(a^2(a-1)/(3b^2)\). A skipped state \(x\) is skipped exactly because an internal edge was selected at \(x+1\). Since the unused uniform \(V_x\) is independent of preceding choices, the expected number of Bernoulli successes at skipped states is at most
\[
 (\max_x q_x)\,\mathbb E D_{a,b}
 \le \frac{a-1}{2b}\frac{a(a-1)}{3b}
 =\frac{a(a-1)^2}{6b^2}.
\]
Here the expected number of internal selections is at most \(\sum_{x=1}^a(x-1)/(3b)=a(a-1)/(3b)\). Thus a coupling yields
\[
 d_{\rm TV}(\mathcal L(D_{a,b}),\mathcal L(S))
 \le\frac{a^2(a-1)}{3b^2}+\frac{a(a-1)^2}{6b^2}.
\]
The standard independent-Bernoulli/Poisson coupling (or Le Cam's bound) gives
\[
 d_{\rm TV}(\mathcal L(S),\operatorname{Pois}(\sum_xq_x))
 \le\sum_xq_x^2=\frac{a(a-1)(2a-1)}{24b^2},
 \qquad\sum_xq_x=\frac{a(a-1)}{4b}.
\]
The triangle inequality gives exactly \(a(a-1)(14a-5)/(24b^2)\) as claimed.

**4. Sharp optimality threshold.** Along the all-cross trajectory write \(r_x=(x-1)/(2b-2a+3x-1)\), so \(\Pr(D_{a,b}=0)=\prod_x(1-r_x)\). Since the denominator is at most \(2b+a\), \(\sum_xr_x\ge a(a-1)/(2(2b+a))\), which diverges whenever \(b=o(a^2)\), proving the limit zero. If \(b/a^2\to\infty\), \(\sum_xr_x\to0\), so the product tends to one. If \(b/a^2\to c>0\), uniform approximation gives \(\sum_xr_x\to1/(4c)\) and \(\sum_xr_x^2\to0\), giving the intermediate limit. The Poisson bound proves total-variation convergence whenever \(a^2/b\) has a finite limit, including zero.

## Verification

Run `python3 verify.py` in an environment with the Python 3 standard library. The checker independently enumerates labeled feasible-edge choices, compares them with the reduced exact rational transition recursion, checks the exact product on small cases, verifies all finite inequalities entering the coupling, and compares computable finite distributions to the explicit Poisson bound. Its reference output is `VERIFY_OK 11717 assertions`. This is finite corroboration; the preceding argument establishes the all-parameter assertions and limits.

## Relationship to prior work

Uniform feasible-edge greedy matching is classical; it is called RANDOM-EDGE by Arnosti (2021) and was studied by Dyer and Frieze (1991). Arnosti proves average-case comparisons of matching algorithms on *random bipartite input graphs*, not a complete split graph containing clique-internal edges. Dyer, Frieze and Pittel (1993) develop asymptotic normal laws for greedy matching on sparse random graphs and random labeled trees, not the fixed complete split family. The present claim concerns the **additive** exact-optimality deficit and the **whole output law**, rather than a multiplicative approximation guarantee or the total matching count in a sparse random input. The Poisson coupling and its explicit error estimate are elementary and are not claimed as a new general approximation principle.

## Limitations

The theorem does not address \(b<a\), nonuniform edge weights, vertex-first selection algorithms, or the behavior of the deficit when \(a^2/b\to\infty\) beyond the exact-optimality probability tending to zero. The finite bound is useful in the high-imbalance regime \(b\ge4a\) and is not claimed optimal in constants. The general random-greedy method and the independent-Bernoulli Poisson inequality are prior tools. Historical priority regarding the precise split-graph formulas cannot be absolutely excluded without a complete survey of older literature; the 1991 Dyer–Frieze full text was not available for complete inspection.

## References

1. N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, Stochastic Systems 12 (2022), 133–150; earliest public online date 2021-11-02. DOI: https://doi.org/10.1287/stsy.2021.0082.
2. M. Dyer and A. Frieze, *Randomized Greedy Matching*, Random Structures & Algorithms 2 (1991), 29–45. DOI: https://doi.org/10.1002/rsa.3240020104.
3. M. Dyer, A. Frieze and B. Pittel, *The Average Performance of the Greedy Matching Algorithm*, Annals of Applied Probability 3 (1993), 526–552. DOI: https://doi.org/10.1214/aoap/1177005436.
4. D. Bal and P. Bennett, *The Matching Process and Independent Process in Random Regular Graphs and Hypergraphs*, Electronic Journal of Combinatorics 30 (2023), P1.11; preprint https://arxiv.org/abs/1603.09232.
