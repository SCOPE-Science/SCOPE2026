# Minimal absent factors of two-marker binary words: exact counts and a limit law

## Finding
A minimal absent factor (MAF) of a finite binary word is a nonempty binary word that does not appear contiguously, although every proper contiguous factor does. Write \(M(w)\) for the number of distinct MAFs of \(w\).

**Exact finite-word theorem.** For arbitrary integers \(a,c\ge0\) and \(b\ge1\), put
\[
w=0^a1\,0^b1\,0^c,\quad U=\max\{a,b\},\quad V=\max\{b,c\},\quad L=\max\{a,b,c\},\quad K=\min\{U,V\}.
\]
Then
\[
\begin{aligned}
M(w)={}&1+K+\mathbf{1}_{L>U}+\mathbf{1}_{L>V}
 +\mathbf{1}_{(a-b)(c-b)>0}\\
&+\mathbf{1}_{a<b\le c}+\mathbf{1}_{c<b\le a}+\mathbf{1}_{a\ge b,\;c\ge b}.
\end{aligned}
\]
Here \(\mathbf{1}_P\) equals one if condition \(P\) holds and zero otherwise. In particular, \(M(w)=\max\{b,\min(a,c)\}+O(1)\), with a uniform absolute error bounded by seven.

**Sparse-word distribution theorem.** Fix \(n\ge3\), and choose \(W_n\) uniformly from all length-\(n\) binary words with exactly two ones, separated by at least one zero. Let \(Z_n=M(W_n)/n\). Then \(Z_n\) converges in distribution to a random variable \(Z\) with cumulative distribution function
\[
F_Z(t)=\begin{cases}
0,&t<0,\\
4t^2,&0\le t\le\frac13,\\
6t-5t^2-1,&\frac13\le t\le\frac12,\\
2t-t^2,&\frac12\le t\le1,\\
1,&t>1.
\end{cases}
\]
The first two limiting moments and limiting variance are
\[
\mathbb E Z=\frac7{18},\qquad
\mathbb E Z^2=\frac{41}{216},\qquad
\operatorname{Var}(Z)=\frac{25}{648}.
\]
Consequently \(\mathbb E M(W_n)=\frac7{18}n+o(n)\) and \(\operatorname{Var}(M(W_n))=\frac{25}{648}n^2+o(n^2)\).

## Assumptions and scope
All factors are contiguous; absence and minimality are relative to the full alphabet \(\{0,1\}\), not to scattered subsequences. Both ones are present and separated by a positive zero gap; terminal gaps may vanish. Random words are sampled uniformly *conditional on this constraint*: there are \(\binom{n-1}{2}\) equally likely ordered gap triples \((a,b,c)\) satisfying \(a+c+b=n-2\), \(b\ge1\), \(a,c\ge0\). A repeated occurrence of the same MAF is counted once. No conclusion is made about arbitrary binary words, adjacent-marker words, or words having three or more ones.

## Proof
**Step 1: MAFs with no ones.** A maximal block of zeros has length \(L\), so precisely \(0^{L+1}\) is minimal absent among zero-only factors.

**Step 2: MAFs with exactly one one.** Every existing such factor is \(0^i1\,0^j\), with \((i,j)\) in the down-closed union
\[
R=([0,a]\times[0,b])\cup([0,b]\times[0,c])\quad\text{on nonnegative integer pairs.}
\]
For a candidate containing one one, minimal absence requires that dropping its first and dropping its last symbol both produce existing factors. The two possible one-sided outer corners are \(0^{U+1}1\), when \(L>U\), and \(1\,0^{V+1}\), when \(L>V\); dropping the corresponding outside zero is possible precisely under these inequalities. The only interior missing corner is \(0^{a+1}1\,0^{c+1}\) when \(a,c<b\), or \(0^{b+1}1\,0^{b+1}\) when \(a,c>b\). The conditions are disjoint, equivalent to \((a-b)(c-b)>0\). There are no additional missing corners because \(R\) is a union of two origin-anchored rectangles. This yields the three one-one indicators in the formula.

**Step 3: MAFs with two ones.** A factor containing two ones must use the unique internal gap \(b\). For \(k\ne b\), the word \(1\,0^k1\) is absent and minimal exactly when both \(1\,0^k\) and \(0^k1\) occur, which is equivalent to \(0\le k\le\min(U,V)=K\). Because \(b\le K\), exactly \(K\) such gaps exist. For gap \(b\), the factor with terminal zero wings \(0^i1\,0^b1\,0^j\) occurs precisely for \(i\le a\), \(j\le c\). Checking the prefix and suffix of an absent wing-extension shows that the only additional MAFs of this form are \(0^{a+1}1\,0^b1\) when \(a<b\le c\), and \(1\,0^b1\,0^{c+1}\) when \(c<b\le a\). A word extended on both wings cannot be minimal absent: one of its single-symbol truncations still exceeds the corresponding available outer gap.

**Step 4: MAFs with three ones.** Every factor with three ones is absent. A minimal one must begin and end with one, since removing an outside zero would retain all three ones and remain absent. Hence the sole candidate is \(1\,0^b1\,0^b1\), whose proper prefix and suffix occur precisely when \(c\ge b\) and \(a\ge b\), respectively. A word with at least four ones cannot be minimal absent, because a single-symbol truncation still contains at least three ones. This exhausts the alphabetically possible MAFs and proves the exact formula.

**Step 5: Limiting distribution.** Since \(\min(\max(a,b),\max(b,c))=\max(b,\min(a,c))\), the exact formula gives \(M(w)=\max(b,\min(a,c))+O(1)\), uniformly. Under the stated uniform composition model, \((a/n,b/n,c/n)\) converges weakly to \((X,Y,T)\) uniformly distributed on the triangle \(X,Y,T\ge0\), \(X+Y+T=1\), equivalently a Dirichlet\((1,1,1)\) law. The continuous mapping theorem gives \(Z=\max(Y,\min(X,T))\).

For \(0\le t\le1\), \(\Pr(Y\le t)=2t-t^2\). The event \(Y\le t\), \(X>t\), \(T>t\) has probability
\[
2\int_0^{\min\{t,(1-2t)_+\}}(1-y-2t)_+\,dy,
\]
where \(u_+=\max\{u,0\}\). Subtracting this from \(\Pr(Y\le t)\) gives exactly the three polynomial regimes stated. Integrating \(1-F_Z(t)\) and \(2t(1-F_Z(t))\) on \([0,1]\) yields the moments. Because \(0\le Z_n\le2\) for all sufficiently large \(n\), the family has uniformly bounded first and second powers, so convergence in distribution also gives the first two moments; the mean and variance asymptotics follow.

## Verification
The accompanying self-contained standard-library `verify.py` enumerates actual factors independently of the formula. It compares complete sets of MAFs for every admissible triple through length \(45\), including boundary gaps and all case distinctions; it also samples longer words up to length \(300\) and evaluates finite-sample moments. These finite checks corroborate the exact formula, but only the preceding classification and simplex argument establish the all-length and limiting statements. Run `python verify.py` with Python 3.

## Relationship to prior work
Barton et al. [1] formalize suffix-array enumeration of minimal absent words; their stated theorem is algorithmic rather than an exact two-marker counting or conditional limit theorem. Akagi et al. [2] partition MAFs of run-length-compressed strings into five general types and establish representation-size bounds and output-sensitive reporting; the explicit gap formula and the nondegenerate conditional limiting law are not consequences stated there. Almirantis et al. [3] discuss extremal examples and applications of MAF counts, including strings with two rare outer markers, but do not determine this full gap-dependent formula or distribution. Aurell et al. [4] study distributions of **MAF lengths** in dense random and genomic sequences, not the count of MAFs under the fixed-two-marker conditional law. Unlike shortest absent **subsequences**, the words counted here are minimal with respect to contiguous substrings.

## Limitations
This is an exact result for a restricted but natural fixed-weight family, not a bound on arbitrary strings. An implementation of a general MAF enumerator can of course evaluate each finite instance: the claimed distinction is an all-parameter symbolic formula and its sharp sparse-random limit law. The historical priority comparison covers the cited full articles and searched records but cannot exclude a presently unindexed equivalent calculation. No independent mathematical audit has been conducted.

## References
[1] C. Barton, A. Heliou, L. Mouchard and S. P. Pissis, *Linear-time Computation of Minimal Absent Words Using Suffix Array*, arXiv:1406.6341, first public 24 June 2014; BMC Bioinformatics 15, 388 (2014). https://arxiv.org/abs/1406.6341 ; https://doi.org/10.1186/s12859-014-0388-9

[2] T. Akagi, K. Okabe, T. Mieno, Y. Nakashima and S. Inenaga, *Minimal Absent Words on Run-Length Encoded Strings*, CPM 2022, LIPIcs 223, article 27. https://doi.org/10.4230/LIPIcs.CPM.2022.27

[3] Y. Almirantis et al., *On avoided words, absent words, and their application to biological sequence analysis*, Algorithms for Molecular Biology 12, article 5 (2017). https://doi.org/10.1186/s13015-017-0094-z

[4] E. Aurell, N. Innocenti and H.-J. Zhou, *The Bulk and The Tail of Minimal Absent Words in Genome Sequences*, arXiv:1509.05188v1 (2015). https://arxiv.org/html/1509.05188v1
