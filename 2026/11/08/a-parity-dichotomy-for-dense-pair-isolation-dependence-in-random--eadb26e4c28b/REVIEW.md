# Self-review

## Correctness — PASS

The assertion applies to a fixed even integer \(n\ge4\), distinct vertices, and the degree-even conditional law with \(0<p<1\). The exact parity-projection expression for \(P_m\) has a direct character-sum derivation, and removal of incident edges yields exact individual and joint isolation probabilities. At \(p=1/2\) the partition probability is \(2^{1-m}\) for \(m\ge1\). At \(p\uparrow1\), complementing a graph of even degree on even \(n\) vertices produces an odd-degree graph, whose edge minimum is a perfect matching. On odd orders, the complete graph has even degrees and hence the pair-isolation probability dominates the product of its one-point probabilities. The leading coefficient is \((n-1)!!\); the two-point event is of strictly higher order than the product of the one-point events. This reconstructs the sign conclusion with no numerical extrapolation. Exact rational exhaustive checks for \(n=3,4,5,6\) and finite formula checks corroborate the derivation. No general uniqueness is claimed.

## Originality — PASS, with residual priority risk

The closest direct literature is Grimmett and Janson, *Random even graphs* (arXiv:0709.3039), which defines the even-edge law and develops its Ising/random-cluster relationship, and Grimmett and Janson, *Random graphs with forbidden vertex degrees* (arXiv:0712.0270), which studies degree-constrained random graphs. The latter's Example 5.4 explicitly lists even graphs on four vertices, so that subcase's enumeration is acknowledged as prior coverage. The **unbounded even-order conditional two-vertex isolation covariance sign change**, with its fixed-order dense asymptotic, was not located in the inspected sections or targeted source searches. The generic parity identity alone does not explicitly settle the sign comparison without additional complement-parity asymptotics. Since the 2007 work treats a broader model, some conclusions may be derivable implicitly, and historical priority remains uncertain.

## Value — PASS

The established boundary is a counterexample, in every even order, to the tempting expectation that isolations must remain positively correlated under global even-degree conditioning. The indicators are positively correlated at the uniform-even-graph parameter in every order; in the dense limit they are positive for odd orders and negative for even orders. The statement concerns a natural conditioning law relevant to random Eulerian graphs, and identifies the mechanism through the minimum-degree parity obstruction and perfect-matchings of the complement. It is not a single arbitrary small-graph calculation: it applies to all even orders and has an explicit asymptotic scale.

## Limits and outstanding comparisons

General uniqueness of the crossing and an odd-order classification are outside the claim. The proof does not establish a nontrivial joint large-\(n\), high-density limit. The parity-dependent sign phenomenon was not explicitly found in the two inspected primary works, but no exhaustive historical-priority guarantee is asserted.

Self-review: passed. Independent audit: not yet performed.
