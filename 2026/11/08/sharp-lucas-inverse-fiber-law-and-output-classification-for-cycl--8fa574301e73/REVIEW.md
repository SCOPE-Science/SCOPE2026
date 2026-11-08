# Self-review

## Correctness

**PASS.** The de Bruijn transfer matrices enumerate indexed cyclic predecessors without quotienting periodic configurations. Direct multiplication yields the exact two-state gap reduction, and the nonnegative matrix inequality \(EF\le F\) bounds all adjacent-one outputs strictly below the Lucas optimum. The equality classification follows from maximal independent sets of even and odd cycles. The standard-library verification script independently counted all output fibers through length 17 and reproduced the predicted optimizers; it is supporting evidence, not a substitute for the proof. The only short-length exceptions were explicitly isolated.

## Originality

**PASS, qualified.** The nearest substantive source is Jen's 1989 full-text preimage enumeration and its Section 5.4 maximal-probability analysis. It establishes alternating optimizers for another elementary rule and gives finite-string constructions, but not the sharp cyclic Rule 28 Lucas count and equality list. Fukś's 2003 analysis uses iteration depth instead of growing ring length; Voorhees's predecessor study is for compositional rules; asynchronous Rule 28 dynamics is governed by a different update scheme. Related published results on cellular-automaton reversibility or inverse counts for other channels and rules do not imply the present statement. The main priority risk is older per-rule enumeration tables, unpublished formulae or reducibility to Jen's general machinery; search failure alone is not proof of novelty. The precise new contribution is the cyclic optimum **and all maximizing indexed output words**, not the classical transfer-matrix method.

## Value

**PASS.** Single-step inverse branching is an intrinsic uncertainty measure for finite cellular-automaton dynamics and finite-state reconstruction. A sharp all-length growth law, a complete optimizer classification, and an exact formula for every cyclic output are mathematically motivated structural information, not just a finite computation or a renamed classical identity. The periodic boundary condition changes both the value and optimizer classification relative to known linear-string analyses.

## Scientific limits and closest literature

This is a complete result for a single synchronous elementary rule. It does not classify other rules or multi-step dynamics. Jen (1989), Fukś (2003), and Voorhees (1996) were inspected in primary full text, and the asynchronous Rule 28 paper was compared at its Rule 28 section. The possibility of historical priority through unindexed tables or supplements remains open. Finite verification reached length 17 exhaustively; the proof covers all lengths. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
