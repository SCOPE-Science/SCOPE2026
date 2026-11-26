# Independent mathematical audit

## correctness

PASS

Reconstructed the four-state inverse recurrence from x_(i+2)=y_i XOR x_i XOR x_(i+1). Counting the old state at each output position, concatenation composes return permutations and adds decorated-letter counts from the second block at the first block's exit state. An independent exact block-composition reconstruction, /workspace/branches/independent-certificate-3.py (replay: python3 /workspace/branches/independent-certificate-3.py), without running the supplied scripts or expanding the words, verified the two depth-16 return permutations (0,3,1,2) and (1,2,0,3), lengths 2584 and 1597, and the complete transpose incidence certificate. With T=Mᵀ and w=Rᵀ, it gave (T³-I)w=(0,0,24,-24,24,-24,0,0)ᵀ and T times that vector equal to itself. Both finite identities matter: the return identities ensure block compatibility inductively under substitution; the invariant increment implies the k+3 identity at every k. Exact k=0,1,2 initial rows match, and log F_(16k+2)=16k log φ+O(1), giving signed count slopes ±1/(8 log φ) with bounded residue terms. The Findings' indexing and the proof agree. Editorial off-by-one in the scope sentence: the last counted pair is (x_(N_k-1),x_(N_k)); the final update uses x_(N_k+1), which is not itself counted. This does not change the explicitly defined count or theorem. No inference is made for arbitrary prefixes or temporal dynamics.

## originality

PASS

Available inverse-lift theory gives structural, and possibly broader qualitative, coverage. The supported distinct claim is the exact branch-dependent period-three discrepancy drift at the specified Fibonacci prefixes, not the existence of inverse branches, the use of permutations, or qualitative frequencies alone.

## value

PASS

For a natural parity inverse of an aperiodic substitution word, identical limiting frequencies conceal a signed logarithmic bias on two of the four branches and bounded bias on the other two. The exact recurrence identifies which initial conditions exhibit the drift and its scale along two permutation-compatible full substitution blocks, not a fitted or arbitrary small-instance table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
