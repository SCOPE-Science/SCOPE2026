# A thirteen-vertex reversal in rare-leaf odds for leaf-driven preferential attachment

## Finding

Start from a single undirected edge, grow a labelled tree by adding one vertex at each step, and choose the attachment vertex with probability proportional to its number of leaf neighbours plus an offset \(a>0\). Let \(L_n^{(a)}\) be the number of degree-one vertices in the tree on \(n\) vertices. For \(n\ge4\), define the *rare-leaf odds*
\[
R_n(a)=\frac{\mathbb P(L_n^{(a)}=3)}{\mathbb P(L_n^{(a)}=2)}.
\]
Then the following is a sharp finite-size dichotomy:

1. For every integer \(4\le n\le12\), the map \(a\mapsto R_n(a)\) is **strictly decreasing** throughout \((0,\infty)\).
2. At \(n=13\), monotonicity fails; explicitly
\[
R_{13}(1/2)-R_{13}(1)=-\frac{15421}{26112}<0.
\]
3. For every integer \(n\ge14\), the function \(a\mapsto R_n(a)\) is nonmonotone: its derivative is positive for all sufficiently large \(a\) and negative for all sufficiently small \(a\).

Despite this low-tail reversal, the *entire* leaf-count distribution remains ordered in the ordinary stochastic sense: for all \(n\ge3\) and \(0<a_1<a_2\),
\[
L_n^{(a_2)}\le_{\mathrm{st}}L_n^{(a_1)},
\]
with strict stochastic order for \(n\ge4\). In particular, at thirteen vertices, the two ordered distributions at offsets \(a=1/2\) and \(a=1\) do **not** obey likelihood-ratio order in the direction of their stochastic order.

The phrase "sharp" refers specifically to first failure of monotonicity for the *two-versus-three-leaf odds*, not to an unproved classification of full likelihood-ratio ordering at smaller sizes.

## Assumptions and scope

The graph at size two is one edge; its endpoints have degree one. At every integer \(n\ge2\), an arriving vertex is connected to one of the existing \(n\) vertices, selected with probability proportional to \(a+\ell_v\), where \(\ell_v\) counts existing leaf neighbours of vertex \(v\). All offsets are positive, and the parameter is held fixed during a given tree-growth trajectory. A leaf means an undirected degree-one vertex, including the endpoints of the initial edge.

For each \(n\ge3\), \(2\le L_n^{(a)}\le n-1\). When there are \(n\ge3\) vertices and \(L_n^{(a)}=k\), every leaf has zero leaf neighbours and therefore attachment weight \(a\). The total attachment weight is \(k+an\), because every leaf contributes exactly one to the sum of leaf-neighbour counts. Hence the exact leaf-count process is a time-inhomogeneous birth/hold chain:
\[
\mathbb P(L_{n+1}^{(a)}=k\mid L_n^{(a)}=k)=\frac{ak}{k+an},\qquad
\mathbb P(L_{n+1}^{(a)}=k+1\mid L_n^{(a)}=k)=1-\frac{ak}{k+an}.
\]
Here \(L_3^{(a)}=2\) deterministically.

## Proof

**1. Stochastic ordering.** For fixed \(n,k\ge3,2\), the upward-transition probability \(1-ak/(k+an)\) strictly decreases with \(a\). Couple the processes at offsets \(a_1<a_2\) using one common independent uniform random variable per arrival, taking an upward step if the uniform value is below the appropriate upward-transition probability. When the two current counts agree, an upward step of the larger-offset process forces an upward step of the smaller-offset process. When the smaller-offset process has at least one extra leaf, the counts cannot cross in one \(0\)-or-\(1\) step. Induction gives \(L_n^{(a_1)}\ge L_n^{(a_2)}\) simultaneously for every \(n\). A strict difference has positive probability at size four and can be maintained by a common sequence of holds or of upward steps; hence the stochastic order is strict at every size \(n\ge4\).

**2. Exact odds recurrence.** Let \(p_{n,k}(a)=\mathbb P(L_n^{(a)}=k)\), which is strictly positive for \(k=2,3\) and \(n\ge4\). Set \(t=2/a>0\), and write \(R_n(t)=p_{n,3}(a)/p_{n,2}(a)\) for the same odds expressed in \(t\). From the birth/hold chain,
\[
p_{n+1,2}=\frac{2}{n+t}p_{n,2},\qquad
p_{n+1,3}=\frac{3}{n+3t/2}p_{n,3}+\frac{n-2+t}{n+t}p_{n,2}.
\]
Dividing these identities proves
\[
\boxed{R_3(t)=0,\qquad R_{n+1}(t)=\frac{3(n+t)}{2n+3t}R_n(t)+\frac{n-2+t}{2}\quad(n\ge3).}
\]
For each fixed \(n\ge4\), this is a rational function with positive denominator on \(t\ge0\).

**3. Exact finite certificate for \(4\le n\le12\).** Define integer-coefficient polynomials \(S_3(t)=0\), \(B_3(t)=1\) by
\[
\begin{aligned}
S_{n+1}(t)&=6(n+t)S_n(t)+(n-2+t)(2n+3t)B_n(t),\\
B_{n+1}(t)&=2(2n+3t)B_n(t).
\end{aligned}
\]
The preceding odds recurrence shows \(R_n(t)=S_n(t)/B_n(t)\); \(B_n(t)>0\) for \(t\ge0\). Thus the derivative has numerator
\[
Q_n(t)=S_n'(t)B_n(t)-S_n(t)B_n'(t).
\]
Direct exhaustive *integer-polynomial* coefficient arithmetic under these two displayed recurrences certifies that **every coefficient** of \(Q_n\) is strictly positive for \(4\le n\le12\). A standalone standard-library verifier (`check.py`) implements integer-list polynomial addition, multiplication and differentiation; it prints the degree and minimum coefficient for each of the nine polynomials. Their degrees are \(2,4,6,8,10,12,14,16,18\) and respective minimum coefficients are
\[
18,\ 1296,\ 69984,\ 3359232,\ 151165440,\ 6530347008,\ 274274574336,\ 11284439629824,\ 457019805007872.
\]
These exact finite coefficient checks, rather than numerical sampling, prove \(Q_n(t)>0\) for all \(t\ge0\) and hence \(R_n'(t)>0\) on these sizes. Since \(t=2/a\) decreases with \(a\), the claimed parameter monotonicity follows. The script is part of the proof certificate and needs no third-party packages.

**4. First reversal at thirteen.** Exact rational iteration of the odds recurrence at \(t=4\) (\(a=1/2\)) and \(t=2\) (\(a=1\)) gives
\[
R_{13}(4)-R_{13}(2)=-\frac{15421}{26112}<0.
\]
The certificate checks this equality using exact fractions. Since \(R_{13}(t)\) grows linearly as \(t\to\infty\), this is a genuine nonmonotonicity, rather than monotonicity in the opposite direction. Therefore an increasing-\(t\) odds law fails for the first possible size \(13\). In particular, a likelihood-ratio increase of the entire leaf-count distribution from \(a=1\) to \(a=1/2\) is impossible: its ratios at the adjacent support points \(2,3\) already run in the wrong direction.

**5. All larger sizes.** Define \(r_n=R_n(0)\) and \(q_n=R_n'(0)\), extending the rational function continuously to \(t=0\). Differentiating the odds recursion gives
\[
\begin{aligned}
r_3&=q_3=0,\\
r_{n+1}&=\frac32r_n+\frac{n-2}{2},\\
q_{n+1}&=\frac32q_n+\frac12-\frac{3r_n}{4n}.
\end{aligned}
\]
Exact fractional iteration gives \(r_7=131/16>7\) and \(q_{14}=-696574397/164003840<0\). From the recurrence, \(r_n\ge n\) for all \(n\ge7\) by induction. Consequently, once \(q_{14}<0\), the recurrence implies \(q_{n+1}\le3q_n/2-1/4<0\) for every \(n\ge14\). This proves \(R_n'(t)<0\) on a sufficiently small positive \(t\)-interval for each \(n\ge14\). On the other hand, the rational recurrence gives \(R_n(t)=(n-3)t/2+O(1)\) as \(t\to\infty\), so \(R_n'(t)>0\) for all sufficiently large \(t\). Thus every \(n\ge14\) has a reversal as claimed. Combined with steps 3 and 4 this proves the sharp cutoff.

## Verification

Run `python3 check.py` with a standard Python 3 interpreter from the folder containing this result. The checker recomputes every derivative-polynomial coefficient over the integers, the thirteen-vertex rational witness, the exact derivative sign at fourteen vertices, a finite sample of the induction, and independent exhaustive labelled-tree growth histories through seven vertices for four rational offsets. It also compares a finite set of stochastic upper-tail probabilities. In this review the checker completed with 326 exact assertions and no failures. Infinite-size and all-positive-parameter conclusions follow from the analytic recurrences and inequality induction, not from sampled runs. The finite \(n\le12\) computer certificate is exhaustive in polynomial coefficients and fully specified by a short integer recurrence.

## Relationship to prior work

Hartle and Krapivsky (2025) introduced and analyzed the leaf-driven attachment model and derived its asymptotic leaf fraction and leaf-degree statistics; the paper provides the exact leaf-count law for the *uniform recursive-tree* benchmark, but not the rare-leaf odds transition in the offset-dependent model established here. The general stochastic-order concepts and parametric likelihood-ratio criteria are standard; see Shaked and Shanthikumar (2007) and Derbazi (2026). The new contribution is the model-specific sharp thirteen-vertex reversal of low-tail odds together with the simultaneous all-parameter stochastic-order comparison. No new general stochastic-ordering theorem is claimed.

## Limitations

This theorem is about the two-versus-three-leaf odds. Its twelve-vertex positive result does not establish full likelihood-ratio ordering for every pair of offsets at sizes at most twelve. The stochastic comparison concerns leaf counts, not a monotone coupling of complete tree shapes. The result does not characterize the number or precise location of all turning points of \(R_n\) once \(n\ge13\). Historical-priority uncertainty, including possibly equivalent general birth-chain results not located in the inspected literature, remains. No independent mathematical audit has been completed.

## References

1. H. Hartle and P. L. Krapivsky, *Statistics of leaves in growing random trees*, arXiv:2511.04085v1 (first posted 2025-11-06), especially Sections III–IV, https://arxiv.org/html/2511.04085v1.
2. M. Shaked and J. G. Shanthikumar, *Stochastic Orders*, Springer (2007), Chapters 1.A and 1.C. DOI: 10.1007/978-0-387-34675-5.
3. Z. Derbazi, *Kernel Characterisations of Stochastic Orders Within Parametric Density Families*, arXiv:2605.18751 (2026), https://arxiv.org/abs/2605.18751.
