# Sharp grazing ellipse and optimal drive balance at a neural-oscillator center

## Finding

For the two-neuron Matsuoka model at its nonswitching-center coupling threshold, the complete family of nonconstant periodic solutions that keep **both** neurons active is an explicitly bounded family of ellipses in a two-dimensional affine plane. The limiting ellipse is tangent to at least one firing threshold. Its enclosed area has an exact piecewise-quadratic dependence on the input ratio and is uniquely maximized by balancing that ratio against the square root of the coupling asymmetry.

In the notation established below, let
\[
R(r)=\frac{1}{K}\min\!\left\{p(r),\frac{q(r)}{\sigma}\right\},\qquad
K=\sqrt{\frac{b\tau_y}{\tau_x}},\quad
\omega=\sqrt{\frac{b-\tau_x/\tau_y}{\tau_x\tau_y}}.
\]
When \(r\) lies in the active-equilibrium interval, the center island in \((x_1,y_1)\) coordinates is exactly
\[
\mathcal E_r=\left\{(x_1,y_1):
(y_1-p)^2+\frac{(x_1-y_1)^2}{(\omega\tau_y)^2}
\le R(r)^2\right\},
\]
where \(p=p(r)\). Its area and unique maximizer, holding the couplings, time constants, feedback, and first input fixed, are
\[
\operatorname{area}(\mathcal E_r)
=\frac{\pi\omega\tau_y}{K^2}\min\!\left\{p(r),\frac{q(r)}{\sigma}\right\}^{\!2},
\qquad r_{\mathrm{opt}}=\sigma=\sqrt{\frac{a_{21}}{a_{12}}},
\]
\[
\max_r\operatorname{area}(\mathcal E_r)
=\frac{\pi\omega\tau_y s_1^2}{K^2(1+b+c)^2},
\quad c=\sqrt{a_{12}a_{21}}.
\]
Every nonconstant orbit in this island has the **same exact primitive period** \(2\pi/\omega\). The boundary ellipse touches both firing thresholds at two opposite phases when \(r=\sigma\); for an unbalanced input ratio it first grazes only the limiting threshold. The closed center island shrinks quadratically in area on approaching either end of the allowed input-ratio interval.

## Assumptions and scope

Consider the globally well-posed continuous piecewise-affine ODE
\[
\begin{aligned}
\tau_x\dot x_1&=-x_1-b y_1-a_{12}\max(x_2,0)+s_1,&
\tau_y\dot y_1&=-y_1+\max(x_1,0),\\
\tau_x\dot x_2&=-x_2-b y_2-a_{21}\max(x_1,0)+r s_1,&
\tau_y\dot y_2&=-y_2+\max(x_2,0).
\end{aligned}
\]
Assume \(\tau_x,\tau_y,b,s_1,a_{12},a_{21},r>0\), with fixed \(\tau_x,\tau_y,b,s_1,a_{12},a_{21}\) satisfying
\[
 c:=\sqrt{a_{12}a_{21}}=1+\frac{\tau_x}{\tau_y}<1+b
\qquad\bigl(\text{equivalently }b>\tau_x/\tau_y\bigr).
\]
Write
\[
\sigma=\sqrt{\frac{a_{21}}{a_{12}}},\qquad
\Delta=(1+b)^2-c^2>0,
\]
\[
p(r)=\frac{s_1(1+b-a_{12}r)}{\Delta},\qquad
q(r)=\frac{s_1((1+b)r-a_{21})}{\Delta}.
\]
The **closed fully active region** means \(x_1(t)\ge0\) and \(x_2(t)\ge0\) at every real time; equality at isolated tangencies is allowed. The center island is a set of initial states in its invariant two-dimensional affine plane, not a positive-four-dimensional-volume set. Its displayed area is the ordinary planar area in coordinates \((x_1,y_1)\). The induced intrinsic Euclidean two-area in four-dimensional state space equals \((1+\sigma^2)\operatorname{area}(\mathcal E_r)\).

## Proof

**1. The full active equilibrium and its feasible interval.** On \(x_1,x_2\ge0\), replace both rectifiers by the identity. Solving the four equilibrium equations gives \((p,p,q,q)\). Because \(\Delta>0\), the inequalities \(p>0\) and \(q>0\) are equivalent to
\[
\frac{a_{21}}{1+b}<r<\frac{1+b}{a_{12}}.
\tag{1}
\]
This interval contains \(\sigma\), since \(c<1+b\). Its endpoints are excluded when seeking nonconstant fully active periodic orbits.

**2. The exact center plane and oscillator.** The affine plane
\[
\mathcal P_r=\{(p+u,p+v,q-\sigma u,q-\sigma v):u,v\in\mathbb R\}
\]
is invariant for the full-active affine equations: use \(a_{12}\sigma=c\), \(a_{21}=c\sigma\), and the two equilibrium identities. On it the equations reduce exactly to
\[
\dot u=\frac{u}{\tau_y}-\frac b{\tau_x}v,
\qquad \dot v=\frac{u-v}{\tau_y}.
\]
Therefore \(\ddot v+\omega^2v=0\), where \(\omega>0\) has the value stated above, and \(u=v+\tau_y\dot v\). Thus for any \(\rho\ge0\) and phase \(\phi\),
\[
 v(t)=\rho\cos(\omega t+\phi),\qquad
 u(t)=\rho\bigl[\cos(\omega t+\phi)-\omega\tau_y\sin(\omega t+\phi)\bigr].
\]
In particular \(\max_t|u(t)|=K\rho\), with \(K^2=1+\omega^2\tau_y^2=b\tau_y/\tau_x\). The positive-firing requirements \(p+u(t)\ge0\) and \(q-\sigma u(t)\ge0\) for every time are therefore **equivalent** to
\[
\rho\le\frac{1}{K}\min\!\left\{p,\frac q\sigma\right\}=R(r).
\tag{2}
\]
Equality in (2) is permissible: the proposed explicit solution stays inside the closed region, and at contact the rectified right-hand side agrees with the full-active affine right-hand side. Local Lipschitz continuity guarantees that this is the solution of the original ODE, including at grazing instants.

**3. Exhaustiveness, not merely construction.** On the full-active affine system the characteristic polynomial factors into the two quadratics
\[
\left(\lambda^2+\frac{\tau_x+\tau_y+\tau_yc}{\tau_x\tau_y}\lambda+\frac{1+b+c}{\tau_x\tau_y}\right)
\left(\lambda^2+\omega^2\right).
\]
Both coefficients of the first quadratic are strictly positive, so both associated eigenvalues have negative real parts. Their stable generalized eigenspace complements the invariant center plane \(\mathcal P_r\). A solution periodic with positive period cannot have any nonzero component in a strictly stable generalized eigenspace, since the corresponding time-return operator has no eigenvalue one. Hence **every** nonconstant periodic solution that stays in the closed fully active region lies on \(\mathcal P_r\), and (2) is necessary as well as sufficient. If \(r\) is outside (1), then \(p\le0\) or \(q\le0\); a nonconstant sinusoidal excursion would make one firing coordinate negative at some phase. Therefore no nonconstant closed-fully-active periodic orbit exists for such \(r\). When (1) holds, all are the ellipses with \(0<\rho\le R(r)\), of primitive period \(2\pi/\omega\).

**4. Exact area and optimal input.** At time zero, write \(v=y_1-p\) and \(w=(x_1-y_1)/(\omega\tau_y)\). The ellipse condition becomes \(v^2+w^2\le R(r)^2\); the coordinate change to \((x_1,y_1)\) has absolute Jacobian \(\omega\tau_y\). Its area is therefore \(\pi\omega\tau_y R(r)^2\). The embedding \((u,v)\mapsto(u,v,-\sigma u,-\sigma v)\) has orthogonal columns of norm \(\sqrt{1+\sigma^2}\), giving the stated intrinsic area factor.

As \(r\) increases, \(p(r)\) decreases strictly and \(q(r)/\sigma\) increases strictly. They intersect precisely when \(r=\sigma\), where
\[
p(\sigma)=\frac{s_1}{1+b+c},\qquad
q(\sigma)=\frac{\sigma s_1}{1+b+c}.
\]
Hence their minimum, and thus the island area, has the **unique** maximum at \(r=\sigma\), with the asserted value. At the lower input endpoint \(q/\sigma\) vanishes linearly and at the upper endpoint \(p\) vanishes linearly, establishing the quadratic area collapse. At the optimum both constraints in (2) are tight and the limiting orbit touches the two switching boundaries at phases separated by half a period.

## Verification

The standalone script `verify.py` uses exact symbolic algebra to check the equilibrium identities, invariant-plane equations, frequency identity, and optimality intersection. Its separate rational parameter example is
\[
\tau_x=1,\quad \tau_y=4,\quad b=\tfrac12,\quad
(a_{12},a_{21})=(1,\tfrac{25}{16}),\quad s_1=1,\quad r=\tfrac54.
\]
Here \(c=\sigma=5/4\), \((p,q)=(4/11,5/11)\), \(\omega=1/4\), \(K=\sqrt2\), and the sharp radius is \(R=2\sqrt2/11\). The exact projected island area is \(8\pi/121\), its induced intrinsic two-area is \(41\pi/242\), and the common primitive period is \(8\pi\). The script substitutes the sinusoidal orbit into **all four** original equations and checks that both grazing amplitudes are exact. To reproduce: install SymPy and run `python verify.py` from the extracted files. Symbolic checks supplement, rather than replace, the all-parameter proof above.

## Relationship to prior work

Muramatsu and Kori, arXiv:2405.08409v1 (May 14, 2024), give the Matsuoka model, the full-active fixed point, the center threshold \(c=1+\tau_x/\tau_y\), the center eigenspace, and a qualitative description of an outermost grazing periodic orbit; their Section VI discusses limitations of harmonic-period approximation for asymmetric connections. **These facts are prior work, not claimed as new.** The present claim adds an exact characterization of *all* closed-fully-active periodic states, a sharp admissible amplitude and ellipse area for each input ratio, and a unique optimal input-balance ratio together with the simultaneous-grazing property. The examined primary preprint, including its appendix, does not state these quantitative area-and-optimization results.

Matsuoka (2011) reports closed-form **approximate** frequency and amplitude relations based on rough linearization, according to the accessible abstract. This is a relevant antecedent, but the complete paper was not accessible for a decisive whole-document comparison. General facts about planar linear centers explain ellipticity but do not supply the input-dependent sharp grazing threshold and its optimal balance without applying the switching constraints in this particular network.

## Limitations

The claim is confined to the stated critical coupling surface and to periodic orbits whose two membrane potentials remain nonnegative for **all** times. It says nothing about periodic orbits that pass through inactive firing regions, global attractor basins, robustness to parameter noise, or the persistence of neutral periodic families off criticality. The optimization holds at fixed first input \(s_1\), not at fixed total drive \(s_1+s_2\). The two-dimensional area is coordinate-dependent; both projected and intrinsic-area normalizations are stated explicitly. Priority relative to unavailable historical full texts remains uncertain. Neither independent publication priority nor independent mathematical validation is asserted.

## References

1. K. Muramatsu and H. Kori, *Bifurcation analysis of a two-neuron central pattern generator model for both oscillatory and convergent neuronal activities*, arXiv:2405.08409v1, 14 May 2024. https://arxiv.org/html/2405.08409v1
2. K. Matsuoka, *Analysis of a neural oscillator*, Biological Cybernetics 104, 297–304 (2011), DOI:10.1007/s00422-011-0432-z; accessible abstract: https://pubmed.ncbi.nlm.nih.gov/21562853/
3. J. M. Gonçalves, *Regions of stability for limit cycle oscillations in piecewise linear systems*, IEEE Transactions on Automatic Control 50, 1877–1882 (2005), DOI:10.1109/TAC.2005.858674.
