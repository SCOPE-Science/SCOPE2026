# Independent mathematical audit

## correctness

PASS

For the zero-run binomial vector, Vandermonde gives the period condition binom(T,j)=0 mod m for 1<=j<=a; necessity from a shift-period of just binom(r,a) follows by evaluating the difference in the binomial basis at r=0,...,a-1. For each p^e dividing m exactly, let h=floor(log_p a) and v=v_p(T). If v>=e+h, binom(T,j)=(T/j)binom(T-1,j-1) suffices for all j. Otherwise, when v<=h the coefficient at j=p^v is nonzero mod p by the base-p digit at v; when h<v<e+h the coefficient at j=p^h has valuation v-h since the low h digits of T-1 are all p-1. This proves the claimed period P. If vectors at r and s coincide, triangular Vandermonde induction forces all the coefficients for T=s-r to vanish, so the phases are distinct. On the degree-1-through-b coefficient module Y, returning the zero count to its fixed phase while appending one 1 realizes F_0(Y)=(1+X)Y and F_1(Y)=(1+X)Y+X, by choosing intermediate phases corresponding to 0 and a. These are permutations, so their inverses are realized by positive powers. F_1 F_0^{-1} translates by X; conjugates translate by X(1+X)^j for j=0,...,b-1. Their coefficient matrix is triangular with diagonal 1, yielding every Y over the residue ring, even over composite m. Advancing by zeros then realizes each phase. For two vectors, choose the highest differing prefix coordinate j and append the target tail of length a+b-j. Smaller differences cannot reach the output in that many symbols, larger differences are zero, and the j-th difference advances along one matching path with coefficient 1. Thus every phase-coefficient pair is distinguishable for the Moore output. At m=2 it also separates either Boolean residue class. Independent BFS and refinement on the uncompressed prefix-vector recurrence agreed on 101 bounded parameter triples, including composite moduli. Replay: `python3 /workspace/branches/review_checks.py 4`.

## originality

PASS

The b=1 exact Boolean bounds and period mechanism, and the exact Moore count for 0011, are credited antecedents. The supported distinction is the uniform exact full-residue state count for both run lengths unrestricted, with each added terminal 1 contributing a free modular coordinate. No compared source establishes that family or an applicable stronger exact theorem; generalized counting maps and periodic binomial phases alone do not establish the necessary orbit and separation.

## value

PASS

The result determines the exact deterministic memory for the natural class of all binary two-run patterns and all moduli, rather than an isolated additional pattern. It explains the asymmetry between the initial-run prime-power staircase and the multiplicative cost of each terminal extension; the group of return loops gives a reason why the second-run coordinates are independent even over composite moduli. The exact count separates genuinely needed memory from the naive full prefix-counter bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
