# Scientific assessment: unique-request packing and Poisson welfare crowd-out

## Correctness — PASS

The exact claim concerns binary complement utilities \(v_i(B)=\mathbf1\{D_i\subseteq B\}\), one indivisible copy per good, complete allocations, uniform demand cardinality \(r\ge2\), and \(n\ge m\). A repeated demand cannot produce any satisfied agent without envy; the satisfied unique demands therefore form a disjoint hyperedge packing. Conversely, a packing is realized by allocating its hyperedges intact and assigning all other goods separately as singletons to distinct remaining agents. This proves both completeness and the envy conditions, without relaxation.

The algorithmic separation is the standard graph-matching/3-dimensional-matching complexity boundary applied to the exact packing equivalence. The hardness reduction pads with a duplicated dummy request that cannot contribute to welfare, preserving the original packing optimum and achieving \(n\ge m\). The finite zero-welfare identity follows from inclusion-exclusion for singly occupied request types. Poisson convergence follows from every fixed factorial moment, and a controlled expected intersecting-pair count shows that maximum packing differs from singleton count with vanishing probability and vanishing expected gap. The one-sided thresholds follow from first and second moments.

A standalone checker directly enumerated literal envy-free allocations and independently maximized unique-request packings for 10,862 small profiles (all profiles in the listed exhaustive parameter cases). Six independent finite occupancy counts agreed with the derived exact formulas. Exhaustive finite checks are not treated as proofs of unbounded claims.

## Originality — PASS, with access risk

The initiating Leontief study of Inamdar, Jain and Pandey, arXiv:2609.28308 (first public 23 September 2026), analyzes complete envy-free allocations and welfare maximization, proving broad hardness and algorithms for one good or identical demands. The inspected introduction and contribution summary do not state a unique-demand packing equivalence or Poisson crowd-out law; its principal positive-demand model differs from this claim's explicit zero-demand-outside-request variant. Full original sections and appendices were not accessible for a complete negative comparison, a nontrivial priority risk recorded in the audit.

Aigner-Horev and Segal-Halevi, arXiv:1901.09527, use *envy-free matching* to mean bipartite one-house-per-agent assignments; their polynomial-time envy-free matching theorem does not entail a packing identity for indivisible complementary bundles. Edmonds' graph matching theorem provides a standard algorithm once the new reduction is established. Karp's 3-dimensional matching hardness provides the starting problem for a new parameter-preserving construction. Classical balls-in-bins formulas explain singleton counts but do not alone imply anything about the maximum welfare of complete envy-free allocations. Targeted literature and mathematical-results comparisons did not identify a stronger theorem covering the same hypothesis-conclusion package. Negative search and categorical partitioning are not proof of publication novelty.

## Value — PASS

The motivating challenge is not merely counting demand collisions. General complete envy-free welfare maximization with perfect complements is hard, and forbidding disposal of unused goods creates an additional feasibility constraint. The structural theorem shows that enough agents can serve as singleton parking locations, converting a seemingly global envy condition into a precise packing invariant. It identifies a genuine tractability boundary at two required goods; the three-good version is NP-complete even with ample agents and one copy per resource. For uniform demands, the optimal fair welfare itself — not just a proxy count — has a universal Poisson extinction threshold. This quantifies a surprising form of crowding: adding agents can eventually destroy all positive envy-free welfare because repeated requests are mutually obstructive. The exact finite zero-welfare probability and limiting distribution are directly useful for benchmarking fair allocation of complementary resource packages.

## Closest literature and limitations

The closest primary source is arXiv:2609.28308. Related but non-covering are arXiv:1901.09527 (one-item bipartite envy-free matching), Edmonds (1965) (unconstrained graph matching), Karp (1972) (3-dimensional matching), and classical occupancy small-count literature (arXiv:0809.4387). Remaining risks include unseen discussions in the inaccessible parts of the initiating manuscript, unindexed single-minded-allocation results, and extension beyond binary unit-supply goods. The proof does not cover unequal request sizes, nonuniform correlated demands, or online irrevocable allocation.

Self-review: passed. Independent audit: not yet performed.
