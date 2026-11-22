# Exact fourth-period energy and Möbius conjugacy in the McMillan sextupole map

## Finding
For each real \(a\), let the rational symplectic map be
\[
F_a(q,p)=\left(p,-q+\frac{p(a-p)}{1+p}\right),\qquad p\ne-1,
\]
and let its polynomial first integral be
\[
K_a(q,p)=q^2+p^2-aqp+qp(q+p).
\]
For every \(a\ne-1\), the **complete set of real points of least period four** is
\[
\operatorname{Per}_4^*(F_a)=
\left\{(q,p)\in\mathbb R^2:K_a(q,p)=-a\right\}
\setminus\left(\{(-1,-1)\}\cup E_a\right),
\]
where \(E_0=\{(0,0)\}\), \(E_8=\{(2,2)\}\), and \(E_a=\varnothing\) otherwise. In particular, this set contains a real one-dimensional continuum for **every** \(a\ne-1\). At the exceptional value \(a=-1\), there are **no** real points of least period four on any forward-defined orbit.

On the entire regular energy curve \(K_a=-a\) away from \((-1,-1)\), the dynamics is explicitly
\[
F_a(q,p)=\bigl(p,g_a(q)\bigr),\qquad
F_a^2(q,p)=\bigl(g_a(q),g_a(p)\bigr),\qquad
g_a(t)=\frac{a-t}{1+t},\quad g_a^2(t)=t.
\]
At every smooth point of this energy curve, the fourth-return derivative has both Floquet multipliers equal to one.

## Assumptions and scope
The map is defined wherever the input second coordinate differs from \(-1\); a point is \(n\)-periodic only when all \(n\) successive iterates are well defined and the \(n\)-th iterate returns it to its initial state. The theorem concerns real coordinates and all real parameters, with no boundedness or stability-domain hypothesis. The excluded point \((-1,-1)\) is a pole of the original rational mapping. The polynomial \(K_a\) and its normalization agree with the sextupole invariant of Zolkin, Nagaitsev and Morozov after setting the sextupole length scale \(\Gamma=1\) and the linear trace parameter \(a=-2\epsilon/\Gamma\).

## Proof
**1. The invariant and the torsion identity.** Put \(f_a(t)=t(a-t)/(1+t)\) and \(H_a(q,p)=K_a(q,p)+a\). Direct rational cancellation gives
\[
K_a\bigl(p,f_a(p)-q\bigr)=K_a(q,p)
\]
whenever \(p\ne-1\). For \(a\ne-1\), define the fractional-linear involution \(g_a(t)=(a-t)/(1+t)\). Two further exact identities are
\[
g_a(g_a(t))=t,\qquad
f_a(p)-q-g_a(q)=-\frac{H_a(q,p)}{(1+p)(1+q)}.
\]
The denominator restrictions are essential. Indeed,
\[
H_a(-1,p)=(a+1)(p+1),\qquad H_a(q,-1)=(a+1)(q+1).
\]
Consequently, for \(a\ne-1\) any point on \(H_a=0\) other than \((-1,-1)\) avoids both coordinate poles. The displayed second identity yields \(F_a(q,p)=(p,g_a(q))\). Invariance preserves this curve on iteration, so the next three iterates are defined, the stated formula for \(F_a^2\) holds, and \(F_a^4=\mathrm{id}\) on the curve.

**2. Converse for every primitive fourth-period orbit.** Write the successive scalar coordinates of a primitive fourth-period orbit as \(q,p,t,u\), so that its four states are \((q,p),(p,t),(t,u),(u,q)\). The recurrence supplies
\[
f_a(p)=q+t,\quad f_a(t)=p+u,\quad
f_a(u)=t+q,\quad f_a(q)=u+p.
\]
Thus \(f_a(p)=f_a(u)\) and \(f_a(q)=f_a(t)\). For any distinct \(v,w\) in the domain,
\[
\frac{f_a(v)-f_a(w)}{v-w}=
\frac{a+1}{(1+v)(1+w)}-1.
\]
At least one of \(p\ne u\) and \(q\ne t\) must hold, or the orbit would have period at most two. If \(p\ne u\), the preceding equality gives \((1+p)(1+u)=a+1\), whence \(u=g_a(p)\). As \(f_a(q)=u+p\), the torsion identity with the two inputs exchanged implies \(H_a(q,p)=0\). If instead \(q\ne t\), then \(t=g_a(q)\), and \(f_a(p)=q+t\) gives \(H_a(q,p)=0\) directly. The possibility \(a=-1\) is treated separately below. This proves necessity for \(a\ne-1\).

**3. Removing lower periods.** On \(H_a=0\), the condition \(F_a^2(q,p)=(q,p)\) is exactly \(g_a(q)=q\) and \(g_a(p)=p\). Real fixed points of \(g_a\) solve \((t+1)^2=a+1\). If \(a<-1\), none exist. If \(a>-1\), put \(s=\sqrt{a+1}>0\). The possible coordinates are \(s-1\) and \(-s-1\). Substitution into \(H_a\) yields, respectively,
\[
\begin{array}{c|c}
(q,p)&H_a(q,p)\\ \hline
(s-1,s-1)&-s^2(s-1)(s-3)\\
(-s-1,-s-1)&-s^2(s+1)(s+3)\\
(s-1,-s-1)\ \text{or}\ (-s-1,s-1)&s^2(s^2+3).
\end{array}
\]
Only \(s=1\) or \(s=3\) makes an allowed value zero. These give \(a=0\), \((q,p)=(0,0)\), and \(a=8\), \((q,p)=(2,2)\), both fixed points of \(F_a\). No other period-one or period-two exceptions exist. All remaining points on \(H_a=0\) therefore have least period four.

**4. Nonemptiness and the exceptional trace.** For every \(a\ne-1\), \(H_a(-1,-1)=0\) and
\[
\nabla H_a(-1,-1)=(a+1,a+1)\ne(0,0).
\]
The implicit-function theorem supplies a nontrivial smooth real arc of \(H_a=0\) passing through this one excluded point. All its other sufficiently nearby points are regular for the rational dynamics and, except finitely many isolated lower-period exceptions, have least period four. For \(a=-1\), the rational expression simplifies on its original domain to \(F_{-1}(q,p)=(p,-q-p)\), a linear transformation of order three. Every forward-defined orbit obeys \(F_{-1}^3=\mathrm{id}\), so least period four is impossible.

**5. Neutrality on the regular curve.** The Jacobian of \(F_a\) is \(\bigl(\begin{smallmatrix}0&1\\-1&f'_a(p)\end{smallmatrix}\bigr)\), of determinant one. At a smooth point of \(H_a=0\), its tangent line is preserved by \(D(F_a^4)\) and the fourth iterate restricts to the identity along the curve. Its tangential multiplier is one, so determinant one forces the other multiplier to equal one as well. No assertion is made about the Jordan type or singular points of the energy curve.

## Verification
The standalone `checker.py` uses exact symbolic rational algebra to verify preservation of \(K_a\), the fractional-linear involution, the crucial torsion identity, the pairwise force identity, the pole restrictions, and all four lower-period substitution formulas. It also verifies exact rational four-step examples at \(a=11,-4,-8/5\), plus the exceptional fixed state at \(a=8\). It requires Python and SymPy; run `python checker.py` in the extracted directory. These computations corroborate, but do not replace, the proof for every real parameter. In particular no finite sampling establishes the infinite classification.

## Relationship to prior work
Zolkin–Nagaitsev–Morozov (2022), the expanded *Dynamics of McMillan mappings I* (first public 2024), and the general symmetric-map study *Dynamics of McMillan mappings III* (first public 2024) provide the sextupole force and first integral, elliptic parametrizations, action-angle and rotation-number descriptions, and the degenerate three-cycle at \(a=-1\). Their inspected discussions of isolated fixed points, two-cycles and resonances do not give this global explicit least-period-four energy equation, the simple Möbius fourth-return form on it, or the complete pole/lower-period census. The statement is compatible with the established general fact that a QRT-type map acts as a translation on a generic invariant genus-one curve; it identifies the precise real four-torsion level for this specific sextupole family by an elementary calculation.

The earlier Iatrou–Roberts works (2001, 2002) develop general normal forms for biquadratic invariant maps; only their public abstracts were accessible. Their possible uninspected period-four implications remain a research-priority risk. Similarly, the later 2026 article on invariant volume forms for three-dimensional QRT maps was checked for broad context and supplies no inspected matching explicit sextupole fourth-period locus. The result is claimed as an explicit complete classification relative to checked evidence, **not** as a certified first-in-literature theorem.

## Limitations
This is a classification of **least-period-four points**, not of all periodic or bounded trajectories. The rational map is undefined at poles and is not replaced by its projective birational compactification. No orbital attraction, global phase-portrait description, or period classification beyond four is asserted. The four-point orbit of a generic level point may lie on an unbounded component, and parameter \(a=-1\) is a removable-degeneracy special case only after an extension. Publication priority remains subject to general QRT literature not available in full text. Independent mathematical audit has not been performed.

## References
1. T. Zolkin, S. Nagaitsev, I. Morozov, *McMillan map and nonlinear Twiss parameters*, arXiv:2204.12691v1 (public April 27, 2022), https://arxiv.org/html/2204.12691v1.
2. T. Zolkin, S. Nagaitsev, I. Morozov, *Dynamics of McMillan mappings I. McMillan multipoles*, arXiv:2405.05652 (public May 9, 2024), https://arxiv.org/html/2405.05652v2.
3. T. Zolkin, S. Nagaitsev, I. Morozov et al., *Dynamics of McMillan mappings III. Symmetric map with mixed nonlinearity*, arXiv:2410.10380 (public October 14, 2024), https://arxiv.org/html/2410.10380v3.
4. A. Iatrou and J. A. G. Roberts, *Integrable mappings of the plane preserving biquadratic invariant curves*, J. Phys. A 34 (2001), 6617–6636, https://doi.org/10.1088/0305-4470/34/34/308.
5. A. Iatrou and J. A. G. Roberts, *Integrable mappings of the plane preserving biquadratic invariant curves II*, Nonlinearity 15 (2002), 459–489, https://doi.org/10.1088/0951-7715/15/2/313.
