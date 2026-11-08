# Scientific review: exact state complexity of shifted generalized period-doubling words

## Correctness (C): PASS

The proof identifies \(P_m(n)=\nu_2(n+1)\bmod m\) from the defining substitution. Every residual after \(e\) least-significant input bits is either constant or \(G_{\lceil(c+1)/2^e\rceil,e\bmod m}\); precisely one low-digit residue at each depth yields a nonconstant function. The \(\lceil\log_2(c+1)\rceil\) distinct descending offsets, \(m\) phase states and \(m\) constants are all reachable. Functions with distinct offsets are separated by inputs \(2^H-q\) of varying \(H\bmod m\), and all other states are also distinguished. These observations constitute a complete proof of both a minimal DFAO and the binary \(2\)-kernel cardinality. Direct standard-library tests checked 2048 machines, including Moore partition refinement, 163840 numerical outputs, padded input and eight independent 8192-letter substitution prefixes. The tests corroborate rather than prove the infinite quantifiers.

## Originality (O): PASS, subject to residual historical priority risk

Bognini–Ammar (arXiv:2511.20881v1) studies the **same** generalized period-doubling substitution but focuses on factorization through kernel words and gaps. Moradi–Popoli–Shallit–Vukusic (arXiv:2603.18858v1) studies automata of **Fibonacci** shifts in Zeckendorf representation; its exact Fibonacci-specific LSD theorem (Theorem 3.2) and its general binary-input transducer upper bound do not imply a sharp count for this different valuation-based word. Charlier–Cisternino–Massuir studies translating the **Thue–Morse set**, not this valuation-period-doubling sequence. Comparisons by 2-kernel alias, valuation formula, shift parameter and stronger possible bounds did not reveal the present exact statement. Other accessible period-doubling results concern attractors, word factors or dynamical lifts. Published-index and prior-claim searches cannot demonstrate uniqueness; historical priority must be independently checked if publication is contemplated.

## Value (V): PASS

For all nonnegative shifts and every finite alphabet size, the theorem determines a natural exact invariant: the minimum size of an automaton producing a shifted canonical automatic word, equivalent to its entire binary-kernel cardinality. The answer is a sharp bit-length law with explicit optimal transition structure. It is substantially more informative than the known general upper bound or isolated computational examples, and directly extends the subject of contemporary state-complexity-under-shifts research.

## Limits

The theorem is limited to base-two least-significant-digit-first representations with arbitrary zero padding; neither most-significant-digit-first complexity nor a different base is included. The code performs finite corroboration, not infinite or independent validation. Historical originality is assessed against accessible literature and may require additional external expertise.

Self-review: passed. Independent audit: not yet performed.
