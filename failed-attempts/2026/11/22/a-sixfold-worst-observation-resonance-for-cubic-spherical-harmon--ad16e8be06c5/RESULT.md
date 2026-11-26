# A sixfold worst-observation resonance for cubic spherical harmonics on eight cubical caps

## Finding
Let \(V=\{(\varepsilon_1,\varepsilon_2,\varepsilon_3)/\sqrt3:\varepsilon_i\in\{-1,1\}\}\), and for \(\sqrt{2/3}\le h<1\) set
\[
\Omega_h=\bigcup_{v\in V}\{x\in S^2:x\cdot v\ge h\}.
\]
The Slepian energy-concentration operator \(T_h\) on the complex seven-dimensional exact-degree-three spherical harmonic space \(\mathcal H_3(S^2)\), defined by \(\langle f,T_hg\rangle=\int_{\Omega_h}\overline f g\,d\sigma\) with \(\sigma(S^2)=1\), has exactly three eigenvalue branches (listed here with algebraic multiplicity, allowing branch coincidences):
\[
\begin{aligned}
A(h)&=\frac{(1-h)(120h^6+120h^5-69h^4-69h^3+h^2+h+36)}9,&&[1],\\
B(h)&=\frac{(1-h)^2(60h^5+120h^4+61h^3+2h^2+13h+24)}6,&&[3],\\
C(h)&=\frac{(1-h)(300h^6+300h^5-393h^4-393h^3+97h^2+97h+216)}{54},&&[3].
\end{aligned}
\]
Throughout the stated domain \(A(h)>\max\{B(h),C(h)\}>0\). There is a unique internal crossing
\[
h_*=\sqrt{\frac{33+\sqrt{249}}{60}}=0.9016626663934014\ldots
\]
with \(C(h)<B(h)\) for \(\sqrt{2/3}\le h<h_*\), \(B(h)<C(h)\) for \(h_*<h<1\), and \(B(h_*)=C(h_*)\). Thus the least observable cubic-harmonic space jumps between distinct three-dimensional octahedral representations and has multiplicity six precisely at \(h_*\). The sharp squared restriction condition number is \(\kappa(h)=A(h)/\min\{B(h),C(h)\}\), and
\[
\kappa(h)\sim\frac{1}{3(1-h)}\quad(h\uparrow1).
\]

## Assumptions and scope
The eight caps are counted once each; their interiors are disjoint since \(h\ge\sqrt{2/3}\). At the endpoint the boundaries may touch at measure-zero locations. All integrals are relative to uniform probability area measure. Harmonics are complex-valued; the stated real polynomial representatives also span their complex eigensectors. This is a **single exact harmonic degree**, not a complete low-pass band. The condition number is the ratio of squared singular values, not its square root.

## Proof
Use homogeneous harmonic cubics, restricted to \(S^2\), and write \(x=(x_1,x_2,x_3)\). The signed-permutation group preserves \(\Omega_h\) and the full-sphere norm. Its invariant orthogonal decomposition of \(\mathcal H_3\) is
\[
\begin{aligned}
U_A&=\operatorname{span}\{x_1x_2x_3\},\\
U_B&=\operatorname{span}\{x_1(x_2^2-x_3^2),x_2(x_3^2-x_1^2),x_3(x_1^2-x_2^2)\},\\
U_C&=\operatorname{span}\{x_i(5x_i^2-3):i=1,2,3\}.
\end{aligned}
\]
The final three representatives are harmonic on the sphere because their homogeneous extensions are \(x_i(5x_i^2-3\lVert x\rVert^2)\). Signed-coordinate reflections eliminate all off-diagonal products except possible same-coordinate \(B\)--\(C\) terms; swapping the other two coordinates reverses the \(B\) factor while preserving the \(C\) factor, eliminating those too. Permutation symmetry makes each sector scalar. Their dimensions sum to seven, and full-sphere norms for the respective displayed basis elements are \(1/105\), \(4/105\), and \(4/7\).

Around \(v=(1,1,1)/\sqrt3\), use \(x=t v+\sqrt{1-t^2}(\cos\phi\,e+\sin\phi\,f)\), \(t\in[h,1]\), where \(e=(1,-1,0)/\sqrt2\), \(f=(1,1,-2)/\sqrt6\). The azimuthal average of the square of one representative from each sector, denoted \(p_A,p_B,p_C\), is exactly
\[
\begin{aligned}
p_A(t)&=(24t^6-27t^4+6t^2+1)/108,\\
p_B(t)&=(1-t^2)(12t^4-5t^2+1)/18,\\
p_C(t)&=(300t^6-495t^4+210t^2+17)/54.
\end{aligned}
\]
The eight cap contributions to every squared representative agree under coordinate signs. Because the spherical probability area element in these coordinates is \(dt\,d\phi/(4\pi)\), division by the full norm gives exactly \(\lambda_j(h)=4\int_h^1p_j(t)\,dt/\lVert F_j\rVert^2\). Elementary integration yields the three displayed eigenvalues.

Their exact factorizations are
\[
\begin{aligned}
A-B&=\frac{35h(1-h^2)(12h^4-9h^2+1)}{18},\\
A-C&=\frac{7h(1-h^2)(60h^4-3h^2-13)}{54},\\
B-C&=-\frac{14h(1-h^2)(30h^4-33h^2+7)}{27}.
\end{aligned}
\]
The quadratic polynomials in \(h^2\) in the first two lines are positive on \([2/3,1)\), establishing the unique top eigenbranch. The final polynomial has exactly one zero in this interval, namely \(h_*^2=(33+\sqrt{249})/60\); its sign gives both regimes and the sixfold coincidence. Positivity of each branch follows from integrating nonzero analytic squared harmonics over open caps. Taylor expansion at \(h=1\) yields \(A\sim(140/9)(1-h)\), \(B\sim(140/3)(1-h)^2\), \(C\sim(112/27)(1-h)\), and the claimed sharp condition-number divergence follows.

## Verification
The standalone `verify_eight_caps.py` uses exact symbolic azimuthal integration to reproduce the three sixth-degree moment polynomials, all three spherical norms, all eigenvalue formulas, difference factorizations and crossing. Independently, it performs six seven-dimensional numerical Galerkin integrations over all eight caps with 14-point Gaussian polar quadrature and a 32-point periodic azimuthal rule, checking every matrix entry against the predicted diagonal spectrum to a \(5\times10^{-12}\) tolerance. Run `python verify_eight_caps.py` with Python, NumPy and SymPy. Exact symbolic calculations, together with the analytic decomposition and factorizations above, rather than finite numerical tests, establish the continuum theorem.

## Relationship to prior work
Michel, Plattner and Seibert (first public March 26, 2021) developed a general scalar/vector/tensor spherical Slepian framework and commuting operators for spherical-cap regions; they did not derive the three branches on this eight-disconnected-cap mask in the inspected manuscript sections. Roddy and McEwen (first public June 3, 2021) developed wavelets for incomplete spherical regions, not the present eigenspectrum. Indexed summaries of closer published computations treat four tetrahedrally centered caps at cubic degree, six octahedrally centered caps at quartic degree, and two antipodal caps at cubic degree. Their stated operators have different observation sets or harmonic degrees; their reported phase transitions therefore do not imply the eight-cap six-dimensional **minimum** resonance here. This nonimplication is specific to the statements inspected and does not establish global priority.

## Limitations
The caps must be equal, centered at all eight cube vertices and nonoverlapping. For lower thresholds they overlap and the integral formula changes. The result is exact for degree three on the ordinary two-sphere, not for general degrees, nonuniform weights, other shapes, or arbitrary incomplete-sphere data. Independent mathematical audit and exhaustive historical-priority verification have not been performed. Some related indexed results were compared via summaries rather than their complete texts.

## References
1. V. Michel, A. Plattner and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650v1 (first public 2021-03-26), https://arxiv.org/abs/2103.14650.
2. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02023v1 (first public 2021-06-03), https://arxiv.org/abs/2106.02023.
3. *A fourfold optimal-mode transition in tetrahedral-cap cubic spherical harmonics*, published research record, 2026-11-08 (comparison of four rather than eight caps).
4. *Exact fourth-degree octahedral-cap concentration and a triple-to-simple optimal-mode transition*, published research record, 2026-11-08 (comparison of six caps and degree four).
5. *Cubic spherical harmonics on antipodal caps: two exact symmetry switches*, published research record, 2026-11-08 (comparison of two caps).
