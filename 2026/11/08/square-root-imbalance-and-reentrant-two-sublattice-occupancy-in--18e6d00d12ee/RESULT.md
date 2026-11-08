# Square-root imbalance and reentrant two-sublattice occupancy in a Widom–Rowlinson gas

## Finding
Consider the two-species Widom–Rowlinson model on the complete bipartite graph \(K_{a,b}\). Each vertex is vacant, occupied by species A, or occupied by species B; unlike occupied species cannot occur at the ends of an edge. An allowed configuration with \(N\) occupied sites has grand-canonical weight \(z^N\), where \(z>0\) is the common species activity.

For fixed \(\kappa\ge0\) and \(c>0\), set
\[
a_n=n,\qquad b_n=n-\lfloor\kappa\sqrt n\rfloor,\qquad z_n=c/\sqrt n,
\]
for every sufficiently large integer \(n\) for which \(b_n\ge1\). Let \(E_L\) be the event that the left part is occupied but the right part is empty, \(E_R\) its reverse, and \(E_B\) the event that both parts contain occupied vertices. Then
\[
\lim_{n\to\infty}\bigl(\Pr(E_L),\Pr(E_R),\Pr(E_B)\bigr)
=\frac{\bigl(e^{-2c^2},e^{-2c^2-2\kappa c},2e^{-c^2-\kappa c}\bigr)}
{e^{-2c^2}+e^{-2c^2-2\kappa c}+2e^{-c^2-\kappa c}}.
\]
The omitted probability of the fully vacant configuration tends to zero. In particular,
\[
P_\kappa(c):=\lim_{n\to\infty}\Pr(E_B)
=\frac{1}{1+e^{-c^2}\cosh(\kappa c)}.
\]
**Sharp reentrance criterion.** If \(0\le\kappa\le\sqrt2\), \(P_\kappa(c)\) increases strictly on \(c>0\). If \(\kappa>\sqrt2\), it first decreases and then increases, attaining its unique minimum at the positive solution \(c_*\) of
\[
\kappa\tanh(\kappa c_*)=2c_*.
\]
Consequently, for each fixed \(\kappa>\sqrt2\), the *finite* graph probability that both parts are occupied is nonmonotone as a function of activity for all sufficiently large \(n\). This is reentrance of a finite-volume occupancy event, **not** a claim of multiple infinite-volume Gibbs phases.

There is also a three-atom limit for the two part occupation counts \(X_L,X_R\): the random vector \((X_L/\sqrt n,X_R/\sqrt n)\) converges in distribution to \((2c,0)\), \((0,2c)\), or \((c,c)\) with the respective probabilities above. Hence the total normalized occupation tends to \(2c\) in all three classes even though the partwise imbalance distinguishes them.

## Assumptions and scope
All graph vertices have independent allowed choices subject solely to the forbidden A–B adjacency constraint. The graph is exactly \(K_{a,b}\), no within-part edges, with one fugacity \(z\) for either species and vacancy weight one. The limiting parameter \(\kappa\) is fixed and nonnegative; \(c\) is fixed and strictly positive. The threshold describes monotonicity of the *limiting scaling function*, not finite-size monotonicity below threshold. Empty-side events are disjoint as defined above, with the all-empty state treated separately.

## Proof
Write \(W_0,W_L,W_R,W_B\) for the weights of the fully empty state, of nonempty occupation restricted to the left part, restricted to the right part, and occupying both parts. Since every left vertex is adjacent to every right vertex, a state in the last class must use the same single species on both parts. Thus for all positive integers \(a,b\) and real \(z>0\),
\[
W_0=1,\quad W_L=(1+2z)^a-1,\quad W_R=(1+2z)^b-1,\quad
W_B=2\bigl((1+z)^a-1\bigr)\bigl((1+z)^b-1\bigr).
\]
Their sum \(Z_{a,b}(z)\) is the exact finite partition function. No state is counted twice: the four classes are disjoint and exhaustive.

For \(z_n=c/\sqrt n\), the logarithmic expansions, with remainders vanishing at fixed \(c,\kappa\), are
\[
\begin{aligned}
 n\log(1+2z_n)&=2c\sqrt n-2c^2+o(1),\\
 b_n\log(1+2z_n)&=2c\sqrt n-2c^2-2\kappa c+o(1),\\
 (a_n+b_n)\log(1+z_n)&=2c\sqrt n-c^2-\kappa c+o(1).
\end{aligned}
\]
Because \(c>0\) and \(a_n,b_n\sim n\), each factor \((1+z_n)^{a_n}\), \((1+z_n)^{b_n}\), \((1+2z_n)^{a_n}\), \((1+2z_n)^{b_n}\) diverges. Accordingly, the subtracted ones are asymptotically negligible. Dividing each \(W\) by \(e^{2c\sqrt n}\) yields, in order, \(0,e^{-2c^2},e^{-2c^2-2\kappa c},2e^{-c^2-\kappa c}\). Dividing by their strictly positive sum establishes the class-weight limits and, after factoring \(2e^{-c^2-\kappa c}\), the stated formula for \(P_\kappa\).

For the count limit, conditional on \(E_L\), occupations in the left part follow independent three-state Bernoulli-weighted choices, conditioned on at least one occupied vertex. The unconditioned occupation count is binomial with parameter \(2z_n/(1+2z_n)\), has mean \(2c\sqrt n+O(1)\) and variance \(O(\sqrt n)\), and the probability of no occupation is exponentially small in \(\sqrt n\). Thus \((X_L/\sqrt n,X_R/\sqrt n)\to(2c,0)\) in probability conditionally. The right-only class is symmetric. Conditional on \(E_B\), choose the common species in two ways; occupancy in each part is independent with parameter \(z_n/(1+z_n)\), then conditioned on both parts nonempty. Again the conditioning events have probability tending to one, the means are \(c\sqrt n+O(1)\), and the variances are \(O(\sqrt n)\). Therefore the conditional limit is \((c,c)\). The law of total probability proves the three-atom weak limit.

Set \(Q_\kappa(c)=e^{-c^2}\cosh(\kappa c)\). Because \(P_\kappa=(1+Q_\kappa)^{-1}\), the sign of \(P_\kappa'\) is opposite to that of
\[
\frac{Q_\kappa'(c)}{Q_\kappa(c)}=-2c+\kappa\tanh(\kappa c).
\]
For \(0\le\kappa\le\sqrt2\) and \(c>0\), \(\tanh t<t\) for \(t>0\) makes this quantity strictly negative. For \(\kappa>\sqrt2\), it is positive for sufficiently small positive \(c\) and negative for sufficiently large \(c\). The function \(t\mapsto\tanh(t)/t\) is strictly decreasing on \(t>0\): its derivative has numerator \(t\operatorname{sech}^2(t)-\tanh(t)<0\), since \(\sinh(t)\cosh(t)>t\). Therefore there is exactly one positive zero, giving a unique minimum of \(P_\kappa\). Finally choose three fixed positive values \(c_1<c_2<c_3\) with \(P_\kappa(c_1)>P_\kappa(c_2)<P_\kappa(c_3)\). Pointwise finite-size convergence at those values makes the same strict inequalities true for all sufficiently large \(n\), showing finite-size nonmonotonicity without claiming an exact finite-size extremum location.

## Verification
The standalone `verify.py` independently enumerates all three-state configurations for each \(1\le a,b\le4\) at four rational activities, checking every disjoint class against the partition-function formula (64 exact comparisons). It separately checks 60 logarithmically stabilized finite-size probabilities against the limiting weights, and scans the predicted monotonicity boundary for seven representative imbalance parameters. Run with `python3 verify.py` using the standard Python library. All checks passed. These finite tests corroborate but do not replace the analytic proof above.

## Relationship to prior work
The underlying two-species Widom–Rowlinson model and its graph-homomorphism encoding are established. Lebowitz, Mazel, Nielaba and Šamaj investigate crystalline and demixed phases on square and Bethe lattices. Brightwell, Häggström and Winkler describe nonmonotone *Gibbs-measure symmetry breaking* on modified trees. Krčmár and Šamaj study reentrance on Bethe and square lattices after relaxing unlike-species exclusion. Cohen, Perkins and Tetali prove extremal occupancy bounds over regular graphs. A published general graph-to-partition-function correspondence also subsumes finite fugacity counts in principle. None of the examined available material states the present double-square-root scaling, explicit three-atom side-occupancy limit, or sharp geometric threshold \(\kappa=\sqrt2\). The exact four-class partition identity alone is not claimed as new; the claimed contribution is the derived scaling and reentrant threshold for this infinite graph family.

## Limitations
The graph degree grows with \(n\), and activity tends to zero as \(n^{-1/2}\); the model does not represent a bounded-degree thermodynamic limit or establish multiple infinite-volume Gibbs measures. The pointwise limit at fixed \(c>0\) does not imply uniform control when \(c\to0\) or \(c\to\infty\) jointly with \(n\). A general partition representation in earlier literature permits the finite graph count, and hidden or inaccessible prior asymptotic applications could subsume the novelty claim. Full text of the 1999 nonmonotonic tree paper was not successfully extracted from its accessible PostScript link.

## References
- J. L. Lebowitz, A. Mazel, P. Nielaba, and L. Šamaj, “Ordering and demixing transitions in multicomponent Widom–Rowlinson models,” *Physical Review E* **52** (1995), 5985. https://doi.org/10.1103/PhysRevE.52.5985 ; full-text version https://arxiv.org/abs/cond-mat/9707009.
- G. R. Brightwell, O. Häggström, and P. Winkler, “Nonmonotonic behavior in hard-core and Widom–Rowlinson models,” *Journal of Statistical Physics* **94** (1999), 415–435. Author's bibliography https://math.dartmouth.edu/~pw/papers/pubs.html.
- E. Cohen, W. Perkins, and P. Tetali, “On the Widom–Rowlinson occupancy fraction in regular graphs,” arXiv first public December 20, 2015. https://arxiv.org/abs/1512.06398.
- R. Krčmár and L. Šamaj, “Reentrant disorder–disorder transitions in generalized multicomponent Widom–Rowlinson models,” *Physical Review E* **92** (2015), 052103. https://doi.org/10.1103/PhysRevE.92.052103 ; full text https://arxiv.org/abs/1601.00515.
- E. Cohen, P. Csikvári, W. Perkins, and P. Tetali, “The Widom–Rowlinson model, the hard-core model and the extremality of the complete graph,” https://tetali.math.gatech.edu/PUBLIS/WidomRowlinson-CCPT.pdf.
