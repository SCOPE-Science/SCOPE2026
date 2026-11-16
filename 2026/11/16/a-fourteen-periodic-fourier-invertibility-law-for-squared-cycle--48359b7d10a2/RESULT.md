# A fourteen-periodic Fourier invertibility law for squared-cycle independent sets

## Finding
Let \(n\ge3\), and let \(C_n^2\) be the distance-two power of the ordinary \(n\)-cycle: vertices at cyclic distance one or two are adjacent. Write \(A_n\subseteq\mathbb F_2^n\) for the incidence vectors of **all** independent vertex sets, including the empty set. Define the unnormalized Walsh transform
\[
W_n(\omega)=\sum_{x\in A_n}(-1)^{\langle\omega,x\rangle},\qquad \omega\in\mathbb F_2^n.
\]
Then the complete Fourier-zero classification is
\[
\exists\omega\;W_n(\omega)=0\quad\Longleftrightarrow\quad n\bmod14\in\{3,5,10,12,13\}.
\]
The exact least positive multiplier magnitude is
\[
\delta_n:=\min_{\omega:W_n(\omega)\ne0}|W_n(\omega)|=
\begin{cases}
4,&n\equiv13\pmod{14},\\
2,&n\bmod14\in\{3,5,6,10,12\},\\
1,&\text{otherwise}.
\end{cases}
\]
In particular, the even-cardinality class \(n\equiv6\pmod{14}\) is **zero-free**, with \(W_n(\omega)\equiv2\pmod4\) for every frequency, while \(W_n(\omega)\equiv0\pmod4\) for all frequencies when \(n\equiv13\pmod{14}\). If \(n=14k+r\) with \(r\in\{3,5,10,12,13\}\) and \(k\ge0\), there are at least \(14^k\) distinct zero frequencies.

For unnormalized convolution by \(\mathbf1_{A_n}\) on the binary group, invertibility holds precisely in the nine remaining residue classes. The \(\ell^2\) inverse norm when invertible, or Moore--Penrose pseudoinverse norm when singular, equals \(\delta_n^{-1}\).

## Assumptions and scope
All vertices are distinctly labelled by \(0,1,\ldots,n-1\), with indices interpreted modulo \(n\). In \(C_3^2\), \(C_4^2\), and \(C_5^2\), repeated cyclic edges are identified: these graphs are complete. Fourier coefficients are **unnormalized integer** character sums. The operator acts on all \(2^n\) functions with the counting-measure \(\ell^2\)-norm.

## Proof
**1. Exact transfer formula.** Put \(t_j=(-1)^{\omega_j}\) and
\[
T(t)=\begin{pmatrix}1&t&0\\0&0&1\\1&0&0\end{pmatrix}.
\]
Its rows and columns are indexed by the last-two-bit states \(00,01,10\). A transition from \(00\) to \(01\) inserts an occupied vertex of weight \(t\); all other allowed transitions insert an unoccupied vertex of weight one. Closed walks of length \(n\) thus correspond bijectively to cyclic binary words with no two ones separated by one or two cyclic steps. Consequently, for every \(n\ge3\),
\[
W_n(\omega)=\operatorname{tr}\bigl(T(t_0)T(t_1)\cdots T(t_{n-1})\bigr).
\]
The formula includes the complete-graph small cases \(n=3,4,5\).

**2. Parity and the exceptional modulo-four obstruction.** Set \(Q=T(1)\). Direct multiplication gives \(Q^7\equiv I_3\pmod2\) and \(Q^{14}\equiv I_3\pmod4\). Thus the unweighted number \(L_n=|A_n|=\operatorname{tr}(Q^n)\) is odd exactly when \(n\bmod7\notin\{3,5,6\}\); in those classes no Walsh coefficient can vanish. The values \(L_6=10\) and \(L_{13}=144\) imply \(L_n\equiv2\pmod4\) when \(n\equiv6\pmod{14}\) and \(L_n\equiv0\pmod4\) when \(n\equiv13\pmod{14}\).

For \(n\ge5\), the number of independent sets containing any specified vertex equals \(a_{n-5}\), where \(a_m\) counts independent sets of the square of a path with \(m\) vertices. The elementary initial values and recurrence are \(a_0=1\), \(a_1=2\), \(a_2=3\), and \(a_m=a_{m-1}+a_{m-3}\) for \(m\ge3\). Its recurrence matrix has seventh power equal to the identity modulo two, and \(a_1\equiv0\pmod2\). Hence \(a_{n-5}\) is even whenever \(n\equiv6\pmod7\). If \(S=\{j:t_j=-1\}\), the congruence \((-1)^h\equiv1-2h\pmod4\) yields
\[
W_n(\omega)\equiv L_n-2|S|a_{n-5}\pmod4.
\]
This proves the two uniform modulo-four statements. In particular, every coefficient is nonzero for \(n\equiv6\pmod{14}\).

**3. Exact fourteen-step replication.** Multiplication of the seven transfer matrices for the sign word \((+,-,+,-,+,-,-)\) gives
\[
B=\begin{pmatrix}1&0&-2\\2&-1&-2\\0&0&-1\end{pmatrix},\qquad B^2=I_3.
\]
Thus appending that seven-letter word **twice** preserves every trace exactly, at every pre-existing sign word. There are in fact fourteen distinct seven-letter sign words whose transfer products square to the identity. They are (the symbols \(+\) and \(-\) stand for weights \(+1\) and \(-1\)):

`+-+-+--`, `+-+--+-`, `+--+-+-`, `+--+---`, `+---+--`, `-+-+-+-`, `-+-+--+`, `-+--+-+`, `-+--+--`, `-+---+-`, `--+-+-+`, `--+--+-`, `--+---+`, `---+--+`.

For every listed word \(s\), the fourteen-letter concatenation \(ss\) has transfer product \(I_3\). The 14 distinct choices in each appended block give \(14^k\) distinct extensions after \(k\) blocks. Each finite matrix identity is checked directly in `CHECK.py`; the finite list is explicit, not an assumption about all possible blocks.

**4. Complete seeds and sharp positive gaps.** For each row below, put negative weights at the displayed **zero-based vertex indices**, all other weights being \(+1\). The displayed exact integer is the resulting transfer trace. Here `zero` is a vanishing witness and `positive` attains the least possible positive magnitude. Base lengths \(n=3,4,\ldots,16\) represent all allowable residues modulo fourteen (residue classes one and two first occur at lengths 15 and 16).

| \(n\) | Zero witness negative indices | Positive witness negative indices | Its trace |
| --- | --- | --- | ---: |
| 3 | `0,1` | `0` | 2 |
| 4 | — | `0,1` | 1 |
| 5 | `0,1,2` | `0,1` | 2 |
| 6 | — | `0,1` | 2 |
| 7 | — | `0,1,3` | 1 |
| 8 | — | `0,1,3` | 1 |
| 9 | — | `0,2,4` | -1 |
| 10 | `0,2,4` | `0,1,2,5` | -2 |
| 11 | — | `0,2,4` | 1 |
| 12 | `0,2,4` | `0,1,2,5` | -2 |
| 13 | `0,2,4` | `0,1,2,5` | -4 |
| 14 | — | `0,2,4` | 1 |
| 15 | — | `0,2,4` | 1 |
| 16 | — | `0,2,4` | 1 |

The zero witness at each of the five listed residues proves existence there for all larger lengths in that residue, by paragraph 3. For odd \(L_n\), a nonzero integer Walsh coefficient has absolute value at least one. For even \(L_n\), every coefficient is even, giving lower bound two away from zero. The modulo-four argument in paragraph 2 strengthens that lower bound to four when \(n\equiv13\pmod{14}\), and eliminates zeros for \(n\equiv6\pmod{14}\). The positive witness in each residue, extended by fourteen-letter identity blocks, attains the corresponding bound for every \(n\). This proves all assertions.

**5. Convolution norms.** Every Walsh character diagonalizes binary-group convolution by \(\mathbf1_{A_n}\), with eigenvalue \(W_n(\omega)\). For the counting-measure \(\ell^2\) norm, the nonzero singular values are the absolute eigenvalues, so the norm of the inverse (when defined) or of the Moore--Penrose pseudoinverse is exactly \(1/\delta_n\).

## Verification
The standalone, standard-library-only `CHECK.py` directly enumerates independent sets and independently compares their signed sums with transfer traces for all sign patterns through \(n=10\). It evaluates complete integer fast Walsh--Hadamard transforms for every \(3\le n\le16\), verifies all seed traces, checks the exact transfer and modular matrix identities, and enumerates all 128 seven-sign words, finding precisely fourteen involution blocks. Its success marker is `CYCLE_SQUARE_FOURIER_EXACT_PASS`. These finite checks corroborate explicit algebraic proof steps; they are not a substitute for the all-length arguments above.

## Relationship to prior work
Adamaszek, *Splittings of independence complexes and the powers of cycles* (first posted 2011-06-30, arXiv:1106.6250), studies the **same distance-power graph family** and derives homotopy splittings of independence complexes. The present theorem studies signed sums over all faces and Fourier-convolution invertibility, which neither follows from nor is stated in those homotopy results. Closely related Fourier classifications of ordinary cycles, squared paths and cyclic maximal independent sets concern distinct incidence families and do not determine this classification. A separately published classification of regular subsets of \(C_n^2\) studies two-cell equitable partitions, a small constrained subfamily of vertex subsets, rather than the signed Fourier transform of the entire independent-set family. Separately, the title *Maximum Independent Sets in Certain Powers of Odd Cycles* (Bohman--Holzman--Natarajan, 2009) concerns **graph strong products** and maximal-cardinality configurations, not distance-two cycle powers and all independent-set character sums. Traditional weighted independence-polynomial transfer methods underlie the method; no uniqueness-of-discovery assertion is made.

## Limitations
The theorem covers unweighted indicators of independent sets of exactly the distance-two powers of single cycles. It does not count all zero frequencies exactly, address higher distance powers, provide endpoint \(\ell^1\) inverse norms, or certify historical novelty beyond the inspected literature. The \(14^k\) estimate is a lower bound, not an exact zero count. Independent mathematical audit has not been performed.

## References
- M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250, initially posted June 30, 2011, https://arxiv.org/abs/1106.6250.
- T. Bohman, R. Holzman, and V. Natarajan, *Maximum Independent Sets in Certain Powers of Odd Cycles*, Electronic Journal of Combinatorics 16 (2009), N26, https://doi.org/10.37236/264. (A different graph-power operation.)
