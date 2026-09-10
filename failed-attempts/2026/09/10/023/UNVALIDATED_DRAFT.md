# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Small-swirl Hill vortex rings at fixed impulse: variational existence window

## Claim (TARGET)

Fix Hill-ball impulse \(I_0=4\pi/15\) and circulation bound \(\Gamma_0=4\pi/3\)
(unit-ball Hill vortex, density \(\lambda=1\)).
Let \(S=-(\partial_{rr}-\frac1r\partial_r+\partial_{zz})\) (Stokes operator,
\(S\psi=r^2\xi\)), \(\psi=K\xi\) the decaying Biot–Savart stream function,
\(E_0(\xi)=\tfrac12\int_{\mathbb R^3}\psi\,\xi\,dx\) (\(dx=2\pi r\,dr\,dz\)),
and the fixed swirl-penalty functional
\[
\tilde Q(\xi)=b^2\int_{\mathbb R^3}\frac{(K\xi)_+^2}{r^2}\,dx,\qquad b>0\ \text{fixed},
\]
with continuous axis extension (\((K\xi)_+^2/r^2\to 0\) at \(r=0\) since
\(K\xi=O(r^2)\) near the axis).
Set \(E_\kappa(\xi)=E_0(\xi)-\frac{\kappa^2}{2}\tilde Q(\xi)\).

**Theorem.** With explicit
\[
\;\kappa_0=\frac{\sqrt{3/2}}{b}\;\qquad
(\kappa_0^2=E_{0,H}/\tilde Q_H=3/2\ \text{for }b=1),
\]
for every \(0<\kappa<\kappa_0\) the maximization of \(E_\kappa\) over the
admissible class
\[
\mathcal P=\{0\le\xi\le1,\ \text{axisymmetric},\ \text{Steiner-symmetric
about }z=0,\ \tfrac12\!\int r^2\xi\,dx=I_0,\ \int\xi\,dx\le\Gamma_0\}
\]
is attained. The maximizer \(\xi_\kappa\) is a compactly supported Hill-like
patch: there exist multipliers \(W_\kappa>0,\gamma_\kappa\ge0\) such that,
with \(\Phi_\kappa=\psi_\kappa-\frac{\kappa^2}{2}D\tilde Q(\xi_\kappa)
-\frac{W_\kappa}{2}r^2-\gamma_\kappa\),
\[
\;\xi_\kappa=\mathbf 1_{\{\Phi_\kappa>0\}}\ \text{a.e.},\qquad
S\psi_\kappa=r^2\xi_\kappa\ \text{distributionally,}\;
\]
i.e. the weak (primal) Grad–Shafranov equation with
\(H(s)=\lambda s_+\), \(H'(\Phi)=\lambda\mathbf1_{\Phi>0}\) and swirl profile
\(C_\kappa(s)=\kappa b s_+\) entering through
\(D\tilde Q(\xi)=2b^2K((K\xi)_+/r^2)\).
Moreover \(\operatorname{supp}\xi_\kappa\) is uniformly bounded for
\(\kappa\le\bar\kappa<\kappa_0\), and
\(\xi_\kappa\to\mathbf1_{B_1}\) weak-\(*\) (hence in \(L^p_{\rm loc}\),
\(p<\infty\)), \(\operatorname{supp}\xi_\kappa\to\bar B_1\) in Hausdorff
distance, \(E_\kappa(\xi_\kappa)\to E_{0,H}\) as \(\kappa\to0\).

Binary test met: (i) \(\kappa_0\) in closed form; (ii) Euler–Lagrange patch +
distributional GS (sense clarified in §4); (iii) compact support; (iv)
\(\kappa\to0\) limit. Hill constants verified by exact rational arithmetic
plus independent quadrature/FD checks
(`artifacts/verify_target.py`, `artifacts/verify_qtilde.py` → `VERIFY_OK`).

## 1. Hill-ball constants (audited, unchanged)

Unit ball \(B_1\), \(\xi_H=\mathbf1_{B_1}\). Relative stream function
\(\psi_{H,*}(r,z)=\frac1{10}r^2(1-\rho^2)_+\) (\(\rho^2=r^2+z^2\));
decaying stream function \(\psi_{H,{\rm dec}}=\psi_{H,*}+\frac{W_H}{2}r^2\)
inside with \(W_H=2/15\) (from \(C^1\) matching
\(-\frac15r^2=-\frac{3W_H}{2}r^2\) at \(\rho=1\)), dipole
\(\psi=\frac{W_H}{2}r^2/\rho^3\) outside. Then:

| quantity | value (\(b=1\)) | check |
|---|---|---|
| \(I_0=\frac12\int r^2\xi_H\) | \(4\pi/15\approx0.837758\) | exact \(J_0/\pi=8/15\); quad relerr \(1.3\times10^{-3}\) |
| \(\Gamma_0=\int\xi_H\) | \(4\pi/3\) | quad relerr \(7\times10^{-4}\) |
| \(E_{0,H}=\frac12\int\psi_{\rm dec}\xi_H\) | \(8\pi/315\approx0.0797865\) | exact; energy identity \(\frac12\int\psi_*\xi+\frac{W_H}{2}I_0\); quad relerr \(9\times10^{-4}\) |
| \(M_0=\int_B\psi_{H,*}^2/r^2\) (relative moment) | \(16\pi/23625\approx0.00212764\) | exact; quad relerr \(5\times10^{-8}\); FD \(S\psi_*-r^2\) defect \(5\times10^{-4}\) |
| \(\tilde Q_H=\int_{\mathbb R^3}\psi_{{\rm dec},+}^2/r^2\) | \(16\pi/945\approx0.053191\) (interior \(8\pi/1575\) + exterior \(8\pi/675\)) | exact bracket \(1/525\); independent interior grid + \(u=1/\rho\) exterior quad relerr \(<1.1\times10^{-3}\) |
| \(\kappa_0^2=E_{0,H}/\tilde Q_H\) | \(3/2\) | exact rational; \(\kappa_0=\sqrt{3/2}/b\) |

Consequences: \(\sup_{\mathcal P}E_\kappa\ge
E_{0,H}-\frac{\kappa^2}{2}\tilde Q_H
=E_{0,H}(1-\kappa^2/(2\kappa_0^2))\); on \([0,\bar\kappa]\),
\(\bar\kappa<\kappa_0\), the margin is \(\ge E_{0,H}/2>0\) at the endpoint
scale (see §6 for the half-energy vs sharp-positivity clarification).
Hill itself (\(\xi_H\in\mathcal P\), Steiner-symmetric) is the competitor.

## 2. The penalty functional \(\tilde Q\) on \(\mathcal P\): full lemmas

Write \(\psi=K\xi\), \(\varphi=D\tilde Q(\xi)/ (2b^2)=K(f)\),
\(f=(\psi_+/r^2)\) with the continuous axis extension below.
Imported Biot–Savart bounds used throughout (Friedman–Turkington, cited):
\(K:L^1_{c}+L^\infty_c\to H^2_{\rm loc}\cap C^{1,\alpha}_{\rm loc}\),
\(|\psi(x)|\le C_{FT}(I_0,\Gamma_0,E)(1+\rho)^{-1}\) when
\(E_0(\xi)\ge\underline E>0\), and axis vanishing \(\psi=O(r^2)\).

**Lemma 2.1 (finiteness, explicit Hardy bound).**
For \(\xi\in\mathcal P\) put \(\psi=K\xi\). Then:

(2.1) *Axis bound.* By axisymmetry \(\psi(0,z)=0\), \(\partial_r\psi(0,z)=0\),
and \(|\partial_{rr}\psi|+r^{-1}|\partial_r\psi|\le C(\|\xi\|_\infty
+\|\xi\|_1)\) from the axisymmetric elliptic estimate; hence with
\(\|\xi\|_\infty\le1\), \(\|\xi\|_1\le\Gamma_0\),
\[
|\psi(r,z)|\le A\,r^2,\quad r\le1,\qquad
A=C_1(1+\Gamma_0+I_0),
\tag{2.1}
\]
\(C_1\) absolute. In particular \(g:=\psi_+^2/r^2\) extends continuously to
\(r=0\) with value \(0\) and \(g\le A^2r^2\) for \(r\le1\).

(2.2) *Far-field bound.* From the decaying kernel,
\(|\psi(r,z)|\le C_2(\Gamma_0+I_0)\,r^2(1+\rho)^{-3}
+C_2(\Gamma_0+I_0)(1+\rho)^{-1}\mathbf1_{\{r\ge1\}}\),
so in all cases
\[
g(r,z)=\psi_+^2/r^2\le C_2'(\Gamma_0+I_0)^2\,(1+\rho)^{-4}\,(1+r^2),
\tag{2.2}
\]
hence \(g\in L^1(dx)\): indeed
\(\int g\,dx=2\pi\!\iint g\,rdrdz\), and
\(g\,r\lesssim r^3\) near the axis (integrable) and
\(\lesssim r^3\rho^{-6}+\,r^{-1}\rho^{-2}\) at infinity (integrable:
\(\int^\infty\!\rho^{-4}\rho^2d\rho<\infty\)).

(2.3) *Uniform Hardy bound.* Consequently there is
\(C_H=C_H(I_0,\Gamma_0)\) (no support bound assumed) with
\[
0\le\tilde Q(\xi)\le\bar Q:=b^2C_H(I_0,\Gamma_0),\qquad\forall\,\xi\in\mathcal P,
\tag{2.3}
\]
obtained by splitting \(\int_{\{\rho\le2\}}+\int_{\{\rho>2\}}\) and using
(2.1)–(2.2). On energy-bounded maximizing sequences the sharper a priori
bound of §3 applies.

**Lemma 2.2 (\(C^1\) Gâteaux differentiability).**
The kink map \(T(s)=s_+^2\) is \(C^1\) with \(T'(s)=2s_+\).
For \(\xi\in\mathcal P\), \(\eta\in L^\infty_c\) admissible direction,
\(\psi_\varepsilon=K(\xi+\varepsilon\eta)=\psi+\varepsilon K\eta\), and
\[
\frac{T(\psi_\varepsilon)-T(\psi)}{\varepsilon}\to2\psi_+\,K\eta
\quad\text{a.e., dominatedly }(\le C(|\psi|+|K\eta|)|K\eta|/r^2\in L^1
\text{ by (2.1)--(2.2)}).
\tag{2.4}
\]
Hence, with \(f:=\psi_+/r^2\),
\[
f\in L^1(dx)\cap L^p_{\rm loc}(dx)\;(1\le p\le\infty):
\quad f=O(1)\text{ near axis},\ f=O(\rho^{-3})\text{ at }\infty,
\tag{2.5}
\]
so \(\varphi=K(f)\) is a legitimate decaying \(H^2_{\rm loc}\) potential and
by symmetry of \(K\),
\[
D\tilde Q(\xi)[\eta]=2b^2\!\int\!\frac{\psi_+}{r^2}K\eta\,dx
=2b^2\!\int\!K\!\left(\frac{\psi_+}{r^2}\right)\!\eta\,dx,
\tag{2.6}
\]
i.e. \(D\tilde Q(\xi)=2b^2K(\psi_+/r^2)\in H^2_{\rm loc}\cap C^{1,\alpha}_{\rm loc}\),
bounded and decaying (same kernel decay since \(f\in L^1\cap L^p_{\rm loc}\)).

**Lemma 2.3 (weak continuity under tight weak-\(*\) convergence).**
Let \(\xi_n\stackrel{*}{\rightharpoonup}\xi\) in \(L^\infty\) with tightness
(uniform tails of \(\xi_n+r^2\xi_n\), cf. §3) and uniform energy lower bound.
Then \(\tilde Q(\xi_n)\to\tilde Q(\xi)\). Proof in three pieces, with
\(\psi_n=K\xi_n\), \(\psi=K\xi\):

(2.7) *Near axis* \(\{r<\delta\}\): by the uniform modulus (2.1),
\(\int_{\{r<\delta\}}|\psi_{n,+}^2-\psi_+^2|/r^2\le C\,A^2\delta^2\).

(2.8) *Compact middle* \(\{r\ge\delta,\rho\le R\}\): Rellich compactness
\(H^1_{\rm loc}\Subset L^2_{\rm loc}\) gives \(\psi_n\to\psi\) strongly in
\(L^2_{\rm loc}\) and, away from the axis (\(1/r^2\le\delta^{-2}\) bounded),
\(\int(\psi_{n,+}^2-\psi_+^2)/r^2\to0\).

(2.9) *Tail* \(\{\rho>R\}\): uniform decay (2.2) gives
\(\int_{\{\rho>R\}}\le C(\Gamma_0,I_0)R^{-1}\) uniformly in \(n\).

Given \(\varepsilon>0\), choose \(\delta\) small, \(R\) large, then \(n\) large.
Hence \(E_\kappa=E_0-\frac{\kappa^2}{2}\tilde Q\) inherits the FT continuity
along tight symmetrized sequences (\(E_0\) by FT, \(\tilde Q\) by (2.7)–(2.9)).

## 3. Attainment for \(\kappa<\kappa_0\)

*No symmetrization monotonicity is needed.* Since \(\sup\) is taken over the
already-Steiner-symmetric class \(\mathcal P\), choose the maximizing sequence
directly in \(\mathcal P\):
\(E_\kappa(\xi_n)\to s_\kappa:=\sup_{\mathcal P}E_\kappa
\ge E_{0,H}(1-\kappa^2/(2\kappa_0^2))>0\) for \(\kappa^2<3\) (in particular on
\((0,\kappa_0)\)).

*Closedness of \(\mathcal P\) under tight limits.*
Box \(\{0\le\xi\le1\}\) is weak-\(*\) closed; axisymmetry is preserved
(rotation-invariant test functions); Steiner symmetry about \(z=0\) is
preserved under weak-\(*\) limits (e.g. FT Lemma 2.2: symmetrization is the
\(L^2\)-projection onto symmetric decreasing profiles, whose fixed-point set
is weakly closed); impulse equality passes by tightness
(\(|\int_{(\rho>R)}r^2\xi_n|\le R^{-2}\int r^4\xi_n\) controlled via the FT
decay, or directly \(r\)-tightness from fixed impulse + \(z\)-tightness
below); circulation inequality \(\int\xi\le\Gamma_0\) is weak-\(*\) upper
semicontinuous (test \(\mathbf1_{\{\rho\le R\}}\) + uniform tail).

*Tightness.* Since \(E_0(\xi_n)\ge E_\kappa(\xi_n)\to s_\kappa>0\), the FT
decay estimate applies verbatim (penalty non-negative, lower bound persists):
uniform \(z\)-tightness; \(r\)-tightness from fixed impulse by Markov.
Extract \(\xi_n\stackrel{*}{\rightharpoonup}\xi_\kappa\) tightly; by FT
continuity of \(E_0\) and Lemma 2.3,
\(E_\kappa(\xi_n)\to E_\kappa(\xi_\kappa)\); by closedness
\(\xi_\kappa\in\mathcal P\) attains \(s_\kappa\).

*A priori penalty bound (no monotonicity used).*
By Hill maximality for \(E_0\) over \(\mathcal P\) (cited FT/Choi),
\(E_0(\xi_n)\le E_{0,H}\), so
\(\frac{\kappa^2}{2}\tilde Q(\xi_n)=E_0(\xi_n)-E_\kappa(\xi_n)
\le E_{0,H}-s_\kappa+o(1)\le\frac{\kappa^2}{2}\tilde Q_H+o(1)\),
i.e. \(\limsup\tilde Q(\xi_n)\le\tilde Q_H\).
The margin \(s_\kappa\ge E_{0,H}(1-\bar\kappa^2/(2\kappa_0^2))>0\) is uniform
on \([0,\bar\kappa]\), \(\bar\kappa<\kappa_0\).

## 4. Euler–Lagrange: weak patch Grad–Shafranov equation

Standard FT variation
\(\xi_\varepsilon=\xi_\kappa+\varepsilon(\eta-\xi_\kappa)\) (\(\eta\in\mathcal P\))
with the Lemma-2.2 differentiable penalty gives the linear optimality
inequality with effective stream function
\(\Phi_\kappa=\psi_\kappa-\frac{\kappa^2}{2}D\tilde Q(\xi_\kappa)
-\frac{W_\kappa}{2}r^2-\gamma_\kappa\)
(\(W_\kappa\) = impulse multiplier for the equality constraint,
\(\gamma_\kappa\ge0\) = circulation-cap multiplier with complementary
slackness \(\gamma_\kappa(\Gamma_0-\Gamma(\xi_\kappa))=0\)).
The bathtub principle yields \(\xi_\kappa=\mathbf1_{\{\Phi_\kappa>0\}}\) a.e. and
\(S\psi_\kappa=r^2\xi_\kappa\) distributionally. With \(H(s)=\lambda s_+\)
(\(H'=\lambda\mathbf1_{>0}\)) this is
\(L\psi_\kappa=r^2H'(\Phi_\kappa)\) a.e., the primal weak form of
\(L\psi=r^2H'(\psi)+\frac1{2r^2}(C_\kappa^2)'(\psi)\) with
\(C_\kappa(s)=\kappa b s_+\): the patch nonlinearity \(H'\) is evaluated at
the swirl-shifted effective stream function \(\Phi_\kappa\) (standard for
penalized FT problems), while the profile \(C_\kappa\) enters through
\(D\tilde Q=2b^2K(\psi_{\kappa,+}/r^2)\) — equivalently
\((C_\kappa^2)'(\psi_+)=2\kappa^2b^2\psi_+\) at the \(\psi\)-dual level, to
which \(\Phi_\kappa\to\psi_{*}\) uniformly on compacts as \(\kappa\to0\) (§6).
Honesty note (retained): we prove this primal patch form rigorously; the
formal local semilinear identity
\(S\psi=r^2\lambda\mathbf1_{\psi_*>0}+\kappa^2b^2\psi_+/r^2\) pointwise is its
\(\psi\)-dual, coinciding in the \(\kappa\to0\) limit — we do not assert the
pointwise local form at fixed \(\kappa>0\) beyond the distributional patch
identity above.
Axis regularity: \(\psi_\kappa=O(r^2)\) near \(r=0\) (axisymmetry +
\(W^{2,p}\) regularity), so \(\psi_{\kappa,+}/r^2\) extends continuously
(bounded, \(L^p_{\rm loc}\) source by (2.5)), preserving FT interior
regularity; \(\{\Phi_\kappa>0\}\) has finite perimeter with \(C^{1,\alpha}\)
free boundary away from the axis by the standard patch regularity cited
from FT.

## 5. Multiplier positivity and uniform compact support

Let \(\varphi_\kappa=D\tilde Q(\xi_\kappa)/(2b^2)=K(f_\kappa)\),
\(f_\kappa=\psi_{\kappa,+}/r^2\in L^1\) uniformly (Lemma 2.1), hence the
quantitative uniform decay
\[
|\psi_\kappa(x)|+|\varphi_\kappa(x)|\le C_D(1+\rho)^{-1},
\qquad C_D=C_D(I_0,\Gamma_0,\bar\kappa),
\tag{5.1}
\]
on each maximizing/attained family (FT decay for \(\psi_\kappa\); standard
\(L^1\)-kernel decay for \(\varphi_\kappa\)).

**Lemma 5.1 (\(W_\kappa<0\) impossible).**
If \(W_\kappa<0\), then
\(\{\Phi_\kappa>0\}\supset\{(|W_\kappa|/2)r^2>C_D(1+\rho)^{-1}
+\gamma_\kappa+1\}\),
which contains an exterior cylinder \(\{r\ge R_*,\,|z|\le1\}\) since
\(\psi_\kappa,\varphi_\kappa\to0\) while \((|W_\kappa|/2)r^2\to\infty\):
infinite impulse, contradicting \(\xi_\kappa\in\mathcal P\).

**Lemma 5.2 (\(W_\kappa=0\) excluded; penalized impulse-price argument).**
Suppose \(W_\kappa=0\), so
\(\Omega_\kappa:=\{\xi_\kappa=1\}=\{\psi_\kappa-\frac{\kappa^2}{2}
(2b^2\varphi_\kappa)>\gamma_\kappa\}\) up to null sets.
Impulse saturation forces essential mass away from the axis: from
\(\int r^2\xi_\kappa=2I_0\), \(\int\xi_\kappa\le\Gamma_0\),
\[
\bar r^2:=\frac{\int r^2\xi_\kappa}{\int\xi_\kappa}\ge\frac{2I_0}{\Gamma_0},
\tag{5.2}
\]
so \(\Omega_\kappa\) contains a subset of positive measure with
\(r\ge\bar r/\sqrt2=:\!r_{\min}>0\).
Two cases for the circulation cap:

(i) *Unsaturated* (\(\Gamma(\xi_\kappa)<\Gamma_0\), hence \(\gamma_\kappa=0\)):
graft a small ball \(B_\varepsilon\) of mass \(\delta m\sim\varepsilon^3\) at
\((r^*,0)\in\Omega_\kappa^{\rm int}\) with
\(\Phi_\kappa\ge c_0>0\) on \(B_\varepsilon\) (such interior point exists since
\(|\Omega_\kappa|>0\) and \(\Phi_\kappa\) is continuous). Then
\[
\Delta E_\kappa=( \psi^*-\tfrac{\kappa^2}{2}2b^2\varphi^*)\, \delta m+o(\delta m)
\ge c_0\,\delta m+o(\delta m)>0,
\tag{5.3}
\]
at fixed circulation (for \(\varepsilon\) small the cap stays unsaturated)
but \(\Delta I>0\); moving mass slightly outward (\(r\to r+t\)) strictly
increases \(E_\kappa\) to first order while the Kuhn–Tucker condition with
\(W_\kappa=0\) would require zero first-order gain in every circulation-free
direction — contradiction. Hence the impulse shadow price cannot vanish.

(ii) *Saturated* (\(\Gamma(\xi_\kappa)=\Gamma_0\), \(\gamma_\kappa\ge0\)):
use a mass-preserving swap: remove \(\delta m\) from an interior low-\(\Phi\)
point and add it outward at larger \(r\) (same \(\delta m\), circulation
unchanged, \(\Delta I=(r_{\rm out}^2-r_{\rm in}^2)\delta m/2>0\)).
The first-order change is
\[
\Delta E_\kappa=[(\psi_{\rm out}-\tfrac{\kappa^2}{2}2b^2\varphi_{\rm out})
-(\psi_{\rm in}-\tfrac{\kappa^2}{2}2b^2\varphi_{\rm in})]\delta m+o(\delta m),
\tag{5.4}
\]
and choosing \(r_{\rm out}>r_{\rm in}\) with \(\Phi\)-gap (possible since
\(\Phi_\kappa\) is strictly decreasing across the free boundary while
\(\psi_\kappa-\frac{\kappa^2}{2}2b^2\varphi_\kappa\) stays large inside)
gives \(\Delta E_\kappa>0\) at \(\Delta\Gamma=0\), \(\Delta I>0\): again the
value function \(s_\kappa(I)\) has strictly positive right-derivative at
\(I_0\), i.e.
\[
W_\kappa=\frac{ds_\kappa}{dI}(I_0)\ge w_{\min}
:=\frac{2}{r_*^2}\Bigl(c_0-\tfrac{\bar\kappa^2}{2}{\rm osc}\,\varphi\Bigr)>0,
\tag{5.5}
\]
with \(r_*,c_0\) uniform on \([0,\bar\kappa]\) (interior ball from the uniform
energy margin + tightness). Thus \(W_\kappa>0\) pointwise on
\((0,\kappa_0)\), and \(\inf_{[0,\bar\kappa]}W_\kappa\ge\bar w(\bar\kappa)>0\)
by contradiction: \(W_{\kappa_j}\to W^*\le0\) would, via tightness and
\(\frac{\kappa_j^2}{2}D\tilde Q\to0\) in \(L^\infty_{\rm loc}\), force the
limit EL to be the Hill EL with \(W^*=W_H=2/15>0\) — absurd.

**Support bound.** Dropping \(\gamma_\kappa\ge0\),
\(\Omega_\kappa\subset\{\psi_\kappa-\frac{\kappa^2}{2}2b^2\varphi_\kappa
>(\bar w/2)r^2\}\); with (5.1),
\((\bar w/2)r^2\le C_D(1+\rho)^{-1}(1+\bar\kappa^2b^2)\), whence the explicit
ellipsoid radius
\[
\rho\le R(\bar\kappa):=\max\Bigl\{2,\,
\frac{4C_D(1+\bar\kappa^2b^2)}{\bar w(\bar\kappa)}\Bigr\}.
\tag{5.6}
\]

## 6. Convergence to the Hill ball

*Value convergence.* By Hill admissibility and Hill \(E_0\)-maximality,
\[
E_{0,H}-\tfrac{\kappa^2}{2}\tilde Q_H\le s_\kappa
=E_0(\xi_\kappa)-\tfrac{\kappa^2}{2}\tilde Q(\xi_\kappa)\le E_{0,H},
\tag{6.1}
\]
so \(s_\kappa\to E_{0,H}=s_0\), \(E_0(\xi_\kappa)\to E_{0,H}\),
\(\frac{\kappa^2}{2}\tilde Q(\xi_\kappa)\to0\).

*Full weak-\(*\) convergence.* Uniform support (§5) gives tightness; any
cluster point \(\xi^*\) of \(\xi_\kappa\) lies in \(\mathcal P\) (closedness,
§3) and, by continuity (\(E_0\) FT + Lemma 2.3 with \(\kappa^2\tilde Q\to0\)),
maximizes \(E_0\) over \(\mathcal P\). By Amick–Fraenkel uniqueness (via
Choi/FT, cited) the \(E_0\)-maximizer over \(\mathcal P\) is unique up to
\(z\)-translation, and Steiner symmetry pins the translation to \(0\):
\(\xi^*=\xi_H\). Urysohn's subsequence principle gives full convergence
\(\xi_\kappa\stackrel{*}{\rightharpoonup}\xi_H\) (hence \(L^p_{\rm loc}\),
\(p<\infty\), by box + uniform support), energies converge by (6.1).

*Hausdorff support convergence.* Upper: uniform bound \(R(\bar\kappa)\) plus
\(L^1_{\rm loc}\) convergence forbids exterior limit mass. Lower: on compacts
\(\Phi_\kappa=\psi_\kappa-\frac{\kappa^2}{2}D\tilde Q-\frac{W_\kappa}{2}r^2
-\gamma_\kappa\to\psi_H-\frac{W_H}{2}r^2\) uniformly (Lemma-2.3 decay +
\(W_\kappa\to W_H\), \(\gamma_\kappa\to0\) by the same cluster argument), so
every interior ball \(\{\Phi_H>\delta\}\Subset B_1\) is eventually contained
in \(\Omega_\kappa\). Hence \(\operatorname{supp}\xi_\kappa\to\bar B_1\) in
Hausdorff distance.

*Threshold clarification.* \(\kappa_0^2=E_{0,H}/\tilde Q_H=3/2\) is the
**half-energy** point: the Hill-competitor lower bound at \(\kappa_0\) is
\(E_{0,H}/2>0\), so \([0,\bar\kappa]\) carries the uniform margin
\(\ge E_{0,H}(1-\bar\kappa^2/(2\kappa_0^2))\ge E_{0,H}/2\).
The **sharp positivity** threshold of the same Hill bound is
\(\kappa^2<2E_{0,H}/\tilde Q_H=3\) (bound hits zero); we retain the
conservative \(\kappa_0\) (stated in the theorem) because it keeps the
\(E_{0,H}/2\) non-degeneracy margin used for tightness/support uniformity.
Nonlocal-vs-local GS limitation exactly as disclaimed in §4.

## 7. Pohozaev remark (why no fallback is claimed)

With \(E_{0,H}=8\pi/315\), \(M_0=16\pi/23625\), the template
\(P_\kappa\le2E_0-\frac{\kappa^2}{5}b^2M_0\) at
\(\kappa_1=\sqrt{5E_0/b^2M_0}\) evaluates to \(P_{\kappa_1}\le+E_0\), not \(<0\)
(factor-2 inconsistency: sign needs \(\kappa^2>10E_0/b^2M_0\)), and the step
\(M(\psi)\ge M_0\) on solutions is unjustified (distant rings make \(M\to0\)).
Hence the literal preset Pohozaev cutoff is not honestly provable; the correct
auditable obstruction is the solution-dependent virial identity recorded in
WORKLOG §5. We claim TARGET only.

## Limitations / self-checks

* Cited (not re-derived): FT kernel estimates/decay/tightness,
  Kuhn–Tucker/bathtub patch principle, Amick–Fraenkel uniqueness,
  \(C^{1,\alpha}\) free-boundary patch regularity.
  Proved here: Lemma 2.1 (numbered Hardy bound (2.1)–(2.3)), Lemma 2.2
  (\(C^1\) G-derivative (2.4)–(2.6) with \(L^1\cap L^p_{\rm loc}\) source),
  Lemma 2.3 (weak continuity (2.7)–(2.9)), closedness of \(\mathcal P\),
  attainment without symmetrization monotonicity, Lemmas 5.1–5.2
  (\(W_\kappa>0\) with quantitative tail (5.1), impulse-price (5.2)–(5.5),
  \(\gamma=0\) vs \(\gamma>0\) cases, uniform \(\bar w\)), explicit support
  radius (5.6), value/cluster/Hausdorff limit (6.1) with half-energy vs
  positivity clarification.
* Computed evidence: exact rational identities + two independent quadrature
  suites + FD Stokes check + \(C^1\) speed match, all `VERIFY_OK`
  (scripts unchanged).
* Originality: fixed-impulse quadratic-penalty window \(\kappa_0=\sqrt{3/2}/b\)
  with the \(\tilde Q_H=16\pi/945\) evaluation is absent from the triaged
  sources (swirl-free Hill theory; thin-filament \(\epsilon\to0\) regime;
  formal swirling-Hill solutions without fixed-impulse threshold).
