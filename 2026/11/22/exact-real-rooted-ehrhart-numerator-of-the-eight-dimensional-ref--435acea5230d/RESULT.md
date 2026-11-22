# Exact real-rooted Ehrhart numerator of the eight-dimensional reflexive facet-bound counterexample

## Finding

Let \(Q\subset\mathbb R^3\) be the lattice polytope with 21 vertices listed below, and define the free sum \(B=Q\circ Q\subset\mathbb R^6\). Consider the reflexive eight-dimensional polytope
\[
P=\operatorname{conv}\bigl((B,-1,-1)\cup\{(0_6,-1,2),(0_6,1,-1)\}\bigr).
\]
It is the 44-vertex, 1371-facet counterexample of Hofscheier and Nill [1]. Its Ehrhart numerator is exactly
\[
\boxed{h_P^*(t)=1+4197t+216653t^2+1654776t^3+3130992t^4
+1654776t^5+216653t^6+4197t^7+t^8.}
\]
All eight roots of this polynomial are **distinct, real and strictly negative**. Moreover its normalized volume is \(8!\operatorname{vol}(P)=6882246\), and its \(\gamma\)-vector is
\[
(1,4189,191491,825921,246354),
\]
so the numerator is in particular strictly unimodal and \(\gamma\)-positive. The real-rootedness is an exact assertion, certified by four rational sign-changing intervals rather than numerical root approximation.

## Assumptions and scope

The 21 vertices of \(Q\) (each row a point) are
\[
\begin{array}{rrr}
6&-6&0\\4&0&-2\\3&1&-2\\3&0&0\\3&0&-3\\
2&1&-1\\2&-2&2\\1&1&-1\\1&0&1\\1&-1&2\\
0&0&-3\\0&-1&2\\0&-3&3\\0&-6&0\\0&-6&-6\\
-1&0&0\\-1&0&-1\\-1&-2&2\\-2&-1&-1\\-2&-2&-2\\-3&-3&0
\end{array}.
\]
Here \(\circ\) is the convex free sum in complementary coordinate subspaces. Normalized volume uses the standard lattice \(\mathbb Z^8\). For integer \(k\ge0\), let \(L_P(k)=\#(kP\cap\mathbb Z^8)\); by definition \(\sum_{k\ge0}L_P(k)t^k=h_P^*(t)/(1-t)^9\). All statements concern this one explicitly defined polytope, not every high-facet reflexive polytope. Reflexivity and the facet count are taken from [1], not newly claimed.

## Proof

**Exact three-dimensional facet data.** From each unordered triple of the 21 input vertices, take the primitive integer cross-product normal of their affine plane; retain the plane if all 21 points lie on one side and orient it as \(\langle u,x\rangle\le h\). Exhaustively doing so gives precisely 37 distinct facet planes, with positive integral heights \(h\in\{1,3,6\}\). This is an exhaustive procedure: any three-dimensional facet contains three affinely independent input vertices. The algorithm in `verify.py` generates all such triples, checks the support inequalities, deduplicates planes, and verifies that each input point is an extreme vertex. As all heights are positive, \(0\) is in the interior of \(Q\).

Define the Minkowski gauge \(\gamma_Q(x)=\inf\{r\ge0:x\in rQ\}\). The 37 supporting inequalities give
\[
\gamma_Q(x)=\max_{(u,h)\in\mathcal F(Q)}\frac{\langle u,x\rangle}{h}.
\]
Thus \(6\gamma_Q(x)\) is a nonnegative integer for all \(x\in\mathbb Z^3\). Set
\[
s_j=\#\{x\in\mathbb Z^3:6\gamma_Q(x)=j\},\qquad 0\le j\le48,
\]
and \(F(r)=\sum_{i+j\le r}s_i s_j\). The sum is over nonnegative indices. By the elementary free-sum gauge identity,
\[
\gamma_B(x,y)=\gamma_Q(x)+\gamma_Q(y),\qquad
F(r)=\#\{(x,y)\in\mathbb Z^6:\gamma_B(x,y)\le r/6\}.
\]

**Exact lattice fibers.** An element of \(kP\) has last two coordinates
\[
(z_1,z_2)=(-k+2c,-k+3b),
\]
where \(a,b,c\ge0\), \(a+b+c=k\), and its first six coordinates belong to \(aB\). The last two coordinates are integral exactly when \(c=n/2\) and \(b=m/3\) for integers \(m,n\ge0\). Consequently
\[
\boxed{L_P(k)=\sum_{\substack{m,n\ge0\\2m+3n\le6k}} F(6k-2m-3n).}
\]
No lattice points are missed or multiply counted, since \(m=z_2+k\) and \(n=z_1+k\) are uniquely determined by the last two integral coordinates.

The finite exact enumeration in `verify.py` evaluates every lattice point in the coordinate bounding box of \(8Q\), computes its gauge from all 37 integer facet inequalities, and records the 49 integer shell counts \(s_0,\ldots,s_{48}\). Every point of gauge at most 8 belongs to \(8Q\), hence is in this box; the computation is exhaustive, not sampled. It gives
\[
\begin{array}{r|r}
k&L_P(k)\\\hline
0&1\\1&4206\\2&254471\\3&3793683\\4&28466361\\5&142125171\\
6&541690094\\7&1703589231\\8&4639992475
\end{array}.
\]
By the degree-eight Ehrhart numerator identity,
\[
h_i^*=\sum_{j=0}^{i}(-1)^j\binom{9}{j}L_P(i-j),\quad 0\le i\le8,
\]
these numbers give exactly the displayed coefficient vector.

**Independent volume cross-check.** Triangulating each of the 37 facet polygons from the interior origin, summing absolute integer determinants of its constituent tetrahedra, gives \(3!\operatorname{vol}(Q)=1071\). This is independently checked using the exact planar convex-hull and triangle-fan routines in `verify.py`. Since \(B=Q\circ Q\), its normalized six-volume is \(1071^2\). The determinant of the two apex displacements in the last coordinates is 6. The join-volume formula therefore yields \(8!\operatorname{vol}(P)=6\cdot1071^2=6882246\), agreeing exactly with the sum of the nine Ehrhart numerator coefficients.

**Strict real-rootedness.** Palindromicity permits the substitution \(x=t+t^{-1}\). Algebraically,
\[
t^{-4}h_P^*(t)=q(t+t^{-1}),\qquad
q(x)=x^4+4197x^3+216649x^2+1642185x+2697688.
\]
The exact integers \(q(-5000)>0>q(-4000)\), \(q(-50)<0<q(-40)\), \(q(-7)>0>q(-6)\), and \(q(-3)<0<q(-2)\) give four different real zeros of the quartic, each strictly less than \(-2\). These are all its roots, by degree. Each root \(x<-2\) produces two distinct strictly negative reciprocal real roots of \(t^2-xt+1=0\), proving eight simple negative roots for \(h_P^*\). Finally direct coefficient comparison in
\[
h_P^*(t)=\sum_{j=0}^4\gamma_j t^j(1+t)^{8-2j}
\]
gives the positive \(\gamma\)-vector displayed above.

## Verification

The self-contained Python 3 standard-library checker `verify.py` enumerates all 1330 vertex triples, derives all 37 integer facets, confirms all 21 vertices are extreme, computes exact normalized three-volume by facet triangulation, enumerates the full gauge shell, verifies all nine lattice counts and all nine numerator coefficients, checks the independent normalized-volume identity, and tests all four quartic sign changes. Every calculation uses integers; no approximate convex hull or root solver is required. Run `python3 verify.py` from the extracted artifact directory. The checker terminates with `PASS` assertions; its code, not a transcript, is the reproducible certificate.

## Relationship to prior work

Hofscheier and Nill [1, Theorem 2.1] introduced \(P\) as an eight-dimensional 44-vertex reflexive polytope with 1371 facets, disproving an earlier sharp facet conjecture. They did not report the Ehrhart numerator or its roots. Beck, Jayawant and McAllister [2] give general lattice-point generating functions for free sums and characterize when Braun's simpler multiplicative formula applies. Those abstract identities do not state the concrete coefficients or strict real-rootedness established here. Since \(Q\) has nonunit facet distances, a reflexive-factor product formula cannot simply be applied to \(Q\circ Q\); the rational-gauge convolution above handles the actual nonreflexive factor. The general significance of real-rooted and unimodal Ehrhart numerators is discussed in [3]. The precise table and the negative-root certificate here are newly computed, rather than attributed to the cited authors.

## Limitations

This is a complete exact invariant for one explicit eight-dimensional example; no classification of all facet-bound counterexamples or theorem about their general Ehrhart roots follows. The exhaustive certificate is finite and supplies no external independent validation. The preceding literature comparison is not a guarantee that no unindexed software database or unpublished calculation already contains the coefficients. The first public date is that of the motivating construction [1], not the date of this computation.

## References

1. Johannes Hofscheier and Benjamin Nill, *Reflexive polytopes can have doubly exponentially many vertices*, arXiv:2611.08819v1, first posted 2026-11-06. https://arxiv.org/abs/2611.08819
2. Matthias Beck, Pallavi Jayawant, and Tyrrell B. McAllister, *Lattice-point generating functions for free sums of convex sets*, Journal of Combinatorial Theory, Series A 120 (2013), 1246–1262; arXiv:1207.0164. https://arxiv.org/abs/1207.0164
3. Benjamin Braun and Robert Davis, *Ehrhart series, unimodality, and integrally closed reflexive polytopes*, Annals of Combinatorics 20 (2016), 705–717. https://doi.org/10.1007/s00026-016-0337-6
4. Benjamin Braun, *An Ehrhart series formula for reflexive polytopes*, Electronic Journal of Combinatorics 13 (2006), N15. https://doi.org/10.37236/1153
