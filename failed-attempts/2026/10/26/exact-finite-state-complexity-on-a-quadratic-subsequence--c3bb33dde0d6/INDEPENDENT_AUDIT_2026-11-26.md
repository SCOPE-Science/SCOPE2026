# Independent mathematical audit

## correctness

PASS

In S0 each of the 2s output fields costs 2|v|+2 bits; non-self-loop target fields can only increase cost. For total stored output L and input length k, n<=kL, so every description costs at least 4s+2L+k>=4+2 sqrt(2n). One state with outputs 0^a and the empty word, fed 0^(2a), costs 2a+4+2a and produces 0^(2a^2). Equality in the real bound forces 2n to be a square because the cost is integral; the even square root is 2a. This verifies the result for every n>=1, including descriptions with unreachable states. Inspected the encoding source and frozen VERIFICATION.md; no enumeration is needed.

## originality

FAIL

Neither inspected prior unary theorem prints the exact equality subsequence, but the closest published prior proof already uses the same storage-versus-input product bound and one-state block-output witness under the same S0 encoding. Retaining the mandatory four delimiter bits, applying AM–GM with its equality condition, and dispensing with the unused loop's nonempty padding output gives the frozen claim directly. The basis is demonstrated mechanical derivation from the prior proof, not failure to retrieve literature or a claim that the exact numbers were printed there.

## value

FAIL

Constant words are a natural benchmark and the equality proof is correct, but this exact subsequence comes from retaining the fixed encoding overhead in the existing unary lower-bound proof and using its block loop without padding. It yields no distinct structural insight about optimal finite-state descriptions beyond that routine optimization. No valuable independent remainder was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
