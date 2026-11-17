# Scientific review: one-way multi-state excitable rings

## Correctness
**PASS.** Each excitation descends from exactly one initial excitation and moves one step at a time until blocked. A local forward window gives an exact first-blocking test: any initially refractory blocker must lie within its unrecovered distance, while a competing excitation can obstruct only when the initial sources are separated by fewer than \(q\) cells. Hence particles either die within \(\min(n,q-1)\) steps or survive forever; finite refractory tails disappear within an additional \(q-2\) steps. Explicit initial configurations attain the stated bound in both circumference regimes. Temporal recurrence, the hard-rod gap count, Möbius inversion, and entropy follow. The finite independent programs reproduced the predicted counts and survivor configurations.

## Originality
**PASS, with residual historical-priority uncertainty.** The full 1995 one-dimensional Greenberg–Hastings study uses symmetric rather than directed one-input neighborhoods and studies infinite-lattice phases, not the sharp finite directed-cycle clock. The 2016 full-text treatment is restricted to three colors and undirected graphs. A previously known three-state directed-ring identity is explicitly excluded by the \(q\ge4\) domain. The nearest related results therefore do not directly imply this full multi-state theorem. Unindexed earlier oriented-automaton literature and the unread full 1978 foundational article remain priority risks; absence of a database hit is not proof of novelty.

## Value
**PASS.** Refractory memory yields the exact and counterintuitive ring-size transition \(T_q(n)=q+\min(n,q-1)-2\), which saturates independent of the number of cells. The same structural particle argument produces the complete time-resolved periodic-orbit census and exact recurrence entropy across all color counts and all ring lengths. This identifies a natural solvable directed excitable system and yields a rigorous comparison target for bidirectional and higher-degree excitable media.

## Closest literature and limitations
Fisch–Gravner (1995), full-text accessible, has general-color pulse interactions but symmetric neighbors and unbounded lattice dynamics. Gravner–Lyu–Sivakoff (2016), full-text accessible, addresses three-color undirected graphs. The 1993 threshold-range preprint supplies archival model context but not a directed finite-orbit theorem. Historical priority is qualified; numerical verification is finite and independent external mathematical validation remains to be done.

Self-review: passed. Independent audit: not yet performed.
