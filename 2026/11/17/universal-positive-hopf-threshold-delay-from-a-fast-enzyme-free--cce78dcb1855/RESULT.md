# Universal positive Hopf-threshold delay from a fast enzyme-free insertion

## Finding

For the four-substrate enzyme-sharing cycle specified below, the Hopf threshold of the unique positive equilibrium satisfies, for each fixed \(\alpha,\beta,\gamma>0\),
\[
 s_{\mathrm H}(K)=s_*+c_*\frac{\alpha+\beta+\gamma}{\alpha\gamma}\frac1K+O(K^{-2}),\qquad
 \omega_{\mathrm H}(K)=\omega_*+d_*\frac{\alpha+\beta+\gamma}{\alpha\gamma}\frac1K+O(K^{-2}),
\]
where \(s_*=13.0160798148892471\ldots\), \(\omega_*=10.7871531900729046\ldots\), \(c_*=670.0071181534651\ldots>0\), and \(d_*=4.0043211218700\ldots\). The three independently variable fast kinetic rates enter the first-order shifts *only* through the positive residence-time factor \(\tau_f=(\alpha+\beta+\gamma)/(\alpha\gamma)\). Consequently inserting a sufficiently fast enzyme-free HMM reaction always shifts this Hopf threshold to **larger** values of the unbinding parameter \(s\), and its Hopf frequency also increases to first order. The exact algebraic characterizations of all constants are given below; the decimals are approximations, not definitions.

## Assumptions and scope

Use the transformation cycle \(X_1\to X_2\to X_3\to X_4\to X_1\), with the first two transformations using one shared enzyme \(E\). The elementary reactions and positive rates are:
\[
\begin{array}{ll}
E+X_1\overset{2400}{\underset{1/2}{\rightleftharpoons}} C_1\overset{5/2}{\longrightarrow}E+X_2,&
E+X_2\overset{102/5}{\underset{2}{\rightleftharpoons}} C_2\overset{100}{\longrightarrow}E+X_3,\\
X_3\overset{s+5}{\underset{s}{\rightleftharpoons}} C_3\overset{5}{\longrightarrow}X_4,&
X_4\overset{K\alpha}{\underset{K\beta}{\rightleftharpoons}} C_4\overset{K\gamma}{\longrightarrow}X_1.
\end{array}
\]
Here \(K>0\), \(s>0\), and \(\alpha,\beta,\gamma>0\) are held fixed in the \(K\to\infty\) limit. The first three modules are the published three-cycle Hopf example, except that its third-module product is now \(X_4\); the fast fourth module returns it to \(X_1\). The enzyme total is \(E+C_1+C_2=411/20\). To compare the same steady concentrations on both sides of insertion, take the conserved substrate total to be
\[
 X_1+X_2+X_3+X_4+C_1+C_2+C_3+C_4=91+50\tau_f/K.
\]
The exact positive equilibrium, for every \(s,K>0\), is
\[
 (X_1,X_2,X_3,E,C_1,C_2,C_3,X_4,C_4)
 =(1/2,50,10,1/20,20,1/2,10,
 50(\beta+\gamma)/(K\alpha\gamma),50/(K\gamma)).
\]
The result concerns the unique Hopf point in a neighborhood of the specified original three-cycle Hopf point; it is not a global count of all Hopf points in the enlarged model.

## Proof

**1. Reduced exact kinetic equations.** Set \(\varepsilon=1/K\), \(a=X_4/\varepsilon\), \(b=C_4/\varepsilon\), \(e=411/20-c_1-c_2\), and
\[
 x_3=91+50\tau_f\varepsilon-x_1-x_2-c_1-c_2-c_3-\varepsilon(a+b).
\]
For \(v_1=2400ex_1-c_1/2\) and \(v_2=(102/5)ex_2-2c_2\), the seven independent equations are
\[
\begin{aligned}
\dot x_1&=-v_1+\gamma b,&\dot x_2&=5c_1/2-v_2,\\
\dot c_1&=v_1-5c_1/2,&\dot c_2&=v_2-100c_2,\\
\dot c_3&=(s+5)(x_3-c_3),&
\varepsilon\dot a&=5c_3-\alpha a+\beta b,\\
\varepsilon\dot b&=\alpha a-(\beta+\gamma)b.
\end{aligned}
\]
Direct substitution verifies the equilibrium stated above. The two fast eigenvalues have negative real parts because their unscaled matrix has trace \(-\alpha-\beta-\gamma<0\) and determinant \(\alpha\gamma>0\).

**2. Exact fast transfer.** In a spectral perturbation with exponent \(z\), elimination of \((a,b)\) gives
\[
\gamma\,\delta b=\frac{5\,\delta c_3}{Q(z,\varepsilon)},\qquad
\delta a+\delta b=\frac{5[\tau_f+\varepsilon z/(\alpha\gamma)]\,\delta c_3}{Q(z,\varepsilon)},
\]
where \(Q=1+\tau_f\varepsilon z+\varepsilon^2z^2/(\alpha\gamma)\). Thus the five-dimensional effective spectral Jacobian equals the limiting matrix \(J_0(s)\), except its entries in row one, column five and row five, column five become
\[
 (J_{\mathrm{eff}})_{1,5}=\frac5Q,\qquad
 (J_{\mathrm{eff}})_{5,5}=-2(s+5)-5\varepsilon(s+5)\frac{\tau_f+\varepsilon z/(\alpha\gamma)}{Q}.
\]
These are Schur-complement identities, not asymptotic guesses.

**3. Limiting characteristic polynomial and its Hopf root.** In the coordinate order \((x_1,x_2,c_1,c_2,c_3)\),
\[
J_0(s)=\begin{pmatrix}
-120&0&2401/2&1200&5\\
0&-51/50&2045/2&1022&0\\
120&0&-1203&-1200&0\\
0&51/50&-1020&-1122&0\\
-s-5&-s-5&-s-5&-s-5&-2s-10
\end{pmatrix}.
\]
Writing \(P(z,s)=\det(zI-J_0(s))\), its numerator is
\[
\begin{aligned}
50P={}&50z^5+(100s+122801)z^4+(244852s+14332133)z^3\\
&+(26827251s+157881855)z^2+(113030565s+566682825)z\\
&+3181788000s+15908940000.
\end{aligned}
\]
The conditions \(P(i\sqrt t,s)=0\), \(t>0\), yield
\[
s=\frac{50t^2-14332133t+566682825}{244852t-113030565}
\]
and
\[
2500t^4+13646747301t^3+166084766332929t^2-19531770063345000t+2434067820000000=0.
\]
The large positive root is isolated by \(116.36267<t_*<116.36268\) (rational Sturm isolation); its associated \(s_*\) is positive. The other positive root corresponds to a negative \(s\). The source establishes the Hopf crossing and stability of the remaining eigenvalues at this branch. The characteristic equation and the exact isolation also establish the simplicity and nonzero crossing derivative used next.

**4. Exact first variation.** Differentiation of the Schur determinant gives the first-order expansion near bounded \(z\):
\[
\det(zI-J_{\mathrm{eff}})=P(z,s)+\varepsilon\tau_f R_1(z,s)+O(\varepsilon^2),
\quad R_1(z,s)=-153000(400z-1)(s+5).
\]
Let \(z_*=i\omega_*\), and put \(L_\varepsilon=-R_1(z_*,s_*)/P_z(z_*,s_*)\), \(L_s=-P_s(z_*,s_*)/P_z(z_*,s_*)\). At fixed \(s\), the critical eigenvalue has derivative \(\tau_f L_\varepsilon\); its parameter derivative is \(L_s\). The implicit function theorem gives
\[
c_*=-\frac{\operatorname{Re}L_\varepsilon}{\operatorname{Re}L_s},\qquad
 d_*=\operatorname{Im}(L_\varepsilon+c_*L_s).
\]
Hence the displayed expansions and their \(\tau_f\)-universality follow, including \(O(K^{-2})\) for each fixed positive rate triple.

**5. Certified sign, not just finite sampling.** For \(t=t_*\), \(s=s_*\), define
\[
\begin{aligned}
A&=[250t^2-(734556s+42996399)t+113030565s+566682825]/50,\\
B&=[-(400s+491204)t+53654502s+315763710]/50,\\
C&=[100t^2-26827251t+3181788000]/50,\\
D&=[-244852t+113030565]/50.
\end{aligned}
\]
These satisfy \(P_z(i\sqrt t,s)=A+i\sqrt t B\), \(P_s(i\sqrt t,s)=C+i\sqrt t D\), and
\[
c_*=\frac{153000(s+5)(400tB-A)}{CA+tDB}.
\]
Using the rational isolating interval for \(t_*\) and the displayed rational formula for \(s_*\), one obtains \(400tB-A>8.90\times10^{11}\) and \(CA+tDB>3.66\times10^{15}\); both can be checked by rational interval substitution. Thus \(c_*>0\) exactly. High-precision evaluation gives \(c_*=670.0071181534651\ldots\), \(d_*=4.0043211218700\ldots\). Since \(\tau_f>0\), the Hopf-threshold displacement is strictly positive for *every* positive triple of fast kinetic coefficients.

## Verification

Run `python verify.py` with SymPy, NumPy and SciPy. It constructs the seven-variable mass-action Jacobian from the independent equations, verifies the exact steady state and five-dimensional polynomial, reconstructs the Schur complement, checks the universal first variation symbolically, isolates the relevant quartic root, and checks finite-rate critical eigenvalues for two distinct fast-rate triples at three values of \(K\). Expected success marker: `VERIFY_OK equilibria=1 exact_schur=1 base_charpoly=1 universal_first_order=1 isolated_Hopf=1 rates=2 finite_K=6`. Numerical eigenvalue samples corroborate the derived asymptotics but do not replace the algebraic proof or an independent scientific audit.

## Relationship to prior work

Joshi and Nguyen (2026, arXiv:2611.02523v1), Section 7 and Appendix D, give the three-cycle benchmark, its supercritical Hopf point, and numerical studies of longer reaction cycles; their framework also covers longer intermediate chains. Banaji (2023) already proves qualitative oscillation inheritance under reaction splitting, and Banaji–Boros–Hofbauer (2025) prove inheritance of transversely unfolded local bifurcations. Accordingly **neither the existence of oscillations after insertion nor persistence of a Hopf point is claimed as new**. The narrowly stated result here is the *direction, exact leading magnitude, and fast-rate residence-time universality* of the shifted Hopf parameter and frequency for this explicit positive equilibrium family. No checked primary result or mathematical-research record supplies this quantitative formula.

## Limitations

The asymptotic expansion is local near the specified positive Hopf point, with \(\alpha,\beta,\gamma\) fixed while \(K\to\infty\). It uses a concentration-matched conserved substrate total \(91+50\tau_f/K\); fixing the substrate total at 91 instead is a different problem. It does not determine remote Hopf bifurcations, global basin geometry, stability at finite arbitrary \(K\), or the effect of non-HMM fast links. The no-covering conclusion is limited by accessible literature and does not establish definitive historical priority. An independent audit has not been performed.

## References

- B. Joshi and T. D. Nguyen, *Substrate hypergraph cycles: unique steady states and persistence for every enzyme assignment; oscillations enabled by enzyme sharing*, arXiv:2611.02523v1 (first public 2026-11-02), https://arxiv.org/abs/2611.02523.
- M. Banaji, *Splitting Reactions Preserves Nondegenerate Behaviors in Chemical Reaction Networks*, SIAM Journal on Applied Mathematics 83 (2023), 748–769, DOI: 10.1137/22M1478392; preprint arXiv:2201.13105.
- M. Banaji, B. Boros, and J. Hofbauer, *The Inheritance of Local Bifurcations in Mass Action Networks*, Journal of Nonlinear Science 35, 72 (2025), DOI: 10.1007/s00332-025-10165-4.
