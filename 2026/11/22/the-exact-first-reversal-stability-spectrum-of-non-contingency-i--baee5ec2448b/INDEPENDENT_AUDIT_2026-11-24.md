# Independent mathematical audit

## correctness

PASS

For a singleton {s}, a successor v with false Δp must beat s and have outdegree at least two. At a failure root x, one has s≠x (the tournament has no opposite arcs) and x cannot beat s, since then Δp at x would force outdegree one. Thus s→x→v→s; the only cycles are j→i→k→j with i<k<j. For j<n, the later vertex j+1 supplies a successor with true Δp in each of the three cyclic roles. The distinct (s,x) pairs are (j,i), (i,k), (k,j), totaling 1+2(j−i−1) when the gap is at least two. For j=n, outdegree one at n rules out two roles, leaving (n,i), which fails exactly if x=i has both n−2 and n−1 as successors: the first beats n and n−1, the second beats only n. For all valuations the adjacent flips remain transitive, and in the terminal triangle each member has one successor while at earlier roots every successor's successor set is contained in the root's. This includes n=3 and gives n preserving labelled choices. The frozen VERIFICATION.md and check.py were inspected; a separate adjacency-set implementation agreed on all 119 reversals and 868 singleton assignments through n=9 and on validity over 11,256 Boolean assignments through n=8. That replay is bounded; the triangle proof covers arbitrary n. No Lean verification or specialist attestation is inferred.

## originality

PASS

Credit the established semantics and transitive-frame 4Kw sufficiency. The supported contribution is the exact perturbation classification including the sole nontransitive preserving flip and the position-sensitive count of singleton valuation–world failures. The closest distinct edge-stability finding is for undirected edge edits, which do not model arc reversal: the undirected skeleton of every tournament in this family is unchanged. No equivalent or stronger coverage was established in the inspected statements.

## value

PASS

A single changed arc is the first natural stability layer of transitivity. The lone cyclic preservation case separates modal validity from transitivity in that layer, and the exact singleton witness-pair profile distinguishes interior and terminal disruptions quantitatively. This is a reusable exact benchmark for tournament frame perturbations, not a claim about all tournaments or all countervaluations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
