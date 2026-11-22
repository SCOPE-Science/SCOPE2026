# Sharp three-block Kaczmarz designs on regular-simplex frames

## Finding
Let \(m\ge4\) and let \(a_1,\ldots,a_m\) be the unit normal vectors of the regular simplex in \(\mathbb R^{m-1}\), so that \(a_i^\mathsf T a_j=-1/(m-1)\) for distinct indices. Partition all \(m\) rows into exactly three nonempty blocks, and, independently at each step, select block \(j\) with a fixed probability \(p_j\ge0\), with \(\sum_j p_j=1\). For consistent equations, update by the exact orthogonal projection onto the selected block's simultaneous equations. The sharp worst-initial-error one-step expected squared-error reduction is
\[
\boxed{R_m^*=\frac{m}{3m-2}.}
\]
Every attaining partition, and no other partition, consists of one block of \(m-2\) rows and two singleton blocks. For such a partition the probabilities are uniquely \(m/(3m-2)\) on the large block and \((m-1)/(3m-2)\) on each singleton. There are \(\binom m2\) unlabeled-block optimal row partitions, each with one optimal probability assignment.

More finely, with \(s_j\) the three positive block sizes, the best reduction for each fixed size profile is exactly
\[
\begin{array}{c|c}
\text{number of singleton blocks}&\max_{p}\lambda_{\min}(\sum_jp_jP_j)\\\hline
2&\dfrac{m}{3m-2}\\
1&\dfrac{m+1}{3m+1}\\
0&\dfrac13
\end{array}
\]
where \(P_j\) denotes projection onto the span of rows in block \(j\). In the one-singleton case the unique optimal masses are \((m+1)/(3m+1)\) on each nonsingleton block and \((m-1)/(3m+1)\) on the singleton, irrespective of the two nonsingleton block sizes. In the no-singleton case each optimal mass is \(1/3\).

## Assumptions and scope
The row normals are a regular-simplex tight frame, not arbitrary equiangular rows. The linear equations are consistent; every block is imposed **exactly**, by its orthogonal projector. Blocks are disjoint, exhaustive, and nonempty, with exactly three blocks. The probabilities are fixed, independent between iterations, and nonnegative. A step has unit weight regardless of how many row equations the selected block contains. No assertion is made about wall-clock cost or flop-normalized efficiency, nor about multi-step optimality.

For an error vector \(e\), the projection update is \(e^+=(I-P_j)e\), hence
\[
\mathbb E\|e^+\|_2^2=\|e\|_2^2-e^\mathsf T\bigl(\sum_jp_jP_j\bigr)e.
\]
The exact worst-error reduction is the least eigenvalue on the \((m-1)\)-dimensional solution space.

## Proof
Identify the error space isometrically with \(H=\{x\in\mathbb R^m:\sum_i x_i=0\}\). The simplex rows are proportional to the centered coordinate vectors; multiplying rows by positive scalars does not affect block projections. For a block \(S\subsetneq[m]\) of size \(s\), orthogonality to all its rows in \(H\) means that all coordinates in \(S\) vanish. Thus the squared projection norm satisfies, for any \(x\in H\),
\[
\langle x,P_Sx\rangle=\sum_{i\in S}x_i^2+\frac{(\sum_{i\in S}x_i)^2}{m-s}.
\tag{1}
\]
Decompose \(H\) orthogonally into the internal zero-sum contrast spaces \(W_j\), of dimensions \(s_j-1\), together with the two-dimensional block-constant mean space \(U\). On \(W_j\), \(P_j\) is identity and the other two projectors vanish. Hence \(\sum_jp_jP_j\) has eigenvalue \(p_j\) with multiplicity \(s_j-1\). On \(U\), each \(P_j\) is rank one: writing \(h_j\) for the unit vector in \(U\) representing block \(j\), the restricted matrix is \(B=\sum_j p_j h_jh_j^\mathsf T\). Its trace is one, and, for the remaining index \(k\),
\[
1-\langle h_i,h_j\rangle^2=\frac{m s_k}{(m-s_i)(m-s_j)}.
\]
Consequently
\[
\det B=\sum_{i<j}\frac{m s_k}{(m-s_i)(m-s_j)}p_ip_j.
\tag{2}
\]
For a positive two-by-two matrix of trace one and a threshold \(0<t\le1/2\), its smallest eigenvalue is at least \(t\) exactly when its determinant is at least \(t(1-t)\).

**Two singleton blocks.** Let \(s_1=m-2\) and \(s_2=s_3=1\), and write \(x=p_1\). The internal contrasts yield \(R\le x\). The unit vector supported with opposite signs on the two singleton coordinates has zero projection onto the large block, and squared projections \(m/[2(m-1)]\) onto each singleton block. It gives
\[
R\le\frac{m(1-x)}{2(m-1)}.
\]
The maximum of the smaller of these two quantities is \(t_1=m/(3m-2)\), achieved only at \(x=t_1\). With \(p_2=p_3=(m-1)/(3m-2)\), (2) yields \(\det B=t_1(1-t_1)\), and the other mean eigenvalue is \(1-t_1>t_1\), so this upper bound is attained. Equality requires the singleton-difference unit vector, whose Rayleigh quotient then equals \(t_1\), to be an eigenvector. Its mixed matrix element with the remaining group-mean direction is a nonzero multiple of \(p_2-p_3\), forcing \(p_2=p_3\). All probabilities are unique.

**Exactly one singleton block.** Write \((s_1,s_2,s_3)=(a,b,1)\) with \(a,b\ge2\) and \(m=a+b+1\), and put \((p_1,p_2,p_3)=(x,y,1-x-y)\). The contrast eigenvalues imply \(R\le\min(x,y)\). Define
\[
A=\frac{m}{(a+1)(b+1)},\quad
B_0=\frac{mb}{(b+1)(m-1)},\quad
C_0=\frac{ma}{(a+1)(m-1)}.
\]
Equation (2) gives \(\det B=Axy+B_0x(1-x-y)+C_0y(1-x-y)=D(x,y)\). Algebra gives
\[
A-B_0-C_0=-\frac{2mab}{(a+1)(b+1)(m-1)}=-K,
\quad \frac K{B_0}=\frac{2a}{a+1}>1,\quad\frac K{C_0}=\frac{2b}{b+1}>1.
\]
Thus for \(x,y\ge1/3\), both partial derivatives \(\partial_xD=B_0(1-2x)-Ky\) and \(\partial_yD=C_0(1-2y)-Kx\) are strictly negative. Put \(t_2=(m+1)/(3m+1)>1/3\). Direct substitution gives \(D(t_2,t_2)=t_2(1-t_2)\). If \(R>t_2\), then \(x,y>t_2\), so strict decrease gives \(\det B<t_2(1-t_2)\), contradicting \(\lambda_{\min}(B)>t_2\). If \(R=t_2\), the same argument forces \(x=y=t_2\). Conversely these probabilities give contrast eigenvalues \(t_2\), and the group-mean eigenvalues \(t_2,1-t_2\). Thus \(t_2\) is attained uniquely for every \(a,b\).

**No singleton block.** All three internal contrast spaces are nonzero, so \(R\le\min(p_1,p_2,p_3)\le1/3\). With each \(p_j=1/3\), the contrast eigenvalues equal \(1/3\). On \(U\), the vectors \(h_j\) arise from the block indicator orthonormal basis by orthogonal projection to \(U\) followed by factors \((1-s_j/m)^{-1/2}\ge1\). Hence \(\sum_jh_jh_j^\mathsf T\succeq I_U\), so \(R=1/3\). The bound on the contrast eigenvalues forces all three probabilities to equal \(1/3\) at equality.

Finally \(t_1-t_2=2/[(3m-2)(3m+1)]>0\) and \(t_2>1/3\), which proves the global optimizer classification. Only the choice of two singleton indices varies; the number of such choices is \(\binom m2\).

## Verification
Run `python check.py` in this package with SymPy installed. It verifies the symbolic determinant contact identities and derivative constants, exact rational projector idempotence and full characteristic-polynomial decompositions for every unordered three-part size profile through eight rows, plus a sequence of strict exact rational gap checks. The proof above establishes the conclusions for **all** \(m\ge4\), independently of the finite checks.

## Relationship to prior work
Needell and Tropp (arXiv:1208.3805) formulate block randomized Kaczmarz with uniformly chosen row pavings and bound its expected convergence using paving constants. Needell, Zhao and Zouzias (arXiv:1403.4192) extend block methods to inconsistent least squares. Gower and Richtárik (arXiv:1506.03296, especially Section 5.1) formulate an optimization of discrete sampling probabilities via the minimum eigenvalue of the expected projection. The present result is the explicit joint **partition-and-probability** solution for the regular-simplex frame with exactly three nonempty blocks. The general spectral formulation and the importance of block pavings are not claimed new.

## Limitations
The result optimizes the sharp **one-step worst-case expected squared-error decrease**, not the realized contraction for each error, multi-step asymptotic exponent, computational cost, or approximate block solve. The largest block contains \(m-2\) equations and may be more expensive to implement than a balanced partition. The improvement over uniform three-block sampling is \(2/[3(3m-2)]\), decreasing as the frame grows. Independent audit and exhaustive publication-priority verification have not been performed; unindexed equivalent results remain possible.

## References
- D. Needell and J. A. Tropp, *Paved with Good Intentions: Analysis of a Randomized Block Kaczmarz Method*, arXiv:1208.3805, initially posted 2012-08-19. https://arxiv.org/abs/1208.3805
- D. Needell, R. Zhao and A. Zouzias, *Randomized Block Kaczmarz Method with Projection for Solving Least Squares*, arXiv:1403.4192. https://arxiv.org/abs/1403.4192
- R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296 (2015). https://arxiv.org/abs/1506.03296
