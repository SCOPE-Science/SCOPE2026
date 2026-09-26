# Independent audit — 2026/09/09/067

## Correctness — FAIL for the genus-8 Brill–Noether headline

The underlying finite graph has V=19, E=24, so its first Betti number is 6. I replayed the original 19-vertex Dhar verifier: all 190 vertex pairs are winnable and the indicated triple is not, confirming the graph Baker–Norine rank r_G(D*)=2 under the standard rank-determining vertex-set criterion. The augmented genus is 8 only after adding the genus-2 curve at vs. The asserted Brill–Noether number −4 uses that augmented genus, but no rank-2 divisor on the metrized complex was established: graph firing ignores linear series on the genus-2 component. For the object actually computed, ρ(6,2,6)=6−3(6−6+2)=0, not −4. Thus the statement “tropically BN-special (ρ<0 yet rank 2)” mixes two distinct rank theories and is unsupported; it is a material part of the accepted result, despite the limitation paragraph conceding the missing complex rank. No non-liftability conclusion follows.

## Originality — FAIL as framed

CDPR's pure-chain Brill–Noether theory and Amini–Baker's metrized-complex framework distinguish the relevant ranks. A single finite graph-rank computation at ρ=0 does not establish the promised augmented-hinge phenomenon. The specific chip placement may be new finite data, but that does not rescue the asserted genus-8 exception.

## Scientific value — FAIL for the intended lifting question

The certificate verifies a graph-only test input. Its purported negative-ρ witness and characteristic-zero lifting obstruction disappear without a metrized-complex rank calculation, so it does not advance the stated realizability problem.

## Sources

- Original RESULT.md, METADATA.json and verify19.py replay (V19,E24, 190 pair tests, triple failure).
- Amini–Baker, https://arxiv.org/abs/1204.3508 .
- Cools–Draisma–Payne–Robeva, https://arxiv.org/abs/1001.2774 .
- Luo, rank-determining sets, https://arxiv.org/abs/0906.2807 .
