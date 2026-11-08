# Exact sphere law for two deletions confined to a three-symbol window

## Finding
For integers \(q\ge2\) and \(n\ge3\), let \(\Sigma_q\) be a \(q\)-symbol alphabet. For each word \(x=x_1\cdots x_n\in\Sigma_q^n\), let \(\mathcal B(x)\) consist of the **distinct** length-\(n-2\) words produced by deleting positions \(i<j\) satisfying \(j-i\le2\). Thus exactly two symbols are removed from a single (unknown) window of length at most three, and duplicate outputs are counted once. Put \(B(x)=|\mathcal B(x)|\).

Define \(d(a,b,c)=1\) if \(a,b,c\) are pairwise distinct, \(d(a,b,c)=-1\) if all three are equal, and \(d(a,b,c)=0\) otherwise. Then the **all-length local sphere identity** is
\[
B(x)=n-1+\sum_{i=1}^{n-2}d(x_i,x_{i+1},x_{i+2}). \tag{1}
\]
Its consequences are as follows.

* The minimum is \(1\), reached by exactly the \(q\) constant words. For \(q\ge3\), the maximum is \(2n-3\) and precisely \(q(q-1)(q-2)^{n-2}\) words attain it. For \(q=2\), the maximum is \(n-1\) and precisely \(2F_{n+1}\) words attain it, with \(F_0=0,F_1=1,F_{r+2}=F_{r+1}+F_r\).
* The complete finite-length enumerator \(P_{n,q}(z)=\sum_{x\in\Sigma_q^n}z^{B(x)}\) is the transfer expression
\[
P_{n,q}(z)=z^{n-1}\mathbf1^\top T_q(z)^{n-2}\mathbf1,\qquad
T_q(z)_{(a,b),(u,c)}=\mathbf1_{\{u=b\}}z^{d(a,b,c)}, \tag{2}
\]
where states are ordered alphabet pairs and \(\mathbf1\) is the all-ones vector of length \(q^2\). Negative intermediate powers of \(z\) are allowed in \(T_q\); the final expression is a polynomial with nonnegative integer coefficients.
* If \(X_1,\ldots,X_n\) are independent uniformly distributed alphabet symbols, then
\[
\mathbb E B(X)=n-1+(n-2)\frac{q^2-3q+1}{q^2}, \tag{3}
\]
\[
\operatorname{Var}B(X)=\frac{(q-1)\bigl(5nq^2-9nq+3n-12q^2+22q-8\bigr)}{q^4}. \tag{4}
\]
For each fixed \(q\ge2\), as \(n\to\infty\),
\[
\frac{B(X)-\mathbb EB(X)}{\sqrt n}\ \xrightarrow{\ d\ }\ \mathcal N\!\left(0,\frac{(q-1)(5q^2-9q+3)}{q^4}\right). \tag{5}
\]

## Assumptions and scope
The alphabet need not be a finite field. The word is an ordered sequence; deletions preserve the relative order of surviving symbols. Windows are nonwrapping. The deletion count is **exactly two**, rather than at most two, and deletions within one three-position window may be adjacent or may skip the middle position. For the probabilistic conclusions the input is uniform independent and \(q\) is fixed in the limit. The theorem does not require a particular code, encoder, or decoder.

## Proof
**Step 1: classify adjacent deletion outputs.** Write \(A_i\) for the output deleting \(i,i+1\), for \(1\le i\le n-1\). For \(i<j\), direct comparison of the surviving coordinate lists shows
\[
A_i=A_j\quad\Longleftrightarrow\quad x_k=x_{k+2}\ \text{for every }i\le k<j.
\]
In particular, the equivalence classes of the \(A_i\)'s are the connected components of the path with edge \(i\sim i+1\) exactly when \(x_i=x_{i+2}\). The number of distinct adjacent-deletion outputs therefore equals
\[
(n-1)-\sum_{i=1}^{n-2}\mathbf1_{\{x_i=x_{i+2}\}}. \tag{6}
\]

**Step 2: classify skipped-middle outputs.** For \(1\le i\le n-2\), let \(D_i\) delete positions \(i,i+2\). If \(x_{i+1}=x_{i+2}\), then \(D_i=A_i\); if \(x_i=x_{i+1}\), then \(D_i=A_{i+1}\). If both inequalities \(x_{i+1}\ne x_i\) and \(x_{i+1}\ne x_{i+2}\) hold, \(D_i\) differs from every \(A_j\): for \(j\le i\), the surviving symbol at output position \(i\) forces \(x_{i+1}=x_{i+2}\), and for \(j\ge i+1\), it forces \(x_{i+1}=x_i\). The same first differing output position shows that distinct such \(D_i,D_j\), with \(i<j\), cannot coincide: the comparison at output position \(i\) would require \(x_{i+1}=x_i\). Hence the number of additional outputs is exactly
\[
\sum_{i=1}^{n-2}\mathbf1_{\{x_{i+1}\ne x_i,\ x_{i+1}\ne x_{i+2}\}}. \tag{7}
\]
For any triple \((a,b,c)\), the quantity \(\mathbf1_{\{b\ne a,b\ne c\}}-\mathbf1_{\{a=c\}}\) is \(+1\) for three different symbols, \(-1\) for three equal symbols, and zero otherwise. Equations (6)–(7) yield (1) for every word.

**Step 3: extrema and enumerator.** For \(q\ge3\), each term of (1) is at most one, with equality exactly on a pairwise-distinct triple. Choosing the first symbol, second symbol, and each subsequent symbol outside the two preceding choices gives the stated maximum and count. For \(q=2\), the positive case is impossible; maximal words are precisely those whose runs have lengths one or two. Each composition of \(n\) into ones and twos determines a run-length sequence, with two choices of initial symbol, giving \(2F_{n+1}\). If \(B(x)=1\), all adjacent outputs \(A_i\) are equal, so (6) forces \(x_i=x_{i+2}\) throughout. Equality with \(D_1\) then forces \(x_2=x_3\), hence the word is constant. Conversely a constant word has one output. The triple decomposition (1), accumulated by keeping the last ordered pair as state, proves (2).

**Step 4: exact moments.** Put \(Z_i=d(X_i,X_{i+1},X_{i+2})\). The event of three distinct symbols has probability \((q-1)(q-2)/q^2\), and three equal symbols has probability \(1/q^2\). Hence
\[
\mu_q=\mathbb E Z_i=\frac{q^2-3q+1}{q^2},\qquad
\gamma_0=\operatorname{Var}(Z_i)=\frac{(q-1)(3q^2-5q+1)}{q^4}.
\]
Conditional on the two shared symbols of successive triples, the two outer symbols are independent. Their common conditional mean is \(-1/q\) if the shared symbols are equal, and \((q-2)/q\) otherwise, giving
\[
\gamma_1=\operatorname{Cov}(Z_i,Z_{i+1})=\frac{(q-1)^3}{q^4}.
\]
For separation two, the triples share just one symbol; conditional expectations given that symbol are both the constant \(\mu_q\) by alphabet symmetry, so \(\gamma_2=0\). At larger separation the triples are disjoint and independent. Thus \(\operatorname{Var}(\sum Z_i)=(n-2)\gamma_0+2(n-3)\gamma_1\), proving (3)–(4).

**Step 5: limit law.** The bounded stationary sequence \((Z_i)\) is two-dependent. Partition its first \(n-2\) terms into blocks of length \(\lfloor n^{1/3}\rfloor\), separated by two discarded terms. Block sums are independent; the discarded sum has variance \(O(n^{2/3})=o(n)\), and the maximal absolute block sum is \(o(\sqrt n)\). The independent-block Lindeberg theorem, together with (4), gives (5). Its variance coefficient is strictly positive for every integer \(q\ge2\).

## Verification
The standalone `checker.py` enumerates each admissible deletion pair directly, with no reliance on (1), and compares its set of outputs against (1). It separately checks the full enumerator by ordered-pair dynamic programming, the extrema and their counts, and the rational mean and variance. Executing `python checker.py` passed 144555 direct word comparisons and 27 complete parameter profiles for \(q=2\) through \(5\). These finite checks are not presented as proof of the all-length statements; the preceding argument supplies that proof.

## Relationship to prior work
Ye, Sun and Ge (2025) study localized deletions and code constructions; Ye and Ge (2026) explicitly formalize the \((t,T)\)-localized model and construct codes correcting such errors, including \((2,3)\). Their inspected model, constructions, redundancy bounds and relevant result sections do not supply the exact sphere-volume formula (1), complete enumerator (2), or moments and limit (3)–(5). Bitar, Hanna, Polyanskii and Vorobyev (2021) study the earlier fixed-window localized model, principally code redundancy, rather than this exact-two-in-three sphere spectrum. Unrestricted two-deletion spheres and ordinary two-consecutive-deletion spheres are different channels and do not imply (1). These comparisons do not establish definitive publication priority.

## Limitations
This is a statement about source-word output-sphere sizes, not an optimal code-size theorem. It treats exact two deletions confined to three positions, not larger windows, variable deletion numbers, nonuniform or dependent inputs, or circular windows. The normal limit fixes \(q\) as \(n\) grows. The mathematical argument and finite checker have undergone a self-review only; independent validation and exhaustive historical priority review have not been performed.

## References
1. Z. Ye, Y. Sun, and G. Ge, *Correcting Bursty/Localized Deletions: A New Error-Position-Estimation Code*, arXiv:2507.04797v1, first public 7 July 2025. https://arxiv.org/html/2507.04797v1
2. Z. Ye and G. Ge, *Substring Edit Correcting Codes and Optimal Single Burst-Deletion Correcting Codes*, arXiv:2610.05696v1, first public 5 October 2026. https://arxiv.org/html/2610.05696v1
3. R. Bitar, J. Hanna, N. Polyanskii, and I. Vorobyev, *Optimal Codes Correcting Localized Deletions*, arXiv:2105.02298, 2021. https://arxiv.org/abs/2105.02298
