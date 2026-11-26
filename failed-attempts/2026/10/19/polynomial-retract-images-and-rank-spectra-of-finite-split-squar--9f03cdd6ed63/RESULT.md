# Polynomial retract images and rank spectra of finite split square-zero algebras

## Finding

Let \(q\) be any prime power and \(d\ge1\). Put \(V=\mathbb F_q^d\) and let \(A=\mathbb F_q\oplus V\) be the unital commutative algebra with square-zero ideal \(V\):
\[
(a,v)(b,w)=(ab,aw+bv).
\]
Let \(\operatorname{Pol}_1(A)\) be the monoid under composition of all **unary polynomial functions** \(A\to A\) induced by polynomials with coefficients in \(A\). A polynomial retraction is an \(F\in\operatorname{Pol}_1(A)\) satisfying \(F\circ F=F\).

For \(Y\subseteq A\) and \(a\in\mathbb F_q\), write \(Y_a=\{v\in V:(a,v)\in Y\}\). Then **\(Y\) is the image of a polynomial retraction if and only if** \(Y\ne\varnothing\) and each \(Y_a\) is empty, a singleton, or all of \(V\).

For any such \(Y\), write \(k=|\{a:Y_a\ne\varnothing\}|\) and \(s=|\{a:Y_a=V\}|\). The number of *distinct polynomial functions* retraction onto this **particular** \(Y\) is exactly
\[
\boxed{(k-s+s q^{d+1})^{q-k}.}
\]
In particular, exactly \((q^d+2)^q-1\) subsets of \(A\) occur as retract images, and the complete polynomial enumerating retractions by image cardinality is
\[
\boxed{I_{q,d}(z)=\sum_{k=1}^{q}\binom{q}{k}\sum_{s=0}^{k}\binom{k}{s}
 q^{d(k-s)}(k-s+s q^{d+1})^{q-k}z^{k+s(q^d-1)}.}
\]
These are identities of ordinary integer polynomials, for all prime powers \(q\) and integers \(d\ge1\).

The attainable retraction ranks are precisely the integers
\[
\boxed{\{\,k+s(q^d-1):1\le k\le q,\ 0\le s\le k\,\}.}
\]
The identity is the only retraction of rank \(q^{d+1}\); every other retraction has rank at most \(q^{d+1}-q^d+1\), and exactly \(q^{d+1}\) retractions attain this sharp proper-rank maximum. Exactly \(q^{d+1}\) retractions have rank one (the constant maps).

## Assumptions and scope

The algebra is the explicitly split square-zero extension \(\mathbb F_q\oplus V\), **not** an arbitrary local ring with square-zero radical. The coefficient ring for representing polynomials is the full algebra \(A\), not just its subfield \(\mathbb F_q\). All ranks mean cardinalities of set-theoretic images, not linear rank of an operator. The variable in a polynomial function is one element of \(A\). Its nonzero nilpotent coordinates may be numerous, but this does not make it a multivariate polynomial map on \(A\).

## Proof

Write a polynomial with coefficients in \(A\) uniquely as \(f(t)=f_0(t)+\sum_{j=1}^d\varepsilon_j f_j(t)\), where \(f_j\in\mathbb F_q[t]\) and \(\varepsilon_i\varepsilon_j=0\). For \(a\in\mathbb F_q\), \(v\in V\), evaluation is
\[
F(a,v)=\bigl(f_0(a),f_0'(a)v+(f_1(a),\ldots,f_d(a))\bigr).
\]
Conversely, **every** triple of functions \(\alpha:\mathbb F_q\to\mathbb F_q\), \(\beta:\mathbb F_q\to\mathbb F_q\), and \(\gamma:\mathbb F_q\to V\) occurs uniquely as the functional normal form
\[
F(a,v)=(\alpha(a),\beta(a)v+\gamma(a)).\tag{1}
\]
Indeed, the ideals \((t-a)^2\) for the distinct field elements \(a\) are pairwise comaximal. The Chinese remainder theorem independently prescribes every pair \((f_0(a),f_0'(a))\), in **every** characteristic. Ordinary Lagrange interpolation independently prescribes the values of the \(d\) polynomials \(f_j\). Evaluating at \(v=0\) and differences of evaluations determines \(\alpha,\beta,\gamma\) uniquely. In particular, there are \(q^{(d+2)q}\) polynomial functions in total.

Composing (1) with itself shows that idempotence is equivalent to, for each \(a\in\mathbb F_q\),
\[
\alpha(\alpha(a))=\alpha(a),\qquad
\beta(\alpha(a))\beta(a)=\beta(a),\qquad
\beta(\alpha(a))\gamma(a)+\gamma(\alpha(a))=\gamma(a).\tag{2}
\]
Thus \(\alpha\) is a set retraction onto a nonempty set \(B\) of \(k\) fixed points. At each \(c\in B\), equation (2) gives \(\beta(c)^2=\beta(c)\) and \(\beta(c)\gamma(c)=0\). Since the base is a field, exactly two cases arise:

* If \(\beta(c)=1\), then \(\gamma(c)=0\); \(F\) fixes and maps onto the entire fiber \(\{c\}\times V\).
* If \(\beta(c)=0\), then \(\gamma(c)\in V\) is arbitrary; \(F\) maps that fiber to the single point \((c,\gamma(c))\), which it fixes.

No point outside these fixed base fibers can create additional image elements, because \(F^2=F\) makes every image point fixed. This proves the necessity of the stated fiberwise description. To prove sufficiency and count retractions onto a prescribed permitted \(Y\), set \(\alpha(c)=c\) for each of its \(k\) active base fibers. On each of its \(s\) full fibers force \(\beta(c)=1,\gamma(c)=0\); on each singleton fiber force \(\beta(c)=0\) and \(\gamma(c)\) equal to the specified point's nilpotent coordinate.

For each of the \(q-k\) remaining base elements \(a\), independently choose its target \(c=\alpha(a)\) among the active fibers. Each full fiber offers exactly \(q\cdot q^d=q^{d+1}\) choices of \((\beta(a),\gamma(a))\), and each singleton fiber offers exactly one. Hence there are \(k-s+s q^{d+1}\) choices per unused base element, proving the displayed fiber cardinality. All constructed triples satisfy (2) and are represented by polynomials by interpolation, so no conditions or multiplicities were omitted.

There are \(\binom{q}{k}\binom{k}{s}(q^d)^{k-s}\) possible images with exactly \(k\) active and \(s\) full fibers. Every such image has \(s q^d+(k-s)=k+s(q^d-1)\) elements. Multiplying by the fixed-image fiber count and summing proves the rank polynomial and the rank support. For each of the \(q\) residue fibers, an image independently contributes one of the disjoint choices empty, full, or one of \(q^d\) singletons. Removing the all-empty choice proves the image count.

For the sharp rank boundary, put \(m=q^d\ge2\). The only rank \(qm\) occurs at \(k=s=q\), giving the identity. For any other pair, \(k+s(m-1)\le qm-m+1\), with equality only at \((k,s)=(q,q-1)\). Its coefficient is \(\binom{q}{q-1}m=q^{d+1}\). Likewise the only rank-one case is \((k,s)=(1,0)\), yielding \(qm=q^{d+1}\) constants.

## Verification

The standalone finite checker `check.py` directly evaluates coefficient polynomials in the square-zero algebra, composes the resulting functions, records their image subsets, and compares every image-fiber multiplicity and rank coefficient with the formulas. Coefficient-polynomial representatives were enumerated exhaustively at \((q,d)=(2,1),(2,2),(2,3),(3,1)\), giving respectively \(21,49,129,604\) idempotents. Independently enumerated affine normal-form functions at \((q,d)=(3,2)\) give \(5374\). Image counts in these cases are respectively \(15,35,99,124,1330\). No disagreement occurred. Arithmetic boundary assertions were also checked for \(32\) further parameter pairs; these finite checks complement, but cannot replace, the general proof above.

For illustration,
\[
I_{2,2}(z)=8z+16z^2+16z^4+8z^5+z^8,
\]
whereas
\[
I_{3,1}(z)=9z+54z^2+270z^3+180z^4+27z^5+54z^6+9z^7+z^9.
\]
Run `python3 check.py` from a directory containing the standalone checker; no third-party package is needed.

## Relationship to prior work

Al-Ezeh, Al-Maktry, and Frisch (arXiv:1910.00238, first submitted 2019-10-01) develop the polynomial-function/derivative description for dual numbers in one nilpotent direction. Al-Maktry (arXiv:2002.01304, first submitted 2020-02-03), especially Theorem 3.4, Corollary 3.6, and Proposition 3.7, develops polynomial functions and their total counts for any number of pairwise-annihilating nilpotent directions. These descriptions underlie the normal form used here and are **not** claimed as new. Al-Maktry (arXiv:2010.00342, first submitted 2020-10-01) studies polynomial permutations and their unit-related groups, not retraction-image cardinalities.

The present result concerns a distinct invariant: the possible images of composition-idempotent polynomial functions, the precise number of retractions onto each image, their complete rank distribution, and the sharp proper-rank gap. These statements are not among the enumerations or classifications established in the inspected sources. Relevant earlier work by Aichinger (2001, DOI:10.1017/S0013091599001418) addresses ideal images of near-ring idempotents in a substantially broader setting, but an equivalent rank/image count in that or related literature remains a residual risk.

## Limitations

This is an exact statement only for the indicated split commutative square-zero algebras and unary polynomial functions. It does not classify arbitrary set retractions, ring-endomorphism retracts, polynomial maps over nonsplit finite local rings, or multivariate polynomial functions with independent input variables. The formula does not assert novelty of the established jet parametrization or of the total polynomial-function count. Exhaustive searches cannot prove global uniqueness of a formula. The cited near-ring work was available here as bibliographic information and an abstract, not as an inspected full paper. No independent mathematical validation has been performed.

## References

1. H. Al-Ezeh, A. A. Al-Maktry, and S. Frisch, *Polynomial functions on rings of dual numbers over residue class rings of the integers*, arXiv:1910.00238, v1 submitted 2019-10-01, published in *Mathematica Slovaca* 71 (2021), 1063–1088. https://arxiv.org/abs/1910.00238
2. A. A. A. Al-Maktry, *Polynomial functions over dual numbers of several variables*, arXiv:2002.01304, v1 submitted 2020-02-03, later in *Journal of Algebra and Its Applications*. https://arxiv.org/abs/2002.01304
3. A. A. Al-Maktry, *On the group of unit-valued polynomial functions*, arXiv:2010.00342, v1 submitted 2020-10-01. https://arxiv.org/abs/2010.00342
4. E. Aichinger, *On near-ring idempotents and polynomial functions on direct products of Omega-groups*, *Proceedings of the Edinburgh Mathematical Society* 44 (2001), 379–388. DOI:10.1017/S0013091599001418.
