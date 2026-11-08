# Scientific assessment

## Correctness — PASS

The main result specifies all even cycle orders starting at six, the binary symmetric pair utility, the weak/strict two-agent swap rule, and the labeled-vertex/unlabeled-pair counting convention. Exhausting the three swap types gives the exact two-part local criterion. This forces odd gaps of length at least three, except that bad pairs are forbidden to close length-three gaps. Inclusion-exclusion over disjoint edges of the compressed cycle yields the counting formula; the case of two unhappy vertices is treated separately. The sharp welfare bound follows from gap lengths and explicit constructions with opposite-index bad pairs. Direct exhaustive computations check each individual exchange on all 146595 pair partitions of cycle orders 6,8,10,12,14, independently reproducing the formula; they are not used as an infinite proof.

## Originality — PASS, with residual priority uncertainty

The published AAAI 2022 Bilò–Monaco–Moscardelli paper sets up precisely the same fixed-size, symmetric, simple-game swap stability framework (the closest direct precursor) and proves existence, a potential, and general worst-case upper bounds, but does not derive the cycle-specific exact stable-pairing census or the uniform sharp welfare ratio. The ordinal seat-arrangement setting of Wilczynski (IJCAI 2023) differs in its utility/graph role and does not imply this binary friendship pairing count. Nearby matching and stable-roommates records concern distinct objectives or general preference profiles. The specific three-edge obstruction is weaker than forbidding all matching augmenting paths, because endpoints must already be paired together. Targeted exact-claim and alias comparisons found no covering statement. Unknown specialized enumeration or inaccessible material could still affect priority, so no novelty certainty is claimed.

## Value — PASS

The agent network is a natural sparse symmetric friendship graph with the smallest nontrivial coalition size. The result provides a complete test for stability, a finite and computable formula for *all* labeled stable allocations, and a sharp social-welfare guarantee independent of the number of coalitions. The transition from no inefficient equilibria at six/eight agents to inefficient cases at ten, followed by an attained asymptotic bound of three halves, gives a meaningful boundary for the general fixed-size hedonic model rather than an arbitrary numerical example.

## Closest literature and limitations

Bilò, Monaco, and Moscardelli, *Hedonic Games with Fixed-Size Coalitions*, AAAI 2022, DOI 10.1609/aaai.v36i9.21156, is the principal precursor. Wilczynski, *Ordinal Hedonic Seat Arrangement under Restricted Preference Domains: Swap Stability and Popularity*, IJCAI 2023, has different host graph and preference semantics. Source-priority uncertainty remains for unindexed specialized studies; the result is confined to even cycles, binary symmetric pair utility, and the specified swap-stability rule. The finite checker does not establish the infinite theorem independently.

Self-review: passed. Independent audit: not yet performed.
