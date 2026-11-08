# Five-periodic top-component counts for one-sided annihilating idempotent–square-zero matrix pairs

## Finding

For every field \(k\) and integer \(n\ge1\), define the algebraic set
\[
X_n(k)=\{(P,N)\in M_n(k)^2:P^2=P,\ N^2=0,\ PN=0\}.
\]
Write \(X_n(r,h)\) for the locus where \(\operatorname{rank}P=r\) and \(\operatorname{rank}N=h\). The strata are nonempty precisely when \(0\le h\le\lfloor n/2\rfloor\) and \(0\le r\le n-h\). Each stratum is smooth and geometrically irreducible and has dimension
\[
d_n(r,h)=2h(n-h)+r(2n-h-2r).
\]
For every prime power \(q\), the exact number of labeled pairs in this stratum over \(\mathbb F_q\) is
\[
C_{n,q}(r,h)={n\brack h}_q{n-h\brack h}_q\,|\mathrm{GL}_h(\mathbb F_q)|\,{n-h\brack r}_q\,q^{r(n-r)}.
\]
The total number of pairs is the sum over the displayed admissible ranks. Here \({a\brack b}_q\) denotes the Gaussian binomial coefficient and \(|\mathrm{GL}_0(\mathbb F_q)|=1\).

The reduced variety has dimension
\[
\dim X_n=\left\lfloor\frac{4n^2}{5}\right\rfloor.
\]
The **exact number of its geometric irreducible components of maximal dimension** is \(1\) if \(n\equiv0,2,3\pmod5\), \(3\) if \(n\equiv1,4\pmod5\) with \(n\ge4\), and \(2\) when \(n=1\).

More precisely, put \(n=5a+b\) with \(0\le b<5\). The maximal-dimensional ordered rank profiles \((r,h)\) are:

| \(b\) | Maximal-dimensional \((r,h)\) |
| --- | --- |
| \(0\) | \((2a,2a)\) |
| \(1\), \(a\ge1\) | \((2a,2a),(2a+1,2a),(2a,2a+1)\) |
| \(2\) | \((2a+1,2a+1)\) |
| \(3\) | \((2a+1,2a+1)\) |
| \(4\) | \((2a+2,2a+2),(2a+2,2a+1),(2a+1,2a+2)\) |

At \(n=1\), the profiles are \((0,0),(1,0)\).

## Assumptions and scope

The field \(k\) is arbitrary, of any characteristic. The geometric assertions refer to the **reduced** algebraic variety over an algebraic closure of \(k\); they do not assert reducedness or smoothness of the full polynomial-equation scheme. The equations are ordered: \(PN=0\) is required, while \(NP=0\) is not. Matrix size satisfies \(n\ge1\); no invertibility or commutation hypothesis is assumed. All finite-field formulas count individual labeled ordered matrix pairs, without dividing by simultaneous conjugacy.

## Proof

**1. Square-zero rank orbits.** Put \(V=k^n\). For \(N^2=0\), its image \(L=\operatorname{im}N\) lies in \(\ker N\). If \(h=\dim L\), necessarily \(2h\le n\). Conversely every such \(h\) occurs. Every square-zero operator of rank \(h\) is conjugate over \(k\) to \(h\) Jordan blocks of size two and \(n-2h\) blocks of size one. Equivalently, specifying \(N\) is the same as specifying nested subspaces \(L\subset K\subset V\), where \(\dim L=h\), \(\dim K=n-h\), together with an isomorphism \(V/K\to L\). Over \(\mathbb F_q\), these choices give exactly
\[
{n\brack h}_q{n-h\brack h}_q|\mathrm{GL}_h(\mathbb F_q)|
\]
operators. Geometrically they form one smooth, geometrically irreducible conjugacy orbit of dimension \(2h(n-h)\): the flag choices have dimensions \(h(n-h)+h(n-2h)\), and the isomorphism has dimension \(h^2\).

**2. Projection fibers.** For a fixed square-zero \(N\) with image \(L\), the equation \(PN=0\) is equivalent to \(L\subseteq\ker P\). A rank-\(r\) idempotent is uniquely determined by an ordered direct-sum splitting \(V=U\oplus W\), where \(\operatorname{im}P=U\), \(\ker P=W\), \(\dim U=r\), \(\dim W=n-r\). Hence \(r\le n-h\). The allowable \(W\) containing \(L\) form a Grassmannian \(\operatorname{Gr}(n-r-h,V/L)\) with point count \({n-h\brack r}_q\) and dimension \(r(n-h-r)\). For each \(W\), complements \(U\) form an affine space of dimension \(r(n-r)\), with \(q^{r(n-r)}\) rational points. These constructions are compatible with base change and give a smooth, geometrically irreducible affine bundle over a relative Grassmannian. Multiplying the counts yields \(C_{n,q}(r,h)\); adding dimensions yields \(d_n(r,h)\). In particular, there are no other pairs or rank profiles.

**3. Sharp dimension.** For real \(r,h\), completion of squares gives
\[
\frac{4n^2}{5}-d_n(r,h)
=2\left(r-\frac{2n}{5}\right)^2
+\left(r-\frac{2n}{5}\right)\left(h-\frac{2n}{5}\right)
+2\left(h-\frac{2n}{5}\right)^2\ge0.
\]
The quadratic form is positive definite. The integer \(d_n(r,h)\) is therefore at most \(\lfloor4n^2/5\rfloor\). Set \(r=h\) to the closest integer to \(2n/5\) (either choice in the unique feasible cases); this is admissible for every \(n\ge1\) and attains \(\lfloor4n^2/5\rfloor\). Thus the bound is sharp.

**4. Five residue phases.** To classify *all* maximizers, write \(n=5a+b\) with \(b\in\{0,1,2,3,4\}\). The displayed positive-definite quadratic form has least eigenvalue \(3/2\), so an integral maximizer must choose both \(r,h\) from the two adjacent integers around \(2n/5\): any coordinate differing by at least one gives a deficit at least \(3/2\), while the exhibited deficit is at most \(4/5\). Substituting these four possibilities gives precisely the residue table, after enforcing \(h\le\lfloor n/2\rfloor\) and \(r\le n-h\); the only boundary exception is \(n=1\).

**5. Top-dimensional irreducible components.** The finitely many rank strata are locally closed, smooth and geometrically irreducible. Each stratum of maximal dimension has irreducible closure of the dimension of the whole variety and hence supplies an irreducible component. Distinct such strata cannot have the same closure: two distinct, disjoint, dense locally closed subsets of one irreducible variety would each contain a nonempty open subset and therefore intersect. Conversely, each full-dimensional irreducible component contains a dense rank stratum of maximal dimension by finite stratification. The number of top-dimensional components is therefore exactly the number of maximal rank profiles found in step 4.

## Verification

Run the embedded dependency-free file `verify_mixed_pairs.py` using Python 3. The checker independently enumerates *every* matrix over prime fields for \((n,q)=(1,2),(2,2),(2,3),(3,2),(3,3)\), tests the original equations, computes both ranks, and compares every rank cell against the closed formula. It also calculates the integer maxima and their profile sets for \(1\le n\le40\). These tests support, but do not replace, the all-field proof.

Representative exact totals are \(2,17,415,27997,5697089,3219343649\) over \(\mathbb F_2\) for dimensions \(1\) through \(6\), respectively. Over \(\mathbb F_3\), the totals for dimensions \(2,3\) are \(46,5020\). The final program marker is `MIXED_PAIR_DIRECT_CHECK_PASS`.

## Relationship to prior work

Schröer, *Varieties of pairs of nilpotent matrices annihilating each other* (arXiv:math/0211293, 2002), classifies components for **two nilpotent matrices subject to both product orders vanishing** and nilpotence bounds. In contrast, one matrix here is **idempotent**, only \(PN=0\) is imposed, and \(NP\) may be nonzero. The proof method shares the language of matrix-representation strata but this theorem's explicit one-sided mixed equations, rank counts, sharp \(4/5\) dimension and residue-five top-component count are not statements of that work.

The two-dimensional zero-product factorization fiber is previously known in the literature of idempotent–nilpotent matrix products; it is **not claimed new**. Dolžan, *Products of Nilpotent and Idempotent Matrices over Finite Local Rings* (arXiv:2608.20934, 2026), studies products of two-by-two matrices and counts distinct realizable products, rather than the all-dimensional distribution of pairs or its geometric components. A broader unpublished or unlocated mixed-matrix representation theorem may imply some or all of the present formulas; independent historical-priority verification remains open.

## Limitations

Only one-sided annihilation and nilpotence index at most two are considered. No assertion is made about nonreduced scheme structure, a complete list of components of smaller dimension, simultaneous-conjugacy classes, or higher nilpotence indices. The full range of geometrically irreducible components is not classified; the count here concerns only those of maximal dimension. Finite enumerations are not infinite certificates.

## References

1. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293, first posted 2002-11-19; published in *Commentarii Mathematici Helvetici* **79** (2004), 396–426. https://arxiv.org/abs/math/0211293
2. D. Dolžan, *Products of Nilpotent and Idempotent Matrices over Finite Local Rings*, arXiv:2608.20934, first posted 2026-08-21. https://arxiv.org/abs/2608.20934
