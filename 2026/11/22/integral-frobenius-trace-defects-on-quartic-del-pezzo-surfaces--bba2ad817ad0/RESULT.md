# Integral Frobenius trace defects on quartic del Pezzo surfaces

## Finding

Let \(X\) be a smooth degree-four del Pezzo surface over any finite field \(\mathbb F_q\). Let \(F\) be arithmetic Frobenius acting on the rank-six geometric Picard lattice \(P=\operatorname{Pic}(X_{\overline{\mathbb F}_q})\). Let \(\mathcal E\) be its sixteen geometric exceptional \((-1)\)-curves. For each \(F\)-orbit \(O\subset\mathcal E\), let \(D_O=\sum_{E\in O}[E]\in P^F\), and put \(L_F=\sum_O\mathbb Z D_O\).

**Theorem.** For every such surface, \(L_F\) has full rank in \(P^F\), and its finite index is one of \(1,2,4,16\). Across the eighteen conjugacy classes of \(W(D_5)\), precisely twelve have index \(1\), three have index \(2\), two have index \(4\), and one has index \(16\). No other index is possible. All six nonunit cases are listed in the accompanying exact eighteen-row certificate.

The class with index \(16\) has order four, invariant Picard rank three, four Frobenius orbits of length four on the sixteen exceptional curves, and conjugacy class size sixty in \(W(D_5)\). In fact, **four distinct order-four classes** have the identical exceptional-curve cycle pattern \(4^4\) and indices \(1,2,4,16\), respectively. Even when invariant Picard rank is fixed at two, there are two classes with the same pattern \(4^4\) but different indices \(2\) and \(4\). Thus the complete extension-field counts of exceptional curves, even together with their invariant Picard rank, need not determine the integral orbit-trace index.

The rational arithmetic effective cone \(\operatorname{Eff}(X_{\overline{\mathbb F}_q})\cap(P^F\otimes\mathbb R)\) is generated as a real cone by the divisor classes \(D_O\), irrespective of the integral index.

| Index \([P^F:L_F]\) | Number of conjugacy classes |
|---|---:|
| \(1\) | 12 |
| \(2\) | 3 |
| \(4\) | 2 |
| \(16\) | 1 |

## Assumptions and scope

The surface is smooth, projective, and of anticanonical degree four; no splitness or restriction on the finite field's characteristic is assumed. The sixteen curves and six-dimensional lattice are understood geometrically after base change to an algebraic closure. The index is an **integral** lattice index, not the quotient of real effective cones. The claimed classification is conditional on the Frobenius type actually arising for the chosen field; it does not claim that every type occurs over every finite field. Frobenius conjugacy classes lie in the order-\(1920\) Weyl group \(W(D_5)\).

## Proof

1. Over the algebraic closure, write \(X\) as a blow-up of \(\mathbb P^2\) in five points in general position, with basis \((H,E_1,\ldots,E_5)\), intersection form \(\operatorname{diag}(1,-1,-1,-1,-1,-1)\), and canonical class \(K=-3H+\sum_iE_i\). The sixteen exceptional classes are the five \(E_i\), ten \(H-E_i-E_j\) with \(i<j\), and one \(2H-\sum_iE_i\). Their classes generate \(P\).
2. The simple roots \(H-E_1-E_2-E_3\), \(E_1-E_2\), \(E_2-E_3\), \(E_3-E_4\), \(E_4-E_5\) are orthogonal to \(K\) and have self-intersection \(-2\). The five reflections \(s_r(v)=v+(v\cdot r)r\) preserve the form and permute the sixteen exceptional classes. They generate \(W(D_5)\); the independent exact group construction in the verifier obtains all \(1920\) elements and enumerates its \(18\) conjugacy classes.
3. For any such group element \(F\), form a \(6\times k\) integer matrix \(A_F\) whose columns are orbit sums of the exceptional classes, with \(k\) the number of orbits. Every column lies in \(P^F\). The verifier computes the rational rank \(r\) of \(A_F\) and separately \(6-\operatorname{rank}(F-I)\), checking that they agree in all eighteen classes. This proves that \(L_F\otimes\mathbb Q=P^F\otimes\mathbb Q\).
4. The integer kernel \(P^F=\ker(F-I:\mathbb Z^6\to\mathbb Z^6)\) is saturated: if a nonzero integer multiple of a vector is fixed, the vector itself is fixed. Therefore the index \([P^F:L_F]\) is exactly the greatest common divisor of all \(r\times r\) minors of \(A_F\), by the integer determinantal-divisor theorem. The exact verifier computes all those minors using a fraction-free determinant, and obtains the eighteen-row certificate. Sorting the indices yields \(1^{12},2^3,4^2,16\). Filtering the order-four, orbit-pattern-\(4^4\) rows produces all four indices, including two rank-two representatives with indices \(2\) and \(4\).
5. The geometric effective cone of a del Pezzo surface is the positive real span of its exceptional curves. For an invariant effective real combination, average its coefficients over the finite cyclic Frobenius action. Its class becomes a nonnegative real combination of the \(D_O\). Conversely every \(D_O\) is effective. This proves the final cone assertion, which makes no claim about the integral effective semigroup.

## Verification

The standalone Python 3 file `verify_quartic_trace_lattice.py` uses only the standard library. Run `python3 verify_quartic_trace_lattice.py > actual.csv` and compare `actual.csv` byte-for-byte with `quartic_trace_lattice_classes.csv`. It constructs all \(1920\) Weyl elements by integer reflection matrices and their faithful actions on sixteen curves; conjugation by simple reflections partitions them into \(18\) classes whose sizes sum to \(1920\). It computes exact fixed-lattice ranks, orbit-sum ranks, and gcds of all maximal minors (no floating-point arithmetic). Its internal assertions verify the full index distribution and the four indistinguishable \(4^4\) line-cycle patterns.

An explicit reflection word for the index-\(16\) class is `32413454134`, with digits indexing the five simple roots in the order above. This word is a **computational representative**, not an arbitrary numerical sample. The file's other seventeen rows provide complete reproduction data.

## Relationship to prior work

Trepalin's finite-field classification gives the \(18\) quartic del Pezzo Frobenius conjugacy classes and their invariant Picard ranks; Blache–Hallouin systematically treat Weyl-group Frobenius types and zeta functions. Those tables classify the rational representation and line permutations but do **not** supply the integral lattice generated by sums of exceptional-curve orbits, nor its saturation indices. The present invariant depends on integer congruence information omitted by the eigenvalue and orbit-count data: two rank-two classes even share the same line-orbit pattern yet have different indices.

A known analogous index computation on degree-five del Pezzo surfaces concerns a different Weyl group and ten, rather than sixteen, exceptional curves. Work on the generalized Jacobian of the sixteen-curve boundary of a quartic del Pezzo surface concerns the Picard group of the **boundary curve**, not the invariant integral Picard lattice of the surface.

## Limitations

This is a classification of the trace-generated lattice for geometric exceptional curves, not of the integral semigroup of rational effective divisors. The finite-field existence of every Weyl conjugacy type for a **fixed** small field is not claimed. The result does not reconstruct an actual surface, the Brauer group, or an intersection form from line counts. The computations are exact finite group calculations and, unlike statistical samples, exhaust all conjugacy classes; they have not received independent mathematical audit. An unindexed equivalent calculation in historical del Pezzo arithmetic cannot be excluded solely by searchable literature.

## References

- A. Trepalin, *Del Pezzo surfaces over finite fields* (first posted March 2018), https://arxiv.org/abs/1803.07421 , especially the degree-four surface classification and its eighteen-class table.
- R. Blache and E. Hallouin, *Classification of singular del Pezzo surfaces over finite fields* (first posted January 2023), https://arxiv.org/abs/2301.13582 , for related Frobenius/Weyl-group arithmetic and geometric Picard representations.
- *Integral Frobenius trace lattices and arithmetic cones of degree-five del Pezzo surfaces*, publicly available research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-integral-frobenius-trace-lattices-and-arithmetic-cones-of-degree--14de99fa5b64 , for the distinct degree-five analogue.
- *Five induced quintic tori for the sixteen-line boundary of a quartic del Pezzo surface*, publicly available research note, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-five-induced-quintic-tori-for-the-sixteen-line-boundary-of-a-qua--5411549db544 , for a different boundary-Picard invariant.
