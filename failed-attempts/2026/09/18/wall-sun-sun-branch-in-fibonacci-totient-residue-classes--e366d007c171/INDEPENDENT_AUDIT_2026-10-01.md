# Independent audit — 2026-10-01

## Final claim

For odd prime q not equal to 5, the relative density of q^2-divisible Fibonacci indices inside a Pisano-period residue class is 1 or 0 in the Wall--Sun--Sun branch and 1/q or 0 otherwise, with the stated consequences for S(q) and external witnesses.

## Correctness — PASS

The proof is correct. For every positive integer N, N divides F_m exactly when z(N) divides m. For an odd prime q not equal to 5, the standard lifting dichotomy gives z(q^2)=z(q) in the Wall--Sun--Sun case and z(q^2)=q z(q) otherwise; also z(q) divides pi(q) and q does not divide pi(q). The progression intersection is therefore empty unless z(q) divides r, and when nonempty has relative density 1 in the exceptional case or 1/q in the ordinary case. On terms with q^2 not dividing F_m, divisibility of phi(F_m) by q must come from a prime divisor p not equal to q with p congruent to 1 modulo q. A fresh direct computation reproduced the rank/period identities for several small primes; the finite script is only a sanity check.

## Originality — FAIL

The exact density statement is a direct corollary of classical rank-of-apparition lifting and elementary congruence intersection. Those stronger prior facts mechanically determine the 0/1/q cases; the new note correctly exposes a flaw in a recent paper, but the mathematical density theorem itself does not survive the implication-based originality test.

### Equivalent formulations

Searches: Wall rank of apparition prime powers; Goel arXiv:2604.17847v3; semantic search for Fibonacci-totient witness density

Evidence: Classical Fibonacci prime-power lifting determines z(q^2); Goel supplies the S(q) progression setting.

Reasoning: The residue-density formulation is equivalent to intersecting one arithmetic progression with the divisibility progression z(q^2)Z.

### Broader coverage

Searches: Wall 1960 rank/period theory; later prime-power witness-density record

Evidence: Classical rank/period results are strictly broader than the q^2 density computation; a later published record further generalizes to q^a.

Reasoning: The final numerical density is a specialization of broader prime-power divisibility structure.

### Exact database or table

Searches: Targeted exact search for the four-case density table

Evidence: No earlier printed four-case table was located.

Reasoning: Absence of the table does not restore originality because the values are mechanically implied by stronger prior theorems.

### Claim versus prior implication

Searches: Goel Lemma 4.3; Wall rank lifting

Evidence: Goel's Lemma 4.3 incorrectly treats nonexistence of known Wall--Sun--Sun primes as universal and claims eventual absence of square divisibility; Wall's lifting facts already imply the corrected recurring pattern.

Reasoning: The correction is scientifically important, but its mathematical content is a direct consequence of prior rank-lifting theory.

### Source inspections

- **Sophie Germain Primes and the Totient of Fibonacci Numbers** (arXiv:2604.17847v3): The paper contains the flawed universal exclusion and all-but-finitely claim that the record corrects. Material read: Full arXiv HTML through Lemma 4.3 and the surrounding S(q) setup. Evidence: Lemma 4.3 argues from the absence of known Wall--Sun--Sun primes and concludes external witnesses for all but finitely many progression terms.

Checked sources: D. D. Wall, Fibonacci Series Modulo m, American Mathematical Monthly 67 (1960); A. Goel, Sophie Germain Primes and the Totient of Fibonacci Numbers, arXiv:2604.17847v3, especially Lemma 4.3; Published-record semantic search including the 2026-09-19 prime-power witness-density strengthening

Residual risks: The originality failure is implication-based; it does not dispute the usefulness of identifying the flaw.

## Scientific value — PASS

The correction isolates a genuine exceptional branch in a recent universal argument, quantifies the ordinary recurring square-witness density, and states exactly when external prime witnesses are forced. That is a motivated boundary/correction even though the arithmetic is classical.

## Limitations

- No Wall--Sun--Sun prime is known; the density-one exceptional branch is conditional on existence.
- Scientific rejection is originality-only; correctness and the correction value survive.

## Conclusion

The final claim is not accepted because all three axes must pass; the surviving correctness/value evidence is retained.
