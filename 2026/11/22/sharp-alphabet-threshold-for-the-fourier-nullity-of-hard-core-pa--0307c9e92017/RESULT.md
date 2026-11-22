# Sharp alphabet threshold for the Fourier nullity of hard-core path words

## Finding
Let \(H\) be an arbitrary finite abelian group of order \(q\ge2\), and let \(n\ge1\). Inside \(H^n\), put \(E_n(H)=\{x: x_i\ne0\text{ and }x_j\ne0\text{ never occur at adjacent positions}\}\). Let \(T_n f=\mathbf1_{E_n(H)}*f\) be **unnormalized** group convolution, acting on complex-valued functions on \(H^n\).

If \(n\not\equiv1\pmod3\), then \(T_n\) is invertible for every \(q\ge2\). If \(n=3k+1\), \(k\ge0\), and \(q\ge k+2\), then a character \(\chi=(\chi_1,\ldots,\chi_n)\) has zero multiplier **if and only if** each coordinate character \(\chi_1,\chi_4,\ldots,\chi_{3k+1}\) is nontrivial. In particular,
\[
\operatorname{nullity}T_{3k+1}=q^{2k}(q-1)^{k+1},\qquad
\operatorname{rank}T_{3k+1}=q^{3k+1}-q^{2k}(q-1)^{k+1}.
\]
The fraction of zero eigenvalues is \((1-1/q)^{k+1}\). The alphabet bound is **sharp** for every \(k\ge1\): at \(q=k+1\), additional zeros occur even with a trivial coordinate character at the first position. At the sharp permitted alphabet \(q=k+2\), the null fraction tends to \(e^{-1}\) as \(k\to\infty\).

## Assumptions and scope
The group \(H\) is finite and abelian; its internal structure does not matter, only its order. Indices are one-based. The empty-support word belongs to \(E_n(H)\). The theorem concerns the exact kernel of a translation-invariant convolution operator on all functions \(H^n\); it does **not** concern adjacency spectra of the induced Hamming graph or restricted Fourier interpolation matrices. Outside the stated high-alphabet regime, the recurrence below is valid but the complete nullity formula is not claimed.

## Proof
For a character \(\chi\) of \(H^n\), character orthogonality gives
\[
a_i=\sum_{h\in H\setminus\{0\}}\chi_i(h)=\begin{cases}q-1,&\chi_i\text{ trivial},\\-1,&\chi_i\text{ nontrivial}.\end{cases}
\]
Summing independently over the occupied positions of a path independent set shows that its unnormalized Fourier multiplier \(P_n\) is determined by \(P_{-1}=P_0=1\) and
\[
P_i=P_{i-1}+a_iP_{i-2}\quad(1\le i\le n).
\]
Regard each \(a_i\) as an integer polynomial in the indeterminate \(Q\), equal to \(Q-1\) for trivial \(\chi_i\) and \(-1\) otherwise. Modulo \(Q\), each \(a_i\equiv-1\); hence \(P_i(Q)\) reduces to \(r_i=r_{i-1}-r_{i-2}\), with \(r_{-1}=r_0=1\). The sequence is \(1,0,-1,-1,0,1\) periodically from \(i=0\) with period six. Thus \(P_n(q)\equiv\pm1\pmod q\) if \(n\not\equiv1\pmod3\), proving invertibility in those lengths.

Now let \(n=3k+1\). The constant coefficient of \(P_n(Q)\) is zero. Let \(U=\{i:\chi_i\text{ is trivial}\}\). To calculate the coefficient of \(Q\), expand the multiaffine path independence polynomial at all vertex activities \(-1\). Differentiating with respect to the activity of vertex \(j\) forces that vertex to be occupied, removing its neighbors, so its derivative is the product of signed independence counts for path segments of lengths \(j-2\) and \(n-j-1\). For a segment of length \(m\ge0\), this count is \(r_m\), and for the empty boundary segment indexed by \(-1\) it is \(r_{-1}=1\). Inspection of the above six-periodic sequence shows that the derivative vanishes unless \(j=3h+1\), with \(0\le h\le k\); in that case it equals \((-1)^h(-1)^{k-h}=(-1)^k\). Therefore
\[
P_{3k+1}(Q)=Q R(Q),\qquad R(0)=(-1)^k t,
\]
where \(t=|U\cap\{1,4,\ldots,3k+1\}|\), so \(0\le t\le k+1\).

If an integer \(q\ge k+2\) satisfies \(P_n(q)=0\), then \(R(q)=0\). Since \(R\) has integer coefficients, the polynomial remainder theorem gives \(q\mid R(0)\). Consequently \(q\mid t\), and \(0\le t\le k+1<q\) implies \(t=0\). All designated characters must be nontrivial.

Conversely, assume \(a_{3h+1}=-1\) for every \(0\le h\le k\). We have \(P_1=P_0-P_{-1}=0\). Whenever \(P_{3h+1}=0\), the recurrence gives \(P_{3h+2}=a_{3h+2}P_{3h}\), \(P_{3h+3}=P_{3h+2}\), and \(P_{3h+4}=P_{3h+3}-P_{3h+2}=0\), independently of the activities in the two intermediate positions. Induction proves \(P_{3k+1}=0\). Exactly \(q-1\) characters of \(H\) are nontrivial and exactly \(q\) choices exist at an unrestricted site. There are \(k+1\) designated and \(2k\) unrestricted sites; Fourier diagonalization yields the asserted rank and nullity.

For sharpness at \(q=k+1\) with \(k\ge1\), prescribe nontrivial coordinate characters at the positions \(S_k=\{2,3\}\cup\{6,9,\ldots,3k\}\), and trivial ones elsewhere. Such choices exist in every abelian group of order at least two; in particular the first coordinate character is trivial. With \(x=Q-1\), the recurrence has activity pattern \((x,-1,-1),(x,x,-1),\ldots,(x,x,-1),x\). After its first triple \((P_3,P_2)=(-1,x)\); each subsequent triple sends the state \((u,v)\) to \((xu,(1+x)u+xv)\). Direct induction then gives
\[
P_{3k+1}(Q)=Q(Q-k-1)(Q-1)^{k-1}.
\]
It vanishes at \(Q=k+1\), while the prescribed first coordinate is trivial, proving that the uniform classification cannot be extended to that alphabet. The limit follows from \((1-1/(k+2))^{k+1}\to e^{-1}\).

## Verification
The standalone \(\texttt{verify.py}\) compares every frequency zero-pattern with the theorem through length 16 for selected alphabet sizes at or above the threshold, with exact integer arithmetic. It also verifies the exceptional sharpness construction through \(k=7\), and independently compares direct cyclic-group character sums at small widths. These finite checks corroborate, but are not substitutes for, the unrestricted algebraic proof above. Reproduce with \(\texttt{python3 verify.py}\); only the Python standard library is needed.

## Relationship to prior work
The path independent-set encoding generalizes Fibonacci strings; Codara and D'Antona [1] study the cardinalities and Hasse-diagram edge counts of these independent sets. Azarija et al. [2] treat generalized Fibonacci-cube isomorphisms and forbidden patterns. Hare and Saunders [3] analyze binary random Fibonacci recurrences, related to the \(q=2\) signed case. None of these inspected statements supplies the sharp high-alphabet \(q\ge k+2\) Fourier-nullity formula or the character support classification. The present statement is about counting convolution over *all finite abelian alphabets*, not the adjacency spectrum or combinatorial size of the Fibonacci cube.

## Limitations
There is no complete classification of exceptional Fourier zeros for \(2\le q\le k+1\); the given boundary example only proves sharpness of the uniform theorem. No claim is made for cycles, general graphs, or nonabelian alphabets. The historical comparison is bounded and may miss an equivalent indexed under signed hard-core partition functions or transfer matrices; no independent audit has been performed.

## References
1. P. Codara and O. M. D'Antona, *On the independent subsets of powers of paths and cycles*, original preprint posted 2012-10-19, https://arxiv.org/abs/1210.5561.
2. J. Azarija, S. Klavžar, J. Lee, J. Pantone, Y. Rho, *On Isomorphism Classes of Generalized Fibonacci Cubes*, first posted 2014-02-25, https://arxiv.org/abs/1402.6377.
3. K. G. Hare and J. C. Saunders, *On (a,b) Pairs in Random Fibonacci Sequences*, first posted 2016-08-11, https://arxiv.org/abs/1608.03522.
