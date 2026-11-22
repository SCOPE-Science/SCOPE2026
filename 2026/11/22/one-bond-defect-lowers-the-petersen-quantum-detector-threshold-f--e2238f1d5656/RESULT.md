# One bond defect lowers the Petersen quantum-detector threshold from five to three

## Finding

For the ten-site coherent Petersen quantum network, changing the hopping on one fixed edge from \(1\) to any positive \(t\ne1\) lowers the minimum number of irreversible vertex absorbers needed to capture **every initial one-particle state** from five to three. Two absorbers never suffice, even after the perturbation. The same three absorbing sites work for every positive nonunit \(t\) and for every choice of strictly positive site loss rates.

A fixed three-site detector that fully captures at \(t\ne1\) captures only \(7/10\) of a maximally mixed initial state at \(t=1\). Thus its infinite-time efficiency is discontinuous at the unperturbed edge weight, although the dynamics at each finite time is continuous in \(t\).

## Assumptions and scope

Identify the Petersen graph with the Kneser graph \(KG(5,2)\): its vertex set comprises the ten two-element subsets of \(\{0,1,2,3,4\}\), and two vertices are adjacent exactly when they are disjoint. Use the lexicographic index order

```
0:(0,1)  1:(0,2)  2:(0,3)  3:(0,4)  4:(1,2)
5:(1,3)  6:(1,4)  7:(2,3)  8:(2,4)  9:(3,4)
```

Let \(H_t\) be the real symmetric adjacency Hamiltonian with unit hopping on every edge except the edge \(\{(0,1),(2,3)\}\), whose hopping is \(t>0\). This is an adjacency-based, **not degree-normalized or Laplacian-based**, model. For a nonempty detector set \(S\), let \(K=-iH_t-\frac12\sum_{s\in S}\kappa_s|s\rangle\langle s|\), with every \(\kappa_s>0\). Complete capture means \(\lim_{\tau\to\infty}\|e^{\tau K}\psi\|^2=0\) for every initial \(\psi\). Sink rates may differ arbitrarily.

The unperturbed minimum is \(5\). At every \(t>0\) other than \(1\), the minimum is \(3\), achieved by

\[
S_3=\{(0,2),(0,3),(2,4)\}.
\]

At \(t=1\), a five-sink witness is

\[
S_5=\{(0,1),(0,2),(0,3),(1,2),(1,3)\}.
\]

For \(S_3\), the bright-subspace dimension is \(7\) at \(t=1\) and \(10\) for \(t>0\), \(t\ne1\). With maximally mixed input \(I/10\), the eventual capture probabilities are accordingly \(7/10\) and \(1\).

## Proof

**Capture criterion.** For a real symmetric finite-dimensional Hamiltonian \(H\) and strictly positive local absorber rates, the nondecaying subspace is exactly the span of eigenvectors of \(H\) vanishing at every detector. Indeed,

\[
\frac{d}{d\tau}\|e^{\tau K}\psi\|^2=-\sum_{s\in S}\kappa_s|\langle s|e^{\tau K}\psi\rangle|^2\le0.
\]

If an eigenvalue of \(K\) has real part zero, its eigenvector has zero amplitudes at every detector, so it is also an eigenvector of \(H\). Conversely such an eigenvector never loses norm. Since the contraction semigroup is finite dimensional, no imaginary-axis Jordan block is possible; its other spectral modes decay. Hence full capture is equivalent to

\[
\operatorname{span}\{H^k|s\rangle:s\in S,\ k\ge0\}=\mathbb C^{10}.
\]

The orthogonal complement of this Krylov span is the dark subspace. The maximally mixed capture probability is the Krylov rank divided by ten.

**A universal three-dimensional obstruction.** Direct polynomial elimination for the explicitly defined matrix gives

\[
\det(xI-H_t)=(x-1)^3(x+2)^2(x^2+tx-2)
\bigl[x^3-(t+1)x^2+(t-6)x+4t+2\bigr].
\]

Consequently, for every \(t>0\), the eigenvalue \(1\) has multiplicity at least three. Any two detector evaluation functionals have a nonzero common kernel in that eigenspace. Therefore at least three absorbers are necessary for full capture, even if \(t\) changes.

**Three-site sufficiency away from the symmetric point.** In the specified vertex order set \(e_j\) to the standard coordinate basis. Form the square Krylov matrix whose ten columns, in this exact order, are

\[
(e_1,e_2,e_8,H_te_1,H_te_2,H_te_8,H_t^2e_1,H_t^2e_8,H_t^3e_1,H_t^3e_8).
\]

Exact polynomial elimination yields its determinant

\[
\boxed{-2(t-1)^3}.
\]

It is nonzero for every \(t\ne1\). Hence \(S_3\) gives full capture for all positive nonunit edge weights and all strictly positive detector rates.

**Five-site sharpness at the unperturbed point.** Setting \(t=1\) gives

\[
\det(xI-H_1)=(x-3)(x-1)^5(x+2)^4.
\]

Every collection of four detector sites has a nonzero dark vector in the five-dimensional \(1\)-eigenspace. Meanwhile, with \(e_0,e_1,e_2,e_4,e_5\) corresponding to \(S_5\), the matrix of columns

\[
(e_0,e_1,e_2,e_4,e_5,H_1e_0,H_1e_1,H_1e_2,H_1e_4,H_1^2e_0)
\]

has determinant \(-2\). Therefore five detectors suffice and are necessary.

**A fixed detector's singular capture law.** At \(t=1\), exact rational row elimination on the nine columns \(H_1^k e_j\), \(0\le k\le2\), \(j\in\{1,2,8\}\), gives rank seven. Since the minimal polynomial of \(H_1\) has degree three, higher powers add no directions. Thus \(S_3\) has bright dimension seven at \(t=1\) and ten at every other allowed parameter. The mixed-state efficiencies follow from the capture criterion.

## Verification

The accompanying standalone programs reproduce the exact matrix from the two-subset construction, check the full characteristic polynomial, both nonzero determinant certificates, and the exact rank-seven calculation. An independent standard-library integer verifier also proves the cubic minor identity by evaluating it at fourteen distinct integer edge weights. The sum of the polynomial degrees of the ten chosen Krylov columns is thirteen, hence the determinant has degree at most thirteen; agreement at fourteen points proves the identity over \(\mathbb Q[t]\), not merely at sampled parameters. Both programs passed on the embedded source files.

Run `python verify_symbolic.py` (requires SymPy) and `python verify_independent.py` (Python standard library only).

## Relationship to prior work

Dark-state obstruction and Krylov methods in coherent transport are established, including Caruso and collaborators (2009) and Razzoli, Paris and Bordone (2021). The latter explicitly treats single-absorber transport on the *unperturbed* Petersen graph. Bassereh and collaborators (2015), Le and collaborators (2017), and Cavazzoni and collaborators (2022) study symmetry breaking and perturbed quantum transport on other graph families or in more general settings. These broad mechanisms are not claimed as new. The present precise weighted-Petersen detector threshold, uniform-in-\(t\) triple, and cubic determinant certificate are the subject of this result. Published results for the complementary unweighted triangular graph \(J(5,2)\) cover the symmetric baseline, not the edge-weight-dependent theorem. Historical priority beyond inspected sources remains uncertain.

## Limitations

This is a ten-site, coherent, one-excitation, adjacency-hopping theorem for positive real edge weights. It does not establish finite-time trapping rates, loss-rate optimization, robustness to additional edge disorder, many-body capture, or a universal theorem for larger Kneser graphs. The disappearance of exact dark states as \(t\to1\) does not imply a uniform capture time. Independent external validation has not been performed.

## References

- Caruso et al., *Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport* (first public 2009-01-28), https://arxiv.org/abs/0901.4454
- Bassereh et al., *Perfect quantum excitation energy transport via single edge perturbation in a complete network* (2015), https://arxiv.org/abs/1504.04398
- Le et al., *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures* (2017), https://arxiv.org/abs/1707.07482
- Razzoli, Paris and Bordone, *Transport Efficiency of Continuous-Time Quantum Walks on Graphs* (2021), https://doi.org/10.3390/e23010085
- Cavazzoni et al., *Perturbed graphs achieve unit transport efficiency without environmental noise* (2022), https://arxiv.org/abs/2205.09408
- Related unweighted triangular-graph spectral rank formula, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-bipartite-component-formula-for-the-absorbing-spectral-rank-of-t--1d711c8bda6b
