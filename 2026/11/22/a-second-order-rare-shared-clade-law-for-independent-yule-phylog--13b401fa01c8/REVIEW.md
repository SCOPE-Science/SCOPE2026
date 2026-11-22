# Review of the rare shared-clade asymptotic

## Correctness — PASS

The YHK single-clade probability and two-clade probability are supported by Zhu–Degnan–Steel, arXiv:1101.1311, Lemma 4.2 and Theorem 4.5. All first and second Bonferroni contributions were reconstructed with their combinatorial multiplicities. The exact disjoint-triple probability is \((35n-141)/(35\prod_{j=1}^5(n-j))\), the nested-triple conditional probability is \(1/6\), and the coefficient simplifies to \(1/2+6/25-1/72-2/75=1259/1800\). Expected larger-clade counts and third intersections are of order \(n^{-3}\). Enumeration through six taxa and single-tree enumeration on seven taxa verify exact identities; computations do not establish infinite claims.

## Originality — PASS, with limitation

Steel (1988) and Steel–Penny (1993) address symmetric-difference/partition metrics and asymptotic Poisson overlaps, so a general Poisson limit for matching cherries is **not** a claimed novelty. Zhu–Degnan–Steel (2011) supplies exact *one-tree* probabilities, including pairs of specified clades; those ingredients are explicitly credited. The assessed claim is instead the second-order *two-tree* non-cherry event probability, requiring the nested three–four, two-triple and disjoint-pattern contribution comparison. It is not logically determined by a first-order Poisson limit. The 1993 paper's abstract indicates potentially broad comparison coverage, and its complete text could not be examined: historical priority is consequently qualified.

## Value — PASS

A shared proper clade is a fundamental unit of topological agreement between independently generated evolutionary trees. Cherries form the leading order-one overlap, so the first coincidence beyond cherries is a motivated, sparse-event boundary. The explicit \(1/(6n)\) scale, the nontrivial \(1259/1800\) correction, and conditional unique-triplet localization give a usable refined null benchmark. The calculation distinguishes nested near-collisions from disjoint ones and is not a table recomputation or arbitrary size cutoff.

## Limitations and sources

The theorem excludes non-independent models, unrooted splits, and nonbinary trees. Relevant inspected full texts include Zhu–Degnan–Steel (arXiv:1101.1311), Zhu–Than–Wu (arXiv:1407.3880), Bryant–Steel (arXiv:0810.0868), and Wu–Choi (arXiv:1508.03139). Steel–Penny (1993), DOI:10.1093/sysbio/42.2.126, was examined through its publisher abstract and bibliographic context only; its full text was inaccessible. No independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
