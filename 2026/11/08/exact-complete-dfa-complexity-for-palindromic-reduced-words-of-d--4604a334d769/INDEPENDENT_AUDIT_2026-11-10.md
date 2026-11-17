# Independent mathematical audit

## correctness

PASS

PASS: Coxeter length in a direct product is additive in factor projections. If a literal palindrome draws letters outside its central factor, one projection is a nonempty even palindrome and has equal adjacent middle letters, hence is nonreduced. Therefore the language is exactly the union of odd alternating single-factor words, bounded by M_i for finite factors. A total DFA has one start and one rejecting sink, four orientation/parity continuation states per infinite factor, 2(M_i−1) proper-prefix states per finite factor and one shared finite terminal accepting state. Myhill–Nerode distinguishes all remaining right contexts by maximum accepted suffix length, next generator, parity, and factor alphabet, giving matching lower bound. Fresh independent residual-state calculations corroborated seven finite parameter configurations and the six-state infinite dihedral case. Infinite/all-parameter proof is not inferred from finite tests.

## originality

PASS

PASS, qualified: Bapat 2026 proves regularity and a direct-product language union lemma, and depicts a four-state automaton for the infinite rank-two case, but the diagram as displayed accepts the nonreduced word stt; a complete six-state minimal recognizer is required. The relevant published material does not state a sharp complete Myhill–Nerode complexity for all finite/infinite rank-two factors with a shared finite terminal quotient. Biagioli–Hohlweg–Sasso concerns reflection-related prefix automata, a different language and complexity. Same-object literature risk recorded.

## value

PASS

PASS: Exact deterministic state complexity is a natural invariant of a regular Coxeter reduced-word language; the formula captures a nontrivial parity jump at even/odd finite exponents, four-state marginal cost of each infinite factor, and cross-factor terminal-state sharing. It corrects a misleading minimality interpretation of an existing displayed recognizer and gives a complete family classification rather than a routine renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
