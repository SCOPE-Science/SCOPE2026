# A complete refuge-protection staircase with baseline shelter under prey-to-cover mortality

## Finding

Consider \(n\ge2\) independent, otherwise identical habitat patches, each with an identical initial group of \(N>0\) exposed prey and pre-existing cover \(b\ge0\). An exactly divisible additional cover budget \(R>0\) is distributed as \(r_i\ge0\), \(\sum_{i=1}^n r_i=R\). During a fixed exposure duration \(T>0\), the per-prey mortality hazard in patch \(i\) is held at \(d_0+d_1N/(b+r_i)\), where \(d_0\ge0\) and \(d_1>0\). At zero total cover, survival is defined by the zero-cover limit. Consequently, the expected total survivors are
\[
N e^{-Td_0}\sum_{i=1}^n\exp\!\left(-\frac{a}{b+r_i}\right),\qquad a=Td_1N>0.
\]
For every parameter choice, each maximizing allocation assigns *the same strictly positive supplement* to exactly \(j\) patches and zero supplement to the others, for some \(j\in\{1,\ldots,n\}\). As predation severity \(\theta=a/R\) increases while baseline ratio \(\beta=b/R\) stays fixed, optimal support size passes, without skipping or reversing, through **every** size \(n,n-1,\ldots,1\). There are exactly \(n-1\) strictly ordered transition severities, each with a tie between precisely two consecutive support sizes; no unequal positive supplements or other ties optimize.

For \(\beta>0\), put
\[
Q_j(\theta,\beta)=j\left[\exp\!\left(-\frac{\theta}{\beta+1/j}\right)-\exp\!\left(-\frac{\theta}{\beta}\right)\right],\quad 1\le j\le n.
\]
The normalized optimal survivor count is \(n e^{-\theta/\beta}+\max_j Q_j\); for each \(1\le j<n\), the equation \(Q_j(\theta_j,\beta)=Q_{j+1}(\theta_j,\beta)\) has exactly one positive solution. These solutions satisfy
\[
0<\theta_{n-1}(\beta)<\cdots<\theta_2(\beta)<\theta_1(\beta).
\]
For \(\theta_{j}(\beta)<\theta<\theta_{j-1}(\beta)\), the unique optimal support size is \(j\), using \(\theta_n=0\) and \(\theta_0=+\infty\); at \(\theta_j\), precisely sizes \(j\) and \(j+1\) tie. At \(\beta=0\), the complete threshold formula is
\[
\boxed{\quad\theta_j(0)=\log\frac{j+1}{j},\qquad 1\le j<n.\quad}
\]
For every fixed \(j\), the positive-baseline threshold approaches this formula as \(\beta\downarrow0\).

A concrete example is four patches with \(\beta=1/2\). The transitions from four to three, three to two, and two to one protected patches occur respectively at approximately \(1.358513261\), \(1.496945596\), and \(1.828133590\). At \(\theta=1.6\) the strictly optimal allocation gives half the supplementary budget to each of two patches; the four possible active-set objective values \(n e^{-\theta/\beta}+Q_j\), in increasing support-size order, are approximately \(0.46644040,0.48531744,0.48058309,0.47376732\).

## Assumptions and scope

The hazard is an explicitly *exogenous, held-fixed* hazard during a one-exposure survival assay, evaluated at the common pre-exposure count \(N\). The theorem does **not** use the instantaneous changing number of survivors in the hazard, does not assert results for an endogenous mortality differential equation, and does not optimize long-term population growth. Patches have identical initial counts, baseline cover, hazard coefficients, and independent exposure; cover has no upper per-patch cap. Expected survivors add across patches, so independent survival events are not required for the expectation. Mortality of the form baseline plus prey-to-refuge ratio is motivated by the additive musical-chairs model of Samhouri et al. (2009). The fixed-exposure design and continuous divisible cover are mathematical modeling assumptions, not claims that this model is the empirically preferred mechanism. The factor \(N e^{-Td_0}\) does not influence the optimizer.

## Proof

**1. All positive supplementary allocations are equal at an optimum.** Define \(f_c(x)=e^{-c/x}\) for \(x>0\), extended by \(f_c(0)=0\). For any \(C,c>0\) consider \(F(x)=f_c(x)+f_c(C-x)\) on \([0,C]\). On the half interval \(0<x<C/2\), putting \(z=x/C\), direct comparison of the two derivatives \(f_c'(x)=c e^{-c/x}/x^2\) yields
\[
\operatorname{sgn} F'(x)=\operatorname{sgn}\left(H(z)-\frac cC\right),\quad
H(z)=\frac{2z(1-z)}{1-2z}\log\frac{1-z}{z}.
\]
Here \(H\) is strictly increasing from \(0\) to \(1\). Indeed, with \(y=(1-z)/z>1\), one has \(H=2y\log y/(y^2-1)\); its derivative in \(y\) has the sign of \((y^2-1)-(y^2+1)\log y<0\). The latter is negative because \(g(y)=\log y-(y^2-1)/(y^2+1)\) obeys \(g(1)=0\) and \(g'(y)=(y^2-1)^2/[y(y^2+1)^2]>0\). Consequently \(F\) first decreases and then increases on the left half if \(c/C<1\), or decreases throughout if \(c/C\ge1\). By symmetry, its global maxima on any symmetric closed interval around \(C/2\) occur only at the endpoints or at the midpoint, never at a strictly unequal interior pair.

Fix two positive supplementary cover amounts \(r_i,r_k>0\) in an alleged global optimum. Holding their sum \(s>0\) fixed, their total survivor contribution is \(F(x)\) for \(C=2b+s\) and \(x=b+r_i\) restricted to \([b,b+s]\). An unequal interior pair is strictly inferior to one of the equal pair or an allocation with at least one supplement zero, by the preceding lemma. Thus every global optimum has equal positive supplements. (Compactness of the budget simplex and continuity, including at zero cover, guarantee existence.)

**2. Reduce to the support-size candidates.** If precisely \(j\) patches receive supplements, they each receive \(R/j\); normalized expected survivors are \(n e^{-\theta/\beta}+Q_j(\theta,\beta)\) when \(\beta>0\). When \(\beta=0\), this reduces to \(Q_j(\theta,0)=j e^{-j\theta}\). The baseline term is independent of \(j\).

**3. Exactly one crossing per neighboring support size.** Fix \(\beta>0\), and write \(v=1/\beta\) and \(u_j=j/(1+\beta j)<v\), so \(u_{j+1}>u_j\). The integral identity
\[
Q_j=j\theta\int_{u_j}^v e^{-\theta t}\,dt
\]
shows that
\[
\frac{Q_{j+1}}{Q_j}=\frac{j+1}{j}\frac{\int_{u_{j+1}}^v e^{-\theta t}\,dt}{\int_{u_j}^v e^{-\theta t}\,dt}
\]
is strictly decreasing in \(\theta>0\). To see this, the ratio of integrals is the conditional probability that \(t\ge u_{j+1}\) under a density proportional to \(e^{-\theta t}\) on \([u_j,v]\); its \(\theta\)-derivative is minus the strictly positive covariance between \(t\) and this increasing nonconstant indicator. The ratio tends at \(\theta\downarrow0\) to \((j+1)(1+\beta j)/[j(1+\beta(j+1))]>1\) and tends to zero as \(\theta\to\infty\). There is therefore exactly one positive crossing \(\theta_j\); below it \(Q_{j+1}>Q_j\), and above it \(Q_j>Q_{j+1}\). For \(\beta=0\), the ratio is \(((j+1)/j)e^{-\theta}\) and the unique crossing is the displayed logarithmic threshold.

**4. Adjacent crossing implies a globally best neighboring pair.** Extend \(j\) to real \(x>0\), writing
\[
Q(x)=x\left(e^{-\theta x/(1+\beta x)}-e^{-\theta/\beta}\right).
\]
Set \(\lambda=\theta/\beta\), \(t=(1+\beta x)^{-1}\), and \(z=\lambda t\). Direct differentiation gives
\[
\operatorname{sgn}Q'(x)=\operatorname{sgn}\left[\frac1\lambda-L(z)\right],\qquad
L(z)=\frac{z-1+e^{-z}}{z^2}=\int_0^1(1-s)e^{-zs}\,ds.
\]
The function \(L\) strictly decreases from \(1/2\) to zero as \(z\) increases, and \(z\) strictly decreases as \(x\) increases. If \(\lambda\le2\), \(Q\) is strictly increasing. If \(\lambda>2\), \(Q\) increases strictly up to one unique maximum and then decreases strictly, because \(L(\lambda)<1/\lambda<L(0+)\). Thus the integer sequence \(Q_1,\ldots,Q_n\) is strictly unimodal, with at most a single adjacent tie at its summit: any equality \(Q_j=Q_{j+1}\) forces the unique continuous peak between those integers and makes both the *global* maximizing support sizes. In particular three support sizes cannot tie at once.

At \(\theta_j\), therefore, \(Q_{j+1}>Q_{j+2}\) whenever \(j+2\le n\). The strictly decreasing crossing ratio in Step 3 then forces \(\theta_{j+1}<\theta_j\). Chaining the strictly ordered adjacent comparisons proves the asserted complete staircase, including the absence of skipped supports. For \(\beta=0\), strict ordering of \(\log((j+1)/j)\) gives the same result. For fixed \(j\), \(Q_j(\theta,\beta)\to j e^{-j\theta}\) as \(\beta\downarrow0\) uniformly on compact positive \(\theta\)-intervals; uniqueness and opposite signs around its limit crossing give \(\theta_j(\beta)\to\log((j+1)/j)\).

## Verification

The self-contained Python standard-library program `check.py` tests, rather than replaces, the analytical proof. Its six named test groups cover exact rational ties at zero baseline, selected budget grids at zero baseline, seeded randomized **zero-baseline** allocations, the zero-baseline two-patch shape on many grids, zero-baseline behavior around transitions, and positive-baseline allocation grids. Its reported group counts are 1,632, 523,590, 56,000, 119,988, 552 and 614,215, totaling 1,315,977 counted checks. These are diagnostic counts (not a literal count of Python `assert` evaluations); in particular, the seeded random tests do not cover positive baseline. The all-parameter theorem rests on Steps 1–4. To reproduce the maximizing support at positive baseline, compute the finitely many \(Q_j\) from the displayed formula.

## Relationship to prior work

Samhouri et al. (2009) investigate mortality increasing with prey abundance per refuge in the empirical musical-chairs framework. Their additive candidate mortality function motivates the held-fixed ratio-hazard model here. Their field-fitting method integrates a mortality differential equation with changing abundance rather than holding the initial count fixed, and the inspected article does not optimize a fixed supplementary refuge budget across equal patches. Ford, Shima and Swearer (2016) report empirical interactions between shelter availability, conspecific density and juvenile mortality. The present result is a **conditional model theorem**, not an empirical endorsement of the additive hazard; the piecewise hazard was best supported in the Samhouri et al. comparison.

Classical separable S-shaped resource allocation is a genuine broader mathematical antecedent. Vicentini (1970) and Ginsberg (1974), the latter claiming a general identical-plants solution in its accessible abstract, may subsume the equal-positive-allocation reduction. They were not demonstrably available in full for comparison; thus such reductions are not claimed as new here. The claimed specific result is the **baseline-sensitive exponential-inverse-cover, strictly ordered, no-skipping staircase with unique integral-ratio crossings and the exact zero-baseline log thresholds**. A separate modern Hill-response allocation theorem and mathematical predator-intake patch-allocation result (links below) concern different functions and objectives, and do not directly imply these explicit bounds. An inaccessible earlier general result remains a material historical-priority risk.

## Limitations

The model assumes identical patches, fixed hazard at initial density, no recruitment or dynamics during the exposure, instantaneous allocation, continuously divisible cover, no cross-patch effect of supplemental cover, and an exactly fixed cover budget. Field response may be thresholded, time-varying, or affected by predator behavior and feedback; experimental parameter uncertainty and spatial access costs are ignored. No result is claimed for the nonlinear differential equation obtained by replacing fixed \(N\) with time-varying survivor density. The theorem is not a calibrated conservation recommendation. Novelty comparisons are best-of-knowledge rather than exhaustive.

## References

1. J. F. Samhouri, R. R. Vance, G. E. Forrester, and M. A. Steele (2009), *Musical chairs mortality functions: density-dependent deaths caused by competition for unguarded refuges*, Oecologia 160, 257–265, first online 2009-03-05, https://doi.org/10.1007/s00442-009-1307-z . Full online article inspected; includes the additive refuge-ratio hazard alternative.
2. J. R. Ford, J. S. Shima, and S. E. Swearer (2016), *Interactive effects of shelter and conspecific density shape mortality, growth, and condition in juvenile reef fish*, Ecology 97, 1373–1380, https://doi.org/10.1002/ecy.1436 . Full online article inspected.
3. F. M. Vicentini (1970), *On the Resource Allocation Problem with S-Shaped Utility Functions*, Technical Memorandum 201, https://commons.case.edu/wsom-ops-reports/370/ . Abstract available; complete report unavailable.
4. W. Ginsberg (1974), *The multiplant firm with increasing returns to scale*, Journal of Economic Theory 9, 283–292, https://doi.org/10.1016/0022-0531(74)90053-2 . Abstract available; full text not obtained.
5. *A complete active-target staircase for independent Hill inhibition under a shared dose budget*, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-a-complete-active-target-staircase-for-independent-hill-inhibiti--a81be9bbd6bd .
6. *Two sharp patch-allocation transitions for a generalized Type III feeding response*, https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-two-sharp-patch-allocation-transitions-for-a-generalized-type-ii--7d3ca49da7d6 .
7. *Sharp resource-allocation staircases under uniform patch dispersal*, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-resource-allocation-staircases-under-uniform-patch-dispers--5d8b1181bd2f .
