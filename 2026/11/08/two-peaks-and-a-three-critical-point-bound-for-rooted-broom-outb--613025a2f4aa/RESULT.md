# Two peaks and a three-critical-point bound for rooted-broom outbreak variance

## Finding
Let \(B_{m,L}\) be the rooted tree consisting of \(m\) pendant edges incident to a root and one further root-to-leaf path of \(L\) edges. In independent homogeneous bond percolation, each edge is open with probability \(p\in[0,1]\), and \(X_{m,L}(p)\) denotes the number of vertices in the root's open component.

**Theorem.** For every pair of integers \(m\ge3\), \(L\ge3\), the function \(p\mapsto\operatorname{Var}(X_{m,L}(p))\) has at most two local maxima in \((0,1)\). For every integer \(L\ge14\) and every integer \(136\le m\le149\), it has **exactly two strict local maxima**, separated by **one strict local minimum**, and exactly three critical points in \((0,1)\). The latter points lie respectively in \((0,2/3)\), \((2/3,3/4)\), and \((3/4,1)\).

Thus a finite tree with a fixed initial outbreak source can have two distinct transmission-probability windows of elevated outbreak-size variance. For example, \(B_{140,14}\) has \(155\) vertices. No assertion of globally minimal tree size is made.

## Assumptions and scope
The graph is a finite, undirected, simple rooted tree. Edges are independently and identically open with common parameter \(p\), with no dependence induced by shared random infectious periods. The outbreak is the connected open cluster of the prescribed root, including the root. An arbitrary constant added to the cluster size does not change its variance. The statement concerns local extrema of variance as a function of transmission parameter, not modes of a cluster-size probability distribution.

## Proof
**Step 1 (exact law and polynomial).** The \(m\) root leaves contribute a binomial random variable \(K\sim\operatorname{Bin}(m,p)\). The path contributes the number \(Y_L\) of consecutive open edges from the root before the first closed edge, truncated at \(L\). The two edge sets are disjoint and hence \(K\) and \(Y_L\) are independent, with \(X_{m,L}=1+K+Y_L\). For \(1\le j\le L\),
\[
\Pr(Y_L\ge j)=p^j,\qquad
\mathbb E Y_L=\sum_{j=1}^L p^j,\qquad
\mathbb E Y_L^2=\sum_{j=1}^L(2j-1)p^j.
\]
The last identity follows from \(Y_L^2=\sum_{j=1}^{Y_L}(2j-1)\). On expanding the square of the first moment and collecting integer powers of \(p\),
\[
V_{m,L}(p):=\operatorname{Var}(X_{m,L}(p))
=mp(1-p)+\sum_{k=1}^L k p^k
-\sum_{k=L+1}^{2L}(2L+1-k)p^k.\tag{1}
\]
This is an exact polynomial identity, including at both endpoints. For \(0<p<1\) its path-only part also has the rational expression
\[
W_L(p):=\operatorname{Var}(Y_L)
=\frac{p}{(1-p)^2}
-\frac{(2L+1)p^{L+1}}{1-p}
-\frac{p^{2L+2}}{(1-p)^2}.\tag{2}
\]
The apparent singularity at \(p=1\) in (2) is removable by (1).

**Step 2 (universal bound for brooms).** For \(m\ge3\), \(L\ge3\), the nonzero coefficients in increasing degree in (1) have four consecutive sign blocks: \(+\) at degree one (coefficient \(m+1\)), \(-\) at degree two (coefficient \(2-m\)), \(+\) at degrees three through \(L\), and \(-\) at degrees \(L+1\) through \(2L\). Differentiating preserves each nonzero coefficient's sign. Consequently the derivative polynomial has **exactly three coefficient sign changes**. Descartes' rule of signs gives at most three positive real roots, counted with multiplicities. Four distinct local maxima would require at least seven intervening critical points; even three distinct local maxima would require at least five. Hence there are at most two interior local maxima.

**Step 3 (two negative/positive derivative brackets).** Differentiating (2), the correction terms subtracted from the infinite-path variance have strictly positive derivatives for \(0<p<1\). Therefore
\[
W_L'(2/3)<\left.\frac{1+p}{(1-p)^3}\right|_{p=2/3}=45.
\]
For every integer \(m\ge136\),
\[
V_{m,L}'(2/3)=W_L'(2/3)-m/3<45-136/3<0.\tag{3}
\]
At \(p=3/4\), direct differentiation of (2) gives
\[
W_L'(3/4)=112-A_L-B_L,\qquad
A_L=4(2L+1)(L+4)(3/4)^L,\quad
B_L=24(L+4)(9/16)^L.\tag{4}
\]
Both positive corrections decrease strictly with integer \(L\ge14\). Indeed,
\[
\frac{A_{L+1}}{A_L}
=\frac{3(2L+3)(L+5)}{4(2L+1)(L+4)}<1
\]
because \(2L^2-3L-29>0\) for \(L\ge14\), while
\[
\frac{B_{L+1}}{B_L}=\frac{9(L+5)}{16(L+4)}<1.
\]
The exact rational inequalities \((3/4)^{14}<1/56\) and \((9/16)^{14}<1/3000\) imply
\[
A_{14}+B_{14}
<\frac{2088}{56}+\frac{432}{3000}
<\frac{75}{2}.
\]
Thus \(W_L'(3/4)>112-75/2=149/2\) for all \(L\ge14\), and for each \(m\le149\),
\[
V_{m,L}'(3/4)=W_L'(3/4)-m/2>0.\tag{5}
\]

**Step 4 (endpoints and exact number of extrema).** From (1),
\[
V_{m,L}'(0)=m+1>0,\qquad
V_{m,L}'(1)=-m-\sum_{j=1}^L j^2
=-m-\frac{L(L+1)(2L+1)}6<0.\tag{6}
\]
For \(L\ge14\) and \(136\le m\le149\), (3), (5), and (6) give derivative signs \(+,-,+,-\) at \(0,2/3,3/4,1\). By continuity, the derivative has a root in each of the three stated disjoint open intervals. The three-sign-change bound from Step 2 allows no additional positive root, nor multiplicity exceeding one at those roots. The roots are simple, and the sign changes force a strict maximum, then a strict minimum, then a strict maximum. This proves the theorem for every permitted integer \(m,L\), not just checked examples.

## Verification
The attached standalone \(verify_broom.py\) uses only standard-library exact integer and rational arithmetic. Execute `python3 verify_broom.py` from the folder containing this result. Its independent checks compare the polynomial with the first two moments, enumerate all edge-open configurations for small trees, verify the rational sign brackets, and check the polynomial's coefficient sign pattern for representative larger parameters. The analytic inequalities and Descartes argument above establish the infinite result; the finite checker is supplementary evidence, not a substitute.

## Relationship to prior work
Moore and Newman (1999 preprint) formulate epidemic transmission through independent occupied bonds and analyze percolation thresholds on small-world networks, rather than the exact number of variance extrema on a prescribed finite rooted broom. Kenah and Robins (2007) establish that general SIR epidemics with random infectious periods are **not**, in general, equivalent to independent bond percolation; the present assumptions deliberately retain the independent-edge model. Sharkey and collaborators (2013) obtain exact Markovian SIR moment equations on trees, a different stochastic process and observable. Nogawa, Hasegawa and Nemoto (2016) describe a **bimodal cluster-size probability density at fixed transmission probability** on Cayley trees, rather than two maxima of variance as the parameter varies on finite broom trees. These distinctions follow from their inspected mathematical statements and scopes. No claim is made that an unsuccessful literature search proves priority over all earlier work.

## Limitations
The three-critical-point upper bound is for rooted brooms, not arbitrary trees or arbitrary graphs. The construction is not asserted to minimize vertex number or number of pendant edges. The edge-independent outbreak model need not represent a continuous-time Markov SIR epidemic with shared recovery-time randomness. The two extrema refer to the variance curve in \(p\), not to a multimodal probability mass function. Historical priority remains provisional until independent comprehensive literature assessment.

## References
1. C. Moore and M. E. J. Newman, *Epidemics and percolation in small-world networks*, arXiv:cond-mat/9911492, first posted 1999-11-30. https://arxiv.org/abs/cond-mat/9911492
2. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, Phys. Rev. E 76, 036113 (2007). https://pmc.ncbi.nlm.nih.gov/articles/PMC2215389/
3. K. J. Sharkey, I. Z. Kiss, R. R. Wilkinson and P. L. Simon, *Exact Equations for SIR Epidemics on Tree Graphs*, Bull. Math. Biol., online 2013-12-18. https://pmc.ncbi.nlm.nih.gov/articles/PMC4541714/
4. T. Nogawa, T. Hasegawa and K. Nemoto, *Local cluster-size statistics in the critical phase of bond percolation on the Cayley tree*, arXiv:1602.00803 (2016). https://arxiv.org/abs/1602.00803
