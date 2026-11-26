# Rank-refined centralizers reconstruct nonconstant directed-path clamps up to reflection

## Finding
Let \(n\geq1\), and let \(W_n\) consist of all full maps \(f:[n]\to[n]\) whose adjacent increments \(f(i+1)-f(i)\) lie in \(\{0,1\}\). This is simultaneously the weak-endomorphism monoid of the directed path, the monoid of order-preserving maps with interval image, and the monoid of nondecreasing chain contractions. Its idempotents are precisely the interval clamps \(e_{a,b}(i)=\min\{b,\max\{a,i\}\}\), with \(1\le a\le b\le n\).

Put \(A=a-1\), \(k=b-a\), \(B=n-b\), \(N=n-1=A+k+B\), and \(t=1+z\). For use in the reconstruction and the pair laws below, mark the rises in the previously established clamp-centralizer decomposition. This gives the **image-rank polynomial of the full composition-centralizer** of a clamp:
\[
\boxed{C_{a,b}(z)=\sum_{f\in W_n:\,fe_{a,b}=e_{a,b}f}z^{|\operatorname{im}f|-1}
=t^{k-1}(k+1+z)+(t^A+t^B-2)t^k+(t^A-1)(t^B-1)z^k.}
\]
The formula also holds at \(k=0\), interpreting \(t^{-1}(1+z)=1\), and then \(C_{a,a}(z)=t^N\). All exponents of \(z\) in the polynomial are nonnegative integers.

For every \(k\ge1\), the **coefficients of degrees zero and two alone** recover the clamp interval up to reversal of the ambient chain: writing \(c_j=[z^j]C_{a,b}(z)\),
\[
\boxed{k=c_0-1,\qquad AB=\binom{N-k}{2}+\binom{k}{2}(k-1)+k(N-k)-c_2.}
\]
Since \(A+B=N-k\), the unordered pair \(\{A,B\}\) is the set of roots, with multiplicity, of \(X^2-(N-k)X+AB\). Consequently, two nonconstant clamps have identical centralizer rank polynomials **if and only if** they are equal or mirror images under order reversal. All constant clamps have the same polynomial \(t^N\), irrespective of position, and their polynomial differs from that of every nonconstant clamp.

The complete joint polynomial over all idempotent–arbitrary commuting pairs has the following rational three-variable generating function, where \(x\) marks \(n-1\), \(y\) marks the clamp's image-rank excess \(k\), and \(z\) marks the commuting map's image-rank excess:
\[
\begin{aligned}
G(x,y,z)&=\sum_{N\ge0}x^N\sum_{A+k+B=N}y^k C_{A,k,B}(z)\\
&=\frac{1-zxy}{(1-x)^2(1-(1+z)xy)^2}
+\frac{2zx}{(1-x)^2(1-(1+z)x)(1-(1+z)xy)}\\
&\qquad+\frac{z^2x^2}{(1-x)^2(1-(1+z)x)^2(1-zxy)}.
\end{aligned}
\]
Here \(C_{A,k,B}\) denotes the polynomial above at gaps \(A,k,B\). In particular, the aggregate rank series has a notably simple product form:
\[
\boxed{G(x,1,z)=\frac{1}{(1-x)^2(1-zx)(1-(1+z)x)^2}.}
\]
Equivalently, the coefficient of \(z^j\) in the aggregate rank polynomial at fixed \(N\) is
\[
\sum_{i+h+\ell=N}(i+1)(\ell+1)\binom{\ell}{j-h},
\]
with out-of-range binomial coefficients zero.

If an ordered pair \((E,F)\) is sampled **uniformly among pairs with \(E\) idempotent and \(EF=FE\)**, then its second-coordinate image rank satisfies the Gaussian limit
\[
\boxed{\frac{2|\operatorname{im}F|-n}{\sqrt{n-1}}\ \Longrightarrow\ \mathcal N(0,1),\qquad n\to\infty.}
\]
This last limit is for uniform commuting pairs, not for choosing a uniformly random idempotent and then choosing a uniform element of its centralizer.

## Assumptions and scope
All maps are full transformations of \([n]=\{1,\ldots,n\}\) and commute under composition. The rank is the *cardinality of the image*, not generator rank, linear rank, or rank of a semigroup. The centralizer is taken within \(W_n\), not the full transformation monoid. The exact formulas hold for every positive integer \(n\), including \(n=1\), \(k=0\), \(A=0\), and \(B=0\). The order-reversal symmetry is conjugation by the reversing permutation in the full transformation monoid, inducing an automorphism of \(W_n\); it is not generally conjugation by a unit of \(W_n\), whose only unit is the identity.

The clamp classification, endpoint decomposition, unrefined centralizer cardinalities \(C_{a,b}(1)\), and unrefined total number of commuting pairs were established earlier. The per-clamp rank polynomial is the direct rise-marking refinement of that decomposition and is included as an ingredient. The contribution here is the two-coefficient reconstruction, the joint and factored aggregate series, and the image-rank limit under uniform sampling of commuting pairs.

## Proof
**1. Binary increments and exact commuting criterion.** An idempotent fixes its interval image pointwise, and all values outside that interval must equal the nearest endpoint because the map is monotone and its image stays within the interval. Thus the only idempotents are the specified clamps. An element of \(W_n\) is determined by its starting value and \(N\) binary adjacent increments. Fix a clamp \(e_{a,b}\), and let \(p=f(a)\), \(q=f(b)\). Commutation on the fixed image interval \([a,b]\) forces \(a\le p\le q\le b\). On the \(A\) edges left of \(a\), if \(p=a\), all binary step choices are valid, with starting value determined by the ending value; otherwise every step must be zero. On the \(B\) edges right of \(b\), if \(q=b\), all binary step choices are valid; otherwise every step must be zero. Conversely these choices and the interior condition imply commutation at every point. The ambient range bounds automatically hold, since an extension of length \(A\) ending at \(a\) cannot start below \(1\), and an extension of length \(B\) starting at \(b\) cannot finish above \(n\).

For an interior walk of length \(k\), let \(h=q-p\) be its number of upward steps and write \(p=a+s\). For any \(0\le h\le k\), there are \(\binom{k}{h}\) step words and \(0\le s\le k-h\). Each such word contributes \(z^h\), multiplied by \(t^A\) exactly if \(s=0\), and by \(t^B\) exactly if \(s+h=k\). Both enhancements occur simultaneously only for \(h=k,s=0\). The weight \(z^{|\operatorname{im}f|-1}\) is \(z\) to the total number of upward steps, because the image is an interval.

**2. Rank polynomial.** Starting with both endpoint multipliers equal to one gives
\[
\sum_{h=0}^k(k-h+1)\binom{k}{h}z^h
=t^{k-1}(k+1+z).
\]
The left and right enhancements contribute \((t^A-1)t^k\) and \((t^B-1)t^k\), respectively, and their intersection contributes \((t^A-1)(t^B-1)z^k\). Adding yields the claimed polynomial. For \(k=0\), both endpoint enhancements always apply and the expression reduces to \(t^{A+B}\).

**3. Reconstruction.** For \(k\ge1\), the constant coefficient is the number of constant maps taking a value in \([a,b]\), hence \(c_0=k+1\). The coefficient of \(z^2\) in the base term is \(\binom{k}{2}(k-1)\); the two single-endpoint corrections add \(k(A+B)+\binom{A}{2}+\binom{B}{2}\). The double-endpoint correction has degree at least \(k+2\ge3\), and contributes nothing to \(c_2\). Thus
\[
c_2=\binom{k}{2}(k-1)+k(A+B)+\binom{A}{2}+\binom{B}{2}.
\]
Using \(\binom{A}{2}+\binom{B}{2}=\binom{A+B}{2}-AB\) gives the displayed reconstruction formula. Conversely, the polynomial expression is symmetric in \(A,B\). Reversing the finite chain exchanges these gaps, proving the precise equality classification. The \(k=0\) exception is necessary: all constant clamps have identical \(t^N\).

**4. Rational joint series.** Sum the base term of Step 2 over \(A,B\ge0\), each contributing \((1-x)^{-1}\), and over \(k\ge0\) with weight \((xy)^k\). This yields \((1-zxy)/((1-x)^2(1-txy)^2)\). Summing either single-endpoint enhancement uses
\[
\sum_{A\ge0}(t^A-1)x^A=\frac{zx}{(1-tx)(1-x)},
\]
and gives the middle summand of \(G\). Summing the product of two enhancements and the \(z^k\) factor gives the last summand. At \(y=1\), common denominators simplify the numerator to one, giving the stated product for \(G(x,1,z)\). Expanding its four geometric factors yields the nonnegative finite coefficient sum. Setting \(z=1\) reproduces the **already known** unrefined aggregate count; that specialization is a consistency check, not a separate novelty claim.

**5. Gaussian limit.** Let \(F_N(z)=[x^N]G(x,1,z)\). For complex \(z\) in a fixed small neighborhood of \(1\), the dominant pole in \(x\) is the double pole at \(x=(1+z)^{-1}\); the poles at \(1\) and \(z^{-1}\) are uniformly farther from the origin. Evaluating the analytic factor at the dominant pole gives \((1+z)^3/z^2\), hence, uniformly near \(z=1\),
\[
F_N(z)=(N+1)\frac{(1+z)^{N+3}}{z^2}\bigl(1+O(N^{-1})\bigr).
\]
For a uniform commuting pair, the probability generating function of \(|\operatorname{im}F|\) is \(zF_N(z)/F_N(1)\). Therefore, uniformly for \(z\) near one, it equals
\[
z^{-1}\left(\frac{1+z}{2}\right)^{N+3}\bigl(1+O(N^{-1})\bigr).
\]
With \(z=\exp(2s/\sqrt N)\), centering at \((N+1)/2\) gives the limiting moment generating function \(\exp(s^2/2)\) for each fixed real \(s\) near zero, proving the claimed weak convergence to a standard normal. This argument uses an exact generating function, not finite sampling.

## Verification
Run `python3 verify_path_rank_centralizers.py` using only the Python standard library. The script constructs every map from binary increments, computes commutation pointwise, and compares the complete second-coordinate image-rank distributions with the derived polynomial for all \(1\le n\le11\). This covers \(286\) idempotent centralizers across these sizes. It separately checks the aggregate rational-factor coefficient convolution, the known unrefined count, and reconstruction signatures for all \(2\le n\le35\). Its expected final line is `RANK_REFINED_PATH_CENTRALIZERS_VERIFIED; cases=286`.

For \(n=4\), a constant clamp has polynomial \(1+3z+3z^2+z^3\), while the interior clamp to \([2,3]\) has \(2+3z+2z^2+z^3\). Both unrefined centralizers have cardinality \(8\), but their rank polynomials are distinct. The aggregate commuting-pair totals for \(n=4\) and \(n=11\) are \(102\) and \(65{,}658\), respectively. The finite checks corroborate the algebraic derivation; they do not by themselves prove the unbounded assertions.

## Relationship to prior work
Fernandes and Paulista (arXiv:2112.13427v1, publicly posted 2021-12-26) establish the directed-path weak-endomorphism normal form, cardinality, idempotent enumeration and generator rank. Fernandes (arXiv:2407.05084v1, 2024-07-06) identifies the same monoid as order-preserving full maps with interval image, and presents it by generators and relations. The cited results do not give the positional reconstruction from the two centralizer coefficients.

Two earlier results give **the identical per-idempotent centralizer cardinality** for this monoid under alternative nomenclature: *Centralizer profiles and a quadratic limit law for idempotent finite-chain contractions* (2026-10-25) and *Idempotent centralizers and commuting semilattices in a finite directed-path monoid* (2026-11-02). Their proofs already give the endpoint criterion, count the interior words by their numbers of rises, and count the outer binary words that occur when the appropriate endpoints are hit. Marking each rise by \(z\) in that decomposition directly yields the per-clamp rank polynomial used here; the formula is not asserted as an independent contribution. Neither earlier record states the two-coefficient positional reconstruction, the trivariate generating function, or the image-rank limit for uniform commuting pairs. The second also gives the unrefined ordered commuting-pair count, which the aggregate formula recovers at \(z=1\).

Konieczny and Korkmaz's 2026 work on centralizers in Catalan monoids concerns decreasing order-preserving maps, a different monoid, and does not imply the current equal-increment weighted rank spectrum. Existing full-transformation centralizer theorems give general structural criteria but do not themselves provide the restricted rank-weighted enumeration here. The closest previously published rank-refined iteration result, *Eventual-image fibers and independent geometric–Gaussian limits in directed-path weak endomorphisms* (2026-11-01), concerns all maps stratified by their eventual fixed interval, rather than maps commuting with a separately chosen clamp.

## Limitations
The theorem treats only centralizers of idempotent maps, not arbitrary centralizers. The rank-polynomial invariant deliberately cannot distinguish positions of constant clamps; a reversal of the ambient chain need not be conjugation by a unit inside the monoid. The normal limit is for uniform commuting *pairs*, not a uniformly sampled clamp followed by uniform sampling in its centralizer. The per-clamp rise marking and the previously known unrefined counts are inputs to the reconstruction and pair-rank analysis. Complete historical priority against all monoid literature is not established.

## References
1. V. H. Fernandes and T. Paulista, *On the Rank of Monoids of Endomorphisms of a Finite Directed Path*, arXiv:2112.13427v1 (2021-12-26), https://arxiv.org/abs/2112.13427.
2. V. H. Fernandes, *On the monoid of order-preserving transformations of a finite chain whose ranges are intervals*, arXiv:2407.05084v1 (2024-07-06), https://arxiv.org/abs/2407.05084.
3. *Centralizer profiles and a quadratic limit law for idempotent finite-chain contractions*, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-centralizer-profiles-and-a-quadratic-limit-law-for-idempotent-fi--22387dfffecf.
4. *Idempotent centralizers and commuting semilattices in a finite directed-path monoid*, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-idempotent-centralizers-and-commuting-semilattices-in-a-finite-d--628a5e7d08b8.
5. *Eventual-image fibers and independent geometric–Gaussian limits in directed-path weak endomorphisms*, https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-eventual-image-fibers-and-independent-geometric-gaussian-limits--04f5773be42b.
6. J. Konieczny and E. Korkmaz, *Centralizers in Catalan Monoids*, arXiv:2611.21071v1 (2026-11-16), https://arxiv.org/abs/2611.21071.
