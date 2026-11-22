# Review of cyclic power-GCD prime-square Smith factors

## Correctness — PASS

The claim is precisely restricted to every odd prime \(p\) and every integer \(a\ge1\). Its matrix identity \(G=uI+v(I_p\otimes J_p)+J\) is verified entrywise for all three gcd classes. For primes \(\ell\ne p\), \(p\)-unit averaging gives a genuine integral local direct-sum decomposition. At \(\ell=p\), a \(p\)-by-\(p\) unit pivot and Schur complement isolate the exact valuation multiplicities. The rational determinant then forces the last \(p\) valuations to be precisely \(a+1\), rather than merely bounded below. Coprimalities with the final scalar eigenvalue and consecutive divisibility identify the global ordered Smith factors. These steps establish an infinite proof independent of the included exact finite checker; the checker reproduced 4,499 grouped assertions across seven test cases.

## Originality — PASS, qualified

The closest earlier arithmetic matrix works, Haukkanen–Korkee (2005) and Hong (2008), study gcds of *entries* in a positive-integer indexing set and matrix divisibility, not the cyclic difference gcd kernel and its integral Smith factors. Telloni–Williams (2014) gives polynomial-matrix Smith forms for a special circulant class, whereas the theorem concerns fixed integer matrices for all odd \(p\) and \(a\). Noferini–Williams (2019) offers general circulant companion-ring reductions, not these closed entries. Nearby arithmetic-circulant results and a largest-factor calculation for the unpowered cyclic gcd matrix do not imply its complete list at every exponent. Exact-claim, equivalence, and broader-coverage searches did not identify a covering result. This is a best-knowledge mathematical novelty assessment, not a proof of priority; general algorithms might yield an implicit specialization.

## Mathematical value — PASS

Cyclic gcd kernels are natural arithmetic convolution matrices, and their full integral cokernel determines all integer obstructions to solving the corresponding convolution equations. The theorem determines every invariant factor over a two-parameter infinite family; its special \(p\)-primary structure and prime-to-\(p\) factors cannot be read from the elementary rational eigenspectrum alone. This is a complete classification at the first nonsquarefree prime-power group order, rather than a routine single determinant or isolated computed example.

## Closest literature and limitations

Relevant primary sources: Haukkanen–Korkee (2005), DOI 10.1155/IJMMS.2005.925 (publisher PDF text, Sections 1–3, inspected); Hong (2008), DOI 10.1016/j.laa.2007.08.037 (abstract examined, full text unavailable); Telloni–Williams (2014), DOI 10.1016/j.laa.2014.06.032 (open preprint, Sections 1–4 and theorem framework inspected); Noferini–Williams (2019), arXiv:1908.07331 (introduction, Theorem A, and related companion-ring formulation examined). The prime \(2\), higher prime-power cyclic orders, and incomplete index sets are not claimed. The possibility of implicit coverage by a general Smith-form specialization remains a genuine residual originality risk. No independent audit was carried out.

Self-review: passed. Independent audit: not yet performed.
