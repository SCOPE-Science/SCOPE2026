# Seven-periodic Walsh invertibility and sharp multiplier gaps for squared-path independent sets

## Finding
Let \(P_n^2\) be the square of the path on \(n\geq1\) labeled vertices, and let \(A_n\subseteq\mathbb F_2^n\) consist of the incidence vectors of all its independent vertex sets, including the empty set. Define the unnormalized Walsh multiplier
\[
W_n(\omega)=\sum_{x\in A_n}(-1)^{\langle\omega,x\rangle},\qquad\omega\in\mathbb F_2^n.
\]
Then
\[
\boxed{\exists\omega:\ W_n(\omega)=0\quad\Longleftrightarrow\quad n\bmod7\in\{1,3,4\}.}
\]
At every length, the exact smallest **positive** absolute Walsh multiplier is
\[
\boxed{\min_{\omega:W_n(\omega)\ne0}|W_n(\omega)|=
\begin{cases}2,&n\bmod7\in\{1,3,4\},\\1,&n\bmod7\in\{0,2,5,6\}.\end{cases}}
\]
For \(n=7k+r\) with \(k\ge0\) and \(r\in\{1,3,4\}\), the number of vanishing Walsh coefficients is at least \(c_r32^k\), with \(c_1=1\), \(c_3=3\), and \(c_4=6\).

If \(C_n\) is unnormalized convolution by \(\mathbf1_{A_n}\) on \(\ell^2(\mathbb F_2^n)\), then it is invertible exactly for \(n\bmod7\in\{0,2,5,6\}\), with exact inverse norm \(\|C_n^{-1}\|_{2\to2}=1\). For the other three residue classes its kernel has dimension at least \(c_r32^k\) and its Moore–Penrose pseudoinverse has exact norm \(\|C_n^\dagger\|_{2\to2}=1/2\).

## Assumptions and scope
The path has vertices \(1,\ldots,n\); two distinct vertices are adjacent in \(P_n^2\) exactly when their indices differ by at most two. All Fourier transforms are **unnormalized** sums over the binary additive group. Fourier characters are \((-1)^{\langle\omega,x\rangle}\), and convolution uses the counting-measure sum. A positive multiplier means a strictly positive absolute value, excluding any Fourier zero. No assertion about exact total zero multiplicities is made.

## Proof
Write \(s_j=(-1)^{\omega_j}\). For each sign prefix, define \(w_m\) to be the signed sum over independent sets in its first \(m\) positions. Set \(w_{-2}=w_{-1}=w_0=1\), a convention appropriate to empty truncated prefixes. Partitioning independent sets according to whether they contain the final vertex gives the exact recurrence, for all \(m\ge1\),
\[
w_m=w_{m-1}+s_mw_{m-3}.
\]
Indeed, excluding the last vertex leaves the first \(m-1\) positions, whereas including it forbids the preceding two and leaves the first \(m-3\) positions. Thus \(W_n(\omega)=w_n\).

First, all Walsh coefficients at a fixed length have the same parity, since \(W_n(\omega)\equiv|A_n|\pmod2\). Let \(a_m=|A_m|\). It obeys the above recurrence with every sign positive. Its first seven parity values, at \(m=0,\ldots,6\), are \((1,0,1,0,0,1,1)\). The recurrence companion matrix over \(\mathbb F_2\) is
\[
T=\begin{pmatrix}1&0&1\\1&0&0\\0&1&0\end{pmatrix},\qquad T^7=I.
\]
Consequently \(a_m\) is odd exactly for \(m\bmod7\in\{0,2,5,6\}\). At those lengths no Walsh coefficient can vanish, and every nonzero coefficient has absolute value at least one. At the three other residues every Walsh coefficient is even, so every nonzero coefficient has absolute value at least two.

The key **seven-sign extension identity** is stronger than parity. For any current prefix of length \(m\), append seven independent signs \(t_1,\ldots,t_7\) satisfying
\[
t_6=-t_5,\qquad t_7=-1,
\]
with the first five signs arbitrary. Then
\[
\boxed{w_{m+7}=-t_3t_5w_m.}
\]
To prove it, use the recurrence, read backward from the appended end:
\[
\begin{aligned}
w_{m+7}&=w_{m+6}-w_{m+4}\\
&=w_{m+5}-t_5w_{m+3}-w_{m+4}\\
&=t_5(w_{m+2}-w_{m+3})=-t_5t_3w_m.
\end{aligned}
\]
This identity holds independently of the preceding signs. There are exactly \(2^5=32\) distinct allowed seven-sign blocks; each preserves the absolute value of \(w_m\). In particular, concatenating any \(k\) such blocks preserves zeros and absolute minima and gives \(32^k\) distinct suffixes.

For completeness, the following short sign words supply all necessary initial values. Here \(+\) denotes sign \(+1\), \(-\) denotes \(-1\), and the empty word has value one.

| Residue \(r\) | Base word with minimum nonzero magnitude | Signed value | Zero word where applicable |
|:--:|:--|--:|:--|
| 0 | empty word | 1 | — |
| 1 | \(+\) | 2 | \(-\) |
| 2 | \(+-\) | 1 | — |
| 3 | \(++-\) | 2 | \(+--\) |
| 4 | \(+++-\) | 2 | \(++--\) |
| 5 | \(+++--\) | −1 | — |
| 6 | \(++++--\) | −1 | — |

All values follow by at most six applications of the recurrence. Append \(k\) admissible blocks to the base word for \(n=7k+r\); for residue zero and \(n\ge1\), take \(k\ge1\). This proves sharpness of both parity lower bounds and constructs a zero at every length in the three singular residue classes. At base lengths one, three and four there are respectively one, three and six zero sign words, by direct enumeration of respectively two, eight and sixteen sign assignments. Each extends in \(32^k\) distinct ways, proving the kernel lower bounds.

Finally, Walsh characters diagonalize convolution on the finite abelian group, with eigenvalues exactly \(W_n(\omega)\). The stated invertibility, spectral inverse and pseudoinverse norms, and kernel-dimension bounds therefore follow from the established multiplier classification.

## Verification
The reproducible standalone Python script `check_walsh_path_square.py` has no third-party dependencies. Run `python3 check_walsh_path_square.py` in the directory containing this document. It checks all 32 admissible seven-sign matrices, independently compares the signed recurrence with a direct independent-set sum for every sign vector through length ten, and computes complete fast Walsh transforms through length sixteen (131,070 frequency evaluations across those dimensions). It checks exact minimum absolute nonzero values and Fourier-zero existence, every one of \(32^2\) two-block null-frequency extensions from each base singular residue, explicit large-length witnesses through length 201, and parity through length 1000. The recorded check output is reproduced in `VERIFICATION.md`. These computations are finite checks; the all-length result follows from the proof above.

## Relationship to prior work
Codara and D'Antona, arXiv:1210.5561v1 (19 October 2012), define independent subsets of powers of paths and derive the ordinary, all-positive independent-set recurrence and associated Hasse-diagram counts. The later arXiv:1410.4080 develops this enumerative setting. Scott and Sokal, arXiv:cond-mat/0309352 (15 September 2003), provide the general multivariate hard-core independent-set polynomial and nonvanishing theory, primarily on fugacity polydiscs. The present Walsh multipliers are that polynomial at all independent sign assignments \(s_j=\pm1\). The known ordinary recurrence explains the modulo-seven parity obstruction, but not the existence of sign cancellations in every even-cardinality case, the seven-block identity, the sharp nonzero gap, or the growing explicit null families. A general result about **restricting** a Fourier matrix to independent-set index sets concerns a different linear operator from full-group convolution by the independent-set indicator.

## Limitations
The statement covers path squares, not higher powers or cycle squares. The lower bound on singular Fourier multiplicity need not be sharp, and no complete spectrum histogram or endpoint \(\ell^1\) inverse norm is determined. Historical priority is assessed only against the explicitly inspected literature and searches; an equivalent earlier result under hard-core partition-function terminology may exist. The mathematical argument and code underwent self-review only, not independent external validation.

## References
1. P. Codara and O. M. D'Antona, “On the independent subsets of powers of paths and cycles,” arXiv:1210.5561v1, publicly submitted 2012-10-19, https://arxiv.org/html/1210.5561v1.
2. P. Codara and O. M. D'Antona, “Generalized Fibonacci and Lucas cubes arising from powers of paths and cycles,” arXiv:1410.4080v1, publicly submitted 2014-10-15, https://ar5iv.labs.arxiv.org/html/1410.4080.
3. A. D. Scott and A. D. Sokal, “The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma,” arXiv:cond-mat/0309352v1, publicly submitted 2003-09-15, https://arxiv.org/html/cond-mat/0309352v2.
