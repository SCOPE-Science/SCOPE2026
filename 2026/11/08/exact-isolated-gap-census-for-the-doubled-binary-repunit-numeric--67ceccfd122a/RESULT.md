# Exact isolated-gap census for the doubled binary-repunit numerical semigroups

## Finding
For each integer \(n\ge3\), set \(h=2^{n-1}\), \(m=2^n-1=2h-1\), and
\[
S_n=\big\langle m,\ m+2(2^j-1):1\le j<n\big\rangle.
\]
An isolated gap is a positive integer \(g\notin S_n\) satisfying \(g-1,g+1\in S_n\). Then its entire set and cardinality are explicit. Let \(c(t)\) be the minimum number of coins in a representation of \(t\) using the Mersenne denominations \(2^j-1\) for \(1\le j<n\), with \(c(0)=0\). For \(0\le t\le h-2\), put \(\delta_t=c(t+1)-c(t)\in\{-1,1\}\). The set of isolated gaps is exactly
\[
\begin{split}
I(S_n)={}&\{mc(t+1)+2(h+t):0\le t\le h-2\}\\
&\quad\cup\{m(c(t+1)-1)+2(h+t):0\le t\le h-2,\ \delta_t=1\}.
\end{split}
\]
These sets are disjoint, and
\[
\boxed{|I(S_n)|=3\cdot2^{n-2}-1.}
\]
The same formula holds at \(n=2\), already within the established embedding-dimension-two theory. The new infinite-family classification concerns \(n\ge3\), where the embedding dimension equals \(n\).

## Assumptions and scope
All semigroups are submonoids of the nonnegative integers. The generators above are exactly the case \(a=2,b=2\) of the generalized repunit semigroups of Branco, Colaço, and Ojeda, whose first generator is \(m\). Since \(m\) is odd, the gcd of the generators is one. The source's Theorems 6 and 15 establish minimal embedding dimension \(n\) and an explicit Apéry set. The Apéry representative \(w_r\) is the smallest semigroup element congruent to residue \(r\pmod m\); a positive integer of residue \(r\) belongs to the semigroup if and only if it is at least \(w_r\).

## Proof
**1. Apéry parametrization.** For every \(T\in\{0,\ldots,m-1\}\), let
\[
W(T)=m c(T)+2T,\qquad r_T\equiv2T\pmod m.
\]
We first show that \(W(T)=w_{r_T}\). Theorem 15 of Branco–Colaço–Ojeda gives the Apéry representatives from canonical vectors \((u_2,\ldots,u_n)\) with digits \(0,1,2\), where any digit \(2\) forces all earlier digits to vanish. The weighted Mersenne sums \(\sum_{j=2}^n u_j(2^{j-1}-1)\) run bijectively through \(0,\ldots,m-1\): by induction on the last digit they comprise two consecutive translated copies of the previous interval and its final endpoint (equivalently the recursion for \(R(2,n)\) given immediately before that theorem). For each such vector the Apéry element is \(m\sum u_j+2T\). If fewer than \(\sum u_j\) Mersenne coins represented \(T\), the corresponding sum of semigroup generators would be a smaller element of the same residue, impossible by the Apéry property. Hence \(\sum u_j=c(T)\), and the displayed formula follows. Because \(m\) is odd, \(T\mapsto r_T\) is a bijection.

**2. Unit-step coin lemma.** For every \(0\le t<m-1\),
\[
c(t+1)-c(t)\in\{-1,1\}.
\]
Every denomination is odd, so \(c(t)\equiv t\pmod2\); consequently this difference is odd. Adding one unit coin proves \(c(t+1)\le c(t)+1\). Conversely, take an optimal representation of \(t+1\). Remove a unit coin if one occurs. Otherwise replace one coin \(2^j-1\) of size at least three by two coins \(2^{j-1}-1\), lowering the represented value by one and increasing the number of coins by one. Thus \(c(t)\le c(t+1)+1\). Both bounds force the claim.

**3. Shift identity.** For \(0\le t\le h-2\),
\[
\boxed{c(h+t)=1+c(t+1).}
\]
The coin of value \(h-1\), together with a representation of \(t+1\), gives the inequality \(\le\). For the reverse inequality put \(\ell=c(h+t)\). We have \(2\le\ell\le t+2\), since \(h+t\) exceeds the largest available coin \(h-1\). Replacing each denomination \(2^j-1\) in an optimal representation by \(2^j\) yields a representation of \(h+t+\ell\) as \(\ell\) powers of two, each at least two. Thus the binary digit sum satisfies \(s_2(h+t+\ell)\le\ell\). Put \(v=t+\ell\); it is even because the parity of \(\ell\) equals the parity of \(h+t\), and \(h\) is even.

If \(v<h\), then \(s_2(h+v)=1+s_2(v)\), hence \(s_2(v)\le\ell-1\). If \(v\ge h\), write \(v=h+u\) with even \(0\le u\le\ell-2\) (from \(t\le h-2\)); then \(s_2(v)=1+s_2(u)\le1+u/2\le\ell-1\). In either case \(v\) is even, \(s_2(v)\le\ell-1\), and \(v\ge2(\ell-1)\) because \(\ell\le t+2\). Therefore \(v\) is a sum of exactly \(\ell-1\) powers of two, each at least two: start with its binary decomposition and repeatedly split a power of at least four into two equal halves until the desired number of summands is attained. (The number of summands varies from \(s_2(v)\) up to \(v/2\).) Each power is at most \(h\) because \(v\le2h-2\) and no binary summand exceeds \(h\); splitting never increases it. Subtract one from each power. This writes \(t+1=v-(\ell-1)\) using \(\ell-1\) allowed Mersenne coins, so \(c(t+1)\le\ell-1\). Equality follows.

**4. Exact isolated-gap thresholds.** Fix \(T\in[0,m-1]\). Positive gaps in residue \(r_T\) have the form \(g=W(T)-km\), \(k\ge1\), whenever positive. Since \(2h=m+1\), the residues of \(g\pm1\) correspond to indices \(T\pm h\pmod m\). The neighboring integers are in \(S_n\) precisely when
\[
 k\le\min\left\{\frac{W(T)-1-W((T-h)\bmod m)}m,\frac{W(T)+1-W((T+h)\bmod m)}m\right\}.
\]
Each quotient is an integer, as its numerator is divisible by \(m\).

If \(0\le T\le h-2\), the second quotient equals \(c(T)-c(T+h)-1=-2-(c(T+1)-c(T))\), hence is negative. For \(T=h-1\), the first quotient equals \(c(h-1)-c(m-1)-1=1-2-1=-2\). None of these indices yields isolated gaps.

For \(T=h+t\), \(0\le t\le h-2\), the corresponding indices are \(t\) and \(t+1\). The two integer quotients are respectively
\[
1+c(h+t)-c(t)=2+\delta_t,\qquad
1+c(h+t)-c(t+1)=2.
\]
Thus the allowable \(k\) are precisely \(\{1\}\) when \(\delta_t=-1\), and \(\{1,2\}\) when \(\delta_t=1\). All these gap positions are positive, since \(W(h+t)-2m=m(c(t+1)-1)+2(h+t)>0\). Substitution in \(W(h+t)-km\) gives exactly the two disjoint sets in the finding.

**5. Counting.** Among the \(h-1\) steps \(t=0,\ldots,h-2\), let \(U\) and \(D\) be the numbers of increments \(+1\) and \(-1\). Then \(U+D=h-1\), while the telescoping sum gives \(U-D=c(h-1)-c(0)=1\), since \(h-1\) itself is one coin. Hence \(U=h/2\). Every step contributes one gap and the \(U\) rising steps one more. Thus
\[
 |I(S_n)|=(h-1)+h/2=3h/2-1=3\cdot2^{n-2}-1.
\]
This completes the proof for every \(n\ge3\).

## Verification
Run `python3 verify_shift2_gaps.py` using only the Python standard library. The checker independently computes all Apéry elements by Dijkstra on residue classes, the Mersenne coin minima by dynamic programming, and ALL isolated gaps below the Frobenius number by direct exhaustive testing for \(2\le n\le10\). The observed output was `VERIFY_OK n_cases=9 apery_residues=2035 isolated_gaps=1524 full_gap_census=complete`. Finite checks corroborate but do not prove the unbounded theorem; the proof above establishes it.

## Relationship to prior work
Branco–Colaço–Ojeda establish the generator and Apéry machinery for all generalized repunit semigroups (Theorems 6 and 15); their paper derives Frobenius, genus, and type formulas rather than the present isolated-gap census. Moreno-Frías–Rosales define and study isolated gaps and perfect semigroups via covarieties; they do not give this explicit doubled-binary-repunit count. Singh–Ram classify embedding-dimension-two isolated gaps; their theorem encompasses the ancillary \(n=2\) case but not the unbounded-dimension assertion. Smith develops general Apéry-based isolated-gap results; its abstract was available but its full publisher text could not be inspected, so coverage by that source remains a residual bibliographic risk. The distinct undoubled-repunit case \(a=1\) has a separate isolated-gap formula; it does not imply this \(a=2\) formula. The present work uses a specialized coin-shift lemma to supply the new enumeration.

## Limitations
This theorem concerns exactly the binary generalized repunit family with coefficient \(a=2\), not other bases or all coefficients. The proof relies on the published Apéry characterization; it is not a new derivation of that theorem. The result does not determine broader gap distributions or classifications under other semigroup operations. Bibliographic searches cannot establish absolute priority; an inaccessible full text of Smith remains a specified risk. No independent validation has been performed.

## References
1. M. B. Branco, I. Colaço, I. Ojeda, *The Frobenius problem for generalized repunit numerical semigroups*, arXiv:2112.01106 (first public 2021-12-02), Theorems 6, 15. https://arxiv.org/abs/2112.01106
2. M. A. Moreno-Frías, J. C. Rosales, *The covariety of perfect numerical semigroups with fixed Frobenius number*, arXiv:2305.14967 (first public 2023-05-24). https://arxiv.org/abs/2305.14967
3. B. Singh, R. Ram, *On Isolated Gaps of Numerical Semigroups of Embedding Dimension Two*, arXiv:2406.09848 (2024). https://arxiv.org/abs/2406.09848
4. D. Smith, *On isolated gaps in numerical semigroups*, Turkish Journal of Mathematics 46 (2022), 123–129, doi:10.3906/mat-2107-54.
