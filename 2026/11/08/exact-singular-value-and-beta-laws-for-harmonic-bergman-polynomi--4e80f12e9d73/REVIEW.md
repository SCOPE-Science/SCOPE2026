# Scientific review

## Correctness — PASS

The normalized harmonic monomial basis gives the monomial Toeplitz coefficient by a direct radial integral. Comparing direct degree-\(m\) projection to iteration of the degree-one projection yields a finite crossing block with the exact coefficient \(n(m-n)/((m+1)\sqrt{(n+1)(m-n+1)})\). For a degree-\(d\) polynomial, its reverse-triangular block has nonzero reverse diagonal because \(a_d\ne0\), proving rank exactly \(d-1\) and square-zero. The monomial block is an anti-diagonal weighted permutation, so its singular values are the displayed weights. Their maximum gives the exact norm; uniform convergence away from endpoints and bounded endpoint contributions give weak convergence to the pushforward of uniform \(t\in[0,1]\) by \(\sqrt{t(1-t)}\), with the stated beta moments.

Risk: a finite computation alone would not prove a spectral limit. Here the limit is established analytically and finite diagnostics are supporting checks only.

## Originality — PASS (qualified)

Huang–Wang–Zhao, arXiv:2610.09638, was inspected through its full publicly readable text, especially its §§2–3, Theorem 3.1, and proof: it classifies operator spectrum and finite isolated eigenvalues, not the singular values of the iterated polynomial-calculus defect. Dong–Zhou, arXiv:1411.0213, §§1–5, Theorems 2.2 and 5.1 and Corollary 5.7, already treats finite-rank two-factor semicommutators and ranks; these related components are prior art. Yang–Liu–Lu (2013), DOI:10.1155/2013/578436, concerns different pluriharmonic Bergman Toeplitz products. Published finding records concerning harmonic Bergman circle-trace staircase and Bergman commutators were checked for implication overlap and did not identify this singular-value law.

Risk: older two-factor canonical-form theorems can imply aspects of finite-rank behavior; publication priority of the entire combined theorem is not independently certified. The genuinely separate claim is the exact all-degree monomial singular spectrum and universal beta-law of its empirical distribution, neither of which appears in the inspected statements. Further exhaustive historical priority verification remains open.

## Mathematical value — PASS

The polynomial spectrum problem motivates asking how far harmonic Bergman Toeplitz quantization fails to be multiplicative. The answer gives an exact sharp finite-dimensional defect rank for every analytic polynomial and a complete singular-spectrum profile for increasing monomials. The limiting density, all Schatten moments, sharp norm and trace/Hilbert–Schmidt asymptotics form a natural nontrivial spectral law: finite-rank errors accumulate linearly many singular values despite each individual defect being nilpotent. This is a structural quantitative answer rather than a selected small numerical example.

Self-review: passed. Independent audit: not yet performed.
