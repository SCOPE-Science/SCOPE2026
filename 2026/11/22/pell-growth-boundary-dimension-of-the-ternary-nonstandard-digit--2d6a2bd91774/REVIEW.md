# Scientific review

## Correctness

PASS. Exact carry arithmetic yields the reachable states \(\{-2,-1,0\}\), their six proper nonempty inverse-image subsets, and the displayed transition matrix. Each nonabsorbing state can reach inclusion and exclusion, so local two-sided positive measure is genuinely equivalent (away from ternary endpoints) to never reaching an absorbing state. The matrix generating function is computed algebraically, and the irreducible right-resolving graph permits a Perron–Frobenius Frostman measure at the claimed exponent. The standard-library verifier independently tests prefix counts and finite recurrence cases. It does not purport to prove the infinite claims by enumeration.

## Originality

PASS, with a material prior-work caveat. Zhou, *Periodic counting, carry synchronization, and primes in nonstandard numeration systems* (arXiv:2611.07446v1), proves the measurable scaling limit and gives the exact same digit set as an example, but does not provide the boundary dimension or reverse ambiguity automaton. Tangjai, *A Non-standard Ternary Representation of Integers* (2020), is an especially close source: its Theorems 3.13 and 3.15 already establish Pell-type counts for maximal consecutive represented-integer blocks. This earlier growth fact is not claimed as novel; the present contribution is the exact undetermined-prefix enumeration and its essential-boundary Hausdorff consequence, requiring separate cylinder and Frostman arguments. Abram and Lagarias provide general graph entropy methods. Searches did not locate a covering complete statement, but other priority remains possible.

## Mathematical value

PASS. The natural boundary of a recently studied measurable scaling set quantifies where representability remains sensitive to arbitrarily deep ternary digits. This is a geometric classification, not just a known integer Pell-sequence restatement. The precise ambiguity-language enumerator provides additional finite-scale information and makes the dimension reproducible.

## Scientific limitations

No independent mathematical audit has been performed; the arbitrary topological boundary of a null-modified measurable representative is excluded. The result is for digits \(\{0,1,5\}\) only, and it does not determine Hausdorff measure or treat other digit sets. Tangjai's Pell antecedent raises a residual implication/priority risk.

Self-review: passed. Independent audit: not yet performed.
