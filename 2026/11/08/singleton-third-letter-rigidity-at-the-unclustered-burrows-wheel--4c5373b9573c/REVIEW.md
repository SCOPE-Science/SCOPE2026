# Scientific review: balanced-singleton BWT rigidity

## Correctness

**PASS.** The statement quantifies over all integers \(m\ge2\), not a finite range. The proof directly classifies every fixed-point-free stable permutation at content \((m,m,1)\), based on a zero-first fixed point, a final-two fixed point, and the occurrence-count fixed-point criterion for a letter \(1\). Deleting the sole \(2\) produces a binary word with at most one equal pair; endpoint and letter-content arguments leave exactly \(A_m\) and \(B_m\). Their exact Hamming distances eliminate \(B_m\) and every odd \(m\). The modular conjugacy is valid over any odd modulus and splices zero into exactly one multiplication orbit, so one-cycle sharpness forces the modulus prime and \(2\) primitive. The finite checker independently tests cases through \(m=100\) and exhaustive small classes, but does not replace the symbolic proof.

## Originality

**PASS, with residual priority uncertainty.** The closest source, Kumallagov arXiv:2606.01267v1, proves the forward prime-root construction and asks for sharpness by Parikh vector; it does not give the necessity, unique image, or exactly two fixed-point-free candidates at content \((m,m,1)\). Fici–Gabory–Romana–Sciortino arXiv:2508.20879v1 proves unrestricted ternary existence and periodic alternating primitive-root conditions, but not this fixed-content extremal classification. Accessible previously computed bounded-length spectra count optimal images without supplying a uniform classification at this specific content. Searches for BWT fixed-content uniqueness, the singleton insertion pattern, the arithmetic equivalence, and nearby transformations found no implication covering the theorem. A differently phrased consequence of older permutation literature remains a realistic but unconfirmed risk.

## Value

**PASS.** This is a complete infinite-family solution of a natural fixed-content subclass of the explicitly stated Parikh-vector problem, including existence, nonexistence, uniqueness and the arithmetic obstruction. It explains why a ternary alphabet does not remove Artin-type arithmetic restrictions when one symbol is present only once, despite unrestricted ternary existence at every length. It is not merely a finite table extension or the sufficient construction already known.

## Closest sources and limitations

The proof uses standard stable BWT facts already in arXiv:2606.01267v1 and arXiv:2508.20879v1, but derives its fixed-point-free classification and reverse arithmetic implication independently. No general classification for arbitrary content or unconditional infinitude of the required primes is claimed. Publication-priority confirmation and independent mathematical validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
