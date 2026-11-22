# Exact ambiguity language and inverse-fiber spectrum of cyclic Rule 150 on the golden-mean constraint

## Finding

For every integer \(n\ge3\), let \(X_n\) be the set of **indexed** binary circular words \(x=(x_0,\ldots,x_{n-1})\) satisfying \(x_i x_{i+1}=0\) for every index modulo \(n\). Define the deterministic three-neighbor parity readout

\[
\Phi_n(x)_i=x_{i-1}\oplus x_i\oplus x_{i+1},\qquad i\in\mathbb Z/n\mathbb Z,
\]

where \(\oplus\) is addition modulo two. Let \(p_n(y)=|\{x\in X_n:\Phi_n(x)=y\}|\) for \(y\in\{0,1\}^n\). For \(n=3m\), define three explicitly recognizable output languages

\[
Y_r=\left\{y:\ y_i=1\ \text{for }i\not\equiv r\pmod3,\quad
\bigoplus_{j=0}^{m-1}y_{r+3j}=m\bmod2\right\},\qquad r\in\{0,1,2\}.
\]

The complete positive inverse-multiplicity classification is as follows.

* If \(3\nmid n\), every attainable output has exactly one admissible predecessor.
* If \(n=3m\), the all-one output \(1^n\) has exactly **three** predecessors. Every \(y\in(Y_0\cup Y_1\cup Y_2)\setminus\{1^n\}\) has exactly **two**. Every other attainable output has exactly **one**. No output has more than three admissible predecessors.

In particular, every word in \(Y_0\cup Y_1\cup Y_2\) is attainable; the three sets have exactly one common/intersecting word, namely \(1^n\), and \(|Y_r|=2^{m-1}\). Write \(L_0=2\), \(L_1=1\), and \(L_{t+2}=L_{t+1}+L_t\) for the Lucas sequence. If \(A_j(n)=|\{y:p_n(y)=j\}|\) for \(j\ge1\), then for \(3\nmid n\),

\[
A_1(n)=L_n,\qquad A_j(n)=0\ (j\ge2),\qquad |\Phi_n(X_n)|=L_n.
\]

For \(n=3m\),

\[
\boxed{A_1(n)=L_n-3\cdot2^m+3,\quad
A_2(n)=3(2^{m-1}-1),\quad A_3(n)=1,\quad A_j(n)=0\ (j\ge4).}
\]

Thus the exact maximum noiseless codebook size obtainable by selecting inputs distinguishable from their parity readouts is

\[
\boxed{|\Phi_n(X_n)|=\begin{cases}
L_n,&3\nmid n,\\
L_n-3\cdot2^{n/3-1}+1,&3\mid n.
\end{cases}}
\]

The fraction of admissible inputs whose readouts uniquely identify them equals one if \(3\nmid n\), and for \(n=3m\) equals \((L_n-3\cdot2^m+3)/L_n\). Since \(L_n=\varphi^n+(-\varphi)^{-n}\), where \(\varphi=(1+\sqrt5)/2\), nonunique decoding is exponentially rare among uniformly sampled admissible inputs, with exponential ratio \(2^{1/3}/\varphi<1\).

## Assumptions and scope

The words have labelled coordinates and are **not** quotiented by cyclic rotation. The source alone is constrained; the observed output need not avoid `11`. The map is one synchronous application of the elementary binary additive rule conventionally called Rule 150; temporal iterates are not considered. The cycle has at least three sites so its three neighbors are distinct. A zero-fiber output is outside the readout image, and the claim about multiplicity one applies only to attainable outputs.

## Proof

**1. Full-ring kernel.** If \(\Phi_n(x)=\Phi_n(x')\), their bitwise difference \(v=x\oplus x'\) obeys

\[
v_{i+1}=v_i\oplus v_{i-1}.
\]

Every nonzero two-bit initial state produces a nonzero three-periodic sequence, one of the rotations of `011`. Hence when \(3\nmid n\) the only circular solution is zero, proving injectivity. When \(n=3m\), the kernel consists of zero and exactly three nonzero vectors \(u^{(r)}\), with \(u_i^{(r)}=0\) exactly at indices \(i\equiv r\pmod3\). There are at most four unrestricted predecessors of any output.

**2. The admissible collision pairs.** Fix \(r\), and suppose both \(x\) and \(x\oplus u^{(r)}\) belong to \(X_n\). At each pair of positions \(r+3j+1,r+3j+2\), both bits are toggled, and the two words must each avoid `11`; therefore the pair in \(x\) is exactly `01` or `10`. At each intervening position \(r+3j\), the bit cannot be one: either value at each of its neighboring positions is complemented in the other input, and one of the two inputs would then contain adjacent ones. Consequently there are bits \(b_0,\ldots,b_{m-1}\) such that

\[
(x_{r+3j},x_{r+3j+1},x_{r+3j+2})=(0,b_j,1\oplus b_j).
\]

Conversely every such \(m\)-block word, and its translate by \(u^{(r)}\), avoids `11`. There are \(2^m\) ordered admissible sources in this collision family and \(2^{m-1}\) unordered pairs.

**3. Exact ambiguous-output language.** Substituting this block description into the parity rule yields

\[
\Phi_n(x)_{r+3j}=1\oplus b_{j-1}\oplus b_j,\qquad
\Phi_n(x)_{r+3j+1}=\Phi_n(x)_{r+3j+2}=1.
\]

Taking the XOR over the first coordinates gives parity \(m\bmod2\), so every pair in step 2 maps to \(Y_r\). Conversely, given \(y\in Y_r\), choose \(b_0\in\{0,1\}\) and reconstruct all other \(b_j\) by the displayed recurrence. The parity condition guarantees consistency at the cyclic boundary. Exactly two choices are possible, differing by the constant complement of every \(b_j\). Thus \(Y_r\) is precisely the set of outputs having a pair of predecessors separated by \(u^{(r)}\), and \(|Y_r|=2^{m-1}\).

For distinct \(r\) and \(s\), the coordinates required to equal one by the definitions of \(Y_r\) and \(Y_s\) jointly cover every position. Thus \(Y_r\cap Y_s=\{1^n\}\). The all-one output indeed belongs to all three because its \(m\) free coordinates have XOR \(m\bmod2\). Its three distinct admissible predecessors are precisely the periodic words with a single one in each block of three, one for each of the three possible one-positions. A fourth admissible predecessor is impossible: the full four-element binary affine kernel coset of \(1^n\) comprises the three single-one period-three words and the all-one word; the latter is inadmissible. A different output in one \(Y_r\) cannot be in another \(Y_s\) and therefore has precisely its displayed pair. Any other output in the image has just one admissible predecessor, since any pair must differ by some \(u^{(r)}\). This proves the exact inverse-fiber classification.

**4. Exact census.** The count of cyclic `11`-avoiding binary words is \(|X_n|=L_n\), by the standard two-state closed-walk trace \(\operatorname{tr}\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)^n\). There is one three-predecessor output and \(3(2^{m-1}-1)\) two-predecessor outputs, because the three sets \(Y_r\) are disjoint away from \(1^n\). Counting the inputs by their output fibers gives

\[
A_1(n)=L_n-2A_2(n)-3A_3(n)=L_n-3\cdot2^m+3.
\]

Summing positive fiber counts gives the image formula. The displayed asymptotic follows from the Lucas closed form. All identities hold for \(m=1\), where \(A_2(3)=0\).

**5. Direct decoding.** Given any indexed output, test membership in \(Y_0,Y_1,Y_2\) by linear scanning. To recover all actual admissible predecessors in linear time, try the four possibilities for \((x_0,x_1)\), use \(x_{i+1}=y_i\oplus x_{i-1}\oplus x_i\) to reconstruct the remaining coordinates, and check both cyclic parity equations and all cyclic `11` constraints. This produces precisely every preimage, including the zero-preimage case, in \(O(n)\) bit operations and \(O(n)\) space.

## Verification

The included standalone standard-library program `verify.py` independently enumerates all admissible indexed inputs and their outputs for every \(3\le n\le18\). It checks all positive inverse-fiber populations, the explicit ambiguous-output languages, the Lucas source count, and, through \(n=11\), a separately coded four-seed inversion algorithm against every one of the \(2^n\) candidate outputs. It also verifies the integer census identities for all \(3\le n\le300\). Run with `python3 verify.py` in the same directory as this file. The program is finite corroboration; the proof above establishes the unbounded quantifiers.

For examples, the fiber spectra \((A_1,A_2,A_3)\) are \((1,0,1)\) at \(n=3\), \((9,3,1)\) at \(n=6\), and \((55,9,1)\) at \(n=9\). At lengths not divisible by three, every image output is unique-predecessor.

## Relationship to prior work

Makri and Psillakis (online 2023-11-21) study counting of constrained binary patterns and their information-theoretic uses, motivating the finite-length exact-counting setting; they do not study parity-readout inverse fibers. Salo (first arXiv 2022-09-27) develops general symbolic-dynamical questions of cellular-automaton inverse behavior, including an analysis of elementary rules, but does not give this constrained Rule 150 inverse spectrum. Jen (1989) gives general arbitrary-rule preimage recurrences, including a discussion of input constraints; those general tools can in principle compute finite instances but do not state the closed form or three-class output language above.

Related published computational records include an unrestricted-source, rotation-quotiented Rule 150 necklace inverse-degree classification, an unrestricted-source fixed-weight Rule 150 inverse spectrum, an exact XOR-pair representation formula for cyclic independent-set words, and a finite injectivity test for all elementary rules on the golden-mean shift. These address other inverse parameters and do not directly specify the indexed constrained output languages \(Y_r\), the unique triple-output, or all-positive constrained inverse multiplicities. The pair-representation result is particularly close: it can account for collision-pair totals after specialization, while the present classification additionally requires mapping individual pairs to outputs and proving their unique triple intersection.

## Limitations

The result concerns a single synchronous update, a binary circular source forbidding adjacent ones, and index-preserving readouts. It does not analyze repeated evolution, noncyclic boundaries, noise tolerance, or equivalence under rotation. The explicit image cardinality is a noiseless distinguishability result, not a claim of error-correcting capability against corruption. Historical priority could change if a previously uninspected or unindexed paper gives an equivalent constrained Rule 150 inverse-fiber theorem. A directly relevant published XOR-representation record was available at abstract/summary level; its full manuscript was not accessible in the consulted source. No independent scientific validation is claimed.

## References

1. F. S. Makri and Z. M. Psillakis, *Distribution of Patterns of Constrained Length in Binary Sequences*, Methodology and Computing in Applied Probability **25** (2023), article 90, DOI: https://doi.org/10.1007/s11009-023-10068-5 (first verified public online date 2023-11-21).
2. V. Salo, *On von Neumann regularity of cellular automata*, arXiv:2209.13373 (first public 2022-09-27), https://arxiv.org/abs/2209.13373.
3. E. Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems **3** (1989), pp. 421–456, https://www.complex-systems.com/abstracts/v03_i05_a02/.
4. published-finding corpus, *The exact inverse-degree spectrum of cyclic Rule 150 necklaces*, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-exact-inverse-degree-spectrum-of-cyclic-rule-150-necklaces--89cc648da7e1 (summary-level comparison only).
5. published-finding corpus, *Exact XOR representation profile and fourth Walsh moment of Fibonacci cubes*, 2026-11-16, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-exact-xor-representation-profile-and-fourth-walsh-moment-of-fibo--04d47201df94 (summary-level comparison only).
