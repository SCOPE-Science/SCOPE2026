# A sharp biomass-gain threshold for lossy source-to-sink migration

## Finding
Consider logistic growth in one source and intrinsic decline in a connected sink, with mortality during migration in both directions. When the source-to-sink emigration rate is varied while return migration is held fixed, the total equilibrium abundance has precisely two possibilities: it decreases strictly at every rate, or it increases to one unique positive optimum and then decreases to extinction. The exact dividing criterion is
\[
 ah>b+v(1-hq).
\]
Here \(a\) is source intrinsic growth, \(b\) is sink intrinsic decline, \(v\) is the fixed sink-to-source migration rate, and \(h,q\) are the fractions surviving source-to-sink and return trips. In the gain regime the positive aggregate-abundance optimum is strictly invadable by a mutant with a lower emigration rate; the zero-emigration strategy instead resists every strictly positive-emigration mutant. Thus the exact population-abundance optimum and individual invasion resistance disagree on a nonempty, explicitly characterized parameter region. Qualitative differences between evolutionary and aggregate objectives, and intermediate-dispersal biomass gains, are already known; the contribution claimed here is the stated joint **lossy source–sink** phase classification and formula, not those general phenomena.

## Assumptions and scope
Fix \(a,b,v>0\), \(0<h,q<1\), and choose \(u\ge0\). For densities \(X,Y\ge0\) in a source and a sink respectively, set
\[
 \dot X=X(a-X)-uX+vqY,\qquad
 \dot Y=-Y(b+Y)-vY+huX.\tag{1}
\]
The source-to-sink movement attempts occur at per-capita rate \(u\) and survive with probability \(h\); sink-to-source attempts occur at fixed per-capita rate \(v\) and survive with probability \(q\). Individuals lost in transit do not enter either patch. The sink has negative intrinsic growth \(-b\) and is not a second positive-growth patch. Densities are in units giving unit quadratic competition in each patch, and total biomass means the physical total \(T=X+Y\), with no rescaling of sink occupancy.

Write \(w=b+v\), \(c=b+v(1-hq)=w-vhq>0\), and \(d=ah-c\). Define \(u_c=aw/c\). For every \(0<u<u_c\) the unique positive equilibrium is globally attractive among strictly positive states, and has a unique parametrization by \(r=Y/X\in(0,ah/c)\):
\[
 X(r)=\frac{ah-cr}{h+r^2},\qquad
 Y(r)=rX(r),\qquad
 u(r)=\frac{r(w+rX(r))}{h},\qquad
 T(r)=\frac{(1+r)(ah-cr)}{h+r^2}.\tag{2}
\]
The map \(r\mapsto u(r)\) is strictly increasing and maps this entire interval bijectively onto \((0,u_c)\). At \(u=0\), the attracting nonnegative equilibrium is \((a,0)\). At and above \(u_c\) all nonnegative trajectories approach extinction.

If \(d\le0\), then \(T(u)\) strictly decreases for \(0<u<u_c\), and \(u=0\) uniquely maximizes equilibrium aggregate abundance. If \(d>0\), then \(T(u)\) has exactly one interior maximizer \(u_*=u(r_*)\), where
\[
 r_* =\frac{hd}{h(a+c)+\sqrt{h^2(a+c)^2+hd^2}}.
\tag{3}
\]
In that case \(T(u)>a\) exactly for \(0<u<u(d/(a+c))\), and \(T(u)<a\) for \(u(d/(a+c))<u\le u_c\). Equality holds at both \(u=0\) and the positive gain boundary \(u(d/(a+c))\). The boundary values \(d=0\) and \(u=u_c\) are included in this statement.

For a rare mutant whose only changed trait is its source emigration rate \(\widehat u\ge0\), the per-capita invasion matrix in a resident environment \((X,Y)\) is
\[
 D(\widehat u)=\begin{pmatrix}a-X-\widehat u&vq\\h\widehat u&-b-v-Y\end{pmatrix}.\tag{4}
\]
At any positive resident equilibrium of \((1)\),
\[
 \det D(\widehat u)=(c+Y)(\widehat u-u).\tag{5}
\]
Consequently every strictly lower-emigration mutant invades a positive-emigration resident, whereas every strictly higher-emigration mutant has negative invasion growth. At the zero-emigration resident equilibrium, all positive-emigration mutants have negative invasion growth. These invasion claims concern the linear rare-mutant criterion, not long-term replacement or stochastic evolutionary outcomes.

## Proof
The equilibrium equations for \(X,Y>0\), divided by \(X\) and \(Y\), are \(a-X-u+vq(Y/X)=0\) and \(hu=(Y/X)(w+Y)\). Substituting \(r=Y/X\) gives \((h+r^2)X=ah-cr\), and thus exactly \((2)\). Positivity holds precisely when \(0<r<ah/c\).

Differentiate the unscaled relation \(hu=wr+r^2X(r)\). An exact cancellation yields
\[
 h(h+r^2)^2u'(r)=w(h+r^2)^2+2ah^2r-3chr^2-cr^4.
\]
Because \(ah>cr\) on the equilibrium interval, the right-hand side strictly exceeds
\[
 wh^2+(2w-c)hr^2+(w-c)r^4>0.
\]
The endpoint limits are \(u(0)=0\) and \(u(ah/c)=aw/c=u_c\), giving the claimed one-to-one parametrization.

For local existence and extinction, the linearization of \((1)\) at the origin is the irreducible Metzler matrix \(L(u)=\bigl(\begin{smallmatrix}a-u&vq\\hu&-w\end{smallmatrix}\bigr)\) when \(u>0\). Its determinant equals \(cu-aw\), and its second diagonal entry is negative. Thus its principal eigenvalue is positive precisely for \(u<u_c\), is zero at \(u=u_c\), and is negative for \(u>u_c\). If \(u\ge u_c\), multiplication by a positive left Perron eigenvector of \(L(u)\) yields \(\frac d{dt}(pX+q_0Y)=\lambda(pX+q_0Y)-pX^2-q_0Y^2\le0\); boundedness and the strict quadratic damping force convergence to the origin, including at criticality. Here \(p,q_0>0\) are arbitrary chosen left-Perron weights, not the survival parameter \(q\). For \(0<u<u_c\), positive initial conditions cannot converge to the origin: in a sufficiently small positive neighborhood their positive Perron-weighted sum increases. All positive trajectories are bounded by the logistic upper estimate on \(X+Y\). On the open quadrant, the Bendixson–Dulac multiplier \((XY)^{-1}\) has divergence
\[
 -1/Y-1/X-vq/X^2-hu/Y^2<0.
\]
There are no positive periodic orbits. The positive equilibrium from the injective parametrization is unique, and standard planar limit-set arguments now give its global attraction. At \(u=0\), the sink satisfies \(\dot Y=-Y(w+Y)\), while the source tends to \(a\) by asymptotically logistic growth with vanishing immigration.

Next, subtraction of the no-dispersal baseline yields the exact gain identity
\[
 T(r)-a=\frac{r[d-(a+c)r]}{h+r^2}.
\tag{6}
\]
Direct differentiation gives
\[
 T'(r)=\frac{N(r)}{(h+r^2)^2},\qquad N(r)=hd-2h(a+c)r-dr^2.
\tag{7}
\]
If \(d>0\), then \(N\) decreases strictly from a positive value at zero to a negative value at \(r=ah/c\), since \(T\) decreases through zero at that right endpoint. Its sole positive root is \((3)\). Formula \((6)\) gives the entire improvement interval and strict inequalities outside it. If \(d=0\), then \(N(r)=-2h(a+c)r<0\). If \(d<0\), \(N\) is convex and both endpoint values are strictly negative; therefore it remains negative throughout the closed interval. Monotonicity of \(u(r)\) transfers these conclusions to the management rate \(u\).

Finally, evaluating the determinant of \((4)\) at \(\widehat u=u\) gives zero because the resident equilibrium vector is a positive null eigenvector. Increasing \(\widehat u\) changes the determinant by \(w+Y-vqh=c+Y>0\) per unit increment, proving \((5)\). The other eigenvalue at equal traits is strictly negative because the trace equals \(-vq(Y/X)-w-Y<0\). Thus a strictly lower trait produces a negative determinant and a positive principal eigenvalue; a strictly higher trait produces positive determinant and strictly negative trace and hence two eigenvalues with negative real parts. At \(u=0\) the resident is \((a,0)\), giving \(\det D(\widehat u)=c\widehat u>0\) and \(\operatorname{tr}D(\widehat u)=-w-\widehat u<0\) for every \(\widehat u>0\).

## Verification
Run `python CHECK.py` with Python's standard library. It independently checks the exact equilibrium identities, gain identity, derivative signs, strict dispersal monotonicity lower bound, and invasion determinants at over 200 rational parameter tuples, plus three exact threshold examples. A finite sweep is evidence of consistent algebra, **not** a proof for every real parameter. The preceding symbolic proof supplies the universal quantifiers.

In an explicit rational example, \(a=4\), \(b=1/2\), \(v=1\), and \(h=q=3/4\). Then \(c=15/16\), \(d=33/16>0\), and \(u_c=32/5\). The unique optimum is \(r_*\approx0.197948831886174\), \(u_*\approx0.582216113146922\), with \(T_*\approx4.272179643843490\), versus \(T(0)=4\). At the boundary \(a=5/4\), holding the remaining parameters fixed, \(d=0\), so every positive dispersal rate reduces total biomass.

## Relationship to prior work
Wu (2016) develops a two-patch, two-direction travel-loss resident–mutant model with positive intrinsic patch growth rates; its equations (2.1)–(2.4), invasion matrix, and Theorems 1–2 provide a foundational precedent. Here the second intrinsic growth is strictly negative, and the **physical aggregate abundance** is optimized over the nonfixed direction. Wu's positive-ESS formula becomes inadmissible in this sink regime; the zero-dispersal invasion result itself should not be mistaken for the main novelty. Zhang and collaborators (2015) already demonstrate biomass gains at intermediate dispersal in heterogeneous, chiefly conservative systems. Shaw, Jalasvuori and Kokko (2014) discuss population-versus-evolutionary outcomes of risky dispersal. The complete source–sink asymmetry classifications of Wu and collaborators (2019/2020) and Elbetch (2024) are particularly close but describe conservative transfers without the two independent travel-survival factors of \((1)\). The exact new criterion depends on their product \(hq\), while the physical abundance includes the unscaled \(Y\); simply changing patch coordinates does not preserve both migration mass conservation and the objective. The combination of the precise lossy threshold, full single-peak formula and associated mutant-invasion comparison is the asserted contribution.

## Limitations
No independent historical-priority review has been performed. Full texts of some closely related conservative source–sink biomass papers and Galanthay (2015) were not available during the comparison; although their stated models differ, stronger generalized coverage remains a residual risk. The model assumes mass-action transfers, constant travel survivals, equal quadratic competition coefficients, two patches, a fixed reverse-flow rate, and a rare-mutant linear fitness criterion. It does not establish empirical policy benefits, evolutionary convergence, ecological resilience, or results for other nonlinear growth functions.

## References
- C.-H. Wu, *The optimal dispersal strategy: a two-patch model with travel loss*, Tamkang Journal of Mathematics 47 (2016), 27–38. DOI: https://doi.org/10.5556/j.tkjm.47.2016.1883. Full text: https://journals.math.tku.edu.tw/index.php/TKJM/article/download/27-38/979/5482.
- B. Zhang et al., *Effects of dispersal on total biomass in a patchy, heterogeneous system: Analysis and experiment*, Mathematical Biosciences 264 (2015), 54–62. DOI: https://doi.org/10.1016/j.mbs.2015.03.005.
- A. K. Shaw, M. Jalasvuori and H. Kokko, *Population-level consequences of risky dispersal*, Oikos (2014). DOI: https://doi.org/10.1111/oik.01229.
- T. E. Galanthay, *Mathematical study of the effects of travel costs on optimal dispersal in a two-patch model*, Discrete and Continuous Dynamical Systems B 20 (2015), 1625–1638. DOI: https://doi.org/10.3934/dcdsb.2015.20.1625.
- H. Wu, Y. Wang, Y. Li and D. L. DeAngelis, *Dispersal asymmetry in a two-patch system with source–sink populations*, Theoretical Population Biology 131 (2020), 54–65. DOI: https://doi.org/10.1016/j.tpb.2019.11.004.
- B. Elbetch, *Influence of Dispersal Asymmetry on Total Biomass in Two-Patch Environment with Generalized Growth Rate*, Journal of Optimization, Differential Equations and Their Applications 32 (2024), 16–40. DOI: https://doi.org/10.15421/142407.
