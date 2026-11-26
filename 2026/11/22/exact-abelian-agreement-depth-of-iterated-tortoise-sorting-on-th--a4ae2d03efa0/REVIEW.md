# Independent mathematical audit

## correctness

PASS

Deleting the first k original ones and appending k ones sorts a word if its weight is at most k; if its weight is k+1, its image is determined by its trailing zero count. The complementary pairs (t_{2i},t_{2i+1}) contain one one each. Thus no factor shorter than 2k has weight above k, and an exceptional weight-(k+1) factor of length 2k must start odd and end in 1, so it sorts too. At 2k+1, the weight is k or k+1; for weight k+1 the terminal one is in one of the final two places by start parity. The proposed i=2^r-k with r congruent to s_2(k-1) modulo 2 gives t_i=0 and t_{i+k}=1 by r-bit complementation. Starts 2i and 2i+1 realize the sorted and interrupted high-weight outputs, and a zero as the extra aligned symbol realizes the low-weight output. This proves exactly three images in two weight classes at first divergence, including k=1; the empty factor has one image and one weight. A separate direct deletion-and-append check on a length-2048 prefix, k=1..8, matched the entire tested threshold profile; it is finite corroboration only. Frozen verify.py and its stored output were inspected, not rerun.

## originality

PASS

The supported contribution is the all-k cutoff and complete first-divergence image set. The k=1 depth is already exhibited by the prior complexity lists. The primary source defines the exact general invariant and proposes its Thue–Morse evaluation; inspected two-pass studies do not resolve its all-iterate value.

## value

PASS

This answers an explicitly proposed evaluation of a natural sorting-complexity invariant for a canonical automatic word. The all-iterate exact cutoff shows precisely where the number of ones ceases to determine the iterated image; the three-image profile identifies the surviving positional information. It is not merely an extrapolation from numerical tables or a restatement of the one-pass result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
