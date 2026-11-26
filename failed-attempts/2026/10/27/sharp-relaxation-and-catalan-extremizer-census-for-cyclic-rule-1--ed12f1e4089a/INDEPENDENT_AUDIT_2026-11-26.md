# Independent mathematical audit

## correctness

PASS

In the unrolled sparse regime the parallel exclusion rule is P_i(t+1)=min(P_i(t)+1,P_{i+1}(t)−1). Subtracting t+2i yields a sliding minimum of initial B_i=p_i−2i, whose drift over k particles is n−2k≥0. At t=k−1 the appended endpoint cannot lower the old minimum, so every empty-cell gap is at least one. At t=k−2 a zero gap occurs exactly when the added endpoint is strictly below the entire old window; its drop is at most one because B increments are ≥−1. Two such records would force B_(ell+k)<B_(ell')<B_ell for ell<ell'<ell+k, contradicting the drift. In reverse gap order the record condition is that the first q gaps sum to at most q−1. A bijection with Dyck paths writes each gap as that many down-steps followed by one up-step, then appends down-steps until the height is zero; the nonnegative condition just before each up-step is the displayed inequality. The omitted physical gap is set by the hole count and is at least two, so each choice of record particle site and Catalan path gives one distinct labeled input. For k=1 all n sparse states are already relaxed, and at half filling gap separation forces alternation. Complement-reflection commutes with the update and handles the dense bound and census. The source verifier and its recorded run were inspected; the general argument is analytic.

## originality

FAIL

Fukś's earlier local preimage theorem and exact ballot count already imply the fixed-mass sharp bound, labeled Catalan census and unique final blockage, including the stated initial strict gap-record characterization. This is concrete prior implication, not just reuse of a general technique, nor a priority inference from the later catalogue matches. The min-plus proof is an alternate derivation of a mechanically covered claim.

## value

FAIL

Worst-case time and first extremal multiplicity are naturally motivated for synchronous traffic. But the exact invariant here reduces to evaluating the published preimage count at its smallest possible height, together with one additive cyclic prefix argument. The min-plus reformulation reads well as an alternate proof; it does not supply a separate unknown or non-mechanically-implied scientific invariant of the system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
