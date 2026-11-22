# Scientific review

## Correctness — PASS
The kernel has exactly three entry levels, leading to an integer block expression. The claimed change of bases uses primitive integer vectors, hence unimodular maps; the reduced two-by-two and four-by-four matrices have calculated determinantal divisors. The Smith list is in divisibility order and has exactly \(p(p-1)\) entries. Exact computations independently confirm the original full matrix at primes \(2,3,5\), the block identity at further primes, and the four-by-four minors through odd primes below \(102\). These finite calculations are not substituted for the general proof.

## Originality — PASS, with risks
The nearest public mathematical literature concerns full-residue GCD graph energies (Sander--Sander, arXiv:1205.4603), full-ring unitary Cayley graph spectral theory (Liu--Zhou, arXiv:1205.5932), and classical index-GCD Smith matrices (Ilmonen--Haukkanen, DOI:10.1080/03081081003709819). The relevant inspected theorems do not imply the integer Smith form of the unit-restricted GCD-difference kernel. Closely related Ramanujan and unrestricted GCD matrices have different entries and index sets. The complete text of the classical index-GCD work was not accessible, and an implicit earlier integer-block-matrix classification remains a bibliographic risk. Search noncoverage alone is not considered a proof of novelty.

## Mathematical value — PASS
At the first nonsquarefree modulus, restricting a natural arithmetic difference kernel to primitive residues produces a highly nontrivial integral cokernel. The theorem determines its full torsion decomposition for every prime, not just rank or determinant, and reveals a distinguished order-three obstruction even when the entries use only prime factors disjoint from three. It has an explicit proof and a natural role in arithmetic linear algebra.

## Evidence and limitations
The exact all-prime proof is in `RESULT.md`; `verify.py` tests three complete integer Smith forms and sparse determinantal divisors across further primes. The claim is restricted to prime-square moduli and makes no claim about all prime powers. Independent validation is not asserted.

Self-review: passed. Independent audit: not yet performed.
