# A modulo-fourteen Walsh invertibility law for cyclic maximal independent sets

## Finding
For every integer \(n\ge 3\), let \(C_n\) be the simple labeled cycle and let \(A_n\subseteq\mathbb F_2^n\) consist of the incidence vectors of all *maximal* independent vertex sets (equivalently, independent dominating sets). For every \(b\in\mathbb F_2^n\), use the **unnormalized** Walsh coefficient
\[
W_n(b)=\sum_{x\in A_n}(-1)^{\sum_{j=1}^n b_jx_j}.
\]
Then the complete zero-versus-nonzero classification is
\[
\boxed{\exists b:\ W_n(b)=0\quad\Longleftrightarrow\quad
n\bmod14\in\{1,2,4,9,11\}.}
\]
Equivalently, unnormalized convolution by \(\mathbf1_{A_n}\) on \(\ell^2(\mathbb F_2^n)\) is invertible exactly for the other nine residue classes modulo fourteen. The apparently exceptional class \(n\equiv8\pmod{14}\) is uniformly zero-free even though \(|A_n|\) is even: every coefficient then satisfies
\[
\boxed{W_n(b)\equiv2\pmod4.}
\]
For all other zero-free classes, \(|A_n|\) is odd and hence every coefficient is odd.

## Assumptions and scope
The cycle has \(n\ge3\) vertices in cyclic order, with the usual distinct-label coordinate group \(\mathbb F_2^n\). A maximal independent set is an independent set that dominates each vertex not selected. The zero frequency corresponds to the total number of such sets. No normalization factor of \(2^{-n}\) is included in \(W_n\) or in the convolution operator. Multiplication and trace below are over the ordinary integers, not over a finite field. There is no assertion here about the exact number of vanishing frequencies in singular dimensions or about sharp inverse norms.

## Proof
**1. A signed three-state transfer.** A cyclic binary incidence word represents a maximal independent set precisely when it has no cyclic `11` and no cyclic `000`. Equivalently, successive selected vertices have circular gaps of length two or three. Track the current number of zeros since the previous selected vertex, in states \(0,1,2\). At position \(j\), placing a one contributes the sign \(t_j=(-1)^{b_j}\). The transition matrix, with old states indexing rows, is
\[
T(t)=\begin{pmatrix}0&1&0\\t&0&1\\t&0&0\end{pmatrix},\qquad t\in\{1,-1\}.
\]
Every admissible cyclic word has at least one selected vertex and determines a unique periodic state trajectory. Conversely, each closed trajectory gives one admissible word and its correct sign. Therefore
\[
W_n(b)=\operatorname{tr}\bigl(T(t_1)T(t_2)\cdots T(t_n)\bigr).
\tag{1}
\]

**2. The zero-free parity classes.** Put \(P_n=W_n(0)\), and let \(Q_n\) be the number of maximal independent sets containing a specified vertex. The characteristic polynomial of \(T(1)\) is \(\lambda^3-\lambda-1\), so \(P_n\) is the Perrin sequence,
\[
P_0=3,\ P_1=0,\ P_2=2,\qquad P_n=P_{n-2}+P_{n-3}\quad(n\ge3).
\]
A maximal independent set containing a specified vertex is uniquely encoded by an *ordered* composition of \(n\) into parts two and three, starting from that vertex; consequently
\[
Q_0=1,\ Q_1=0,\ Q_2=1,\qquad Q_n=Q_{n-2}+Q_{n-3}\quad(n\ge3).
\]
Direct substitution into these order-three recurrences shows that \(P_n\bmod2\) has period seven, \(P_n\bmod4\) has period fourteen, and \(Q_n\bmod2\) has period seven: their respective state triples at the period endpoints agree with their initial triples. It follows that \(P_n\) is even precisely for \(n\bmod14\in\{1,2,4,8,9,11\}\). If \(P_n\) is odd then every \(W_n(b)\) is odd, since all summands are signs; no coefficient can vanish.

For the remaining residue class \(n\equiv8\pmod{14}\), the same recurrence calculation gives \(P_n\equiv2\pmod4\) and \(Q_n\equiv0\pmod2\). For any subset \(B\) of negative-sign positions, one has \((-1)^k\equiv1-2k\pmod4\). Summing over all incidence vectors and using cyclic symmetry therefore yields
\[
W_n(\mathbf1_B)\equiv P_n-2\sum_{j\in B}\#\{x\in A_n:x_j=1\}
\equiv P_n-2|B|Q_n\equiv2\pmod4.
\]
This rules out zero coefficients for every frequency in the ninth zero-free residue class.

**3. Explicit zeros in every other class.** For each of the five starting lengths in the table, set \(t_j=-1\) at exactly the displayed 1-based positions and \(t_j=+1\) elsewhere. Direct multiplication of the three-by-three matrices in (1) gives trace zero in each case.

| Length | Negative-sign positions | Trace |
| ---: | --- | ---: |
| \(4\) | \(\{1\}\) | \(0\) |
| \(9\) | \(\{1,4\}\) | \(0\) |
| \(11\) | \(\{1,2,7\}\) | \(0\) |
| \(15\) | \(\{1,3,7\}\) | \(0\) |
| \(16\) | \(\{1,3,7\}\) | \(0\) |

Now define the seven-sign block \(B=(+,+,+,-,+,+,-)\). Its exact transfer product is
\[
T(+)^3T(-)T(+)^2T(-)
=\begin{pmatrix}-1&0&2\\0&-1&2\\0&0&1\end{pmatrix}
=:J,
\qquad J^2=I_3.
\]
Appending two copies of \(B\) to any trace-zero sign word adds fourteen positions and multiplies its transfer product on the right by \(I_3\), preserving trace zero. Every integer \(n\ge3\) with \(n\bmod14\in\{1,2,4,9,11\}\) is one of the five starting lengths plus a nonnegative multiple of fourteen. Thus a vanishing coefficient exists in precisely those classes.

**4. Convolution.** On the Boolean group, Walsh characters diagonalize unnormalized convolution by \(\mathbf1_{A_n}\), with eigenvalues exactly \(W_n(b)\). The claimed invertibility classification follows from steps 2 and 3.

## Verification
The standalone file `verify.py` uses integer arithmetic only and has no third-party dependencies. Execute `python3 verify.py` from a directory containing that file. It checks the transfer identity independently against direct signed enumeration for every frequency at lengths three through ten; it also computes complete Walsh transforms from explicit incidence-set enumeration through length eighteen. The code checks all five zero witnesses, the order-two matrix and fourteen-letter padding, and the claimed modular recurrences. The finite checks corroborate, but do not replace, the all-length proof above.

## Relationship to prior work
Bisdorff and Marichal's 2007 preprint establishes the classical Perrin counts of maximal independent sets of cycles and their encoding by circular gaps of lengths two and three; its main results count dihedral orbits. Those counts are the \(b=0\) specialization used here, but neither orbit enumeration nor the unweighted Perrin recurrence determines whether **every signed multivariate specialization** is nonzero. The result above requires an all-frequency argument and five explicit cancellation constructions. Other work on implication bases and Boolean traces of cycle maximal-independent-set incidence contexts concerns a different invariant and does not imply invertibility of the full Boolean-group convolution. Likewise, an analogous signed-path classification does not imply the cyclic trace condition or its modulo-fourteen exception.

## Limitations
The result is specific to *maximal*, rather than arbitrary or maximum-cardinality, independent sets of simple cycles, and to binary coordinate-wise Walsh characters. It does not count all zero frequencies in singular dimensions or determine exact spectral condition numbers in nonsingular dimensions. The priority comparison covers the literature and records named here, but cannot exclude an earlier unindexed signed-enumeration specialization. Independent mathematical validation has not been performed.

## References
1. Raymond Bisdorff and Jean-Luc Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph*, arXiv:math/0701647, first posted 2007-01-23; Journal of Integer Sequences 11 (2008), Article 08.5.7. https://arxiv.org/abs/math/0701647
2. *Minimal one-pass implications and exact Boolean trace rank for cycle maximal-independent-set contexts*, published research record, 2026-10-26 (distinct incidence-closure invariant).
