# Review of the cyclic Rule 18 inverse-fiber formula

**Correctness — PASS.** A maximal run of at least two zeros creates exactly two one-sites, and no other one-sites occur. The two noncrossing adjacent pairings of marked output sites exhaust all possible parents; an intervening gap of length \(g\ge1\) has exactly \(F_g\) fillings with endpoints one and no adjacent zeros, while length-zero gaps are impossible. This proves the identity without computation. The zero-output Lucas count and strict \(\varphi\)-bound cover all \(n\ge1\). Separate direct enumeration and a transfer-matrix implementation agree with the theorem; they do not constitute an infinite proof.

**Originality — PASS, with historical-priority risk.** The May 8, 2007 paper by Shreim and colleagues already reports the zero hub of Rule 18 numerically and the general de Bruijn trace formula. Jen (1989) gives broader unrestricted-boundary preimage recurrences and Fibonacci-type block formulas. The novel content assessed is not those methods or the already-observed hub, but the explicit *all-output indexed cyclic* two-alternating-Fibonacci-product identity, its exact reachability criterion, and its all-length strict comparison. The inspected passages and targeted scholarly searches did not locate this complete statement; a general transfer algorithm can be specialized to recover it, and unlocated sources remain possible.

**Value — PASS.** This solves the entire one-step inverse-fiber problem by a short formula in the observed zero gaps, rather than recomputing a matrix product for each output. The even-parity and alternating-gap test gives a sharp global image characterization, while the strict maximum supplies a proven inverse-degree extremizer in a standard non-linear elementary automaton. These are structural reconstruction facts for arbitrary ring lengths, not an arbitrary small table.

**Limits.** Only one synchronous Rule 18 update on labeled finite cycles is considered. Historical priority has not been independently audited. Direct enumeration is finite corroboration.

Self-review: passed. Independent audit: not yet performed.
