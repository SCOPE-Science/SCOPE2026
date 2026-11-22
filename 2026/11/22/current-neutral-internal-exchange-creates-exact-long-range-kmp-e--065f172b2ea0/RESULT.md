# Current-neutral internal exchange creates exact long-range KMP energy covariance

## Finding
For every integer \(n\ge2\) and every internal redistribution rate \(v\ge0\), the two-reservoir complete-graph KMP process below has exactly
\[
\operatorname{Cov}(E_i,E_j)=\frac{v(T_+-T_-)^2}{2[(3n+1)v+12]},\qquad i\ne j.
\]
Although all internal links carry zero stationary *mean* energy current, strengthening them strictly increases every distinct-site energy covariance when the reservoirs have different temperatures. The signed plus-to-minus reservoir current remains \(n(T_+-T_-)/4\). For \(nv_n\to\lambda\in[0,\infty)\), the scaled covariance has the exact crossover \(\lambda(T_+-T_-)^2/[2(3\lambda+12)]\); for \(nv_n\to\infty\), it tends to \((T_+-T_-)^2/6\).

## Assumptions and scope
There are \(n\) labelled nonnegative interior energies \(E_1,\dots,E_n\). At rate \(v\) on every unordered pair, replace \((E_i,E_j)\) by \((U(E_i+E_j),(1-U)(E_i+E_j))\), with independent uniform \(U\in[0,1]\). Each interior vertex is connected separately to two infinite reservoirs of fixed temperatures \(T_+,T_->0\). A rate-one clock on each site–reservoir edge replaces \(E_i\) by \(U(E_i+H_\alpha)\), with \(H_\alpha\sim\operatorname{Exp}(\text{mean}\ T_\alpha)\), independent at every ring. Reservoir energy is freshly sampled; its output is not an additional dynamical site. This is the boundary-edge convention in De Masi–Ferrari–Gabrielli, not the independently refreshing boundary-site convention of the original chain. All Poisson clocks and split marks are independent. Observables refer to the unique stationary measure.

## Proof
Let \(c=(T_++T_-)/2\) and \(\Delta=T_+-T_-\). Permutation symmetry gives a common stationary first moment \(m\), diagonal second moment \(q\), and distinct-site moment \(z\). For a bath-edge update, \(\mathbb E[U]=1/2\), \(\mathbb E[U^2]=1/3\), and \(\mathbb E[H_\alpha^2]=2T_\alpha^2\); internal exchange has \(\mathbb E[U(1-U)]=1/6\). The stationarity equation for \(E_i\) is \(0=2(c-m)/2\), so \(m=c\).

The exact stationary second-moment equations, multiplying the diagonal equation by three and the off-diagonal equation by three, are
\[
0=-4q+4c^2+2(T_+^2+T_-^2)+(n-1)v(-q+2z),
\]
\[
0=6c^2-6z+v(q-2z).
\]
For the second equation, only the internal edge joining the selected pair contributes to its mixed-moment drift: interactions with third vertices have vanishing expectation by exchangeability. Solving these two equations gives
\[
q=2c^2+\frac{\Delta^2(v+3)}{(3n+1)v+12},\quad
z=c^2+\frac{\Delta^2v}{2[(3n+1)v+12]}.
\]
The denominator is strictly positive for all stated parameters, which proves the covariance formula including \(v=0\) and equilibrium \(\Delta=0\).

The mean energy increment at a rate-one site–plus-reservoir event is \((T_+-m)/2=\Delta/4\), while the minus reservoir has the opposite signed mean flux. Every interior edge has mean transfer \(v(\mathbb E E_i-\mathbb E E_j)/2=0\), proving the current statement. Direct differentiation of the covariance with respect to \(v\) yields \(6\Delta^2/[(3n+1)v+12]^2\), strictly positive for \(\Delta\ne0\). Rewriting \(n\operatorname{Cov}=\Delta^2(nv)/(2[(3+1/n)(nv)+12])\) gives both scaling limits. The standard boundary-driven KMP stationary existence and moment representation apply to this finite, reservoir-connected graph; equivalently, the present finite-moment drift system has a unique solution. No inference from a finite computational sample is needed.

## Verification
The independent standalone script `kmp_silent_checks.py` constructs the polynomial generator on every monomial of total degree at most two without invoking the reduced equations. For each \(n\in\{2,3,4,5\}\) and \(v\in\{0,1/3,2\}\), with \(T_+=3\), \(T_-=1\), it solves the full exact-rational linear system, checking all first moments, variances and off-diagonal covariances against the theorem. It reports `PASS: 12 exact independent generator systems, 144 exact moment equations; all moments and covariances agree.` The finite tests are corroboration, not proof of the quantified theorem.

## Relationship to prior work
Giardinà, Kurchan, Redig and Vafayi (arXiv:0810.1202, Section 6.3) establish the KMP thermalization connection and duality framework. De Masi, Ferrari and Gabrielli (arXiv:2310.01672, Section 2 and Theorem 2.3) define the boundary-edge version on arbitrary finite graphs and give a general stationary exponential-mixture representation. Their general representation does not itself tabulate the present two-reservoir, completely mixed finite-size covariance, the strict rate dependence, or the \(nv\) onset. Other previously examined KMP network covariance laws use different reservoir topology and/or site-refreshing boundary dynamics; their parameter formulas do not imply the present law. This is a specific exact evaluation within an established general model, not a claim to invent the KMP process or its moment closure.

## Limitations
Only stationary equal-time second moments and first-moment currents are determined; not temporal correlations, fluctuations of integrated current, large deviations, or a robustness theorem for heterogeneous internal edges. The claim assumes identical couplings to both reservoirs from each site, uniform internal complete-graph rates and the specified boundary-edge dynamics. Historical priority cannot be certified from literature search alone; an unindexed earlier equivalent exact evaluation remains possible.

## References
1. C. Giardinà, J. Kurchan, F. Redig, K. Vafayi, *Duality and hidden symmetries in interacting particle systems*, arXiv:0810.1202 (first public 2008-10-07), especially Section 6.3. https://arxiv.org/abs/0810.1202
2. A. De Masi, P. A. Ferrari, D. Gabrielli, *Hidden temperature in the KMP model*, arXiv:2310.01672 (2023), especially equations (2.1)–(2.3) and Theorem 2.3. https://arxiv.org/abs/2310.01672
3. C. Kipnis, C. Marchioro, E. Presutti, *Heat flow in an exactly solvable model*, Journal of Statistical Physics 27 (1982), 65–74, DOI:10.1007/BF01011740; foundational source (not asserted to contain the present network formula).
