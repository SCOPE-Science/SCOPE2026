# Exact four-good EF1 with frequency predictions and early-allocation obstructions

## Finding

**Theorem.** Consider exactly three agents and exactly four indivisible goods with strictly positive additive valuations. Before the first arrival, each agent learns the **exact multiset of her four single-good values**, but not their order or the values other agents assign to the same good. An adaptive adversary chooses each arriving value vector subject to those multisets, and each good must be assigned immediately and irrevocably.

There is a deterministic online policy guaranteeing envy-freeness up to one good (EF1) after all four arrivals. The policy can be chosen to allocate the first two arrivals to different agents on every input. Moreover, even when all three agents have the same four distinct positive predicted values, neither of the following restricted policy classes contains a guaranteed-EF1 policy: policies that always give the first two arrivals to one agent, and policies that always give the first three arrivals to three different agents.

Thus exactly one surplus good beyond the three-agent one-good-each horizon already creates a genuine distinction between adaptive allocations and simple fixed early-allocation patterns, while exact frequency predictions nevertheless suffice for exact terminal EF1.

## Assumptions and scope

The agents are labeled \(1,2,3\). The four goods arrive in an unknown order. All twelve single-good values are strictly positive; ties are permitted. Each agent has an additive valuation \(v_i\). The adversary may choose alignments and order adaptively but cannot change any agent's predicted multiset. The policy is deterministic, has no buffer and cannot reassign past goods. There is no welfare-optimality requirement and no claim of fairness before the fourth good.

For all distinct \(i,j\), EF1 means there exists \(g\in A_j\) such that \(v_i(A_i)\ge v_i(A_j\setminus\{g\})\), whenever \(A_j\) is nonempty. The two restrictions in the theorem are universal rules about the first two or three allocation decisions on every possible input, not assumptions about which agent is named first.

## Proof

**1. Ordinal reduction.** Since all four goods are strictly positive to every agent, a four-good EF1 allocation must have bundle cardinalities \((2,1,1)\) up to permutation. Otherwise some agent gets no good while another gets at least two, and that empty agent still envies after one good is removed. In a \((2,1,1)\) allocation, every comparison involving an envied singleton is automatic. If agent \(j\) has the double bundle \(\{x,y\}\), EF1 reduces exactly to
\[
 v_i(z_i)\ge \min\{v_i(x),v_i(y)\}\quad\text{for both singleton agents }i\ne j,
\]
where \(z_i\) is singleton agent \(i\)'s good. Thus the answer depends only on each agent's weak order of the four item values, not on value ratios or sums.

Give each agent four artificial strict ranks \(0,1,2,3\) in increasing order of predicted value. When predictions contain ties, assign the tied ranks to successive actual equal-valued arrivals by any fixed deterministic rule. This produces a bijection of rank labels to actual goods preserving all strict comparisons of unequal values. A strategy that wins for every permutation of four distinct ranks therefore also wins in the presence of ties: a successful rank comparison implies the corresponding weak numerical comparison.

**2. Finite adversarial recursion.** A state consists of the remaining ranks \(R_i\subseteq\{0,1,2,3\}\) for each agent and the rank vectors of previously arrived goods together with their irrevocable recipients, recorded as a multiset \(H\). Initially \(R_1=R_2=R_3=\{0,1,2,3\}\) and \(H\) is empty. At a nonterminal state the adversary may reveal any vector \(r\in R_1\times R_2\times R_3\); the allocator may then give it to any of the three agents, after which its components are deleted from the corresponding remaining sets. The finite game-winning predicate is defined by
\[
 W(R,H)=\bigwedge_{r\in R_1\times R_2\times R_3}
       \bigvee_{a\in\{1,2,3\}} W(R\setminus r,H\cup\{(r,a)\}),
\]
with terminal value given by the two singleton-versus-double ordinal inequalities in step 1. All terminal states have four arrivals. Under a restricted policy the disjunction includes only legal early recipients. The recursion is well-founded because every successor has one fewer unconsumed rank for each agent. Because this is a finite perfect-information adversarial game, the displayed alternating-quantifier recurrence is necessary and sufficient for the existence of a deterministic winning online policy: at each arriving vector choose the least-indexed successor with value true.

**3. Exhaustive exact evaluation.** The accompanying independent Python and C++ programs implement the recurrence using two different state representations and terminal tests. The C++ program checks terminal EF1 directly by evaluating all ordered-pair bundle-value inequalities at values \(1,2,3,4\), while the Python program uses only the singleton-versus-double ordinal criterion. The four starting-state truth values are, in this order:

| Allowed policy class | Winning? |
|---|---|
| No early restriction | Yes |
| First two recipients different | Yes |
| First two recipients identical | No |
| First three recipients all different | No |

For reference the C++ memo table visits respectively \(33{,}661\), \(36{,}240\), \(9{,}825\), and \(8{,}526\) information states, whereas the independent Python implementation, with more eager branch evaluation, visits \(115{,}651\), \(104{,}443\), \(24{,}681\), and \(21{,}189\) states. These finite counts are computational checks, **not** statistical observations or extrapolations. Two explicit adaptive adversary trees for the losing restricted games are included as `four_goods_restricted_witnesses.json`: they have respectively \(27\) and \(18\) terminal paths. Every legal allocator response at every node is represented, and each terminal outcome violates EF1. The Python verifier separately checks these negative certificates.

**4. Universality and policy.** The positive entries give winning strategies against all possible four-rank streams, including every adaptive alignment. Step 1 transports the strategy to every family of strictly positive numerical predictions, including equal values. The all-different-first-two entry yields the claimed stronger constructive guarantee. The negative entries already use the common numerical predictions \((1,2,3,4)\), and by the ordinal reduction also apply to every common strictly increasing positive four-value multiset. This proves all three clauses.

## Verification

Place `verify_four_goods_frequency.py`, `verify_four_goods_frequency.cpp`, and `four_goods_restricted_witnesses.json` in one directory. With Python 3 and a C++17 compiler, run:

```bash
python3 verify_four_goods_frequency.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_four_goods_frequency.cpp -o verify_four_goods_frequency
./verify_four_goods_frequency
```

Both programs contain their own expected-value assertions and require no third-party packages. The Python program additionally validates both complete losing adversary trees. Output from execution of the embedded files is recorded in `EXACT_CHECKS.txt`.

## Relationship to prior work

Neoh, Peters and Teh introduced the per-agent frequency-prediction information model and established share-based transfer results; their paper does not imply general EF1 for three agents. Neoh and Teh subsequently established \(1/2\)-EF1 for three agents, while leaving exact EF1 outside their general guarantee. The present result concerns the **exact** guarantee at the natural first-surplus-item horizon and identifies restrictions on the early allocation policy. General claims for all horizons cannot be inferred from this result. Earlier online work on personalized two-value valuations treats a substantially narrower valuation alphabet and different prediction or lookahead information; its positive statements do not imply the arbitrary four-level instance here.

## Limitations

Only three agents and at most four arrivals are addressed; this theorem does not settle exact EF1 for larger horizons, and it does not assert efficient implementation as the number of agents or arrivals varies. The ordinal reduction uses positivity in proving that all final EF1 allocations have the \((2,1,1)\) bundle pattern. A separate proof would be necessary for zero-valued goods, chores or nonadditive valuations. Computation certifies the finite rank game because the proof reduces the stated infinite cardinal domain to that finite game; the numerical tables alone would not prove a claim at other horizons. The scientific assessment is not an independent validation.

## References

1. T. Y. Neoh and N. Teh, *Online Fair Division with Frequency Predictions*, first posted 2026-10-25, arXiv:2610.34625, https://arxiv.org/abs/2610.34625.
2. T. Y. Neoh, J. Peters and N. Teh, *Online Fair Division with Additional Information*, first posted 2025-05-30, arXiv:2505.24503, https://arxiv.org/abs/2505.24503; ICML 2026, https://proceedings.mlr.press/v306/neoh26a.html.
3. G. Amanatidis, A. Lolos, E. Markakis and V. Turmel, *Online Fair Division for Personalized 2-Value Instances*, first posted 2025-05-28, arXiv:2505.22174, https://arxiv.org/abs/2505.22174.
4. Y. Wang and T. Wei, *Online Fair Allocations with Binary Valuations and Beyond*, first posted 2025-05-30, arXiv:2505.24321, https://arxiv.org/abs/2505.24321.
