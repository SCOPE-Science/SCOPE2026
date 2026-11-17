# Exponential loss of negative type in complete-transposition symmetric-group metrics

## Finding
Let \(S_n\) carry the Cayley metric \(d_n(g,h)=n-c(g^{-1}h)\), where \(c(\sigma)\) counts all cycles, including fixed points. Define \(\beta_n\) to be its generalized roundness, equivalently the largest exponent \(p\ge0\) for which \(d_n^p\) is conditionally negative semidefinite (CND). For every \(n\ge3\), \(0<\beta_n\le\log_2(3/2)\); more sharply, \(\beta_n\) decays exponentially. For every \(0<u<v<\log 2\), put
\[
 a_{u,v}=(1-e^{-u})(2e^{-v}-1),\qquad
 \rho_v=\frac{3}{2(1+e^{-v})}<1,\qquad
 C_{u,v}=\frac{1}{a_{u,v}\log(v/u)\log2}.
\]
Then
\[
 0<\beta_n\le\min\!\left\{\log_2(3/2),\ C_{u,v}\rho_v^{\,n-3}\right\},\qquad
 \limsup_{n\to\infty}\beta_n^{1/n}\le\frac34.
\]
The exponent \(3/4\) is an upper exponential rate, not an assertion of sharpness.

The first three nontrivial exact values are
\[
 \beta_3=\log_2(3/2)=0.5849625007\ldots,
\]
\[
 \beta_4=0.4821471851\ldots\quad\text{(unique positive solution of }6\cdot3^p-3\cdot2^p-6=0\text{)},
\]
\[
 \beta_5=0.3131601640\ldots\quad\text{(unique solution in }(3/10,8/25)\text{ of }24\cdot4^p-50\cdot3^p+35\cdot2^p-10=0\text{)}.
\]
The least Euclidean embedding dimensions of \((S_n,d_n^{p/2})\) below the critical exponent are respectively \(5,23,119\) for \(n=3,4,5\); at \(p=\beta_n\) they drop to exactly \(4,14,118\). No isometric Euclidean embedding of the powered distance exists for \(p>\beta_n\).

## Assumptions and scope
All symmetric groups are finite and carry the *complete-transposition* generating set, not adjacent transpositions. A symmetric zero-diagonal kernel \(K\) is CND if \(\sum_{g,h}\overline{z_g}z_hK(g,h)\le0\) for every complex \(z\) with \(\sum_gz_g=0\). The distance \(d_n\) counts the minimum number of arbitrary transpositions; indeed \(d_n(g,h)=n-c(g^{-1}h)\). Generalized roundness and \(p\)-negative type are identified by the standard negative-kernel equivalence. The result does not claim exact \(\beta_n\) for \(n\ge6\) or a matching asymptotic lower bound.

## Proof
**1. Central Fourier criterion.** On a finite group, the kernel \(K(g,h)=f(g^{-1}h)\) with real central \(f\) is CND if and only if its regular-representation Fourier scalars \(d_\lambda^{-1}\sum_{\sigma\in S_n}f(\sigma)\chi_\lambda(\sigma)\) are nonpositive for every *nontrivial* irreducible representation \(\lambda\). This follows from the complete orthogonal decomposition of the zero-mean space into isotypic blocks of dimensions \(d_\lambda^2\). Here \(f(\sigma)=(n-c(\sigma))^p\). At \(p=0^+\), every nontrivial scalar is \(-1\), since \(f\) becomes the discrete metric \(\mathbf1_{\sigma\ne e}\). Hence each finite \(S_n\) has positive generalized roundness.

**2. The hook Fourier obstruction.** Let \(\lambda=(n-2,1,1)\), with \(d_\lambda=(n-1)(n-2)/2\). The Jucys--Murphy product identity, obtained by inserting \(n\) either as a singleton cycle or into an existing cycle, gives
\[
 \sum_{\sigma\in S_n}t^{c(\sigma)}\sigma=\prod_{j=1}^n(t+J_j),\qquad J_j=\sum_{i<j}(i\ j).
\]
Each \(J_j\) acts on a Young seminormal vector by the content of the box occupied by \(j\). The contents of this hook are \(0,1,\ldots,n-3,-1,-2\). Therefore the normalized character transform of \(e^{-td_n(e,\sigma)}\) is *exactly*
\[
 H_n(t)=\frac1{d_\lambda}\sum_\sigma\chi_\lambda(\sigma)e^{-t(n-c(\sigma))}
 =(1-e^{-t})(1-2e^{-t})\prod_{j=1}^{n-3}(1+je^{-t}).
\]
For \(0<p<1\), the Bernstein fractional-power identity and nontrivial-character orthogonality imply
\[
 \frac1{d_\lambda}\sum_\sigma\chi_\lambda(\sigma)d_n(e,\sigma)^p
 =-\frac{p}{\Gamma(1-p)}\int_0^\infty H_n(t)t^{-1-p}\,dt.
\]
The integral converges: \(H_n(t)=O(t)\) near zero and is bounded at infinity. Its sign is the opposite of the Fourier scalar's sign.

**3. Explicit exponential comparison.** Fix \(0<u<v<\log2\). On \([u,v]\), \(H_n(t)\le -a_{u,v}\prod_{j=1}^{n-3}(1+je^{-v})\). On \((0,\log2)\) its sign is nonpositive; on \([\log2,\infty)\), \(0\le H_n(t)\le\prod_{j=1}^{n-3}(1+j/2)\). Consequently
\[
 \int_0^\infty H_n(t)t^{-1-p}\,dt\le
 -a_{u,v}\log(v/u)\prod_{j=1}^{n-3}(1+je^{-v})
 +\frac1{p\log2}\prod_{j=1}^{n-3}(1+j/2),
\]
where \(t^{-1-p}\ge t^{-1}\) on \([u,v]\subset(0,1)\) and \((\log2)^{-p}\le(\log2)^{-1}\). Each factor in the ratio of products satisfies
\[
 \frac{1+j/2}{1+je^{-v}}\le\frac{3}{2(1+e^{-v})}=\rho_v\quad(j\ge1).
\]
Hence the integral is strictly negative whenever \(p>C_{u,v}\rho_v^{n-3}\), so the \(\lambda\)-Fourier scalar is *positive* and CND fails. If \(p\ge1\), failure follows from the downward-closure of negative type once the bound is below one; a trivial bound from the \(S_3\) subgroup handles the other dimensions. The natural embeddings \(S_3\hookrightarrow S_n\) are isometric, giving \(\beta_n\le\beta_3\). As \(v\downarrow0\) with \(u=v/2\), \(\rho_v\downarrow3/4\), proving the limsup statement. No uniform finite constant in \(v\) is needed for this limit.

**4. Sharp small ranks.** Write \(x=2^p\), \(y=3^p\), \(z=4^p=x^2\). For \(S_3\), the nontrivial unnormalized Fourier character sums are \(-2x\) (degree two) and \(-3+2x\) (sign); the latter vanishes at \(x=3/2\). For \(S_4\), the nontrivial sums, ordered by partitions \((3,1),(2,2),(2,1,1),(1^4)\), are
\[
 6-3x-6y,\quad -2x,\quad -6-3x+6y,\quad -6+11x-6y.
\]
The third vanishes at a unique \(p\in(0,1/2)\), since \(3^p-1-2^{p-1}\) increases strictly, starts negative and is positive at \(p=1/2\). At equality, \(y=1+x/2\), so the sign sum is \(8x-12<0\); the other two are negative.

For \(S_5\), the six nontrivial unnormalized sums, ordered by partitions \((4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1^5)\), are
\[
 20+20x-20y-24z,\quad10-5x-10y,\quad-30x+24z,
\]
\[
 -10-5x+10y,\quad-20+20x+20y-24z,\quad-10+35x-50y+24z.
\]
Exact rational-root sign bounds establish that the last sum is negative at \(p=3/10\) and positive at \(p=8/25\). On this interval its derivative is strictly positive: using \(\log2>0.69\), \(\log3<1.1\), \(2^p>1.23\), \(4^p>1.51\), \(3^p<1.422\), the derivative exceeds \(0.69(35\cdot1.23+48\cdot1.51)-50(1.1)(1.422)>0\). Thus it has exactly one root \(\beta_5\) there. At this root \(1<x<5/4\) and \(x<y<z=x^2\). The first sum is at most \(20-24x^2<0\); the second is strictly negative; the third is \(6x(4x-5)<0\); the fourth is at most \(-10-5x+10x^2<0\); and the fifth is at most \(-20+20x-4x^2<0\). The last two elementary quadratic bounds are negative throughout \(1\le x\le5/4\). Hence all other Fourier blocks are strictly negative.

The usual snowflake closure of negative type (\(0<q<p\) preserves CND and makes it strict on distinct points) proves all smaller exponents. Immediately above each root, the indicated block becomes positive, and closure rules out *any* larger exponent. On the equality boundary, the only zero nontrivial block has Specht degree \(1,3,1\) respectively for \(n=3,4,5\). The centered squared-distance Gram matrix has rank \(n!-1-d_\lambda^2\), namely \(4,14,118\); strictly below it has rank \(n!-1\), namely \(5,23,119\). These ranks are the least Euclidean embedding dimensions by Schoenberg's construction.

## Verification
Run `python3 verify_roundness.py` with Python 3.11 or later. The checker reconstructs each symmetric-group irreducible character table via rim-hook removal, verifies character-column orthogonality, checks *all* nontrivial Fourier sums through \(S_5\), proves the \(S_5\) endpoint sign bracket using rational integer-power comparisons, and checks the positive derivative bracket. If NumPy is installed, it additionally constructs the complete \(120\times120\) distance matrix at the calculated \(S_5\) endpoint and independently checks its inertia. Recorded output: `ALL_CAYLEY_ROUNDNESS_CERTIFICATES_OK`. The infinite-family exponential comparison is the analytic argument above; no finite enumeration is asserted to prove it.

## Relationship to prior work
Lafont--Prassidis (first posted 2004-12-10) provides the generalized-roundness and negative-kernel perspective, but not these permutation-metric exponents. Ganesan (first posted 2014-04-27) studies the complete transposition graph's automorphisms, not negative type. Féray (first posted 2009-04-30) develops related Jucys--Murphy star-factorization methods; the group-algebra identity and content calculus are established tools, not claimed as new. The contribution assessed here is the **specific sign-changing hook-character obstruction with its exponential bound**, together with the sharp initial negative-type thresholds and embedding dimensions. A broader pre-existing theorem on conditionally negative definite central permutation kernels could subsume these conclusions and remains an originality risk.

## Limitations
The bound \(3/4\) concerns the limsup of the \(n\)-th root of the critical exponent; it is not a demonstrated optimal asymptotic. Exact values beyond \(n=5\) and a matching lower rate are not claimed. The historical comparison is bounded, and no independent mathematical validation is asserted. The numerical checker confirms finite tables and a low-dimensional endpoint, while the infinite-family conclusion relies on the written proof.

## References
- J.-F. Lafont and S. Prassidis, *Roundness properties of groups*, arXiv:math/0412219, first public 2004-12-10. https://arxiv.org/abs/math/0412219
- V. Féray, *Partial Jucys--Murphy elements and star factorizations*, arXiv:0904.4854, first public 2009-04-30. https://arxiv.org/abs/0904.4854
- A. Ganesan, *Automorphism group of the complete transposition graph*, arXiv:1404.7363, first public 2014-04-27. https://arxiv.org/abs/1404.7363
