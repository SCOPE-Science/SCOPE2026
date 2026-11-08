# Scientific review: one-wildcard endpoint enumeration

## Correctness — PASS

The claim fixes the linear-word normalization, labeled binary alphabet, unique joker, wildcard location and no symmetry quotient. It follows from the published necessary forced-prefix lemma, open Euler-trail BEST enumeration, and a directed rooted-tree ratio derived from a finite overlap Green function. The full de Bruijn root-tree count is derived independently by the finite-step uniform random walk. The three-by-three ratio is evaluated for all integers \(n\ge4\), with a separate explicitly computed \(n=4\) matrix, and both smaller cases are treated directly. The residual graphs are genuine directed graphs with correctly tracked edge identities; their Euler-trail factorial weights are all one. The packaged standard-library checker independently recomputes direct counts, large graph determinants and Green-function determinants. The infinite claim depends on the exact symbolic derivation, not these finite experiments.

## Originality — PASS, qualified

Chen, Kitaev, Mütze and Sun, *On universal partial words*, arXiv:1601.06456, provide the exact prerequisite forced-prefix lemma and existence at the first two positions (their Lemma 4 and Theorems 9–10), but their examined theorem statements and construction sections do not give a formula counting *all* completions. Their small examples and existence table do not imply a solution-space census. The new quantity is the exact number of linear one-wildcard words per each of these two locations, with a nontrivial parity correction at the second location, not the existence result, not the classical de Bruijn count, and not the mere fact that BEST applies. Distinct related work on nonbinary or cyclic universal partial words does not give this exact linear enumeration in the accessible material. A published unindexed count could remain; priority has not been independently checked.

## Value — PASS

Fixing the wildcard position identifies how placement of a single universal matching symbol changes the number of shortest complete linear dictionaries. The second-position family does not simply inherit the ordinary de Bruijn cycle count: it is governed by a rooted-tree vertex deletion and exhibits an exact parity-dependent factor. The joint all-order enumeration provides a meaningful structural invariant of the simplest nontrivial wildcard placement problem and the full counts of its solutions, rather than arbitrary small-parameter examples.

## Relevant prior literature and limitations

Primary paper: https://arxiv.org/abs/1601.06456 ; full text https://dmtcs.episciences.org/en/articles/2205/download . Later discussion of counting and nonbinary alphabets: https://arxiv.org/abs/1611.03928 . Counts for other joker positions, multiple jokers and cyclic partial words are not proved. The starting necessary-prefix lemma is appropriately credited to the primary paper. The full-proof review and reproducibility tests do not constitute independent confirmation.

Self-review: passed. Independent audit: not yet performed.
