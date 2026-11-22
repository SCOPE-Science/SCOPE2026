# Exact containment-pruning size for random axis-parallel boxes

## Finding
For fixed integer dimension \(d\ge2\), sample \(n\ge1\) independent axis-parallel boxes in \([0,1]^d\), taking in each coordinate the interval between two independently uniform endpoints. Let \(M_{n,d}\) count boxes that contain no other sampled box. Then
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
where \(\gamma\) is Euler's constant. Removing all nonminimal boxes leaves the exact minimum piercing number of the family unchanged. Thus, the natural containment-pruning preprocessing yields a family of mean cardinality of order \(\sqrt n(\log n)^{d-1}\), rather than \(n\).

## Assumptions and scope
The boxes are labeled and independently sampled. The \(2dn\) endpoint coordinates are independent uniform real variables on \([0,1]\); their induced coordinate intervals are closed and have positive length almost surely. A box is containment-minimal if it contains no *distinct* sampled box, including no coincident box (coincidences have probability zero). The dimension \(d\) is fixed before taking \(n\to\infty\); no bound uniform in growing dimension is claimed. The exact formula holds for all integers \(n\ge1\) and \(d\ge1\), but the claimed higher-dimensional asymptotics are for \(d\ge2\). All logarithms are natural. No concentration or distributional limit for \(M_{n,d}\) is asserted.

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

**5. Piercing equivalence.** In any *finite* family of boxes, every nonminimal box contains a minimal box by descending a strict containment chain. Any point set intersecting all minimal boxes therefore also intersects every box. Conversely, any piercing set for the full family pierces its minimal subfamily. Thus both families have the same minimum piercing number, pointwise in every realization.

## Verification
The accompanying standalone Python checker compares the exact formula against an independently integrated planar product density for eight sample sizes; checks exact rational bounds for \(245\) size/dimension pairs; and numerically illustrates convergence of the two-term formula. These are finite checks, not substitutes for the proofs of the fixed-dimensional asymptotics. The box-containment and pruning equivalences are deterministic.

## Relationship to prior work
Tran's *Piercing Random Boxes* establishes sharp-order estimates for the optimal piercing number in this random-box model; its studied statistic is an optimization over piercing sets, not the size of the inclusion-minimal subfamily. Coffman, Lueker, Spencer and Winkler study maximal pairwise-disjoint packings rather than containment pruning. Chao, Hwang and Liang derive the *measure of the union* of random rectangles by Mellin analysis; that is not the number of inclusion-minimal boxes. The exact planar product-length density and the logarithmic dimensional factor concern a different observable from all three.

The one-dimensional expected minimal-interval count has an exact \(\sqrt n\)-order law; the present result demonstrates a different, dimension-dependent \((\log n)^{d-1}\) multiplicative factor. Neither a one-dimensional mean nor a piercing-number bound directly gives this box-count formula. The similarity of methods to existing random-box integrals nevertheless leaves residual historical-priority uncertainty.

## Limitations
Only expectation is addressed; the size of the retained subfamily may vary across realizations. No concentration statement, algorithmic runtime guarantee, optimal piercing-set construction, or uniform-in-\(d\) asymptotic is proved. Classical multivariate extrema and older geometric prefiltering work could contain equivalent formulas not identified in the consulted material. The complete text of Coffman et al.'s original packing paper was not accessible in this review; its abstract establishes a different optimization objective but does not rule out an auxiliary containment lemma.

## References
- L. V. Tran, *Piercing Random Boxes*, Random Structures & Algorithms 38 (2011), 365–380; first public journal online posting 2010-03-11; DOI: 10.1002/rsa.20321.
- E. G. Coffman, Jr., G. S. Lueker, J. Spencer and P. Winkler, *Packing Random Rectangles*, Probability Theory and Related Fields 120 (2001), 585–599; DOI: 10.1007/PL00008793.
- C.-C. Chao, H.-K. Hwang and W.-Q. Liang, *Expected Measure of the Union of Random Rectangles*, Journal of Applied Probability 35 (1998), 495–500; DOI: 10.1239/jap/1032192865.
