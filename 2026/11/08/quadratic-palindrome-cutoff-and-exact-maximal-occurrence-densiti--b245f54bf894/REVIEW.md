# Scientific review

## Correctness — PASS
The transition equation is derived directly from the substitution. It forces one transition at residue \(b-2\) and confines all transitions to two residues. For palindromes of either length needed to rule out longer factors, the two possible reflection residues force an impossible run of \(b\) identical transition symbols. A separate residue argument treats equality, including the exceptional base-three parity condition. The occurrence condition is equivalent to a run of \(b\) parent letters, and transition frequencies provide the exact densities. The packaged finite verifier checks a broad but explicitly finite range; it does not replace the infinite argument.

## Originality — PASS (best-knowledge, with residual risk)
The central source, Dvořáková--Ochem--Opočenská (2023), optimizes critical exponents under restrictions on the number of palindromes. Frid--Laborde--Peltomäki (2020) establish automaticity of prefix-palindromic-length differences assuming finitely many palindromes, not the exact threshold or occurrence data here. Bulgakova--Frid--Scanvic (2022) analyze a different fixed point. Exact family/alias and parameter searches in the mathematical-record index and primary-source searches revealed no implication covering this result; see `AUDIT.json` for exact comparisons. Unindexed equivalent results remain possible.

## Value — PASS
The theorem is an exact all-base classification of a natural palindrome invariant for a primitive automatic family, with a sharp quadratic length transition, only two longest factors, all occurrence positions and exact densities. The base-three case is a classical named sequence; the base-two exception distinguishes the bounded-palindrome regime from the unbounded Thue--Morse regime. This supplies a concrete setting for automatic palindromic-length questions without claiming to solve those separate problems.

## Scope and limitations
Base two is excluded; shorter palindromes and exact prefix palindromic-length functions are not classified. Verification is finite diagnostics plus a symbolic proof; prior-art completeness and independent evaluation remain open.

Self-review: passed. Independent audit: not yet performed.
