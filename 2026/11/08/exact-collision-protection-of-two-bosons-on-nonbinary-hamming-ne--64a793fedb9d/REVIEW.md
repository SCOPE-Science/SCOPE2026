# Scientific review: nonbinary Hamming collision-loss classification

## Correctness — PASS

The domain is every integer \(d\ge1\), every integer \(q\ge3\), common real nonzero hopping amplitude, and strictly positive collision-loss strength at every vertex. The proof explicitly reduces asymptotic capture to the orthogonal complement of collision-free Hamiltonian eigenstates, counts one bright vector per accessible total-momentum/energy sector, and derives a complete finite rational capture formula. Critical nonstandard steps were checked: nonbinary momentum coordinates admit both one- and two-unit weight contributions; therefore all integer energy indices in the claimed interval occur; the Fourier collision vector is nonzero in exactly those sectors; and the root-of-unity identity \(\sum_{a=1}^{q-1}|1+e^{2\pi ia/q}|^2=2(q-2)\) gives the squared-projection sum. Two independently coded finite checks agreed for the stated examples. Their scope is finite corroboration, not an infinite certificate. A residual implementation risk is addressed by the analytic derivations and independent direct matrix construction.

## Originality — PASS on examined evidence

The nearest published quantum-walk mechanism is Krovi–Brun's dark-state analysis of quantum hitting times [1]. The nearest explicit two-boson graph Hamiltonian is Gamble and collaborators [2]. An explicit treatment of **the same Hamming graphs** is Bernard–Crampé–Vinet [3], which examines free-fermion entanglement instead of continuous bosonic collision loss. The checked prior results do not state or directly imply the nonbinary two-boson dark rank together with all separation-resolved eventual capture probabilities. An available binary-hypercube collision classification does not cover any \(q\ge3\) network: its parity-restricted momentum sectors and rank formula are different. An unindexed equivalent derivation, or later work not fully searchable, remains a historical-priority risk; absence from searches is not a proof of uniqueness.

## Mathematical value — PASS

The natural observable is the probability that two quantum walkers collide and are irreversibly lost. This result gives a full infinite-family classification on \(K_q^{\square d}\), including the nonbinary spectral-support transition and a rational formula evaluable without constructing the exponentially large two-body matrix. On the smallest nontrivial two-dimensional networks, it yields simple nonfactorizing distance-dependent capture laws. The distinction between same-site, neighboring, and more distant initial pairs is physically meaningful for particle transport. It is not a finite-time decay estimate or a claim of robustness under disorder and interactions.

## Literature and scope limitations

Sources inspected for the comparison: [1] https://arxiv.org/pdf/quant-ph/0606094 (continuous-time no-hitting subspaces); [2] https://arxiv.org/pdf/1002.3003 (two-boson graph Hamiltonian and interacting/noninteracting comparison); [3] https://doi.org/10.1016/j.nuclphysb.2022.116061 (fermionic Hamming Hamiltonian and entanglement). The limitations and precise detector/hopping assumptions are in `RESULT.md`. No historical-priority claim is made beyond the examined evidence.

Self-review: passed. Independent audit: not yet performed.
