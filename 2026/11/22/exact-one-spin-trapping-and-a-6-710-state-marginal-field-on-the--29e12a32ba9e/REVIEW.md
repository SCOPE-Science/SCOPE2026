# Scientific review: dodecahedral one-spin stability

## Correctness — PASS

The stated finite graph is explicit as \(GP(10,2)\), with twenty vertices and thirty edges. Direct differentiation of the Ising energy gives the flip cost \(2\sigma_i(h-J\sum_{j\sim i}\sigma_j)\). The pentagonal-face parity and matching argument proves the entire low-field classification and reduces its count to 125 perfect matchings of the dual icosahedron. The upper-field strict states are maximal independent sets; the two critical points reduce to exact local degree constraints. The proof also establishes the ground states in all intervals without assuming a transition where none exists. Independent full-mask and constrained combinatorial programs passed; all counts and field endpoints were checked in exact integer arithmetic. The calculations prove a finite statement and do not rely on statistical samples.

## Originality — PASS on examined evidence, provisional

The closest specific prior paper is Strečka–Karľová–Madaras (2015), whose complete equilibrium dodecahedral tables already imply the 250 zero-field ground states, the 5-state positive-field plateau and the 5828 independent-set total, none claimed new here. The paper does not specify one-spin adjacency in configuration space or weak/strict kinetic stability. Konstantinidis (2023) examines equilibrium spin configurations in anisotropic Heisenberg interpolation; Spirin–Krapivsky–Redner (2001) consider freezing in ferromagnetic lattices. Full published records on the dodecahedral independence complex, a two-range Ising equilibrium interaction and a spin-one dodecahedral equilibrium model were read for implications. Their conclusions do not include the new field-dependent one-spin stability classification or its 6710 critical marginal count. A broader unpublished classification or unindexed kinetic table remains a residual priority risk.

## Mathematical value — PASS

This result resolves a physically motivated distinction between the *thermodynamic* magnetization plateau and the *kinetic* trap landscape on the canonical frustrated C20 cage. Within an unchanged equilibrium ground-state regime, an interior field changes the absorbing-state census and creates a 6710-state marginal landscape. The face-dual matching proof explains why the unperturbed dodecahedron has no excited strict local minima; the maximal-independent-set and dissociation-set correspondences explain the later onset of traps and its critical boundary. These are exact, natural finite-model classifications, not an arbitrary field sample or recomputation of the established equilibrium partition function.

## Closest literature and limits

The best source for preexisting dodecahedral equilibrium tables is arXiv:1502.04449, Table 5 and the dodecahedral section of its discussion. The nearest kinetic context is arXiv:cond-mat/0105037. The result applies only to classical one-spin flips and does not determine low-temperature escape times or multispin pathways. No definitive historical-priority certification or independent scientific audit is asserted.

Self-review: passed. Independent audit: not yet performed.
