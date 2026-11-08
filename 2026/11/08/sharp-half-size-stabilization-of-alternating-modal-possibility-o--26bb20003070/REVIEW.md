# Scientific review

**Correctness — PASS.** With \(B_0=\varnothing\), the exact modal recurrence is \(B_{t+1}=\{x:\exists y\in R(x),\ R(y)\subseteq B_t\}\). An induction shows that any world first lost at step \(t\) has a never-lost successor whose outgoing worlds have maximum finite loss rank \(t-1\). Recursing on ranks gives two distinct vertices per step, and a simple path to a dead end; hence the \(2t\)-world lower bound. A directed path realizes each rank. The proof explicitly addresses empty successor sets, arbitrary loops and cycles, the base rank, and all positive integers; the checker tests exact finite semantics but is not treated as an infinite certificate.

**Originality — PASS within the inspected evidence.** The most relevant 2026 preprint [1] gives separating paths at every depth, but expressly states that this does not prove minimality. Its lower-bound certificates cover only the first three depths. The new part is a uniform lower-bound/witness theorem and the sharp global stabilization consequence. A semantic search of indexed published findings for this exact operator and path length, its minimal-countermodel aliases, and alternating game iteration did not return an equivalent claim. Generic modal fixed-point approximants [2] and path examples do not entail the half-size extremal inequality without the rank-infinity witness argument. Relevant older unindexed game-semantics literature remains a residual historical risk.

**Value — PASS.** The work closes the explicit all-depth minimum-size gap left by [1], promotes three finite cases to a universal structural theorem, and gives a sharp stopping depth for this natural modal fixed-point approximant on every finite frame. The compulsory simple-path certificate explains why one world per iteration is impossible. This is a natural exact invariant, not a parameter substitution or a known-table recomputation.

**Limits and risks.** No claim is made for arbitrary contexts or initial valuations; the witness path is not generally induced. Older alternating-reachability or fixed-point sources might contain the same sharp fact under different terminology. Independent mathematical and historical-priority audit remains outstanding.

[1] Alpay and Basaran, *GPU-Accelerated Search and Certification of Bounded Indistinguishability in Finite Kripke Semantics*, arXiv:2606.15437v1, Sections 6–7, Proposition 5, Lemma 2, Table 3 (2026-06-13).

[2] *Modal Logic: A Contemporary View*, Internet Encyclopedia of Philosophy, section on the modal \(\mu\)-calculus.

Self-review: passed. Independent audit: not yet performed.
