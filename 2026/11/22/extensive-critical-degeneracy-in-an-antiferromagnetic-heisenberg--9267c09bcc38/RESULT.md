# Extensive critical degeneracy in an antiferromagnetic Heisenberg triangular bouquet

## Finding

Consider the friendship graph (triangular bouquet) with one shared central vertex and \(m\ge 2\) disjoint outer pairs. For spin-\(1/2\) operators \(\mathbf S_0,\mathbf S_{a_i},\mathbf S_{b_i}\), use the isotropic Hamiltonian

\[
H_m(J,K)=J\sum_{i=1}^{m}\mathbf S_0\cdot(\mathbf S_{a_i}+\mathbf S_{b_i})+K\sum_{i=1}^{m}\mathbf S_{a_i}\cdot\mathbf S_{b_i},\qquad J,K>0.
\]

All spins obey \(\mathbf S_v^2=3/4\); no field, anisotropy or further interactions are included. The exact ground energy is

\[
E_0=-\frac{3mK}{4}+\min\left\{0,\ K-J,\ mK-\frac{(m+1)J}{2}\right\}.
\]

The complete ground-state classification is:

| Coupling ratio | Ground total-spin sector(s) | Ground-space dimension |
|---|---|---|
| \(0<K<J/2\) | \(m-1/2\) | \(2m\) |
| \(K=J/2\) | \(k-1/2\), each \(1\le k\le m\) | \(m2^m\) |
| \(J/2<K<J\) | \(1/2\), with exactly one triplet outer pair | \(2m\) |
| \(K=J\) | \(1/2\), with zero or one triplet outer pair | \(2(m+1)\) |
| \(K>J\) | \(1/2\), with no triplet outer pairs | \(2\) |

At the lower critical ratio the ground-state multiplicity grows exponentially, while it is only linear or constant at every fixed ratio away from the two crossings. The zero-temperature residual entropy per physical spin at \(K=J/2\) is

\[
\lim_{m\to\infty}\frac{\log(m2^m)}{2m+1}=\frac{\log2}{2};
\]

at every fixed other positive ratio this limit is zero. The spin sector changes from collective ferrimagnetic \(m-1/2\) to localized \(1/2\) as the ratio crosses \(1/2\).

For every \(m\ge2\), the spectral gap to the first *distinct* energy level is also exactly

\[
\Delta_m(J,K)=\begin{cases}
J/2-K,&0<K<J/2,\\
J/2,&K=J/2,\\
\min\{K-J/2,J-K\},&J/2<K<J,\\
J/2,&K=J,\\
K-J,&K>J.
\end{cases}
\]

The positive gap at a crossing is the separation above the enlarged degenerate ground space; it does not mean that the lowest two individual eigenvalues remain separated on approach to the crossing.

## Assumptions and scope

Each outer pair consists of two distinguishable spin-\(1/2\) sites, coupled by \(K\). The shared central spin couples identically with strength \(J\) to all \(2m\) outer sites. Each Pauli spin operator is normalized as one half of the corresponding Pauli matrix. The graph has \(2m+1\) vertices and \(3m\) bonds. All ground-state counts include magnetic multiplet dimensions, including degeneracy from choosing triplet outer pairs. Couplings are strictly positive and \(m\) is an integer at least two. The entropy refers to an exact zero-temperature ground-state count followed by the large-\(m\) limit, not to a positive-temperature transition.

## Proof

**Pair-spin conserved quantities.** Set \(\mathbf T_i=\mathbf S_{a_i}+\mathbf S_{b_i}\) and \(\mathbf T=\sum_i\mathbf T_i\). Each \(\mathbf T_i^2\) commutes with the Hamiltonian and has eigenvalues \(0\) (one singlet) or \(2\) (one triplet). The outer-pair interaction satisfies

\[
\mathbf S_{a_i}\cdot\mathbf S_{b_i}=\tfrac12(\mathbf T_i^2-\tfrac32).
\]

If exactly \(k\) outer pairs are triplets, the pair energy is \(K(k-3m/4)\). Let their combined integer spin be \(s\in\{0,\dots,k\}\), keeping only those \(s\) that actually occur in the tensor product of \(k\) spin-one representations. The central spin couples to it to form \(j=s+1/2\) and, for \(s\ge1\), also \(j=s-1/2\).

**Complete spectrum.** Angular-momentum addition gives the two branches

\[
E_{k,s,+}=K\left(k-\frac{3m}{4}\right)+\frac{Js}{2},\qquad
E_{k,s,-}=K\left(k-\frac{3m}{4}\right)-\frac{J(s+1)}{2}\quad(s\ge1).
\]

The multiplicity of a spin-\(s\) representation in \((\mathrm{spin}\ 1)^{\otimes k}\) is

\[
a_{k,s}=[z^s](z^{-1}+1+z)^k-[z^{s+1}](z^{-1}+1+z)^k,
\]

with \(a_{0,0}=1\). Consequently the corresponding eigenspace dimensions, *before combining accidental equal energies*, are \(\binom mk a_{k,s}(2s+2)\) in the plus branch and \(\binom mk a_{k,s}(2s)\) in the minus branch. These formulas also include \(k=0,s=0\) through the plus branch alone. Their dimension sum is

\[
2\sum_{k=0}^{m}\binom mk3^k=2\cdot4^m=2^{2m+1},
\]

so the decomposition exhausts the entire Hilbert space. It provides an exact finite-temperature partition function by summing \(e^{-\beta E}\) with these multiplicities, though no finite-temperature singularity is asserted.

**Energy minimization.** For \(k\ge1\), the minus branch strictly minimizes at the largest possible triplet sum \(s=k\), which occurs once per chosen set of \(k\) pairs. Its energy is

\[
e_k=-\frac{3mK}{4}+k\left(K-\frac J2\right)-\frac J2.
\]

The all-singlet sector has energy \(e_0=-3mK/4\). The affine dependence on \(k\in\{1,\ldots,m\}\) shows that the best positive \(k\) is \(m\) for \(K<J/2\), all positive \(k\) for \(K=J/2\), and \(1\) for \(K>J/2\). Comparing with \(e_0\) gives the second crossing at \(K=J\). This proves the energy and the classification without assuming an unverified variational ansatz.

**Multiplicities and entropy.** At \(k=0\) the central free spin contributes two states. For a chosen \(k\ge1\), the maximally aligned triplet sum \(s=k\) is unique and the lower total-spin multiplet \(j=k-1/2\) has dimension \(2k\). Thus \(k=1\) contributes \(2m\), \(k=m\) contributes \(2m\), and the \(K=J/2\) crossing contributes

\[
\sum_{k=1}^{m}\binom mk(2k)=m2^m.
\]

At \(K=J\), add two all-singlet central-spin states to the \(2m\) states with one triplet pair. The residual-entropy formula follows directly. In the strict regions, the multiplicities are at most \(2m\) and thus yield zero entropy per spin in the specified limit.

**First distinct energy.** The next candidate among the affine minima is the neighboring \(k\)-sector; within a fixed positive \(k\), lowering the combined triplet spin by one costs at least \(J/2\), and selecting the upper coupling branch costs at least \(3J/2\). Comparing the neighboring minimum \(k\), the zero-triplet branch, and these internal excitation costs yields the five stated gap cases. At \(K=J/2\), the first distinct excitation is the zero-triplet sector at cost \(J/2\). At \(K=J\), the first distinct excitation is the two-triplet aligned sector at cost \(J/2\). Since \(m\ge2\), both relevant sectors are available.

## Verification

The standalone program `verify_spin.py` constructs the \(2^{2m+1}\times2^{2m+1}\) Hamiltonian directly using computational-basis spin exchanges, independently constructs the predicted multiplets from integer spin-one weight counts, and compares every eigenvalue including multiplicity. It also checks the ground energy, ground degeneracy, and first distinct gap in 15 cases: \(m\in\{2,3,4\}\) and \(K/J\in\{0.2,0.5,0.75,1,1.2\}\). The maximum absolute full-spectrum discrepancy was \(2.31\times10^{-14}\). Separate dimension checks were performed for \(2\le m\le10\). Run `python verify_spin.py` with Python 3 and NumPy; a single-core BLAS mode reduces variability.

These finite cases do not prove the all-size theorem; the commuting-Casimir decomposition and exact spin multiplicities do.

## Relationship to prior work

Antonosyan, Bellucci, and Ohanyan (2008) analyzed exactly solvable *Ising-mediated* chains containing Heisenberg triangular plaquettes. Their triangles are not all coupled through one shared quantum spin, and their conserved local variables are different. Xian (1995) established a dimerization transition in coupled quantum Heisenberg chains with rungs and inter-rung exchange, not a common-center triangular bouquet. Karl'ová and Strečka (2023) computed entanglement of a four-spin Heisenberg star whose three peripheral vertices form a *single triangle*: it is a different graph from the present \(m\)-petal bouquet and does not provide its all-size exponentially degenerate level crossing. These related results demonstrate the motivation for exact frustration and coupled-spin classifications but are not represented as evidence that the construction is wholly new. The calculations here use standard spin-addition techniques; originality, to the extent supported by the searches, lies in the all-\(m\) phase boundary, exact degeneracy spike and spectrum for this particular topology.

## Limitations

This is an ideal, finite-size quantum-spin family with identical couplings in each bond class and exact spin rotational symmetry. The extensive degeneracy can be lifted by generic petal-dependent perturbations, anisotropy, nonuniform hub bonds, or magnetic fields, none of which is covered here. The entropy is a limit of ground-state multiplicities, not a claim of an infinite-temperature or finite-temperature phase transition. Historical priority against all unpublished and unindexed calculations is not established. No experimental realization, robustness bound, or independent audit is claimed.

## References

1. D. Antonosyan, S. Bellucci, V. Ohanyan, "Exactly solvable Ising–Heisenberg chain with triangular XXZ-Heisenberg plaquettes," arXiv:0807.4300 (first public version 2008-07-27), https://arxiv.org/abs/0807.4300.
2. Y. Xian, "Rigorous results on a first-order phase transition in antiferromagnetic spin-1/2 coupled chains," arXiv:cond-mat/9501006 (1995-01-04), https://arxiv.org/abs/cond-mat/9501006.
3. K. Karl'ová and J. Strečka, "Distribution of Bipartite and Tripartite Entanglement within a Spin-1/2 Heisenberg Star in a Magnetic Field," *Molecules* 28, 4037 (2023), https://pmc.ncbi.nlm.nih.gov/articles/PMC10222075/.
4. B. Jeevanesan and P. P. Orth, "Classical ground states of Heisenberg and XY antiferromagnets on the windmill lattice," *Physical Review B* 90, 144435 (2014), https://doi.org/10.1103/PhysRevB.90.144435.
