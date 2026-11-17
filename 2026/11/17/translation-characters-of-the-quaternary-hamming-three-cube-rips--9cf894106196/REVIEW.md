# Scientific review: quaternary Hamming translation character

## Correctness (PASS)

The theorem's domain is the sixty-four words in \((\mathbb Z/4\mathbb Z)^3\), inclusive Hamming threshold two, and the translation subgroup \(C_4^3\). `verify_full.py` independently reconstructs the previously published topological premise, checking the complete \(830101\)-face complex and an acyclic augmented face matching with \(405\) unmatched three-simplices. Its \(830101\)-node Hasse topological sort proves that the matching has no directed cycles. Thus the sole reduced rational homology is degree three of rank \(405\).

For each of the \(64\) translations, `character.py` computes the exact orbit-compatibility graph and its integer independence-polynomial value at \(-1\). A mathematical Lefschetz argument proves that value equals the action trace on third homology, without assuming the numerical result. Complete signed fixed-face sums, independently derived from a different facet taxonomy, verify all ten symmetry types in `direct_fixed_check.py`. Exact Gaussian-integer Fourier inversion gives the ten stated multiplicities; their total is \(405\) and nonnegative. The trace sums \(576\) and \(568\) correctly yield ranks \(9\) and \(71\) for the two invariants. The characteristic-zero invariant-chain argument establishes rational homology of the actual geometric orbit spaces. No infinite-parameter inference is made; ordinary code/interpreter correctness remains an assumption.

## Originality (PASS, with defined residual risk)

The closest exact calculation, *Integral Rips homotopy of the quaternary Hamming three-cube* (published research record 2026-10-25), proves the nonequivariant \(405\)-sphere decomposition and does not compute the \(C_4^3\) translation character. That fact is explicitly credited rather than claimed again. *Complete ternary translation character of the radius-two Hamming Rips complex* proves an analogous character for the **three-letter** cube and a different group \(C_3^3\), so its character formula cannot determine the order-two/ order-four split of the quaternary translation action. Galetto–Montaño–Wellner (arXiv:2606.20784) treat the **binary** Hamming cube and hyperoctahedral symmetries. Antolín Camarena–Carnero Bravo (arXiv:2307.12401) give nonequivariant categorical-product results and a three-factor conjecture; they do not imply a quaternary translation module. Actual published-record semantic queries also checked equivalent wording, quotient statements, representation decomposition, and stronger group coverage. The main unresolved risk is unindexed or implicit work giving the same quaternary character; no independent priority certification is asserted.

## Mathematical value (PASS)

In a composite alphabet, translation cycle order affects the homology trace beyond support size: among translations supported in two coordinates, the double half-turn has trace \(45\) but those involving an order-four shift have trace \(-3\). The complete sixty-four-character decomposition is therefore not a restatement of the known wedge count, and the ranks \(9\) and \(71\) of two rational quotient homologies are additional invariants. The fixed natural object and full translation representation are motivated by recent equivariant Hamming-Rips research. This settles a coherent, finite, non-arbitrary classification without claiming a general alphabet-size theorem.

## Boundaries and comparison

The assertion does not classify the integral representation, full wreath-product action, quotient torsion, or equivariant homotopy. Source inspection covers the closest exact public quaternary record and relevant ternary translation record, along with the binary group-action preprint and categorical-product results. Bibliographic discovery is not a proof of absolute priority. The mathematical checks here are the supplied exact proofs and executable calculations, not independent validation.

Self-review: passed. Independent audit: not yet performed.
