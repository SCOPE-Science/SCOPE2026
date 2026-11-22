# Tame cyclic and wild symmetric trigonal branch profiles of all minimal binary quadric-filling curves

## Finding

Let \(Q=\mathbb P^1_{\mathbb F_2}\times\mathbb P^1_{\mathbb F_2}\), and let \(C\subset Q\) be a geometrically smooth divisor of bidegree \((4,3)\) containing every point of \(Q(\mathbb F_2)\). Write \(\pi:C\to\mathbb P^1\) for projection onto the first ruling, a separable morphism of degree three. There are exactly \(66\) such curves, in four orbits under the ruling-preserving group \(\operatorname{PGL}_2(\mathbb F_2)^2\); those counts are known. The **new classification** gives the complete geometric ramification, arithmetic branch-point splitting, and monodromy of \(\pi\):

| Equation mask | Embedded orbit size | Branch support degrees over \(\mathbb F_2\) | Ramification at each geometric branch point | Geometric monodromy |
|:--:|--:|:--:|:--:|:--:|
| `396246` | 6 | \((8)\) | \(e=3\), tame | \(C_3\) |
| `399606` | 18 | \((8)\) | \(e=2\), wild | \(S_3\) |
| `404886` | 36 | \((8)\) | \(e=2\), wild | \(S_3\) |
| `420790` | 6 | \((2,6)\) | \(e=3\), tame | \(C_3\) |

Consequently, exactly \(12\) of the \(66\) degree-three projections are tame cyclic Galois covers, and the remaining \(54\) have wild ramification and geometric monodromy \(S_3\). Every projection has exactly eight geometric branch values, no rational branch value, and different divisor of degree \(16\) supported on eight distinct geometric ramification points; each local different exponent is \(2\). The wild projections are weakly ramified at every branch value. The Frobenius action on the branch support is an eight-cycle for \(60\) curves and a \((2,6)\)-cycle for the other \(6\).

## Assumptions and scope

We work entirely over \(\mathbb F_2\). A *filling* curve satisfies \(C(\mathbb F_2)=Q(\mathbb F_2)\), so it has exactly nine rational points. Smoothness means geometric smoothness. The first coordinate is \([X_0:X_1]\) and the second \([Y_0:Y_1]\). For a section \(F\) of bidegree \((4,3)\), write

\[
F=\sum_{i=0}^{4}\sum_{j=0}^{3}\epsilon_{ij}X_0^{4-i}X_1^iY_0^{3-j}Y_1^j,\qquad
m(F)=\sum_{i,j}\epsilon_{ij}2^{4i+j},\quad\epsilon_{ij}\in\mathbb F_2.
\]

The *mask* is \(m(F)\); its numerical value depends on this declared monomial ordering. The genus of every smooth member is \((4-1)(3-1)=6\). The degree-three map is induced by the first ruling, not by the second (which gives a degree-four morphism). Cycle partitions in the table describe closed points in the reduced geometric branch divisor, not orbits on the three sheets.

## Proof

**Exhaustion and geometry.** Evaluate the twenty basis monomials at all nine rational product points. The evaluation matrix over \(\mathbb F_2\) has rank nine, leaving \(2^{11}=2048\) filling sections including zero. Enumerate all \(2047\) nonzero sections. On all four standard affine charts, a section \(f\) defines a geometrically smooth curve precisely when the ideal \((f,f_x,f_y)\) is the unit ideal in \(\mathbb F_2[x,y]\). Exact characteristic-two Gröbner bases yield precisely \(66\) such sections. They form four orbits under the \(36\) first/second-ruling coordinate changes, with representatives and orbit sizes exactly those in the table. The supplied verifier reconstructs these facts from the full parameter space, independently of published census tables. Smoothness and positive bidegrees imply geometric integrality; adjunction gives genus six.

**The half-discriminant.** On \(X_0=Y_0=1\), write

\[
f(x,y)=a_3(x)y^3+a_2(x)y^2+a_1(x)y+a_0(x),\qquad\deg a_j\le4.
\]

The characteristic-two cubic discriminant (the resultant of \(f\) and \(f_y\), with leading homogeneous coefficient included) equals

\[
\operatorname{Disc}_y(f)=D(x)^2,\qquad
D(x)=a_3(x)a_0(x)+a_2(x)a_1(x).
\]

For all four representatives, \(D\) is a squarefree polynomial of degree eight, has \(D(0)=D(1)=1\), and is nonzero at infinity after homogenization. In addition \(\gcd(D,a_3)=1\). Thus exactly eight geometric branch values occur, none rational, and all finite branch fibers are genuine cubic polynomials.

**Double versus triple ramification.** At a root of \(D\), the cubic has a repeated root. It is a triple root exactly when

\[
T=a_2^2+a_3a_1=0
\]

there, equivalently when the root lies in \(\gcd(D,T)\). Exact polynomial gcd shows \(\gcd(D,T)=D\) for masks `396246` and `420790`, and \(\gcd(D,T)=1\) for masks `399606` and `404886`. The former therefore have one triply supported fiber at each branch value; the latter have a double point and a distinct simple point. Since \(C\) is geometrically smooth, the local map has indices \(3\) and \(2\), respectively. In characteristic two, these are tame and wild as indicated.

**Branch fields.** Exact factorization over \(\mathbb F_2[x]\) gives the four half-discriminants, all with distinct roots:

| Mask | Half-discriminant \(D(x)\) | Irreducible-factor degrees |
|:--:|---|:--:|
| `396246` | \(x^8+x^6+x^5+x^4+x^3+x+1\) | \((8)\) |
| `399606` | \(x^8+x^5+x^4+x^3+1\) | \((8)\) |
| `404886` | \(x^8+x^7+x^6+x^5+x^4+x^3+1\) | \((8)\) |
| `420790` | \(x^8+x+1=(x^2+x+1)(x^6+x^5+x^3+x^2+1)\) | \((2,6)\) |

Every other smooth section lies in an orbit of one of the representatives, and base-line automorphisms over \(\mathbb F_2\) preserve the number and degrees of closed branch points and the local ramification type.

**Monodromy and different.** The subgroup of \(\operatorname{PGL}_2(\mathbb F_2)\) acting only on the \(Y\)-coordinate and preserving the representative has order three in both triple-fiber cases, and order one in both double-fiber cases. Consequently, the two triple-fiber projections admit a rational order-three deck transformation and are cyclic Galois. The double-fiber cases cannot be geometrically cyclic, since a separable cyclic cubic extension is tamely ramified in characteristic two, whereas here the geometric index is two. Every separable transitive cubic extension has geometric monodromy either \(C_3\) or \(S_3\), so the double-fiber cases have \(S_3\).

The Riemann–Hurwitz formula gives degree of the different \(2g(C)-2+6=16\). There are exactly eight distinct ramification points. A tame index-three point has different exponent two; a wildly ramified index-two point has different exponent at least two. Hence the latter cases must each have different exponent exactly two, with no other ramification. For an index-two local extension in characteristic two this is the weakly ramified case. The classification follows.

## Verification

Run `python verify_filling43_branch.py` using Python 3 and SymPy. The program regenerates the entire \(2048\)-section filling linear space, checks all four affine Jacobian ideals for all nonzero sections, constructs the full \(36\)-element factor-preserving group action, checks its four smooth orbits and their sizes, computes the four cubic half-discriminants, verifies their factorization and squarefreeness and the \(\gcd(D,T)\) dichotomy, and detects the fiberwise order-three deck transformations. Expected final marker:

```text
FILLING43_RAMIFICATION_VERIFIED equations=2048 smooth=66 orbits=4 cyclic_tame=12 S3_wild=54 branch_cycle_profiles=(8)x3,(2+6)x1
```

This is an exact finite proof for this finite coefficient space; no assertion concerning arbitrary fields or bidegrees is inferred from experimentation.

## Relationship to prior work

Homma and Kim (2022, Theorem 4.1) proved that \((4,3)\) and \((3,4)\) are the minimum bidegrees of irreducible filling curves over \(\mathbb F_2\), and explicitly constructed a smooth example. Previously published exact computations classify all \(66\) smooth sections into four ambient orbits, their stabilizers and their Weil polynomials. Those statements are taken as prior results, not claimed here. The newly calculated invariant is the complete **geometric Hurwitz ramification type and Frobenius splitting of the branch divisor** of their degree-three projections, including the tame/wild dichotomy and local different. Even knowing the orbit sizes, stabilizer orders and zeta polynomials does not provide the eight-point branch factorization or wild different exponents without additional work.

A previously published census of degree-three projections of smooth genus-four \((3,3)\) curves counts rational *totally ramified* fibers. It treats another genus and does not address the degree-eight geometric branch support of the present degree-three projections. Work on cyclic trigonal septics studies Cartier strata of a different family; it does not supply the four branch polynomials above.

## Limitations

Only the first-ruling projections of smooth minimal-filling bidegree-\((4,3)\) curves on the split quadric over \(\mathbb F_2\) are classified. The theorem does not classify all degree-three maps from the underlying abstract curves, all possible twists, or the full moduli of degree-three covers. It also does not determine higher ramification filtrations of the complete six-sheeted \(S_3\) Galois closures. Finite exact algebra establishes these results within the stated family; a previously unindexed equivalent ramification computation remains a historical-priority risk. No independent external mathematical audit has been performed.

## References

1. M. Homma and S. J. Kim, *Filling curves for \(\mathbb P^1\times\mathbb P^1\)*, arXiv:2203.11595 (initially public 2022-03-22), especially Theorem 4.1. https://arxiv.org/abs/2203.11595
2. *Four arithmetic classes of minimum-degree smooth filling curves on \(\mathbb P^1\times\mathbb P^1\) over \(\mathbb F_2\)* (2026-11-08), publicly available at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-four-arithmetic-classes-of-minimum-degree-smooth-filling-curves--a6904b15fda5 .
3. *Four ambient symmetry classes of minimal smooth filling curves on the binary quadric* (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-four-ambient-symmetry-classes-of-minimal-smooth-filling-curves-o--e7a76829ef36 .
4. *Paired total-ramification spectra of binary genus-four trigonal curves on the split quadric* (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-paired-total-ramification-spectra-of-binary-genus-four-trigonal--6b3c6b41e8c6 .
5. *Three complete Cartier-iterate strata for genus-six cyclic trigonal covers in characteristic two* (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-complete-cartier-iterate-strata-for-genus-six-cyclic-trigo--cb7dccd8ed2c .
