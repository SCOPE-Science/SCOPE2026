# Independent mathematical audit

## correctness

PASS

The claim is mathematically correct. A cyclic word gives balanced vertex incidence on the triple graph. For each uniform triple aaa there are three incident nonpalindromic reversal pairs and the selected incidence is even, so at most two selected edges meet it. In the potential certificate, the adjacency-equality masks 000, 010, 110/011, 101 and 100/001 partition the nonpalindromic words; mask 010 excludes equal outer letters. Substitution gives the five claimed local inequality values (1,1,1,2,1) and counts (108,24,24,12,72). Reversal exclusion bounds the lambda contribution by 90, uniform triples bound the charge by 16, and balance cancels the potential. The explicit 106-symbol cycle attains the bound. An independent replay (`python3 /workspace/audit-evidence/replay.py 5`) checked all 256 local words and all cyclic witness windows, including wraparound, with no collision or palindrome; distinct windows force a fundamental period of 106. The scope's edge characterization should not be read as a converse for arbitrary disconnected balanced edge sets: a single Eulerian tour additionally needs connectivity on the support. Only the forward implication is used.

## originality

FAIL

The exact frozen finding M_4(4)=106 is explicitly covered by a distinct indexed result with the same cyclicity, order, alphabet and reversal conditions. Its optimization proof differs from the frozen solver-independent proof. The catalog dating does not decide discovery priority, dependence, or authorship; the failure is exact claim-level overlap, not an accusation or a correctness failure.

## value

FAIL

The even-alphabet order-four gap is explicitly motivated, and the solver-independent extremal argument is useful. But the frozen Finding is the narrow exact value 106, directly covered by a distinct indexed record. A different certificate is not a new exact invariant. No separate structural theorem beyond that value is asserted or audited as a surviving claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
