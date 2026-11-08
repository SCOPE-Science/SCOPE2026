# Rank-resolved idempotent decomposition fibers at square-zero matrices in characteristic two

## Finding
Let \(k=\mathbb F_q\), where \(q=2^f\) and \(f\ge1\). Fix \(n\ge1\), and a matrix \(N\in M_n(k)\) satisfying \(N^2=0\). Put \(r=\operatorname{rank}N\) and \(s=n-2r\). For integers \(b\) define
\[
H_{n,r,b}(q)=\#\{(P,Q)\in M_n(k)^2:P^2=P,\ Q^2=Q,\ P+Q=N,\ \operatorname{rank}P=\operatorname{rank}Q=r+b\}.
\]
Then for every integer \(0\le b\le s\),
\[
\boxed{H_{n,r,b}(q)=q^{rs}{s\brack b}_q q^{b(s-b)}\sum_{a=0}^{r}{r\brack a}_q\,q^{r^2-a(r-a)}.}
\]
No decomposition with unequal summand ranks, or with their common rank outside \(r,\ldots,r+s\), exists. The symbol \({u\brack v}_q\) means the number of \(v\)-dimensional subspaces of \(k^u\), equivalently \(\prod_{i=0}^{v-1}(q^{u-i}-1)/(q^{v-i}-1)\), and equals zero for out-of-range indices. Thus the total number of ordered decompositions is the sum of the displayed fibers over \(b\).

## Assumptions and scope
All matrices are labeled, not identified up to similarity. The field has characteristic two, including all finite extension fields. The only target hypothesis is \(N^2=0\); necessarily \(0\le r\le\lfloor n/2\rfloor\). The value of each fiber depends only on \(n,r,q\). There is no requirement that either idempotent have rank one or be nonzero.

## Proof
Because \(Q=P+N\) in characteristic two, the two equations \(P^2=P\) and \(Q^2=Q\) are equivalent to \(P^2=P\) and \(PN+NP=N\). Choose a decomposition \(k^n=U\oplus W\oplus Z\), where \(\dim U=\dim W=r\), \(\dim Z=s\), and \(N\) sends \(W\) identically onto \(U\), annihilating \(U\oplus Z\). In these ordered block coordinates, the anticommutator equation forces exactly
\[
P=\begin{pmatrix}A&B&C\\0&I_r-A&0\\0&H&K\end{pmatrix},
\quad A,B\in M_r(k),\ C\in M_{r\times s}(k),\ H\in M_{s\times r}(k),\ K\in M_s(k).
\]
Direct block multiplication gives necessary and sufficient remaining conditions
\[
A^2=A,\qquad K^2=K,\qquad AB+BA=CH,\qquad AC+CK=C,\qquad HA+KH=0.
\]
Fix \(a=\operatorname{rank}A\) and \(b=\operatorname{rank}K\). Since idempotents are diagonalizable even in characteristic two, we may independently choose bases in \(U\) and \(Z\) such that \(A=\operatorname{diag}(I_a,0)\), \(K=\operatorname{diag}(I_b,0)\). The equation \(AC+CK=C\) allows precisely those entries of \(C\) joining **opposite** eigenvalues of \(A\) and \(K\); their number is \(a(s-b)+(r-a)b\). The equation \(HA+KH=0\) allows precisely those entries of \(H\) joining **equal** eigenvalues; their number is \(ab+(r-a)(s-b)\). The sum of these two dimensions is \(rs\), so the pair \((C,H)\) has exactly \(q^{rs}\) possibilities independently of \(a,b\).

Every allowed product \(CH\) is off-diagonal relative to the \(A\)-eigenspace splitting. The linear map \(B\mapsto AB+BA\) has image exactly these off-diagonal blocks and kernel dimension \(a^2+(r-a)^2\). Consequently there are exactly \(q^{a^2+(r-a)^2}\) solutions \(B\) for each allowed \((C,H)\). The number of rank-\(a\) idempotents \(A\) equals \({r\brack a}_q q^{a(r-a)}\): choose their image and a complementary kernel. Analogously the number of rank-\(b\) idempotents \(K\) is \({s\brack b}_q q^{b(s-b)}\). Multiplying and using \(a(r-a)+a^2+(r-a)^2=r^2-a(r-a)\) produces the stated sum.

For rank support, reorder the blocks from \((U,W,Z)\) to \((U,Z,W)\). The resulting \(P\) is block upper triangular with diagonal blocks \(A,K,I_r-A\). Since \(P\) is idempotent, its rank is the multiplicity of eigenvalue one, namely \(a+b+(r-a)=r+b\). The second idempotent \(Q=P+N\) has the same diagonal blocks in this order and hence the same rank. This proves every asserted zero fiber, including all unequal ranks, and completes the proof. The formula also covers the boundary \(r=0\) (arbitrary idempotents with \(N=0\)) and \(s=0\) (maximal-rank square-zero targets).

## Verification
The accompanying standalone Python script `squarezero_idempotent_sum_verify.py` directly enumerates matrices over \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\), using polynomial-basis field arithmetic. It tests \(P^2=P\) and \((P+N)^2=P+N\) by literal multiplication, determines matrix ranks by independent Gaussian elimination, and compares complete rank-profile dictionaries against the formula. The test families are \((n,r)=(2,0),(2,1)\) for all three fields; \((3,0),(3,1)\) over \(\mathbb F_2,\mathbb F_4\); and \((4,0),(4,1),(4,2)\) over \(\mathbb F_2\). The embedded log records all checked cases and `ALL_SQUAREZERO_IDEMPOTENT_SUM_FIBERS_PASS`. These finite computations check the implementation and sample boundary cases; the proof establishes the unrestricted result.

## Relationship to prior work
The fundamental existence/classification problem for sums of two idempotents was solved over arbitrary fields by de Seguins Pazzis (arXiv:0907.4436, first publicly posted July 25, 2009). In particular, his Theorem 5 addresses characteristic two and the constraints on Jordan blocks, but is a **yes/no criterion** rather than a count of prescribed-target witnesses or their common ranks. The related arXiv:0907.5360 studies minimal numbers of idempotent summands. Xu's work (doi:10.1080/03081087.2014.966646) characterizes when a linear combination of two idempotents is square-zero, but the accessible abstract does not resolve the present finite-field enumeration. For a nonzero rank-one nilpotent target, the rank-one-summand subcase agrees with the previously documented \(2q^{n-1}\) formula; the present theorem additionally gives every higher-rank summand fiber and every square-zero target rank. Historical priority is provisional, particularly where full relevant texts could not be examined.

## Limitations
The formula is specific to characteristic two, to square-zero targets, and to ordered decompositions into exactly two unrestricted idempotents. It does not address general prescribed matrices, odd characteristics, conjugacy classes of witnesses, or higher-order nilpotent targets. An inaccessible plausible structural characterization and possible broader counting frameworks present residual historical-priority risk. No independent audit or claim of exhaustive literature coverage is made.

## References
1. Clément de Seguins Pazzis, *On linear combinations of two idempotent matrices over an arbitrary field*, arXiv:0907.4436 (first posted July 25, 2009). https://arxiv.org/abs/0907.4436
2. Clément de Seguins Pazzis, *On sums of idempotent matrices over a field of positive characteristic*, arXiv:0907.5360 (2009). https://arxiv.org/abs/0907.5360
3. Chuang Xu, *On the idempotency, involution and nilpotency of a linear combination of two matrices*, Linear and Multilinear Algebra 63 (2015), DOI:10.1080/03081087.2014.966646. https://doi.org/10.1080/03081087.2014.966646
