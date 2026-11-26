# Independent mathematical audit

## correctness

PASS

RESULT.md lines 13–30 give the correct all-parameter proof. The binary increment edges of each carry length toggle by the corresponding prefix parity; the full carry and wrap toggle by the last prefix parity. Dividing the transition total by two gives an integer in [0,K] as a bijectively encoded integer in [0,K−1] plus one bit. Excluding the constant mask leaves two masks per interior count and one at K, and each mask gives two offsets. If a low bit is active, no zero run contains a whole aligned block; the prefix/suffix lengths across one boundary sum to at most L, including at wraparound. With no active low bit, block expansion of the balanced quotient word gives n/2+LR by counting zero windows, also for s=0 and K=1. The remaining multiplicity is 2^(m+1)−1−4(K−1). Reflected Gray evaluation preserves the entire word set by invertible linear precomposition; no arbitrary-order invariance follows. An independent packed-bit rotation/AND census confirmed every stated window for m=2 through 9 in both orders (python3 /workspace/branches/audit_rm.py); this is supplemental, not the proof. The deposited script was inspected, not executed.

## originality

FAIL

The distinct 2026-10-13 ordered RM(1,m) all-width result 4ba592bdb146 already entails the full binary-order histogram, not merely its minimum. Reflected Gray order is a routine invertible linear coordinate relabeling that yields exactly the same evaluation word set, not an independent, uncovered spectrum.

## value

FAIL

Ordered cyclic spectra are useful, but this exact slice is a direct specialization of the existing all-width enumerator and supplies no independently needed invariant beyond it. The Gray case preserves the entire codeword set by a standard linear change of variables, rather than treating a substantively different order. Exact recomputation and a shorter specialized proof do not establish a surviving valuable claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
