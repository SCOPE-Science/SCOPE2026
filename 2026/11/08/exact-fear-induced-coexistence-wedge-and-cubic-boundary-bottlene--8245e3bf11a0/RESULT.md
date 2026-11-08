# Exact fear-induced coexistence wedge and cubic boundary bottleneck

## Finding
Consider the positive-parameter, two-competitor fear system
\[
\dot u=u(a_1-b_1u-c_1v),\qquad
\dot v=v\left(\frac{a_2}{1+ku}-b_2v-c_2u\right).
\]
Put \(U=a_1/b_1\) and \(c=c_1/b_1\). Whenever \(a_2>c_2U\), define
\[
k_c=\frac{a_2/(c_2U)-1}{U}>0,\qquad
b_*=c\left(c_2+\frac{a_2k_c}{(1+k_cU)^2}\right)>0.
\]
At \((k,b_2)=(k_c,b_*)\), the positive center direction at the boundary equilibrium \((U,0)\) has the **strictly repelling cubic normal form**
\[
\dot v=C_*v^3+O(v^4),\quad
C_*=\frac{a_2k_c^2c^2}{(1+k_cU)^3}>0.
\]
For every \(b_2>b_*\) with \(k=k_c\), this boundary state is locally attracting from the positive quadrant, and all sufficiently close strictly positive initial states satisfy
\[
\lim_{t\to\infty}t v(t)=\frac1{b_2-b_*},\qquad
\lim_{t\to\infty}t(U-u(t))=\frac{c}{b_2-b_*}.
\]

For the natural integer-calibrated slice \(a_1=b_1=c_1=c_2=1\), \(a_2=2\), \(3/2<b=b_2<2\), there is additionally an exact **complete positive-equilibrium phase diagram** as the fear coefficient \(k>0\) varies. Write \(\tau=b-1\) and
\[
k_f(b)=\frac{2\tau}{\left(2-\sqrt{2(1-\tau)}\right)^2}\in(1/2,1).
\]
There are no positive coexistence equilibria for \(k<k_f(b)\), exactly one double positive equilibrium at \(k=k_f(b)\), two positive equilibria (a sink at smaller \(v\) and a saddle at larger \(v\)) for \(k_f(b)<k<1\), and one positive saddle for \(k\geq1\). At \(k=1\) the other root has merged into the \(v=0\) boundary and this boundary is locally attracting from the positive quadrant; at \(k>1\) the boundary is hyperbolically attracting. The \(u=0\) boundary equilibrium \((0,2/b)\) is hyperbolically attracting throughout.

The fold and boundary-invasion curves have a **quadratic tangency** as \(b\downarrow3/2\):
\[
k_f(3/2+\eta)=1-2\eta^2+2\eta^3+O(\eta^4),\qquad \eta\downarrow0.
\]
The limiting double-degeneracy is \((b,k)=(3/2,1)\), where the center-normal-form cubic coefficient is exactly \(1/4\). The result is a **local dynamical theorem** and an exact equilibrium census; it does not assert global basins at every parameter value.

## Assumptions and scope
All biological growth, competition, and fear coefficients in the general model are strictly positive; the restricted equilibrium \(u=U\) exists in the positive boundary. The additional assumption \(a_2>c_2U\) makes \(k_c\) strictly positive. Solutions start in the nonnegative quadrant, an invariant region for this smooth model. The center-manifold claims are local near \((U,0)\). The full positive-equilibrium census is for the explicitly normalized two-parameter subfamily \(3/2<b<2\), \(k>0\), with coexistence meaning \(u>0\) and \(v>0\). No claim is made about persistence under arbitrary structural modifications, spatial diffusion, noise, or all global attraction basins.

## Proof
**1. Nullcline and center degeneration for general parameters.** The positive \(u\)-nullcline is the line \(u=U-cv\), \(0<v<U/c\). On that line, the other per-capita growth rate is
\[
H(v)=\frac{a_2}{1+k(U-cv)}-c_2(U-cv)-b_2v.
\]
At \(k=k_c\), \(H(0)=0\). At \(b_2=b_*\), also \(H'(0)=0\), and direct differentiation yields
\[
H''(0)=\frac{2a_2k_c^2c^2}{(1+k_cU)^3}>0.
\]
At the boundary equilibrium the Jacobian eigenvalues are \(-a_1\) and zero, and the center eigendirection is \((-c,1)\). Write a center manifold as \(u=U-cv+\beta v^2+O(v^3)\). The invariance equation compares \(u'=-b_1u\beta v^2+O(v^3)\) with the left side \((-c+O(v))v'=O(v^3)\), forcing \(\beta=0\). Therefore on the center manifold \(v'=v[H(v)+O(v^3)]=C_*v^3+O(v^4)\). Since \(C_*>0\), all sufficiently small center-manifold points with \(v>0\) move away from the boundary equilibrium; the stable eigendirection is precisely the invariant \(v=0\) axis. This establishes the positive-quadrant repelling conclusion locally.

**2. Critical boundary extinction.** Keep \(k=k_c\), but choose \(b_2>b_*\). On a center manifold \(u=U-cv+O(v^2)\), and substitution gives \(v'=-(b_2-b_*)v^2+O(v^3)\). Thus the zero eigenvalue is attracting on the physical half-line. The other eigenvalue remains \(-a_1<0\), so the equilibrium is locally asymptotically stable relative to the nonnegative quadrant. The stable-foliation estimate places nearby positive trajectories exponentially close to a center orbit; the scalar asymptotic integration of \(v'=-\delta v^2+O(v^3)\), \(\delta=b_2-b_*>0\), gives \(t v(t)\to1/\delta\). Since \(U-u(t)=cv(t)+O(v(t)^2)+O(e^{-\sigma t})\) for some \(\sigma>0\), the second limit follows. Strict positivity persists at finite time because each population equation has that population as a factor.

**3. Exact positive-equilibrium census for the normalized subfamily.** With \(u=1-v\), the second nullcline is
\[
H_{k,b}(v)=\frac{2}{1+k(1-v)}-1-(b-1)v=0,\quad 0<v<1.
\]
Let \(\tau=b-1\in(1/2,1)\). Solving \(H_{k,b}(v)=0\) for \(k\) gives
\[
k=K_\tau(v)=\frac{1-\tau v}{(1-v)(1+\tau v)}.
\]
Its derivative is
\[
K_\tau'(v)=-\frac{\tau^2v^2-2\tau v+2\tau-1}{(1-v)^2(1+\tau v)^2}.
\]
The only root of the numerator in \((0,1)\) is
\[
v_f=\frac{1-\sqrt{2(1-\tau)}}{\tau};
\]
the other root lies above \(1\). Hence \(K_\tau\) decreases strictly from \(K_\tau(0)=1\) to its unique nondegenerate minimum at \(v_f\), then increases strictly to infinity as \(v\uparrow1\). Direct substitution gives \(K_\tau(v_f)=k_f(b)\). Consequently, horizontal intersections yield exactly the stated zero, one, or two **strictly positive** equilibria for every \(k>0\), including both boundaries \(k=k_f\) and \(k=1\). At \(k=1\), the surviving positive root is \(v=(2\tau-1)/\tau\), and the other root is \(v=0\).

At any positive equilibrium, the Jacobian has
\[
\operatorname{tr}J=-u-bv<0,\qquad
\det J=-uv\,H_{k,b}'(v).
\]
The smaller-\(v\) root has \(H'_{k,b}(v)<0\) and hence positive determinant, so it is a hyperbolic sink; the larger-\(v\) root has negative determinant, so it is a saddle. The double root is an ordinary saddle-node because \(K_\tau''(v_f)>0\), and \(\partial_kH=-2u/(1+ku)^2\ne0\) there. The boundary state \((0,2/b)\) has eigenvalues \(1-2/b<0\), \(-2<0\). The boundary state \((1,0)\) has eigenvalues \(-1\), \((1-k)/(1+k)\); at \(k=1\), Step 2 applies with \(b_*=3/2\). All asserted local types follow.

**4. Tangency, cubic sign, and an exact witness.** Substituting \(\tau=1/2+\eta\) into \(k_f\) and Taylor expanding at \(\eta=0^+\) gives \(k_f=1-2\eta^2+2\eta^3+O(\eta^4)\). At \((b,k)=(3/2,1)\), the general cubic formula in Step 1 reduces to \(C_*=1/4\). For the rational parameters \((b,k)=(8/5,99/100)\), the two roots are exactly
\[
v_{\pm}=\frac{17\pm2\sqrt{31}}{99},\quad u_{\pm}=1-v_{\pm},
\]
with the minus sign giving the sink and the plus sign the saddle. Both satisfy \(0<v<1\), demonstrating coexistence in the strict interval \(3/2<b<2\).

## Verification
The standalone `verify.py` (Python 3 with SymPy) checks the exact equilibrium polynomial, rational parametrization, unique critical point, fold formula, Taylor coefficients, Jacobian determinant identity, double-degeneracy cubic coefficient, general positive-parameter coefficient, and an exact two-equilibrium witness. Reproduce by running `python verify.py` in the directory containing this document and the checker. Successful output includes `VERIFY_OK` and `GENERAL_CUBIC_VERIFY_OK`. The program's finite checks do not replace the analytical root-count argument, center-manifold proof, or asymptotic integration.

## Relationship to prior work
Srivastava, Takyi and Parshad introduce exactly this rational fear-modified two-species competition system, derive a coexistence quadratic, prove several sufficient existence and bifurcation statements, and numerically illustrate a saddle-node–transcritical interaction. This work does **not** claim the first discovery of two positive equilibria, fear-induced bistability, saddle-node bifurcations, transcritical bifurcations, or the general interaction phenomenon. The new content is the exact all-\(k\) phase boundary within the natural \(3/2<b<2\) subfamily, its quantified fold–invasion tangency, and the general-parameter positive cubic sign and sharp \(1/t\) critical relaxation law. In particular, a sufficient two-positive-root regime in the initiating paper assumes \(b_1b_2>2c_1c_2\), which the explicit \(b<2\) subfamily does not satisfy; that sufficiency statement cannot by itself establish this census.

Saputra, van Veen and Quispel prove general saddle-node–transcritical normal-form principles for a **different** harvested Lotka–Volterra system, including the qualitative nonversal-cusp tangency. Thus the generic geometry is precedent, not a novelty claim; their equations do not determine the fear model's exact \(k_f(b)\), biological branch types, cubic coefficient, or extinction constants. Chen, Chen, Srivastava and Parshad study a related allelopathic extension with an extra toxin-induced interaction. Its general bifurcation theory and some zero-toxin specializations may be relevant to broader priority; the exact quantitative statement above was not identified in inspected sections. Equivalent unindexed or subsequent work remains possible.

## Limitations
The center-manifold dynamics and critical extinction rate are local. The exact count is a classification of **positive equilibria**, not an assertion of complete global basin boundaries. The particularly simple fold formula is for a physically positive, explicitly calibrated two-parameter family, not for every parameter choice in the general model. The cubic coefficient is positive when \(a_2>c_2U\) and \(k_c>0\); it does not apply to the different degeneracy \(k_c=0\). The infinite-time asymptotics use standard center-manifold and stable-foliation theory, not finite numerical experiments. Results are not independently audited or externally certified. Publication priority cannot be proven from finite literature searches.

## References
- V. Srivastava, E. M. Takyi and R. D. Parshad, *The effect of "fear" on two species competition*, arXiv:2210.10280 (first public version 2022-10-19), *Mathematical Biosciences and Engineering* 20 (2023), 8814–8855, DOI: https://doi.org/10.3934/mbe.2023388. Equation (3.1), Theorems 3.1, 3.11–3.12, and Figure 7.
- K. V. I. Saputra, L. van Veen and G. R. W. Quispel, *The saddle-node-transcritical bifurcation in a population model with constant rate harvesting*, arXiv:1002.4150 (2010), DOI: https://doi.org/10.3934/dcdsb.2010.14.233. Sections 1–2.
- S. Chen, F. Chen, V. Srivastava and R. D. Parshad, *Dynamical Analysis of an Allelopathic Phytoplankton Model with Fear Effect*, arXiv:2309.08383 (2023). Sections 3–4 and 6.
