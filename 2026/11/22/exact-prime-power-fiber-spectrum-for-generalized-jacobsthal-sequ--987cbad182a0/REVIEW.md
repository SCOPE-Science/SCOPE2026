# Self-review

## Correctness — PASS
The closed form \(J_n=(a^n-(-1)^n)/(a+1)\) and the primitive-root order establish the least period \(\varphi(p^r)\). The even and odd index branches exhaust the square and nonsquare units, respectively; each contributes at most one preimage. The overlap character sum is evaluated by the identity \(\sum_{z\bmod p}\chi_p(z^2-1)=-1\) and yields \(c_p\). The three histogram entries follow by counting branch sizes and their intersection. This is a proof for all \(p\ge5\) and \(r\ge1\), not extrapolation from finite data. The included independently programmed check passed 76 cases, 583,944 targets and 566,784 sequence terms.

## Originality — PASS
Al-Kateeb (arXiv:1911.11515, 2019) and Bród–Michalski (2022) already provide the generalized recurrence and its Binet formula; the present claim does not repackage these as new. Griffiths–Bramham (2015) and the published 2026 complete-modulus and local-isometry classification establish residue-completeness statements but not the primitive-root, nonsurjective prime-power fiber multiplicities. A differently parameterized 2023 Jacobsthal article is inapplicable. The supplied structured review records exact search formulations, implication comparisons and material inspected. Classical Legendre-symbol calculations are credited. An undiscovered general result about Lucas recurrence fibers could still subsume this theorem.

## Value — PASS
This result resolves the natural first-coordinate multiplicity question beyond binary completeness: every target gets an exact count, the entire histogram is independent of the generating parameter, and an explicit \(p\bmod8\) bias persists unchanged at every prime-power level. The scope is natural and infinite while the required proof remains self-contained.

## Limitations
The result only treats primes \(p\ge5\) at which the fixed parameter is a primitive root modulo the stated prime power. It neither classifies arbitrary parameters nor proves a fixed base works at infinitely many primes. Bibliographic priority is qualified by the residual search risks above. Machine verification checks finite examples and is not independent validation.

Self-review: passed. Independent audit: not yet performed.
