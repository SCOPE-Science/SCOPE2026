# A singular rate–energy crossover and uniform predator-log occupation in Lotka–Volterra cycles

## Finding
Consider the normalized Lotka–Volterra system
\[
\dot u=\lambda u(1-v),\qquad \dot v=\lambda^{-1}v(u-1),\qquad u,v>0.
\]
Define \(f(z)=e^z-z-1\) and the conserved energy
\[
E=\lambda^{-1}f(\log u)+\lambda f(\log v)>0.
\]
Fix a finite constant \(c>0\) and impose the **simultaneous scaling** \(\lambda=cE\) as \(E\to\infty\). Define the unique roots \(y_-(c)<0<y_+(c)\) of \(f(y)=1/c\), and let \(Z_c\) be uniform on the closed interval \([y_-(c),y_+(c)]\). For the least period \(T_c(E)\) in the displayed original time, the sharp leading coefficient and an absolute error bound are
\[
T_c(E)=cE\bigl[y_+(c)-y_-(c)\bigr]
 +O_c\!\left(\frac{\log E}{E}\right).
\]
For normalized original-time occupation \(\mu_{c,E}\) of the rescaled pair \((-\log u/(cE^2),\log v)\), the limiting joint law is the non-linear **fold curve**
\[
 W_1\left(\mu_{c,E},\mathcal L(1-c f(Z_c),Z_c)\right)
 =O_c\!\left(\frac{\log E}{E^2}\right).
\]
Here \(W_1\) uses the \(\ell^1\) metric in \(\mathbb R^2\). In particular, the predator-log coordinate becomes uniform across a nontrivial finite interval, whereas the scaled negative prey-log coordinate becomes its explicit non-linear function. The proportion of the period with \(u>1\) is \(O_c(\log E/E^2)\).

## Assumptions and scope
The number \(c>0\) is fixed as \(E\to\infty\), and \(\lambda=cE\) varies with energy. For each \(E>0\) the initial point is an arbitrary point of the corresponding strictly positive compact energy oval; the time-average probability law is independent of the initial phase. The equilibrium \((1,1)\), which has energy zero, is excluded. All time units are those of the displayed normalized original system; no reparametrized angular time is used. Error constants depend on fixed \(c\), not on the initial phase or energy.

This regime is distinct from taking \(E\to\infty\) at fixed \(\lambda\): fixing \(c\) forces the predator logarithm to have an order-one limiting excursion and produces the curved joint limit above.

## Proof
**1. Hamiltonian and two inverse branches.** Set \(x=\log u\), \(y=\log v\). The equations become \(\dot x=-\lambda(e^y-1)\), \(\dot y=\lambda^{-1}(e^x-1)\), with the stated conserved \(E\). Since \(f\) is strictly convex, nonnegative, diverges at both infinities and has a unique minimum at zero, every \(E>0\) level is a smooth compact regular oval with no stationary point, hence a periodic orbit. For \(h>0\), let \(s_-(h)<0<s_+(h)\) be the two solutions of \(f(s)=h\). Differentiating the inverse equations gives the positive time-density functions
\[
 d_-(h)=\frac{1}{1-e^{s_-(h)}},\qquad
 d_+(h)=\frac{1}{e^{s_+(h)}-1}.
\]
The identity \(f(s_-(h))=h\) also gives
\[
 s_-(h)=-h-1+e^{s_-(h)},\qquad
 0\le-s_-(h)-h\le1.
\]

**2. Exact original-time branch disintegration.** Write \(\lambda=cE\), \(M=\lambda E=cE^2\), and \(g(y)=1-cf(y)\). The permissible interval for \(y\) is \([y_-(c),y_+(c)]\), and the energy equation becomes \(f(x)=Mg(y)\). Its two branches are \(x=s_\pm(Mg(y))\). Since \(\dot y=\lambda^{-1}(e^x-1)\), each branch traverses this entire \(y\)-interval once per orbit, with its exact positive-time element
\[
  dt_-=\lambda d_-(Mg(y))\,|dy|,\qquad
  dt_+=\lambda d_+(Mg(y))\,|dy|.
\]
Here the subscripts indicate respectively \(x<0\) and \(x>0\). Consequently, for any bounded Borel test function \(\Phi\), the time integral is exactly
\[
 \int_0^{T_c(E)}\!\Phi\!\left(-\frac{x(t)}M,y(t)\right)dt
 =\lambda\int_{y_-}^{y_+}\!\sum_{\sigma\in\{-,+\}}d_\sigma(Mg(y))
 \Phi\!\left(-\frac{s_\sigma(Mg(y))}M,y\right)dy.
\]
All inverse-branch endpoint singularities in this formula are integrable.

**3. Uniform estimate at the two turning points.** The function \(g\) vanishes simply at both endpoints because \(g'(y_\pm)=-cf'(y_\pm)\ne0\); it is positive in the open interval. Local inversion at the nondegenerate minimum of \(f\) implies
\[
 d_-(h)-1=O(h^{-1/2}),\quad d_+(h)=O(h^{-1/2})\quad(h\downarrow0).
\]
At infinity \(s_-(h)\le-h\), so \(d_-(h)-1=O(e^{-h})\), whereas \(s_+(h)=\log h+O(\log h/h)\), so \(d_+(h)=O(1/h)\). Splitting the fixed \(y\)-interval into two neighborhoods where \(g(y)\) is comparable to the distance from the nearest endpoint, and a compact interior with \(g\ge\eta>0\), gives the explicit integral estimates
\[
 \int_{y_-}^{y_+}\bigl(d_-(Mg(y))-1\bigr)dy=O_c(M^{-1}),
\]
\[
 \int_{y_-}^{y_+}d_+(Mg(y))dy=O_c\!\left(\frac{\log M}{M}\right).
\]
For example, near each endpoint substitute \(z=Mg(y)\), using the inverse function theorem and \(|dy/dz|\le C_c/M\); integrability at zero and the respective exponentially decaying and reciprocal tails yield the displayed bounds. The compact interior contributes exponentially little to the first integral and \(O_c(M^{-1})\) to the second. These estimates are uniform over the entire orbit.

**4. Period and positive-prey time.** Put \(L_c=y_+(c)-y_-(c)>0\). Applying step 3 to the branch time formula yields
\[
 \frac{T_c(E)}{\lambda}=L_c+O_c\!\left(\frac{\log M}{M}\right).
\]
As \(\lambda=cE\) and \(M=cE^2\), this is precisely the asserted period expansion, with absolute remainder \(O_c(\log E/E)\). The \(x>0\) branch occupies time \(\lambda O_c(\log M/M)\), so its relative time is \(O_c(\log E/E^2)\).

**5. Joint time law with a quantitative transport bound.** For the negative branch, the exact identity in step 1 gives, uniformly in \(y\),
\[
 \left|-\frac{s_-(Mg(y))}{M}-g(y)\right|\le M^{-1}.
\]
Its original-time density in \(y\), after normalization by \(T_c(E)\), differs in total variation from the uniform density \(L_c^{-1}\) by \(O_c(\log M/M)\), using step 3 and the small positive-branch mass. On the positive branch, \(-s_+(Mg(y))/M\) lies in a uniformly bounded interval; its total mass is \(O_c(\log M/M)\). The second coordinate \(y\) remains in the fixed compact interval. Couple the dominant branch to a uniform \(Z_c\), paying at most \(M^{-1}\) in first-coordinate displacement on the matched part, and couple unmatched mass at uniformly bounded cost. This yields \(W_1=O_c(\log M/M)=O_c(\log E/E^2)\), as claimed. No numerical or finite-state approximation enters these infinite-energy bounds.

## Verification
The supplied `check_lv_crossover.py` independently reconstructs the two inverse branches, integrates their exact physical-time densities for three distinct values of \(c\) and three energies, and compares the period, positive-branch share and both first-coordinate means with the claimed limiting expressions. It emits `RARE_RATE_LOTKA_VOLTERRA_CROSSOVER_CHECK_OK` upon successful finite checks. The proof's reciprocal-tail, exponential-tail, simple-root and coupling estimates establish the theorem; numerical agreement alone would not.

## Relationship to prior work
Boulnois (arXiv:2301.00673, 2022) establishes the normalized equations, Hamiltonian reduction and an exact period quadrature, treating high-energy asymptotics primarily at a fixed coupling ratio; the expanded 2023 treatment and a 2026 follow-up examine fixed or moderate \(\lambda\), with the latter noting a practical \(\lambda\lesssim5\) approximation range. Earlier Waldvogel, Rothe, Shih and Grasman–Veling works provide period quadratures or asymptotics; the exact periodic integral itself is not new. A separate 2026 mathematical result, *Dual high-energy occupation laws and beta reaction-flux moments for the classical Lotka–Volterra oscillator*, treats only the symmetric **fixed** \(\lambda=1\) model, with a different limiting segment and no singular joint rate–energy scaling. The new claim is specifically the **finite-\(c\) double-scaling limit with a nondegenerate, uniform predator-log law, curved joint support, explicit new period coefficient and quantitative transport rate**; these do not follow from fixed-parameter asymptotics without uniform estimates in the diverging coupling.

## Limitations
The theorem is deterministic, confined to positive periodic orbits, and holds for each fixed \(c\in(0,\infty)\); no uniform constants as \(c\downarrow0\) or \(c\uparrow\infty\) are claimed. A different clock scaling changes the period coefficient. Population randomness, finite carrying capacities and stochastic extinction are not addressed. The published literature's full set of derivable consequences is difficult to exclude; exact period quadratures could be asymptotically reworked to recover part of this result. A relevant older asymptotic article could be accessed only through its abstract; its full text remains a publication-priority risk. Independent mathematical audit has not been performed.

## References
1. J.-L. Boulnois, *Predator-Prey Linear Coupling with Hybrid Species*, arXiv:2301.00673 (first public 2022-12-29), https://arxiv.org/abs/2301.00673 .
2. J.-L. Boulnois, *Hybrid Species and Closed-Form Solutions of the Lotka–Volterra Equations*, *American Journal of Biomedical Science & Research* **18** (2023), 501–513, https://doi.org/10.34297/AJBSR.2023.18.002503 .
3. J.-L. Boulnois, *On Hybrid-Function Solutions of the Lotka–Volterra Equations*, *Mathematics* **14** (2026), 3162, https://doi.org/10.3390/math14173162 .
4. S.-D. Shih, *The Period of a Lotka–Volterra System*, *Taiwanese Journal of Mathematics* **1** (1997), 451–470, https://doi.org/10.11650/twjm/1500406122 .
5. F. Rothe, *The Periods of the Volterra–Lotka System*, *Journal für die reine und angewandte Mathematik* **355** (1985), 129–138, https://doi.org/10.1515/crll.1985.355.129 .
6. J. Waldvogel, *The Period in the Volterra–Lotka Predator–Prey Model*, *SIAM Journal on Numerical Analysis* **20** (1983), 1264–1272, https://doi.org/10.1137/0720098 .
7. J. Grasman and E. J. M. Veling, *An Asymptotic Formula for the Period of a Volterra–Lotka System*, *Mathematical Biosciences* **18** (1973), 185–189, https://doi.org/10.1016/0025-5564(73)90029-1 .
