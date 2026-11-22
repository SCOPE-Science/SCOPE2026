# Review: centered-clock Schatten expansion

## Correctness

**PASS.** The exact Dirichlet polynomial eigenspaces give eigenvalues \(\prod_{j<k}(n-j)/(n+A+j)\). Centering at \(N=n+A/2\) makes their logarithms a sum of odd powers; its first term is \(q_k=k(k+A-1)\), its third-order coefficient is the stated \(D_k\), and the remaining terms are nonnegative. For \(k\le n/2\), the fifth-order tail is bounded by \(C(k+1)^6/N^4\), which gives the fourth-order corrected remainder. For higher indices, the global bound by \(e^{-tq_k}\) supplies Gaussian tails, uniform Schatten estimates, and the exact first-order comparison for arbitrary fixed additive clocks. Finite exact Dirichlet-moment cross-checks and scalar residual tests corroborate constants; they are not substitutes for the analytic proof. All parameter and temporal boundaries appear explicitly in the finding.

## Originality

**PASS for the strict multivariate/general-time extension, with historical-priority qualification.** An earlier exact theorem for the unweighted interval already proves the optimal integer \(n+1\) clock, its positive trace-class second-order limit and uniqueness among integer offsets at \(t=1\). Those conclusions are not claimed to be original here. The genuinely broader claims address all simplex dimensions, arbitrary positive Dirichlet vectors, arbitrary positive times, every quasi-Schatten exponent, and an explicit fourth-order corrected remainder. The 2019 Altomare semigroup treatment gives approximation of the Jacobi diffusion by Durrmeyer iterates; the 2010 Abel–Berdysheva analysis supplies polynomial eigenstructures and fixed-operator expansions. Gonska–Heilmann–Raşa (2009) studies related semigroup approximation rates on \(C^2\) rather than all-Schatten sharp error coefficients. The closest published trace theorem for Dirichlet Bernstein–Durrmeyer operators studies fixed positive spectral exponents and growing-rank trace asymptotics, which does not imply the spectral powers growing linearly with \(n\). The multivariate all-ideal expansion and its general shape-dependent fourth-order remainder were not identified in the available full-text and index comparisons. An uninspected relevant older full text may conceal a related clock acceleration, so priority is qualified, not absolute.

## Mathematical value

**PASS as a nontrivial extension to Dirichlet simplices and full trace-ideal asymptotics.** The question is motivated by an established Jacobi-diffusion semigroup approximation problem. The theorem upgrades qualitative/first-order convergence to a sharp and uniform second-order trace-ideal limit with an actual fourth-order corrected remainder. The finite-rank scheme is simultaneously controlled in every \(\mathcal S_p\) quasi-norm, including the trace norm that measures total spectral error. The positive ordering and the uniqueness of the additive time correction supply a structural, reusable characterization rather than only a reparameterization of the one-dimensional statement: new spectral multiplicities and arbitrary Dirichlet shapes enter every leading trace-ideal coefficient.

## Sources and limitations

The principal antecedents include the previously derived one-dimensional unweighted time-one trace-class theorem (item 3ac17f17-da22-4174-b315-06b64e0ec105), Altomare (2019), Abel–Berdysheva (2010), and Gonska–Heilmann–Raşa (2009). Positive time and fixed dimension are essential for the all-Schatten statement; integer powers are available automatically when the centered clock is integral. The checker is finite and non-independent. The research index and accessible primary texts support originality only to the stated qualified degree.

Self-review: passed. Independent audit: not yet performed.
