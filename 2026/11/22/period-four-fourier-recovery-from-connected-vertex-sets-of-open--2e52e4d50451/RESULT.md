# Period-four Fourier recovery from connected vertex sets of open ladders

## Finding

Let \(L_n=P_n\square K_2\) be the open ladder with two labelled vertices in each of \(n\ge1\) successive columns. Let \(f_n:\mathbb F_2^{2n}\to\{0,1\}\) indicate the nonempty vertex subsets that induce a connected subgraph. Its unnormalized counting convolution \(T_n:g\mapsto f_n*g\) has an inverse exactly when

\[
\boxed{n\equiv1\text{ or }2\pmod4.}
\]

In each invertible case the smallest absolute Walsh multiplier is exactly \(1\), the largest is the connected-set count \(C_n\), and hence the sharp \(\ell^2\) condition number is \(C_n\). In every singular case an explicit character with multiplier zero is given below. The claim concerns the full Fourier spectrum's *zero-freeness*, not a classification of every zero character or the singular cases' least nonzero magnitude.

## Assumptions and scope

The vertices are \(u_i,v_i\), \(1\le i\le n\), with the rung edges \(u_iv_i\) and rail edges \(u_iu_{i+1},v_iv_{i+1}\) for \(1\le i<n\). The empty subset is excluded; singleton subsets are connected. Addition in \(\mathbb F_2^{2n}\) is coordinatewise XOR. For a frequency \(\xi\in\mathbb F_2^{2n}\) the unnormalized Walsh multiplier is

\[
\lambda_n(\xi)=\sum_{\substack{\varnothing\ne S\subseteq V(L_n)\\L_n[S]\text{ connected}}}(-1)^{\langle\xi,1_S\rangle}.
\]

Convolution is on counting measure. The orthogonal Walsh basis diagonalizes \(T_n\) with eigenvalues \(\lambda_n(\xi)\), so zero-free multipliers are equivalent to invertibility. Define \(C_n=\lambda_n(0)\).

## Proof

**1. A contiguous-column characterization.** Every connected nonempty vertex set occupies a nonempty interval of consecutive columns. In each occupied column its state is \(U\) (upper vertex only), \(V\) (lower only), or \(D\) (both). A state word encodes a connected set if and only if neither \(UV\) nor \(VU\) occurs consecutively. Necessity follows from the cut between such two adjacent singleton columns; sufficiency follows because every pair of successive selected columns shares a rail edge and the two vertices in a double state share a rung edge. Thus connected sets occupying exactly \(m\) columns have \(a_m\) admissible state words in each of the \(n-m+1\) possible intervals.

Writing \(p_m\) for the number of length-\(m\) admissible words ending in \(U\) (equally, \(V\)) and \(q_m\) for those ending in \(D\), we have

\[
\binom{p_{m+1}}{q_{m+1}}=
\begin{pmatrix}1&1\\2&1\end{pmatrix}
\binom{p_m}{q_m},\quad p_1=q_1=1,\qquad a_m=2p_m+q_m.
\]

Consequently \(a_1=3\), \(a_2=7\), and \(a_{m+2}=2a_{m+1}+a_m\) for all \(m\ge1\). In particular, every \(a_m\) is odd. Hence

\[
C_n=\sum_{m=1}^{n}(n-m+1)a_m
\equiv\frac{n(n+1)}2\pmod2.
\]

The right side is odd exactly for \(n\equiv1,2\pmod4\). Every Walsh multiplier is a sum of \(C_n\) signs and therefore has the same parity as \(C_n\). Thus all multipliers are nonzero in these two residue classes.

**2. Signed-state transfer.** Fix any character, writing its single-vertex factors at column \(i\) as \(\alpha_i=(-1)^{\xi_{u_i}}\) and \(\beta_i=(-1)^{\xi_{v_i}}\). Let \(t_i,b_i,d_i\) be the signed sums of connected subsets whose rightmost occupied column is \(i\) and whose last state is \(U,V,D\), respectively. Let \(z_i\) be the total signed sum over all connected subsets contained in the first \(i\) columns. Starting with \(t_0=b_0=d_0=z_0=0\), extension by one column and the two forbidden adjacent transitions give the exact integer recurrences

\[
\begin{aligned}
t_i&=\alpha_i(1+t_{i-1}+d_{i-1}),\\
b_i&=\beta_i(1+b_{i-1}+d_{i-1}),\\
d_i&=\alpha_i\beta_i(1+t_{i-1}+b_{i-1}+d_{i-1}),\\
z_i&=z_{i-1}+t_i+b_i+d_i.
\end{aligned}
\]

In particular \(z_n=\lambda_n(\xi)\).

**3. A periodic zero certificate.** Choose the first three sign pairs \((\alpha_i,\beta_i)\) as

\[
(+1,-1),\quad(+1,+1),\quad(+1,-1),
\]

and, starting at column four, repeat the four-column block

\[
(+1,-1),\quad(+1,-1),\quad(-1,+1),\quad(-1,-1).
\]

The exact recurrence gives \((t_1,b_1,d_1,z_1)=(1,-1,-1,-1)\), \((t_2,b_2,d_2,z_2)=(1,-1,0,-1)\), and then the following four-state cycle:

| Last column index | \((t_i,b_i,d_i,z_i)\) |
|---|---|
| \(i\equiv3\pmod4\) | \((2,0,-1,0)\) |
| \(i\equiv0\pmod4\) | \((2,0,-2,0)\) |
| \(i\equiv1\pmod4,\ i\ge5\) | \((1,1,-1,1)\) |
| \(i\equiv2\pmod4,\ i\ge6\) | \((-1,1,-2,-1)\) |

Each transition follows from the displayed integer recurrence and the corresponding next sign pair, so induction proves this cycle for every \(i\ge3\). In particular, \(\lambda_n(\xi)=z_n=0\) for \(n\equiv3,0\pmod4\), establishing singularity in all remaining orders. The same character has multiplier of magnitude \(1\) for \(n\equiv1,2\pmod4\), including the separately computed \(n=1,2\). Thus the lower bound \(1\) in the invertible orders is attained. Since \(|\lambda_n(\xi)|\le C_n\) for every character and \(\lambda_n(0)=C_n\), the stated maximum and sharp condition number follow.

## Verification

The standalone file `verify_connected_ladder.py` uses two independent finite constructions: brute-force graph connectivity on each vertex subset, followed by a full integer Walsh–Hadamard transform, and the signed three-state recurrence derived above. It compares every frequency in each dimension \(1\le n\le8\), verifies exact connected-set counts and the signed certificate, and checks the four-state cycle through \(n=400\). In the supplied execution it passed \(93{,}771\) exact assertions. The finite tests are corroborative, not the proof of the all-size result; the proof is the parity argument and four-state induction above.

For reproducibility, run `python3 verify_connected_ladder.py` using Python 3 with only its standard library. The printed frequency-zero counts for \(n=1,2,3,4,5,6,7,8\) are \(0,0,9,66,0,0,870,7462\), respectively.

## Relationship to prior work

Tittmann, Averbouch and Makowsky introduced the subgraph-component polynomial for counting induced subgraphs by size and number of components (public preprint of 2008-12-22). Vince subsequently gave a Pell-number enumeration of connected vertex subsets of ladders and their unsigned total; the 2017 paper, Example 3, uses the same three-state word encoding. Vince (2020) further studied connected-set average size and generating functions for ladders. These results supply the enumerative setting and, via the parity of the total, suggest one direction of the theorem. They do not state the all-size signed Walsh cancellation construction, its period-four zero criterion, or the sharp invertible \(\ell^2\) multiplier gap. The distinction is between aggregate cardinality enumerators and the full character-resolved signed distribution.

## Limitations

The theorem covers open two-rail ladders only, not circular ladders or arbitrary grid widths. It does not determine the multiplicity of zero frequencies in singular orders, nor the smallest positive multiplier there. The novelty comparison is limited to the cited accessible sources and targeted searches: an overlooked multivariate signed connected-set specialization or independently developed Fourier criterion could predate this formulation. The result has not received independent validation.

## References

1. P. Tittmann, I. Averbouch, J. A. Makowsky, *The Enumeration of Vertex Induced Subgraphs with respect to the Number of Components*, arXiv:0812.4147, first public posting 2008-12-22. https://arxiv.org/abs/0812.4147
2. A. Vince, *Counting connected sets and connected partitions of a graph*, Australasian Journal of Combinatorics 67(2) (2017), 281–293, especially Example 3. https://ajc.maths.uq.edu.au/pdf/67/ajc_v67_p281.pdf
3. A. Vince, *The average size of a connected vertex set of a graph—Explicit formulas and open problems*, Journal of Graph Theory 97 (2021), 82–103, first published 2020-11-03, DOI:10.1002/jgt.22643. https://people.clas.ufl.edu/avince/files/JGTfinal2.pdf
