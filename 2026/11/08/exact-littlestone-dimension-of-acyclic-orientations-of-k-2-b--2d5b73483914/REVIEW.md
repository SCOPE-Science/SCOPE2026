# Scientific review

**Correctness — PASS.** The forbidden-opposite-column description follows from the fact that every simple cycle in \(K_{2,b}\) is a four-cycle. The conditional-state recursion enumerates every possible first query and its two answer families, using a separately proved rank for the independent fixed-sign products. A complete induction solves the recursion for all nonnegative parameters and gives \(\operatorname{Ldim}=\lceil3b/2\rceil\). Exhaustive finite checks through seven columns independently agree with the formula; the infinite assertion rests on the induction, not enumeration.

**Originality — PASS (within accessible literature).** The 2013 forest-shattering theorem proves only the known VC term. The 2014 lonesum-matrix identification and \(2\cdot3^b-2^b\) count, and the 2018 complete-multipartite enumeration recurrence, do not derive the exact adaptive rank: the count bound is not sharp already at four columns. Searches using both graph-orientation and lonesum/Ferrers-matrix formulations found no equivalent conditional-state formula. Residual priority risk remains for terminology not surfaced by these searches.

**Value — PASS.** This gives a precise all-parameter separation between static and online shattering on a natural, labelled, bounded-treewidth graph family, rather than an arbitrary finite example. The full residual-rank theorem explains the mechanism and yields a constant-time rank evaluation after arbitrary consistent partial edge answers, beyond a numerical evaluation of a known enumeration.

The closest published sources are Kozma–Moran (2013), Cameron et al. (2014), and Blagoev (2018); see `RESULT.md` for mathematical implications, exact scope, and references. A plausible but unlocated earlier result in alternate learning terminology remains a scientific priority risk, not a proof gap.

Self-review: passed. Independent audit: not yet performed.
