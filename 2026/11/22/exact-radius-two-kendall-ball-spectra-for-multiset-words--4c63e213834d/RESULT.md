# Exact radius-two Kendall-ball spectra for multiset words

## Finding

Let \(q\ge 2\), \(n\ge2\), and \(x=x_1\cdots x_n\in\Sigma_q^n\), with alphabet symbols allowed to repeat. Two words are adjacent when one is obtained from the other by exchanging two *unequal consecutive* symbols. Let \(B_2(x)\) contain the distinct words at graph distance at most two from \(x\), including \(x\) itself. Put \(m=n-1\) and define

\[
K(x)=\#\{i\in[1,m]:x_i=x_{i+1}\},\quad
C(x)=\#\{i\in[1,m-1]:x_i=x_{i+1}=x_{i+2}\},
\]
\[
A(x)=\#\{i\in[1,m-1]:x_i=x_{i+2}\ne x_{i+1}\}.
\]

The center-specific identity used below is a consequence of the support partition in *Complete maximizers of exact-two adjacent-swap spheres over nonbinary alphabets* (see Relationship to related work). In the present shorthand it gives

\[
\boxed{|B_2(x)|=\binom{m-K(x)}2+2m-K(x)-C(x)-2A(x).}
\tag{1}
\]

The contribution here is the **complete all-length ball-size distribution over labeled words**, with binary extremal counts and fluctuation limits. For \(n\ge2\), let

\[
G_{q,n}(u,v,w)=q\,(u,\ q-1)
\begin{pmatrix}uv&q-1\\u&q-2+w\end{pmatrix}^{n-2}
\binom11.
\tag{2}
\]

The coefficient \([u^k v^c w^a]G_{q,n}\) counts exactly the words with \((K,C,A)=(k,c,a)\). Consequently the number of length-\(n\) centers having ball size \(s\) is the exact finite sum

\[
\boxed{N_{q,n}(s)=\sum_{\substack{k,c,a\ge0:\\\binom{m-k}{2}+2m-k-c-2a=s}}
[u^k v^c w^a]G_{q,n}(u,v,w).}
\tag{3}
\]

For \(q\ge3\), a direct consequence of (1) is that the sharp maximum is \(\binom m2+2m\), attained by exactly \(q(q-1)(q-2)^{n-2}\) length-\(n\) words. The maximizing words have every adjacent pair unequal and every consecutive triple pairwise distinct; in particular at \(n=2\) the two letters must differ. For the binary alphabet, the maximum ball size is \(2,3,6,8\) at lengths \(2,3,4,5\), with respectively \(2,6,2,6\) labeled maximizing words; for every \(n\ge6\), the maximum equals \(2+\binom{n-1}{2}\) and is attained only by the two alternating words.

For a uniformly random word \(X\in\Sigma_q^n\), write \(p=(q-1)/q\). The exact mean is

\[
\mathbb E|B_2(X)|=1+\binom{m-1}{2}p^2+(3m-2)p
-\frac{2(m-1)(q-1)}{q^2}.
\tag{4}
\]

For every fixed \(q\ge2\), a Gaussian limit holds:

\[
\frac{|B_2(X)|-\mathbb E|B_2(X)|}{m^{3/2}}
\ \xrightarrow{\mathrm d}\ \mathcal N\bigl(0,p^3(1-p)\bigr).
\tag{5}
\]

There is also a distinct rare-collision limit. If \(q=q_n\to\infty\) and \(n/q_n\to\lambda\in[0,\infty)\), with \(M_n=\binom{n-1}{2}+2(n-1)\), then

\[
\frac{M_n-|B_2(X)|}{n-1}\xrightarrow{\mathrm d}
\operatorname{Poisson}(\lambda).
\tag{6}
\]

For \(n=1\), every ball has size one. Equations (1)–(6) concern linear indexed words, not cyclic words or exchanges of arbitrary nonadjacent positions.

## Assumptions and scope

A word is labeled by its positions and letters. A legal step exchanges two consecutive symbols only when they are different; exchanging equal letters has no effect and does not create a new vertex. The graph is the ordinary multiset-permutation graph under adjacent swaps, also called Kendall adjacent-transposition distance. The alphabet need only have cardinality \(q\); no ordering of letters enters the result. Coefficients are counted over **all** \(q^n\) labeled words, allowing arbitrary multiplicity vectors. The zero-length word is outside the stated formulas; the singleton case is explicit above. Matrix powers in (2) are ordinary polynomial matrix powers, with the zeroth power the identity. The Gaussian statement keeps \(q\) fixed, while (6) varies \(q\) with \(n\).

## Proof

**Center-specific identity.** For completeness, write \(b_i=\mathbf 1_{x_i\ne x_{i+1}}\), \(t=\sum_{i=1}^m b_i=m-K\), and \(H=\sum_{i=1}^{m-1}b_i b_{i+1}\). There are exactly \(t\) nonidentity one-swap outputs. For two swaps with disjoint swapped pairs, both original boundaries must be unequal. The result differs from the source at all four swapped positions, so different disjoint pairs give different outputs, not obtainable with overlapping swaps. Their count is \(\binom t2-H\).

Two overlapping swaps act on a unique consecutive triple. A triple with three distinct symbols gives two distinct three-cycle outputs; a triple with exactly one unequal boundary gives one genuinely new output; a triple of the form \(aba\) with \(a\ne b\) gives no new output after two legal swaps; a constant triple gives none. These outputs have minimal changed interval of length three and are distinct from disjoint-pair outputs and from those belonging to other triples. Thus the total number from overlapping swaps is

\[
\sum_{i=1}^{m-1}\bigl(b_i+b_{i+1}-2\mathbf1_{x_i=x_{i+2}\ne x_{i+1}}\bigr)
=2t-b_1-b_m-2A.
\]

Adding radius zero and one gives

\[
|B_2(x)|=1+t+\binom t2-H+2t-b_1-b_m-2A.
\]

Let \(e_i=1-b_i\), so \(K=\sum e_i\) and \(C=\sum e_i e_{i+1}\). Direct expansion yields

\[
H=(m-1)-2K+e_1+e_m+C,
\qquad b_1+b_m=2-e_1-e_m.
\]

Substitution proves (1) exactly, including \(m=1\) with empty triple sums. No probabilistic or finite-experiment step is needed for this identity.

**Distribution by transfer.** After reading two letters, label the last adjacent pair \(E\) (equal) or \(D\) (different). There are respectively \(q\) and \(q(q-1)\) initial words, with initial \(K\)-weights \(u\) and one. Appending a letter to state \(E\) gives: one option maintaining equality (increment \(K\) and \(C\)), or \(q-1\) options entering state \(D\). From state \(D\): one option making the new adjacent pair equal (increment \(K\)); one option creating a returning triple \(aba\) (increment \(A\)); or \(q-2\) other distinct options. These four choices are precisely the matrix entries of (2). Induction on the word length proves (2), and substitution of (1) proves (3).

**Maxima.** The preceding disjoint/overlapping decomposition has the absolute bounds \(t\le m\), \(\binom t2-H\le\binom m2-(m-1)\), and at most \(2(m-1)\) overlapping outputs. Their sum is \(\binom m2+2m\). For \(q\ge3\) simultaneous equality holds exactly if every adjacent pair is unequal and every consecutive triple has three distinct symbols. There are \(q(q-1)(q-2)^{n-2}\) such words.

For \(q=2\), every triple with both adjacent boundaries unequal is of type \(aba\), and hence \(A=H\). Let \(e=e_1+e_m\). Rewriting (1) shows

\[
|B_2(x)|=2+\binom{m-K}{2}+3K-2e-3C,
\quad
|B_2(x)|-\bigl(2+\binom m2\bigr)
=\frac{K(K-2m+7)}2-2e-3C.
\]

For \(m\ge8\) this difference is negative whenever \(K\ge1\). For \(m=7\), only \(K=7\) could make its first term nonnegative, and then \(e+C>0\). For \(m=5,6\), possible nonnegative first terms likewise have \(K\) so large that \(e+C\ge K-\lfloor(m-1)/2\rfloor\); indeed deleting endpoint zeros and all but one zero from each consecutive zero cluster leaves at most \(\lfloor(m-1)/2\rfloor\) isolated interior zeros. Using \(2e+3C\ge2(e+C)\) makes the difference strictly negative for each such \(K\). Thus for \(m\ge5\) only \(K=0\) maximizes, giving the two alternating words. Exhausting the boundary vectors for \(m=1,2,3,4\) gives the exceptional sizes and multiplicities stated above.

**Mean and limits.** For a uniform word, its successive equal/different indicators are independent Bernoulli variables: each equality has probability \(1/q\). Thus \(t\sim\operatorname{Bin}(m,p)\); also \(\mathbb E H=(m-1)p^2\), \(\mathbb E A=(m-1)(q-1)/q^2\), and \(\mathbb E(b_1+b_m)=2p\). Taking expectations in the unsimplified identity proves (4). Uniformly in every word, \(|B_2(x)|=\tfrac12 t^2+O(m)\), so the binomial central limit theorem and the delta method give (5), including the centering by its exact mean.

For the rare-collision regime put \(K=m-t\). Exact subtraction from the maximal ball yields

\[
M_n-|B_2(x)|=K\left(m-\frac{K-1}{2}\right)+C+2A.
\]

Now \(K\sim\operatorname{Bin}(m,1/q_n)\) tends to \(\operatorname{Poisson}(\lambda)\). Moreover \(\mathbb EC=(m-1)/q_n^2=o(1)\) and \(\mathbb EA=(m-1)(q_n-1)/q_n^2=O(1)\). Hence division by \(m\) and Slutsky's theorem prove (6).

## Verification

The included standalone Python program `verify.py` computes each ball independently by breadth-first adjacent swapping, compares it against (1), and independently counts the \((K,C,A)\) coefficient distribution through the two-state transfer. It exhausts alphabets of size \(2\) through length \(10\), size \(3\) through length \(8\), and size \(4\) through length \(7\), a total of \(33{,}730\) labeled source words. It also checks the exact mean and the maximizer counts. Run it with `python3 verify.py`. The mathematical proofs above, rather than the finite checks, justify all lengths, alphabet sizes, and limits.

## Relationship to related work

*Complete maximizers of exact-two adjacent-swap spheres over nonbinary alphabets* uses the same word model but counts outputs of exactly two swap operations, allowing equal-letter swaps as no-ops. Its support partition gives \(|T_2|=1+\binom{t}{2}+a+h-2A+s\), where \(a\) counts successive pairs of active boundaries, \(h\) counts successive pairs with exactly one active boundary, and \(s\) counts the distinct one-effective-swap outputs present in \(T_2\). Every zero-distance or distance-two output of the closed ball is already present in \(T_2\). Passing from \(T_2\) to the closed ball therefore adds \(t-s\) one-swap outputs. Using \(a+h=m-1-C\) yields (1). This identity is used as input for the transfer distribution and its consequences rather than claimed as an independent enumeration of the same two-swap structure.

Buzaglo–Yaakobi–Etzion–Bruck (2013) establish foundational Kendall-distance properties for multipermutations, give the radius-one ball size in terms of runs, and state bounds for radius-two ball volumes in a fixed-multiplicity family. Their stated bounds do not determine every center-specific volume or the all-alphabet two-state enumerator. Bereg and collaborators (2023) study distance bounds for *permutations without repeated labels*. Their framework yields the familiar distinct-letter specialization but not the repeated-letter correction terms. Adamson–Flaherty–Potapov–Spirakis (2023) investigate arbitrary-position swaps, for which their configuration graph has markedly different local structure; adjacent-only two-step balls are not covered by their results. Gregor–Merino–Mütze (2023) treat star-transposition Gray codes rather than radius-two adjacent-swap ball distributions.

## Limitations

The claim is confined to graph distance at most two, not larger error radii, nearest-neighbor decoding algorithms, or optimal codebook sizes. The all-length distribution (3) is given by an explicit coefficient transform, not a single univariate rational generating function in ball size. The asymptotics are under uniformly distributed labeled words, not fixed multiplicity-vector sampling. No priority is asserted for the center-specific identity.

## References

- *Complete maximizers of exact-two adjacent-swap spheres over nonbinary alphabets*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-complete-maximizers-of-exact-two-adjacent-swap-spheres-over-nonb--228c8deb5a52/RESULT.md , especially Finding and Proof §1.
- S. Buzaglo, E. Yaakobi, T. Etzion, J. Bruck, *Error-Correcting Codes for Multipermutations*, IEEE ISIT 2013, https://www.paradise.caltech.edu/~yaakobi/publications/multipermutations_isit13.pdf .
- S. Bereg, W. Bumpass, M. Haghpanah, B. Malouf, I. H. Sudborough, *Improved Permutation Arrays for Kendall Tau Metric*, arXiv:2301.11423 (first public 2023-01-26), https://arxiv.org/abs/2301.11423 .
- D. Adamson, N. Flaherty, I. Potapov, P. G. Spirakis, *Structural and Combinatorial Properties of 2-swap Word Permutation Graphs*, arXiv:2307.01648 (first public 2023-07-04), https://arxiv.org/abs/2307.01648 .
- P. Gregor, A. Merino, T. Mütze, *Star transposition Gray codes for multiset permutations*, Journal of Graph Theory 103 (2023), https://doi.org/10.1002/jgt.22915 .
