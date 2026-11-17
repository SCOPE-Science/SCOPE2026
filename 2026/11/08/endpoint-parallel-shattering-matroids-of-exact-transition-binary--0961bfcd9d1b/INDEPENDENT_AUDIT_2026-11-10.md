# Independent mathematical audit

## correctness

PASS

For a queried support S={i_1<...<i_s} without both endpoints, every prescribed coordinate labeling gives interior switch totals of fixed parity in each gap; at least one exterior edge makes the attainable totals the entire integer interval [d,M]. Alternating queried labels force k>=s-1 and gap-parity-opposite labels force k<=n-s. The endpoint XOR equals k mod 2, forbidding the pair {1,n}. Singletons by complement symmetry and empty support settle boundaries. Partition matroid truncation gives all coefficients; the online upper bound follows from 2*C(n-1,k) hypotheses and independent threshold blocks give k floor(log2 floor((n-1)/k)) lower bound. A separate direct exhaustive computation verified 8,192 supports through n=9, but not infinite n.

## originality

PASS

Candidate novelty is the exact coordinate support criterion and matroid face polynomial for a constrained *class* of exactly k switches; online threshold-tree construction is deliberately acknowledged prior technique. Johnson 2101.06490 addresses shifts/substrings of one word, and general Ghazi et al closure bounds do not imply this support characterization. No dominating published Resultary result was identified by semantic query; unindexed sign-change hypotheses could still cover it.

## value

PASS

The complete shattering complex rather than only VC dimension is a natural structural invariant of a fixed-switch combinatorial concept class. Its rank-truncated parallel-endpoint matroid and support polynomial determine all allowable query positions, and the same model exhibits genuine adaptive/static separation at fixed k. A mathematical classification, not mere program output.

The dated certificate retains the supplied scientific assessment, sources and limitations.
