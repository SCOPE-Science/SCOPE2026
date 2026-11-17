# Exact variation-norm mass design for two-color conditional expectations on weighted paths

## Finding
Let \(n\ge2\) be an integer. Partition the vertices \(1,\ldots,n\), in their path order, into two nonempty color classes \(A\) and \(B\). Let \(\mu_i>0\) be vertex masses and \(w_k>0\), \(1\le k<n\), be independently prescribed edge-variation weights. The conditional expectation \(P_\mu\) replaces a real signal at every vertex by the \(\mu\)-weighted average of the vertices of its color. Put
\[
V_w(f)=\sum_{k=1}^{n-1}w_k|f_{k+1}-f_k|,
\quad M_A=\sum_{i\in A}\mu_i,\quad M_B=\sum_{i\in B}\mu_i.
\]
Define the signed normalized prefix imbalance
\[
S_k=\frac{\sum_{i\le k,\ i\in A}\mu_i}{M_A}
 -\frac{\sum_{i\le k,\ i\in B}\mu_i}{M_B},\qquad 0\le k\le n.
\]
Let \(J=\{k:1\le k<n,\ \text{colors at }k\text{ and }k+1\text{ differ}\}\), \(r=|J|\ge1\), \(W=\sum_{k\in J}w_k\), and \(w_*=\min_{1\le k<n}w_k\).

**Exact fixed-mass norm and extremizers.** For every choice of strictly positive masses,
\[
\boxed{K(\mu;w)=\sup_{V_w(f)>0}\frac{V_w(P_\mu f)}{V_w(f)}
 =W\max_{1\le k<n}\frac{|S_k|}{w_k}.}
\]
A single-jump vector \(f_i=\mathbf1_{\{i>k\}}\), with \(k\) maximizing the displayed ratio, attains the norm. Since the projection is linear, the same constant is its exact two-input variation Lipschitz factor.

**Complete mass-design law.** For *every* fixed two-color word and every strictly positive edge-weight profile, there are strictly positive vertex masses for which \(K=1\). The exact range when vertex masses vary over all positive choices is
\[
\boxed{\{K(\mu;w):\mu_i>0\}=
\begin{cases}
\{1\},&W=w_*,\\
[1,W/w_*),&W>w_*.
\end{cases}}
\]
Thus the optimal value is always one, the sharp worst-design supremum is \(W/w_*\), and the upper endpoint is unattained unless it is equal to one.

**Every contractive design.** Enumerate the consecutive monochromatic runs \(R_0,\ldots,R_r\). Let \(t_j\) be the edge between runs \(R_j\) and \(R_{j+1}\), and put \(b_j=w_{t_j}\). The norm equals one if and only if both conditions hold:

1. The fraction of the total mass of each run's own color assigned to that run equals \(b_0/W\) for \(R_0\), \((b_{j-1}+b_j)/W\) for every internal \(R_j\), and \(b_{r-1}/W\) for \(R_r\).
2. At every edge \(k\notin J\) strictly within a run, its realized prefix imbalance satisfies \(|S_k|\le w_k/W\).

The first condition alone forces the exact signed values at transition edges. When all edge weights are equal, the second condition follows automatically from the first. In that case, the exact stability-one run fractions are \(1/r,2/r,\ldots,2/r,1/r\) relative to the two respective color totals. For equal vertex masses, this yields precisely the alternating run-length pattern \(a,2a,\ldots,2a,a\) for some positive integer \(a\). In particular, nonconsecutive color classes can still yield a total-variation contraction.

## Assumptions and scope
The path has \(n\ge2\) vertices; both classes are nonempty. The independent edge weights and vertex masses are real and strictly positive. Signals are arbitrary real vectors. The total variation seminorm is measured on the path, **without a closing edge**, and is applied to both input and output. Separate normalization within the two color classes is essential; no monotonicity or regularity of the masses or color word is assumed. The statement concerns exactly two classes, not arbitrary multiclass partitions or cycles.

## Proof
**1. Norm formula and attainment.** Define \(\alpha_i=\mu_i/M_A\) for \(i\in A\) and \(\alpha_i=-\mu_i/M_B\) for \(i\in B\). Since \(\sum_i\alpha_i=0\), writing \(S_k=\sum_{i\le k}\alpha_i\), discrete summation by parts gives
\[
\sum_{i=1}^n\alpha_i f_i=-\sum_{k=1}^{n-1}S_k(f_{k+1}-f_k).
\]
The output has exactly \(r\) candidate color-transition edges and constant values elsewhere. Therefore
\[
V_w(P_\mu f)=W\left|\sum_i\alpha_i f_i\right|
\le W\left(\max_{k<n}\frac{|S_k|}{w_k}\right)V_w(f).
\]
For the tail step \(f_i=\mathbf1_{\{i>k\}}\), the input variation is \(w_k\) and \(\sum_i\alpha_i f_i=-S_k\). Choosing a maximizer proves equality. No finite sampling assumption enters this operator-norm identity.

**2. Why the norm cannot be below one.** The map \(P_\mu\) is an idempotent projection which fixes the nonconstant two-valued indicator \(\mathbf1_A\). Consequently \(V_w(P_\mu\mathbf1_A)=V_w(\mathbf1_A)>0\), so \(K\ge1\).

**3. Exact rigidity of mass designs.** For any \(\mu\), the norm formula gives \(|S_k|\le K w_k/W\). At an edge \(t_j\in J\), consider \(\mathbf1_A\). The identity in step 1 and \(\sum_i\alpha_i\mathbf1_A(i)=1\) imply
\[
1=-\sum_{j=0}^{r-1}S_{t_j}
\bigl(\mathbf1_A(t_j+1)-\mathbf1_A(t_j)\bigr).
\]
If \(K=1\), every summand is at most \(b_j/W\), and their sum is \(\sum_jb_j/W=1\). Equality therefore holds term by term: \(S_{t_j}=b_j/W\) if run \(R_j\) has color \(A\), and \(S_{t_j}=-b_j/W\) if that run has color \(B\). Subtracting adjacent transition values forces the listed run fractions: \(b_0/W\) at the first run, \((b_{j-1}+b_j)/W\) in each interior run, and \(b_{r-1}/W\) at the last. Conversely, these fractions force the transition imbalances, and the stated internal-edge inequalities give \(K\le1\); step 2 gives equality. This proves the complete equivalence.

**4. Positive mass designs exist for *all* edge weights.** Normalize each of the two color-class totals to one. The required run fractions in step 3 sum to one within each color, because each transition weight \(b_j\) contributes exactly once to the total normalized mass of the run of either color bordering that edge. Set \(\varepsilon=w_*/(10nW)\). In the first run, allocate \(\varepsilon\) to every vertex except the final one, which receives the remaining run fraction. In the final run, put the remaining fraction on its first vertex and \(\varepsilon\) on all later vertices. For an interior run of length at least two, allocate \(b_{j-1}/W\) to its first vertex, \(\varepsilon\) to all vertices strictly between the first and last, and \(b_j/W-(|R_j|-2)\varepsilon\) to its last vertex. A singleton interior run receives its full prescribed fraction. Every mass is positive because all transition weights are at least \(w_*\), while at most \(n\varepsilon<w_*/W\) is subtracted. The prefix sums at transitions have exactly the required alternating values, and at every internal edge their magnitudes are less than \(n\varepsilon<w_*/W\le w_k/W\). Hence the constructed masses satisfy both conditions of step 3 and give \(K=1\).

**5. Sharp upper design envelope and complete range.** For every internal cut \(k\), its two normalized class fractions both lie between zero and one, so \(|S_k|\le1\). Thus \(K\le W/w_*\). Equality \(|S_k|=1\) requires all vertices of one color on one side of the cut and all vertices of the other color on the other side; strict positivity makes this equivalent to a two-run color word with its sole transition at \(k\). Hence when \(W>w_*\), no cut of minimum edge weight can have \(|S_k|=1\), and every positive-mass design has \(K<W/w_*\). Choose a minimum-weight cut \(k_*\); some opposite-colored vertices lie on opposite sides of that cut (otherwise both colors could not be present). Give these two vertices a common mass tending to infinity while all others retain unit mass. Their respective normalized class totals are dominated by the chosen vertices, so \(|S_{k_*}|\to1\), proving the supremum equals \(W/w_*\). The map from the connected positive mass cone to \(K\) is continuous, the value one is attained by step 4, and the upper bound is approached but not attained. Its entire image is therefore \([1,W/w_*)\). If \(W=w_*\), the lower bound of step 2 and upper bound just proved coincide, so \(K\equiv1\). This proves the claimed spectrum in every case.

## Verification
The embedded `check.py` reproduces exact rational identities, including direct independent single-step calculations for 2,026 pairs of color words and weighted mass/edge profiles, constructive norm-one mass designs for every tested case, and minimum-weight cut witnesses approaching the sharp unattained upper envelope. Every binary word of length 2 through 10 beginning with its first color is tested with two positive edge profiles, and the random profiles are reproducibly seeded. The checker uses only Python's standard library and prints `ALL_WEIGHTED_PATH_TWO_COLOR_CHECKS_PASS` on success. These finite computations check the formulas and construction; steps 1–5 prove the theorem for all lengths and real positive parameters.

For a concrete example with unit edge and vertex weights and four color runs of lengths \(1,2,2,1\), the weighted conditional expectation has sharp variation factor one despite its two classes being interlaced. The same word under arbitrary positive edge weights admits a different positive mass design that again achieves factor one.

## Relationship to prior work
Nochetto–Salgado's 2012 continuous finite-element construction produces a total-variation-diminishing *local interpolation* operator; its Theorem 3.7 and nonperiodic Section 4 do not classify weighted conditional expectations on nonconsecutive two-class path partitions. Gaubert–Qu's 2013 operator theory gives sharp contraction coefficients for *oscillation* and the dual measure-total-variation norm, not for total variation formed from neighboring **signal differences**. A publicly available cyclic two-cell conditional-expectation theorem provides a related signed-prefix argument, but the present edge-weighted path formula, endpoint/interior run-mass design, arbitrary-weight contractivity construction, and complete \(W/w_*\) attainable range do not follow from that theorem's stated unweighted-cycle result. A prior finite-path result on the maximal unweighted two-class norm across all partitions addresses a different extremal question and does not give the fixed-partition independently weighted mass-design theorem. The elementary facts that positive conditional expectations preserve constants and reduce ordinary oscillation are not asserted as new. Priority uncertainty remains for unindexed specialized weighted-path projection results.

## Limitations
This is an exact finite-dimensional real theorem for exactly two output classes, positive vertex masses, and strictly positive edge weights; it does not classify three or more classes, arbitrary graphs with cycles, nor continuum conditional expectations. The supremum \(W/w_*\) is nonattained whenever it exceeds one; in particular, it must not be presented as a positive-mass equality case. The exact range is over **varying vertex masses** with the color word and edge weights held fixed, not over varying color words or varying edge weights. The diagnostic check is finite. Independent validation has not been performed.

## References
1. R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, arXiv:1211.1069v1, first posted 2012-11-05, https://arxiv.org/abs/1211.1069. Section 3, Theorem 3.7, and Section 4.
2. S. Gaubert and Z. Qu, *Dobrushin's Ergodicity Coefficient for Markov Operators on Cones*, arXiv:1307.4649v1, first posted 2013-07-17, https://arxiv.org/abs/1307.4649. Introduction and Theorem 1.1.
3. *Sharp cyclic-variation stability of two-cell conditional expectations*, publicly accessible mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-cyclic-variation-stability-of-two-cell-conditional-expecta--19779f163091. Full proof and the cyclic run-mass theorem.
