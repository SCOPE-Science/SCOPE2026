# Complementary lures eliminate the rare-trappability tail at a sharp allocation budget

## Finding

A population with heterogeneous, persistent aversion to one trap lure can retain a polynomially decaying survivor fraction even under large trapping effort. A second lure whose individual hazard complements the first gives a sharp allocation law: beyond a finite threshold, extra effort is split equally while a *fixed absolute excess* on the initially favoured lure is maintained. The optimized survivor tail is exponentially small. The result is exact under the mathematical model below and does not claim that real lure attraction is literally complementary.

Let \(B>0\) be total normalized trap exposure and let \(P\) be an unknown but fixed, individual-specific preference with law \(\nu\) supported on \([0,1]\). If \(\nu([0,1/2))>0\) and \(\nu((1/2,1])>0\), define

\[
\Phi(z)=\mathbb E[e^{-z(P-1/2)}],\qquad
z_*:\ \mathbb E[(P-1/2)e^{-z_*(P-1/2)}]=0.
\]

There is exactly one such \(z_*\). The unique allocation maximizing expected fraction captured, equivalently minimizing expected surviving fraction, is

\[
\boxed{x_B=\frac{B+\operatorname{clip}(z_*,-B,B)}2,\qquad y_B=B-x_B.}
\]

When \(\mathbb E[P]\ne 1/2\), the threshold \(B_c=|z_*|>0\) exactly marks the first activation of the less favoured lure. For \(B>B_c\), the optimum satisfies \(x_B-y_B=z_*\), an invariant absolute effort difference despite increasing total exposure, and

\[
\min_{x+y=B}S_B(x,y)=\Phi(z_*)e^{-B/2}.
\]

Equal effort is independently the unique minimax strategy when the distribution of \(P\) is completely unknown on \([0,1]\), with optimal worst-case survivor fraction \(e^{-B/2}\). For \(P\sim\operatorname{Beta}(a,b)\), \(a,b>0\), survival under A-only and B-only efforts is respectively asymptotic to

\[
\frac{\Gamma(a+b)}{\Gamma(b)}B^{-a},\qquad
\frac{\Gamma(a+b)}{\Gamma(a)}B^{-b},
\]

whereas the optimized two-lure survival is eventually exactly \(\Phi(z_*)e^{-B/2}\). Thus the scheme changes the long-effort tail from polynomial to exponential for every positive beta parameter pair.

## Assumptions and scope

There is a closed, initially fixed population with no recruitment, immigration, mortality other than trapping, changing preference, or density dependence. Individuals have latent personal preferences \(P\in[0,1]\), possibly distributed arbitrarily. Given a preference, exposure \(x\ge0\) to lure A produces Poisson lethal encounters with integrated hazard \(Px\), while exposure \(y\ge0\) to lure B independently produces integrated hazard \((1-P)y\). Exposure is nonnegative and budgeted by \(x+y=B\); both intensities have the *same calibrated exposure units*. The order of exposures is immaterial conditional on the fixed trait. The initial law of preferences is unaffected by the decision except through survival selection. Results are about **expected surviving proportion**, not extinction probability with an uncertain count. The unique finite-threshold theorem assumes the trait law gives positive mass on both sides of \(1/2\). For a symmetric mean \(\mathbb E[P]=1/2\) with mass on both sides, \(z_*=0\) and an equal split is optimal for every positive budget.

## Proof

**1. Survival identity.** Conditional on \(P=p\), the no-capture probability is \(e^{-px-(1-p)y}\) by zero counts from the two independent Poisson encounter processes. Set \(z=x-y\). Since \(x+y=B\), direct algebra yields \(px+(1-p)y=B/2+z(p-1/2)\). Therefore

\[
S_B(x,y)=e^{-B/2}\Phi(z),\quad \Phi(z)=\int_0^1 e^{-z(p-1/2)}\,\nu(dp),\quad -B\le z\le B.
\]

**2. Unique unconstrained minimum and exact clipping.** Because \(|P-1/2|\le1/2\), differentiation under the integral is justified for every finite \(z\), giving

\[
\Phi'(z)=-\mathbb E[(P-1/2)e^{-z(P-1/2)}],\quad
\Phi''(z)=\mathbb E[(P-1/2)^2e^{-z(P-1/2)}]>0.
\]

The strict inequality holds by nonzero mass off the midpoint. The portions with \(P<1/2\) drive \(\Phi'(z)>0\) eventually as \(z\to+\infty\); those with \(P>1/2\) drive \(\Phi'(z)<0\) eventually as \(z\to-\infty\). To justify these signs without any density assumption, choose \(\epsilon>0\) with positive mass on \([0,1/2-\epsilon]\), respectively \([1/2+\epsilon,1]\); each exponentially growing contribution dominates the derivative contributions of the opposite sign, which are bounded or decay in that limit. Thus strict monotonicity of \(\Phi'\) gives its unique zero \(z_*\). Strict convexity on \([-B,B]\) then makes its minimum exactly \(\operatorname{clip}(z_*,-B,B)\), proving the allocation law.

**3. Sharp inclusion threshold.** Since \(\Phi'(0)=1/2-\mathbb E[P]\), strict monotonicity implies \(\operatorname{sgn}z_*=\operatorname{sgn}(\mathbb E[P]-1/2)\). When \(B<|z_*|\), clipping places all exposure on A if the mean exceeds one-half, otherwise on B. At equality the other exposure is still zero. When \(B>|z_*|\), the clipped difference equals \(z_*\) and both exposures are strictly positive. Hence the transition is sharp and the optimal difference freezes. The formula for minimum survival follows from step 1.

**4. Distribution-free minimax robustness.** For fixed \(x,y\), survival is maximized over all probability laws on \([0,1]\) by a point mass at whichever endpoint \(p=0\) or \(p=1\) yields the smaller hazard. Thus

\[
\sup_{\nu} S_B(x,y)=\exp[-\min(x,y)].
\]

For fixed \(x+y=B\), its unique minimizer is \(x=y=B/2\), and the worst-case survival is then exactly \(e^{-B/2}\). Thus balanced exposure is a robust guarantee, even though the Bayesian optimum may be unequal.

**5. Polynomial-to-exponential transition for beta preferences.** The beta density \(p^{a-1}(1-p)^{b-1}/\operatorname{B}(a,b)\) for \(a,b>0\) has positive probability on each side of one-half, ensuring finite \(z_*\). A-only survival is

\[
\frac1{\operatorname{B}(a,b)}\int_0^1 e^{-Bp}p^{a-1}(1-p)^{b-1}\,dp.
\]

Substitute \(u=Bp\), multiply by \(B^a\), and use a dominated-convergence splitting at \(p=1/2\): on the low half the factor \((1-p)^{b-1}\) is bounded and the integrable majorant is a multiple of \(e^{-u}u^{a-1}\); the high-half contribution vanishes exponentially even if the beta density diverges at one. The limit is \(\Gamma(a)/\operatorname{B}(a,b)=\Gamma(a+b)/\Gamma(b)\). By exchanging \(p\) with \(1-p\) the B-only constant is \(\Gamma(a+b)/\Gamma(a)\). Since \(B>|z_*|\) eventually, step 3 supplies the exact exponential optimum for all larger budgets.

**6. Explicit two-class certificate.** If \(P=1/4\) with probability \(1/3\), and \(P=3/4\) with probability \(2/3\), then \(\Phi(z)=e^{z/4}/3+2e^{-z/4}/3\); its derivative vanishes exactly when \(e^{z/2}=2\). Therefore \(z_*=2\log2\), \(B_c=2\log2\), and \(\Phi(z_*)=2\sqrt2/3\). For example, for \(B>2\log2\) the unique optimal exposures are \(x_B=B/2+\log2\) and \(y_B=B/2-\log2\), with survival exactly \((2\sqrt2/3)e^{-B/2}\).

## Verification

The included standalone Python script `verify.py` computes explicit survival functions, tests the two-class exact constants, numerically confirms clipped convex minima over many discrete preference laws and budgets, compares the beta \(\operatorname{Beta}(2,1)\) optimum against a grid, and checks the minimax endpoint bound. Its supplementary finite assertions passed when executed against the embedded source. The integral argument, strict convexity and beta endpoint asymptotic above—not the finite tests—establish the infinite-domain statements.

## Relationship to prior work

Johnstone, Garvey and Hickling (2023) provide evidence that successful kill-trapping selects harder-to-trap animals, motivating persistent trait heterogeneity and the survivor objective. Nguyen and colleagues (2024) study allocation among general and species-specific pest-surveillance tools, a different optimization involving species coverage and expected surveillance cost. Vattiato and colleagues (2024, first public release 28 November 2024) simulate combinations and switches of lures with *independently drawn* lure attraction probabilities, not the exact complementary preference constraint used here. Classical exponential-mixture frailty theory explains selection among survivors; it does not by itself supply the budget-clipping theorem, the minimax complement guarantee and the beta polynomial/exponential comparison. The mathematical novelty assessment is conditional on inspected sources and may require expanded historical bibliographic review.

## Limitations

Complementarity \(p+(1-p)=1\) is a strong stylized assumption, not an empirically estimated universal property. Hazard additivity and equal exposure units are essential. Trap avoidance may evolve, lures may interfere, trap numbers are discrete and populations reproduce or recolonize; none are in this model. Expected survivor fraction does not ensure finite-population eradication. The beta family is used as an exact mathematical heterogeneity class, not as a validated preference distribution. Numerical tests do not certify the universal theorem; independent external review has not occurred.

## References

1. Johnstone, K. C., Garvey, P., and Hickling, G. J. (2023). *Invasive mammal control selects for trap-recalcitrant behaviour and personality*. Biological Invasions. First publicly published 8 November 2023. https://doi.org/10.1007/s10530-023-03191-4
2. Nguyen, H.-T.-M., et al. (2024). *Optimal allocation of resources among general and species-specific tools for plant pest biosecurity surveillance*. Ecological Applications. First published 20 February 2024. https://doi.org/10.1002/eap.2955
3. Vattiato, G., et al. (2024). *Optimising Control Device Luring Strategies for Invasive Predator Control: A Modelling Approach*. Ecology and Evolution. First published 28 November 2024. https://doi.org/10.1002/ece3.70604
