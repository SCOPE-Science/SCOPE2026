# Independent mathematical audit

## correctness

PASS

P1–P4 force the top row, absorption by intersection with the antecedent, and monotonicity. P5 after absorption is exactly the displayed constraint for d ⊆ a; self-coherence rules out a doubleton's other atom in a singleton column unless the value is top. Thus all constraints between distinct nontrivial rows run from singleton rows to doubleton rows. P5 at c=0 and consequent monotonicity give antitonicity of N, and double-negation inflation plus antitonicity is equivalent to self-adjointness. Testing against singletons then yields the common-neighbor polarity of a loop-free undirected graph. The smaller carriers have forced top and bottom rows (including the single-element carrier if allowed); on the two-atom carrier only singleton rows remain. Independent replay: `python3 /workspace/reproduce_reviews.py 2` enumerated 512000 candidate full tables at three atoms after P1–P4, identity and semicomplementation, applied P5 to complete tables, and obtained 7820 T and 1021 F. It matched all sixteen orbit-size and projected-row triples and F fibers 729, 81, 16, 1 with multiplicities 1, 3, 3, 1; the smaller carriers give (T,F)=(1,1),(1,1),(4,2) for zero to two atoms with distinct negations in each class. The frozen verifier was inspected, not executed.

## originality

FAIL

Earlier public findings state the exact F census, F fibers, and first-carrier result; the earlier census's public, exhaustive verifier also gives the exact T census for the identical axioms. The T count need not be the earlier headline to be existing exact coverage. The current directed orbit table is an alternate finite evaluation of those constraints, not a surviving census theorem.

## value

FAIL

The finite boundary and the distinction between unary and binary counts are worthwhile in themselves, but these exact facts were already available. The alternate grouping of the known total into directed graph orbits is a transparent re-expression of the same small row census with no separately motivated mathematical use in the frozen contribution. No distinct valuable remainder has been established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
