# Independent mathematical audit

## correctness

PASS

For epsilon-free transition-bipartite unary NFA, any repeated-state subrun has even length; deleting it preserves acceptance and the parity of a run. The first word in each accepted parity therefore has a simple run. Shortest accepted length tn gives at least tn+1 states, and when n is odd the first opposite-parity accepted length (t+1)n requires at least (t+1)n+1 states. The explicit even-n path with return cycle n and odd-n path with return cycle 2n recognize exactly the requested length progressions in transition-bipartite cactus graphs, with all n>=2,t>=1 boundary cases including n=2. Independently reconstructed witness transitions at n=3,4 and verified the general path/cycle argument from actual RESULT.md and checker.py; finite checker ranges cannot be proofs.

## originality

FAIL

The October 25, 2026 published theorem for all unary residue-delay languages has identical optimization hypotheses and strictly broader parameters. Its exact formula specializes algebraically to every submitted claimed optimum. Submitted formula, extra-cost parity law, construction and lower-bound implication are already covered; this is decisive prior mathematical coverage, not an unsuccessful novelty search.

## value

FAIL

A delayed-modular unary family is natural and sharp state complexity would be worthwhile, but all exact bounds and witnesses in the submitted claim are a direct subfamily of the earlier all-residue-delay classification. The package supplies no unproved special boundary, tighter bound or new independent structural conclusion beyond that theorem. Correctness and independent rechecking of a known special case are not independent scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
