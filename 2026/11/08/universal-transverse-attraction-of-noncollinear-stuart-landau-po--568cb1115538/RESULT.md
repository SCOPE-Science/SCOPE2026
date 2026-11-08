# Universal transverse attraction of noncollinear Stuart–Landau polygons under reactive coupling

## Finding
Let \(M\ge3\), \(k>0\), \(\beta_j>0\), \(\omega\in\mathbb R\), and \(\gamma\in\mathbb R\setminus\{0\}\). Consider the all-to-all complex Stuart–Landau flow
\[
\dot z_j=(\beta_j+i\omega-k|z_j|^2)z_j+i\gamma\sum_{\ell\ne j}(z_\ell-z_j),\qquad j=1,\ldots,M.
\]
For every **noncollinear closed polygon** \(w=(w_1,\ldots,w_M)\in\mathbb C^M\) with
\[
|w_j|=\sqrt{\beta_j/k},\qquad \sum_j w_j=0,\qquad
\dim_{\mathbb R}\operatorname{span}\{w_1,\ldots,w_M\}=2,
\]
the rotating orbit \(z_j(t)=e^{i(\omega-M\gamma)t}w_j\) belongs to a locally smooth, \((M-2)\)-dimensional manifold of phase-locked polygons. **Every normal Floquet exponent of that manifold has strictly negative real part**, while exactly \(M-2\) real rotating-frame eigenvalues are zero and semisimple. In a neighborhood of each such orbit, every initial condition converges exponentially, after removing the common rotation, to some nearby polygon in this manifold.

The same local normal attraction holds for **all sufficiently small positive dissipative coupling strengths** \(\varepsilon\) in the perturbed system
\[
\dot z_j=(\beta_j+i\omega-k|z_j|^2)z_j+(\varepsilon+i\gamma)\sum_{\ell\ne j}(z_\ell-z_j),
\]
using the nearby closed polygon with radii \(\sqrt{(\beta_j-M\varepsilon)/k}\). The permitted upper bound on \(\varepsilon\) depends on the fixed noncollinear polygon and parameters; no uniform upper bound is asserted.

For \(M=3\), strict triangle inequalities for the three radii guarantee such a noncollinear configuration. Therefore **both oriented heterogeneous triangular waves** are transversely attracting for every nonzero reactive strength and remain so at small positive dissipative strength.

## Assumptions and scope
All variables are complex with the standard Euclidean real inner product on \(\mathbb C^M\cong\mathbb R^{2M}\). Coupling is complete, reciprocal, unnormalized, and diffusive. The local nonlinear frequency-shift (Kerr) coefficient is zero; natural frequencies are identical, but positive growth rates \(\beta_j\) may be arbitrary and unequal. The polygon's noncollinearity is essential for the regular manifold argument. Exponential convergence is local and in the frame rotating at \(\Omega=\omega-M\gamma\), not a claim of global attraction or attraction to a prescribed polygon shape.

## Proof
**1. Exact rotating frame and polygon manifold.** Write \(z_j(t)=e^{i\Omega t}u_j(t)\), with \(\Omega=\omega-M\gamma\) and \(S(u)=\sum_j u_j\). For purely reactive coupling,
\[
\dot u_j=(\beta_j-k|u_j|^2)u_j+i\gamma S(u).
\]
Every polygon satisfying the stated radii and \(S(w)=0\) is an equilibrium. In angular coordinates \(u_j=r_j e^{i\theta_j}\), the closure map \(\theta\mapsto\sum_j r_j e^{i\theta_j}\) has real derivative whose columns are \(i w_j\). Noncollinearity means this derivative has real rank two. The implicit-function theorem gives a smooth equilibrium manifold of real dimension \(M-2\) through \(w\).

**2. Exact dissipative/skew decomposition.** The real-linear Jacobian \(A\) at \(w\) acts on \(v\in\mathbb C^M\) as
\[
(Av)_j=-2k\operatorname{Re}(\overline w_jv_j)w_j+i\gamma\sum_\ell v_\ell.
\]
Thus the symmetric part of \(A\) obeys the exact energy identity
\[
\langle v,Av\rangle_{\mathbb R}
=-2k\sum_j\bigl[\operatorname{Re}(\overline w_jv_j)\bigr]^2\le0.
\]
The mean-field operator \(v\mapsto i\gamma\sum v_\ell\) is skew-adjoint, so it makes no contribution. The matrix semigroup is a Euclidean contraction. Consequently every spectral real part is nonpositive, and any eigenvalue on the imaginary axis is semisimple (a nontrivial Jordan block would force polynomial growth in a contraction semigroup).

**3. Exclusion of all nonzero imaginary eigenvalues.** Complexify the real Jacobian. If \(Av=i\nu v\) for real nonzero \(\nu\), taking the Hermitian inner product with the eigenvector and its real part in the energy identity gives \(\langle w_j,v_j\rangle_{\mathbb C^2}=0\) in the complexified radial direction for every \(j\). Consequently the dissipative radial term vanishes, and
\[
i\nu v_j=\gamma J_2\sum_\ell v_\ell
\]
for each \(j\), where \(J_2\) is the real \(90^\circ\) rotation matrix. Since \(\nu\ne0\), every \(v_j\) must equal a common complexified two-vector \(v_0\). Yet this vector is orthogonal to each real vector \((\operatorname{Re}w_j,\operatorname{Im}w_j)\). Two noncollinear \(w_j\)'s span \(\mathbb R^2\), so \(v_0=0\), contradicting the eigenvector assumption. Hence no nonzero purely imaginary spectrum exists.

**4. Exact kernel and normal attraction.** If \(Av=0\), the dissipativity identity implies every \(v_j\) lies in the tangent direction \(i\mathbb Rw_j\). Since \(\gamma\ne0\), the eigenvalue equation then forces \(\sum_jv_j=0\). Conversely these conditions give \(Av=0\). By noncollinearity they impose two independent real constraints on the \(M\) tangential coefficients, so
\[
\ker A=T_w\mathcal P,\qquad\dim_{\mathbb R}\ker A=M-2.
\]
Zero is semisimple by Step 2, and Steps 2–3 show all remaining \(M+2\) eigenvalues have strictly negative real parts. A local compact patch of the smooth equilibrium manifold has a uniform normal spectral gap. The standard local normally-attracting invariant-manifold/stable-foliation theorem therefore gives exponential convergence in the co-rotating frame to a nearby equilibrium. In the laboratory frame this means exponential convergence to a rotating polygon with the same angular frequency, possibly a different nearby phase and shape.

**5. Small positive dissipative coupling.** Write \(C_r=\varepsilon\ge0\). In the same rotating frame the equation is
\[
\dot u_j=(\beta_j-M\varepsilon-k|u_j|^2)u_j+(\varepsilon+i\gamma)S(u).
\]
For small \(\varepsilon\), each squared polygon radius varies continuously as \((\beta_j-M\varepsilon)/k>0\). Rank-two closure persists at a nearby polygon by the implicit-function theorem, and the corresponding equilibrium manifold still has dimension \(M-2\). The Jacobian and its nonzero spectrum vary continuously. The \(M-2\) exact tangential zero eigenvalues persist, while the strictly negative normal spectrum remains in the open left half-plane for sufficiently small \(\varepsilon>0\). The same local stable-foliation argument applies.

For \(M=3\), strict triangle inequalities are necessary and sufficient for noncollinear closure with the prescribed radii. Reflection produces its second orientation, and Steps 1–5 apply to each.

## Verification
Run `python verify_reactive_polygons.py` using NumPy. The checker reconstructs the real Jacobian and independently tests both heterogeneous triangles (growth parameters \((1,3/2,2)\)) and heterogeneous quadrilaterals (growth parameters \((1,4,1,4)\)) for four positive/negative nonzero reactive strengths and for both zero and small positive dissipative coupling. It checks polygon closure, noncollinearity, expected zero-mode count, strict negativity of all computed normal eigenvalue real parts, and the exact symmetric-part matrix identity in the purely reactive cases. These finitely many numerical cases are independent sanity checks of the formulas, **not** the universal proof; Steps 1–5 establish the universal quantifiers.

## Relationship to prior work
Zhao and Uchida (2026) derive the vanishing-order-parameter polygon manifold and describe its stability through configuration sampling at a fixed coupling ratio \(C_r=C_i/4\), but do not give a general analytic theorem covering **every** noncollinear polygon at \(C_r=0\) for **arbitrary unequal positive growth rates**. The present theorem treats that distinguished conservative-coupling boundary exactly and proves persistence under small dissipative coupling.

Nicks, Allen and Coombes (2024) obtain exact transverse stability boundaries for **homogeneous** splay states of identical globally coupled oscillators. Their equal-amplitude assumptions do not imply the heterogeneous all-shape statement. León and Pazó (2020) study exact incoherent-state stability for **identical** globally coupled \(\lambda\)-\(\omega\) oscillators; the available abstract describes a different population assumption. The full text could not be assessed, so this remains a historical-priority uncertainty. Other splay-state and reactive-coupling literature addresses homogeneous or differently coupled configurations. Established matrix dissipativity and normal-hyperbolicity principles are used as tools, not claimed as inventions.

## Limitations
At collinear closed polygons, the closure constraint can be singular and the argument gives no complete nonlinear classification. The convergence theorem is local; its rate need not be uniform as \(\gamma\to0\) or as a polygon degenerates. No explicit positive numerical value of the persistence threshold in \(C_r\) is asserted. The result excludes nonlinear frequency shift, frequency heterogeneity, and incomplete or directed interaction graphs. Historical priority and independent validation remain open.

## References
1. L. Zhao and N. Uchida, *Heterogeneity-induced chaos in globally coupled Stuart–Landau oscillators*, arXiv:2610.08239v1, 6 October 2026. https://arxiv.org/html/2610.08239v1
2. R. Nicks, A. Allen and S. Coombes, *Insights into oscillator network dynamics using a phase-isostable framework*, *Chaos* (2024), DOI:10.1063/5.0179430. https://doi.org/10.1063/5.0179430
3. I. León and D. Pazó, *Quasi phase reduction of all-to-all strongly coupled \(\lambda-\omega\) oscillators near incoherent states*, *Physical Review E* **102** (2020), 042203. https://arxiv.org/abs/2006.02159
4. I. Lepri and A. Pikovsky, *Phase-locking dynamics of heterogeneous oscillator arrays*, arXiv:2112.04852, 2021. https://arxiv.org/abs/2112.04852
