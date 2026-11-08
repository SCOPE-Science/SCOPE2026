# Scientific assessment

## Correctness — PASS

The upper bound counts all nonfixed coordinatewise-involution orbits of ordered pairs. The quotient multigraph has precisely one edge per orbit and is balanced and strongly connected. Its Euler tours lift uniquely between paired symbols and freely at fixed vertices. A bit-xor telescoping argument gives the necessary obstruction for odd numbers of transposition pairs when there are no fixed symbols; removing a label-one loop restores lift closure with exactly one fewer edge. Thus both upper bounds and all matching constructions are established for every allowable \((f,r)\). The standalone verifier reproduces 56 direct constructions and a separate finite brute-force check in small cases. The infinite proof is independent of the finite tests.

## Originality — PASS, with a stated residual risk

Mitchell and Wild's 2026 full text, Sections 6 and 8, proves span-two sharpness for the special negation involutions and explicitly raises the broader alphabet-involution question. Their binary complement example accounts for \(r=1,f=0\) but does not state the general \(r\)-parity classification or the full \((f,r)\)-law. Kari and Xu 2012 use antimorphic (reversing) involutions, while Alhakim et al. 2024 study reversal-pairing. Searches for equivalent formulations, the specific formula, and dominated special cases in accessible mathematical records yielded no covering result. The claim is restricted to the precise new uniform classification; no discovery priority is claimed over unindexed material.

## Value — PASS

This resolves the complete span-two case of a natural class of pair-selecting universal-cycle problems highlighted as open in the recent source. It supplies a sharp arithmetic criterion for when the elementary orbit upper bound is attainable, and proves that all exceptional fixed-point-free cases have deficit exactly one. The single parity obstruction and constructive Euler tours give reusable structural insight beyond a single example or routine numerical table.

## Closest literature and limitations

- C. J. Mitchell and P. R. Wild, *Negative Avoiding Sequences*, arXiv:2603.25286, especially Sections 6 and 8; covers negation but explicitly asks about arbitrary alphabet involutions.
- L. Kari and Z. Xu, *De Bruijn Sequences Revisited*, Int. J. Found. Comput. Sci. 23 (2012); different antimorphic (reversal-including) orbit relation.
- A. Alhakim et al., *Orientable sequences over non-binary alphabets*, Cryptography and Communications 16 (2024); factors are paired by reversal.

The statement concerns cyclic windows of span two, allows a one-symbol period, and does not address higher spans or classify every maximizing cycle. Literature search has residual unindexed-priority risk. No independent validation has occurred.

Self-review: passed. Independent audit: not yet performed.
