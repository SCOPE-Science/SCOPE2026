# A sharp period-two extinction-and-reentry crossover in an Anosov-driven Möbius map

## Finding

Consider the three-torus skew diffeomorphism introduced by Chigarev, Kazakov and Pikovsky, on its zero-phase-offset slice:
\[
\mathcal F(t,s,x)=\left(2t+s,\ t+s,\ x+\omega+\mu\sin(2\pi t)-\frac1\pi\arctan\frac{\varepsilon\sin(2\pi x)}{1+\varepsilon\cos(2\pi x)}\right)\pmod1.
\]
Assume \(0<\mu<1/2\), \(0<\varepsilon<1\), and \(0\leq\omega<1/2\). Put
\[
\sigma_H=\sin(2\pi/5),\quad\sigma_L=\sin(\pi/5),\quad
u_j=\pi\mu\sigma_j\quad (j=H,L),
\]
and define four exact boundaries
\[
L_j=\frac1\pi\arcsin(\varepsilon\cos u_j),\qquad
U_j=\frac12-\frac1\pi\arcsin(\varepsilon\sin u_j).
\]
Every **primitive period-two orbit** of \(\mathcal F\) projects onto one of the two primitive period-two orbits of its cat-map base. The complete count of primitive period-two orbits is
\[
N_2(\omega)=n_H(\omega)+n_L(\omega),\quad
n_j(\omega)=\begin{cases}
2,&0\leq\omega<L_j\ \text{or}\ U_j<\omega<1/2,\\
1,&\omega=L_j\ \text{or}\ \omega=U_j,\\
0,&L_j<\omega<U_j.
\end{cases}
\]
In particular, every bifurcation endpoint contributes a **single isolated parabolic orbit**, never an identity-return circle. The two pairs of boundaries always satisfy \(0<L_H<L_L<U_L<1/2\) and \(L_H<U_H<U_L\).

There is a **sharp crossover** at
\[
\boxed{\varepsilon_*(\mu)=\bigl(\cos^2 u_L+\sin^2 u_H\bigr)^{-1/2}\in(0,1).}
\]
For \(\varepsilon<\varepsilon_*\), the interval \((L_L,U_H)\) is nonempty and contains **no primitive two-cycle**. At \(\varepsilon=\varepsilon_*\), the two boundaries meet, leaving exactly two isolated parabolic two-cycles at their common value. For \(\varepsilon>\varepsilon_*\), the interval \((U_H,L_L)\) instead contains **four primitive two-cycles**: two above each of the two distinct base cycles. This is a reentrant period-two coexistence window, even though each base cycle separately has an intervening interval with no period-two fiber fixed point.

The signed width of the central transition, \(W(\varepsilon)=L_L-U_H\), crosses zero transversely:
\[
W(\varepsilon)=\frac{(\cos^2u_L+\sin^2u_H)^{3/2}}{\pi\cos u_L\sin u_H}
\bigl(\varepsilon-\varepsilon_*\bigr)+O_\mu\bigl((\varepsilon-\varepsilon_*)^2\bigr).
\]
The full count at all threshold equalities follows from the piecewise formula, not from limiting counts on adjacent open intervals.

## Assumptions and scope

The phase space is \(\mathbb T^3=(\mathbb R/\mathbb Z)^3\). Its two-dimensional base is the toral automorphism with matrix \(\begin{psmallmatrix}2&1\\1&1\end{psmallmatrix}\). The third coordinate is an orientation-preserving Möbius circle diffeomorphism because \(0<\varepsilon<1\). The parameter \(\omega\) denotes the frequency mismatch \(c\) in the originating model; the phase shift \(\alpha\) of that paper is fixed to zero here. The bounds \(0<\mu<1/2\) and \(0\leq\omega<1/2\) are essential to this theorem and avoid finite-order fiber returns at excluded resonances. A primitive period-two orbit is an unordered two-point orbit of exact least period two, rather than two separately counted fixed points of the second iterate. All trigonometric inverse functions use their principal real branches.

The theorem counts **every** primitive two-cycle of the full three-dimensional system within this parameter domain, not merely normally attracting cycles or cycles visible in a numerical experiment.

## Proof

**1. Exhaust the base.** Let \(A=\begin{psmallmatrix}2&1\\1&1\end{psmallmatrix}\). Since \(|\det(A-I)|=1\) and \(|\det(A^2-I)|=5\), the only fixed base point is \((0,0)\), while exactly four other base points have least period two. Explicitly they form
\[
(1/5,2/5)\leftrightarrow(4/5,3/5),\qquad
(2/5,4/5)\leftrightarrow(3/5,1/5).
\]
Their first-coordinate sequences are \(1/5,4/5\) and \(2/5,3/5\), respectively. Consequently the two forcing increments along base cycle \(j\) are \(\omega+\mu\sigma_j\) and \(\omega-\mu\sigma_j\), with \(\sigma_H=\sin(2\pi/5)\) and \(\sigma_L=\sin(4\pi/5)=\sin(\pi/5)\). The two possible cyclic starting points give conjugate two-step fiber returns and hence the same fixed-point count.

**2. Compute the exact return trace.** With \(z=e^{2\pi i x}\), the fiber step at shift \(v\) is
\[
z\longmapsto e^{2\pi i v}\frac{z+\varepsilon}{1+\varepsilon z}.
\]
Here the given arctangent is the continuous argument because \(1+\varepsilon\cos(2\pi x)>0\). A determinant-one matrix representative is \(M_v=U_vB\), where
\[
B=(1-\varepsilon^2)^{-1/2}
\begin{pmatrix}1&\varepsilon\\\varepsilon&1\end{pmatrix},\qquad
U_v=\begin{pmatrix}e^{i\pi v}&0\\0&e^{-i\pi v}\end{pmatrix}.
\]
The return above base cycle \(j\) is represented by
\[
P_j=M_{\omega-\mu\sigma_j}M_{\omega+\mu\sigma_j},\qquad
\frac12\operatorname{tr}P_j=
\frac{\cos(2\pi\omega)+\varepsilon^2\cos(2\pi\mu\sigma_j)}{1-\varepsilon^2}=:h_j(\omega).
\]
The expression \(h_j(\omega)\) strictly decreases as \(\omega\) ranges over \((0,1/2)\), from a value greater than one to a value less than minus one. The equations \(h_j=1\) and \(h_j=-1\) have exactly the respective solutions \(L_j\) and \(U_j\) written above. By the classification of real circle Möbius maps, \(|h_j|>1\) gives two boundary fixed points and \(|h_j|<1\) none; a nonidentity parabolic matrix with \(|h_j|=1\) gives one.

**3. Exclude identity returns on the boundaries.** The upper-right entry of \(P_j\) is
\[
(P_j)_{12}=\frac{2\varepsilon e^{i\pi(\omega-\mu\sigma_j)}}{1-\varepsilon^2}
\cos\bigl(\pi(\omega+\mu\sigma_j)\bigr).
\]
If \(P_j\) were scalar, this entry would vanish, forcing \(\omega+\mu\sigma_j=1/2\) in the stipulated ranges. At that value the first Möbius factor is a projective involution, and the product is a pure rotation. It can be scalar only if the second shift also equals \(1/2\) modulo one. Their difference is \(2\mu\sigma_j\in(0,1)\), so this is impossible. Hence the \(|h_j|=1\) endpoints are genuine nonidentity parabolics, each with exactly one circle fixed point.

**4. Exclude period-two orbits above the base fixed point.** Above \((t,s)=(0,0)\), the fiber map is the autonomous Möbius map \(M_\omega\), with determinant-one trace \(2\cos(\pi\omega)/\sqrt{1-\varepsilon^2}\). An orientation-preserving real Möbius circle map possesses a nonfixed point of least period two only if its projective action has order two, which requires a trace-zero matrix. Because \(0\leq\omega<1/2\), the trace is strictly positive. There are therefore no additional primitive two-cycles. This proves the exhaustive count formula.

**5. Order the boundaries and prove the crossover.** Since \(0<u_L<u_H<\pi/2\), monotonicity of sine, cosine and arcsine gives \(L_H<L_L\) and \(U_H<U_L\). For every \(j\), strict \(\varepsilon<1\) implies
\[
\arcsin(\varepsilon\cos u_j)+\arcsin(\varepsilon\sin u_j)<\pi/2,
\]
so \(L_j<U_j\). Consequently the only undetermined relative order is that of \(L_L\) and \(U_H\). For positive \(A,B<1\),
\[
\arcsin A+\arcsin B\ \mathrel{\lessgtr}\ \pi/2
\quad\Longleftrightarrow\quad A^2+B^2\ \mathrel{\lessgtr}\ 1.
\]
Taking \(A=\varepsilon\cos u_L\) and \(B=\varepsilon\sin u_H\) gives the stated \(\varepsilon_*\). Because \(u_H>u_L\), the sum \(\cos^2u_L+\sin^2u_H\) exceeds one, so \(0<\varepsilon_*<1\). The resulting two possible strict boundary orders are
\[
\begin{array}{ll}
\varepsilon<\varepsilon_*:& L_H<L_L<U_H<U_L,\\
\varepsilon>\varepsilon_*:& L_H<U_H<L_L<U_L.
\end{array}
\]
Inserting these orders into the proved contribution formula gives the claimed zero-cycle gap, crossing, and four-cycle reentry. At equality, both relevant return matrices are nonidentity parabolic, hence give exactly one orbit each. Finally differentiating
\(W(\varepsilon)=\pi^{-1}\bigl[\arcsin(\varepsilon\cos u_L)+\arcsin(\varepsilon\sin u_H)\bigr]-1/2\)
and substituting \(\varepsilon_*=(\cos^2u_L+\sin^2u_H)^{-1/2}\) gives the positive derivative and the stated Taylor law.

## Verification

The standalone Python 3 program `verify.py` uses exact rational arithmetic to exhaust the base second-iterate fixed points, forms the full complex Möbius matrices independently of the closed trace formula, and tests determinant, return trace, circle-boundary roots, four parabolic boundaries, the critical ordering, and the positive crossover slope. It uses only Python's standard library. Run `python3 verify.py`; it prints `CHECK_OK` on success. The program performs finite consistency tests; the unlimited parameter and orbit-count statements follow from the analytic proof, not from enumeration or numerical tolerance. As a concrete example, \(\mu=0.3\) gives \(\varepsilon_*\approx0.866038843300\).

## Relationship to prior work

Chigarev, Kazakov and Pikovsky (2023) introduced this driven Möbius model, describe periodic-driver returns, and numerically plotted bifurcation curves for driving periods through seven. Their Section IV and Möbius appendix establish the tools for a trace analysis. In the full accessible arXiv text, they do not provide the exact four period-two thresholds, the complete endpoint census, or the critical forcing \(\varepsilon_*\) at which a period-two extinction interval is replaced by four-cycle coexistence. The present theorem does **not** assert that this finite-period threshold determines the global attractor–repeller collision, which can involve other base periods or nonperiodic trajectories.

An earlier published calculation of the same cat-driven system on the more restrictive \(\omega=0\) slice establishes arithmetic identity resonances and an exact two-cycle count there. Its conclusions do not imply the drift-dependent hyperbolic-to-elliptic-to-hyperbolic reentry or the critical forcing boundary proved here. The matrix group identities themselves are classical and are not claimed as new.

## Limitations

The theorem applies only to \(0<\mu<1/2\), \(0<\varepsilon<1\), \(0\leq\omega<1/2\), with zero phase offset. The excluded endpoint \(\omega=1/2\) has additional period-two points above the **fixed** base orbit because its one-step fiber Möbius map has order two; thus the half-open restriction cannot simply be dropped. The theorem classifies period two, not higher periods, chaotic attractors, global transport, or a rigorous global heterodimensional transition. Exact prior equivalences outside the inspected sources remain possible. Independent validation has not been performed.

## References

1. V. Chigarev, A. Kazakov, A. Pikovsky, *Attractor-repeller collision and the heterodimensional dynamics*, arXiv:2305.18172v1, first public 2023-05-29; *Chaos* **33**, 063113 (2023), DOI 10.1063/5.0144672. Full text: https://arxiv.org/html/2305.18172v1 .
2. *Arithmetic isolation of identity resonances in a cat-driven Möbius map*, published research note (2026), full text: https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-arithmetic-isolation-of-identity-resonances-in-a-cat-driven-m-bi--a1ced3096486/RESULT.md .
3. V. Chigarev, A. Kazakov, A. Pikovsky, *Mutual singularities of overlapping attractor and repeller*, *Chaos* **31**, 083127 (2021), DOI 10.1063/5.0056891; abstract: https://pubmed.ncbi.nlm.nih.gov/34470236/ .
