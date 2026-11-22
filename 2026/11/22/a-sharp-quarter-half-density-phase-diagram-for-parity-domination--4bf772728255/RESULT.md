# A sharp quarter–half density phase diagram for parity domination on Cartesian tori

## Finding
For every pair of integers \(m,n\geq3\), let \(G=C_m\square C_n\). Call \(D\subseteq V(G)\) *odd open dominating* if every vertex has an odd number of neighbors in \(D\). Then such a set exists exactly when \(4\mid m\) or \(4\mid n\). When exactly one circumference is divisible by four, **every** odd open dominating set has exactly \(mn/2\) vertices. When both are divisible by four, the minimum cardinality is exactly \(mn/4\), attained by a periodic perfect open dominating set. In the other cases the minimum is undefined because there is no feasible set.

More strongly, if \(4\nmid m\), write \(m=2^\varepsilon a\), where \(\varepsilon\in\{0,1\}\) and \(a\) is odd. The indicator of **every** odd open dominating set obeys
\[
 x(i,j+2a)=1+x(i,j)\pmod2
\]
for all \((i,j)\in\mathbb Z_m\times\mathbb Z_n\). There is a symmetric statement interchanging the two coordinates. This forced antiperiodicity is the structural reason for both the impossibility and half-density regimes.

## Assumptions and scope
All cycles have at least three vertices, and Cartesian adjacency means \((i,j)\) is adjacent to \((i\pm1,j)\) and \((i,j\pm1)\), with cyclic indices; these are four **distinct** neighbors for \(m,n\geq3\). Vertex indicators are elements of the vector space of functions \(\mathbb Z_m\times\mathbb Z_n\to\mathbb F_2\); their integer support size, rather than their field sum, is the objective. For a fixed graph, \(\gamma_{\mathrm{oo}}(G)\) denotes the minimum size of a set with odd open-neighbor counts, when one exists. No assertion is made about the number of such sets or their reconfiguration graph.

## Proof
Write \(S\) and \(T\) for coordinate translation operators on this binary function space. They commute, are invertible, and satisfy \(S^m=T^n=I\). Set
\[
 B=S+S^{-1},\qquad C=T+T^{-1},\qquad A=B+C.
\]
The condition is \(Ax=\mathbf1\), where \(\mathbf1\) is the constant-one function. Since every vertex has four neighbors, \(A\mathbf1=0\), and consequently \(A^2x=0\) for every feasible \(x\).

Define polynomials over \(\mathbb F_2\) by \(P_0(z)=0\), \(P_1(z)=z\), and \(P_{k+1}(z)=zP_k(z)+P_{k-1}(z)\). Induction gives \(P_k(U+U^{-1})=U^k+U^{-k}\) for invertible \(U\), and \(P_k'(0)=1\) for odd \(k\) (the linear coefficient alternates between one at odd indices and zero at even indices). Suppose \(4\nmid m\), and write \(m=2^\varepsilon a\) with odd \(a\) and \(\varepsilon\in\{0,1\}\). Since \(m\mid 2a\), we have \(S^a=S^{-a}\), whence \(P_a(B)=0\) as an operator.

Because \(B=C+A\), the operators \(C,A\) commute. For any polynomial \(Q\) and any \(x\) satisfying \(A^2x=0\), the binomial expansion yields \(Q(C+A)x=Q(C)x+Q'(C)Ax\). Thus for feasible \(x\),
\[
 0=P_a(B)x=P_a(C)x+P_a'(C)\mathbf1=P_a(C)x+\mathbf1,
\]
where the last equality follows from \(C\mathbf1=0\) and \(P_a'(0)=1\). Using the shift identity again gives \((T^a+T^{-a})x=\mathbf1\), and multiplying by \(T^a\) gives
\[
 (I+T^{2a})x=\mathbf1.
\]
Therefore \(T^{2a}x=x+\mathbf1\): every feasible pattern changes to its pointwise complement after translation by \(2a\) in the second coordinate.

If also \(4\nmid n\), then \(n\) has 2-adic valuation at most one and \(2a\) has valuation exactly one. The order \(n/\gcd(n,2a)\) of this translation on \(\mathbb Z_n\) is odd. Iterating an odd number of complementation steps would make \(x=x+\mathbf1\), an impossibility. Therefore no feasible set exists when neither dimension is divisible by four.

If \(4\mid n\) and \(4\nmid m\), complementing by \(T^{2a}\) is a bijection between selected and unselected vertices. Hence every feasible set has cardinality \(mn/2\). The same holds after exchanging coordinates when \(4\mid m\) and \(4\nmid n\). Feasibility in these cases is witnessed, for \(4\mid n\), by a set depending only on column \(j\), with indicator period four \((0,0,1,1)\): its two horizontal neighbors have equal membership and its two vertical neighbors have opposite membership, so each vertex sees an odd number of selected neighbors.

Finally suppose \(4\mid m,n\). Counting incidences between \(D\) and all vertices gives \(4|D|=\sum_{v\in V(G)}|N(v)\cap D|\geq mn\); hence \(|D|\geq mn/4\). Choose the four residue classes \((0,0),(0,1),(2,2),(2,3)\) modulo four. Every residue class has **exactly one** neighboring selected residue class; periodic extension across the two circumferences is therefore perfect open domination and has exactly \(mn/4\) vertices. This proves every asserted bound and boundary case.

## Verification
`verify_linear.py` independently constructs the four-neighbor binary adjacency equations and uses exact Gaussian elimination for each of the 196 parameter pairs \(3\leq m,n\leq16\); it tests solvability, all homogeneous basis vectors, forced antiperiodicity in the half-density regime, and the periodic quarter-density witness. The results are 100 infeasible pairs, 80 mixed cases, and 16 two-fourfold cases, as predicted. `verify_bruteforce.cpp` independently exhausts every binary subset by Gray-code syndrome updates for the eight parameter pairs \((3,3),(3,4),(3,5),(4,4),(4,5),(4,6),(5,4),(6,4)\), confirming the true minimum and number of minimizers in each case. Run these scripts directly as described in `VERIFICATION.md`. These finite tests corroborate but are not the proof of the unbounded assertion; the preceding algebraic and counting arguments establish all parameter values.

## Relationship to prior work
Goldwasser and Klostermeyer (2007) define odd open domination and use Fibonacci-polynomial and linear-algebraic methods to study finite rectangular **path-grid** graphs \(P_m\square P_n\). This is not a toroidal periodic-boundary classification. Yamagishi (2015) studies spaces of homogeneous periodic harmonic functions over fields, including the nullity of \(A(C_m\square C_n)\) in characteristic two using Chebyshev polynomials. The binary all-ones affine equation \(Ax=\mathbf1\), its solution support minimum, and the universal forced translation-complement rule are different assertions; homogeneous nullity alone does not imply the claims here. The polynomial shift identity is classical and is not presented as new.

## Limitations
The theorem is specific to four-neighbor Cartesian products of **simple** cycles of order at least three. It does not enumerate all feasible sets or their weight distribution, except for the rigid half-density case. Although the cited full texts and indexed mathematical records were compared, an unindexed or differently formulated historical result could cover some or all of the stated claims. No independent scholarly review has occurred.

## References
1. J. L. Goldwasser and W. F. Klostermeyer, *Odd and Even Dominating Sets with Open Neighborhoods*, **Ars Combinatoria** 83 (2007), 229–247, first public date reported April 30, 2007. https://combinatorialpress.com/ars-articles/volume-083-ars-articles/odd-and-even-dominating-sets-with-open-neighborhoods/
2. M. Yamagishi, *Periodic harmonic functions on lattices and Chebyshev polynomials*, **Linear Algebra and its Applications** 476 (2015), 1–15. https://doi.org/10.1016/j.laa.2015.03.004
