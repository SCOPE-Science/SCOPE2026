# Scientific review

## Correctness — PASS

The proof uses the unique factorization of height-two Dyck words into \(B_p=1(10)^{p-1}0\), exhaustively classifies every possible four-letter factor by interior, one-boundary and two-boundary occurrences, and derives ten explicit count identities. These identities recover the feasible tuple \((n,b,c,d,f,g)\) from the full oriented histogram; the endpoint triples recover all smaller-factor counts. Sharp unit-run and long-component feasibility constraints are both necessary and constructively sufficient. Counting the feasible tuples by a sum of four geometric terms yields the stated reduced rational generating function. Its order-four pole at one and primitive-third/fourth-root poles yield cubic growth and exact quasiperiod twelve. Direct exhaustive verification through semilength 17 and a separate series/occurrence calculation through semilength 55 provide finite corroboration, not an infinite proof.

## Originality — PASS (qualified)

Karhumäki–Saarela–Zamboni (arXiv:1301.5104v1, 2013) give the general \(k\)-Abelian equivalence framework and a growth-order theorem for full shift languages, not a sharp joint feasible profile characterization on height-two Dyck paths. Sapounakis–Tasoulas–Tsikouras (2009) and Manes–Sapounakis–Tasoulas–Tsikouras (2011) enumerate particular factor-occurrence statistics in Dyck paths, not the entire simultaneous vector image. Previously recorded all-height three-Abelian Dyck profiles are strictly coarser: \((1,1,2)\) and \((1,3)\) have equal three-Abelian but different four-Abelian observations. Cyclic four-factor reconstructions with forbidden adjacent `11` concern neither the same source nor the same boundary model. Searches for exact height-two four-Abelian profiles and the integer sequence gave no clearly equivalent result. Residual risk: an unindexed prior joint enumeration or a derivation hidden within related enumerations might exist.

## Value — PASS

Height two is the first nontrivial stack-height restriction on Dyck streams: it still contains \(2^{n-1}\) distinct length-\(2n\) sources. The theorem completely characterizes which four-factor histograms occur and proves their sharp error-free code capacity, \(R_n=n^3/18+O(n^2)\), with an exact period-twelve enumerator. In particular an exponential source language collapses to a cubic number of distinguishable local observations. This is a motivated global realizability result, not just a table of small cases, a renaming of a standard recurrence, or a claim of noisy-channel coding performance.

## Closest sources and limits

The inspected primary sources concern general finite-word \(k\)-Abelian equivalence and individual Dyck factor statistics. The classification and construction here concern *joint* oriented factor multiplicities for *height-two* Dyck words. Earlier unpublished or unindexed equivalent work remains possible. The proof does not supply the distribution of all fiber sizes or extend to greater path height.

Self-review: passed. Independent audit: not yet performed.
