# Two hidden topology transitions in the five-active zero-mean oscillator polygon

## Finding

Consider the eight-oscillator Stuart–Landau model of Zhao and Uchida [1], with linearly spaced growth rates, positive cubic saturation, no nonlinear frequency shift, and complex all-to-all diffusive coupling at the stipulated ratio \(C_r=C_i/4\). In the open parameter region in which exactly the last five oscillators have positive rotating-state amplitude, the space of zero-mean phase-locked states modulo common phase rotation undergoes **two topology transitions without a change in active-oscillator count**.

Write \(h=\Delta\beta/7>0\) and
\[
 t=\frac{\beta_4-8C_r}{h}=\frac{0.01+3h-2C_i}{h},\qquad 0<t<1.
\]
Let \(t_0\) and \(t_1\) be the unique roots in \((0,1)\) of, respectively,
\[
 \sqrt t+\sqrt{t+1}+\sqrt{t+4}=\sqrt{t+2}+\sqrt{t+3},
\]
\[
 \sqrt{t+2}+\sqrt{t+4}=\sqrt t+\sqrt{t+1}+\sqrt{t+3}.
\]
Their rigorous rational enclosures are
\[
 0.020752<t_0<0.020754<0.386280<t_1<0.386282.
\]
Denote by \(\mathcal P_t\) the moduli space of all ordered phase configurations of the five nonzero oscillators satisfying zero mean, modulo simultaneous \(S^1\)-rotation **but not reflection**. Then for all \(t\in(0,1)\setminus\{t_0,t_1\}\), \(\mathcal P_t\) is a smooth closed orientable surface, with exact classification
\[
\begin{array}{c|c|c}
\text{parameter interval}& \text{homeomorphism type}&(b_0,b_1,b_2)\\\hline
(0,t_0)&T^2\sqcup T^2&(2,4,2)\\
(t_0,t_1)&\Sigma_2&(1,4,1)\\
(t_1,1)&\Sigma_3&(1,6,1).
\end{array}
\]
Here \(\Sigma_g\) denotes a connected closed orientable surface of genus \(g\). At each excluded threshold exactly one collinear polygonal shape occurs; the regular-value/smooth-surface hypothesis fails there. No smooth-manifold classification at either threshold is asserted. The two transition loci in the original parameters are the lines
\[
 C_i=0.005+\frac{3-t_j}{14}\,\Delta\beta,\qquad j\in\{0,1\},
\]
restricted to the five-active region. They are strictly internal to that region, unlike its activation boundaries.

## Assumptions and scope

The complex dynamical system is
\[
\dot z_j=\left(\beta_j+i\omega-k_r|z_j|^2\right)z_j+(C_r+iC_i)\sum_{\ell\ne j}(z_\ell-z_j),\quad j=1,\ldots,8,
\]
with \(\beta_j=0.01+(j-1)\Delta\beta/7\), \(\Delta\beta>0\), \(k_r=0.01\), \(\omega=0.2\), \(C_r=C_i/4\), and \(C_i>0\). Write \(Z=8^{-1}\sum_j z_j\). We restrict to relative equilibria \(z_j(s)=r_j e^{i(\Omega s+\theta_j)}\) with \(Z=0\), \(\Omega=\omega-8C_i\), and exactly indices \(j=4,\ldots,8\) nonzero. On that branch, \(r_j=\sqrt{(\beta_j-8C_r)/k_r}\). Such a branch is dynamically invariant but is **not claimed attracting**. Inactive oscillators have \(z_j=0\) and carry no phases; all five nonzero oscillators are distinguished by their indices. Reflection of a polygon is not identified unless a global rotation maps it to itself.

The five-active condition is \(\beta_3<8C_r<\beta_4\), equivalent to \(0<t<1\). Every such \(t\) is physically realizable for some \(\Delta\beta>0\), \(C_i>0\). Common positive scaling of \((r_4,\ldots,r_8)\) does not change the phase-closure space, giving length vector
\[
 L(t)=(\sqrt t,\sqrt{t+1},\sqrt{t+2},\sqrt{t+3},\sqrt{t+4}).
\]

## Proof

**Step 1: Reduction to a planar polygon space.** Substituting the rotating ansatz in the model and using \(Z=0\) gives \(r_j^2=(\beta_j-8C_r)/k_r\) for each nonzero oscillator. The remaining condition is \(\sum_{j=4}^8 r_je^{i\theta_j}=0\). After quotienting common rotation this is exactly the oriented planar five-link polygon moduli space \(\mathcal M_{L(t)}\) studied in [2]. The longest side \(e=\sqrt{t+4}\) is shorter than the sum of the other four for all \(0<t<1\), so the space is nonempty.

**Step 2: Exactly two walls.** Put \(a=\sqrt t\), \(b=\sqrt{t+1}\), \(c=\sqrt{t+2}\), \(d=\sqrt{t+3}\), \(e=\sqrt{t+4}\), so \(0<a<b<c<d<e\). A subset is short when its length sum is strictly below that of its complement. To apply [2], only subsets containing the unique longest side \(e\) are needed.

For pairs, \(\{e,a\}\) and \(\{e,b\}\) are always short: \(a+c+d-b-e\) is increasing, and its value at \(t=0\) equals \(\sqrt2+\sqrt3-3>0\). The pair \(\{e,d\}\) is always long: \(d+e-a-b-c\) is strictly decreasing, with positive value \(2+\sqrt5-1-\sqrt2-\sqrt3\) at \(t=1\). The remaining pair \(\{e,c\}\) is short exactly when
\(f_1(t)=c+e-a-b-d<0\). Its derivative is strictly negative, since \(c'<a'\), \(e'<d'\), and \(b'>0\); moreover \(f_1(0)>0\) and \(f_1(1)<0\). Hence it changes sign only at \(t_1\).

Every triple containing \(e\) except possibly \(\{e,a,b\}\) is long: already \(e+a+c>b+d\) holds because \(e>d\) and \(c>b\), and increasing any selected side can only increase its length-sum difference. The remaining triple is short precisely when \(f_0(t)=a+b+e-c-d<0\). Its derivative is strictly positive, since \(a'>c'\), \(b'>d'\), and \(e'>0\); also \(f_0(0)=3-\sqrt2-\sqrt3<0\) while \(f_0(1)>0\). Thus it changes sign exactly once at \(t_0\). Every subset containing \(e\) of size four or five is long. Rational interval enclosures based on integer square roots in the accompanying checker rigorously separate the two walls, locating them at the bounds in the statement. Consequently the lengths are generic away from precisely \(t_0,t_1\).

**Step 3: Complete topological classification.** Let \(a_k\) be the number of short \((k+1)\)-subsets containing \(e\). The preceding analysis yields
\[
 (a_0,a_1,a_2)=
 \begin{cases}
 (1,2,1),&0<t<t_0,\\
 (1,2,0),&t_0<t<t_1,\\
 (1,3,0),&t_1<t<1.
 \end{cases}
\]
The Farber–Schütz homology theorem [2, Theorem 1] applied with five links and no median subsets gives \((b_0,b_1,b_2)=(a_0+a_2,2a_1,a_0+a_2)\). Every generic planar pentagon space modulo rotations is an orientable compact surface of dimension two. In the first chamber, \(b_0=2\) and the disconnected-case theorem in [2] identifies two disjoint two-dimensional tori; in the other chambers \(b_0=1\) and \(b_1=2g\) gives genus two and three. At a wall exactly one subset-complement partition has equal sum, so the polygon corresponding to its two antiparallel directions is collinear and its closure constraint has deficient rank. The wall equations mapped back to \((\Delta\beta,C_i)\) give the two claimed internal lines.

## Verification

Run `python3 verify.py` using the Python standard library. Its exact-integer interval arithmetic bounds radicals at denominator \(10^{35}\), certifies signs at four rational endpoints bracketing the two unique roots, and independently enumerates all relevant short subsets in each of the three chambers. Its output is `VERIFY_OK exact_sign_checks 43 threshold_certificates 4 generic_topology_chambers 3`. The infinite classification relies on the derivative and ordering arguments above and the published polygon-space theorem, not on a finite grid. Source [1] was inspected in full for the reduction and [2] for the global polygon homology theorem.

## Relationship to prior work

Zhao and Uchida [1, Section 5] already derive the zero-order-parameter relative-equilibrium polygon and its active-number-dependent dimension. The present result does not claim that derivation or any transverse stability theorem. Farber and Schütz [2, Theorem 1 and subsequent examples] give a general Betti-number formula for arbitrary length vectors and a disconnected-torus criterion, which the proof above explicitly uses. Thus this is a **parameter-specific exact bifurcation classification within a dynamical model**, not a new general polygon-space homology theorem. These sources supply the framework, while the two threshold values, their uniqueness, and the full chamber allocation for the oscillator's square-root progression require the separate parameter-specific inequality analysis. Classical polygon spaces with arbitrary length vectors and equilateral pentagons do not list the present one-parameter oscillator family.

## Limitations

The claim concerns the set of rotating relative equilibria, not their basins, transverse Floquet stability, physical attractors, or chaos. No assertion about \(t\notin(0,1)\), other active-site counts, or the topological structure at the two non-generic wall points is made. The numerical root displays are enclosed rather than treated as defining exact data. Historical-priority searches cannot rule out specialized work on this precise square-root length family. The result depends on the already-published general polygon-space theorem and should be read as an exact dynamical-model application, not as independent polygon topology theory.

## References

[1] L. Zhao and N. Uchida, *Heterogeneity-induced chaos in globally coupled Stuart–Landau oscillators*, arXiv:2610.08239 (first posted October 6, 2026), https://arxiv.org/abs/2610.08239. Full text Section 2 and Section 5.

[2] M. Farber and D. Schütz, *Homology of planar polygon spaces*, Geometriae Dedicata **125** (2007), 75–92, arXiv:math/0609140; lawful full text https://www.maths.dur.ac.uk/users/dirk.schuetz/d15.pdf. Theorem 1, examples on pp. 3–4.
