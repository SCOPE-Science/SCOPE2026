# Exact all-cutoff bounded-variation error of Walsh-Paley orthogonal projections

## Finding

Let \(\{w_k\}_{k\ge0}\) be the orthonormal Walsh system in **Paley (binary) order** on \([0,1)\), with \(w_0=1\), and let \(S_N\) be the \(L^2(0,1)\)-orthogonal projection onto \(\operatorname{span}\{w_0,\ldots,w_{N-1}\}\), for any integer \(N\ge1\). For every real \(f\in BV(0,1)\),

\[
\|f-S_Nf\|_{L^2(0,1)}\le \frac{\operatorname{TV}(f)}{2\sqrt N}.
\]

The constant is **sharp at every integer cutoff**, including non-powers of two. All nonconstant equality functions, modulo equality almost everywhere, are precisely \(f(x)=a+b\mathbf1_{[t,1)}(x)\) with real \(a\), nonzero real \(b\), and jump positions as follows. Write
\[
M=2^{\lfloor\log_2 N\rfloor},\qquad r=N-M,\qquad 0\le j<M.
\]
Then
\[
t=\frac jM+\frac1{2N}\quad\text{or}\quad t=\frac{j+1}{M}-\frac1{2N}.
\]
For \(N=M\), the two positions in each base cell coincide at its midpoint. In particular, the sharp error equals that of the orthogonal projector onto constants on **\(N\) equal intervals**, despite the very different shapes of non-dyadic Walsh projection kernels.

## Assumptions and scope

Functions are real-valued elements of distributional \(BV(0,1)\), identified almost everywhere, with ordinary (not circular) total variation \(\operatorname{TV}(f)=|Df|((0,1))\). No endpoint jump is included in this variation. The Hilbert space \(L^2(0,1)\) has unweighted Lebesgue probability measure. Each \(S_N\) includes the constant Walsh mode. The ordering is the Paley order, not Walsh-Kaczmarz or an arbitrary permutation. The rank \(N\) is any positive integer.

Put \(h=1/M\) and let \(H_t(x)=\mathbf1_{[t,1)}(x)\), with \(t=(j+q)/M\) and \(0\le q\le1\), where \(j\) indexes a dyadic level-\(\log_2M\) cell. A stronger exact jump-response identity is
\[
\|(I-S_N)H_t\|_2^2
=\frac1M\left[q(1-q)-\frac rM\min(q,1-q)^2\right].
\]
This identity provides both the norm and the equality characterization.

## Proof

**1. Orthogonal dyadic decomposition.** The first \(M\) Paley characters span all functions constant on the \(M\) dyadic cells \(I_j=[j/M,(j+1)/M)\). Therefore \(S_M\) is cellwise averaging. The within-cell variance of the jump \(H_t\), with jump fraction \(q\), is
\[
\|(I-S_M)H_t\|_2^2=\frac{q(1-q)}M.
\]
Let \(\rho_m(x)=(-1)^{\lfloor 2Mx\rfloor}\) be the next Rademacher function, which is \(+1\) on the first half and \(-1\) on the second half of each \(I_j\). The Paley product rule gives \(w_{M+k}=\rho_mw_k\) for \(0\le k<M\). In particular, \(S_N-S_M\) projects orthogonally onto \(\rho_mw_0,\ldots,\rho_mw_{r-1}\).

**2. Exact coefficient energy.** For each \(0\le k<r\), the lower-level character \(w_k\) is constant and of magnitude one on each \(I_j\). All complete cells contribute zero to the integral of \(H_t\rho_mw_k\), because \(\rho_m\) has zero cell mean. Within the partial cell,
\[
\left|\langle H_t,\rho_mw_k\rangle\right|
=\frac{\min(q,1-q)}M.
\]
Orthogonality removes exactly \(r\min(q,1-q)^2/M^2\) of the squared residual energy after \(S_M\), proving the stated jump-response identity. This calculation also holds for \(r=0\), when the sum is empty.

**3. Sharp global maximization.** The jump response is symmetric under \(q\mapsto1-q\). On \(0\le q\le1/2\), its bracket equals
\[
q-\left(1+\frac rM\right)q^2
=q-\frac NMq^2.
\]
Its unique maximizer on the left half is \(q_*=M/(2N)\), which belongs to \((1/4,1/2]\), and its maximum is \(M/(4N)\). The corresponding right-half maximum occurs at \(1-q_*\). Hence
\[
\sup_{0<t<1}\|(I-S_N)H_t\|_2^2=\frac1{4N},
\]
with exactly the jump positions specified above.

**4. From single jumps to all bounded-variation inputs.** The distributional derivative \(\mu=Df\) is a finite signed Borel measure on \((0,1)\), and up to a constant, \(f(x)=\int_{(0,1)}H_t(x)\,d\mu(t)\) for almost every \(x\). As \(S_N\) fixes constants, this identity passes through \(I-S_N\) as a Bochner integral in \(L^2\). The triangle inequality gives
\[
\|(I-S_N)f\|_2
\le\int\|(I-S_N)H_t\|_2\,d|\mu|(t)
\le\frac{|\mu|((0,1))}{2\sqrt N}.
\]
Each stated single jump attains equality.

**5. Rigidity of equality.** If equality holds and \(\mu\ne0\), then the strict jump-response bound away from its finitely many maximizers forces \(\mu\) to be supported on those maximizers. Equality in the Hilbert-space triangle inequality then forces every nonzero residual \((I-S_N)H_t\) in that support to be collinear up to a real scalar. This is impossible for two different maximizing positions: when \(r>0\), all such positions are strictly off the dyadic grid of length \(1/(2M)\), so \(H_t\) has a jump at \(t\) where every \(S_NH_u\) is locally constant; when \(r=0\), all maximizing positions are midpoints of the \(M\) cells, off the coarser grid on which \(S_MH_u\) can jump. If \((I-S_N)H_t\) and \((I-S_N)H_u\) were proportional, \(H_t-cH_u\) would lie in the finite Walsh space, contradicting the distinct non-grid jump(s). Thus \(\mu\) has exactly one atom, proving all equality cases.

The comparison with the \(N\)-equal-cell projector follows independently by computing the within-cell variance of a unit jump: the same maximization gives squared norm \(1/(4N)\), with a jump at the midpoint of an equal cell.

## Verification

`checker.py` independently integrates the first \(N\) Walsh coefficients of rationally placed unit jumps by exact rational arithmetic, subtracts their squared energy from the exact jump norm, checks the formula and global inequality, and verifies the predicted sharp jump positions. It also tests the bound on finite linear combinations of distinct jumps. Its self-contained run prints `PASS exact rational assertions: 1658` on the supplied version. These finite checks corroborate the algebra; the universal inequality and all equality cases are proved in the preceding argument, not inferred from enumeration.

To reproduce: run `python3 checker.py` from a directory containing the embedded file; no third-party dependencies are needed.

## Relationship to prior work

Fine's foundational treatment [1] establishes the Paley Walsh ordering, dyadic partial-sum cell averages, and a single-coefficient \(BV\) bound. Neither its coefficient-by-coefficient estimate nor the dyadic averaging identity determines the **simultaneous residual energy** for every non-dyadic cutoff. Móricz [2] studies convergence from variation conditions on the *coefficient sequence*, not the sharp \(BV\)-to-\(L^2\) operator error. Vyas and Darji [3] derive multivariate Walsh-coefficient magnitude estimates for generalized variation classes; their main theorem does not give the all-cutoff one-dimensional joint-tail constant or extremizer locations. The variation-norm Walsh partial-sum theorem [4] has a different input norm and output quantity. The present result concerns an exact, finite-cutoff approximation inequality and not an improvement of those papers' theorems.

## Limitations

The equality characterization concerns real inputs and ordinary interval variation. The result does not apply without additional analysis to Walsh systems in another order, periodic/circular variation, higher-dimensional rectangular cutoffs, weighted measures, nonlinear thresholding, or arbitrary orthogonal bases. It is not an assertion that Paley subspaces are globally optimal among **all** rank-\(N\) approximating subspaces. Historical-priority searches cannot exclude every unindexed equivalent, especially older dyadic approximation literature; one related coefficient article [5] was available only at abstract level.

## References

[1] N. J. Fine, *On the Walsh Functions*, Transactions of the American Mathematical Society **65** (1949), 372–414, https://webhomes.maths.ed.ac.uk/~v1ranick/papers/fine1.pdf. The paper reports presentation to the Society on 23 August 1946; this is the earliest day-specific public-disclosure evidence used for the archival context, not the date of the printed journal issue.

[2] F. Móricz, *Walsh-Fourier series with coefficients of generalized bounded variation*, Journal of the Australian Mathematical Society **47** (1989), 458–465, https://doi.org/10.1017/S144678870003319X.

[3] R. G. Vyas and K. N. Darji, *On multiple Walsh–Fourier coefficients of functions of \(\varphi\)-\(\Lambda\)-bounded variation*, Arabian Journal of Mathematics **5** (2016), 117–123, https://doi.org/10.1007/s40065-016-0145-1 (first published online 16 February 2016).

[4] T. P. Hytönen, M. T. Lacey, and I. Parissis, *A variation norm Carleson theorem for vector-valued Walsh-Fourier series*, arXiv:1209.3383v1 (15 September 2012), https://arxiv.org/abs/1209.3383.

[5] L. D. Gogoladze and V. Sh. Tsagareishvili, *The Fourier coefficients of functions with bounded variation*, Russian Mathematics **57** (2013), 10–19, https://doi.org/10.3103/S1066369X13080021; full text was not accessible in this review.
