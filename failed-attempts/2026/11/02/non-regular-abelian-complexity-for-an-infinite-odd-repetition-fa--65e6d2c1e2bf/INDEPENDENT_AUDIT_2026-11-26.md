# Independent mathematical audit

## correctness

PASS

All nine adjacent pairs occur: same-letter and successor pairs appear within images, and predecessor pairs across images of a repeated letter. For the weighted recurrence split a window of length k^(m+1) into r whole blocks and two end fragments which themselves form a legal length-k^m window when joined. For attainment maintain a maximizing window starting in the first block of either (c-1,c) or (c,c+1), where c maximizes the level-m block weight. At offset j in either first block, the suffix, r copies of U_c, and the required length-j prefix occur in U_(c-1)^r U_c U_c^r U_(c+1). The lift starts in the first large block, so its new pair (c-1,c) serves for either allowed next maximizer c or c-1; c+1 cannot strictly beat c. At m=0 the invariant holds with the maximizing letter as the first block. Applying this to weights ±1_{a=0}, with the sliding-window step at most one, gives the exact complexity. The cyclic Fourier formula and its difference product yield the median criterion at m=3n, where the parity vector is (0,1,1). The rational cosine of 2 arg(r+ω) lies strictly between 1/2 and 1, so on every progression 3pn both sides of the median criterion occur infinitely often. Thus the range parity and, by differencing and odd r, complexity parity are not eventually periodic at powers. A finite automaton on the inputs 10^m would be eventually periodic, contrary to the reduction modulo 2 of any integer k-regular sequence. The supplied Python and output are finite corroboration only; the block-invariant and parity proof were reconstructed from the frozen text.

## originality

FAIL

Two distinct indexed full texts cover the mathematical finding. The October 26 entry gives the identical morphism and coding, the identical power-length formula and nonregularity for all r≥4, with a stronger limit-set conclusion. The distinct November 2 entry additionally proves nonperiodicity of the very same range parity; on odd r its modulus-2r first-difference argument gives the frozen assertion modulo 2. This is established scope and implication overlap, not a priority decision based on dates or a claim that the frozen proof is false.

## value

PASS

The theorem addresses a natural question from the r=3 precursor in infinitely many bases. Power-length exact extrema and the parity mechanism are informative beyond verifying individual examples. This is an assessment of the mathematical question and result in isolation; it does not supply an incremental contribution over the covering records.

The dated certificate retains the supplied scientific assessment, sources and limitations.
