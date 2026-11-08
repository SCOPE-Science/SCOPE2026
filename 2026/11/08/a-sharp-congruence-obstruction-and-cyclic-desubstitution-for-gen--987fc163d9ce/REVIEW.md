# Scientific review

## Correctness — PASS

The theorem reduces every rotation-complete circular factor beyond the sharp threshold to a length-\(b\) uniquely phased transition code. The block code \(0^{b-2}1\epsilon\) has one mandatory transition and at most one optional transition per block; every length-\(b\) window fixes its phase. A full cycle of length \(n\) forces \(n\equiv0\pmod b\). The exact morphic desubstitution is reversible because a one-position-inside-block rotation determines the cyclic length-\((m+1)\) source extension. The short exceptional values use run lengths \(1,b-1,b\) and an explicit ternary four-factor check. `verify.py` independently compares directly enumerated cyclic classes with the desubstituted classes at 408 tested base/length pairs. The proof, not the finite test, establishes the infinite statement.

## Originality — PASS, with limits

Bell and Shallit, *Lie complexity of words* (2021; https://arxiv.org/abs/2102.03821), introduce the invariant and prove automaticity for automatic words. Their examples include the ordinary Thue–Morse and Cantor words but do not supply this generalized Mephisto–Waltz congruence support or its one-step cyclic source-window bijection. Li, *A note on the Lie complexity and beyond* (2022; https://arxiv.org/abs/2207.05859), provides general Rauzy-graph and extended-Lie bounds, again without this same-word conclusion in the inspected sections. Earlier ordinary-square calculations for the classical Mephisto–Waltz word, and earlier palindrome work for the generalized family, concern different invariants: neither determines all rotation-complete cyclic classes. The distinct geometric-marker-word Lie computation concerns a different word family. An uncatalogued recognizable-substitution theorem could still dominate this result, so novelty is best-knowledge, not independently certified.

## Mathematical value — PASS

The sharp zero-support congruence and bijection provide exact all-length structural information for an infinite natural family of binary automatic words. They separate the new invariant from ordinary-square spectra, and the value \(L_b(2b)=3\) plus infinitely many nonvanishing multiples demonstrates a nontrivial surviving language. The result does not rely on arbitrary finite cutoff choices. It does not claim a numerical formula for every surviving multiple.

## Limitations

The source-window cardinality is a classification, not a simplified closed numerical sequence at every multiple. Base \(b=2\) is excluded by failure of phase uniqueness. The computational checks are finite; an independent audit and broader bibliographic check remain unperformed.

Self-review: passed. Independent audit: not yet performed.
