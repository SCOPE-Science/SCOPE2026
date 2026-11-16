# The sharp three-edge Walsh-cancellation cutoff for spanning trees of Boolean hypercubes

## Finding

For an integer \(d\ge2\), let \(Q_d\) be the graph whose vertices are binary words of length \(d\) and whose edges change exactly one bit. Let \(\mathcal T_d\) denote the family of all spanning-tree edge-incidence vectors in the additive group \(G_d=\mathbb F_2^{E(Q_d)}\). For every set \(F\subseteq E(Q_d)\), form the **unnormalized** Walsh coefficient
\[
W_d(F)=\sum_{T\in\mathcal T_d}(-1)^{|F\cap T|}.
\]

**Theorem.** The number of edge supports \(F\) for which \(W_d(F)=0\), classified by \(|F|=1,2,3\), is exactly:

| Dimension | Singleton zeros | Pair zeros | Triple zeros |
|---|---:|---:|---:|
| \(d=2\) | 0 | 6 | 0 |
| \(d=3\) | 0 | 6 | 20 |
| \(d=4\) | 0 | 208 | 832 |
| Every \(d\ge5\) | 0 | 0 | 0 |

Thus the three-edge cancellation phenomenon occurs in dimensions three and four but **never** in any dimension at least five. This is a sharp dimension cutoff for the initial three Walsh support levels, not a claim of invertibility of the full spanning-tree convolution.

## Assumptions and scope

Every spanning tree is counted once and all graph edges have unit conductance. Edge supports consist of **distinct undirected edges**, but an arbitrary fixed edge orientation is used for transfer-current matrices. Let \(m_d=d2^{d-1}\). The assertions concern all \(\binom{m_d}{k}\) supports of size \(k\in\{1,2,3\}\), not merely symmetry representatives. There is no assertion about support sizes four or larger. Counting convolution by \(\mathbf1_{\mathcal T_d}\) has eigenvalues \(W_d(F)\) under the unnormalized Walsh transform.

## Proof

**1. Exact transfer-current reduction.** Orient the edge changing coordinate \(i\) as \((u,u\oplus e_i)\), with the \(i\)-th bit of \(u\) equal to zero. Write \(b_e\) for the incidence vector of oriented edge \(e\), \(L\) for the cube Laplacian, and \(K_{ef}=b_e^{\mathsf T}L^+b_f\). The established transfer-current theorem implies the polynomial identity
\[
\mathbb E\prod_{e\in F}(1-2\mathbf1_{\{e\in T\}})=\det(I-2K_F),
\]
where \(T\) is a uniform spanning tree and \(K_F\) is the principal submatrix indexed by \(F\). Consequently
\[
W_d(F)=\tau_d\det(I-2K_F),\qquad \tau_d=|\mathcal T_d|>0.
\]
For the characters \(\chi_S(u)=(-1)^{\sum_{i\in S}u_i}\), the cube Laplacian has eigenvalue \(2|S|\). Thus, for edges \(e=(u,u\oplus e_i)\) and \(f=(v,v\oplus e_j)\),
\[
K_{ef}=2^{1-d}\sum_{\substack{\varnothing\ne S\subseteq[d]\\i,j\in S}}\frac{(-1)^{\sum_{a\in S}(u_a+v_a)}}{|S|}.
\]
This formula is entirely rational. Choose \(D_d=2^{d-1}\operatorname{lcm}(1,2,\ldots,d)\). Then \(H_d=D_d(I-2K)\) is an **integer** matrix. Since \(\tau_d>0\),
\[
W_d(F)=0\quad\Longleftrightarrow\quad\det((H_d)_F)=0.
\]
For one edge, this is a diagonal entry. For two edges with diagonal entries \(a,b\) and off-diagonal entry \(x\), it is \(ab-x^2\). For three edges, writing the diagonal \(a,b,c\) and off-diagonal entries \(x,y,z\), it is
\[
abc+2xyz-az^2-by^2-cx^2.
\]
These closed integer expressions are the basis of the finite portion of the proof.

**2. Exhaustive finite certificate through dimension seven.** The attached `verify_low_support.py` constructs \(H_d\) directly from the displayed character sum using Python arbitrary-precision integers. For each \(d=2,3,4,5,6,7\), it checks **every** singleton, unordered edge pair, and unordered three-edge set by the respective exact determinant expression. The output table is exactly the one above. The largest case has \(448\) edges and inspects all \(\binom{448}{3}=14,885,696\) triples, with no random sampling or floating-point tests. The code includes hard assertions on every stated count; the loops are complete by standard combination iteration.

**3. Infinite tail by strict spectral dominance.** Every diagonal entry of \(K\) is
\[
p_d=\frac{2^d-1}{d2^{d-1}}.
\]
For distinct perpendicular edges, their absolute transfer current is bounded by
\[
B_d=2^{1-d}\int_0^1t(1+t)^{d-2}\,dt.
\]
For distinct parallel edges the corresponding bound is
\[
A_d=2^{1-d}\int_0^1(1-t)(1+t)^{d-2}\,dt.
\]
Indeed, the exact integral expressions for separated edges insert nonnegative factors \(((1-t)/(1+t))^r\), each at most one. Moreover \(A_d\le B_d\) for \(d\ge2\): after removing the common factor, this is \(\int_0^1(2t-1)(1+t)^{d-2}\,dt\ge0\), by monotonicity of the increasing weight \((1+t)^{d-2}\) and the zero mean of \(2t-1\). Therefore \(|K_{ef}|\le B_d\) for all distinct edges. Both \(p_d\) and \(B_d=\tfrac12\int_0^1t((1+t)/2)^{d-2}\,dt\) decrease with dimension. Direct rational integration gives
\[
p_8=\frac{255}{1024},\qquad B_8=\frac{769}{7168},\qquad p_8+2B_8=\frac{3323}{7168}<\frac12.
\]
For every \(d\ge8\) and every set of at most three edges, the symmetric matrix \(K_F\) has diagonal \(p_d\), with the sum of absolute off-diagonal entries of each row at most \(2B_d\). Gershgorin's bound places every eigenvalue of \(K_F\) strictly below \(1/2\). Thus \(I-2K_F\) is positive definite, so its determinant is strictly positive. Combining this with the exact finite certificate proves the theorem for all dimensions.

## Verification

Run `python3 verify_low_support.py` and `python3 verify_matrix_tree.py` in the same directory (only the Python 3 standard library is required). The first program checks every candidate at dimensions \(2\) through \(7\), including \(14,885,696\) distinct triples at dimension seven, and verifies the exact rational tail bound. The second calculates signed weighted Laplacian cofactors **independently of the transfer-current implementation** for all 6+4 configurations at dimension two, 66+220 at dimension three, 496+4960 at dimension four, and 319 representative triples at dimension five. Both checkers have been executed from the packaged source with matching results. This is exact finite arithmetic and a symbolic infinite-tail argument, not finite extrapolation or independent external certification.

## Relationship to prior work

Burton–Pemantle developed the general transfer-current determinant for arbitrary edge inclusion events; it is a premise here, not a new result. Martin–Reiner and Bernardi studied hypercube spanning-tree enumerators and weighted direction statistics. A separately published hypercube edge-covariance study gives exact **pairwise** transfer currents and spatial asymptotics, but explicitly does not address higher-order correlations. The theorem above adds the first complete three-edge Walsh-cancellation classification and the sharp nonvanishing cutoff at dimension five. The presence of an existing formula for the transfer-current matrix means the conclusion is computable in principle; neither that formula nor its pairwise evaluation by itself supplies the exhaustive three-edge zero classification or the infinite-dimensional positivity cutoff.

## Limitations

No assertion is made about all Walsh frequencies, total convolution rank, larger support sizes, or other graph families. The dimension-three and dimension-four counts use exhaustive exact computational certificates, not a short uniform orbit formula. The proof contains a deterministic finite enumeration of moderate size, independently cross-checked on the smaller dimensions; an unindexed historical signed-tree table or an unstated consequence of a specialized prior theorem remains an originality risk. The work has not undergone independent mathematical audit.

## References

1. J. L. Martin and V. Reiner, *Factorizations of some weighted spanning tree enumerators*, first public version February 18, 2003, https://arxiv.org/abs/math/0302213 .
2. R. Burton and R. Pemantle, *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances*, Annals of Probability (1993), lawful public preprint April 2, 2004, https://arxiv.org/abs/math/0404048 .
3. O. Bernardi, *On the spanning trees of the hypercube and other products of graphs*, https://arxiv.org/abs/1207.0896 .
4. C. Tuffley, *Counting the spanning trees of the 3-cube using edge slides*, https://arxiv.org/abs/1109.6393 .
5. *The half-cube spatial crossover for edge correlations in a uniform hypercube spanning tree*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-half-cube-spatial-crossover-for-edge-correlations-in-a-unifo--4ff8e7482039 .
