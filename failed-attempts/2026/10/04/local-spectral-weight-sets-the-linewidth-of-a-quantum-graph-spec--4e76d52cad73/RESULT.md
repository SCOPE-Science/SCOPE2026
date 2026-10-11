# Local spectral weight sets the linewidth of a quantum-graph spectral filter

## Finding

Consider the attached-graph band-pass filter of Turek and Cheon. A finite compact quantum graph \(\Gamma\) is attached at a vertex \(v_0\) to an input-output line through their scale-invariant coupling with strength \(\alpha>0\). Restrict here to real bounded scalar edge potentials, no magnetic vector potential, and self-adjoint vertex conditions. Write
\[
c=\frac{\hbar^2}{2m},
\qquad
E=ck^2.
\]
Let \(E_0>0\) be a simple eigenvalue of the compact graph Hamiltonian \(H_\Gamma\), let \(\psi_0\) be an \(L^2\)-normalized eigenfunction, and assume
\[
\psi_0(v_0)\ne0.
\]
Then \(E_0\) is a visible filter resonance. If \(\Lambda(E)\) denotes the scalar Dirichlet-to-Neumann function used in the filter construction, normalized by boundary value \(1\) at \(v_0\), then
\[
\Lambda(E_0)=0,
\qquad
\Lambda'(E_0)=\frac{1}{c|\psi_0(v_0)|^2}.
\]

The source transmission formula therefore has a universal strong-coupling line shape. Put
\[
k_0=\sqrt{E_0/c}.
\]
For bounded real \(x\),
\[
P_\alpha\!\left(
E_0+\frac{2ck_0|\psi_0(v_0)|^2}{\alpha^2}x
\right)
\longrightarrow
\frac{1}{1+x^2}
\]
locally uniformly as \(\alpha\to\infty\).

For all sufficiently large \(\alpha\), there are exactly two local half-maximum energies
\[
E_-(\alpha)<E_0<E_+(\alpha)
\]
near \(E_0\), and
\[
E_\pm(\alpha)
=
E_0
\pm
\frac{2ck_0|\psi_0(v_0)|^2}{\alpha^2}
+
O(\alpha^{-4}).
\]
Their separation has the sharper expansion
\[
\operatorname{FWHM}_\alpha
=
E_+(\alpha)-E_-(\alpha)
=
\frac{4ck_0|\psi_0(v_0)|^2}{\alpha^2}
+
O(\alpha^{-6}).
\]

There is a second observable with the same local spectral weight. Choose a fixed sufficiently small closed interval \(J\) around \(E_0\) containing no other zero or singularity of \(\Lambda\). Then
\[
\alpha^2\int_J P_\alpha(E)\,dE
\longrightarrow
2\pi ck_0|\psi_0(v_0)|^2.
\]
Consequently,
\[
\frac{\int_J P_\alpha(E)\,dE}{\operatorname{FWHM}_\alpha}
\longrightarrow
\frac{\pi}{2}.
\]

Thus the narrow resonance peaks identified in the original spectral-filter construction are not merely located by the eigenvalues of \(H_\Gamma\): their leading width and area recover the local spectral mass \(|\psi_0(v_0)|^2\) at the attachment point.

## Assumptions and scope

The attached compact graph is finite, its scalar edge potentials are real and bounded, and its vertex conditions are self-adjoint. Magnetic vector potentials are excluded in order to keep the scalar Dirichlet-to-Neumann function and the Green-identity argument in the stated real form. The attachment vertex \(v_0\) has the free condition in the uncoupled compact graph, as in the source construction.

The theorem is local to a positive simple eigenvalue \(E_0\) with \(\psi_0(v_0)\ne0\). It does not cover invisible eigenvalues whose eigenfunctions vanish at the attachment vertex, multiple visible eigenvalues, threshold energy \(E_0=0\), or overlapping resonances. The interval \(J\) in the peak-area statement is fixed and small enough to contain no other zero or singularity of \(\Lambda\).

## Proof

For energies near \(E_0\), let \(u_E\) be the solution on \(\Gamma\) of
\[
(H_\Gamma-E)u_E=0
\]
with the same internal vertex conditions as \(H_\Gamma\) and with
\[
u_E(v_0)=1.
\]
Because \(E_0\) is simple and \(\psi_0(v_0)\ne0\), this boundary problem is regular near \(E_0\), and
\[
u_{E_0}=\frac{\psi_0}{\psi_0(v_0)}.
\]
The Dirichlet-to-Neumann function is the sum of outgoing derivatives at \(v_0\):
\[
\Lambda(E)=\sum_{e\sim v_0}\partial_\nu u_E(v_0).
\]
At \(E_0\), the free condition for the eigenfunction gives \(\Lambda(E_0)=0\).

Differentiate the boundary-value equation with respect to \(E\). If
\[
w=\left.\frac{\partial u_E}{\partial E}\right|_{E=E_0},
\]
then
\[
(H_\Gamma-E_0)w=u_{E_0},
\qquad
w(v_0)=0.
\]
Apply Green's identity to \(u_{E_0}\) and \(w\). All internal vertex contributions cancel by self-adjointness, while the attachment contribution is
\[
c\,u_{E_0}(v_0)\sum_{e\sim v_0}\partial_\nu w(v_0)
=
c\,\Lambda'(E_0).
\]
The volume term is
\[
\|u_{E_0}\|_2^2
=
\frac{1}{|\psi_0(v_0)|^2},
\]
because \(\psi_0\) is normalized. Therefore
\[
\Lambda'(E_0)
=
\frac{1}{c|\psi_0(v_0)|^2}.
\]

Turek and Cheon's transmission amplitude is
\[
T_\alpha(k)
=
\left(
1+\frac{\alpha^2\Lambda(E)}{2ik}
\right)^{-1}.
\]
For real regular energies, \(\Lambda(E)\) is real, so
\[
P_\alpha(E)
=
|T_\alpha(k)|^2
=
\left[
1+\alpha^4F(E)^2
\right]^{-1},
\qquad
F(E)=\frac{\Lambda(E)}{2k(E)}.
\]
At the resonance,
\[
F(E_0)=0,
\qquad
F'(E_0)
=
\frac{1}{2ck_0|\psi_0(v_0)|^2}.
\]

For
\[
E=E_0+\frac{2ck_0|\psi_0(v_0)|^2}{\alpha^2}x,
\]
Taylor expansion gives
\[
\alpha^2F(E)=x+O(\alpha^{-2})
\]
uniformly for \(x\) in any bounded set. Substitution into the probability formula proves the Lorentzian limit.

For the half-maximum points, \(P_\alpha(E)=1/2\) is equivalent locally to
\[
F(E)=\pm\alpha^{-2}.
\]
Since \(F'(E_0)>0\), the inverse-function theorem gives a local analytic inverse \(G\) with \(G(0)=E_0\). Hence
\[
E_\pm(\alpha)=G(\pm\alpha^{-2}).
\]
Because
\[
G'(0)=\frac{1}{F'(E_0)}=2ck_0|\psi_0(v_0)|^2,
\]
the individual expansions follow. In the difference
\[
G(\alpha^{-2})-G(-\alpha^{-2}),
\]
all even Taylor powers cancel. Therefore
\[
\operatorname{FWHM}_\alpha
=
\frac{4ck_0|\psi_0(v_0)|^2}{\alpha^2}
+
O(\alpha^{-6}).
\]

Finally, shrink \(J\) if necessary so that \(F\) is one-to-one there and \(E_0\) is its only zero. With \(y=\alpha^2F(E)\),
\[
\alpha^2\int_J P_\alpha(E)\,dE
=
\int_{\alpha^2F(J)}
\frac{G'(y/\alpha^2)}{1+y^2}\,dy.
\]
The endpoints tend to \(-\infty\) and \(+\infty\), while \(G'(y/\alpha^2)\) is uniformly bounded on the transformed interval and converges pointwise to \(G'(0)\) on every fixed \(y\)-range. Dominated convergence therefore gives
\[
\lim_{\alpha\to\infty}
\alpha^2\int_JP_\alpha(E)\,dE
=
\pi G'(0)
=
2\pi ck_0|\psi_0(v_0)|^2.
\]
Dividing by the FWHM asymptotic gives the universal ratio \(\pi/2\).

## Verification

`verify_filter_linewidth.py` checks an exactly solvable compact graph: one interval of length \(L\), attached at one endpoint and carrying a Neumann condition at the other. For the \(n\)-th positive compact-graph eigenvalue,
\[
k_0=\frac{n\pi}{L},
\qquad
|\psi_0(v_0)|^2=\frac{2}{L},
\qquad
\Lambda(E)=k\tan(kL).
\]
The checker verifies the derivative coefficient and uses the exact local half-maximum roots
\[
k_\pm
=
k_0
\pm
\frac{1}{L}\arctan\!\left(\frac{2}{\alpha^2}\right).
\]
Thus the exact energy FWHM is
\[
4ck_0\,\frac{1}{L}
\arctan\!\left(\frac{2}{\alpha^2}\right),
\]
whose leading term is exactly
\[
\frac{8ck_0}{L\alpha^2}
=
\frac{4ck_0|\psi_0(v_0)|^2}{\alpha^2}.
\]
The script also checks the half-maximum equations and the rescaled Lorentzian line shape over several lengths, kinetic constants, eigenmodes, and coupling strengths. It prints `VERIFY_OK`.

The computation is supplementary. The all-graph statement rests on Green's identity and the local inverse-function argument above.

## Relationship to prior work

Turek and Cheon derive the exact transmission amplitude
\[
T(k)
=
\left(
1+\frac{\alpha^2\Lambda(E)}{2ik}
\right)^{-1}
\]
for a compact graph attached to an input-output line. They prove that, as \(\alpha\to\infty\), the transmission probability tends to one at visible compact-graph eigenenergies and to zero away from them. Their paper repeatedly describes the resulting passbands as “narrow” or “sharp” peaks, but the inspected full text does not state a linewidth formula; a full-text search for “width” returns no occurrence.

Bandwidth formulas do exist in related but different quantum-graph filter designs. In *Potential-controlled filtering in quantum star graphs*, Turek and Cheon compute the bandwidth of a threshold/star-graph passband controlled by an external potential and a vertex parameter. Turek's later *On quantum graph filters with flat passbands* likewise studies a different vertex filter whose flat-passband width is controlled by auxiliary-edge potentials. Those results do not identify the linewidth of the attached-compact-graph resonance peaks with the local spectral weight of an eigenfunction.

The identity
\[
\Lambda'(E_0)=\frac{1}{c|\psi_0(v_0)|^2}
\]
is a scalar Weyl-function/Dirichlet-to-Neumann norm identity specialized to this attachment normalization. Combining it with the source transmission formula produces the stated Lorentzian scaling, FWHM, area, and local-spectral-weight interpretation. Targeted searches for the source title together with “linewidth,” “FWHM,” “peak width,” “local spectral weight,” and “eigenfunction value” did not locate the displayed result.

## Limitations

The result is a local simple-resonance theorem. Multiple eigenvalues can require a matrix-valued or higher-rank local analysis, and invisible eigenvalues remain blocked by the attachment geometry. Magnetic vector potentials are not treated here. At finite \(\alpha\), the peak need not be exactly Lorentzian, and the theorem does not claim a global decomposition of the entire transmission curve into independent resonances.

The originality claim is intentionally narrow. The exact transmission formula, resonance locations, and strong-coupling indicator limit are prior work. The contribution assessed here is the quantitative local line-shape theorem that ties the width and area of those peaks to \(|\psi_0(v_0)|^2\). An equivalent statement may exist in literature using Weyl-function or boundary-triple terminology that was not surfaced by the searches.

## References

1. O. Turek and T. Cheon, “Quantum graph as a quantum spectral filter,” *Journal of Mathematical Physics* 54, 032104 (2013), arXiv:1206.1931, DOI: 10.1063/1.4795404.
2. O. Turek and T. Cheon, “Potential-controlled filtering in quantum star graphs,” *Annals of Physics* 330 (2013), 104–141, arXiv:1203.6555, DOI: 10.1016/j.aop.2012.11.011.
3. O. Turek, “On quantum graph filters with flat passbands,” arXiv:1512.09366 (2015); later published in *Functional Analysis and Operator Theory for Quantum Physics*.
4. R. Carlson, “Dirichlet to Neumann maps for infinite quantum graphs,” *Networks and Heterogeneous Media* 7 (2012), 483–501, arXiv:1109.3132, DOI: 10.3934/nhm.2012.7.483.
