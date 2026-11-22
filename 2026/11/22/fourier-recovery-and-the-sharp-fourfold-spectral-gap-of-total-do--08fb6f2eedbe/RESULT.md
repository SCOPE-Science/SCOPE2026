# Fourier recovery and the sharp fourfold spectral gap of total domination on paths

## Finding

Let \(P_n\) be the path on labelled vertices \(1,\ldots,n\), with \(n\ge2\). A *total dominating set* is a subset \(S\subseteq[n]\) such that every vertex has at least one **neighbor** in \(S\) (membership of the vertex itself does not suffice). Let \(\mathcal D_n\) contain all such sets, and define the unnormalized Walsh multipliers
\[
\Lambda_n(b)=\sum_{S\in\mathcal D_n}(-1)^{\sum_{i\in S}b_i},\qquad b\in\mathbb F_2^n.
\]
The convolution operator \(T_n\) on \(\ell^2(\mathbb F_2^n)\) is \((T_nf)(x)=\sum_{S\in\mathcal D_n}f(x+\mathbf1_S)\).

**Theorem.** For every integer \(n\ge2\), this convolution has a zero Walsh eigenvalue exactly when \(n\equiv1\pmod3\). The least strictly positive multiplier magnitude is
\[
 g_n=\min_{b:\Lambda_n(b)\ne0}|\Lambda_n(b)|=
 \begin{cases}4,&n\equiv1\pmod3,\\1,&n\not\equiv1\pmod3.\end{cases}
\]
Consequently \(T_n\) is invertible precisely when \(n\not\equiv1\pmod3\), with exact inverse operator norm \(\|T_n^{-1}\|_{2\to2}=1\). At the singular lengths its Moore--Penrose pseudoinverse has exact norm \(\|T_n^\dagger\|_{2\to2}=1/4\). If \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), the total number of admissible sets is
\[
 M_n=|\mathcal D_n|=
 \begin{cases}F_{m+1}^2,&n=2m,\ m\ge1,\\
 F_{m+3}F_m,&n=2m+1,\ m\ge1.
 \end{cases}
\]
Thus the sharp \(\ell^2\) spectral condition ratio, restricted to the recoverable spectral range when necessary, is \(M_n/g_n\).

## Assumptions and scope

The graph is the *ordinary open-neighborhood path*, not a cycle, not a path power, and not a graph with closed-neighborhood (ordinary) domination. All total dominating sets are counted once, including nonminimal ones. The path has at least two vertices because an isolated vertex cannot be totally dominated. Each Fourier character is indexed by an arbitrary \(n\)-bit frequency, not just by its Hamming weight. Fourier and convolution are on the entire Boolean group with counting measure; there is no \(2^{-n}\) normalization in the multipliers. The operator norm is on real or complex \(\ell^2\).

## Proof

**1. Split the total-domination constraints into two parity chains.** Write \(x_i=\mathbf1_{i\in S}\). For each internal vertex \(i\), its open-neighborhood requirement is \(x_{i-1}\lor x_{i+1}=1\). The two endpoints require \(x_2=x_{n-1}=1\), with the two forced conditions referring to the same coordinate when \(n=3\). These conditions separate the odd-indexed and even-indexed coordinates: in each parity chain, two consecutive chain entries may not both be zero.

For \(n=2m\), the odd-indexed chain has its last entry fixed to one and the even-indexed chain has its first entry fixed to one. The remaining two disjoint free chains both have length \(m-1\). For \(n=2m+1\) with \(m\ge2\), the odd-indexed chain has length \(m+1\) with no fixed entries, and the even-indexed chain has both endpoint entries fixed to one, leaving a free chain of length \(m-2\). For \(n=3\), the even coordinate is forced to one while the odd chain has length two. Thus in every case the signed enumeration factors, up to an overall sign, into the signed enumerations of two free chains with the no-adjacent-zero restriction.

**2. Identify the free-chain signed sum.** For an integer \(L\ge0\) and signs \(t_1,\ldots,t_L\in\{-1,+1\}\), define
\[
 Z_L(t_1,\ldots,t_L)=\sum_{A\subseteq[L]\,\mathrm{independent\ in}\ P_L}\prod_{i\in A}t_i,
\]
with \(Z_0=1\). This is the multivariate independence-set polynomial of a path evaluated at signs; the underlying polynomial and endpoint recurrence are classical. To evaluate the Walsh sum over a free binary chain \(y\) whose zero positions form an independent set, factor out \(\prod_i(-1)^{b_i}\) and take \(t_i=(-1)^{b_i}\). Hence the Walsh sum has absolute value \(|Z_L(t)|\). The recurrence
\[
 Z_0=1,\quad Z_1=1+t_1,\quad
 Z_L=Z_{L-1}+t_L Z_{L-2}\quad(L\ge2)
\]
follows by conditioning on whether the last position belongs to the independent set. For each fixed \(L\), varying the frequency varies the signs independently. The two parity-chain sign choices are also independent, so their possible absolute multipliers form the product of the two respective sets of absolute values.

**3. Prove the exact zero and least-positive classification of the path polynomial.** Modulo two, every evaluation \(Z_L(t)\) equals the number of independent sets of \(P_L\), which is \(F_{L+2}\). Fibonacci numbers are even precisely at indices divisible by three. Thus if \(L\not\equiv1\pmod3\), all signed evaluations are odd and therefore nonzero. If \(L\equiv1\pmod3\), all signed evaluations are even.

For the constant signing \(t_i=-1\), the recurrence yields the six-periodic sequence
\[
 Z_0,Z_1,Z_2,Z_3,Z_4,Z_5,\ldots
 =1,0,-1,-1,0,1,1,0,\ldots,
\]
so a zero exists exactly at lengths \(L\equiv1\pmod3\), and for every nonresonant length there is a coefficient of magnitude one. For the signing \(t_1=+1\) and \(t_2=\cdots=t_L=-1\), the recurrence gives the six-periodic values \(Z_1=2,Z_2=1,Z_3=-1,Z_4=-2,Z_5=-1,Z_6=1,Z_7=2\). In particular its magnitude is exactly two at every \(L\equiv1\pmod3\). Therefore
\[
 \min_{t:\,Z_L(t)\ne0}|Z_L(t)|=
 \begin{cases}2,&L\equiv1\pmod3,\\1,&L\not\equiv1\pmod3,\end{cases}
\]
and there is a zero in the signed path spectrum if and only if \(L\equiv1\pmod3\). This also holds for \(L=0\), where the unique sum is one.

**4. Combine the two factors.** For even \(n=2m\), both free chains have length \(m-1\). They are resonant exactly when \(m\equiv2\pmod3\), equivalently \(n\equiv4\pmod6\). For odd \(n=2m+1\), \(m\ge2\), the free-chain lengths \(m+1\) and \(m-2\) differ by three, so they are simultaneously resonant exactly when \(m\equiv0\pmod3\), equivalently \(n\equiv1\pmod6\). At \(n=3\), the length-two and length-zero factors are both nonresonant, in agreement with the same rule. The union of the even and odd resonance classes is exactly \(n\equiv1\pmod3\). Since each resonant factor has a zero and smallest positive magnitude two, the product has zeros and smallest positive magnitude four; outside the resonance classes both factors are zero-free and have minimum absolute value one. Independent frequency choices attain the product minima.

**5. Count the sets and diagonalize convolution.** A binary chain of length \(L\) with no adjacent zero entries is counted by the number of independent sets of \(P_L\), namely \(F_{L+2}\). Taking the product for the even and odd parity chains gives the stated formula for \(M_n\), with \(M_3=3=F_4F_1\) checked directly. Walsh characters are an orthogonal eigenbasis for unnormalized XOR convolution, with eigenvalues \(\Lambda_n(b)\). The bound \(|\Lambda_n(b)|\le M_n\) is attained at the trivial character. The established minimum nonzero magnitude therefore proves the exact norms and condition ratios.

## Verification

The accompanying standard-library-only Python file `verify.py` independently constructs every total-dominating-set incidence mask, applies an exact integer fast Walsh--Hadamard transform, and compares it with a parity-chain evaluation using the signed-independent-set recurrence for all \(2^n\) frequencies at every \(2\le n\le16\). It separately enumerates signed character sums directly through \(n=8\), and compares all signed path-polynomial values to an independent fast Walsh transform through free-chain length 15. It verifies the exact resonance and least-positive gaps and checks rank/nullity examples at lengths 4, 7, 10 and 13. Run `python3 verify.py`; the expected terminal marker is `TOTAL_DOMINATION_WALSH_EXACT_PASS assertions=197234`. These finite tests corroborate, but do not replace, the all-length proof above.

## Relationship to prior work

Scott and Sokal (2003), Section 3.2, Example 3.2, give the classical path independence polynomial and its endpoint recurrence, used and explicitly credited in the proof above. Henning and Yeo (2007) use the established open-neighborhood definition of total domination and study bounds on the minimum size of a total dominating set, not arbitrary signed counts. Alikhani and Jafari (2016) study the univariate total-domination polynomial and its roots, and include an inclusion--exclusion formula for ordinary size enumerators. The present statement concerns the complete **multivariate signed incidence transform of all total dominating sets of paths**, including every Boolean character, exact invertibility, and the sharp fourfold spectral gap. The univariate total-domination polynomial alone does not evaluate arbitrary signed substitutions; the polynomial machinery by itself does not state the endpoint-forced parity-chain factorization or the resulting all-character theorem.

Two related published results concern Walsh transforms of cycle independent sets and cyclic window-covering words, respectively. Those are different families with cyclic boundary conditions; neither directly gives the total-domination path theorem with two independent free chains and the squared spectral gap. The comparisons are bounded and do not establish exclusive historical priority.

## Limitations

The theorem does not classify the exact multiplicity of each nonzero multiplier, optimal endpoint \(\ell^1\)/\(\ell^\infty\) projection norms, or total domination on general trees or cycles. The classical signed independent-set recursion is not claimed as novel. A prior work on trivariate total-domination polynomials could contain an equivalent special case; the full text of one plausible 2016 graph-product paper was not accessible for a decisive comparison. Independent mathematical validation and exhaustive priority verification remain outstanding.

## References

1. A. D. Scott and A. D. Sokal, *The Repulsive Lattice Gas, the Independent-Set Polynomial, and the Lovász Local Lemma*, arXiv:cond-mat/0309352, version 1 publicly submitted 2003-09-15, Section 3.2, Example 3.2; https://arxiv.org/abs/cond-mat/0309352.
2. M. A. Henning and A. Yeo, *A New Upper Bound on the Total Domination Number of a Graph*, Electronic Journal of Combinatorics 14 (2007), R65, published 2007-09-07; https://www.combinatorics.org/ojs/index.php/eljc/article/download/v14i1r65/pdf/.
3. S. Alikhani and N. Jafari, *On the Roots of Total Domination Polynomial of Graphs*, arXiv:1605.02222, version 1 posted 2016-05-07, Section 3, Theorem 3.1; https://arxiv.org/abs/1605.02222.
4. S. Alikhani and N. Jafari, *Total domination polynomial of graphs from primary subgraphs*, arXiv:1609.07789, version 1 posted 2016-09-25; https://arxiv.org/abs/1609.07789.
5. *Cycle independent sets: a modulo-three Fourier invertibility law with sharp spectral gaps*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-cycle-independent-sets-a-modulo-three-fourier-invertibility-law--acf4a6fabe72.
6. *Cyclic window covers: a complete Walsh singularity and sharp gap law*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-cyclic-window-covers-a-complete-walsh-singularity-and-sharp-gap--2e48ad120cf2.
