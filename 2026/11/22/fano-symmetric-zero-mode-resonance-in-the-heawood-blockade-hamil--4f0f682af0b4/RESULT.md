# Fano-symmetric zero-mode resonance in the Heawood blockade Hamiltonian

## Finding

Let \(H(t)\) be the zero-detuning, perfect-nearest-neighbour-blockade PXP Hamiltonian on the fourteen-vertex Fano point–line incidence graph (the Heawood graph), with uniform real spin-flip amplitude \(t\) on its seven point vertices and amplitude one on its seven line vertices. On the entire independent-set Hilbert space its zero-energy multiplicity is exactly

\[
\dim\ker H(t)=\begin{cases}
148,&t=0,\\
26,&t=1\text{ or }t=-1,\\
8,&t\in\mathbb R\setminus\{0,-1,1\}.
\end{cases}
\]

The Hilbert-space dimension is \(458\), with \(232\) even-excitation and \(226\) odd-excitation states. The elementary excitation-parity index thus guarantees only six zero modes. The Fano incidence symmetry protects two additional zero modes for every real \(t\); equal-magnitude point and line drives produce eighteen further zero modes.

## Assumptions and scope

Write the seven points and seven lines of the Fano plane as nonzero three-bit vectors \(p,\ell\in\mathbb F_2^3\), declaring them incident precisely if \(p\cdot\ell=0\). A configuration \(S\) is any independent subset of these fourteen vertices. The orthonormal configuration vectors are \(\lvert S\rangle\). The operator connects configurations differing by one legal occupation flip; the associated real symmetric matrix element is \(t\) if a point is flipped and one if a line is flipped, and all diagonal entries vanish. There are no longitudinal fields or interactions beyond the hard blockade constraint. All conclusions concern every real \(t\), including zero and negative amplitudes. In particular, the zero modes are mid-spectrum eigenstates, not asserted to be ground states.

## Proof

1. Direct enumeration of the \(2^{14}\) subsets using the seven-by-seven Fano incidence relation gives exactly \(458\) independent sets: by occupation number the counts are \(1,14,70,154,147,56,14,2\), for occupation numbers zero through seven. Thus the even and odd spaces have dimensions \(232\) and \(226\). In this ordering,
\[
H(t)=\begin{pmatrix}0&B(t)^\mathsf T\\B(t)&0\end{pmatrix},\qquad B(t)=tA+C,
\]
where \(A,C\) are disjoint-support, binary \(226\times232\) incidence matrices recording legal point and line flips. Consequently \(\dim\ker H(t)=458-2\operatorname{rank}B(t)\).

2. All \(168\) invertible linear maps of \(\mathbb F_2^3\), acting covariantly on points and contragrediently on lines, commute with \(H(t)\). The induced action on independent configurations has exactly \(13\) even orbits and \(14\) odd orbits. Thus the restriction of \(B(t)^\mathsf T\) from the fourteen-dimensional invariant odd subspace into the thirteen-dimensional invariant even subspace has a nonzero kernel for **every** \(t\). In particular \(\operatorname{rank}B(t)\le225\) for all real \(t\). This is stronger than the unrefined six-mode excitation-parity bound.

3. Exact integer fraction-free elimination gives \(\operatorname{rank}B(0)=155\) and \(\operatorname{rank}B(1)=216\). Conjugation by the diagonal sign \((-1)^{\#\text{occupied points}}\) maps \(H(t)\) unitarily to \(H(-t)\). Hence the rank at \(t=-1\) is also \(216\).

4. For completeness, an all-real-parameter lower-rank certificate consists of **two explicit** \(225\times225\) minors \(M_0(t),M_1(t)\) of \(B(t)\). Their row and column indices, in increasing binary-mask configuration order, are stored in `minor_indices.json`. Set
\[
Q(t)=1440t^8+7125t^6-17018t^4+7125t^2+1440,
\quad K=-4334215495680.
\]
Their exact determinant identities are
\[
\det M_0(t)=K\,t^{80}(t^2-1)^9(t^2-5)Q(t)^6,
\]
\[
\det M_1(t)=K\,t^{80}(t^2-1)^9(5t^2-1)Q(t)^6.
\]
The identities are certified without numerical polynomial fitting: for each determinant of degree at most \(225\), evaluations at \(226\) distinct field elements in each of twelve specified prime fields establish every coefficient modulo their prime product. Hadamard's determinant bound on the unit circle, followed by Cauchy's coefficient bound, and a verified product-of-primes inequality establish equality over the integers. The reproducible verification code performs all evaluations and bound comparisons from the actual indexed matrices.

5. For nonzero real \(t\), put \(u=t^2+t^{-2}\ge2\). Then
\[
Q(t)/t^4=1440u^2+7125u-19898.
\]
The right-hand side is strictly increasing for \(u\ge2\), and equals \(112>0\) at \(u=2\). Thus \(Q(t)>0\) for every nonzero real \(t\). The two remaining minor factors \(t^2-5\) and \(5t^2-1\) cannot vanish simultaneously. At every real \(t\notin\{0,-1,1\}\), at least one minor is therefore nonzero, so \(\operatorname{rank}B(t)\ge225\). Together with Step 2 this gives rank exactly \(225\), proving the stated multiplicity formula.

## Verification

Run `python verify_exact.py` in the folder containing `minor_indices.json` (Python 3 with NumPy and SymPy). The verifier rebuilds the graph and all \(458\) configurations, counts the \(168\)-element point–line-preserving symmetry group and its \(13/14\) orbit split, performs exact integer rank eliminations, and verifies both determinant identities by finite-field evaluation and rigorous integer coefficient bounds. The two certificates can also be replayed separately with `python verify_exact.py 0` and `python verify_exact.py 1`. Run `python verify_independent.py` for a second, independently labelled cyclic-difference-set realization of the Fano plane and exact rational ranks at \(t=0,\pm1,\pm2\). These checks were executed successfully from the package contents.

## Relationship to prior work

Lesanovsky's 2010 Rydberg-gas construction explains the perfect-blockade, projector-constrained flip model in one-dimensional lattices. Schecter and Iadecola establish the general spectral-reflection and chiral-index mechanism. Buijsman's PXP zero-mode analysis gives chain-based symmetry-sector lower bounds. Lin, Calvera, and Hsieh study exact scars in two-dimensional Rydberg arrays. These frameworks motivate the present finite incidence-network problem but do not directly supply the Heawood graph's all-real-parameter zero-mode multiplicity or the two polynomial minor identities. The parity-index lower bound is a known principle, not claimed here as new.

## Limitations

The theorem is confined to this single fourteen-site incidence network with ideal nearest-neighbor blockade, zero detuning, shore-uniform drives and unit line drive. It does not assert stability of the extra zero modes under arbitrary site-dependent drives, finite blockade strength, longitudinal fields, disorder, or changes of graph topology. It does not determine wavefunctions, entanglement or dynamics away from zero energy. Literature priority is provisional; independent scientific verification has not been performed.

## References

- I. Lesanovsky, *Many-body spin interactions and the ground state of a dense Rydberg lattice gas*, arXiv:1010.2349 (first public version 2010-10-12), https://arxiv.org/abs/1010.2349.
- M. Schecter and T. Iadecola, *Many-Body Spectral Reflection Symmetry and Protected Infinite-Temperature Degeneracy*, arXiv:1801.03101 (2018), https://arxiv.org/abs/1801.03101.
- W. Buijsman, *Number of zero-energy eigenstates in the PXP model*, arXiv:2203.09264 (2022), https://arxiv.org/abs/2203.09264.
- C.-J. Lin, V. Calvera and T. H. Hsieh, *Quantum Many-Body Scar States in Two-Dimensional Rydberg Atom Arrays*, arXiv:2003.04516 (2020), https://arxiv.org/abs/2003.04516.
