# Review of three-marker binary jumbled-spectrum rigidity

## Correctness

PASS. The proof uses the independently explicit minimum/maximum length intervals for factors containing zero, one, two, or three ones. Those data recover the unordered outer and interior gap pairs, after which two canonical orientations differ in exactly one threshold. Direct algebra shows that the thresholds coincide exactly when the smaller interior gap is at least the larger outer gap, assuming both pairwise inequalities are strict. The four-element classes are parameterized bijectively by a nonnegative four-variable equation, and reversal Burnside counting yields the exact formula. The coefficient asymptotics follow from the order-four pole. Independent-in-method finite brute-force Parikh-set enumeration through length 21 and parameter enumeration through length 100 passed, but those checks are corroboration rather than infinite proof.

## Originality

PASS, qualified by historical-priority risk. The Fici–Lipták 2011 work proves a general equivalence characterization using two prefix-normal forms. The 2014 generating algorithm and the expanded 2016 preprint treat efficient generation and fixed-density counts of prefix-normal words, including density three, but those facts do not give the joint two-form fiber classification or the exact four-element ambiguity count without a further gap-orientation analysis. The 2026 jumbled-index article is algorithmic. Exact statement/implication comparisons found no cited theorem that already gives this weight-three all-length spectrum; additional claim searches and accessible historical-claim comparisons also did not yield a covering assertion. Residual risk: an unindexed specialized enumeration or implicit equivalent might exist.

## Value

PASS. A binary jumbled-pattern-matching index deliberately forgets both factor order and multiplicity; knowing precisely how many indexed inputs share an observation is a natural inverse/reconstruction problem. This theorem resolves the first nontrivial sparse-marker ambiguity threshold, gives every exact fiber size and an all-length closed enumeration, and quantifies the asymptotic frequency of non-reversal ambiguity. The partition-number appearance is structural, not merely a re-evaluation of a known integer table. This is a fixed-weight result only.

## Relevant prior literature and boundaries

Fici–Lipták (DLT 2011) supplies the general normal-form equivalence; Burcsi et al. (arXiv:1401.6346 and arXiv:1611.09017) supply generation and fixed-density normal-word counts; Cunha–Medina (2026) addresses indexing. The novelty claim excludes the general normal-form theorem, the rational generating functions for density-three prefix-normal words, and the classical restricted-partition sequence. The result has not received an external independent audit.

Self-review: passed. Independent audit: not yet performed.
