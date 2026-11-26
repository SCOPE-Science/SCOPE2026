# Two-parameter sink-side law for unbalanced random bipartite acyclic orientations

## Finding

Let \(K_{m,n}\) be the complete bipartite graph with two labeled vertex classes \(A\) and \(B\), of sizes \(m\) and \(n\). Select an acyclic orientation uniformly from all acyclic orientations of this graph. Let \(S\geq 1\) be its total number of sinks (vertices of outdegree zero), and let \(J\in\{A,B\}\) be their common class.

Suppose \(m,n\to\infty\) with \(m/n\to\rho\in(0,\infty)\). There is a unique pair \((a,b)\) of positive numbers satisfying
\[
(e^a-1)(e^b-1)=1,\qquad \rho=\frac{a}{(e^a-1)b}.
\]
Set \(w_A=e^a/(e^a+e^b)\) and \(w_B=e^b/(e^a+e^b)\). The **joint law** of sink class and number of sinks converges in total variation to
\[
\Pr(J=A,S=k)\longrightarrow w_A\frac{a^k}{k!(e^a-1)},\quad
\Pr(J=B,S=k)\longrightarrow w_B\frac{b^k}{k!(e^b-1)},\qquad k=1,2,\ldots.
\]
Here the probabilities on the left belong to the corresponding finite graph. Thus the limiting marginal sink-count law is a mixture of zero-truncated Poisson laws with respective parameters \(a\) and \(b\), with mixing weights \(w_A\) and \(w_B\). For \(\rho\ne1\), the parameters are distinct and the marginal is **not** itself a zero-truncated Poisson law. The limiting probability that the sinks lie in the larger vertex class is greater than one-half. At \(\rho=1\), both parameters equal \(\log 2\), and the marginal generating function is \(2^z-1\), a previously established balanced-case result.

For use in deriving the unequal-ratio limit, the exact finite-size exponential generating functions can be written in the following class-resolved form, with \(z\) marking sink number. These finite counts follow directly by separating the two designated-sink sums in the earlier balanced-limit record [7] and are not asserted as a new enumeration:
\[
F_A(x,y;z)=\frac{e^x(e^y-1)(e^{zx}-1)}{1-(e^x-1)(e^y-1)},\qquad
F_B(x,y;z)=\frac{e^y(e^x-1)(e^{zy}-1)}{1-(e^x-1)(e^y-1)}.
\]
For every \(m,n\ge1\), the coefficient \(m!n![x^m y^n z^k]F_A\) (respectively \(F_B\)) is the number of acyclic orientations of \(K_{m,n}\) with exactly \(k\) sinks, all in class \(A\) (respectively \(B\)). The sums of these coefficients over positive \(k\) recover the usual negative-index poly-Bernoulli enumeration.

## Assumptions and scope

All vertices within each part are individually labeled. Every **acyclic orientation** has equal probability; orienting edges independently and then conditioning on acyclicity would give the same distribution because the initial edge orientation is fair, but orienting edges using a uniform random vertex permutation gives a different distribution. The asymptotic theorem assumes both parts diverge and their ratio tends to a finite, strictly positive constant; it does not cover a bounded side or a ratio tending to zero or infinity. The sink-side variable is well-defined because vertices in opposite parts are adjacent, so no orientation can have a sink in each part.

The parameter pair is the positive critical point of \(1-(e^x-1)(e^y-1)=0\) in direction \((m,n)\), whose existence and uniqueness in every positive limiting aspect ratio follow from the strictly minimal smooth critical-point theory established for lonesum-matrix enumeration by Khera, Lundberg and Melczer (2019/2020), cited below.

## Proof

**1. Canonical alternating blocks.** In a finite directed acyclic graph, repeatedly remove all sinks. For an acyclic orientation of a complete bipartite graph, each removed nonempty sink set belongs to one class. While both classes are present, the next sink set must belong to the opposite class: removing a set of vertices from one class does not change the outgoing edges of any other vertex in that same class. Once a class is exhausted, all vertices in the remaining class form the last sink layer. Hence the sink layers, read in reverse, form a unique alternating sequence of nonempty labeled blocks of the two colors, of length at least two. Conversely, each such alternating block sequence defines one acyclic orientation by directing all edges between different-colored blocks toward the later block. Its final block is exactly the set of sinks. These two maps are inverse.

**2. Marking the last block.** Write \(X=e^x-1\), \(Y=e^y-1\). A nonempty block of class \(A\) has exponential generating function \(X\), and one of class \(B\) has \(Y\). Alternating nonempty prefixes ending in \(B\) have generating function
\[
Y+XY+YXY+XYXY+\cdots=\frac{Y(1+X)}{1-XY}=\frac{Ye^x}{1-XY}.
\]
Appending a nonempty final \(A\)-block, whose size is marked by \(z\), multiplies this by \(e^{zx}-1\). The symmetric calculation for a final \(B\)-block yields the stated exact \(F_A,F_B\). At \(z=1\), the sum differs from the standard complete orientation enumerator \(e^{x+y}/(1-XY)\) only by \(e^x+e^y-1\), which has no strictly positive mixed coefficient. Therefore the marked functions recover all actual orientations for \(m,n\ge1\).

Equivalently, writing \(\mathcal B=e^{x+y}/(1-XY)\), the first-side designated-sink sum of [7] has EGF \(\mathcal B(e^{(z-1)x}-1)\). On strictly mixed sizes it counts \(z^S-1\) for orientations whose sinks are in \(A\) and zero for the others. Subtracting its value at \(z=0\) leaves the first-side marked count. Its EGF agrees with \(\mathcal B e^{-x}(e^{zx}-1)\), up to pure terms. In fact \(e^y=e^xY+(1-XY)\) so the latter differs from \(F_A\) only by \(e^{zx}-1\). Exchanging \(x\) and \(y\) proves the second identity. The total marked EGF of [7] is \(F_A+F_B+e^{zx}+e^{zy}-1\).

**3. Fixed-multiplicity singular transfer.** For any fixed integer \(k\ge1\), extracting the coefficient of \(z^k\) gives
\[
[z^k]F_A=\frac{e^xYx^k}{k!(1-XY)},\qquad
[z^k]F_B=\frac{e^yXy^k}{k!(1-XY)}.
\]
The corresponding unmarked numerator is \(G_1=e^xYX+e^yXY\). The denominator \(H=1-XY\) is exactly the smooth strictly minimal singular variety treated by Khera, Lundberg and Melczer, Section 3, Lemma 3.1 and Theorem 3.2. Their multivariate coefficient transfer applies to each of the displayed entire numerators: the positive critical point is unique for the direction, the Hessian factor is nonzero, the numerators are positive there, and all these functions have the same denominator. The resulting leading coefficient factors are identical except for evaluation of their numerators at the critical point, with error vanishing along any sequence of bounded positive aspect ratio. The critical-point equations are
\[
(e^a-1)(e^b-1)=1,\qquad
\frac{m}{n}=\frac{a H_x(a,b)}{b H_y(a,b)}=\frac{a}{(e^a-1)b}.
\]
Here the second equality uses \(H_x=-e^x(e^y-1)\), \(H_y=-e^y(e^x-1)\) and the singular equation. At that point, \(G_1(a,b)=e^a+e^b\), and \(Y=1/(e^a-1)\). Dividing the asymptotic marked coefficient by the unmarked one yields exactly
\[
\frac{e^a(a^k/k!)/(e^a-1)}{e^a+e^b}
=w_A\frac{a^k}{k!(e^a-1)},
\]
with the analogous expression for class \(B\). Since the limiting masses sum to \(w_A+w_B=1\), coordinatewise convergence on the countable space \(\{A,B\}\times\{1,2,\ldots\}\) implies total-variation convergence (by a finite-tail argument or the discrete Scheffé lemma).

**4. Strict mixture and side asymmetry.** Uniqueness of the positive critical point gives \(a=b=\log 2\) only when \(\rho=1\). Monotonicity of the critical-point parametrization shows \(\rho>1\) precisely when \(a>b\), giving \(w_A>1/2\); swap classes for \(\rho<1\). If \(\rho\ne1\), then \(a\ne b\). The sequence \(k!\Pr(S=k)\) for the limiting distribution is a strictly positive sum of two exponential sequences with distinct bases and weights, and hence is strictly log-convex in \(k\); a single zero-truncated Poisson distribution instead gives a geometric sequence and equality in the log-convexity relation. Thus the unequal-class limit is genuinely a mixture, not a reparameterized zero-truncated Poisson law.

## Verification

The included standard-library program `verify.py` independently enumerates all directed edge assignments for 15 small bipartite graphs, tests acyclicity by topological deletion, and compares the sink-side and sink-count tables with the alternating-block Stirling-number calculation. It also checks the resulting total against the classical poly-Bernoulli enumeration for all 81 pairs \(1\le m,n\le9\). The executed result was: `PASS: 81 Stirling-count identities; 15 independent exhaustive DAG enumerations`. These are finite checks, not evidence replacing the singularity-analysis proof of the limit law.

## Relationship to prior work

Cameron, Glass, Rekvényi and Schumacher give the acyclic-orientation/lonesum-matrix bijection and the poly-Bernoulli total counts. Khera, Lundberg and Melczer prove the bivariate coefficient asymptotics, strict minimality and smooth saddle transfer used in Step 3. Their unmarked theorem is powerful enough to support this calculation but does not state the marked sink law or its unequal-class mixture. Hwang, Jung, Lee, Oh and Yu develop the general acyclic-orientation sink polynomial and its symmetric-function description, but do not specialize it to this unequal-bipartition limit. Ayyer, Hathcock and Tetali enumerate orientations having a **unique** sink; that is the \(k=1\) slice, not the joint limiting distribution over all \(k\). Khera and Lundberg study the **longest directed path**, not sink multiplicity. The result in [7] gives the exact aggregate sink marking for all sizes (its designated-sink proof also yields the side counts, as explained above), and its asymptotic concerns the balanced diagonal. Neither the finite formulas nor the balanced law is claimed as new. The contribution is the joint side/count limit along unequal positive limiting ratios, identifying the bias toward the larger part and the distinct conditional Poisson parameters that produce the non-Poisson mixture.

## Limitations

The result is not an independence theorem: sink side and sink number have a nontrivial limiting association whenever the part sizes are unbalanced. The proof imports a published analytic multivariate transfer theorem and its regularity checks rather than independently reproving that general machinery. It establishes neither a convergence rate in total variation nor uniformity as the ratio approaches zero or infinity. Earlier literature on sink enumerations and lonesum variants is extensive; uninspected older sources, including West's 1995 complete-bipartite orientation article, remain a priority risk, and the claim has not undergone independent validation.

## References

1. P. J. Cameron, C. A. Glass, K. Rekvényi and R. U. Schumacher, *Acyclic orientations and poly-Bernoulli numbers*, first preprint 2014-12-11, https://arxiv.org/abs/1412.3685 (especially Section 3).
2. J. Khera, E. Lundberg and S. Melczer, *Asymptotic Enumeration of Lonesum Matrices*, first preprint 2019, https://arxiv.org/abs/1912.08850 (Lemma 3.1 and Theorems 3.1–3.2).
3. A. Ayyer, D. Hathcock and P. Tetali, *Toppleable Permutations, Excedances and Acyclic Orientations*, first preprint 2020, https://arxiv.org/abs/2010.11236 (sections on unique sinks).
4. J. Khera and E. Lundberg, *The distribution of the length of the longest path in random acyclic orientations of a complete bipartite graph*, first preprint 2024, https://arxiv.org/abs/2408.12716.
5. B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh and S.-H. Yu, *Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions*, first preprint 2019, https://arxiv.org/abs/1910.10920.
6. D. B. West, *Acyclic orientations of complete bipartite graphs*, Discrete Mathematics 138 (1995), 393–396, https://doi.org/10.1016/0012-365X(94)00222-5 (full text not inspected).
7. *Zero-truncated Poisson sink law for uniform acyclic orientations of balanced complete bipartite graphs*, 2026-11-08, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-zero-truncated-poisson-sink-law-for-uniform-acyclic-orientations--71931ebc05c2 .
