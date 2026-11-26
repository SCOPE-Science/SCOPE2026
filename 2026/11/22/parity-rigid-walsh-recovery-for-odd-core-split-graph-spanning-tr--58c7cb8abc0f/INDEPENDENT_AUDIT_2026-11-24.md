# Independent mathematical audit

## correctness

PASS

Each unnormalized multiplier is the signed Kirchhoff cofactor with independent weights ±1. Independently, on vectors summing to zero within the clique and within the independent part the unweighted eigenvalues are m+n and m, respectively, of dimensions m−1 and n−1; the two constant-on-part modes have eigenvalues 0,m+n. Dividing the nonzero product by m+n verifies the tree count, odd when n is even. When n is odd, the cofactor modulo 2 has the indicated all-ones upper blocks, identity lower block and zero Schur complement, since n≡1. A mod-two corank m−1 gives determinant divisible by 2^(m−1), e.g. by Smith normal form. In the n=1 cofactor rooted at the independent vertex, the rank-one correction to diag(m+σ_i) has determinant zero at p=(m+1)/2 positive signs because p/(m+1)=(p−1)/(m−1)=1/2. In the clique-rooted cofactor each new independent vertex has odd nonzero signed degree d(s), and elimination contributes H(s)=diag(s′)−s′s′ᵀ/d(s). For opposite sign vectors the contributions cancel and their pivots multiply to −d(s)^2. The independent choices of p positive positions on the first vertex and of the first sign vector in each fixed labelled pair produce distinct characters as counted. For m=3 the even seed has Schur block [[2,−1],[−1,0]] and both leaf pivots 1; the odd seed cofactor diag(4,2,2)−J has determinant −4. Degree-one pairs preserve both moduli. Thus the lower bounds are sharp, and the character triangle inequality makes the all-positive count the exact maximum. Replay: python3 /workspace/reproduce_reviews.py 4 enumerated edge subsets via component merging and directly summed signs for all characters at m=3,n=1..4, confirming zero counts 30,0,1088,0 and least positive moduli 4,1,4,1. The all-size result uses the cofactor argument, not extrapolation.

## originality

PASS

This is a bounded positive assessment of the odd-core join theorem, in particular propagation beyond the complete-graph boundary, the all-n nullity lower bound and the uniform sharp triangular-core gap. Signed Kirchhoff machinery, the unsigned count and the n=1 case are covered antecedents, not independent novelty.

## value

PASS

Spanning-tree incidence is an intrinsic graph ensemble, and exact identifiability and restricted conditioning of its translation convolution are useful invariants. The contribution goes beyond the trivial odd-count guarantee and covered complete-graph case: it gives an all-parameter character construction of many blind modes, a uniform arithmetic obstruction, and optimal recoverable-mode stability for the first odd core. The lower bound is not advertised as the full nullity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
