# Seven-step Fourier invertibility for binary words avoiding \(101\)

## Finding
For every integer \(n\ge1\), let \(F_n\subseteq\mathbb F_2^n\) consist of all length-\(n\) binary words having no consecutive factor \(101\). Define the unnormalized Walsh coefficients
\[
W_n(u)=\sum_{x\in F_n}(-1)^{\langle u,x\rangle},\qquad u\in\mathbb F_2^n,
\]
with the standard mod-two coordinate pairing. Let \(T_nf=\mathbf1_{F_n}*f\) denote counting convolution on the finite group \(\mathbb F_2^n\), with no factor of \(2^{-n}\) in the convolution.

**Theorem.** The following conditions are equivalent:

1. \(T_n\) is invertible on complex or real functions on \(\mathbb F_2^n\).
2. \(W_n(u)\ne0\) for every \(u\in\mathbb F_2^n\).
3. \(n\bmod7\in\{0,3,5,6\}\).

For every invertible length there is an explicit frequency \(u\) for which \(W_n(u)=1\). In particular,
\[
\min_{u\in\mathbb F_2^n}|W_n(u)|=1,
\qquad \|T_n^{-1}\|_{\ell^2\to\ell^2}=1.
\]
For every other length, an explicit frequency has \(W_n(u)=0\), so the convolution is singular. The result is for unrestricted length-\(n\) words: no prescribed weight, prefix-balance condition, or cyclic identification is assumed.

## Assumptions and scope
All words have ordered, labelled positions \(0,\ldots,n-1\). The forbidden factor occurs only at three consecutive ordinary positions, without wraparound. The singleton and two-coordinate cases are included. The Walsh transform is unnormalized, and the norm is for the usual counting-measure Hilbert norm on \(\mathbb F_2^n\). No assertion is made about exact nullity or the least nonzero multiplier in singular dimensions.

## Proof
Let \(e=(1,0,0)\) be a row vector and let \(\mathbf1=(1,1,1)^{\mathsf T}\). A three-state prefix automaton records respectively the empty suffix, the suffix \(1\), and the suffix \(10\) of a word already avoiding \(101\). A next bit \(1\) is forbidden only from the third state. For a bit whose Walsh sign on a \(1\) is \(s\in\{1,-1\}\), its signed transition matrix is
\[
M(s)=\begin{pmatrix}1&s&0\\0&s&1\\1&0&0\end{pmatrix}.
\]
Put
\[
A=M(1)=\begin{pmatrix}1&1&0\\0&1&1\\1&0&0\end{pmatrix},\qquad
B=M(-1)=\begin{pmatrix}1&-1&0\\0&-1&1\\1&0&0\end{pmatrix}.
\]
If the set of negative-sign positions is \(J\), form the ordered product of \(n\) matrices, using \(B\) at positions in \(J\) and \(A\) otherwise. Then the corresponding Walsh coefficient is exactly \(e(\prod M_i)\mathbf1\). Thus every displayed matrix product below represents an actual frequency, not a formal relaxation.

**Parity and necessity in the zero-free classes.** The number \(a_n=|F_n|=eA^n\mathbf1\), with \(a_0=1\), \(a_1=2\), \(a_2=4\), satisfies
\[
a_n=2a_{n-1}-a_{n-2}+a_{n-3}\quad(n\ge3),
\]
since the characteristic polynomial of \(A\) is \(\lambda^3-2\lambda^2+\lambda-1\). Direct multiplication gives \(A^7\equiv I\pmod2\), and the first seven cardinalities modulo two are \(1,0,0,1,0,1,1\) for indices \(0,\ldots,6\). Consequently \(a_n\) is odd exactly for \(n\bmod7\in\{0,3,5,6\}\). Since every Walsh coefficient is a sum of \(a_n\) signs, \(W_n(u)\equiv a_n\pmod2\). Hence **every** coefficient is nonzero in those four residue classes.

**Explicit resonance and sharpness.** Set \(C=BA^6\), \(D=A^6B\), \(L=eA\), \(R=BA\mathbf1\), and \(R'=A\mathbf1\). Direct integer multiplication gives
\[
C=\begin{pmatrix}3&4&2\\-2&-3&-2\\12&16&9\end{pmatrix},\quad
D=\begin{pmatrix}21&-28&16\\16&-21&12\\12&-16&9\end{pmatrix},
\]
\[
L=(1,1,0),\qquad R=(0,-1,2)^{\mathsf T},\qquad R'=(2,2,1)^{\mathsf T},
\]
and the **three invariant-vector identities**
\[
LC=L,\qquad CR=R,\qquad DR'=R'.
\]
Additional direct products have the values
\[
eB\mathbf1=0,\quad eBR'=0,\quad eBA^5R=0,\quad LBA^2\mathbf1=0,
\]
\[
eBA^2\mathbf1=1,\quad eBA^7R=1,\quad
LBA^j\mathbf1=1\quad(j\in\{3,4,5\}).
\]
These equalities give a uniform signed-word witness in every residue class. Writing \(n=7k+r\), the next table lists an ordered transition product and its exact Walsh value. Whenever \(k=0\) is not permitted, the short boundary length is stated separately.

| \(r\) | Range | Witness scalar | Value |
|---|---|---|---:|
| \(0\) | \(k\ge1\) | \(eAC^{k-1}BA^5\mathbf1\) | \(1\) |
| \(1\) | \(k=0\) | \(eB\mathbf1\) | \(0\) |
| \(1\) | \(k\ge1\) | \(eBA^5C^{k-1}R\) | \(0\) |
| \(2\) | \(k\ge0\) | \(eBD^kA\mathbf1\) | \(0\) |
| \(3\) | \(k=0\) | \(eBA^2\mathbf1\) | \(1\) |
| \(3\) | \(k\ge1\) | \(eBA^7C^{k-1}R\) | \(1\) |
| \(4\) | \(k\ge0\) | \(eAC^kBA^2\mathbf1\) | \(0\) |
| \(5\) | \(k\ge0\) | \(eAC^kBA^3\mathbf1\) | \(1\) |
| \(6\) | \(k\ge0\) | \(eAC^kBA^4\mathbf1\) | \(1\) |

For example, the negative-sign positions in the \(r=2\) row are \(0,7,14,\ldots,7k\). Every word in the table has exactly \(7k+r\) transition letters, because a factor \(C\) or \(D\) consists of seven letters and \(R=BA\mathbf1\) supplies the last two. The displayed zero values follow immediately from the invariant-vector identities; they are exact in every dimension. In the four odd-cardinality classes the same identities supply a coefficient equal to one, proving the sharp lower bound. This completes the classification.

Finally, Fourier characters are an orthogonal eigenbasis for counting convolution and \(T_n\chi_u=W_n(u)\chi_u\). Thus invertibility is equivalent to absence of zero Walsh multipliers, and in the invertible cases the \(\ell^2\)-operator norm of the inverse is \(1/\min_u|W_n(u)|=1\).

## Verification
The accompanying standalone Python program `CHECK.py` uses exact integer arithmetic. It checks the three invariant-vector identities and all scalar boundary products, the period-seven cardinality parity, and all displayed witness values through length 120. It also exhaustively computes full Walsh transforms for every length \(1\le n\le17\), totaling 262,142 Fourier frequencies, checking the stated zero-free/singular alternatives and comparing selected values against direct word enumeration and automaton transfer. The proof above, not this finite computation, establishes the all-length statements. Run: `python CHECK.py`.

## Relationship to prior work
Bilotta, Grazzini, Pergola, and Pinzani (2012) develop exhaustive generation for words excluding alternating patterns \((10)^j1\), including \(101\), under an additional balance constraint and indexed by numbers of ones. Bilotta, Grazzini, and Pergola (2013) develop generating functions for that restricted family. The present object is instead the **unrestricted fixed-length** avoidance language; the new invariant is the Fourier zero set of its binary indicator across all coordinate signings, not its unsigned enumerator. Classical finite automata and Fourier diagonalization are used as tools, not claimed as new. Separate Fourier studies of independent-set languages concern different support sets and do not imply this classification.

## Limitations
The theorem does not classify all nonzero multiplier magnitudes or their multiplicities, the exact kernel dimension at singular lengths, sharp endpoint \(\ell^1\) or \(\ell^\infty\) projection norms, or different forbidden words and cyclic avoidance. The literature comparison is bounded rather than a proof of historical priority. No independent mathematical audit has been performed.

## References
1. S. Bilotta, E. Grazzini, E. Pergola, and R. Pinzani, *Generation of binary words avoiding alternating patterns*, arXiv:1210.7620, first submitted 2012-10-29, https://arxiv.org/abs/1210.7620.
2. S. Bilotta, E. Grazzini, and E. Pergola, *Counting Binary Words Avoiding Alternating Patterns*, Journal of Integer Sequences **16** (2013), Article 13.4.8, https://cs.uwaterloo.ca/journals/JIS/VOL16/Grazzini/grazzini2.html.
