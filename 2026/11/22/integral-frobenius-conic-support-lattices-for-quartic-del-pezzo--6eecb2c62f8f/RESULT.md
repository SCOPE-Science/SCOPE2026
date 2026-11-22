# Integral Frobenius conic-support lattices for quartic del Pezzo surfaces

## Finding
Let \(S/\mathbb F_q\) be any smooth degree-four del Pezzo surface, in arbitrary characteristic. Its sixteen geometric exceptional curves form a finite Frobenius set \(\mathcal L\), and its ten geometric conic-fibration classes form a second finite Frobenius set \(\mathcal P\). Each pencil has four reducible geometric fibers and thus eight distinct exceptional-curve components. Define the canonical unsigned support map
\[
\Phi:\mathbb Z^{\mathcal P}\longrightarrow\mathbb Z^{\mathcal L},\qquad
[p]\longmapsto\sum_{\ell\text{ a component of a reducible fiber of }p}[\ell].
\]
It is equivariant for the type-\(D_5\) Weyl group. The restriction \(\Phi^F:(\mathbb Z^{\mathcal P})^F\to(\mathbb Z^{\mathcal L})^F\) to geometric Frobenius invariant **integral permutation lattices** has the following exact cokernels for all eighteen signed-cycle conjugacy classes in \(W(D_5)\). The columns \(r_{\mathcal L},r_{\mathcal P}\) denote the numbers of line and pencil Frobenius orbits; \(s\) is the rank of \(\Phi^F\), and \(f=r_{\mathcal L}-s\).

| Signed cycle type | \(|\mathrm{class}|\) | \(r_{\mathcal L}\) | \(r_{\mathcal P}\) | \(s\) | \(f\) | Torsion in \(\operatorname{coker}\Phi^F\) |
|---|---:|---:|---:|---:|---:|---|
| \(5+\) | 384 | 4 | 2 | 2 | 2 | \(\mathbb Z/10\mathbb Z\) |
| \(1+\), \(4+\) | 240 | 6 | 4 | 3 | 3 | \(\mathbb Z/2\mathbb Z\) |
| \(1-\), \(4-\) | 240 | 2 | 2 | 1 | 1 | trivial |
| \(2+\), \(3+\) | 160 | 6 | 4 | 3 | 3 | \(\mathbb Z/2\mathbb Z\) |
| \(2-\), \(3-\) | 160 | 2 | 2 | 1 | 1 | trivial |
| \(1+\), \(1+\), \(3+\) | 80 | 8 | 6 | 4 | 4 | \(\mathbb Z/2\mathbb Z\) |
| \(1+\), \(1-\), \(3-\) | 160 | 4 | 4 | 2 | 2 | trivial |
| \(1+\), \(2+\), \(2+\) | 60 | 10 | 6 | 4 | 6 | \(\mathbb Z/2\mathbb Z\) |
| \(1+\), \(2-\), \(2-\) | 60 | 4 | 4 | 2 | 2 | trivial |
| \(1-\), \(1-\), \(3+\) | 80 | 4 | 4 | 2 | 2 | trivial |
| \(1-\), \(2+\), \(2-\) | 120 | 4 | 4 | 2 | 2 | trivial |
| \(1+\), \(1+\), \(1+\), \(2+\) | 20 | 12 | 8 | 5 | 7 | \(\mathbb Z/2\mathbb Z\) |
| \(1+\), \(1+\), \(1-\), \(2-\) | 60 | 4 | 6 | 3 | 1 | trivial |
| \(1+\), \(1-\), \(1-\), \(2+\) | 60 | 8 | 6 | 3 | 5 | trivial |
| \(1-\), \(1-\), \(1-\), \(2-\) | 20 | 4 | 4 | 1 | 3 | trivial |
| \(1+\), \(1+\), \(1+\), \(1+\), \(1+\) | 1 | 16 | 10 | 6 | 10 | \(\mathbb Z/2\mathbb Z\) |
| \(1+\), \(1+\), \(1+\), \(1-\), \(1-\) | 10 | 8 | 8 | 4 | 4 | trivial |
| \(1+\), \(1-\), \(1-\), \(1-\), \(1-\) | 5 | 8 | 6 | 2 | 6 | trivial |

In particular, **eleven** types have torsion-free cokernel, **six** have a single two-torsion factor, and the ordinary positive five-cycle has
\[
\boxed{\operatorname{coker}(\Phi^F)\cong\mathbb Z^2\oplus\mathbb Z/10\mathbb Z.}
\]
The geometric, non-invariant map has Smith diagonal \(\operatorname{diag}(1,1,1,1,1,2)\), so the five-primary torsion is a genuinely arithmetic orbit-sum effect, not torsion in its geometric cokernel.

## Assumptions and scope
A degree-four del Pezzo surface is a smooth projective surface over a field with ample anticanonical divisor of square four. Over an algebraic closure it is the blow-up of \(\mathbb P^2\) at five points in general position. Choose formal labels \(H,E_0,\dots,E_4\) for its Picard group, where \(H^2=1\), \(E_i^2=-1\), and the remaining intersections vanish. The sixteen \((-1)\)-classes are
\[
E_i,\qquad L_{ij}=H-E_i-E_j\ (0\le i<j\le4),\qquad Q=2H-\sum_{i=0}^4 E_i.
\]
The ten conic classes, each of anticanonical degree two and self-intersection zero, are
\[
F_i=H-E_i,\qquad G_i=2H-\sum_{j\ne i}E_j\qquad(0\le i\le4).
\]
The five natural complementary pairs satisfy \(F_i+G_i=-K_S\). Each is base-point-free and defines a geometric conic fibration. The map is on **formal free abelian groups on geometric labels**. In particular, its cokernel is *not* the Picard group, the divisor class group, an arithmetic Brauer group, or the group of rational conic fibrations. An invariant orbit-sum basis element may involve pencils that are not separately rational. The theorem is conditional on the actual Frobenius class; it does not assert that every Weyl type occurs over every finite field.

Represent a signed cycle by its length and the product of its signs, writing \(1+\), \(2-\), etc.; commas combine disjoint cycles. Only sign assignments with total product \(+1\) occur. The list in the table is exactly the eighteen conjugacy classes of \(W(D_5)\cong(\mathbb Z/2)^4\rtimes S_5\), with class sizes totaling 1920.

## Proof
**1. Geometric components and the unsigned incidence matrix.** The pencil \(F_i\) has exactly the four reducible fibers \(E_j+L_{ij}\) for \(j\ne i\). The pencil \(G_i\) has the reducible fiber \(E_i+Q\), together with the three fibers \(L_{jk}+L_{lm}\) as \(\{j,k\}\sqcup\{l,m\}=\{0,1,2,3,4\}\setminus\{i\}\). Thus each pencil supports eight different exceptional curves. Define the \(16\times10\) binary matrix \(B\) with entry one exactly when the line occurs in that pencil. Every row has five ones, every column has eight ones, and a line is supported by exactly one pencil in each pair \(\{F_i,G_i\}\). Consequently the line rows are identified with the sixteen odd-sign words in \(\{+1,-1\}^5\), the pencil columns with five coordinate/sign pairs, and \(B\) is the universal half-cube/coordinate incidence matrix. Direct elementary integer elimination yields Smith diagonal \(1,1,1,1,1,2\) (with four zero columns or ten? Here the map has rank six, so it has four additional zero Smith positions among its ten domain columns). The supplied verifier constructs \(B\) from the displayed Picard classes and verifies this diagonal exactly.

**2. Frobenius actions.** The geometric Weyl action on the line rows is the even-signed permutation action on the sixteen odd-sign words, and on the pencil columns it permutes the five coordinate/sign pairs. Since \(B\) is invariant, for each \(F\in W(D_5)\) it descends to the matrix \(T_F\) in orbit-sum bases of the two fixed integer permutation modules. More explicitly, if \(O\) is a line orbit and \(P\) a pencil orbit, its integer entry is the number of pencils in \(P\) supporting a *fixed* line in \(O\). Equivariance makes the number independent of the chosen line. This is the actual matrix of \(\Phi^F\), rather than a rationally averaged or divided matrix.

**3. Exhaustive finite classification.** Every Weyl element is encoded uniquely by a permutation \(\pi\in S_5\) and a sign vector \((\epsilon_0,\ldots,\epsilon_4)\in\{\pm1\}^5\) with product \(+1\), so there are exactly \(120\cdot16=1920\) elements. The accompanying standalone `verify.py` exhausts these 1920 elements. For each, it constructs the two explicit finite orbits, forms the integer orbit-sum matrix, computes its exact Smith diagonal using unimodular Euclidean row/column operations and a divisibility check, and verifies its rank, free cokernel rank and nontrivial invariant factors against the full eighteen-row `cases.csv` table. It also checks by explicit conjugation that each signed-cycle label defines a single entire conjugacy class, and that the classes partition all 1920 elements. Because all possible integral Weyl actions have been covered and the geometric setup determines the matrix, the finite calculation is exhaustive for all arithmetic types.

**4. A direct five-primary witness.** For the positive five-cycle on the five blow-up labels, the sixteen line orbits are \(\{Q\}\), \(\{E_i\}\) and the two five-element orbits \(\{L_{i,i+1}\}\), \(\{L_{i,i+2}\}\), with subscripts modulo five. The ten conic classes have orbits \(\{F_i\}\) and \(\{G_i\}\). In these orbit-sum bases, the map is exactly
\[
T=\begin{pmatrix}0&5\\4&1\\2&3\\2&3\end{pmatrix}.
\]
The gcd of its entries is one, and the gcd of its six \(2\times2\) minors is ten; its rank is two. Hence the two nonzero Smith factors are \(1,10\), so \(\operatorname{coker}(T)=\mathbb Z^2\oplus\mathbb Z/10\mathbb Z\). The five-part therefore cannot be inferred from the geometric Smith diagonal, which has only two-primary torsion.

## Verification
The package contains `verify.py` and `cases.csv`. From a directory containing both, execute `python3 verify.py`; Python 3 standard library is the only dependency. It reconstructs the sixteen line classes, ten pencils, all component incidences, and all 1920 even-signed Weyl elements; tests all conjugacy classes and every invariant integral Smith diagonal; and verifies the direct five-cycle matrix and the geometric Smith diagonal. It prints four `PASS` lines if all assertions hold. A separate cross-check using SymPy's independent `smith_normal_form` on one representative of each of the eighteen signed-cycle types agreed with the bundled exact Smith algorithm. The supplied data are a complete finite certificate for the Weyl enumeration, not a sampling of finite-field surfaces.

## Relationship to prior work
Luc Pirio's 2024 preprint (later published in 2025) develops the ten conic fibrations, sixteen exceptional lines, Weyl action and their rational representations. The geometric support construction is built from those classical data; neither the conic fibrations nor the \(D_5\) action is claimed as new. Sections 2.3.2--2.3.3 give the line and conic classes and representation information. The inspected paper does not calculate arithmetic Frobenius-invariant integer orbit-sum cokernels and has no Smith or Frobenius analysis. Banwait--Fité--Loughran and Trepalin classify finite-field Frobenius information for del Pezzo surfaces, but the inspected finite-field paper addresses arithmetic Picard traces, not the present map between free label lattices.

The closest published comparison for the *same* surface type is an integral trace-lattice calculation using the map from the sixteen exceptional lines into the Frobenius-fixed **Picard group**; its indices \(1,2,4,16\) are not the cokernels of the present ten-pencil-to-sixteen-formal-line incidence map. Another published five-cycle calculation identifies an induced torus as the connected Picard scheme of the reduced sixteen-line boundary; its invariant is the dual-graph cycle lattice, not the conic-support map. A degree-five del Pezzo integral trace-lattice classification concerns a different geometric configuration. These implications and matrix domains differ; none determines the complete eighteen-row classification here. Search failure does not establish global priority.

## Limitations
The classification is conditional on a surface's actual \(W(D_5)\) Frobenius class and does not classify which classes are realized over each finite field. The module is purely combinatorial/geometric with arithmetic Galois action and must not be identified with actual integral line divisors, the Brauer group, or Picard torsion. The finite verifier proves the exact Smith statements only after using the standard geometric list of exceptional curves, pencils and Weyl actions. Reproduction requires executing its checker, not merely reading a static output table. A preexisting equivalent tabulation in specialized integral design, signed-permutation or finite-geometry literature remains a residual originality risk. No independent mathematical audit has been performed.

## References
1. Luc Pirio, *On the 10-web by conics on the quartic del Pezzo surface*, arXiv:2401.06711v1, first public 2024-01-12, especially Section 2.3.2 and Table 2; published 2025 in *Annales de la Faculté des sciences de Toulouse*. https://arxiv.org/abs/2401.06711
2. Barinder Banwait, Francesc Fité, Daniel Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, arXiv:1606.00300v1, first public 2016-06-01, especially Section 3. https://arxiv.org/abs/1606.00300
3. Andrey Trepalin, *Del Pezzo surfaces over finite fields*, arXiv:1803.07421v1, first public 2018-03-17. https://arxiv.org/abs/1803.07421
4. *Integral Frobenius trace lattices and arithmetic cones of degree-five del Pezzo surfaces*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-integral-frobenius-trace-lattices-and-arithmetic-cones-of-degree--14de99fa5b64
5. *Five induced quintic tori for the sixteen-line boundary of a quartic del Pezzo surface*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-five-induced-quintic-tori-for-the-sixteen-line-boundary-of-a-qua--5411549db544
