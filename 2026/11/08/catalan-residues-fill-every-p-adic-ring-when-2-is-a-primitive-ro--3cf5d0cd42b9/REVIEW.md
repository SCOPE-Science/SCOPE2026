# Scientific review of the corrected Catalan residue theorem

## Correctness — PASS for the final corrected statement

The original version's sparse-window unit congruence was false for prime-power precision beyond two: for example, at \(p=3,k=3,n=3^9\) it predicted \(C_n\equiv2\pmod{27}\), but the actual value is \(20\pmod{27}\). That version of the proof is superseded, not silently declared correct. The complete replacement in `RESULT.md` proves the same unconditional-on-\(k\), conditional-on-primitive-root conclusion by a different argument. Its exact factorial identity makes high blocks multiplicative modulo an arbitrary chosen precision, while central binomial units at indices \(p^T\) converge to a unit congruent to \(2\pmod{p^2}\). The latter is a generator at every prime-power level under the stated hypothesis. Kummer's carry theorem provides base indices with arbitrary prescribed valuation; successive high blocks multiply their normalized units by arbitrary powers of the generator. These facts jointly prove surjectivity and infinitely many witnesses. Bounded independent modular tests, including the regression counterexample, corroborate but do not replace the proof.

## Originality — PASS, materially qualified

Burns (2017) gives surjectivity only modulo \(p\), and previously established exact all-powers results at \(p=3\) do not imply the larger primitive-root prime class. Rowland–Yassawi and Granville provide background congruence techniques, not this precise universal Catalan-image statement. Berend–Harmse (1998) proves density for *central binomial* coefficients, which does not directly imply the Catalan sequence with the needed index congruence. A contemporaneously published theorem on all-odd-prime central-binomial index–value fibers *does* imply a stronger Catalan coverage result: its source commit was recorded 46 seconds after this source, and both entered the same Resultary publication commit. This unusually strong overlap remains an explicit priority/publication-coordination risk. Do not claim independent global priority.

## Scientific value — PASS

Unbounded prime-power surjectivity of a classical integer sequence is a motivated arithmetic gap; the explicit generator-and-carry proof gives infinitely many witnesses and extends beyond the single earlier ternary case. This is distinct from a finite residue table. The primitive-root hypothesis is explicit, testable, and sufficient; necessity, abundance of qualifying primes, and witness density are not claimed.

## Scope and verification

The exact domain is odd prime \(p\) with \(2\) primitive modulo \(p^2\), any exponent \(k\ge1\), all residues, with infinitely many indices for each. All files use the standard convention \(C_n=B_n/(n+1)\). `verify_catalan.py` replaces tests of the false sparse-window congruence with independent checks of the corrected lemmas. Earlier scientific review evidence and source blobs are preserved in version history and in the independent-audit ledger; a corrected independent assessment is not an expert attestation or formal verification.
