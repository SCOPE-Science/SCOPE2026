# First cubic Walsh blind spots in the thirteen-dimensional generalized Fibonacci cube

## Finding
Let \(C_n\subseteq\mathbb F_2^n\) be the words containing no three consecutive ones, and let \(f_n\) be their indicator. Give \(\mathbb F_2^n\) its usual additive group law and let \(T_n:g\mapsto f_n*g\) be unnormalized counting convolution. For a frequency \(S\subseteq\{1,\ldots,n\}\), set
\[
\widehat f_n(S)=\sum_{x\in C_n}(-1)^{\sum_{j\in S}x_j}.
\]
Among singular operators with \(1\le n\le13\), dimension \(n=13\) is the first whose Fourier zero set avoids **both** first- and second-order Walsh characters. Precisely,
\[
|C_{13}|=3136,\quad \operatorname{nullity}(T_{13})=1296,\quad
\operatorname{rank}(T_{13})=6896.
\]
The only degree-three zero frequencies are the four subsets
\[
\{1,7,9\},\quad\{1,9,11\},\quad\{3,5,13\},\quad\{5,7,13\}.
\]
For the earlier singular dimensions \(n=1,2,5,6,9,10\), the minimum vanishing frequency degrees are respectively \(1,1,2,2,2,2\); at \(n=13\) it is \(3\).

## Assumptions and scope
Words have open (noncyclic) boundaries, indexed left-to-right, and the forbidden substring is exactly `111`. The complete ambient Walsh transform has \(2^n\) characters, including the trivial character. A character's degree is the cardinality of its frequency support. Convolution is over complex-valued functions on the binary group, with **no normalization** in the forward Fourier transform. The main assertion concerns the specific natural run constraint and its first finite transition, not all forbidden-pattern cubes or all dimensions.

## Proof
**Convolution diagonalization.** Each character \(\chi_S(x)=(-1)^{\sum_{j\in S}x_j}\) is an eigenvector of \(T_n\) with eigenvalue \(\widehat f_n(S)\). The characters form a basis, so the nullity equals the number of zero character sums.

**Symbolic location of possible singular dimensions.** More generally, for a binary word set avoiding \(r\ge2\) consecutive ones, let \(U_r(z)\) be its ordinary length enumerator and \(V_r(z)\) its length enumerator weighted by \((-1)^{\text{number of ones}}\). Cutting words at each zero and allowing final runs of fewer than \(r\) ones gives
\[
U_r(z)=\frac{1-z^r}{1-2z+z^{r+1}},\qquad
V_r(z)=\frac{1-(-z)^r}{1-(-z)^{r+1}}.
\]
In characteristic two, \(U_r(z)\equiv(1+z^r)/(1+z^{r+1})\). Consequently the number of allowed words is odd exactly at lengths congruent to \(0\) or \(r\) modulo \(r+1\); all their Walsh sums are then odd and nonzero. At the remaining lengths the full-parity character has eigenvalue zero, by the formula for \(V_r\). For \(r=3\), this gives the singular dimensions among \(1\le n\le13\) as \(1,2,5,6,9,10,13\). This elementary parity test is background, not the claimed new finite spectral classification.

**Exact character census.** The accompanying `check.py` implements two exact and mathematically equivalent descriptions of every eigenvalue. The first enumerates each of the \(2^n\) binary words, accepts it precisely when the intersection of \(r\) consecutive bit shifts is empty, and applies the standard integer butterfly Walsh transform. By induction on butterfly stages, its output at frequency \(S\) is the displayed signed sum. The second is a separate left-to-right dynamic program with \(r\) states: state \(j\) stores the signed total of allowed prefixes ending in exactly \(j\) ones; appending zero resets the state to zero with coefficient \(1\), while appending one increases the state index with coefficient \((-1)^{\mathbf1_{i\in S}}\), unless that creates \(r\) successive ones. Induction on prefix length proves its output is the same signed sum. Thus both algorithms calculate **all**, rather than sampled, characters for each claimed finite dimension.

The exact integer comparison across every frequency and every dimension \(1\) through \(13\) yields the values above. At \(n=13\) the zero frequencies have the degree histogram
\[
\begin{array}{c|rrrrrrrrrrr}
\text{degree}&3&4&5&6&7&8&9&10&11&12&13\\\hline
\text{zeros}&4&33&93&198&280&295&223&118&42&9&1
\end{array}
\]
whose total is \(1296\). The absolute coefficients at degrees one and two have respective minima \(274\) and \(2\), certifying absence of low-degree zeros; the four degree-three zeros are exactly those listed in the finding. The earlier first-zero degrees are checked exhaustively in the same program. The finite classifications are established by complete integer enumeration, not by extrapolating sampled frequencies.

## Verification
Run `python3 check.py` from the directory containing this file. No third-party packages, external data, network services, or random choices are needed. The checker independently computes every Walsh coefficient using a butterfly transform and a separate finite-state recurrence and asserts agreement, the singularity pattern, all first-zero degrees, the exact \(n=13\) rank and nullity, its entire zero-degree histogram, the four degree-three masks, and the smallest nonzero low-degree magnitudes. It additionally tests the general run-limit parity criterion for \(2\le r\le6\) and \(1\le n\le10\). The algebraic generating-function proof above, rather than finite testing, establishes the auxiliary general run-limit criterion.

## Relationship to prior work
Run-length constraints and per-word signal spectra were studied by Kurmaev (2010). The third-order generalized Fibonacci cube as a graph on these forbidden-pattern words was explicitly studied by Rho and Vesel (2016). Their discussed recurrences and graph-recognition results supply context, not a full coordinate-wise Walsh convolution nullity table or the first degree-three blind-spot boundary stated here. The lower-order no-adjacent-ones case and general weighted-enumerator theory explain parts of the auxiliary parity criterion, which are not asserted to be novel. The finite cubic zero masks and total nullity require substantially more than an univariate word-count generating function.

## Limitations
This result makes no assertion about nullity or first-zero degree after dimension \(13\), no claim of a general symbolic closed formula for all Walsh coefficients, and no claim of independent external verification. An equivalent specialized Walsh table or an unindexed prior exact spectrum could preempt originality. The checker certifies only the stated finite calculations; the displayed proof explains the algorithms and their exhaustiveness.

## References
1. O. F. Kurmaev, *An Enumerative Method for Encoding Spectrum Shaped Binary Run-Length Constrained Sequences*, 2010-01-25, https://arxiv.org/abs/1001.4334.
2. Y. Rho and A. Vesel, *Linear recognition of generalized Fibonacci cubes Q_h(111)*, Discrete Mathematics & Theoretical Computer Science 17(3), 2016, https://doi.org/10.46298/dmtcs.2165.
3. J. Azarija, S. Klavžar, J. Lee, J. Pantone, and Y. Rho, *On Isomorphism Classes of Generalized Fibonacci Cubes*, arXiv:1402.6377, 2014-02-25, https://arxiv.org/abs/1402.6377.
