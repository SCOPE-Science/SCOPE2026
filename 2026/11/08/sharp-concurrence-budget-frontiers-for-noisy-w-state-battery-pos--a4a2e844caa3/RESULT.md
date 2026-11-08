# Sharp concurrence-budget frontiers for noisy W-state battery postselection

## Finding

For the globally depolarized three-qubit W resource, there are **two different sharp, linear entanglement-budget laws** governing a selected auxiliary measurement outcome. Let the two-qubit rank-one measurement ray have pure-state concurrence at most \(\gamma\in[0,1]\). With the definitions and assumptions below, its success probability and conditional battery capacity are maximized at
\[
N_{\max}(\gamma)=\frac{4+2\gamma}{3},\qquad
P_{\max}(\gamma,p)=\frac p4+\frac{(1-p)(4+2\gamma)}9,
\]
while its conditional battery ergotropy is maximized at
\[
\mathcal E_{\max}(\gamma,p)
=\frac{8(1-p)(1+\gamma)}{3p+4(1-p)(1+\gamma)}\,\epsilon.
\]
The corresponding optimal conditional capacity and probability-weighted quantities are
\[
\mathcal C_{\max}(\gamma,p)
=\frac{8(1-p)N_{\max}(\gamma)}{3p+4(1-p)N_{\max}(\gamma)}\,\epsilon,
\]
\[
(P\mathcal C)_{\max}=\frac{2(1-p)}3N_{\max}(\gamma)\epsilon,
\qquad (P\mathcal E)_{\max}=\frac{2(1-p)}3(1+\gamma)\epsilon.
\]
All five bounds are attained. For every \(\gamma<1\), **no single measurement outcome** can attain both the success-probability and conditional-ergotropy maxima; for \(\gamma=1\), the symmetric Bell outcome attains both. This is an exact classification of the selected-branch measurement-concurrence budget, not an assertion about experimental entangling-gate cost or a full-cycle work balance.

## Assumptions and scope

Let \(A\) be the battery qubit and \(B,C\) be independently addressable auxiliary qubits. In computational order \(A,B,C\), use
\[
|W_3\rangle=(|100\rangle+|010\rangle+|001\rangle)/\sqrt3,
\quad \rho_p=(1-p)|W_3\rangle\langle W_3|+\frac p8 I_8.
\]
The battery Hamiltonian is \(H_A=\epsilon\sigma_z\) with \(\epsilon>0\), \(\sigma_z|0\rangle=|0\rangle\), and \(\sigma_z|1\rangle=-|1\rangle\). Assume \(0<p<1\), a complete rank-one projective measurement of \(BC\), and postselection on one outcome. Every normalized vector \(|v\rangle=a|00\rangle+b|01\rangle+c|10\rangle+d|11\rangle\) extends to a full projective measurement; we optimize this selected ray, not the remaining outcomes. Its concurrence is
\[
\Gamma(v)=2|ad-bc|\in[0,1],\qquad \Gamma(v)\le\gamma.
\]
Here \(\mathcal C\) denotes the battery capacity (maximum minus minimum energy over its unitary orbit), \(\mathcal E\) denotes ergotropy (actual energy minus passive-state energy), and \(P\) is the selected-outcome Born probability. Local unitaries on the battery are included in the definition of extractable work; preparation, postselection and reset costs are excluded.

## Proof

**1. Reduction to two quadratic forms.** Set \(q=|a|^2\), \(\zeta=|b+c|^2\), and \(N=q+\zeta\). Directly projecting the pure W component onto \(\langle v|\) gives the battery vector \((\overline{b+c},\overline a)^\top/\sqrt3\). Its unnormalized density matrix is
\[
\sigma_A(v)=\frac p8 I_2+\frac{1-p}{3}
\begin{pmatrix}\overline{b+c}\\\overline a\end{pmatrix}
\begin{pmatrix}b+c&a\end{pmatrix}.
\]
Consequently, and by sorting the two eigenvalues for the passive state,
\[
P=\frac p4+\frac{1-p}{3}N,\quad
\mathcal C=\frac{8(1-p)N}{3p+4(1-p)N}\,\epsilon,\quad
\mathcal E=\frac{8(1-p)\zeta}{3p+4(1-p)(q+\zeta)}\,\epsilon.
\]
The probability-weighted counterparts are \(P\mathcal C=2(1-p)N\epsilon/3\) and \(P\mathcal E=2(1-p)\zeta\epsilon/3\). For \(0<p<1\), probability and capacity strictly increase with \(N\). Ergotropy strictly increases with \(\zeta\) and weakly decreases with \(q\) (strictly for \(\zeta>0\)).

**2. Sharp success-probability bound.** Introduce \(u=(b+c)/\sqrt2\) and \(w=(b-c)/\sqrt2\). Put \(x=|a|\), \(y=|d|\), \(t=|w|\), and \(g=\Gamma(v)\). Normalization gives \(x^2+y^2+t^2+|u|^2=1\), while \(g=|2ad-u^2+w^2|\). The triangle inequality yields
\[
|u|^2\le g+2xy+t^2,
\quad 1-g\le(x+y)^2+2t^2.
\]
Weighted Cauchy–Schwarz and \(2t^2\le3t^2\) give
\[
(x+y)^2+2t^2\le\frac32(x^2+2y^2+2t^2).
\]
Since \(N=x^2+2|u|^2=2-x^2-2y^2-2t^2\), these inequalities imply
\[
N\le\frac{4+2g}{3}\le\frac{4+2\gamma}{3}.
\]
Sharpness is witnessed, for every \(\gamma\in[0,1]\), by the normalized real ray
\[
|v_P(\gamma)\rangle=
\frac{2\sqrt{1-\gamma}}3|00\rangle
+\sqrt{\frac{4+5\gamma}{18}}(|01\rangle+|10\rangle)
+\frac{\sqrt{1-\gamma}}3|11\rangle.
\]
It satisfies \(\Gamma(v_P)=\gamma\) and \(N(v_P)=(4+2\gamma)/3\). This proves the bounds for \(P,\mathcal C,P\mathcal C\).

**3. Sharp ergotropy bound.** The triangle inequality and \(2|ad|\le|a|^2+|d|^2\) yield
\[
\zeta\le |b|^2+|c|^2+2|bc|
\le 1-|a|^2-|d|^2+2|ad|+g\le1+g\le1+\gamma.
\]
For any fixed positive \(\zeta\), the ergotropy expression is maximized when \(q=0\). It is then strictly increasing in \(\zeta\) when \(0<p<1\). Both requirements can be met simultaneously: put
\[
|v_E(\gamma)\rangle=
\sqrt{\frac{1+\sqrt{1-\gamma^2}}2}|01\rangle
+\sqrt{\frac{1-\sqrt{1-\gamma^2}}2}|10\rangle.
\]
This normalized ray satisfies \(\Gamma(v_E)=\gamma\), \(q=0\), and \(\zeta=1+\gamma\). Substitution proves the sharp \(\mathcal E\) and \(P\mathcal E\) formulas.

**4. Incompatibility.** If \(\gamma<1\), then \(N_{\max}(\gamma)-(1+\gamma)=(1-\gamma)/3>0\). Every ergotropy-maximizing ray has \(q=0\) and \(\zeta=1+\gamma\); hence its \(N\) is strictly below the success optimum. At \(\gamma=1\), the two displayed witnesses both reduce to \((|01\rangle+|10\rangle)/\sqrt2\), which simultaneously optimizes all listed quantities. This completes the proof.

## Verification

The standalone script `check_frontier.py` verifies five exact symbolic equalities using SymPy, explicitly constructs both witness rays for eight concurrence budgets, compares the formulas against direct eight-dimensional density-matrix projection for four noise strengths, and tests the global inequalities and ergotropy frontier on 12,000 seeded complex rays. Its recorded execution completed 48,253 assertions. These tests are reproducibility checks, not a substitute for the analytic inequalities valid for every normalized complex ray.

Run `python check_frontier.py` with Python 3, NumPy and SymPy installed. The script is distributed with this result and does not require third-party source code or data.

## Relationship to prior work

Du, Zhou and Hu (2026, arXiv:2610.41121v1) introduced the exact selected-branch formulas, proved the entangled joint-versus-product gap for noisy \(W_3\), and computed the endpoint optima for product rays and unrestricted joint rays. Those formulas and endpoint values are prior results. The present claim interpolates between them under a **quantitative bound on the measurement ray's concurrence**, proving two distinct *sharp* continuous budget frontiers, their explicit equality states, and the incompatibility of their optimizers. No unrestricted generalized-eigenvalue principle or endpoint product/JL bound is claimed as new.

Wang, Liu, Fei and Zhang (2025, arXiv:2506.15074) studied local projective measurements of tripartite batteries and noise-robust capacity, rather than an entangled auxiliary measurement ray with a continuously restricted concurrence. A publicly indexed product-overlap frontier for generalized three-qubit W states concerns product-state acceptance and does not directly imply these concurrence-constrained postselected energetic quantities. Standard concurrence formulas and elementary inequalities are used as tools, not new mathematical principles.

## Limitations

The result concerns only a selected rank-one branch of the depolarized symmetric three-qubit W resource, a one-qubit battery, and a noiseless energy Hamiltonian. It does not include operation cost, postselection frequency across complete cycles, mixed auxiliary measurement effects, GHZ or general W amplitudes, or an operational resource theory of nonlocal measurement implementation. The parameter \(\gamma\) constrains the entanglement **of the selected measurement vector**, not the physical entanglement consumed by an apparatus. The boundary values \(p=0\) and \(p=1\) require separate monotonicity statements and are excluded from the main classification. Exact originality is asserted only relative to the accessible literature and indexed claims; publication-priority assessment by independent researchers has not been performed.

## References

1. Y. Du, Z. Zhou and X. Hu, *Entangled Measurement Outcomes for Optimal Postselection in Quantum Batteries*, arXiv:2610.41121v1 (first submitted 2026-10-30). https://arxiv.org/html/2610.41121v1
2. Y. Wang, H. Liu, S.-M. Fei and T. Zhang, *Improving Quantum Battery Capacity in Tripartite Quantum Systems by Local Projective Measurements*, arXiv:2506.15074v1 (first submitted 2025-06-18). https://arxiv.org/abs/2506.15074
3. F. Bernards, M. Kleinmann, O. Gühne and M. Paternostro, *Daemonic ergotropy: generalised measurements and multipartite settings*, Entropy 21 (2019), 771. https://doi.org/10.3390/e21080771
