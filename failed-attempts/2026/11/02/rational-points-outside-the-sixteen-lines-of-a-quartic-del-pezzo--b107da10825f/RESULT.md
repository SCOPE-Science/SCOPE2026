# Rational points outside the sixteen lines of a quartic del Pezzo surface: all Frobenius types

## Finding
Let \(S\) be a smooth del Pezzo surface of degree \(4\) over \(\mathbb F_q\), and let \(U\) be the complement of the union of its sixteen geometric exceptional curves. Choose a marking of the geometric Picard lattice and let \(g\in W(D_5)\) represent arithmetic Frobenius. Write \(t(g)\) for the trace on the five-dimensional root lattice; write \(f(g)\) for its number of fixed exceptional curves, \(a(g)\) for the number of intersections between *two individually fixed* exceptional curves, and \(b(g)\) for the number of pairs of intersecting exceptional curves interchanged by Frobenius. Then
\[
\boxed{\#U(\mathbb F_q)=q^2+[1+t(g)-f(g)]q+1-f(g)+a(g)-b(g).}
\]
All four quantities are determined by the signed-cycle type of \(g\), giving the following exhaustive table of eighteen possible polynomials (not every type is geometrically realized over every small field). In the first two columns, `+` and `-` denote partitions of the lengths of positive and negative signed cycles; the third is the number of elements of the class in \(W(D_5)\). The remaining columns are \(f,a,b,t\) and the open-locus count.

| + | - | Class size | \(f\) | \(a\) | \(b\) | \(t\) | \(\#U(\mathbb F_q)\) |
|---|---|---:|---:|---:|---:|---:|---|
| 11111 | — | 1 | 16 | 40 | 0 | 5 | \(q^2-10q+25\) |
| 2111 | — | 20 | 8 | 12 | 0 | 3 | \(q^2-4q+5\) |
| 221 | — | 60 | 4 | 2 | 2 | 1 | \(q^2-2q-3\) |
| 311 | — | 80 | 4 | 4 | 0 | 2 | \(q^2-q+1\) |
| 32 | — | 160 | 2 | 0 | 0 | 0 | \(q^2-q-1\) |
| 41 | — | 240 | 2 | 1 | 1 | 1 | \(q^2-1\) |
| 5 | — | 384 | 1 | 0 | 0 | 0 | \(q^2\) |
| 111 | 11 | 10 | 0 | 0 | 0 | 1 | \(q^2+2q+1\) |
| 1 | 1111 | 5 | 0 | 0 | 8 | -3 | \(q^2-2q-7\) |
| 11 | 21 | 60 | 0 | 0 | 0 | 1 | \(q^2+2q+1\) |
| 1 | 22 | 60 | 0 | 0 | 0 | 1 | \(q^2+2q+1\) |
| 1 | 31 | 160 | 0 | 0 | 2 | 0 | \(q^2+q-1\) |
| — | 2111 | 20 | 0 | 0 | 0 | -3 | \(q^2-2q+1\) |
| 21 | 11 | 60 | 0 | 0 | 4 | -1 | \(q^2-3\) |
| 2 | 21 | 120 | 0 | 0 | 0 | -1 | \(q^2+1\) |
| 3 | 11 | 80 | 0 | 0 | 0 | -2 | \(q^2-q+1\) |
| — | 32 | 160 | 0 | 0 | 0 | 0 | \(q^2+q+1\) |
| — | 41 | 240 | 0 | 0 | 0 | -1 | \(q^2+1\) |

**Sharp empty-complement classification.** For an *existing* smooth quartic del Pezzo surface, \(U(\mathbb F_q)\) is empty if and only if either (i) \(q=3\) and Frobenius has two positive cycles of length two and one positive fixed coordinate (signed type `+221`), or (ii) \(q=5\) and Frobenius is the identity (`+11111`). Both possibilities occur. In particular every such surface over \(\mathbb F_q\) with \(q\ge7\) has a rational point lying on no geometric exceptional curve.

## Assumptions and scope
The surface is **smooth**, geometrically integral, and del Pezzo of degree four over a finite field of arbitrary characteristic. The exceptional divisor is the *reduced geometric union* of all sixteen \((-1)\)-curves; a rational point on any non-rational geometric component is excluded as well. Frobenius is the action on the geometric Picard lattice. A marking identifies the five-dimensional orthogonal complement of the canonical class with the \(D_5\) root lattice and Frobenius with an even signed permutation of its five coordinates. A signed cycle is *positive* when the product of its coordinate signs is \(+1\), and *negative* otherwise. Such an even signed permutation has an even number of negative cycles. The result is conditional on the signed-cycle type being realized by a smooth surface over the field; no assertion of simultaneous realization of all types is made.

## Proof
**1. The exceptional-curve incidence graph.** Over an algebraic closure, \(S\) is the blow-up of \(\mathbb P^2\) in five points in general position. Its sixteen exceptional-curve classes are \(E_i\), \(H-E_i-E_j\) for \(i<j\), and \(2H-\sum_iE_i\). Each curve meets exactly five others transversely and no three have a common point. Thus the incidence graph has sixteen vertices, forty edges, and no triangles. Identifying its vertices with even subsets of \(\{1,\dots,5\}\), two vertices are joined exactly when their symmetric difference has cardinality four. The automorphism group of this graph is \(W(D_5)\); sign changes with even parity and coordinate permutations give the action \(x\mapsto p(x)\mathbin\triangle s\).

**2. Rational points on the exceptional divisor.** An \(\mathbb F_q\)-point of a geometric exceptional curve either belongs to a Frobenius-fixed curve or must lie in the intersection of that curve with its Frobenius image. Since there are no triple intersections, the second case can only occur when Frobenius interchanges two intersecting curves. Every fixed curve is an \(\mathbb F_q\)-form of \(\mathbb P^1\), hence has \(q+1\) rational points. Of the intersections of fixed curves, precisely \(a(g)\) have been counted twice. Each of the \(b(g)\) interchanged edges supplies one further rational point; it belongs to neither fixed curve. These points are distinct by the absence of triple intersections. Therefore
\[
\#(S\setminus U)(\mathbb F_q)=f(g)(q+1)-a(g)+b(g).
\]

**3. The ambient surface.** The Weil-Lefschetz trace formula, with the standard cohomology of a geometrically rational surface, gives
\[
\#S(\mathbb F_q)=q^2+q\operatorname{tr}(g\mid\operatorname{Pic}(\bar S))+1=q^2+[1+t(g)]q+1.
\]
Subtracting the boundary count proves the boxed formula.

**4. Exact classification over the entire Weyl group.** An even signed permutation is specified by a coordinate permutation \(p\in S_5\) and an even-parity sign vector \(s\in\mathbb F_2^5\). There are \(120\cdot16=1920\) elements. The companion `verify.py` enumerates every element; computes its signed-cycle type; computes \(f,a,b\) from the sixteen vertices and forty edges; computes the root trace directly from the signed permutation matrix; and verifies that all elements of each of the eighteen types have exactly the asserted invariants. Thus the table is a finite, exhaustive group computation, not a sample of surfaces. Checking the eighteen explicit quadratic polynomials for all prime-power values \(q\ge2\) reduces to the small values \(2\le q\le6\), since for \(q\ge7\) they are all strictly positive; the only zeros are at \(q=3\) for `+221` and \(q=5\) for `+11111`. Some classes yield a negative numerical polynomial at \(q=2\) or \(3\); such a class simply cannot be realized by a smooth surface over that field, because its point count cannot be negative.

**5. Both zeros are realized.** For \(q=5\), blow up \(\mathbb P^2_{\mathbb F_5}\) at any five distinct rational points of the smooth conic \(XZ=Y^2\); they are in general position and yield split type `+11111`. The formula gives \(\#U(\mathbb F_5)=(5-5)^2=0\). For \(q=3\), take \(\mathbb F_9=\mathbb F_3[i]\) with \(i^2=-1\) and blow up the conic points \([1:t:t^2]\) for \(t=0,i,-i,1+i,1-i\). This Frobenius-stable set has orbit type \((1)(2)(2)\), giving positive signed type `+221`. Its formula gives \(\#U(\mathbb F_3)=3^2-2\cdot3-3=0\). The verifier independently enumerates all rational projective-plane points off the ten joining lines and the conic; it reproduces zero for this example. Its split five-point \(\mathbb F_7\) example yields four rational complement points.

## Verification
Run `python3 verify.py` with Python 3.10 or newer; only the standard library is needed. Its checks include all sixteen even-parity vertices, all forty incidence edges, the complete \(1920\)-element even signed permutation group, an eighteen-type partition with class sizes summing to \(1920\), signed-cycle invariance of every table entry, all zero and negative small-field polynomials, and two explicit finite-field blow-up configurations. A successful run terminates with `VERIFY_OK`. Group enumeration proves the complete *finite combinatorial* table; the Weil-Lefschetz formula, classification of exceptional curves, and no-triple-intersection geometry are mathematical inputs separately proved or cited above. The verifier does not claim to realize every Weyl conjugacy class over every finite field.

## Relationship to prior work
The geometry of sixteen exceptional curves, their \(D_5\)-Weyl action, and the Frobenius-trace formula are classical. Rybakov (2005) studies zeta functions of degree-four del Pezzo surfaces; Banwait, Fité and Loughran (2016) tabulate Frobenius trace and rational point counts for del Pezzo surfaces. Neither gives in the inspected material the count on the *complement of all sixteen curves* for the eighteen signed types. Knecht (2013 preprint) analyzes rational points off exceptional loci in the construction of unirational parametrizations, emphasizing the motivation for their existence; Hirschfeld had previously classified several split-surface line-covered cases, so the split \(q=5\) zero by itself is not proposed as new. A public study entitled *Integral homology of the five-point parabolic very-stable surface* determines the integral homology of the complex complement of exactly these sixteen curves, but not its finite-field Frobenius-stratified counts. The claimed contribution is the full equivariant boundary point-count table and the exact two-type emptiness classification, not the known individual inputs.

## Limitations
The eighteenth-type table is a list of **conditional** count formulas for Weyl actions. It is not a classification of which signed types occur at each small field. No unique historical priority is proved: the full equivariant tabulation may be implicit in earlier finite-geometry or Weyl-group discussions; the older Hirschfeld classification is particularly relevant to the split case. The computational certificate is exhaustive over the finite Weyl group but does not independently reprove the classical geometry or the Grothendieck–Lefschetz trace formula. The theorem makes no claims about unirationality degrees, Brauer groups, or rationality of the surface.

## References
1. A. Knecht, *Degree of Unirationality for del Pezzo Surfaces over Finite Fields*, arXiv:1307.3215v1 (first publicly posted 2013-07-11); Journal de théorie des nombres de Bordeaux **27** (2015), 171–182.
2. B. Banwait, F. Fité, D. Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, arXiv:1606.00300v1 (2016-06-01).
3. S. Rybakov, *Zeta functions of conic bundles and del Pezzo surfaces of degree 4 over finite fields*, Moscow Mathematical Journal **5** (2005), 919–926.
4. A. Knecht and K. Reyes, *Full Degree Two del Pezzo Surfaces over Small Finite Fields*, arXiv:1510.04621v1 (2015-10-15), referring to Hirschfeld's earlier split cases.
5. *Integral homology of the five-point parabolic very-stable surface*, publicly available mathematical research record, https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-integral-homology-of-the-five-point-parabolic-very-stable-surfac--7a46e6c434a8/RESULT.md (different invariant over \(\mathbb C\)).
