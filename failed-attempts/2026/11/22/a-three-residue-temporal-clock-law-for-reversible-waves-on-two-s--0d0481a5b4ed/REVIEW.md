# Independent mathematical audit

## correctness

PASS

For M=A_K−I=UV on the labelled 2-subsets, the injective U=B^T and surjective B give VU=(2−n)I−nJ. For n≡0, M/2 is a rank-n projection; for n≡1, M is a rank-(n−1) projection, using im V equal to the sum-zero hyperplane. For n≡2, M has rank n and M² rank 1 with a nonzero eigenvalue 2 on the constant line, leaving n−1 nilpotent blocks of size two and N−2n+1 singleton blocks. On a size-two spatial block at 1, put R=A−I and Z=T+I. Then Z²=RT, Z³=−RZ≠0 and Z⁴=0, giving a single length-four block. The scalar spatial eigenvalues 0,1,2 yield temporal order 4,6,3 respectively, and the long block order 18. In characteristic three raising a signed unipotent block to a t-th power yields the stated sign and min(block length,3^ν₃(t)) fixed dimension. Component least common multiples give the exact supports and orders, including KG(4,2); dimensions are invariant under field extension. In the third residue E(18)=2N−2, E(12)=2N−n+1, E(6)=2N−n−1; inclusion–exclusion gives the asserted factorization. The source's verify_kneser.py and captured verification_output.txt were inspected, not run: they record direct prime-field matrix nullities at nine times for n=4,…,10 and a full state census only at n=4. The all-size result follows from algebra, not those finite checks.

## originality

FAIL

The earlier triangular Johnson result supplies the exact spatial Jordan blocks in every residue and the temporal fixed-space rule. Although the two wave maps need not be conjugate, the Kneser adjacency is a polynomial in the triangular adjacency in characteristic three, so the entire frozen result is a blockwise corollary. Let C=A_tri and M=C−I=B^TB over F₃. Then M²=(n−2)M+J_N by BB^T=(n−2)I+J_n and B^TJ_nB=4J_N=J_N. Thus A_K=J_N−I−C=p_n(C), p_n(x)=x²−(n+1)x+n−2. On J₂(λ) the image is p_n(λ)I+p′_n(λ)R. For n≡0, p_n(2)=p′_n(2)=0 and p_n(1)=1: it gives n scalar zeros and N−n scalar ones. For n≡1, p_n(1)=1,p′_n(1)=0,p_n(0)=2: N−n+1 scalar ones and n−1 scalar twos. For n≡2, p_n(x)=x², p′_n(1)=2 and p_n(0)=0: the prior triangular Jordan form is preserved up to similarity. The prior temporal-block rules now give the three clocks and all dimensions and least periods, and the period-36 fraction is inclusion–exclusion on the already identical third-residue census.

## value

FAIL

A full fixed-state and orbit census for these natural graphs is a meaningful objective, but the claimed incremental invariant is already known or mechanically obtained by applying an explicit quadratic to the prior Jordan table and reusing its temporal rule. The compact extremal fraction is routine inclusion–exclusion in the literally shared fixed-state table. No distinct valuable remainder was established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
