# Opposite-field probing preserves joint information in a frustrated Ising trimer

## Finding

**Theorem (sharp paired-field information-design threshold).** For the classical symmetric Ising triangle, sample independent equilibrium spin-configuration observations at the two known longitudinal field settings \(+y\) and \(-y\), in any relative allocation, and jointly estimate infinitesimal changes in the dimensionless exchange coupling and an unknown *common* longitudinal-field offset. At the nominal offset zero, the D-optimal allocation at every nonzero field magnitude is uniquely equal between the settings. Put
\[
 a=e^{4x}>0,\qquad a_c=\frac{23+4\sqrt{55}}{39}=1.35037933200981\ldots,\qquad x_c=\tfrac14\log a_c.
\]
Among **all opposite-sign, equal-magnitude two-setting designs**, the optimal magnitude is \(y=0\) for \(a\ge a_c\), and is uniquely \(y=y_*(a)>0\) for \(0<a<a_c\), where
\[
 q_*(a)=2\cosh(2y_*(a))-1
\]
is the unique positive zero of
\[
\begin{aligned}
 P_a(q)={}&2a^2q^4+(21a^2-6a)q^3\\
 &+(12a^3+48a^2-33a)q^2\\
 &+(27a^3+27a^2-81a)q-27(a^2+a+1).
\end{aligned}
\]
For \(a<a_c\), this zero satisfies \(q_*(a)>1\). In the strongly antiferromagnetic limit \(x\to-\infty\),
\[
 a q_*(a)\longrightarrow3,\qquad
 y_*(a)+2x\longrightarrow\tfrac12\log3,\qquad
 \max_{y,w}\det\mathcal I(x,0;y,w)\longrightarrow4.
\]
In contrast, **every single constant-field experiment** (one field magnitude and one sign for all observations) obeys
\[
 \sup_{z\in\mathbb R}\det g(x,z)
 \sim\frac{64}{3}e^{4x}\longrightarrow0,
\]
so the best paired-to-single-field determinant ratio is asymptotic to \(3/(16e^{4x})\). Here all information matrices are **per independent observation**; the comparison uses the same total observation count.

## Assumptions and scope

There are exactly three classical spins \(s_i\in\{-1,+1\}\) on a triangle, inverse temperature \(\beta>0\), bond statistic \(B=s_1s_2+s_2s_3+s_3s_1\), magnetization \(M=s_1+s_2+s_3\), and the Gibbs family
\[
 p_{x,z+\varepsilon y}(s)=Z(x,z+\varepsilon y)^{-1}\exp[xB(s)+(z+\varepsilon y)M(s)],\quad\varepsilon\in\{+1,-1\}.
\]
The known controllable fields are \(\pm y\) and the unknown parameter vector is \((x,z)\), with the design evaluated *locally* at the nominal true offset \(z=0\) and fixed nominal \(x\). Observations are independent full-spin configurations. A fraction \(w\in[0,1]\) uses \(+y\), and \(1-w\) uses \(-y\). The D-criterion is the determinant of their weighted average Fisher information, not the determinant of its individual components. The theorem does not optimize over arbitrary numbers of field magnitudes, nonequilibrium protocols, partial spin readout, or uncertain nominal couplings.

## Proof

**1. Fisher matrix of the Gibbs triangle.** Directly enumerating the eight spin states gives
\[
 Z(x,t)=2e^{-x}\cosh t\,[e^{4x}(2\cosh2t-1)+3].
\]
With \(a=e^{4x}\) and \(q=2\cosh2y-1\ge1\), the Hessian of \(\log Z\), equivalently \(g=\operatorname{Cov}(B,M)\), has entries
\[
 g_{xx}=\frac{48a q}{(aq+3)^2},\qquad
 g_{xy}=\frac{48a\sinh2y}{(aq+3)^2},
\]
\[
 g_{yy}=\frac{12(3a^2+aq^2+6aq+3a+3)}{(q+3)(aq+3)^2}.
\]
The displayed cross-entry is evaluated at \(y\); it is odd in \(y\), whereas both diagonal entries are even. Consequently the Fisher matrix for the two-field allocation is
\[
 \mathcal I(x,0;y,w)=
 \begin{pmatrix}g_{xx}(x,y)&(2w-1)g_{xy}(x,y)\\
 (2w-1)g_{xy}(x,y)&g_{yy}(x,y)\end{pmatrix}.
\]
When \(y>0\), the cross-entry is strictly positive; maximizing its determinant over \(w\in[0,1]\) therefore forces \(w=1/2\), uniquely. At \(y=0\), the two settings coincide, making the allocation immaterial.

**2. Exact reduction of the design objective.** At the optimal equal allocation,
\[
 F_a(q):=\det\mathcal I(x,0;y,\tfrac12)
 =\frac{576a q(3a^2+aq^2+6aq+3a+3)}{(q+3)(aq+3)^4},\qquad q\ge1.
\]
A direct differentiation and cancellation yields the *exact* identity
\[
 F_a'(q)=-\frac{576a P_a(q)}{(q+3)^2(aq+3)^5}.
\]
All denominators are strictly positive and \(F_a(q)\to0\) as \(q\to\infty\).

**3. Existence, uniqueness, and sharp boundary.** The coefficient list of \(P_a\), ordered by descending power of \(q\), has signs governed by
\[
 2a^2>0,\qquad 3a(7a-2),\qquad 3a(4a^2+16a-11),\qquad27a(a^2+a-3),\qquad-27(a^2+a+1)<0.
\]
Their three interior sign changes as \(a\) increases occur at \(2/7\), \((-4+3\sqrt3)/2\), and \((\sqrt{13}-1)/2\), strictly in that order. Thus the coefficient signs always have exactly **one** positive-to-negative transition. By Descartes' rule of signs and \(P_a(0)<0<P_a(+\infty)\), \(P_a\) has exactly one positive root, counted with multiplicity, and changes from negative to positive across it. Moreover
\[
 P_a(1)=(a+3)(39a^2-46a-9).
\]
The positive root of the second factor is \(a_c=(23+4\sqrt{55})/39\). When \(a<a_c\), the sole positive zero lies strictly above \(1\); hence \(F_a\) increases then decreases on \([1,\infty)\), making that point the unique global maximum. When \(a\ge a_c\), \(F_a\) is strictly decreasing after \(q=1\), so \(q=1\), equivalently \(y=0\), is the unique maximizing magnitude. This proves all finite-parameter claims, including the threshold equality.

**4. Antiferromagnetic scaling and the single-field obstruction.** For every fixed \(z>0\),
\[
 a^2P_a(z/a)\longrightarrow2z^3(z-3)\qquad(a\downarrow0).
\]
Using the unique-root result and the opposite limiting signs at \(z=3\pm\epsilon\) gives \(a q_*(a)\to3\). The elementary large-argument asymptotic of \(\operatorname{arcosh}\) then yields \(y_*+2x\to\frac12\log3\). Also, for fixed \(z>0\),
\[
 F_a(z/a)\longrightarrow\frac{576z^2}{(z+3)^4},
\]
so substitution of the actual optimizer gives \(\max F_a\to576\cdot9/6^4=4\).

For a single fixed field \(t\), the determinant is precisely
\[
 G_a(q)=\det g(x,t)
 =\frac{576a(q+3a)}{(q+3)(aq+3)^3},\qquad q=2\cosh2t-1\ge1.
\]
For \(0<a\le1\), \((q+3a)/(q+3)\le1\) and \(aq+3\ge3\), whence \(G_a(q)\le64a/3\) *uniformly in the applied field*. Taking \(q=a^{-1/2}\) makes both bounds sharp asymptotically. Thus \(\sup_tG_a(q)\sim64a/3\), establishing the diverging paired-design improvement factor \(3/(16a)\). This bound is independent of any numerical optimization.

## Verification

The standalone standard-library Python script `verify.py` independently enumerates all eight spin microstates and constructs Fisher covariances from Boltzmann weights, without using the closed-form metric in that calculation. It compares the result to the displayed rational expressions, tests symmetry cancellation for opposite fields, verifies global designs against finite numerical grids in both threshold regimes, and checks the strong-antiferromagnet asymptotics. Run `python3 verify.py` in the directory containing the file. It reports `PASS 114 ...`. These numerical checks are finite and are not substituted for Descartes' rule, the exact differentiation, or the limiting proof above.

## Relationship to prior work

Ebadi, Einali Saghavaz, Monem, and Mohammadzadeh obtained the equilibrium partition function, Fisher–Rao matrix, and *single-field* determinant for this triangle [1, sections 2–4 and Appendix A, (A.4)–(A.6)]. Their exact formulas are credited as ingredients. The object optimized here is different: the determinant of a weighted **two-experiment sum of information matrices** for a common unknown offset. Its sharp quartic optimum, change of symmetry at \(a_c\), and nonvanishing low-temperature joint information are not presented there. The general motivation for externally tuning fields to improve estimation precision is longstanding; Invernizzi et al. [2] analyze one-parameter quantum Fisher information in a transverse-field Ising chain, not this two-parameter classical trimer design. The overall D-optimal criterion is standard, but the classification and contrast with every single-field setting are model-specific.

## Limitations

This is a local Fisher-information design at a nominal zero common offset, not a global minimax statement for unknown offsets or couplings. The two applied fields are opposite and of equal magnitude; other multi-field designs are not ruled out as better. Large-sample covariance interpretations require usual regularity and efficient estimation, whereas all Fisher calculations themselves hold for each finite \(x,y\). The threshold is a bifurcation in *experimental design*, not a thermodynamic phase transition of a finite spin cluster. The prior source's published analytic Fisher matrix makes derivation of this result possible, and implicitly overlapping unindexed optimal-design work remains a priority risk.

## References

[1] Z. Ebadi, N. Einali Saghavaz, O. Y. Monem, and H. Mohammadzadeh, *Thermodynamic geometry of three coupled Ising spins: exact curvature, frustration and bond anisotropy*, arXiv:2611.08072v1 (5 November 2026), https://arxiv.org/abs/2611.08072 .

[2] C. Invernizzi, M. Korbman, L. C. Venuti, and M. G. A. Paris, *Optimal quantum estimation in spin systems at criticality*, Physical Review A 78, 042106 (2008), arXiv:0807.3213, https://arxiv.org/abs/0807.3213 .
