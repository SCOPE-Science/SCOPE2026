# Self-review

## Correctness — PASS

For each integer \(q\ge4\) and \(a,b\ge1\), the deterministic rule is fixed unambiguously. Each excitation at time \(t\) has a predecessor excitation at time \(t-1\); two-step revisitation is impossible because state one deterministically progresses to state three after two updates. Therefore all ancestry walks on the double star are simple and at most three edges long. Every excitation is absent beyond time three, yielding a universal extinction bound \(q+2\). Equality requires excitation at time three. The only distance-three paths connect leaves across the two hubs. Conditional on their orientation, the initial state restrictions are necessary and sufficient; their two disjoint counts are exactly \(L_q(a)R_q(b)\) and \(L_q(b)R_q(a)\). Dividing by \(q^{a+b+2}\) proves the positive limiting probability \(2/q^2\). Both independent enumerators agree with the closed formula and the independently implemented oriented-event criterion in all recorded finite instances. These checks are supportive, not infinite proofs.

## Originality — PASS, historically qualified

Fisch and Gravner's 1995 paper investigates one-dimensional percolating paths rather than competing branch histories on double stars. Gravner, Lyu and Sivakoff develop finite-tree convergence for a three-color medium; the present theorem assumes \(q\ge4\), where the absence of two-step return and the distinct three-color terminal set give a different exact shell count. The published three-state finite-path sharp-shell count applies neither to two branching hubs nor four-or-more refractory colors. Specific published-finding corpus searches for double-star extinction and multistate excitation did not reveal an equivalent or stronger covering claim, and a claim-level overlap search of accessible prior local research found no same system and formula. This is evidence of noncoverage within examined material, not proof of historical uniqueness. A 1993 foundational preprint could be checked in abstract/metadata but not in its original full text; unindexed tree enumerations remain the primary residual risk.

## Value — PASS

The exact sharp-extinction population reveals a structural phenomenon not supplied by a bare diameter bound: as both leaf degrees diverge, a fixed positive \(2/q^2\) fraction of configurations still require the maximum number of updates to become quiescent. The formula resolves how initial excitations in one branch are screened or admitted by the other hub and its leaf colors. It supplies a natural, exact, all-size invariant for a canonical branching tree family and is useful for distinguishing worst-case from typical finite-time relaxation.

## Closest sources and limitations

The closest inspected sources are Fisch–Gravner (1995), *One-dimensional Deterministic Greenberg–Hastings Models*, Section 5; Gravner–Lyu–Sivakoff (2016/2018), *Limiting behavior of 3-color excitable media on arbitrary graphs*, introduction and finite-tree/height results; and the published three-color finite-path maximum-extinction enumeration of 2026-11-08. None contains the derived four-or-more-state double-star last-layer count. The original full PDF of the 1993 foundational arXiv source was not available during inspection, and priority uncertainty remains. Only maximal extinction times are enumerated; no full intermediate-time census or independent review is claimed.

Self-review: passed. Independent audit: not yet performed.
