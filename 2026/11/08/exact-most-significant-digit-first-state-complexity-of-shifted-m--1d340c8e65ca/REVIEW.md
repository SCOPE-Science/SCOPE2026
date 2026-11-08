# Scientific review: shifted modular ruler state complexity

## Correctness — PASS

The right-context equivalence follows from the exact identity
\[
b^\ell n+r+d=b^\ell\bigl(n+\lceil d/b^\ell\rceil\bigr)
\]
for the unique suffix residue \(r\equiv-d\pmod{b^\ell}\). When the suffix is not exceptional, its valuation is independent of the prefix. Testing every exceptional suffix of length at most \(K\) shows that the complete vector of \(K+1\) shifted valuations is necessary and sufficient to describe all continuations. The radix trie partitions every integer prefix into a missing-child case or exactly one marked leaf. The former fixes every coordinate; in the latter only one valuation coordinate varies, and arbitrary residues are attained by explicit powers of \(b\). This establishes both inclusions in the exact formula and minimality via distinguishable right contexts. The composite-radix valuation comparisons use differing divisibility depths, not multiplicativity of an integer prime valuation. A standalone checker independently minimized 896 reachable output automata and performed 12,136 signature-witness checks plus 107,520 arithmetic evaluations. Finite tests are supplementary; the universal proof is the right-context and trie argument.

## Originality — PASS, subject to priority limitations

The closest shift-complexity source, Moradi–Rampersad–Shallit (arXiv:2512.10017; initial release 2025-12-10), develops automatic-sequence shifts and a two-tape addition relation, but its inspected Sections 3–4 do not state the exact MSD-first modular-valuation trie formula. Moradi–Popoli–Shallit–Vukusic (arXiv:2603.18858; initial release 2026-03-19) concerns Fibonacci-word shifts in Zeckendorf notation, not the present valuation-residue sequence. Kosoy (arXiv:2607.17369; initial release 2026-07-19) considers digit-direction complexity and learning but not this explicit shifted-ruler enumeration. The relevant previously recovered specialization for LSD-first valuation automata does not imply the new MSD-first formula: reversing input digits changes the Myhill–Nerode residuals, and the binary case \(m=2,c=10\) has distinct minima 8 versus 9. General constructive minimization procedures may derive the count algorithmically, but they do not explicitly state this parameterized closed finite arithmetic formula. Historical priority is not independently certified; an unindexed earlier specialization remains possible.

## Value — PASS

The object is a natural automatic sequence (the modular ruler function under translation), and the invariant is the exact number of states of its minimal MSD-first DFAO. The opposite digit direction is known to have markedly different behavior; therefore merely transferring an LSD result is not legitimate. A finite trie of at most logarithmic depth produces the exact size for every radix, modulus and shift, supplies all reachable right-context signatures and yields a quadratic-logarithmic uniform upper bound for fixed radix and modulus. This is a meaningful all-parameter structural classification, though it does not prove that the upper bound is asymptotically optimal.

## Limits and closest literature

The construction treats end-output deterministic automata with arbitrary leading-zero padding and valuation of positive integers, not arbitrary integer-valued ruler sequences. The finite signature count is not simplified into a uniform elementary expression. Relevant primary texts are arXiv:2512.10017, arXiv:2603.18858, and arXiv:2607.17369. Further specialist historical examination and independent proof review remain needed.

Self-review: passed. Independent audit: not yet performed.
