# Scientific assessment

## Correctness — PASS
The proof is self-contained beyond standard Perron–Frobenius theory. The accepted digit language is exactly \(1(1\mid0^r)^*\), the lexicographically minimal carry produces the exact next accepted integer, and the subtracted suffix values give the explicit gap formula. The unique last zero block yields exact shell multiplicities \(T_r(n-r-t-1)\). The primitive length-\(1\)/length-\(r\) tiling recurrence yields positive dominant root \(\lambda_r\); a bounded prefix-subtree decomposition extends frequency convergence from complete shells to all thresholds. Explicitly checking the wraparound in the modular exponent shows that the only duplicated gap is \(H_r(0)=H_r(1)\). These are mathematical arguments, not inference from finite tests.

## Originality — PASS, qualified
Merta (2018) defines the word family and proves unbounded zero blocks, two-one maxima, parity properties and nonregularity of the index sequence, but does not establish the present exact gap spectrum, finite shell multiplicities or frequency distribution. His Theorem 5.10 concerns differences of a *formal-inverse* coefficient-position sequence rather than consecutive one-positions of the original word. Allouche–Yao (2024) treat opacity complexity, and the full inspected OEIS A060142 entry lists the indices of the ordinary word without the claimed all-order distribution. Mathematical database queries under variants of gap spectrum, renewal times, consecutive one-positions and Perron distributions did not identify a covering result. These searches are not a proof of global novelty; prior unindexed sources remain possible.

## Mathematical value — PASS
The accepted indices form a sparse automatic family with unbounded zero blocks, so ordinary symbol-density data conceal almost all recurrence structure. An *exact all-order return-gap spectrum* and a nondegenerate probability law, holding for every real cutoff rather than only dyadic shells, provide natural complete classifications and numerical invariants for the full family. The law is not determined by the previously known unboundedness of zero blocks or by the parity of the one-position sequence.

## Boundaries and closest literature
The result concerns successive marked integer positions, not composition inverse positions. It gives relative return-gap distributions and no claim about a density of accepted indices among all integers. Primary sources inspected: Merta, arXiv:1803.00292v1 (Sections 2 and 5, especially Theorems 2.5, 5.1, 5.2, and 5.10); Allouche–Yao, arXiv:2404.13601v1 (Example 9); OEIS A060142 (definition, values, references). An unindexed equivalent remains a bibliographic risk, and no independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
