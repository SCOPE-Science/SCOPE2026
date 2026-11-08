# Scientific review: exact mixed additive conductor

## Correctness

PASS. The theorem is about all positive integers, not a sampled interval. The odd infinite tail is covered by 99,225 residue classes modulo 198450, using a proof of coprime-multiplier preservation. The gap up to the verified tail cutoff is covered by exact finite arithmetic, including all 208 odd Zumkeller summands needed and the single special 20177 case. The obstruction at 19067 is checked by the *necessary* even-sigma and abundancy inequalities for every possible practical partner, so no omitted odd Zumkeller case could invalidate sharpness. The even case has elementary residue-class identities. These steps have been reconstructed and the executable certificate replayed.

## Originality

PASS within inspected sources. Somu–Kukla–Tran (arXiv:2310.14149v2, Section 4) proves qualitative eventual coverage for Zumkeller-plus-practical numbers but supplies no least cutoff; its numerical 32761 concerns Zumkeller-plus-Zumkeller, not the present problem. Searches for exact conductor 19067, mixed practical/Zumkeller exceptions and equivalent additive formulations found no covering statement. OEIS A005153 and A083207 classify the summand types, not their exact mixed-sum cutoff. Related published results about Zumkeller numbers with prescribed prime support and divisor partitions have different conclusions. Unindexed prior computations or unpublished work remain a residual risk, and only abstracts were accessible for some ancillary articles.

## Mathematical value

PASS. The exact last exceptional integer is a natural invariant of a previously studied additive representation problem, and the sharpness witness 19067 makes the cutoff meaningful. The result replaces a non-effective existence threshold with a complete sharp conductor, not an arbitrary finite computation. The modular part supplies a finite, reproducible certificate for the infinite tail and a bridge down to the true threshold.

## Scope and limits

The full list of smaller exceptions and representation multiplicities are not classified. The computational certificate uses integer arithmetic without floating point. It has not received an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
