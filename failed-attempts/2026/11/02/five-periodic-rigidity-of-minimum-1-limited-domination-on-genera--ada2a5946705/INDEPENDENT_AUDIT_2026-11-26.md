# Independent mathematical audit

## correctness

PASS

Since n>=5 gives a simple cubic graph, the local inequalities sum to 3|D|>=2n+|D|, and either full layer attains |D|=n. Equality makes every local inequality exact and is equivalent to exactly one crossing edge per vertex. In spins this gives v_i=u_i-u_{i-1}-u_{i+1} and v_{i-2}+v_{i+2}+u_i=v_i. Eliminating v leaves u_{i+3}-u_{i+2}=u_{i-2}-u_{i-3}; therefore the differences repeat after five. The sum of five consecutive differences is a constant increment for u, and summing all cyclic shifts proves it is zero. If 5 does not divide n, u must be constant; otherwise the requirement v_i=±1 excludes precisely the singleton cyclic runs in the five-letter word. A nonconstant permitted word therefore has a run of length two and one of length three, producing exactly ten nonconstant labelled words and two constant ones. Conversely these five-periodic patterns satisfy both spin equations, and the one-cross-edge condition forces equally many plus and minus vertices. This argument uses cyclic identities and remains valid at n=5,6. Independent replay `python3 /workspace/branches/independent_checks.py 2` exhausts the allowed choices of the outer layer and derives the spoke assignments directly from crossing counts for n=5..15, giving 12 exactly at 5,10,15 and 2 elsewhere. The infinite classification is algebraic; the frozen verifier was read, not run.

## originality

FAIL

A distinct Resultary record, 07ff361ad99e, covers the complete proposed finding via a bijective reformulation: it gives precisely the same two-or-twelve labelled colorings and exactly the same five-periodic nonlayer patterns for all n>=5. The frozen finding contributes no further classification beyond that covered statement. The companion uses a finite-state proof and the frozen one a short spin elimination, so this is coverage of the theorem, not a claim of identical proofs, historical priority, or copying. The records have the same displayed date; their relative priority is unresolved. The fail is based on demonstrated equivalent coverage, not lack of access to a paper.

## value

PASS

The structural period-five family classification is worthwhile in itself, and this proof explains the period directly via a cyclic linear recurrence rather than just rechecking small graphs or restating the count. That explanatory value does not make the exact census a distinct finding relative to the matching-cut record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
