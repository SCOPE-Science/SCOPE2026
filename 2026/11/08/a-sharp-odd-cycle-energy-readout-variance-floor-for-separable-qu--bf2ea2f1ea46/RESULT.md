# A sharp odd-cycle energy-readout variance floor for separable quantum chargers

## Finding

For every odd integer \(n\geq3\), take a cyclic array of \(n\) charger qubits coupled to a battery qubit in the fully separable density operator specified below. Among **all fixed, nonadaptive, rank-one local product-projective readouts of the chargers**, the exact variance of the conditional battery excited-state probability is

\[
\boxed{\inf_{\mathcal M_{\rm prod}}\operatorname{Var}_{\mathcal M_{\rm prod}}(E_B)= (2^n\delta)^2\min\!\left\{h^2,\frac{nJ^2}{2}\bigl[1-\cos(\pi/n)\bigr]\right\}.}
\]

Both branches are attainable. If \(h^2\) exceeds the second entry, uniformly twisted equatorial readout axes minimize variance; when \(h^2\) is below it, one vertical readout axis and an alternating orthogonal equatorial path minimize variance. There is a sharp crossover at \(h/J=\sqrt{n[1-\cos(\pi/n)]/2}\), asymptotic to \(\pi/(2\sqrt n)\). Positive \(h,J,\delta\) imply a strictly positive floor even though the entire preparation is fully separable.

The exact graph extension is that complete branch-energy equalization by such a product readout is possible for the same construction on a finite simple graph \(G\) **if and only if \(G\) is bipartite** (provided \(h,J,\delta>0\)). This feasibility obstruction is a qualitative corollary of familiar local-orthogonality constraints; the quantitative odd-cycle minimum and its crossover are the assessed contribution.

## Assumptions and scope

Let \(G=(V,E)\) be a finite undirected simple graph with \(n=|V|\) vertices and Pauli matrices \(X_i,Y_i,Z_i\) on charger \(i\). Let \(h,J>0\), and define

\[
H_G=h\sum_{i\in V}Z_i+J\sum_{\{i,j\}\in E}(X_iX_j+Y_iY_j), \quad d=2^{n+1}.
\]

The battery computational basis is \(\{|0\rangle,|1\rangle\}\), with \(Z_B=|1\rangle\langle1|-|0\rangle\langle0|\). Consider the joint (chargers plus battery) density matrix

\[
\rho_{G,\delta}=\frac{I_d}{d}+\delta H_G\otimes Z_B,\qquad
0<\delta\leq\bigl[d(nh+2|E|J)\bigr]^{-1}.
\]

For each charger vertex select an arbitrary Bloch unit vector \(\boldsymbol a_i=(a_i^x,a_i^y,z_i)\in\mathbb S^2\). Measure the local observables \(\boldsymbol a_i\cdot\boldsymbol\sigma_i\) simultaneously and without feedforward. An outcome is a sign vector \(\boldsymbol s\in\{\pm1\}^n\); \(E_B(\boldsymbol s)\) is the conditional probability of measuring \(|1\rangle_B\), equivalently the expected normalized battery Hamiltonian \(|1\rangle\langle1|\). The objective is **variance across readout branches of these conditional mean energies**, not intrinsic quantum energy variance within a branch and not the dynamics of a repeated-collision charging protocol. Here and below every minimization ranges over all such fixed product bases, with no restriction to the equator.

The parameter range makes \(\rho_{G,\delta}\) **fully separable**, not merely positive: expand \(H_G\otimes Z_B\) into \(n+2|E|\) Pauli strings \(P_\ell\) with positive coefficients \(c_\ell\in\{h,J\}\). Writing \(w_\ell=d\delta c_\ell\) and \(w_0=1-\sum_\ell w_\ell\geq0\),

\[
\rho_{G,\delta}=w_0\frac{I_d}{d}+\sum_\ell w_\ell\frac{I_d+P_\ell}{d}.
\]

Each \((I_d+P_\ell)/d\) is a normalized state diagonal in a tensor product of single-qubit Pauli eigenbases, hence a mixture of product pure states; the displayed decomposition proves full separability. Taking strict inequality in the bound on \(\delta\) also makes the joint density matrix full rank.

## Proof

**1. Exact measurement law.** For a sign vector \(\boldsymbol s\), the charger projector is \(\Pi_{\boldsymbol s}=\bigotimes_{i\in V}(I+s_i\boldsymbol a_i\cdot\boldsymbol\sigma_i)/2\). Since \(\operatorname{Tr}H_G=0\), all outcomes have probability \(2^{-n}\). The normalized conditional battery density matrix is

\[
\rho_{B|\boldsymbol s}=\frac{I_2}{2}+2^n\delta F(\boldsymbol s)Z_B,\qquad
F(\boldsymbol s)=h\sum_i s_i z_i+J\sum_{\{i,j\}\in E}s_is_j(a_i^xa_j^x+a_i^ya_j^y).
\]

Consequently \(E_B(\boldsymbol s)=1/2+2^n\delta F(\boldsymbol s)\). The parity characters \(s_i\) and \(s_is_j\) are distinct nonconstant orthogonal Walsh characters under the uniform sign law (simplicity of \(G\) is used here). Their mean vanishes. Thus

\[
\operatorname{Var}(E_B)=(2^n\delta)^2Q_G(\boldsymbol a),\quad
Q_G=h^2\sum_i z_i^2+J^2\sum_{\{i,j\}\in E}\bigl(\boldsymbol u_i\cdot\boldsymbol u_j\bigr)^2,
\]

where \(\boldsymbol u_i=(a_i^x,a_i^y)\in\mathbb R^2\) and \(\|\boldsymbol u_i\|^2+z_i^2=1\).

**2. General graph zero criterion.** All terms in \(Q_G\) are nonnegative. Because \(h>0\), \(Q_G=0\) forces \(z_i=0\) at every vertex, so each \(\boldsymbol u_i\) is a planar unit vector. Because \(J>0\), every edge then joins perpendicular planar vectors. The perpendicular direction to a given planar line is uniquely determined as an unoriented line. Moving around any cycle alternates between two perpendicular lines, so an odd cycle cannot close. Thus \(G\) must be bipartite. Conversely, for any bipartite graph assign the \(x\) axis on one color class and the \(y\) axis on the other, which gives \(Q_G=0\). This statement includes disconnected graphs by applying the coloring componentwise.

**3. Reduction to equator-or-vertical axes on an odd cycle.** Write \(t_i=\|\boldsymbol u_i\|^2\in[0,1]\), \(\boldsymbol u_i=\sqrt{t_i}(\cos\phi_i,\sin\phi_i)\) where a phase at \(t_i=0\) may be arbitrary. On \(G=C_n\),

\[
Q_{C_n}=h^2\sum_{i=0}^{n-1}(1-t_i)+J^2\sum_{i=0}^{n-1}t_it_{i+1}\cos^2(\phi_i-\phi_{i+1}),
\]

with indices modulo \(n\). At fixed angles, this function is affine in each \(t_i\) separately. Replacing \(t_0,t_1,\ldots,t_{n-1}\) successively by whichever endpoint \(0\) or \(1\) gives no larger objective. Hence its global minimum is attained with all \(t_i\in\{0,1\}\); minimizing over angles afterwards preserves this conclusion. If at least one \(t_i=0\), the field term is at least \(h^2\). This lower bound is attained with **exactly one** vertical axis and all other axes equatorial, alternating orthogonal \(x,y\) along the remaining path. The minimum within this branch is precisely \(h^2\).

**4. Exact all-equatorial branch.** If \(t_i=1\) for every \(i\), put \(\boldsymbol v_i=(\cos2\phi_i,\sin2\phi_i)\). Then

\[
\sum_{i=0}^{n-1}\cos^2(\phi_i-\phi_{i+1})
=\frac n2+\frac12\sum_{i=0}^{n-1}\boldsymbol v_i\cdot\boldsymbol v_{i+1}.
\]

For odd \(n\), the adjacency matrix of the cycle has least eigenvalue \(-2\cos(\pi/n)\), by its discrete Fourier eigenvalues \(2\cos(2\pi k/n)\). Applying the Rayleigh bound to both real coordinate vectors of \(\boldsymbol v_i\) gives

\[
\sum_i\boldsymbol v_i\cdot\boldsymbol v_{i+1}\geq -n\cos(\pi/n).
\]

Equality holds for the unit planar Fourier mode \(\boldsymbol v_i=(\cos[\pi(n-1)i/n],\sin[\pi(n-1)i/n])\), which is realized by the charger measurement angles \(\phi_i=\pi(n-1)i/(2n)\). Therefore the equatorial branch has exact minimum \(J^2n[1-\cos(\pi/n)]/2\). Combining both branches yields the boxed theorem, its exact optimal configurations, and the crossover. The asymptotic threshold follows from \(1-\cos(\pi/n)\sim\pi^2/(2n^2)\).

**5. Explicit three-charger witness.** For \(n=3\), \(h=J=1\) and \(\delta=1/256\), the separability bound holds because \(d=16\) and \(nh+2nJ=9\). The optimal squared-energy dispersion is exactly

\[
(8/256)^2\cdot\frac34=\frac{3}{4096},\qquad
\sqrt{\operatorname{Var}(E_B)}=\frac{\sqrt3}{64}.
\]

The state can be expressed as a convex combination of \(I_{16}/16\) with weight \(7/16\) and nine normalized Pauli projectors \((I_{16}+P_\ell)/16\) with weight \(1/16\) each. This displays a completely classical-separable source with an unavoidable positive **conditional-mean** readout variance under the stated fixed local measurement restriction.

## Verification

Run `python3 verify.py` using only the Python standard library. The checker reconstructs independent small Pauli matrices, evaluates Born expectations for random product bases, checks Walsh-Parseval identities, independently tests both analytic optimizer constructions over odd cycles, checks the exact three-site variance, and conducts bounded randomized searches for violations. Its finite numerical diagnostics are not used to infer a universal optimization theorem: Steps 1–4 above supply the analytic proof, including global minimization over all Bloch spheres.

## Relationship to prior work

Gong, Zhang and Li (2026) investigate uniform expected battery charging through **adaptive two-charger-qubit measurements** within a collision model; they do not present the quantified fixed-product-readout floor on an arbitrarily long odd ring of separable mixed chargers. The present construction is a *single-state, one-time readout problem*, not a claimed impossibility for their adaptive scheme.

Liu, Yang, Shi and Yu (2025; preprint 2023) develop local-measurement orthogonality conditions for quantum metrology and give a three-qubit example with incompatible pairwise planar-orthogonality constraints (their Section IV C, Example 3). Thus the **qualitative triangle orthogonality obstruction is already known in a related setting**; neither the use of an odd-cycle frustration argument nor the bipartite feasibility implication is claimed as independently novel. Their metrological criterion neither evaluates the energy-branch variance in the fully separable mixed battery family above nor yields the all-axis sharp minimization and field/coupling switch. The quantitative result additionally uses a standard spectral bound for odd-cycle XY frustration; that matrix fact itself is not claimed as new.

## Limitations

The theorem concerns one fixed, nonadaptive, rank-one tensor-product projective measurement of a specified joint state and the classical dispersion of **conditional expected** battery energy. It does not cover feedforward/adaptive local measurements, entangled collective measurements, general POVMs, unitary collision protocols, charging power, ergotropy, intrinsic energy spread, or multipartite entanglement. The constructed source is fully separable and deliberately contains classical charger–battery correlations; it need not arise from a specified collision Hamiltonian. This proof does not establish a new quantum-metrological orthogonality theorem or novelty of the classical odd-cycle spectral eigenvalue. Independent scholarly priority and mathematical validation have not been performed.

## References

1. L. Gong, J. Zhang, Y. Li, *Fluctuation-free Quantum Battery Charging Enabled by Bell-like Entangled and Separable Charger States*, arXiv:2610.31242v1, first public posting 2026-10-22, https://arxiv.org/abs/2610.31242 . Primary motivation.
2. J. Liu, Y. Yang, H.-L. Shi, S. Yu, *Optimal Local Measurements in Single-Parameter Quantum Metrology*, arXiv:2310.00285, https://arxiv.org/pdf/2310.00285 . Published framework and an explicit incompatible three-qubit orthogonality example; Section IV C, Example 3.
3. S. M. Giampaolo, B. C. Hiesmayr, F. Illuminati, *Global-to-local incompatibility, monogamy of entanglement, and ground-state dimerization: Theory and observability of quantum frustration in systems with competing interactions*, Physical Review B 92, 144406 (2015), https://doi.org/10.1103/PhysRevB.92.144406 . Background frustration framework, not claimed to contain the present readout minimization.
