# Exact three-level online EF1 and unavoidable temporary envy for three agents and four goods

## Finding

Fix exactly three agents and exactly four sequentially arriving indivisible goods. Each agent has an additive, strictly positive valuation, and for agent \(i\) every single-good value lies in a known ordered alphabet of at most three levels \(0<a_i<b_i<c_i\). Alphabets may differ between agents. Each item's three values become known upon arrival, after which that item must be assigned immediately and irrevocably to one agent. There are no predictions of future item values; fairness is required at the end, not at every intermediate time.

There exists a deterministic online rule that guarantees **exact final envy-freeness up to one good (EF1)** against every adaptive value sequence. The positive result is sharp in alphabet size: for any four strictly ordered positive levels for each agent, an adaptive adversary defeats **every** deterministic online rule, even with the four-good horizon known in advance.

Moreover, no rule assigning the first two goods to *distinct* agents on every history can guarantee final EF1 in the three-level setting; nor can a rule assigning the first two goods to the *same* agent on every history. Consequently every deterministic rule guaranteeing final EF1 must sometimes make each choice, depending on observed values. In particular, it must sometimes violate EF1 after the second arrival, although it guarantees EF1 after the fourth.

## Assumptions and scope

Let agents be \(N=\{0,1,2\}\) and arrivals \(G=\{g_0,g_1,g_2,g_3\}\), in this order. Before choosing the recipient of \(g_t\), the allocator observes its complete valuation vector \(v(g_t)=(v_0(g_t),v_1(g_t),v_2(g_t))\). The adversary chooses this vector after seeing the allocation history up to \(g_{t-1}\). The horizon \(|G|=4\) is known. An allocation \(A=(A_0,A_1,A_2)\) is EF1 when, for every two distinct agents \(i,j\), either \(A_j\) is empty or there is \(g\in A_j\) such that

\[
v_i(A_i)\ge v_i(A_j\setminus\{g\}).
\]

We require a complete allocation with no discarded good and no reassignment. The result applies to arbitrary strict positive level values (not merely the numerical levels used by the verifier). Repeated levels among different goods are permitted, as are different level scales across agents. No approximation, ex ante randomization, temporal-EF1 guarantee, or unknown-horizon guarantee is asserted.

## Proof

**Ordinal reduction.** Because every agent values every good strictly positively, a final EF1 allocation of four goods among three agents must have bundle-cardinality multiset \((2,1,1)\). Indeed, if some agent receives nothing, another has at least two goods, and that empty agent still strictly envies after deletion of any one good. Conversely, consider a cardinality pattern \((2,1,1)\), with doubled bundle \(\{g,h\}\) owned by \(j\). Comparisons with singleton bundles are automatically EF1. For either singleton holder \(i\ne j\), with own good \(s_i\), the sole nontrivial requirement is

\[
v_i(s_i)\ge\min\{v_i(g),v_i(h)\}.
\]

It follows that the terminal EF1 indicator is completely determined by the relative order of each agent's values, including ties. Replacing the \(L\) positive values of each agent independently by ranks \(0,1,\ldots,L-1\) leaves the indicator unchanged. This reduction is valid specifically because of the fixed four-good/three-agent cardinalities, and it covers *all* real magnitudes in each ordered alphabet.

**Exact finite adversarial game.** For an integer \(L\ge1\), let \(V_L=\{0,\ldots,L-1\}^3\). A length-\(t\) history \(H\) records the first \(t\) triples and their recipients. Define \(B_t(H)\in\{0,1\}\), indicating whether the adversary has a forcing strategy against the allocator from \(H\). At the terminal layer, set \(B_4(H)=1\) exactly when the allocation violates EF1. At every earlier layer define

\[
B_t(H)=\max_{w\in V_L}\min_{j\in J_t(H)} B_{t+1}(H\mathbin{\|}(w,j)),
\]

where \(J_t(H)=N\) for unrestricted play. The adversary chooses \(w\) first and the allocator observes it before choosing \(j\), so the order of the quantifiers is essential. For the *different-first-two* game, restrict \(J_1(H)=N\setminus\{j_0\}\), where \(j_0\) received the first good. For the *same-first-two* game, restrict \(J_1(H)=\{j_0\}\). All other layers have unrestricted actions. Every maximum and minimum is over an explicit finite set.

The accompanying exact recurrence implementations `verification/verify_game.py` and `verification/verify_numeric.cpp` independently establish the four initial game values:

| Number of ranks | Second-good rule | \(B_0(\emptyset)\) |
|---|---|---:|
| \(3\) | unrestricted | \(0\) |
| \(3\) | must choose a different recipient | \(1\) |
| \(3\) | must choose the same recipient | \(1\) |
| \(4\) | unrestricted | \(1\) |

The Python program uses the reduced ordinal terminal predicate; the C++ program separately uses the cardinal EF1 inequality with positive integer levels. Both perform exact Boolean backward induction and assert the displayed game values. They are finite exhaustive certificates with logical short-circuiting, not Monte Carlo searches.

When \(B_0(\emptyset)=0\), the recurrence constructs a deterministic online strategy: upon observing a new valuation triple at any reachable losing state for the adversary, choose the least-indexed recipient whose successor still has value \(0\). Such a recipient exists by the recurrence, and induction keeps the adversary from reaching a terminal failure. Conversely, when \(B_0(\emptyset)=1\), at each history the adversary selects a triple attaining the maximum; all permitted allocator choices lead to another adversary-winning state, proving impossibility. These are explicit finite deterministic procedures, not assertions based on random trials.

Since every instance with at most three value levels embeds into a three-rank instance, the first game value proves sufficiency for all smaller alphabets too. Since the four-rank adversary can choose only a fixed four-element subset of any larger alphabet, the last game value proves impossibility for any alphabet with at least four levels. The two constrained three-rank game values show that neither fixed first-two occupancy pattern can guarantee success. A successful unrestricted policy must therefore use both patterns on different histories. Assigning two strictly positive goods to the same agent while another agent has none necessarily violates EF1 at that intermediate time, proving the final assertion.

## Verification

Run both standalone checkers from this package root:

```sh
python3 verification/verify_game.py
g++ -std=c++17 -O2 verification/verify_numeric.cpp -o verify_numeric
./verify_numeric
```

The Python verifier's four results are, in order: `False`, `True`, `True`, `True` for adversary forcing success in (three ranks/unrestricted), (three ranks/first-two distinct), (three ranks/first-two same), and (four ranks/unrestricted). Its terminal-node visit counts, reflecting early Boolean pruning, are respectively `1623792`, `814168`, `223632`, and `6953346`. The C++ implementation independently returns `0`, `1`, `1`, `1` and uses the full cardinal EF1 predicate. Both print `ALL FOUR GAME VALUES VERIFIED` and exit successfully; neither relies on external packages or a mixed-integer solver.

To evaluate the constructed online policy on a particular observed history, run the finite recurrence on each possible next recipient and select the first with successor adversary-win value \(0\). This may be computationally expensive; no polynomial-time running time is claimed. The four values establish a finite game theorem valid for arbitrary positive real level magnitudes by the ordinal reduction above.

## Relationship to prior work

Neoh and Teh, *Online Fair Division with Frequency Predictions* (arXiv:2610.34625v1, first posted October 25, 2026), establish general approximate EF1 guarantees and a negative result for five or more agents, including four or more value scales in a many-agent construction. Their examined introduction, Sections 3–4 and appendices do not state the exact three-agent/four-good three-tier cutoff or the necessary first-two occupancy adaptivity. Their guarantees for three agents are approximate, not the present exact terminal guarantee.

Wang and Wei, *Online Fair Allocations with Binary Valuations and Beyond* (arXiv:2505.24321v2), prove impossibility statements for tri-valued domains in a model that requires fairness at **every** arrival. Their three-agent/four-good adversarial example therefore does not imply the absence of a terminal-only guarantee; the present necessity of temporarily violating EF1 explains the discrepancy. Elkind et al., *Temporal Fair Division of Indivisible Items* (arXiv:2410.14593v1), treat fairness throughout the sequence and include a positive theorem for two **global item types**, a different structural restriction from three personalized value levels and terminal fairness.

The previously known two-agent/three-good exact ordinal-alphabet boundary concerns a strictly smaller market and does not imply an online strategy for three agents. Its claims are not reproduced here. The contribution is the three-agent surplus-good cutoff together with necessary non-fixed early occupancy decisions.

## Limitations

This theorem is for exactly three agents, exactly four goods, additive strictly positive utilities, known four-good horizon, complete irrevocable assignment, and deterministic algorithms against an adaptive adversary. It does not imply temporal EF1 or any infinite-horizon or large-market guarantee. Cardinal ratios matter for other cardinality patterns and longer horizons; the ordinal reduction must not be extrapolated. The positive algorithm is a finite backward-induction oracle and may be inefficient. The literature comparison is limited to accessed primary texts and searched research records; unindexed equivalent exact finite-game results remain possible. Independent scientific validation has not been performed.

## References

1. T. Y. Neoh and N. Teh. *Online Fair Division with Frequency Predictions.* arXiv:2610.34625v1 (October 25, 2026). https://arxiv.org/html/2610.34625v1
2. Y. Wang and T. Wei. *Online Fair Allocations with Binary Valuations and Beyond.* arXiv:2505.24321v2 (September 9, 2025; first public preprint May 30, 2025). https://arxiv.org/html/2505.24321v2
3. E. Elkind and coauthors. *Temporal Fair Division of Indivisible Items.* arXiv:2410.14593v1 (October 18, 2024). https://arxiv.org/html/2410.14593v1
