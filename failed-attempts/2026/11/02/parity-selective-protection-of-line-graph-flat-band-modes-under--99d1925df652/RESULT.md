# Parity-selective protection of line-graph flat-band modes under discrete onsite disorder

## Finding
Let \(G\) be a finite *cycle flower*: \(k\ge1\) simple cycles of lengths \(\ell_1,\ldots,\ell_k\ge3\) meeting at exactly one common vertex and otherwise vertex-disjoint. On the \(N=\sum_i\ell_i\) sites of its line graph \(L(G)\), take the nearest-neighbor hopping Hamiltonian \(H_0=A_{L(G)}\), with hopping amplitude one. Let \(F=\ker(H_0+2I)\) be its original \(-2\) flat-band eigenspace, and let \(H=H_0+\operatorname{diag}(d_e)\), where the onsite values \(d_e\) are arbitrary complex numbers.

For every complex \(z\), let \(e_z\) be the number of even flower cycles all of whose edge-sites have onsite value \(z\), and let \(o_z\) be the corresponding number of odd flower cycles. Then the complete space of eigenvectors **retained inside the original flat-band space** at energy \(z-2\) has dimension
\[
\boxed{\dim\bigl(F\cap\ker(H-(z-2)I)\bigr)=e_z+\max\{o_z-1,0\}.}
\]
Thus one uniformly tuned even loop protects a mode, whereas an odd loop protects a mode only when paired with another odd loop whose entire onsite pattern has the *same* value. The full original flat-band space is invariant under the diagonal perturbation if and only if every even loop has constant onsite value and, when at least two odd loops exist, **all** odd-loop sites share one common onsite value. A unique odd loop imposes no restriction, since it carries no original flat-band amplitude.

For local absorption \(d_e=-i\gamma_e\), \(\gamma_e\ge0\), put \(e_0^{\rm free}\) and \(o_0^{\rm free}\) for the counts of even and odd cycles untouched by positive-rate absorbers. Exactly \(e_0^{\rm free}+\max\{o_0^{\rm free}-1,0\}\) original flat-band modes remain undamped. Consequently the minimum number of distinct absorbing sites needed to eliminate *all original-flat-band dark modes* is \(e+\max\{o-1,0\}\), where \(e,o\) count all even and odd cycles, respectively; a minimum placement uses at most one site per selected cycle. This says nothing about possible additional dark modes outside \(F\).

A further exact disorder consequence arises when the sites have independent onsite values uniformly sampled from \(q\ge2\) distinct levels. For a flower of \(k\) odd cycles of common length \(\ell\), let \(R_k\) count all eigenvectors retained inside \(F\), across the possible shifted energies, with multiplicities. Then
\[
\boxed{\mathbb E R_k=kq^{1-\ell}-q\bigl[1-(1-q^{-\ell})^k\bigr],\qquad
\lim_{k\to\infty}\frac{R_k}{k}=q^{1-\ell}\quad\text{almost surely}.}
\]
In particular, independent binary disorder on a growing bouquet of triangles leaves an asymptotic fraction \(1/4\) of the original flat-band degrees of freedom as exact eigenmodes. With independent nonatomic continuous onsite values, none of those modes survives almost surely at any finite \(k\). These are statements about exact eigenvectors in \(F\), not about Anderson localization lengths or the complete perturbed spectrum.

## Assumptions and scope
The graph is simple, finite, and contains exactly the specified cycles joined at a single common hub; there are no edges between their other vertices. The line graph has one site per edge of \(G\), with off-diagonal hopping one between edges sharing an endpoint. Onsite potentials may be arbitrary complex numbers in the deterministic classification, real numbers for conservative disorder, and nonpositive imaginary numbers for absorption. No normalization of eigenvectors is assumed. A "retained" mode means a nonzero vector in the **unperturbed** space \(F\) which remains an exact eigenvector of the perturbed Hamiltonian. The discrete-disorder expectation assumes independent uniform sampling for every line-graph site, not one common random draw per cycle. The almost-sure assertion is in the natural nested coupling of independent flowers as \(k\) grows, for fixed \(q,\ell\).

## Proof
Write \(B\) for the unsigned vertex-edge incidence matrix of \(G\). Since every edge has two distinct endpoints and two distinct edges of a simple graph share at most one endpoint, \(B^{\mathsf T}B=A_{L(G)}+2I\). Hence \(F=\ker B\). Number the edges of cycle \(i\) consecutively as \(e_{i,0},\ldots,e_{i,\ell_i-1}\), beginning and ending at the hub. At each of its non-hub vertices, the incidence equation \(Bx=0\) forces the adjacent edge amplitudes to sum to zero. Therefore every \(x\in F\) has
\[
x_{i,j}=(-1)^j a_i\qquad(0\le j<\ell_i).
\]
The two hub-adjacent amplitudes on that cycle sum to \(0\) when \(\ell_i\) is even and to \(2a_i\) when it is odd. Thus the only remaining incidence equation is
\[
\sum_{i:\,\ell_i\text{ odd}}a_i=0.
\]
This parametrizes \(F\) completely and establishes \(\dim F=e+\max\{o-1,0\}\). In particular, an active cycle (\(a_i\ne0\)) has nonzero amplitude on *every* one of its edges.

For \(x\in F\) the eigenvalue equation \((H_0+\operatorname{diag}d)x=(z-2)x\) reduces exactly to \(d_ex_e=zx_e\) at every edge-site. If \(a_i\ne0\), all sites on cycle \(i\) must therefore have the same potential \(z\). Conversely, any collection of such monochromatic cycles with an arbitrary coefficient on each even cycle and coefficients summing to zero across the odd cycles gives an exact eigenvector. The dimension is \(e_z+\max\{o_z-1,0\}\). This proves both necessity and sufficiency and excludes partial-cycle modes within \(F\).

For invariance of the *whole* space \(F\), apply the diagonal perturbation separately to each even-cycle basis vector and to every difference of two odd-cycle basis vectors. The even vectors force constancy individually, while the odd-pair vectors force all odd-cycle potentials to be equal to one common value when there are at least two odd cycles. Conversely these equalities visibly preserve the above parametrization. If there are fewer than two odd cycles, no coefficient on an odd cycle can occur in \(F\), so its potentials are unrestricted.

For \(d_e=-i\gamma_e\) with \(\gamma_e\ge0\), an undamped vector \(x\in F\) must obey \(\operatorname{diag}(\gamma)x=0\). Since every active cycle uses every edge, a cycle touched by any positive absorber is excluded. The same incidence parametrization on untouched cycles proves the dark-mode formula. Eliminating the even-cycle modes requires one absorbing site on each even cycle. Eliminating odd-cycle modes requires leaving at most one odd cycle untouched. These conditions are necessary and are achieved by one selected edge per required cycle, yielding the minimum placement. The protected vectors lie in a common reducing subspace of the Hermitian operators \(H_0\) and \(\operatorname{diag}(\gamma)\); hence each has exactly constant norm under the loss dynamics. For a maximally mixed one-excitation initial state, the persistent norm is at least this protected dimension divided by \(N\).

For independent uniform \(q\)-level disorder on odd cycles of length \(\ell\), let \(X_z\) count cycles all of whose \(\ell\) onsite values equal a fixed level \(z\). For every \(z\), \(X_z\) is binomial with parameters \(k\) and \(q^{-\ell}\). The deterministic formula gives \(R_k=\sum_z(X_z-1)_+\). Since \((X_z-1)_+=X_z-\mathbf1_{\{X_z\ge1\}}\), linearity of expectation yields the claimed exact formula. The strong law gives \(X_z/k\to q^{-\ell}\) for each of the finitely many levels, whence \(R_k/k\to q^{1-\ell}\) almost surely. For an independent nonatomic law, any cycle of length at least three is monochromatic with probability zero, so the finite union of such events has probability zero, proving the continuous-disorder contrast.

## Verification
The companion `checker.py` constructs each original graph, its unsigned incidence matrix and line-graph adjacency by independent combinatorial definitions, and uses exact rational row reduction on stacked eigenvalue/incidence constraints. It checks 77 independently specified integer onsite patterns on 11 mixed-parity cycle flowers (up to 16 edge-sites), five absorber patterns in each case, and exhaustively sums all binary potentials for flowers of lengths \((3,3)\), \((3,3,3)\), \((3,3,3,3)\), and \((4,4)\). The exact expected retained dimensions in these four cases are \(1/32\), \(23/256\), \(353/2048\), and \(1/4\). Run `python checker.py` with SymPy installed. All checked assertions pass. The all-size theorem follows from the preceding proof; finite checks are not the proof for arbitrary cycle counts or lengths.

## Relationship to prior work
Mielke (1991) established basic line-graph flat-band structure in Hubbard models; the unperturbed incidence-kernel mechanism and baseline degeneracy are acknowledged. Flach, Leykam, Bodyfelt, Matthies and Desyatnikov (2013/2014) explained compact localized states and the sufficient local-symmetry condition that identical onsite values on a compact state's support preserve it; that generic sufficiency is not claimed as new. Bodyfelt and colleagues (2014) analyzed correlated disorder and mobility-edge effects for the cross-stitch lattice. Kollár and colleagues (2019) gave a broad line-graph spectral and physical construction. The claim here is the necessary-and-sufficient **cycle-flower parity and multiplicity classification**, its exact absorber-placement threshold, and the finite-alphabet statistical law. None of the examined primary full texts states these combined finite-flower formulas. This comparison does not constitute independent historical priority certification.

## Limitations
The result counts only modes retained in the original \(-2\) eigenspace, not the complete spectrum of the perturbed Hamiltonian, and it does not exclude other symmetry-protected or accidental dark states. The capture statement is an obstruction from surviving modes, not an exact all-state capture probability or a finite-time absorption law. The random theorem uses idealized iid onsite levels; correlated distributions, continuous broadening, interactions, decoherence and thermodynamic transport limits are not addressed. The original 1991 Mielke full text could not be inspected, leaving a historical-priority risk.

## References
1. A. Mielke, *Ferromagnetism in the Hubbard model on line graphs and further considerations*, J. Phys. A 24, 3311–3321 (1991), DOI: https://doi.org/10.1088/0305-4470/24/14/018.
2. S. Flach, D. Leykam, J. D. Bodyfelt, P. Matthies, A. S. Desyatnikov, *Detangling Flat Bands into Fano Lattices*, arXiv:1311.5689 (first public 2013-11-22), https://arxiv.org/html/1311.5689v3.
3. J. D. Bodyfelt, D. Leykam, C. Danieli, X. Yu, S. Flach, *Flat Bands Under Correlated Perturbations*, arXiv:1407.8345 (first public 2014-07-31), https://arxiv.org/html/1407.8345v3.
4. A. J. Kollár, M. Fitzpatrick, P. Sarnak, A. A. Houck, *Line-Graph Lattices: Euclidean and Non-Euclidean Flat Bands, and Implementations in Circuit Quantum Electrodynamics*, arXiv:1902.02794 (2019), https://arxiv.org/abs/1902.02794.
