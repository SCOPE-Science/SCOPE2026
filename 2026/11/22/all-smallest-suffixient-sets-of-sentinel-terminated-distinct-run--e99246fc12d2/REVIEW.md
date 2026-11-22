# Scientific review of the minimum suffixient-set census

## Correctness

**PASS.** The claim is exact for all integer parameters \(q\ge2\), \(k\ge2\) and \(r_i\ge2\), with a unique terminal letter. A mixed factor of the infinite periodic word identifies its phase from its first change of letter; every mixed right-branch in the finite word must therefore be caused by the sentinel at the end. This gives precisely the two long SREs, while the remaining SREs are short unary-to-next-run branches. Distinct end offsets give independent \(k\)-fold occurrence choices. The full direct substring checker confirms the list and its endpoint sets on 246 varied instances and exhaustively enumerates minimum sets in four small examples. The proof, rather than the tests, covers all parameters.

## Originality

**PASS against inspected evidence.** The 2026 Köppl–Kucherov source defines and maintains suffixient sets, and Cenzato et al. give general suffixient-array constructions. The full 2025/2026 Fujimaru–Navarro–Romana–Urbina paper likewise concerns broad bounds and distinct Fibonacci/episturmian families, not this periodic family. None of these inspected primary texts supplies this symbolic all-parameter SRE classification or count. The closest published special-family formula is for *string attractors* of the unmarked distinct-run powers, not for suffixient sets of the marked word; string attractors cover all factors, whereas suffixient sets require endings of right extensions and have larger minimum cardinality here. The checked published research records do not contain a corresponding suffixient-set theorem. Indexed retrieval and external literature search cannot rule out all unindexed equivalents.

## Value

**PASS.** Suffixient sets are a computable repetitiveness measure used in compressed pattern indexes. Determining all optimal position sets is more informative than computing their size, and generally difficult for factor-covering structures. This theorem provides a complete, length-independent characterization and an exact enumeration for arbitrary alphabet sizes, repetition counts and independent run lengths in a natural class of highly repetitive texts. It quantifies a gap of \(q\) positions from minimum string attractors on the same sentinel-terminated text, a concrete reason the two measures are not interchangeable.

## Evidence and limitations

Primary literature: arXiv:2604.27548v1, full MFCS 2026 HTML (definitions and SRE representation); Cenzato et al., Theory of Computing Systems 70, article 50 (open full text); Fujimaru et al., arXiv:2506.05638v7 (full HTML); the related published cyclic-bigram attractor result (complete `RESULT.md`). Verification files: `verify.py`, `verify_output.txt`. The conclusion depends on the unique terminal marker and all runs having length at least two. There is no claim of a general classification of periodic words, and no independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
