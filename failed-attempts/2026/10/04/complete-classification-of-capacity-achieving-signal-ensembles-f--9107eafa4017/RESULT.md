# Complete classification of capacity-achieving signal ensembles for qubit amplitude damping
## Finding
Let \(0<p<1\) and let \(\mathcal A_p\) be the qubit amplitude-damping channel
\[\mathcal A_p(\rho)=K_0\rho K_0^\dagger+K_1\rho K_1^\dagger,\qquad K_0=|0\rangle\!\langle0|+\sqrt{1-p}|1\rangle\!\langle1|,\quad K_1=\sqrt p\,|0\rangle\!\langle1|.\]
Define
\[g_p(q)=h_2\!\left(\frac{1+\sqrt{1-4p(1-p)q^2}}{2}\right),\qquad F_p(q)=h_2((1-p)q)-g_p(q).\]
Tang, Zhu, Bai and Wang prove that \(C(\mathcal A_p)=\max_{0\le q\le1}F_p(q)\) and that, for \(p<1\), the maximizing average input is unique. Since \(F_p\) is strictly concave, its maximizer \(q_*\) is unique and belongs to \((0,1)\).

A finite ensemble with positive probabilities \(\{(\pi_j,\rho_j)\}_{j=1}^m\) attains \(C(\mathcal A_p)\) if and only if there are phases \(\phi_j\) such that
\[\rho_j=|\psi_j\rangle\!\langle\psi_j|,\qquad |\psi_j\rangle=\sqrt{1-q_*}|0\rangle+e^{i\phi_j}\sqrt{q_*}|1\rangle,\qquad \sum_{j=1}^m\pi_j e^{i\phi_j}=0.\]
Thus all capacity-achieving letters lie on one latitude of the input Bloch sphere, and the only remaining freedom is a weighted phase polygon whose barycenter is the origin.

Equivalently, a prescribed positive probability vector \((\pi_1,\ldots,\pi_m)\) admits a capacity-achieving choice of phases if and only if
\[\max_j\pi_j\le\frac12.\]
For \(m=2\), this forces \(\pi_1=\pi_2=1/2\) and \(\phi_2-\phi_1=\pi\) modulo \(2\pi\). Hence the familiar binary ensemble is support-minimal and is unique up to a common phase and relabeling. For \(m\ge3\), regular phase polygons are only one subfamily; every weighted polygon satisfying the longest-side condition is optimal.
## Assumptions and scope
The statement concerns finite ensembles for the ordinary qubit amplitude-damping channel with \(0<p<1\), and the vanishing-error unassisted classical capacity established in arXiv:2609.28592v1. Zero-probability labels are discarded. The endpoint channels \(p=0\) and \(p=1\) are excluded because their equality structure is degenerate. The theorem classifies exact capacity-achieving single-use signal ensembles used in the product-state achievability of the capacity; it does not classify decoders, strong-converse behavior, or optimal ensembles for generalized finite-temperature amplitude damping.
## Proof
Write an arbitrary qubit state as
\[\rho=\begin{pmatrix}1-q&z\\ z^*&q\end{pmatrix},\qquad |z|^2\le q(1-q).\]
Its output is
\[\mathcal A_p(\rho)=\begin{pmatrix}1-(1-p)q&\sqrt{1-p}\,z\\ \sqrt{1-p}\,z^*&(1-p)q\end{pmatrix},\]
with determinant
\[\det\mathcal A_p(\rho)=p(1-p)q^2+(1-p)\bigl(q(1-q)-|z|^2\bigr).\]
For a qubit, entropy is a strictly increasing function of the determinant on \([0,1/4]\). Therefore, at fixed excitation \(q\),
\[S(\mathcal A_p(\rho))\ge g_p(q),\]
with equality, for \(0<p<1\) and \(0<q<1\), exactly when \(|z|^2=q(1-q)\), equivalently when \(\rho\) is pure.

Strict convexity is also exact. Put \(a=p(1-p)\), \(d=\sqrt{1-4aq^2}\). Differentiating gives, in bits,
\[g_p''(q)=\frac{4a}{\ln2}\,\frac{\operatorname{artanh}(d)-d}{d^3}>0\]
whenever \(0<d<1\), with the positive continuous limit at \(d=0\); the endpoint behavior preserves strict convexity on \([0,1]\). Hence Jensen equality for \(g_p\) occurs only when all averaged excitation probabilities coincide.

Now let \(\{(\pi_j,\rho_j)\}\) be capacity achieving and let \(q_j=\langle1|\rho_j|1\rangle\). Proposition 5.6 of arXiv:2609.28592v1 implies that the unique capacity-achieving average input is
\[\tau_*=(1-q_*)|0\rangle\!\langle0|+q_*|1\rangle\!\langle1|.\]
Thus \(\sum_j\pi_jq_j=q_*\). Its Holevo information obeys
\[\chi=S(\mathcal A_p(\tau_*))-\sum_j\pi_jS(\mathcal A_p(\rho_j))\le h_2((1-p)q_*)-\sum_j\pi_j g_p(q_j)\le F_p(q_*)=C(\mathcal A_p).\]
Because the ensemble attains capacity, both inequalities are equalities. Strict Jensen equality gives \(q_j=q_*\) for every positive-weight letter. Equality in the fixed-excitation entropy bound then makes every \(\rho_j\) pure. Hence each letter has the displayed latitude form for some \(\phi_j\). Averaging their off-diagonal entries shows that \(\tau_*\) is diagonal exactly when \(\sum_j\pi_j e^{i\phi_j}=0\). This proves necessity. Conversely, that phase-balance condition makes the average input exactly \(\tau_*\), while every output entropy equals \(g_p(q_*)\), so the ensemble has Holevo information \(F_p(q_*)\) and is capacity achieving.

Finally, unit complex numbers \(e^{i\phi_j}\) can satisfy \(\sum_j\pi_j e^{i\phi_j}=0\) exactly when the lengths \(\pi_j\) close to a planar polygon. The elementary polygon criterion is that the longest side not exceed the sum of the others, namely \(\max_j\pi_j\le1/2\). For two positive weights, cancellation of two vectors forces equal lengths and opposite directions. This proves the probability-vector and minimal-support statements.
## Verification
The proof is analytic. The accompanying `verify.py` independently checks the channel determinant identity, positivity of the strict-convexity formula on a parameter grid, numerical locations of \(q_*\), and exact Holevo equality for balanced two-, three-, and four-phase constellations. It also checks a mixed state at the same excitation has strictly larger output entropy. Running `python3 verify.py` prints `VERIFY_OK`.
## Relationship to prior work
Giovannetti and Fazio (arXiv:quant-ph/0405110v3, Sec. III.1, Eqs. (50)–(54)) derived the one-use Holevo formula and exhibited, for every alphabet size \(d>1\), an equal-weight regular phase polygon at fixed excitation. That is a sufficient family, not a necessity theorem and not a characterization of admissible probability vectors. Schumacher and Westmoreland (arXiv:quant-ph/9912122v1) proved general geometric properties of optimal signal ensembles, including equal relative-entropy distance, but did not specialize those conditions to classify amplitude-damping ensembles.

Tang, Zhu, Bai and Wang (arXiv:2609.28592v1) newly prove that the known one-use optimum equals the true unassisted classical capacity, derive the fixed-input output-entropy roof, and prove the unique optimal average input. They explicitly note that uniqueness of the average still allows different optimal ensembles. The result here closes that equality case: it gives necessary and sufficient conditions for every finite optimal alphabet and the exact probability-simplex criterion. A 2024 variational signal-state paper (DOI:10.1109/TQE.2024.3393416) studies binary discrimination and explicitly restricts its optimization to binary systems; it does not provide this Holevo-capacity classification.
## Limitations
No claim is made for \(p=0\) or \(p=1\), generalized amplitude-damping channels, infinite signal measures, finite-error coding, or decoder structure. The proof relies on the capacity/additivity and unique-average theorem of arXiv:2609.28592v1; without that recent many-use converse it would classify one-use Holevo optimizers rather than true capacity-achieving ensembles. The literature search found the regular-polygon sufficient construction and general optimal-ensemble geometry, but an equivalent necessity classification could conceivably exist under different terminology.
## References
1. Z. Tang, C. Zhu, G. Bai, and X. Wang, *Classical Capacity and Entanglement Cost of the Amplitude Damping Channel*, arXiv:2609.28592v1 (2026).
2. V. Giovannetti and R. Fazio, *Information-capacity description of spin-chain correlations*, arXiv:quant-ph/0405110v3; Phys. Rev. A 71, 032314 (2005), DOI:10.1103/PhysRevA.71.032314.
3. B. Schumacher and M. D. Westmoreland, *Optimal signal ensembles*, arXiv:quant-ph/9912122v1 (1999).
4. L. Oleynik, J. U. Rehman, H. Al-Hraishawi, and S. Chatzinotas, *Variational Estimation of Optimal Signal States for Quantum Channels*, IEEE Trans. Quantum Eng. 5 (2024), DOI:10.1109/TQE.2024.3393416.
