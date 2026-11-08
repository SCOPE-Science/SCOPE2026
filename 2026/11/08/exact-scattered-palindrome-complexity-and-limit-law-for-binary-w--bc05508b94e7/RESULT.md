# Exact scattered-palindrome complexity and limit law for binary words with three ones

## Finding
Let \(P(w)\) denote the number of **distinct nonempty palindromic subsequences** (scattered palindromic subwords) of a binary word \(w\). For all nonnegative integers \(a,b,c,d\), put
\[
w=0^a1\,0^b1\,0^c1\,0^d,\qquad z=a+b+c+d,
\]
\[
T=\max\{\min(a,b+c+d),\min(a+b,c+d),\min(a+b+c,d)\},
\quad r=\min(a,d),\quad s=\min(b,c),
\]
and
\[
E=\begin{cases}
\min(b,d-a)(c+1),&a\le d,\\
\min(c,a-d)(b+1),&a>d.
\end{cases}
\]
Then the complete exact gap formula is
\[
\boxed{P(w)=z+(T+1)+(r+1)(b+c+1)+E+(r+1)(s+1).}
\]

For each integer \(n\ge3\), independently choose \(W_n\) uniformly among the \(\binom n3\) binary length-\(n\) words with exactly three ones. Let \((A,B,C,D)\) be uniform on the simplex \(A,B,C,D\ge0\), \(A+B+C+D=1\), equivalently Dirichlet\((1,1,1,1)\). Set \(R=\min(A,D)\) and
\[
\Phi(A,B,C,D)=R\bigl(B+C+\min(B,C)\bigr)+
\begin{cases}
\min(B,D-A)\,C,&A\le D,\\
\min(C,A-D)\,B,&A>D.
\end{cases}
\]
Then
\[
\boxed{\frac{P(W_n)}{n^2}\ \xrightarrow{\mathrm d}\ \Phi(A,B,C,D)},
\]
and the limiting random variable has **positive variance**, with exact moments
\[
\boxed{\mathbb E\Phi=\frac7{80},\qquad
\operatorname{Var}(\Phi)=\frac{2299}{1209600}.}
\]
In fact, the first two moments of \(P(W_n)/n^2\) converge to these limits.

## Assumptions and scope
A subsequence may omit letters but must preserve order. Different choices of indices spelling the same palindrome count **once**. The empty subsequence does not count. Every triple of one-positions is equally likely in the random model; this is not the iid fair-bit model. The result covers every word with exactly three ones, including zero-length gaps and \(w=111\). All limits take \(n\) through positive integers tending to infinity.

## Proof
**Exact enumeration.** Every palindromic subsequence of \(w\) contains exactly \(k\in\{0,1,2,3\}\) ones. For \(k=0\), the distinct words are \(0,0^2,\ldots,0^z\), giving \(z\). For \(k=1\), all candidates are \(0^i1\,0^i\); selecting one of the three original ones as its center allows \(0\le i\le\min\{a,b+c+d\}\), \(\min\{a+b,c+d\}\), or \(\min\{a+b+c,d\}\), respectively. The union is the interval \(0\le i\le T\), giving \(T+1\).

For \(k=2\), all candidates are \(0^i1\,0^j1\,0^i\) and are uniquely specified by the ordered pair \((i,j)\). Using original one-positions \((1,2)\), \((2,3)\), or \((1,3)\) gives the respective integer rectangles
\[
[0,\min(a,c+d)]\times[0,b],\quad
[0,\min(a+b,d)]\times[0,c],\quad
[0,\min(a,d)]\times[0,b+c].
\]
If \(a\le d\), the first rectangle is contained in the third, and the part of the second beyond the third has \(\min(b,d-a)(c+1)\) points. The union therefore contains \((a+1)(b+c+1)+E\) points. If \(a>d\), the second rectangle is contained in the third and the first contributes \(\min(c,a-d)(b+1)\) extra points. This proves the \(k=2\) term for both boundary cases. For \(k=3\), every candidate has the unique form \(0^i1\,0^j1\,0^j1\,0^i\), with \(0\le i\le r\) and \(0\le j\le s\), so there are \((r+1)(s+1)\). The four \(k\)-classes are disjoint, establishing the formula for all gap quadruples.

**Limit law.** Each length-\(n\), weight-three word corresponds bijectively to a nonnegative composition of \(n-3\) into four gaps. The vector \((a,b,c,d)/n\) thus converges in distribution to uniform simplex measure, the stated Dirichlet vector. In the exact formula, the \(z\), \(T+1\), and all lower-degree terms are uniformly \(O(n)\); its homogeneous degree-two part is precisely \(\Phi(a/n,b/n,c/n,d/n)\). Therefore the difference between \(P(w)/n^2\) and \(\Phi(a/n,b/n,c/n,d/n)\) is uniformly \(O(1/n)\). Continuity of the \(\min\) expressions proves distributional convergence. Since all these normalized quantities are uniformly bounded, their first and second moments converge as well.

**Exact moments.** Let \(U_1,U_2,U_3,U_4\) be independent exponential random variables of mean one, and let \(S=U_1+U_2+U_3+U_4\). The normalized four-vector is Dirichlet\((1,1,1,1)\), independent of \(S\). By homogeneity, \(G=S^2\Phi(U_1/S,U_2/S,U_3/S,U_4/S)\). Let \(M=\min(U_1,U_4)\), \(\Delta=|U_1-U_4|\), \(B=U_2\), and \(C=U_3\). The independent random variables \(M\sim\mathrm{Exp}(2)\) and \(\Delta\sim\mathrm{Exp}(1)\) are independent of \(B,C\); conditional on the outer-gap orientation, symmetry in \(B,C\) shows that \(G\) has the same first two moments as \(MH+J\), where
\[
H=B+C+\min(B,C),\qquad J=\min(B,\Delta)C.
\]
The exponential moment identities, with a split of the integrals at \(B=C\), give
\[
\mathbb EM=\tfrac12,\quad \mathbb EM^2=\tfrac12,\quad
\mathbb EH=\tfrac52,\quad \mathbb EH^2=\tfrac{19}2,
\]
\[
\mathbb EJ=\tfrac12,\quad\mathbb EJ^2=1,\quad
\mathbb E(HJ)=\tfrac{41}{18}.
\]
For clarity, the only mixed integral is evaluated by conditioning on \(B\): \(\mathbb E[\min(B,\Delta)\mid B]=1-e^{-B}\). Then
\[
\mathbb E(HJ)=\tfrac34+1+\tfrac34-
\mathbb E[e^{-B}C\min(B,C)],
\]
where splitting \(B\le C\) and \(C<B\) yields respectively \(5/27\) and \(1/27\), giving \(41/18\). Consequently
\[
\mathbb EG=\tfrac74,\qquad \mathbb EG^2=\tfrac{289}{36}.
\]
Finally \(S\sim\mathrm{Gamma}(4,1)\) has \(\mathbb ES^2=20\) and \(\mathbb ES^4=840\), independently of its normalized direction. Thus \(\mathbb E\Phi=\frac{7/4}{20}=7/80\) and \(\mathbb E\Phi^2=\frac{289/36}{840}=289/30240\). Subtracting the squared mean gives \(2299/1209600>0\), as claimed.

## Verification
Run `python3 verify.py` with Python 3 and no external dependencies. It separately builds all distinct subsequences, removes duplicates and tests palindromicity for all \(\sum_{n=3}^{18}\binom n3=3876\) binary weight-three words of lengths \(3\) through \(18\), checking the gap formula against that independent algorithm. It also recomputes the exact exponential-integral moment identities using rational arithmetic. A successful run prints `GAP_FORMULA_OK 3876` and `RATIONAL_MOMENTS_OK 7/80 2299/1209600`. Finite checks corroborate but do not replace the unrestricted proof above.

## Relationship to prior work
Holub and Saari study **scattered** palindromic subwords and prove that their full set determines a binary word up to reversal; they do not give this fixed-weight cardinality formula or law. Rubinchik and Shur study the expected number of distinct palindromic **factors**, which must be contiguous, in an iid uniform-word model; neither the object nor the distribution is the present one. Mahalingam and Pandoh study scattered-palindrome counts, prove general alphabet-dependent bounds and determine unrestricted extremal formulas when the number of distinct letters is at least half the length. Their finite tables and general bounds do not imply this exact three-one gap formula or its conditional limit law. Published results concerning distinct subsequences without a palindromicity constraint also address a different statistic. These distinctions concern logical coverage, not only matching terminology.

## Limitations
The count is restricted to exactly three ones and a binary alphabet; it is not a formula for arbitrary composition or for palindromic factors. The limiting law is specified as a pushforward of uniform simplex measure, not by a closed elementary density. No claim of exact all-length extremizers, general higher-weight formulas, or independent external verification is made. As with any literature review, equivalent unindexed formulations cannot be excluded categorically.

## References
- Š. Holub and K. Saari, *On highly palindromic words*, Discrete Applied Mathematics 157 (2009), 953–959; DOI: https://doi.org/10.1016/j.dam.2008.03.039 ; lawful author manuscript: https://www.karlin.mff.cuni.cz/~holub/soubory/subpal.pdf .
- M. Rubinchik and A. M. Shur, *The Number of Distinct Subpalindromes in Random Words*, arXiv:1505.08043v1, public preprint May 29, 2015: https://arxiv.org/pdf/1505.08043 .
- K. Mahalingam and P. Pandoh, *Counting Scattered Palindromes in a Finite Word*, arXiv:2108.02729v1, August 5, 2021: https://arxiv.org/pdf/2108.02729 .
- C. H. Elzinga, S. Rahmann and H. Wang, *Algorithms for subsequence combinatorics*, Theoretical Computer Science 409 (2008), 394–404; DOI: https://doi.org/10.1016/j.tcs.2008.08.035 .
