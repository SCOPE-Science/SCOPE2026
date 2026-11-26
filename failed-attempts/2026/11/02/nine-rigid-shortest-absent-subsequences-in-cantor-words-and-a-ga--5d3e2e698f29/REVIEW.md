# Independent mathematical audit

## correctness

PASS

For a prescribed first bit, its earliest occurrence leaves the largest possible residual suffix, so minimizing the two residual shortest absent lengths gives exactly the SAS and their lengths. Applying this to 101000101 and its first-symbol-deleted suffix gives A·1·B and 11·B at lengths 5 and 4. Independently generated all bounded-length subsequences by iteratively appending each source symbol, verifying both base cases and the formula in 273 bounded gap configurations; replay: python3 /workspace/branches/independent-boundary-checks.py. For W_(r+1)=101000W_r, the residual offsets 3,4,5 each have the shorter choice starting with 1 and set 1^(2r−1)B; offset 2 ties with set {0,1}1^(2r−1)B; offset 1 has only the shorter 1 choice and set 1^(2r)B; offset 0 ties and gives A1^(2r−1)B. These transitions verify both induction statements for arbitrary r. Deleting surplus zeros embeds W_r, proving universality through m and presence of every noncandidate at m+1. A candidate's prefix 00 or 01 forces two or one initial source ones to be unused, respectively, and suffix 00 or 10 has the reversed effect; the units at the two ends suffice, regardless of internal odd gaps. The two sets of forced exclusions are disjoint, and the candidate needs one more 1 than remains. The nine choices are distinct because the boundary blocks occupy fixed positions. Finally, binary carrying in the ternary positions of the ones gives gap 3^ν₂(j); for k≥2 this places the complete Cantor iterates in the stated family. The original checker was inspected, not run; bounded checks are not the induction.

## originality

FAIL

The distinct indexed f1b1925790cc record proves the exact formula when every odd gap is one. Its proof already implies the full frozen extension: deleting surplus zeros from internal odd gaps preserves presence of every noncandidate through template embedding, and its §4 absence bound uses only the two unit end gaps. Both arguments apply unchanged to positive internal odd gaps. Thus the weakened hypothesis does not leave a distinct mathematical result, and the Cantor specialization is explicitly covered by both indexed matches. This is an implication comparison, not an inference about priority or provenance from a shared date.

## value

PASS

The full spectrum of first missing deletion patterns for a natural self-similar sequence family is mathematically informative: exact identities, not just the shortest length or number, describe its first failure of universality and its invariance to gap growth. This assesses the value of that structural result itself, not an incremental gain over the indexed proofs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
