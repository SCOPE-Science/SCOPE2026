# Self-review

## Correctness — PASS

The claim concerns the canonical earliest-failure greedy online attractor, with zero-based indices, not offline optimum. The proof checks both necessary directions at each scale: the entire trailing segment before the next proposed mark occurs earlier (therefore all newly exposed factors are already attracted), while at the proposed mark the first longer all-zero run is wholly beyond the existing marks. The initial marks \(0,2\), every dyadic transition \(3\cdot2^k-1\mapsto3\cdot2^{k+1}-1\), endpoint uniqueness, and the exact cost formula are explicitly established. Three independent classes of finite checks corroborate but do not replace the infinite argument.

## Originality — PASS, qualified

Schaeffer–Shallit arXiv:2012.06840 treats the same powers-of-two indicator with different feasible attractors and introduces the general online greedy rule; no exact greedy indices follow from its cited theorems. Whittington arXiv:2407.15599 establishes equivalence with a particular self-referencing novel Lempel–Ziv parsing but does not compute it on this word. Cassaigne et al. (2024) study optimum and other complexity profiles. Béal–Crochemore–Romana arXiv:2509.08503 use a distinct backwards greedy algorithm and report numerical results for this word, not the present online positions. Relevant mathematical-record, exact-substring, alias and equivalent-parsing searches found no dominating statement. Bibliographic search cannot exclude a previously unstated or unindexed Lempel–Ziv equivalent.

## Mathematical value — PASS

The powers-of-two characteristic word is a standard natural automatic word with logarithmic optimal-attractor profile. Giving every selected position of a canonical online scheme and its exact all-prefix size supplies a finer, reproducible structural invariant and an equivalent exact description of phrase endpoints for a standard Lempel–Ziv variant. This is neither an arbitrary finite table nor an offline-optimality claim.

## Limitations

No claim of independent validation, exhaustive literature coverage, optimal offline attractors or generalization to every sparse automatic sequence is made. The test code probes only finite prefixes. No use is made of any unverified general theorem to prove the specific induction.

Self-review: passed. Independent audit: not yet performed.
