# Independent mathematical audit

## correctness

PASS

In the stated axiom-only syntax with distinct conjunction and implication constructors, necessity follows immediately by reading the boxed-operand bits from the world’s generated set. For sufficiency let H be the set of true bits in the subformula-closed support S containing top, and P the closure of H under conjunction formation alone if C is present (P=H otherwise). P∩S=H by induction on conjunction formation: the operands of a conjunction in S are in S, and the finite C implications suffice. If M is present, any conjunction in P either came from H, where its parts are in H by the finite M constraints, or was constructed from parts in P. Any implication in P was already in H; if its antecedent is in P, it is in S and hence in H, so K supplies its consequent in H. N is already satisfied in H when selected. Thus P is globally closed under all selected rules and realizes exactly the guessed bits in S. Ordinary Boolean evaluation at a one-world model gives the witness; there are linearly many guessed bits and polynomial-time checks. Modal-free SAT and TAUT give the matching lower bounds, since all propositional assignments extend to suitable one-world models. This confirms the unrestricted proof, with ordinary faithful abbreviations read via the corresponding syntax, not arbitrary rewrites inside boxes. The frozen checker uses separate syntax constructors and 1,568 bounded comparisons; it was inspected, not executed, and the finite checks are not a proof.

## originality

FAIL

Nishimura’s Corollary 3.14 already gives linear-size one-point candidate descriptions and explicitly states the same finite subformula restriction for closure membership. The stages of Definition 3.7 are just monotone forward chaining of the four Horn rules over those formulas. Counting additions per stage rather than accepting the paper’s loose primitive-recursive bound makes the NP/coNP classification immediate. The complexity labels are sharper than the published labels, but the candidate space and the load-bearing finite-support algorithm are already in the proof for exactly the same sixteen logics.

## value

FAIL

Optimal formula complexity is a legitimate question. Here the gap between primitive recursiveness and coNP closes by counting stages in the same previously published subformula computation and guessing one of its already published linear-size candidates. The Horn presentation is a convenient reformulation, not an independently useful new decision algorithm or structural lemma beyond that computation. No substantive remainder warrants a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
