# Square-root fibers and the scarcity of nonidempotent squares in cyclic inverse monoids

## Finding

Let \(n\ge1\), let \(X=\mathbb Z/n\mathbb Z\), and let \(\mathcal C\mathcal I_n\) be the inverse monoid of restrictions of translations of \(X\), including the empty partial map \(0\). Write \(f_{k,A}\) for the restriction of \(x\mapsto x+k\) to \(A\subseteq X\). Its nonempty elements have unique labels \((k,A)\).

**Exact individual square-root fibers, every \(n\).** For a nonempty target \(f_{j,B}\), the number of solutions of \(f^2=f_{j,B}\) is
\[
\sum_{\substack{k\in X\\2k=j}}\ \prod_{\mathcal O\in X/\langle k\rangle}
 \rho_{|\mathcal O|}(B|_{\mathcal O}),
\]
where each \(k\)-orbit \(\mathcal O\) is listed in forward \(+k\) order and the local fiber \(\rho_\ell\) is defined below. The empty map has exactly
\[
1+\sum_{k\in X}\left(L_{n/\gcd(n,k)}^{\gcd(n,k)}-1\right)
\]
square roots, with \(\gcd(n,0)=n\) and Lucas numbers \(L_1=1,L_2=3,L_{\ell+2}=L_{\ell+1}+L_\ell\).

For a cyclic binary output word \(b=(b_0,\ldots,b_{\ell-1})\), let \(\rho_\ell(b)\) count binary cyclic words \(a\) satisfying \(b_i=a_i a_{i+1}\), indices modulo \(\ell\). Explicitly:

- If every bit of \(b\) is zero, \(\rho_\ell(b)=L_\ell\); if every bit is one, \(\rho_\ell(b)=1\).
- Otherwise, \(\rho_\ell(b)=0\) if \(b\) contains the cyclic pattern \(101\). If it avoids \(101\), and the maximal zero runs have lengths \(r_1,\ldots,r_t\), then
  \[\rho_\ell(b)=\prod_{i=1}^{t}F_{r_i-1},\qquad F_0=0,\ F_1=1,\ F_{s+2}=F_{s+1}+F_s.\]
  Every zero run then has length at least two.

**Square-image census, odd \(n\).** Put \(C_1=C_2=2\), \(C_3=5\), and
\[C_{\ell+3}=2C_{\ell+2}-C_{\ell+1}+C_\ell\quad(\ell\ge1).\]
Then \(C_\ell\) is the number of cyclic binary words of length \(\ell\) avoiding \(101\). For every odd \(n\ge1\), the number \(S_n=|\{f^2:f\in\mathcal C\mathcal I_n\}|\) is
\[
\boxed{S_n=\sum_{d\mid n}\varphi(d)\,C_d^{n/d}-n+1.}
\]
Moreover, with \(\beta=2(7/8)^{1/5}<2\),
\[
2^n\le S_n\le2^n+(n-1)\beta^n,\qquad
\frac{S_n}{|\mathcal C\mathcal I_n|}=\frac1n+O((\beta/2)^n)
\]
as odd \(n\to\infty\), where \(|\mathcal C\mathcal I_n|=n2^n-n+1\). Thus although every partial identity is a square, **the proportion of squares is asymptotic to \(1/n\)**, and the contribution from nonidempotent squares is exponentially small relative to the whole monoid.

The initial odd-degree counts are \(S_3=16\), \(S_5=96\), \(S_7=428\), \(S_9=1702\), and \(S_{11}=6898\).

## Assumptions and scope

Composition is ordinary partial-function composition and \(f^2=f\circ f\). A nonempty partial translation has a unique displacement, since one defined arrow determines the translation. Zero is the unique empty transformation. The index \(n=1\) is allowed; the interesting infinite family is odd \(n\ge3\). The full individual-fiber statement also applies to even \(n\), where \(2k=j\) can have zero or two solutions; the divisor-sum image formula is asserted only for odd \(n\).

## Proof

For any \(k\) and \(A\), direct composition gives
\[
f_{k,A}^2=f_{2k,\, A\cap(A-k)}.
\]
If \(a_x\) is the indicator of \(A\) and \(b_x\) is the indicator of the square's domain, then \(b_x=a_xa_{x+k}\). Each orbit of translation by \(k\) is a cycle of equal length \(\ell=n/\gcd(n,k)\), and the equations on separate orbits are independent. For a nonempty output the displacement must satisfy \(2k=j\), and choices for different solutions \(k\) represent distinct nonempty roots. For zero output, all empty-domain choices represent the same root, so subtract one duplicate for each \(k\) and add zero back once.

For one cyclic binary word, the edge equation \(b_i=a_i a_{i+1}\) forces \(a_i=a_{i+1}=1\) whenever \(b_i=1\). In a nonconstant target, an isolated zero between two ones is therefore impossible. Conversely, if the target contains no cyclic \(101\), setting \(a_i=1\) precisely when \(b_{i-1}=1\) or \(b_i=1\) gives one precursor: no zero edge has both endpoints forced to one. In each maximal block of \(r\ge2\) zero edges between positive-edge blocks, the endpoint vertices are forced to one, the two adjacent interior vertices must be zero (coinciding when \(r=2\)), and the remaining free vertices form a binary string with no adjacent ones. The count is \(F_{r-1}\). These blocks have independent choices. If all output bits are zero, precursors are independent sets on the cyclic adjacency graph, counted by \(L_\ell\) (including \(\ell=1,2\) by direct check). If all are one, only the all-one precursor works. This proves all root-fiber formulas.

The image of the map \(a\mapsto (a_i a_{i+1})\) on cyclic binary words is therefore exactly the cyclic words avoiding \(101\). Track successive two-bit states \(00,01,10,11\), deleting the transition that would complete \(101\). The transfer matrix is
\[
T=\begin{pmatrix}
1&1&0&0\\0&0&1&1\\1&0&0&0\\0&0&1&1
\end{pmatrix}.
\]
The cyclic-word count is \(C_\ell=\operatorname{tr}(T^\ell)\). The characteristic polynomial is \(\lambda(\lambda^3-2\lambda^2+\lambda-1)\), giving the stated recurrence for \(\ell\ge1\) and initial values. Equivalently, \(\sum_{\ell\ge1}C_\ell z^\ell=(2z-2z^2+3z^3)/(1-2z+z^2-z^3)\).

If \(n\) is odd, doubling is a bijection of \(X\). Hence each nonempty output displacement \(j\) uniquely determines the root displacement \(k\). For a fixed \(k\) of additive order \(d\), there are \(n/d\) orbits and \(C_d^{n/d}\) admissible output domain indicators (one of them empty). Exactly \(\varphi(d)\) values of \(k\) have additive order \(d\). Sum over divisors \(d\mid n\), discard the \(n\) copies of the empty output, and restore it once. This proves the divisor sum.

All \(2^n\) partial identities are idempotent, so are squares. To bound nonidempotent squares, any circular word of length \(d\ge3\) avoiding \(101\) in particular avoids this pattern in each of \(\lfloor d/3\rfloor\) disjoint consecutive triples. Thus
\[C_d\le 2^d(7/8)^{\lfloor d/3\rfloor}\le\beta^d,\]
because \(\lfloor d/3\rfloor/d\ge1/5\) for every \(d\ge3\). For odd \(n\), every nonzero \(k\) has odd additive order \(d\ge3\); its contribution is bounded by \(\beta^n\). The zero displacement contributes \(C_1^n=2^n\), so \(S_n\le2^n+(n-1)\beta^n\). Divide by \(n2^n-n+1\) to obtain the asymptotic.

## Verification

The standalone `verify_square_fibers.py` constructs each partial map as an explicit length-\(n\) tuple, with \(-1\) denoting undefined; it computes squares by actual function composition. For every \(1\le n\le10\) it compares all observed and unobserved output fibers with the independent orbit/Fibonacci formulas. For each odd \(n\le9\) it also compares the image-size count with the divisor sum. A separate direct enumeration of every binary input word through length \(16\) checks all cyclic local fiber sizes and the forbidden-pattern criterion. The script prints `CYCLIC_INVERSE_SQUARE_FIBERS_VERIFIED 24001 n<=10; local cycle lengths<=16` on success. These finite checks corroborate but do not replace the proof for all degrees.

## Relationship to prior work

V. H. Fernandes, *On the cyclic inverse monoid on a finite set*, initially publicly posted 2022-11-03 as arXiv:2211.02155, introduces the precise monoid and establishes its cardinality and ranks/presentations. Its sections on sizes, ranks and presentations do not state a square-power image census or square-root fiber law. The existing cardinality \(n2^n-n+1\) is credited. L. Elliott, A. Levine and J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, arXiv:2303.12387 (2023), count abstract monogenic submonoids up to isomorphism; this neither counts square outputs nor determines fibers of the squaring endomorphism of the underlying set. The avoidance sequence \(C_\ell\) is a standard finite-automaton computation, not claimed as a newly discovered word sequence. The contribution is its exact connection with the power-map image and fibers in this inverse monoid.

Related published results on square roots in **different** partial transformation monoids and on nilpotency/rank of cycle partial-isometry monoids were compared by their claim descriptions; they do not imply the formulas here. This does not certify comprehensive historical priority: inaccessible source texts and alternate terminology may conceal equivalent results.

## Limitations

The displayed divisor-sum formula and asymptotic are proved for odd \(n\). The root-fiber formula applies in even degrees as well but does not simplify the union of two possible root displacement classes into a single divisor sum. No classification of higher power maps is asserted. The asymptotic error bound is explicit but not optimized. Exact computational verification stops at finite degrees, independently of the general proof.

## References

1. V. H. Fernandes, *On the cyclic inverse monoid on a finite set*, arXiv:2211.02155, initial public version 2022-11-03, https://arxiv.org/abs/2211.02155.
2. L. Elliott, A. Levine and J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, arXiv:2303.12387, initial public version 2023-03-22, https://arxiv.org/abs/2303.12387.
3. S. Bilotta, D. Merlini, E. Pergola and R. Pinzani, *Binary words avoiding a pattern and marked succession rule*, arXiv:1103.5689 (2011), https://arxiv.org/abs/1103.5689, as background for transfer methods rather than novelty.
