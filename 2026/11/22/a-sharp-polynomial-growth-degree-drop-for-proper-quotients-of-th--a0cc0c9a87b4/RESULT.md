# A sharp polynomial-growth degree drop for proper quotients of the free monogenic inverse monoid

## Finding

Let \(F\) be the free inverse monoid on a single inverse-monoid generator \(x\), equipped with the symmetric alphabet \(\{x,x^{-1}\}\). If \(\pi:F\twoheadrightarrow Q\) is a **proper** surjective inverse-monoid homomorphism (nontrivial kernel), then the word ball in \(Q\), with respect to \(\{\pi(x),\pi(x)^{-1}\}\), satisfies

\[
|B_Q(n)|=O_Q((n+1)^2).
\]

By contrast, \(|B_F(n)|=\Theta((n+1)^3)\). The quadratic upper bound cannot be lowered uniformly: the bicyclic inverse monoid quotient defined by \(xx^{-1}=1\) satisfies

\[
|B_Q(n)|=\binom{n+2}{2}.
\]

Thus the polynomial ball-growth degree of this rank-one free inverse monoid drops **strictly** in every proper inverse-monoid quotient, despite the fact that exponential growth rate cannot distinguish any of these infinite polynomial-growth examples.

## Assumptions and scope

A quotient here means a surjective homomorphism in the category of inverse monoids, with the identity and inverse operation preserved; ``proper'' means the quotient map identifies two different elements of \(F\). Word length is the minimum length over both \(x\) and \(x^{-1}\), with the empty word representing the identity. Constants implicit in \(O_Q\) depend on the quotient, not on \(n\). Nothing is asserted for free inverse monoids of higher rank, for arbitrary monoid homomorphic images that are not inverse monoids, or for unrelated generating sets.

In the standard Munn interval model, the distinct elements of \(F\) are exactly triples

\[
(a,b,k),\qquad a,b\in\mathbb N_0,\quad -a\le k\le b.
\]

They represent the finite interval \([-a,b]\) traversed by the word path on \(\mathbb Z\), rooted at \(0\), and terminal displacement \(k\). Multiplication and inversion are

\[
(a,b,k)(c,d,\ell)=\bigl(\max(a,c-k),\max(b,d+k),k+\ell\bigr),
\]
\[
(a,b,k)^{-1}=(a+k,b-k,-k).
\]

The idempotents are \(e(a,b)=(a,b,0)\), and \(e(a,b)e(c,d)=e(\max(a,c),\max(b,d))\). The generators are \(x=(0,1,1)\), \(x^{-1}=(1,0,-1)\). These are ordinary Munn normal forms, not additional restrictions on quotients.

## Proof

**1. A nontrivial congruence identifies distinct idempotents.** Suppose \(u=(a,b,k)\) and \(v=(c,d,\ell)\) are distinct but \(\pi(u)=\pi(v)\). Since homomorphisms preserve inversion, they identify both corresponding range idempotents \(uu^{-1}\) and \(vv^{-1}\), and domain idempotents \(u^{-1}u\) and \(v^{-1}v\). In these coordinates the two idempotents of \(u\) are

\[
 uu^{-1}=e(a,b),\qquad u^{-1}u=e(a+k,b-k).
\]

If both idempotent pairs were equal in \(F\), then \(a=c\), \(b=d\), and \(a+k=c+\ell\), forcing \(k=\ell\) and hence \(u=v\). Therefore the kernel contains a pair \(e(a,b)\ne e(c,d)\) that become equal in \(Q\).

**2. An idempotent identification produces eventual one-coordinate periodicity.** If \(a\ne c\), exchange the two idempotents if needed and assume \(a<c\), writing \(\delta=c-a>0\) and \(B=\max(b,d)\). Multiply their quotient equality by \(e(0,B)\) to obtain

\[
 \pi(e(a,B))=\pi(e(c,B)).
\]

For any integer \(t\ge B\), conjugation by \(x^{-t}\) gives the Munn interval identity

\[
 x^{-t}e(h,B)x^t=e(h+t,0)\qquad(h\ge0),
\]

hence \(\pi(e(a+t,0))=\pi(e(c+t,0))\). Multiplication by any \(e(0,b')\) now yields, uniformly for every \(b'\ge0\),

\[
 \pi(e(A,b'))=\pi(e(A+\delta,b'))\qquad(A\ge A_0:=a+B).
\]

The factorization \((A,b',k)=e(A,b')x^k\), valid whenever \(-A\le k\le b'\), extends this relation to every such terminal displacement \(k\).

If instead \(a=c\) and \(b\ne d\), reflect the integer line, exchanging \(x\) and \(x^{-1}\) and the two interval extents. The same argument produces a number \(\delta>0\) and a threshold \(B_0\) such that, for all \(b'\ge B_0\) and all \(A\ge0\), the images of \(e(A,b')\) and \(e(A,b'+\delta)\) agree. Both cases therefore make at least one of the two interval extents eventually periodic, uniformly in the other extent.

**3. Bound the quotient ball.** Work in the first case, where the left extent is periodic. Every element of the length-\(n\) word ball in \(F\) has \(a,b\le n\) and \(|k|\le n\). Repeatedly replace a large left extent \(a'\) by \(a'-\delta\) whenever \(a'-\delta\ge\max(A_0,-k)\). The resulting triple still has terminal point in its interval, belongs to the same quotient class, and has the **same** right extent and terminal displacement. There are at most \(A_0+\delta+1\) possible reduced left extents for any fixed \(k\): if \(-k>A_0\), the reduced left extent lies in an interval of length \(\delta\) above \(-k\); otherwise it is bounded by \(A_0+\delta\). Therefore at most

\[
 (A_0+\delta+1)(n+1)(2n+1)
\]

quotient classes meet the length-\(n\) ball, because \(b\in\{0,\ldots,n\}\) and \(k\in\{-n,\ldots,n\}\). The reflected case is identical. The reductions never increase the original Munn interval and therefore cannot increase word length; even without this observation, their images already cover the desired quotient ball. Thus \(|B_Q(n)|=O_Q(n^2)\).

**4. Free growth and sharpness.** A shortest walk on the integer line that starts at zero, visits both endpoints of \([-a,b]\), and ends at \(k\) has length

\[
 \ell_F(a,b,k)=2(a+b)-|k|.
\]

It follows that \(|B_F(n)|=O(n^3)\). Conversely, the triples with \(0\le a,b\le\lfloor n/5\rfloor\) and any \(-a\le k\le b\) have length at most \(4n/5\); their count is \(\Theta(n^3)\). Hence the free ball growth is cubic.

The bicyclic inverse monoid \(C=\langle p,q\mid pq=1\rangle\), with \(q=p^{-1}\) in the inverse-monoid sense, is a proper image of \(F\) under \(x\mapsto p\). Its pairwise distinct normal forms are \(q^i p^j\) for \(i,j\ge0\), of minimal word length \(i+j\). Thus

\[
 |B_C(n)|=\#\{(i,j)\in\mathbb N_0^2:i+j\le n\}=\binom{n+2}{2},
\]

proving sharpness.

## Verification

The standalone Python file `verify.py` implements the Munn interval product, inversion, length function, and the bicyclic quotient map \((a,b,k)\mapsto(a,a+k)\). It exhaustively compares word-ball enumeration against the triple formula through length ten, checks inversion identities, checks the quotient homomorphism on all pairs in the length-four ball, and verifies bicyclic ball counts. It additionally checks representative interval/congruence manipulations on bounded parameters. Successful output: `MONOGENIC_INVERSE_QUOTIENT_GROWTH_CHECKS_OK`. The universal upper bound depends on the preceding symbolic congruence proof, not on finite enumeration.

## Relationship to prior work

Bodart, Carvalho and Monteiro's 2026 paper proves strict **exponential** growth-rate loss for proper free inverse-monoid quotients when the free generating set has at least two elements (Theorem 10.9). The present statement is its **rank-one, polynomial-degree analogue** and is not implied by their positive-rank exponential estimates. The free monogenic cubic growth itself is classical and explicitly calculated by Kambites, Nyberg-Brodda, Szakács and Webb (Proposition 3.4); it is used here, not claimed as new. Elliott, Levine and Mitchell study enumeration of monogenic inverse submonoids of finite symmetric inverse monoids, not arbitrary proper quotients and their word-ball growth. Rees-quotient results concern restricted classes of quotients with zero and do not by themselves imply the universal statement here. No priority claim is made concerning older, unindexed congruence classifications that might imply this conclusion.

## Limitations

The result controls growth degree, not precise word-ball coefficients or a classification of every proper congruence. It is possible for proper quotients to have linear, bounded, or quadratic growth. The proof and checker concern inverse-monoid quotients with the indicated symmetric generator set. A self-review is not an independent mathematical audit; historical priority remains subject to specialist literature that has not been fully accessed.

## References

- C. Bodart, A. Carvalho, A.-C. Monteiro, *Green languages and growth of free inverse monoids*, arXiv:2609.35251 (first public version 2026-09-28), https://arxiv.org/abs/2609.35251 .
- M. Kambites, C.-F. Nyberg-Brodda, N. Szakács, R. Webb, *The growth of free inverse monoids*, arXiv:2407.10489 (first public version 2024-07-15), https://arxiv.org/abs/2407.10489 ; J. Inst. Math. Jussieu 25 (2026), 2047–2067.
- L. Elliott, A. Levine, J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, arXiv:2303.12387, https://arxiv.org/abs/2303.12387 ; Commun. Algebra 51 (2023), 4654–4661.
- W. D. Munn, *Free inverse semigroups*, Proc. London Math. Soc. (3) 29 (1974), 385–404.
- L. M. Shneerson, D. Easdown, *Growth of finitely presented Rees quotients of free inverse semigroups*, Internat. J. Algebra Comput. 21 (2011), 315–328.
