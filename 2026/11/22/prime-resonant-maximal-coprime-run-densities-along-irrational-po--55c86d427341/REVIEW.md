# Scientific review: prime-resonant maximal coprime-run densities

## Correctness — PASS

For each fixed block length, Weyl's polynomial equidistribution provides uniform pairs of residues of \(n\) and \(\lfloor f(n)\rfloor\) modulo every fixed squarefree modulus. A prime excludes precisely \(\min\{p,r\}\) residue pairs with \(p\mid n\), giving the local factor \(1-\min\{p,r\}/p^2\). Holdridge's Theorem 1.3 removes the large-prime obstruction for each of finitely many integer translates of \(f\), so the global density exists. Inclusion-exclusion across the two endpoint failures gives the exact second difference, and two distinct primes larger than \(r+1\) provide a strictly positive density witness. The identity for \(C_{r+1}/C_r\), Mertens' theorem, and a prime-tail estimate prove both distinct asymptotics, including the factor removal exactly when \(r+1\) is prime. The independent finite arithmetic verifier passed 166 checks. Its finite tests are not treated as infinite proofs. The original analytic theorem is cited as an input rather than represented as a newly proved lemma.

## Originality — PASS, with residual priority risk

The source Holdridge paper proves an individual coprimality density and a large-prime elimination theorem. A published shifted-integer-polynomial result has the same Euler factors for a different deterministic arithmetic event, and therefore the block Euler product is not represented as a new numerical invariant. The new final claim is the existence and positivity of exact **maximal runs in the floor-shifted event**, with the sharp, two-scale prime/composite large-run asymptotics. The inspected complete theorems of the nearest published run-spectrum results concern finite fixed moduli and distinct predicates, not this varying-modulus floor-polynomial family. The second-difference technique, CRT, and prime number theorem are standard ingredients. The residual risk is an equivalent asymptotic derived in older generalized Schemmel or Jacobsthal literature under different terminology; it was not located in actual searches. This is not a claim of proven worldwide priority.

## Mathematical value — PASS

The exact positive density for *each* maximal length, followed by the unexpected factor-\((\log r)^2\) enhancement whenever \(r+1\) is prime, reveals fine arithmetic structure that a one-point density or a simple Euler-product statement does not display. The distinction persists across every qualifying irrational real polynomial of degree at least two and has a sharp leading constant. It is a motivated classification of the natural local-run statistic, not an arbitrary finite slice or minor numerical improvement.

## Closest literature and limits

Holdridge (2026), arXiv:2611.02223v1, Theorems 1.2–1.3, and the published *Coprimality densities for split integer polynomials and equidistributed integer parts* are the most relevant precursors. The published regular-residue and square-gcd maximal-run classifications also supply conceptual analogues. The source large-prime theorem is used as a cited premise; no joint-growth-in-\(n,r\) estimate or priority certification is claimed. The accompanying script provides finite consistency checks only.

Self-review: passed. Independent audit: not yet performed.
