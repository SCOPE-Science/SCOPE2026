# Adjacent-generator common centralizers in type-A 0-Hecke monoids

## Finding

Let \(H_n=H_0(S_n)\) be the type-A 0-Hecke **monoid**, with standard idempotent generators \(\pi_1,\ldots,\pi_{n-1}\). For \(n\ge4\) and \(1\le i\le n-2\), define the common centralizer
\[
C_{n,i}=\{u\in H_n:u\pi_i=\pi_i u\ \text{and}\ u\pi_{i+1}=\pi_{i+1}u\}.
\]
Put \(m=n-3\) and
\[
D_n=\sum_{t=0}^{\min(3,m)}\binom mt^2(m-t)!.
\]
Then the complete positional centralizer spectrum is
\[
\boxed{|C_{n,i}|=D_n+m!+\bigl((i-1)^2+(n-i-2)^2\bigr)(n-4)!.}
\]
The four disjoint contributing strata, indexed by \((D,D),(D,F),(F,D),(F,F)\) as defined in the proof, have respective cardinalities
\[
D_n,\qquad(n-i-2)^2(n-4)!,\qquad(i-1)^2(n-4)!,\qquad(n-3)!.
\]
Consequently, among the \(n-2\) adjacent pairs, there are exactly \(\lfloor(n-3)/2\rfloor+1\) distinct cardinalities. The smallest occurs at the middle pair(s), and the largest at the two boundary pairs; each noncentral size occurs twice and the central size occurs once when \(n-3\) is even, otherwise twice. The exact maximum-minus-minimum gap is
\[
2\left\lfloor\frac{n-3}{2}\right\rfloor
\left\lceil\frac{n-3}{2}\right\rceil(n-4)!.
\]
Uniformly over \(1\le i\le n-2\),
\[
\frac{|C_{n,i}|}{n!}=\frac1{36}+O(n^{-1}).
\]
In the ordinary symmetric group \(S_n\), the simultaneous centralizer of the corresponding adjacent transpositions has only \((n-3)!\) elements. For the exceptional case \(n=3\), the 0-Hecke common centralizer consists of the identity and the longest element, hence has size two.

## Assumptions and scope

The monoid has presentation \(\pi_j^2=\pi_j\), \(\pi_j\pi_{j+1}\pi_j=\pi_{j+1}\pi_j\pi_{j+1}\), and \(\pi_j\pi_k=\pi_k\pi_j\) when \(|j-k|>1\). Its \(n!\) elements are indexed by permutations \(w\in S_n\) using reduced words and the Demazure product. The convention is that right multiplication by \(\pi_j\) swaps values at positions \(j,j+1\) if they are increasing, and left multiplication swaps the positions of values \(j,j+1\) if those positions are increasing. Centralizers are taken in the **monoid**, not in its linear monoid algebra. All asserted counts are exact integers and hold for every allowed \(n,i\).

## Proof

**1. The one-generator dichotomy.** Write \(w\) in one-line notation, and \(w^{-1}\) for its inverse permutation. Directly from the Demazure multiplication rule, \(\pi_w\pi_j=\pi_j\pi_w\) precisely in either of two disjoint situations:

* \(D_j\): \(w(j)>w(j+1)\) **and** \(w^{-1}(j)>w^{-1}(j+1)\). Both products equal \(\pi_w\).
* \(F_j\): \(w(j)=j\) **and** \(w(j+1)=j+1\). Neither side is absorbing; the two resulting length-increasing products agree.

To justify that there is no third case: if exactly one descent holds, the two products have different Coxeter lengths. If neither descent holds, both are length-increasing; equality means \(s_jw=ws_j\) in the symmetric group. This forces \(w\) to preserve the set \(\{j,j+1\}\). The nontrivial swap of these two elements would make both descents hold; hence both must be fixed.

**2. Decompose the simultaneous centralizer.** For the adjacent indices \(i,i+1\), the two independent choices \(D\) or \(F\) give disjoint strata. In \(F_i\cap F_{i+1}\), all three positions \(i,i+1,i+2\) are fixed, leaving \((n-3)!\) permutations.

In \(F_i\cap D_{i+1}\), positions \(i,i+1\) are fixed. The value at position \(i+2\) must belong to \(\{1,\ldots,i-1\}\), and the position of value \(i+2\) must belong to the same earlier interval. Their choices give two disjoint prescribed matrix entries, so there are \((i-1)^2(n-4)!\) completions. Similarly, \(D_i\cap F_{i+1}\) requires the value at position \(i\) and the position of value \(i\) both to be chosen from \(\{i+3,\ldots,n\}\), giving \((n-i-2)^2(n-4)!\) completions.

**3. The double-descent stratum.** Let \(B=\{i,i+1,i+2\}\), \(T=\{1,\ldots,n\}\setminus B\), and let \(W_B\cong S_3\) be the parabolic subgroup permuting \(B\) and fixing \(T\). The condition \(D_i\cap D_{i+1}\) says precisely that both the left and the right descent sets contain \(\{i,i+1\}\). The standard finite Coxeter parabolic double-coset theorem says that every \(W_B\)-double coset of \(S_n\) has exactly one maximal-length representative, characterized by these left and right descents. Thus \(|D_i\cap D_{i+1}|\) equals the number of double cosets \(W_B\backslash S_n/W_B\).

A double coset is uniquely specified by the partial bijection obtained by retaining exactly the arrows \(a\mapsto w(a)\) with \(a\in T\) and \(w(a)\in T\). Indeed the left and right \(W_B\)-actions merely relabel the values and positions in \(B\), and act transitively on all completions of any fixed partial bijection on \(T\). That partial bijection omits exactly \(t\) of the \(m\) domain positions and exactly \(t\) of the \(m\) range values, where \(0\le t\le\min(3,m)\) because only three positions lie in \(B\). Choose its omitted domain and range sets and then biject the remaining \(m-t\) positions. The number is
\[
\sum_{t=0}^{\min(3,m)}\binom mt^2(m-t)!=D_n.
\]
Adding the four strata proves the count.

**4. Spectrum, extrema and limit.** Set \(a=i-1\); then \(n-i-2=m-a\). The only position-dependent term is \(a^2+(m-a)^2\), symmetric under \(a\leftrightarrow m-a\), strictly decreasing toward the midpoint and increasing afterward. This yields the distinct-value count, multiplicities, and maximum-minus-minimum formula. As \(n\to\infty\), the \(t=3\) term in \(D_n\) is \(n!/36\,(1+O(n^{-1}))\), while the terms with \(t\le2\) contribute \(O(n!/n)\); the remaining strata contribute \(O(n!/n^2)\), uniformly in \(i\). Finally, commuting with adjacent transpositions in \(S_n\) means centralizing the full \(S_3\) on \(B\); its centralizer fixes \(B\) pointwise and permutes \(T\), so has \((n-3)!\) elements.

## Verification

A standalone checker uses **actual left and right Demazure multiplication**, not the dichotomy as its acceptance criterion. It enumerates all permutations for \(3\le n\le9\), compares direct products for both adjacent generators, separately checks the dichotomy and all four strata, and verifies the displayed closed formula. Observed centralizer sizes for consecutive \(i\) are:

| \(n\) | Counts from the left boundary to the right boundary |
|---|---|
| 3 | 2 |
| 4 | 4, 4 |
| 5 | 13, 11, 13 |
| 6 | 58, 50, 50, 58 |
| 7 | 328, 292, 280, 292, 328 |
| 8 | 2240, 2048, 1952, 1952, 2048, 2240 |
| 9 | 17880, 16680, 15960, 15720, 15960, 16680, 17880 |

Run `python3 check_hecke.py`; the captured output is supplied in `checker_output.txt`. Exhaustive checks validate only these finite instances; the all-dimensional statement follows from the preceding argument, not from enumeration.

## Relationship to prior work

The Demazure generators, permutation indexing, and descent multiplication are classical and explicitly taken as background, notably from Hivert–Schilling–Thiéry (2009). Denton–Hivert–Schilling–Thiéry (2010) describe 0-Hecke and related \(\mathcal J\)-trivial representation theory, and Hivert–Schilling–Thiéry (2010) develop biHecke monoids; neither result as inspected provides the all-element common-centralizer sizes for two fixed adjacent generators. The double-descent count uses the standard parabolic double-coset theorem, not a new theorem about double cosets. The additional mixed fixed-point/descent strata produce the explicit location-dependent centralizer spectrum. The 2025 work on centralizers of generic Hecke **algebras** assumes invertible quadratic parameters and concerns a linear-algebra centralizer; it does not directly specialize to these basis-element counts in the 0-Hecke monoid.

## Limitations

The result counts simultaneous centralizers only for pairs of **adjacent** standard generators of the type-A 0-Hecke monoid; it does not classify arbitrary pairs, entire centralizer submonoids up to isomorphism, or centralizers in the monoid algebra. A wider unlocated formula for monoid centralizers might subsume the count. The archival 2009 source supplies the underlying monoid, not the present enumeration. No independently performed mathematical validation is claimed.

## References

1. F. Hivert, A. Schilling, N. M. Thiéry, *The biHecke monoid of a finite Coxeter group*, arXiv:0912.2212, first publicly posted 2009-12-11. https://arxiv.org/abs/0912.2212
2. T. Denton, F. Hivert, A. Schilling, N. M. Thiéry, *On the representation theory of finite J-trivial monoids*, arXiv:1010.3455, 2010-10-17. https://arxiv.org/abs/1010.3455
3. F. Hivert, A. Schilling, N. M. Thiéry, *The biHecke monoid of a finite Coxeter group and its representations*, arXiv:1012.1361, 2010-12-06. https://arxiv.org/abs/1012.1361
4. H. Chen, *Centralizers in Hecke Algebras of Any Coxeter Group*, arXiv:2508.14473, 2025-08-20. https://arxiv.org/abs/2508.14473
