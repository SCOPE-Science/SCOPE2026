# Independent mathematical audit

## correctness

PASS

Any pair of input embeddings into a minimal common supersequence must cover all positions, or an uncovered position is deletable. Thus length is at most a+b+c+d. At equality the embeddings must be disjoint and both unique (fix either embedding; the other must use the whole complement). The a-th zero and c-th one cannot coincide. If the a-th zero comes first, at least b+1 ones follow it, giving multiple embeddings of A; if the c-th one comes first, at least d+1 zeros follow it, giving multiple embeddings of B. This reduces the upper bound by one. At that length every embedding pair shares exactly one position; the letter inventory determines its symbol. For the zero-sharing branch take first a zeros and last b ones for A, first c ones and last d zeros for B, which are valid whenever the inputs embed. The shared a-th zero lies between ones c and c+1, defining a unique central gap of h≥1 zeros. With x prefix and y suffix zeros the exact feasibility conditions are x+h≥a and h+y≥d, with x+h+y=a+d−1; hence x≤a−1 and y≤d−1. These last two bounds make all ones essential: losing one of the first c forces a later c-th matched one for B, and losing one of the last b forces an earlier first matched one for A. A prefix zero is essential iff x+h=a, a suffix zero iff h+y=d, and a gap zero iff at least one of these equalities holds. For a,d≥2 both x,y must be positive: if only one is positive its tightness forces a=1 or d=1; if both are zero a gap zero is deletable. The equalities then force x=a−1,h=1,y=d−1. When a=1 or d=1 the corresponding outer zero count vanishes and summing all permitted gap lengths gives the stated hockey-stick identities, including a=d=1. Independent interleavings of the prefix and suffix yield the binomial product in the interior. Complementation and input exchange give the disjoint other inventory with H(c,d,a,b); the positive counts construct words attaining the bound. Replay: python3 /workspace/branches/frozen_math_reproductions.py 5, a separate standard-library literal enumeration, checked counts separately by inventory and excluded length L+1 for 86 tuples (1,294 longest words summed over tuples), including asymmetric boundary examples. This supports but does not replace the all-parameter proof. Uploaded code and recorded outputs were inspected, not executed.

## originality

PASS

Pass the unrestricted four-positive-run binomial count and structural split at the longest deletion-minimal layer. Prior records exactly give the counts and lengths on balanced and cross-equal subfamilies; general graph enumeration is not new. The same-date shortest-supersequence result also agrees on the slice where shortest and longest-minimal lengths coincide, but not in general. No identified earlier result establishes the full longest-layer count with independently variable run lengths.

## value

PASS

Even a longest-length algorithm leaves open how many distinct input-merging outcomes realize that length. This formula classifies all four freely variable run lengths, accounts for the change of behavior when an outer run has size one, and counts words without overcounting different embeddings. Its simple geometric decomposition into forced central gaps is useful for the longest layer beyond previously counted symmetric cases; it does not assert shorter-layer or general-string closed formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
