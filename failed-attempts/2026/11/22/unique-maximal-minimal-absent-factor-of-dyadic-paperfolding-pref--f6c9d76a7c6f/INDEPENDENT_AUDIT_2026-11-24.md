# Independent mathematical audit

## correctness

PASS

In the 8-symbol synchronization base, for a fixed zero-based residue modulo 16 all positions except the sole multiple of 8 have fixed bits. Both exceptional bits occur and the 32 patterns are distinct. Equal length-2^r windows have the same start parity, so one-based even-index subsampling gives equal length-2^(r-1) windows with starts floor(i/2) and floor(j/2); induction proves the claimed synchronization. In the quarter-block check the invariant for j<m other than m/2 is equality of odd parts modulo four, not literal equality of the odd parts as integers. This follows because m divided by the exact power of two in j is divisible by four. The exception and the four boundary bits give B=D and opposite final bits in A and C. The only possible gap between equal length-m starts is 2m, and comparing those starts gives exactly m and 3m. Any longer repeat would repeat the first length-m block, but the second B has no next symbol. A minimal absent word of length at least 3 needs distinct occurrences of its interior to realize its two proper extensions. The predecessor sets at the two occurrences of B and the missing terminal successor therefore give exactly C_m B C_1 at maximal length. Independent recurrence, sorting and context-set checks confirmed k=5 through 13; the argument for all k is analytic.

## originality

FAIL

Under the exact older longest-repeat bound for the one-symbol-shorter prefix that the frozen record itself specifically credits to Bates–Bunder–Tognetti, all key conclusions are a mechanical boundary extension. The review establishes this implication directly without assuming their exact repetition table. The standard minimal-absent-word construction is verified separately in Barton et al. The decision is based on the recorded specific prior bound and the elementary extension, not on inability to read the older article or on title similarity.

## value

FAIL

The maximal missing factor of a canonical word is a natural invariant, but the specified one-symbol boundary makes it a direct corollary of the already credited longest-repeat length. Only one length-m window is added, its earlier occurrence is a direct comparison of two blocks, and the MAW is then the unique missing cross-context. The synchronization lemma is a proof device, not a separately substantiated new finding in the frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
