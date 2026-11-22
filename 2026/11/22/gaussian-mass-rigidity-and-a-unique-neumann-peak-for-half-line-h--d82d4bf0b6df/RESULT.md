# Gaussian-mass rigidity and a unique Neumann peak for half-line heat commutators

## Finding
Let \(P_t^{\mathrm N}\) and \(P_t^{\mathrm D}\) be the Neumann and Dirichlet heat semigroups for \(\Delta=d^2/dx^2\) on \(L^2(0,\infty)\), with \(t>0\). For a measurable set \(E\subset(0,\infty)\) of finite Lebesgue measure, set \(C_t^{\mathrm N}(E)=[P_t^{\mathrm N},M_{\mathbf1_E}]\) and define \(C_t^{\mathrm D}(E)\) analogously. Both are Hilbert–Schmidt. With the normalized Gaussian boundary mass
\[
q_t(E)=\sqrt{\frac{2}{\pi t}}\int_E e^{-x^2/(2t)}\,dx,
\]
there is an **exact geometry-blind boundary-condition contrast**
\[
\boxed{\|C_t^{\mathrm N}(E)\|_{\mathcal S_2}^2-\|C_t^{\mathrm D}(E)\|_{\mathcal S_2}^2=q_t(E)(1-q_t(E))\le\frac14.}
\]
The bound \(1/4\) is attained exactly by sets with Gaussian mass \(q_t(E)=1/2\); finite intervals can attain it.

For the boundary-attached interval \(E=(0,L)\), put \(c=L/\sqrt t\), \(A(c)=\int_0^c e^{-u^2/2}\,du\), and \(Q(c)=\int_c^\infty e^{-u^2/2}\,du\). Then the two individual squared norms are exactly
\[
\boxed{F_{\pm}(c)=\frac{1-e^{-2c^2}+2cQ(2c)\ \pm\ 2A(c)Q(c)}{2\pi},}
\]
where \(F_+\) denotes Neumann and \(F_-\) Dirichlet. The Dirichlet function is strictly increasing to \(1/(2\pi)\). The Neumann function is strictly increasing up to one and only one \(c_*>0\), then strictly decreasing to \(1/(2\pi)\) from above. The peak is the unique root of
\[
Q(2c_*)=e^{-c_*^2/2}(A(c_*)-Q(c_*)),
\]
with \(c_*=0.7990017881788918\ldots\) and \(F_+(c_*)=0.2719729564300915\ldots\). At the absorbing boundary, the small-interval singular mass is suppressed by two additional powers:
\[
F_+(c)\sim \sqrt{2/\pi}\,c,\qquad F_-(c)\sim\frac{c^3}{6\sqrt{2\pi}},\qquad \frac{F_+(c)}{F_-(c)}\sim\frac{12}{c^2}\quad(c\downarrow0).
\]

## Assumptions and scope
The underlying measure is Lebesgue measure on the positive half-line. The semigroup generator is \(d^2/dx^2\) (not \(\tfrac12d^2/dx^2\)); therefore the heat kernel is \(g_t(u)=(4\pi t)^{-1/2}e^{-u^2/(4t)}\). The multipliers are orthogonal projections \(M_{\mathbf1_E}\) for arbitrary measurable finite-measure sets. All operator norms appearing in the theorem are the Hilbert–Schmidt norm squared, except where explicitly stated. Statements about interval peaks require exactly \(E=(0,L)\). No regularity, connectedness, or perimeter condition is imposed on the general mask.

## Proof
**1. Kernel reduction and finiteness.** The method of images gives
\[
k_t^{\pm}(x,y)=g_t(x-y)\pm g_t(x+y),\qquad x,y>0,
\]
with \(+\) for Neumann and \(-\) for Dirichlet. For a measurable mask, the commutator kernel is \((\mathbf1_E(y)-\mathbf1_E(x))k_t^{\pm}(x,y)\). Since \((a\pm b)^2\le 2(a^2+b^2)\) for real \(a,b\), and \(\sup_x\int_0^\infty g_t(x\pm y)^2dy<\infty\), its squared integral is bounded by a constant times \(|E|/\sqrt t\). Therefore both commutators are Hilbert–Schmidt, and by symmetry
\[
\|C_t^{\pm}(E)\|_{\mathcal S_2}^2=2\int_E dx\int_{(0,\infty)\setminus E}dy\,k_t^{\pm}(x,y)^2.
\]
**2. Geometry-blind gap.** The pointwise identity \((a+b)^2-(a-b)^2=4ab\), together with
\[
g_t(x-y)g_t(x+y)=\frac1{4\pi t}e^{-(x^2+y^2)/(2t)},
\]
implies
\[
\|C_t^{\mathrm N}(E)\|_{\mathcal S_2}^2-\|C_t^{\mathrm D}(E)\|_{\mathcal S_2}^2=\frac2{\pi t}\left(\int_E e^{-x^2/(2t)}dx\right)\left(\int_{E^c}e^{-y^2/(2t)}dy\right).
\]
The full Gaussian mass on the half-line is \(W_t=\sqrt{\pi t/2}\). Substitution gives exactly \(q_t(E)(1-q_t(E))\). The elementary quadratic bound is sharp precisely at Gaussian half-mass. The interval \((0,\sqrt{2t}\,\operatorname{erf}^{-1}(1/2))\) provides equality.

**3. Boundary interval formula.** Dilation \(x=\sqrt t\,u\) and \(y=\sqrt t\,v\) reduces the norms to
\[
F_{\pm}(c)=\frac1{2\pi}\int_0^c du\int_c^\infty dv\,[e^{-(v-u)^2/4}\pm e^{-(v+u)^2/4}]^2.
\]
Write \(Q(z)=\int_z^\infty e^{-w^2/2}dw\). The two square terms integrate to \(\int_0^c Q(c-u)du\) and \(\int_0^c Q(c+u)du\), whose sum is \(1-e^{-2c^2}+2cQ(2c)\). The mixed integral factors as \(A(c)Q(c)\). This proves the displayed exact expressions. The large-\(c\) limits are \(1/(2\pi)\); the small-\(c\) laws follow by Taylor expansion, or for the Dirichlet term by \(e^{-(v-u)^2/4}-e^{-(v+u)^2/4}=uv e^{-v^2/4}+o(u)\) in the rescaled double integral and dominated convergence.

**4. Strict shape classification.** Put \(W=\sqrt{\pi/2}\), so \(A(c)+Q(c)=W\). Direct differentiation gives
\[
F_{\pm}'(c)=\frac1\pi\{Q(2c)\pm e^{-c^2/2}[Q(c)-A(c)]\}.
\]
For Dirichlet let \(H(c)=e^{c^2/2}Q(2c)+2A(c)-W\). Then \(H(0)=0\) and
\[
H'(c)=c e^{c^2/2}Q(2c)+2e^{-3c^2/2}(e^{c^2}-1)>0\quad(c>0).
\]
Thus \(F_-'(c)=e^{-c^2/2}H(c)/\pi>0\). For Neumann set \(G(c)=e^{c^2/2}Q(2c)-2A(c)+W\). We have \(G(0)=2W>0\) and \(G(c)\to-W\) as \(c\to\infty\). For \(c>0\), the Mills bound \(Q(2c)<e^{-2c^2}/(2c)\) implies
\[
G'(c)=c e^{c^2/2}Q(2c)-2e^{-3c^2/2}-2e^{-c^2/2}<0.
\]
There is one positive zero, where \(F_+'\) changes from positive to negative. Numerical values above merely locate this uniquely proved peak. Finally the first nonzero terms of the Taylor expansions are \(F_+(c)=\sqrt{2/\pi}\,c+O(c^2)\) and \(F_-(c)=c^3/(6\sqrt{2\pi})+O(c^5)\), proving the quoted ratio.

## Verification
The standalone `checker.py` evaluates the exact half-line kernels by adaptive quadrature for multiple times and interval masks, tests the general Gaussian-mass identity for disconnected masks, checks the derivative signs over a dense numerical grid, and independently computes the peak. The script reports 10,053 successful assertions in a standard Python/SciPy environment. The infinite-dimensional theorem, global sharpness, and strict monotonicity rely on the analytic proof, not on finite numerical testing.

## Relationship to prior work
Schilling (first public preprint 2020) treats short-time heat content for fixed smooth sets on boundaryless manifolds; it does not give an exact finite-time contrast of Dirichlet and Neumann half-line commutators for arbitrary measurable masks or a boundary-scale peak. Duong and collaborators (first public preprint 2017) develop weighted BMO and Riesz-transform commutators in Dirichlet/Neumann settings; their operators and conclusions are different. Kovács, Lang and Petersson (2021 preprint) study Schatten regularity for integral covariance operators with these boundary conditions, not the exact difference of two squared commutator norms. The elementary reflected heat kernels are classical and constitute an essential premise; the work does not claim to discover them. Other Gaussian-interface crossover results use different operators and do not imply the mask-invariant quadratic contrast or the unique interval peak.

## Limitations
This is an exact Hilbert–Schmidt result for the one-dimensional half-line Laplacian with indicator multipliers. It gives neither trace-norm asymptotics nor an assertion of analogous universal constants for other semigroups, higher dimensions, or general bounded multipliers. Distinct masks with the same Gaussian mass have the same **contrast**, not necessarily the same two individual norms. Classical heat-content or method-of-images literature might contain an equivalent formulation not located here; independent priority and mathematical review remain outstanding.

## References
- N. Schilling, *Short-time heat content asymptotics via the wave and eikonal equations*, arXiv:2001.08789, first public 2020-01-23; Journal of Geometric Analysis 31 (2021), 2172–2181. https://arxiv.org/abs/2001.08789
- X. T. Duong, I. Holmes, J. Li, B. D. Wick, D. Yang, *Two weight commutators in the Dirichlet and Neumann Laplacian settings*, arXiv:1705.06858, first public 2017-05-19; Journal of Functional Analysis 276 (2019), 1007–1060. https://arxiv.org/abs/1705.06858
- M. Kovács, A. Lang, A. Petersson, *Hilbert–Schmidt regularity of symmetric integral operators on bounded domains with applications to SPDE approximations*, arXiv:2107.10104, first public 2021-07-21; Stochastic Analysis and Applications 41 (2023), 564–590. https://arxiv.org/abs/2107.10104
