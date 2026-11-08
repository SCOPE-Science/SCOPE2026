# An arithmetic jump law for triangular-indicator jittered integration

## Finding
Consider independent uniform one-point-per-cell jittered integration of the sloping triangle \(T_\alpha=\{(x,y)\in[0,1]^2:0\le y<\alpha x\}\), for fixed \(0<\alpha\le1\). With \(n^2\) grid cells and estimator \(Q_{n,\alpha}\), the exact variance has a boundary-phase formula, and the limiting normalized variance
\[
C(\alpha)=\lim_{n\to\infty}n^3\operatorname{Var}(Q_{n,\alpha})
\]
exists for every slope, but is **discontinuous at every rational slope** and continuous at every irrational slope:
\[
C(\alpha)=\frac16+\frac{\alpha^2}{12}-\frac{\alpha^3}{60}+
\begin{cases}
\dfrac{1}{60ab^3},&\alpha=a/b\text{ reduced},\\
0,&\alpha\notin\mathbb Q.
\end{cases}
\]
Here \(a,b\) are positive integers with \(1\le a\le b\). Thus the rational orientation creates an exactly quantified lattice resonance in the root-mean-square error constant, even though the integral \(I(\alpha)=\alpha/2\) varies smoothly. The rational part alone, and the standard independent-cell variance identity, are not asserted as independently novel; the claim concerns their comparison with irrational slopes and the resulting all-real classification.

## Assumptions and scope
Let \(n\ge1\) be an integer. Partition \([0,1]^2\) into cells \(S_{ij}=[i/n,(i+1)/n)\times[j/n,(j+1)/n)\) for \(0\le i,j<n\). Draw \(U_{ij}\) mutually independently, each uniformly distributed in its cell, and set
\[
Q_{n,\alpha}=\frac1{n^2}\sum_{i,j=0}^{n-1}\mathbf1_{\{(x,y):y<\alpha x\}}(U_{ij}).
\]
Every result uses exact real arithmetic and the open sloped boundary is immaterial because the sampling laws are continuous. \(\mathbb E Q_{n,\alpha}=I(\alpha)=\alpha/2\). The slope is fixed as \(n\to\infty\), and is restricted to \(0<\alpha\le1\); rotating or changing the grid is not covered.

## Proof
**1. Exact cell law.** In local coordinates \(X=nx-i\), \(Y=ny-j\), the boundary is \(j+Y=\alpha(i+X)\). Write \(q_i=\{\alpha i\}\) and \(k_i=\lfloor\alpha i\rfloor\). Because \(0<\alpha\le1\), only row \(k_i\) and possibly row \(k_i+1\) in column \(i\) can have nontrivial Bernoulli variance. If \(q_i\le1-\alpha\), the crossing stays in the lower row, and its area fraction is \(p=q_i+\alpha/2\). If \(q_i>1-\alpha\), putting \(t=1-q_i\), the lower fraction is \(p_0=1-t^2/(2\alpha)\) and the upper fraction is \(p_1=(\alpha-t)^2/(2\alpha)\). All other cells have deterministic indicator. Define
\[
v_\alpha(q)=\begin{cases}
(q+\alpha/2)(1-q-\alpha/2),&0\le q\le1-\alpha,\\
\dfrac{(1-q)^2}{2\alpha}\left(1-\dfrac{(1-q)^2}{2\alpha}\right)
+\dfrac{(q+\alpha-1)^2}{2\alpha}\left(1-\dfrac{(q+\alpha-1)^2}{2\alpha}\right),&1-\alpha<q<1.
\end{cases}
\]
The two formulas agree at the branch join, and the right endpoint limit agrees with the value at zero; hence \(v_\alpha\) extends continuously and periodically. Independence gives the exact *finite-grid* identity
\[
\operatorname{Var}(Q_{n,\alpha})=\frac1{n^4}\sum_{i=0}^{n-1}v_\alpha(\{i\alpha\}). \tag{1}
\]
This identity is valid also for \(n=1\) and \(\alpha=1\).

**2. Irrational orientations.** For irrational \(\alpha\), the fractional-part rotation \(\{i\alpha\}\) is equidistributed in \([0,1)\): for each nonzero integer \(m\), the normalized geometric sum \(n^{-1}\sum_{i<n}e^{2\pi\mathrm{i}m i\alpha}\) tends to zero. By trigonometric polynomial approximation, the averages of the continuous periodic \(v_\alpha\) tend to its integral. Direct integration of its two polynomial branches yields
\[
\int_0^1v_\alpha(q)\,dq=\frac16+\frac{\alpha^2}{12}-\frac{\alpha^3}{60}.\tag{2}
\]
Combining (1)–(2) gives the irrational formula, and no finite enumeration is used to establish this infinite statement.

**3. Rational orientations.** Suppose \(\alpha=a/b\) with \(\gcd(a,b)=1\), \(1\le a\le b\). The phases \(\{i\alpha\}\) are periodic with minimal period \(b\), running once each through \(r/b\), \(0\le r<b\). Hence their mean tends to the period average, and when \(b\mid n\), it equals the mean *exactly*. With \(M=b-a\), the period sum is explicitly
\[
\frac1b\left[\sum_{r=0}^{M}\frac{r+a/2}{b}\left(1-\frac{r+a/2}{b}\right)
+\sum_{j=1}^{a-1}\left(\frac{j^2}{ab}-\frac{j^4}{2a^2b^2}\right)\right]. \tag{3}
\]
The second sum pairs the complementary cap sizes for the two crossing rows. Expanding the first sum and applying
\[
\sum_{r=0}^{M}r=\frac{M(M+1)}2,\quad
\sum_{r=0}^{M}r^2=\frac{M(M+1)(2M+1)}6,
\]
\[
\sum_{j=1}^{a-1}j^2=\frac{(a-1)a(2a-1)}6,\quad
\sum_{j=1}^{a-1}j^4=\frac{(a-1)a(2a-1)(3a^2-3a-1)}{30}
\]
reduces (3), without limits, to
\[
\frac16+\frac{a^2}{12b^2}-\frac{a^3}{60b^3}+\frac1{60ab^3}.\tag{4}
\]
The formulas include \(a=b=1\), for which the crossing is a cell diagonal and \(v_1(0)=1/4\).

**4. Continuity classification.** The smooth background \(g(\alpha)=1/6+\alpha^2/12-\alpha^3/60\) is continuous. Every reduced rational \(a/b\) has a positive spike \(1/(60ab^3)\); taking irrational slopes arbitrarily close to it yields the strictly smaller limiting value \(g(a/b)\). At an irrational slope, reduced rationals converging to it must have denominators \(b\to\infty\), so their spike magnitude is bounded by \(1/(60b^3)\to0\). Thus \(C\) is continuous at precisely the irrational slopes and discontinuous at every rational slope in the stated domain.

## Verification
Run `python3 verify.py` from the same directory. It executes 23,772 exact-rational assertions. The verifier independently clips the true half-plane against grid squares using polygon intersections and checks their Bernoulli probabilities against (1); it tests all reduced rational slopes up to denominator \(35\) against the period formula, multiple period lengths and boundary cases. The file `verification_output.txt` contains the replay output. A separate symbolic derivation with exact power sums checks the simplification of (3) to (4), shown explicitly above. Numerical tests illustrate the proof but do not certify the irrational limit or the all-integer identity.

At \(\alpha=1/2\), \(C=3/16\) whereas the local irrational limit is \(89/480\); the exact jump is \(1/480\). At \(\alpha=1\), \(C=1/4\) and the left-hand irrational limit is \(7/30\).

## Relationship to prior work
Doerr (2021) studies jittered sampling on equally sized cells and establishes sharp expected *star discrepancy* bounds for axis-aligned anchored boxes. Kiderlen and Pausinger (2021) establish discrepancy comparisons and existence of good general partitions. Neither of these primary statements gives the fixed slanted-triangle all-slope variance constant or the dense rational discontinuity. Ramamoorthi and collaborators (2012) analyze Monte Carlo sampling of binary visibility and the geometric relevance of edges versus sampling grids. Their relevant planar-light sections do not state the arithmetic resonance formula. Standard grid-cell variance identities and rational-slope occupancy calculations are prerequisites, not novel claims. The contribution isolated here is the orientation-classification theorem including irrational limits, endpoint comparison and sharp rational jump.

## Limitations
This result concerns one independent random point per square cell, one fixed triangular indicator, and \(0<\alpha\le1\). The limit is along integer grid refinements with the slope held fixed; convergence is not uniform in slope. The rational spikes can be small for large denominators and do not, by themselves, imply a material advantage in any specific application. It is a variance statement, not a distributional CLT, a star-discrepancy guarantee, or a general polygonal cubature theorem. Specialist prior publication precedence has not been independently certified; a previous restricted rational-slope formula is not counted as new.

## References
1. B. Doerr, *A Sharp Discrepancy Bound for Jittered Sampling*, arXiv:2103.15712, original version 29 March 2021, https://arxiv.org/abs/2103.15712 .
2. M. Kiderlen and F. Pausinger, *Discrepancy of stratified samples from partitions of the unit cube*, Monatshefte für Mathematik 195 (2021), https://doi.org/10.1007/s00605-021-01538-4 .
3. R. Ramamoorthi et al., *A Theory of Monte Carlo Visibility Sampling*, ACM Transactions on Graphics 31 (2012), article 121, https://cseweb.ucsd.edu/~viscomp/classes/cse168/sp26/readings/a121-ramamoorthi.pdf .
4. H. Weyl, classical equidistribution criterion (used for irrational rotations; an elementary geometric-series proof is supplied above).
