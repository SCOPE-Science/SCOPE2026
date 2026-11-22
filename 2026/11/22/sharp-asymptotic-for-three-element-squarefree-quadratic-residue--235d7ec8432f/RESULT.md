# Sharp asymptotic for three-element squarefree quadratic-residue covers

## Finding

Let \(H(N)\) count unordered three-element subsets \(\{a,b,c\}\) of distinct squarefree integers in \(\{2,\ldots,N\}\) such that, for **every** prime \(p\), at least one of \(a,b,c\) is a square modulo \(p\), with zero counted as a square. As \(N\) tends to infinity through positive integers,

\[
H(N)=\left(\kappa+o(1)\right)N^{3/2},\qquad
\kappa=\frac{2}{3}\prod_{p\ \mathrm{prime}}\left(1-\frac1p\right)^3\left(1+\frac3p\right)
=0.0765897\ldots.
\]

The Euler product is absolutely convergent and strictly positive. For each integer \(N\ge 2\), there is also the exact finite count

\[
H(N)=\sum_{\substack{1\le u<v<w\\vw\le N}}\mu^2(uvw).
\]

This is a sharp leading-term count, not a claim of a power-saving error term.

## Assumptions and scope

The elements are **positive, pairwise distinct, squarefree and greater than one**; they need not be pairwise coprime. The word square modulo a prime includes the residue zero. The count is of unordered sets, not ordered triples. The property is required for all primes, although in this domain it is equivalent to the property for all but finitely many primes. The source context is Mishra's 2023 study of finite sets containing a power residue for almost every prime, whose primary MSC2020 includes 11A15.

## Proof

**1. Prime-residue condition.** For positive squarefree \(a,b,c>1\), none is an integer square. Fried's criterion, in the formulation of Mishra's Proposition 2.1, asserts that a finite set of nonzero integers contains a square modulo almost every prime precisely when an odd-cardinality subproduct is an integer square. With three elements and no square singleton, this says exactly that \(abc\) is a square. Conversely, if \(abc\) is a square, then for primes dividing \(abc\) one of the three residues is zero, and at primes coprime to \(abc\) the product of their three Legendre symbols is \(+1\), so the symbols cannot all be \(-1\). Hence \(abc\) square is also sufficient for **every** prime, without exceptions.

**2. Unique parameterization.** Write the three elements in increasing order \(a<b<c\). As each is squarefree, the condition that \(abc\) is a square means that every prime divides either none or exactly two among \(a,b,c\). Set

\[
u=\gcd(a,b),\quad v=\gcd(a,c),\quad w=\gcd(b,c).
\]

These three positive integers have pairwise disjoint prime supports and are squarefree, and

\[a=uv,\quad b=uw,\quad c=vw.\]

The inequalities \(a<b<c\) give \(u<v<w\), and the height restriction is exactly \(vw\le N\). Conversely any such \(u,v,w\) with squarefree product produces one admissible set. This proves the exact identity for \(H(N)\).

**3. Archimedean volume and tail.** Put \(X=\sqrt N\) and consider

\[
\mathcal R=\{(x,y,z)\in\mathbb R_{>0}^3:x<y<z,\ yz\le1\}.
\]

Its finite volume is

\[
\operatorname{vol}(\mathcal R)=\int_0^1\int_y^{1/y}\int_0^y dx\,dz\,dy
=\int_0^1(1-y^2)dy=\frac23.
\]

For \(B\ge1\), the truncated region \(\mathcal R_B=\mathcal R\cap\{z\le B\}\) has volume \(2/3-1/(2B)\). Moreover, disregarding squarefreeness, lattice points with \(w>B\sqrt N\) are bounded by

\[
\frac12\sum_{w>B\sqrt N}\left(\frac Nw\right)^2
=O(N^{3/2}/B).
\]

Thus no mass escapes toward the unbounded cusp.

**4. Local squarefree sieve.** For a fixed prime \(p\), requiring that \(uvw\) be squarefree permits either no coordinate divisible by \(p\), or exactly one coordinate divisible by \(p\) to valuation one. Counting classes modulo \(p^2\) gives the local probability

\[
\delta_p=(1-p^{-1})^3+3(p^{-1}-p^{-2})(1-p^{-1})^2
=(1-p^{-1})^3(1+3p^{-1}).
\]

In particular \(\delta_p=1+O(p^{-2})\), and all factors are positive, so \(\prod_p\delta_p\) converges to a positive constant.

For a fixed cutoff \(Y\), the Chinese remainder theorem makes the combined local probability \(\prod_{p\le Y}\delta_p\). On the bounded Jordan-measurable region \(X\mathcal R_B\), lattice points in each fixed residue class modulo \(\prod_{p\le Y}p^2\) are equidistributed after division by \(X^3\). Therefore the count satisfying the local conditions up to \(Y\), divided by \(N^{3/2}\), tends to

\[\operatorname{vol}(\mathcal R_B)\prod_{p\le Y}\delta_p.\]

To remove the cutoff, every offending prime \(p>Y\) has either \(p^2\) dividing one coordinate or \(p\) dividing two different coordinates. Inside the box \((0,BX]^3\), for fixed \(p\), the first type accounts for at most \(3(BX)^3/p^2\) lattice points and the second for at most \(3(BX)^3/p^2\); contributions vanish when the requisite modulus exceeds \(BX\). Consequently the union bound over all \(p>Y\) is

\[O(B^3N^{3/2}/Y),\]

uniformly in \(N\). First let \(N\to\infty\) with fixed \(B,Y\), then let \(Y\to\infty\) and finally \(B\to\infty\). The tail bound and the sieve estimates yield

\[\lim_{N\to\infty}\frac{H(N)}{N^{3/2}}=\frac23\prod_p\delta_p.\]

## Verification

The accompanying standalone `check.py` performs two separate integer enumerations: one from the \(u<v<w\) factorization and another directly over all distinct squarefree triples using an exact integer-square test. Both agree at heights \(30,100,200,300\): respective counts are \(12,77,222,422\). Factor enumeration additionally gives \(2491\) at \(N=1000\), \(12775\) at \(N=3000\), and \(77719\) at \(N=10000\). The finite-prime Euler product through \(p\le100000\) gives \(0.076589731381\); this decimal is numerical, not a certified error bound for the full product. The proof above, rather than these computations, establishes the infinite statement.

## Relationship to prior work

Mishra's first public 2023 preprint, *Almost No Finite Subset of Integers Contains a qth Power Modulo Almost Every Prime*, proves a generic upper bound on sets with a power-residue covering property and states the Fried–Filaseta–Richman odd-subproduct criterion. For three elements and squares, its generic \(O(N^{5/2})\) bound does not imply the exact squarefree \(N^{3/2}\) asymptotic or its Euler product.

Tao's first public 2024 work, *On Product Representations of Squares*, recalls the standard \(a=uv,b=uw,c=vw\) representation when discussing extremal sets that avoid square products. The parameterization is therefore not claimed as new here. The inspected article does not state the present complete squarefree-triple count or its constant. Erdős–Sárközy–Sós (1995) study maximum sizes of square-product-free sets, while Skałba (2010) proves Ramsey and density thresholds forcing square-product triples; their stated theorems concern existence/extremality, not this count.

## Limitations

Originality is assessed relative to the inspected primary literature and mathematical-record searches; unlocated implicit equivalents in broader multiplicative extremal-set literature remain possible. This is a leading asymptotic only: no effective uniform remainder, finite-height bound, or equidistribution theorem in other coordinate constraints is asserted. This work has not received independent mathematical validation.

## References

1. B. Mishra, *Almost No Finite Subset of Integers Contains a qth Power Modulo Almost Every Prime*, arXiv:2308.13167, first submitted 25 August 2023, Proposition 2.1 and Theorem 1.1. https://arxiv.org/abs/2308.13167
2. T. Tao, *On Product Representations of Squares*, arXiv:2405.11610 (2024), §1 and equation (1.3). https://arxiv.org/abs/2405.11610
3. P. Erdős, A. Sárközy and V. T. Sós, *On Product Representations of Powers, I*, European Journal of Combinatorics 16 (1995), 567–588. https://real.mtak.hu/110606/1/1-s2.0-019566989590039X-main.pdf
4. M. Skałba, *Product of Three Numbers Being a Square as a Ramsey Property*, Colloquium Mathematicum 120 (2010), 1–5. https://doi.org/10.4064/cm120-1-1
