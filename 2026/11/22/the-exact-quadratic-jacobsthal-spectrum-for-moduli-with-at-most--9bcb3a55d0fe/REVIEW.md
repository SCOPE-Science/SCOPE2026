# Scientific review

## Correctness

**PASS.** The claim specifies every parameter: a modulus with one or two distinct prime factors, an initial shift of positive-square indices, a fixed residue class, and all nonnegative lengths. Prime-power scaling is exact because prime divisibility depends only on the radical. CRT converts the two-prime problem into covering initial indices by two square-residue fibers. Explicit tables for primes \(2,3,5\), the at-most-two-root constraint for larger primes, and index-square differences prove all entries through length six and exclude every longer run. The independent script reproduces every count over 1,059 eligible moduli up to 1,600 and 210 prime pairs below 79; these checks are corroborative rather than a proof of the infinite range.

## Originality

**PASS, subject to documented residual risk.** The nearest primary source is Kalmynin–Konyagin (arXiv:2302.00459, submitted 1 February 2023), which defines \(j_f\) and proves asymptotic lower bounds for primorial inputs. Its theorem, main proof, and polynomial square example were examined. They do not provide an exact one-/two-prime-factor classification, the complete initial-run count spectrum, or uniqueness of the extreme class. Searches for a quadratic-polynomial Jacobsthal semiprime spectrum and comparison with adjacent polynomial-value and quadratic-residue results identified no statement implying this one. Search failure by itself does not certify originality; the possibility of an older small-support calculation remains.

## Value

**PASS.** Two prime divisors form the first nontrivial interaction between independent local root fibers in this 2023-defined polynomial Jacobsthal invariant. The result is a complete infinite-family classification, not an arbitrary numerical cutoff: it identifies the exact threshold at small prime divisors, includes every prime exponent, computes all residue-class frequencies rather than merely a maximum, and proves unique long-run configurations. These exact small-support benchmarks are relevant to the local-cover perspective behind the general polynomial sieve construction.

## Scope and limits

The count starts at the first positive square and does not address shifted-index windows, radicals with three or more prime factors, or other polynomials. The literature comparison is best-knowledge rather than a certification of uniqueness. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
