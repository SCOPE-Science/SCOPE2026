# Independent mathematical audit

## correctness

PASS

Reconstructed E(n)≡a_lead n (mod 2); every even input and every leading-2 input is excluded. For leading-1 strings of lengths ℓ∈[k−M,k], independent lower digits give S=1+∑D_i², mean (5ℓ−2)/3 between 9B/4 and 11B/4 for all r≥3 (exact rational inequalities, checked for r=3..13). If |S−mean|<B/4 then 2B<S<3B, so E²(n) has even leading-2 first image and cannot reach 1. Hoeffding with ℓ−1<3B/2 and summand range 4 yields 2 exp(−B/192); all smaller lengths contribute <3^{k−M}. Summing all leading-1 lengths gives exactly the displayed bound; division by X→∞ yields liminf 0. Independent modulo-two check for 12,000 inputs corroborates only the finite parity identity; the infinite proof uses algebra and concentration.

## originality

PASS

PASS best-of-knowledge: distinct quantitative subsequence-density theorem for the Fox et al. ternary elated map, excluding only the prior parity lemma and ordinary concentration inequality; the published paper's explicitly stated density question remains open beyond the proved lower-density consequence. No dominating prior implication identified in actual literature searches.

## value

PASS

A motivated exact quantitative restriction on an explicitly posed natural-density problem for the ternary elated map: arbitrarily sparse scales and a necessary zero value for any existing density. This uses nontrivial large-deviation phase localization and is not the original paper's parity lemma alone. It does not settle density existence or the upper density, which limits but does not erase mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
