# Scientific review of the ternary connected-noncrossing-graph index sum theorem

## Correctness — PASS

The nondivisibility index description is the exact Deutsch–Sagan congruence, proved in the primary literature and independently by Gessel. The digit-sum support inclusion follows by carry monotonicity, and reverse inclusion has explicit constructions for targets of weights zero and one and a unit partition for weights two to four. For the full fiber histogram, each digit transition is derived from integer digit addition, with two carry states and two independent digit weights truncated at two. The provided `fiber_certificate.py` constructs the reachable 18-dimensional integer coefficient vectors and verifies the 18-state transition table and the 18-by-18 identity \(T^2(T-3I)(T-I)^5=0\) using exact integer arithmetic. The histogram polynomials satisfy this same recurrence, including the two exceptional initial depths, and the first eight exact depth comparisons force equality for every depth. The energy formula is the squared-fiber sum. An independent four-input carry computation and direct set enumeration provide cross-checks. No finite sample is passed off as an infinite argument.

## Originality — PASS, with historical-priority qualification

The original Deutsch–Sagan and Eu–Liu–Yeh graph-count congruences, Gessel's complete short proof, and Krattenthaler–Müller's later stronger graph-number congruences address values of graph counts and **individual** index membership, not the cyclic pair-sum representation function of their nondivisibility indices. Green's broader digital additive-energy result is an inequality for arbitrary low-support digital sets and does not determine these exact fibers. Published exact energies for binary digit sets involve different representations and carry systems. Search of the available research-record corpus and accessible prior claims found no statement whose implication directly yields this complete ternary low-weight histogram. Residual risk: a specialized or generalized digital-convolution paper not retrieved could imply this exact formula; originality is a best-knowledge judgment, not a certification of priority. The Eu–Liu–Yeh paper's full text was not accessible; Gessel supplies the needed premise and a fully inspected original proof.

## Mathematical value — PASS

The graph-nondivisibility indices are a classical, arithmetically motivated sparse set with \(|S_r|\) quadratic in the digit length. The result gives a complete all-depth representation function distribution, exact support, a universal sharp fiber bound, and an exact quartic cyclic additive-energy formula. These are genuine additive invariants of the number-theoretic index set that cannot be read directly from the published congruence criterion. The finite-state reduction explains why the distribution has a bounded fiber spectrum and is reusable for related automatic-index convolution problems; the exact prime-power information has mathematical content beyond a finite census.

## Evidence and limits

Primary sources: Deutsch–Sagan, arXiv:math/0407326v1 (2004); Gessel, arXiv:1403.7656v1 (2014). Closest broader comparisons: Krattenthaler–Müller, DOI:10.1007/s00010-025-01195-0 (2025), §5; Green, DOI:10.1112/S0010437X24007723 (2025), Proposition 2.4 and §7. Code checks: `fiber_certificate.py` and `independent_energy_check.py`. All proofs concern modular sums of indices, not sums of graph counts. No external mathematical audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
