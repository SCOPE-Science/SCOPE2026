# Independent mathematical audit

## correctness

PASS

For H_n with only nonzero products a_{2i}a_{2i+1}=a_i, source Example5.4 gives a nonzero balanced product of 2^{n-1} leaves and maximal surviving multiplication depth n-1. Every binary term with more than 2^{n-1} leaves must have depth >=n. By source Theorem4.7 every depth-n term vanishes, so Pol*_{2^{n-1}+1} vanishes; by Theorem3.9 the groupoid is 2^{n-1}-supernilpotent. The published nonzero balanced term of 2^{n-1} distinct variables disproves (2^{n-1}-1)-supernilpotency. Hence least parameters n and 2^{n-1}. Independent bottom-up capacity recursion checked n=3..9 as finite confirmation; general proof uses the elementary binary-tree leaves/depth inequality.

## originality

FAIL

FAILED: The SAME 2026 primary paper arXiv:2610.03348, Theorem4.7 plus Example5.4, already implies all depth-n terms in the given H_n vanish and supplies a nonzero balanced 2^{n-1}-variable term. Its Theorem3.9 translates zero Pol*_{k+1} to k-supernilpotency. The universal binary-term bound leaves<=2^{depth} immediately yields the claimed upper k=2^{n-1}, while the published witness proves sharpness. So the exact class is already a direct corollary of published results, irrespective of whether the authors explicitly wrote the closed-form parameter.

## value

FAIL

FAILED: The assigned leaf capacity function is a correct alternative notation for the elementary full-binary-tree maximum-leaf bound. Since its sharp lower witness and both conversion theorems are published together in the very same paper, the exact numerical parameter requires no substantial new classification, boundary, or unresolved lemma; the arithmetic exponential wording alone does not create independent scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
