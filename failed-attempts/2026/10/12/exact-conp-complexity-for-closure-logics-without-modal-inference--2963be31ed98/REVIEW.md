# Independent mathematical audit

## correctness

PASS

The exact result follows from the already published canonical one-point model construction: for input phi its candidate finite generator G(Delta) is a subset of the source Sub*(neg phi), polynomial in syntax length. Membership in cl_Lambda(G) for a queried box subformula can be decided by saturation restricted to the subformulas of G union {psi,top}, as Nishimura explicitly states in Corollary 3.14; this finite set has polynomial cardinality, and each monotone rule M/C/N/K adds each relevant formula only once, so O(poly(|phi|)) rounds/checks. Thus a guessed one-point model verifies SAT in polynomial time. Classical SAT and tautology embed as box-free fragments; negation transfers SAT to invalidity and strong completeness to derivability. Unrestricted C-closure can be infinite but is never claimed finite. All 16 systems and both modal-free lower bounds are covered. Correctness does NOT make this corollary original.

## originality

FAIL

FAILED originality by decisive prior implication: Nishimura arXiv:2610.01433, Corollaries 3.13-3.14, already supply the polynomial-size one-point candidate family and EXACT closure membership restricted to subformulas of G(Delta) union {psi,top}. Counting at most |R| insertions and selecting a nondeterministic candidate yields NP membership immediately; ordinary propositional NP-hardness then gives exact NP/coNP completeness. Rebranding the same restricted saturation as a polynomial relevance lemma does not avoid prior coverage by the stronger full construction, irrespective of original source calling general computational complexity an open problem.

## value

FAIL

FAILED independent value: the exact complexity labels are correct but adding elementary polynomial bookkeeping and the textbook SAT/TAUT identity reductions to the already published concrete finite-subformula model-checking procedure is a routine consequence, not a new substantive boundary proof. Contrasts with congruential nonnormal cube do not rescue the already implied classification; no distinct nonstandard lemma remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
