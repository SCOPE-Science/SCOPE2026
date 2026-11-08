# Algebraic cardinality series and sharp growth of parity-preserving fence inverse monoids

## Finding
For every integer \(n\geq 1\), let \(M_n\) consist of all partial injections on the chain \([n]=\{1,\ldots,n\}\) that preserve the natural order, preserve the alternating fence order in both directions, and map every point to one of the same parity. Include the empty map. Put \(M_0=\{\varnothing\}\), and \(a_n=|M_n|\). The complete ordinary cardinality generating function is
\[
\boxed{\sum_{n\geq0}a_nz^n=\frac1z\left(\frac{1-z^2}{\sqrt{1-2z-3z^2+4z^3+4z^6}}-1\right).}
\]
The square root denotes the unique formal series with constant coefficient \(1\), so the apparent pole at zero is removable. The first values are \(1,2,4,10,22,52,120,286,678,1628,3912,9460\).

Let \(\rho\) be the unique positive root of \(Q(z)=1-3z+2z^2-2z^3\), and set \(P(z)=1-2z-3z^2+4z^3+4z^6\). Then \(\rho=0.3966082527360922060\ldots\), and
\[
\boxed{a_n\sim C\rho^{-n}n^{-1/2},\qquad C=\frac{1-\rho^2}{\rho\sqrt{-\pi\rho P'(\rho)}}=1.2671654090206336721\ldots.}
\]
In particular, the exponential growth rate is \(\rho^{-1}=2.5213797068\ldots\). As the containing monoid of all order-preserving partial injections has cardinality \(\binom{2n}{n}\), the relative density has the sharp asymptotic
\[
\frac{|M_n|}{\binom{2n}{n}}\sim C\sqrt\pi\,(4\rho)^{-n}.
\]
The rank refinement is also exact: for \(1\le r\le n\), the number of elements with domain size \(r\) is the diagonal coefficient described in the proof below.

## Assumptions and scope
The alternating fence on \([n]\) has covers \(1\prec2\succ3\prec4\succ\cdots\). A partial injection \(f:D\longrightarrow[n]\) is order-preserving for the chain when \(i<j\) implies \(f(i)<f(j)\) for \(i,j\in D\). It is fence-preserving in both directions when both \(f\) and \(f^{-1}\) preserve the induced fence order on their respective domains. It is parity-preserving when \(i\equiv f(i)\pmod 2\) for all \(i\in D\). This is exactly the inverse monoid usually denoted \(IOF_n^{\mathrm{par}}\). No asymptotic assertion concerns the semigroup rank (minimal number of generators); the statistic counted here is its cardinality.

## Proof
Every nonempty element of rank \(r\) is uniquely specified by two increasing sequences of equal length, \(d_1<\cdots<d_r\) and \(m_1<\cdots<m_r\), with \(f(d_i)=m_i\). The characterization in Sareeto–Koppitz [1, Proposition 1] is equivalent to the following: \(d_1\equiv m_1\pmod2\), and for every consecutive pair the two positive gaps have the same one of the three types
\[
(1,1),\qquad(2+2i,2+2j),\qquad(3+2i,3+2j),\qquad i,j\geq0.
\]
Indeed, the source and target gaps must agree on being \(1\), and must have the same parity. Conversely these conditions enforce parity at every matched point and preserve fence adjacency in both directions. In particular there is no extra multiplicity from the map, because pairing the increasing sequences uniquely specifies it.

Mark the final domain and image coordinates by \(x\) and \(y\). The generating function for the first matched pair is
\[
A(x,y)=\sum_{a,b\geq1\,;\,a\equiv b\ (2)}x^ay^b
=\frac{xy(1+xy)}{(1-x^2)(1-y^2)}.
\]
The generating function for one matched gap is
\[
H(x,y)=xy+\frac{x^2y^2(1+xy)}{(1-x^2)(1-y^2)}.
\]
The final coordinates need only be at most \(n\), so summing the two nonnegative endpoint slacks gives \((1-x)^{-1}(1-y)^{-1}\). Consequently, for \(r\geq1\), the exact rank-\(r\) count is
\[
a_{n,r}=[x^ny^n]\,\frac{A(x,y)H(x,y)^{r-1}}{(1-x)(1-y)}.
\]
Summing over all positive ranks and adding the unique empty map yields
\[
a_n=1+[x^ny^n]B(x,y),\quad
B(x,y)=\frac{xy(1+xy)}{(1-x)(1-y)\bigl((1-xy)(1-x^2-y^2)-2x^3y^3\bigr)}.
\]

To take the diagonal exactly, introduce the symmetric elementary variables \(u=x+y\) and \(v=xy\). Then
\[
B=\frac{v(1+v)}{(1+v-u)\bigl((1+v)(1-2v^2)-(1-v)u^2\bigr)}.
\]
A monomial \(v^j u^k\) can contribute to the diagonal only when \(k=2\ell\), in which case its diagonal contribution is \(\binom{2\ell}{\ell}z^{j+\ell}\). The even-in-\(u\) part of \(B\) is
\[
\frac{v(1+v)^2}{\bigl((1+v)^2-u^2\bigr)\bigl((1+v)(1-2v^2)-(1-v)u^2\bigr)}.
\]
Writing \(U=(1+v)^2\), \(V=(1+v)(1-2v^2)\), and \(W=1-v\), the identity \(V-WU=-v^2(1+v)\) gives the partial fractions
\[
\frac{1+v}{v}\left(\frac{W}{V-Wu^2}-\frac1{U-u^2}\right).
\]
The intermediate terms are Laurent in \(v\), but their sum is the preceding formal power series. The formal central-binomial identity \(\sum_{\ell\geq0}\binom{2\ell}{\ell}t^\ell=(1-4t)^{-1/2}\) now yields
\[
\operatorname{Diag}B(z)=\frac{1+z}{z}\left(
\frac{1-z}{\sqrt{(1+z)(1-2z^2)(1-3z+2z^2-2z^3)}}-\frac1{1-z^2}\right).
\]
Since the empty map contributes \(1\) to \(a_n\) in every dimension, its generating function is \((1-z)^{-1}\), rather than just a constant. Adding this to \(\operatorname{Diag}B(z)\), and using
\[
(1+z)(1-2z^2)(1-3z+2z^2-2z^3)=1-2z-3z^2+4z^3+4z^6=P(z),
\]
proves the stated ordinary generating function.

For the asymptotic, \(Q'(z)=-3+4z-6z^2<0\) for real \(z\), so \(Q\) has exactly one real zero, lying in \((0,1/2)\). Its other two zeros are conjugate and have modulus \((2\rho)^{-1/2}>1\), from their product. The other zeros of \(P=(1+z)(1-2z^2)Q(z)\) are \(-1\) and \(\pm1/\sqrt2\), all strictly farther from the origin than \(\rho\). Hence \(\rho\) is the unique dominant square-root singularity and \(P'(\rho)<0\). The standard binomial coefficient estimate applied to the local expansion
\[
\frac{1-z^2}{z\sqrt{P(z)}}\sim
\frac{1-\rho^2}{\rho\sqrt{-\rho P'(\rho)}}(1-z/\rho)^{-1/2}
\]
proves the claimed sharp asymptotic. The density statement follows from \(\binom{2n}{n}\sim4^n/\sqrt{\pi n}\).

## Verification
The accompanying dependency-light `verify.py` checks the exact algebraic square identity through degree \(33\), computes the integer coefficients through \(n=32\), and independently enumerates the literal order-preserving, parity-preserving, two-sided fence-preserving partial maps for every \(0\le n\le11\). It independently enumerates the three gap types through \(n=6\) and evaluates the dominant root and asymptotic constant with high precision. Run `python verify.py`; a successful execution ends with `VERIFY_OK`. Finite computations are checks of the algebraic proof, not a substitute for it.

## Relationship to prior work
Sareeto and Koppitz [1] define this inverse monoid, characterize its increasing-domain/increasing-image maps, and determine its minimal generating-set rank, \(3n-6\) for \(n\ge4\). The characterization is explicitly used as an input here. Their later work [2] gives a monoid presentation, and [3] describes ideals, Green relations, and maximal subsemigroups. The inspected statements do not state this algebraic cardinality generating function or sharp asymptotic. Those enumerative assertions are distinct from generator rank, presentations, and ideal structure; their derivation requires the gap-pair generating kernel, a symmetric diagonal extraction, and singularity analysis. More general results not located by the searches could conceivably subsume the calculation; publication priority is not independently certified.

## Limitations
Only the parity-preserving, two-sided fence-preserving **order-preserving partial injection** monoid is counted; dropping parity, inverse fence preservation, or chain monotonicity changes the object. The asymptotic has fixed monoid family and \(n\to\infty\), not a uniform statement for any varying external parameter. The paper does not count isomorphism classes or classify all subsemigroups. The search cannot establish global priority or mathematical independence.

## References
[1] A. Sareeto and J. Koppitz, *The rank of the semigroup of order-, fence-, and parity-preserving partial injections on a finite set*, arXiv:2208.03202, first submitted 5 August 2022, Proposition 1 and Theorem 2. https://arxiv.org/abs/2208.03202

[2] A. Sareeto and J. Koppitz, *A presentation for a submonoid of the symmetric inverse monoid*, arXiv:2310.15809, first submitted 24 October 2023, Theorem 2. https://arxiv.org/abs/2310.15809

[3] A. Sareeto and J. Koppitz, *The maximal subsemigroups of the ideals on a monoid of partial injections*, arXiv:2403.06957, first submitted 11 March 2024, Proposition 1 and Theorem 1. https://arxiv.org/abs/2403.06957

[4] V. H. Fernandes, *The monoid of all injective order-preserving partial transformations on a finite chain*, Semigroup Forum 62 (2001), 178–204; the enclosing monoid's cardinality is \(\binom{2n}{n}\), as cited by [1].
