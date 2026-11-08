# Scientific review: periodic antisquare-good binary sequences

## Correctness

**PASS.** The claim is for every labeled period \(n\ge1\), counting words of any minimal period dividing \(n\). The source paper's Proposition 18 excludes heteroclinic exceptional factors from periodic good sequences, and its minimal-antisquare theorem identifies a finite forbidden-factor test. Cyclic change codes have zero runs of length at least two and one runs of length exactly two or four; the number of one symbols is even, so each cyclic code has exactly two binary lifts. Marking one of the \(m\) cyclic run-pair boundaries yields \(2n[z^n]A(z)^m/m\), with the two constant sequences handled separately. The formal logarithmic sum gives exactly \((1-z-z^4-z^6)^{-2}\). An independently constructed 32-state transfer matrix has matching exact characteristic polynomial, and direct finite tests agree. The proof does not conflate counts of marked words with counts of primitive rotation orbits.

## Originality

**PASS, qualified by bibliographic uncertainty.** The underlying finite forbidden-factor description, Pansiot coding, and supergolden growth rate are existing results of Baranwal et al., not claimed here. Their theorem concerns ordinary finite good-word growth and gives no complete periodic-point or primitive-orbit distribution. The new argument counts cyclic cuts with multiplicity, retains both constant configurations, establishes the exact square zeta function, and inverts fixed-point counts to all primitive orbit counts. OEIS A307732 concerns linear finite words rather than cyclically admissible configurations. Targeted searches for periodic good words, circular antisquare avoidance, Pansiot-code orbit counts and the exact denominator did not reveal a dominating prior formula. An unpublished or differently indexed equivalent remains possible.

## Mathematical value

**PASS.** The question is natural because the asymptotic size of the language and its forbidden-factor/renewal descriptions were known, while the closed orbit structure was not determined by the linear enumeration. The exact zeta function and Möbius formula give a complete infinite periodic-orbit census of a nontrivial finite-type symbolic system, distinguishing primitive necklaces from marked periodic words. The perfect-square factorization and the same supergolden spectral scale yield structural information independent of a finite sample.

## Sources and limitations

Primary full-text inspection: Baranwal et al., *Antisquares and Critical Exponents*, arXiv:2209.09223, Section 6 and the entirety of relevant Section 7 (including Proposition 18 and Theorem 19), https://arxiv.org/pdf/2209.09223. Database comparison: OEIS A307732, https://oeis.org/A307732. The proof is conditional on the published minimal-antisquare classification and exceptional-sequence proposition, both quoted precisely. The distribution says nothing about aperiodic orbit classification. Bibliographic novelty is qualified; independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
