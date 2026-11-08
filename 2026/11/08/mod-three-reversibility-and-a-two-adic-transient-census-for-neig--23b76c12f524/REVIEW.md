# Review of the ladder neighbor-sum dynamics theorem

## Correctness

**PASS.** The open-neighbor ladder update becomes \((u,v)\mapsto((S+I)u,u+(S+I)v)\) by the invertible row transformation \(u=x+y,v=x\). The one-row open-path adjacency is cyclic, so the root-one multiplicity of its characteristic polynomial determines precisely one path Jordan block. The tridiagonal recurrence and unramified Laurent substitution at a primitive cubic root give the multiplicity \(2^{\nu_2(n+1)+1}\) precisely when \(3\mid n+1\). On the resulting primary component, the change \(z=t+\varepsilon\) in \(\mathbb F_q[t,\varepsilon]/(t^m,\varepsilon^2)\) is valid since \(m\) is a power of two, and proves two equal size-\(m\) blocks. The Fitting decomposition then establishes the stated entrance counts. Neither the matrix experiments nor a dimension count alone serves as the proof. Independent graph constructions corroborate 525 exact kernel-rank checks and 5,456 complete labelled binary trajectories.

## Originality

**PASS, subject to historical-priority risk.** Earlier work on finite linear cellular automata already provides characteristic-polynomial recurrences for the null-boundary path and general algebraic methods for transient/periodic decomposition. This antecedent is explicitly acknowledged rather than repackaged. The full accessible 2006 treatment of Rule 90/Rule 150 (Thomas–Stevens–Lettieri), the 2012 preprint on automatic columns (Rowland–Yassawi), and the inspected introductory material from the 1984 foundational analysis (Martin–Odlyzko–Wolfram) do not state an exact two-row open-ladder Jordan partition or first-entry law. A directly ladder-related 2010 interlace-polynomial article was identified, but only its abstract could be obtained; it discusses graph polynomials and a tridiagonal rank, so an unknown full-text implication is an acknowledged residual risk. Publicly indexed related results concerning dual-number Jordan lifts and other parity graphs were compared by implications rather than title. None of the inspected statements entails the all-length ladder entrance-time formulas as presented.

## Mathematical value

**PASS.** The strip \(P_n\square K_2\) is a standard bounded-width, bounded-degree network on which open-neighbor parity is a natural local rule. Its reversal from an entirely periodic permutation to irreversible dynamics at exactly one residue class modulo three is structurally informative. On the singular lengths, the *entire* transient profile reduces to two equal Jordan chains whose length is governed by a separate two-adic statistic; \(1-q^{-2}\) of configurations attain the sharp maximum irrespective of strip length. This is a complete infinite-family classification of a natural dynamical observable, not a small numerical improvement or a repackaged nullity test. The proof explains the arithmetic interaction of open boundaries and rung coupling.

## Sources and limitations

The dated public preprint anchor is Rowland–Yassawi, arXiv:1209.6008v1 (2012-09-26), which is distinct from a publication/revision date. More directly relevant historical references are Martin–Odlyzko–Wolfram (1984), Thomas–Stevens–Lettieri (2006) and Li–Wu (2010); their exact first online availability is not inferred from journal dates. The full text of Li–Wu could not be accessed despite searches for open copies and an authorized institutional request, and a covering unindexed source cannot be excluded. This review does not claim a complete census of possible periodic orbit lengths.

Self-review: passed. Independent audit: not yet performed.
