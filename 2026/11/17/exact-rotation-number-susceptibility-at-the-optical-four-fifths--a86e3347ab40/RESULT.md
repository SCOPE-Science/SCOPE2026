# Exact rotation-number susceptibility at the optical four-fifths resonance

## Finding

For the optical refraction piecewise-linear circle homeomorphism of Glendinning, Ma and Montaldi [1], fix \(\alpha=2\) and let \(\beta\) vary. At the natural conjugate-to-rigid-rotation point \(\beta_0=\sqrt5-1\), the rotation number of the continuously chosen lift has the exact two-sided derivative

\[\boxed{\rho(F_\beta)=\frac45-\frac{15+7\sqrt5}{100}(\beta-\beta_0)+o(|\beta-\beta_0|).}\]

The numerical coefficient is approximately \(-0.306524758424985\). The same calculation yields a five-way exact balance of the passage times through the intervals between points on the critical orbit: each contributes \(3-7\sqrt5/5\) to the signed reciprocal-drift integral. This balance makes the exact constant particularly simple despite the map's four unequal slopes.

## Assumptions and scope

Work with the circle \(\mathbb R/\mathbb Z\). Fix \(\alpha=2\) in the refraction map of [1, Section 10]. For \(\beta>1\) sufficiently close to \(\beta_0=\sqrt5-1\), write \(b=(\beta-1)/\beta\), and define the circle representative \(f_\beta:[0,1)\to[0,1)\) by

\[f_\beta(x)=\begin{cases}
\frac{x}{2}+\frac{\beta+1}{2\beta},&0\le x<b,\\
\frac{\beta x}{2}+\frac{1-\beta}{2},&b\le x<\frac12,\\
\beta(x-1)+\frac{2+\beta}{4},&\frac12\le x<\frac34,\\
\frac{2(x-1)}{\beta}+\frac{\beta+1}{2\beta},&\frac34\le x<1.
\end{cases}\]

The natural continuous lift is \(F_\beta(x)=f_\beta(x)+\mathbf1_{[b,1)}(x)\) for \(x\in[0,1)\), extended by \(F_\beta(x+k)=F_\beta(x)+k\) for integral \(k\). Define \(\rho(F_\beta)=\lim_{n\to\infty}(F_\beta^n(x)-x)/n\), independent of \(x\). The shift in the lift is fixed as \(\beta\) varies; a different lift would differ by an integer in rotation number, but would have the same derivative.

## Proof

**1. The critical identity and its five sectors.** Theorem 10.1 of [1] gives \(F_{\beta_0}^5(x)=x+4\) and \(\rho(F_{\beta_0})=4/5\). The orbit cuts in increasing order are

\[u_0=0,\quad u_1=\frac{3-\sqrt5}{4},\quad u_2=\frac12,\quad u_3=\frac34,\quad u_4=\frac{5+\sqrt5}{8},\quad u_5=1.\]

For the five open sectors \(I_j=(u_j,u_{j+1})\), numbered \(j=0,\ldots,4\), five-step branch itineraries (using the four branches numbered \(0,1,2,3\) in the displayed order) are

\[(0,3,3,2,1),\quad(1,0,3,3,2),\quad(2,1,0,3,3),\quad(3,2,1,0,3),\quad(3,3,2,1,0).\]

All five words have one occurrence each of branches \(0,1,2\) and two of branch \(3\), in cyclic order. Their product of spatial slopes is

\[\frac12\cdot\frac\beta2\cdot\beta\cdot\left(\frac2\beta\right)^2=1.\]

Consequently, for any fixed point in the interior of one sector and all sufficiently close \(\beta\), its fivefold lift displacement \(G_\beta(x)=F_\beta^5(x)-4-x\) is constant in \(x\) (not merely to first order).

**2. Exact differentiated drifts.** Differentiating each fivefold affine composition in \(\beta\) and then substituting \(\beta=\beta_0\) gives \(a_j=\partial_\beta G_\beta(x)|_{\beta_0}\), respectively

\[\begin{aligned}
a_0&=-\frac{5+3\sqrt5}{8},&a_1&=-\frac{5+2\sqrt5}{4},&a_2&=-\frac{15+7\sqrt5}{16},\\
a_3&=-\frac{5+2\sqrt5}{8},&a_4&=-\frac{5+3\sqrt5}{16}.
\end{aligned}\]

The five sector lengths are

\[(\ell_0,\ell_1,\ell_2,\ell_3,\ell_4)=\left(\frac{3-\sqrt5}{4},\frac{\sqrt5-1}{4},\frac14,\frac{\sqrt5-1}{8},\frac{3-\sqrt5}{8}\right).\]

Direct simplification using \((\sqrt5)^2=5\) gives the identity

\[\frac{\ell_j}{a_j}=3-\frac{7\sqrt5}{5}\qquad(0\le j\le4),\]

and hence the signed reciprocal-drift integral

\[\mathcal T=\int_0^1\frac{dx}{a(x)}=\sum_{j=0}^4\frac{\ell_j}{a_j}=15-7\sqrt5<0,\]

where \(a(x)=a_j\) on \(I_j\). This accounts for every component and includes the fifth, non-original break point \(u_4\).

**3. Passage-time limit.** Let \(\varepsilon=\beta-\beta_0\). On compact interior subintervals of \(I_j\), \(G_{\beta_0+\varepsilon}(x)=\varepsilon a_j+O(\varepsilon^2)\), uniformly. All five \(a_j\) are strictly negative. The exceptional neighborhoods where the branch itinerary changes have total length \(O(|\varepsilon|)\), since the finite collection of break points of \(F_\beta^5\) moves Lipschitzly with \(\beta\). Continuity and monotonicity of the lift imply the displacement there remains between negative multiples of \(\varepsilon\); hence each such neighborhood costs only \(O(1)\) return iterations. On a sector of fixed length \(\ell_j\), the number of fifth-return iterates needed to cross it is \(\ell_j/(|\varepsilon|\,|a_j|)+O(1)\), because each regular step is the exact sector translation \(\varepsilon a_j+O(\varepsilon^2)\). Thus a complete winding of the fifth-return map takes

\[N_\varepsilon=\frac1{|\varepsilon|}\sum_{j=0}^4\frac{\ell_j}{|a_j|}+O(1).\]

The same leading constant applies from either sign of \(\varepsilon\), with the orientation reversed. This elementary passage-time argument is also the constant-drift case of the rigorous perturbative rotation-number theorem [1, Theorem 2.6 and Lemmas 8.1–8.2]; the continuous-drift formulation is in [2]. Therefore

\[\rho(G_\beta)=\frac{\varepsilon}{\mathcal T}+o(|\varepsilon|).\]

Since \(G_\beta=F_\beta^5-4\), the lift identity gives \(\rho(F_\beta)=4/5+\rho(G_\beta)/5\). It follows that

\[\rho'(F_{\beta_0})=\frac1{5(15-7\sqrt5)}=-\frac{15+7\sqrt5}{100}.\]

This proves the asserted two-sided limit.

## Verification

Run `python verify.py` with Python 3 and SymPy. The checker independently composes the five itineraries symbolically, verifies unit spatial slopes, differentiates them in the parameter, and exactly checks the interval lengths, five equal passage times, and closed derivative. It reports `VERIFY_OK` on success. These algebraic checks certify the displayed symbolic identities conditional on the code's input map and itineraries; the passage-time argument establishes the limiting dynamical result for all sufficiently small real perturbations.

## Relationship to prior work

The refraction map, rational conjugacy point, general linear-scaling theorem, and the numerical slope regression are from Glendinning, Ma and Montaldi [1]. In its refraction example, [1] reports a regression slope near \(-0.312\) but explicitly leaves evaluation of its general derivative formula for this example undone. The separate general derivative theory of Glendinning [2] also covers such perturbations in principle, but neither inspected work states this five-sector constant or its exact crossing-time balance. This note supplies an exact evaluation for this natural optical one-parameter slice, not a new general rotation-number theorem.

## Limitations

Only the local \(\beta\)-derivative with \(\alpha\) fixed at \(2\) is claimed; holding \(\alpha/\beta\) fixed gives a different derivative. The five passage-time equalities are sectorwise at the conjugacy parameter and are not global finite-parameter equalities. No second-order coefficient, global parameter classification, or independent historical-priority certification is claimed. A related doctoral thesis may contain additional calculations not accessible for full comparison.

## References

[1] P. Glendinning, S. Ma and J. Montaldi, *Piecewise linear circle maps and conjugation to rigid rational rotations*, arXiv:2505.13689v1 (first public 19 May 2025), Section 10, Theorem 2.6 and Section 8; journal version, *Nonlinearity* **39** (2026), 035016. https://arxiv.org/html/2505.13689v1 ; https://doi.org/10.1088/1361-6544/ae49d2

[2] P. Glendinning, *Scaling of the rotation number for perturbations of rational rotations*, arXiv:2506.19508 (first public 24 June 2025), Sections 4–5. https://arxiv.org/html/2506.19508v2
