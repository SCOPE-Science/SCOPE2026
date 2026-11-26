# Exact containment-pruning size for random axis-parallel boxes

## Finding
For fixed integer dimension \(d\ge2\), sample \(n\ge1\) independent axis-parallel boxes in \([0,1]^d\), taking in each coordinate the interval between two independently uniform endpoints. Let \(M_{n,d}\) count sampled boxes that contain no other sampled box. Then
\[
\mathbb E M_{n,d}=n\sum_{k=0}^{n-1}(-1)^k\binom{n-1}{k}
\left[\frac{2}{(2k+1)(2k+2)}\right]^d.
\]
For each *fixed* dimension \(d\ge2\) as \(n\to\infty\),
\[
\boxed{\mathbb E M_{n,d}\sim \frac{\sqrt\pi}{(d-1)!}\sqrt n\,(\log n)^{d-1}.}
\]
In the planar case the next term is also exact:
\[
\boxed{\mathbb E M_{n,2}=
\sqrt{\pi n}\big(\log n+\gamma+2\log2-4\big)+O(\log n),}
\]
where \(\gamma\) is Euler's constant. Almost surely the sampled boxes are pairwise distinct as sets, and removing all nonminimal boxes leaves the exact minimum piercing number unchanged. For a deterministic family with repeated boxes, first replace each set of coincident copies by one representative, then prune by inclusion. The natural containment-pruning preprocessing therefore yields a family of mean cardinality of order \(\sqrt n(\log n)^{d-1}\), rather than \(n\).

## Assumptions and scope
The boxes are labeled and independently sampled. The \(2dn\) endpoint coordinates are independent uniform real variables on \([0,1]\); their induced coordinate intervals are closed and have positive length almost surely. In the definition of \(M_{n,d}\), containment includes equality with a different label. Coincidence has probability zero and hence does not change the mean. The deterministic piercing equivalence below applies to pairwise distinct boxes or to the family after deduplication. If two coincident labeled copies were the only input boxes, for example, removing every box that contains another labeled copy would wrongly discard both. The dimension \(d\) is fixed before taking \(n\to\infty\); no bound uniform in growing dimension is claimed. The finite formula also holds for \(d=1\), where it specializes to the separate minimal-interval mean discussed below. All logarithms are natural. No concentration or distributional limit for \(M_{n,d}\) is asserted.

## Proof
**1. Conditional containment probability.** For one sampled box \(B\), write its side lengths as \(X_1,\ldots,X_d\). They are independent, and each \(X_i=|U_i-V_i|\) has density \(2(1-x)\) on \(0<x<1\). Given \(B\), another independent box lies inside \(B\) exactly when each of its two endpoints in each coordinate lies inside the corresponding side interval. This has probability \(Q=\prod_{i=1}^d X_i^2\). Hence, conditioning on \(B\) and using independence of the other \(n-1\) boxes,
\[
\mathbb P(B\text{ is minimal}\mid B)=(1-Q)^{n-1},\quad
\mathbb E M_{n,d}=n\mathbb E(1-Q)^{n-1}.
\]
Since \(\mathbb E X_i^{2k}=2/[(2k+1)(2k+2)]\), binomial expansion and coordinate independence prove the finite sum.

**2. Product-length density near zero.** Put \(T_i=-\log X_i\), \(S=\sum_{i=1}^dT_i\), and \(Z=e^{-S}=\prod_{i=1}^dX_i\). The density of each \(T_i\) is \(2e^{-t}(1-e^{-t})\), for \(t>0\). Convolving on the simplex of dimension \(d-1\) gives
\[
f_S(s)=2^de^{-s}\int_{\substack{t_i\ge0\\\sum_i t_i=s}}
\prod_{i=1}^d(1-e^{-t_i})\,dt_1\cdots dt_{d-1}.
\]
The simplex has volume \(s^{d-1}/(d-1)!\); the difference between that volume and the displayed integral is nonnegative and at most the sum of its \(d\) one-coordinate integrals with \(e^{-t_i}\) in place of the product. Each is \(O_d((1+s)^{d-2})\), as \(s\to\infty\). Thus, for fixed \(d\ge2\),
\[
f_Z(z)=\frac{2^d}{(d-1)!}\big(\log(1/z)\big)^{d-1}
+O_d\big((1+\log(1/z))^{d-2}\big),\qquad z\downarrow0.
\]

**3. Leading asymptotic.** Substitution \(u=\sqrt n\,z\) yields
\[
\mathbb E M_{n,d}=\sqrt n\int_0^{\sqrt n}
(1-u^2/n)^{n-1}f_Z(u/\sqrt n)\,du.
\]
For fixed \(u>0\), the integrand, after division by \((\log n)^{d-1}\), tends to \(2e^{-u^2}/(d-1)!\) because \(2^d(1/2)^{d-1}=2\). To justify integration, split at \(u=1\) and \(u=n^{1/4}\). The product-density bound from Step 2 is dominated on \((0,1]\) by a constant times \(1+|\log u|^{d-1}\), and on \([1,n^{1/4}]\) by a constant, after normalization. Both are integrable against \(e^{-u^2/2}\). The remaining tail is exponentially negligible since \((1-u^2/n)^{n-1}\le e^{-u^2/2}\) for \(n\ge2\), while \(f_Z\) has at most polynomial logarithmic growth. Dominated convergence gives
\[
\frac{\mathbb E M_{n,d}}{\sqrt n(\log n)^{d-1}}
\longrightarrow \frac2{(d-1)!}\int_0^\infty e^{-u^2}\,du
=\frac{\sqrt\pi}{(d-1)!}.
\]

**4. Planar second term.** For \(d=2\), elementary product-density integration gives the *exact* expression
\[
f_Z(z)=4\big[(1+z)\log(1/z)-2(1-z)\big],\quad 0<z<1.
\]
In the integral of Step 3, discard the terms proportional to \(z\) at total cost \(O(\log n)\); replacing \((1-z^2)^{n-1}\) by \(e^{-nz^2}\) contributes \(O(\log n)\) as well. The remaining expression equals
\[
4\sqrt n\int_0^\infty e^{-u^2}
\left(\frac12\log n-\log u-2\right)\,du+O(\log n).
\]
Using \(\int_0^\infty e^{-u^2}du=\sqrt\pi/2\) and
\(\int_0^\infty e^{-u^2}\log u\,du=\sqrt\pi(-\gamma-2\log2)/4\)
produces the stated planar expansion.

**5. Piercing equivalence.** First discard duplicate copies, which impose identical piercing constraints. In the resulting finite family of distinct sets, every nonminimal box contains a minimal box by descending a strict containment chain. Any point set intersecting all remaining minimal boxes therefore also intersects every original box. Conversely, any piercing set for the full family pierces its minimal subfamily. This proves equality of the minimum piercing numbers for every deterministic input under the deduplicate-then-prune rule, and for the sampled family almost surely without a separate deduplication step.

## Verification
The accompanying standalone Python checker compares the exact formula against an independently integrated planar product density for eight sample sizes; checks exact rational bounds for \(245\) size/dimension pairs; and numerically illustrates convergence of the two-term formula. These are finite checks, not substitutes for the proofs of the fixed-dimensional asymptotics. The piercing equivalence after deduplication is deterministic.

## Relationship to prior work
Tran's *Piercing Random Boxes* establishes order bounds for the optimal piercing number in this random-box model; its studied statistic is an optimization over piercing sets, not the size of the inclusion-minimal subfamily. Coffman, Lueker, Spencer and Winkler study maximal pairwise-disjoint packings rather than containment pruning. Chao, Hwang and Liang use Mellin analysis for the *measure of the union* of random rectangles, a different observable. A point in an expected union is covered by an input box with probability depending on its position, whereas the pruning count uses the squared volume of a sampled box.

For \(d=1\) the displayed finite sum restates the minimal-interval mean \(\sqrt\pi\,\Gamma(n+1)/\Gamma(n+1/2)-1\) given in *Exact dual containment-frontier means for random intervals*. Indeed \(2n\int_0^1(1-x)(1-x^2)^{n-1}\,dx=nB(1/2,n)-1\). The contribution here is the exact finite mean for the multidimensional input, its dimension-dependent \((\log n)^{d-1}\) factor and leading coefficient, and the planar correction. No distinct priority claim is made for the one-dimensional specialization or for the deterministic containment-pruning rule.

## Limitations
Only expectation is addressed; the size of the retained subfamily may vary across realizations. There is no concentration statement, algorithmic runtime guarantee, optimal piercing-set construction, or uniform-in-\(d\) asymptotic. Classical multivariate extrema and older geometric prefiltering work could contain equivalent formulas. The objective in the introduction of the packing paper differs from the present one, but that comparison does not rule out an auxiliary containment lemma elsewhere in the paper.

## References
- L. V. Tran, *Piercing Random Boxes*, Random Structures & Algorithms 38 (2011), 365–380; first public journal online posting 2010-03-11; DOI: 10.1002/rsa.20321. See also *Random Matrices and Random Boxes*, Chapter 3, https://rucore.libraries.rutgers.edu/rutgers-lib/31202/PDF/1/.
- E. G. Coffman, Jr., G. S. Lueker, J. Spencer and P. Winkler, *Packing Random Rectangles*, Probability Theory and Related Fields 120 (2001), 585–599; DOI: 10.1007/PL00008793.
- C.-C. Chao, H.-K. Hwang and W.-Q. Liang, *Expected Measure of the Union of Random Rectangles*, Journal of Applied Probability 35 (1998), 495–500; DOI: 10.1239/jap/1032192865.
- *Exact dual containment-frontier means for random intervals*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-dual-containment-frontier-means-for-random-intervals--c51867200019.
