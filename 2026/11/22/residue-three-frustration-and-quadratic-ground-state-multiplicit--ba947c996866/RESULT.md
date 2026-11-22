# Residue-three frustration and quadratic ground-state multiplicities on three-colour Potts antiprisms

## Finding

For the equal-coupling, zero-field, three-colour Potts antiferromagnet on every \(n\)-antiprism, \(n\ge3\), define \(N=2n\), write \(N=3m+r\), \(r\in\{0,1,2\}\), and let \(G_N(y)\) count **all labelled minimum-energy colourings** by the number of occurrences of a fixed one of the three named colours. Then the complete answer is

\[
\begin{aligned}
 r=0:\quad& B_{\min}=0, &G_N(y)&=6y^m,\\
 r=1:\quad& B_{\min}=1, &G_N(y)&=2Ny^m(2+y),\\
 r=2:\quad& B_{\min}=2, &G_N(y)&=Ny^m\bigl((9m-3)+(10m+2)y+(2m-2)y^2\bigr).
\end{aligned}
\]

Here \(B_{\min}\) is the minimum number of monochromatic edges, so the exact minimum Hamiltonian energy is \(JB_{\min}\). Summing coefficients yields total ground-state multiplicity \(6\), \(6N\), or \(N(7N-17)\) according to the three congruence classes. In particular, an arithmetically forced one- or two-defect sector has respectively linear or quadratic finite-size degeneracy even though its minimum energy is bounded. The residual entropy density is zero in all three classes.

## Assumptions and scope

Fix an integer \(n\ge3\) and put \(N=2n\). The labelled vertex set is \(\mathbb Z/N\mathbb Z\) with an undirected edge between each \(i\) and \(i+1\), and each \(i\) and \(i+2\), indices modulo \(N\). Because \(N\ge6\), these are exactly \(2N\) distinct edges and the graph is the \(n\)-antiprism. Each vertex takes a named spin colour \(c_i\in\{0,1,2\}\). With uniform antiferromagnetic exchange \(J>0\), no field, and no other interactions, define

\[
H(c)=JB(c),\quad B(c)=\sum_{i=0}^{N-1}\bigl(\mathbf1_{c_i=c_{i+1}}+\mathbf1_{c_i=c_{i+2}}\bigr),\quad K(c)=\sum_i\mathbf1_{c_i=0}.
\]

All colour assignments are distinguishable by the labelled sites and three named colours. Define \(G_N(y)=\sum_{c:B(c)=B_{\min}}y^{K(c)}\). The statement concerns strictly zero field; \(y\) is a bookkeeping marker, not an applied magnetic fugacity.

## Proof

**Exact finite-range transfer.** Index a nine-dimensional transfer by the ordered pairs \((a,b)\in\{0,1,2\}^2\). There is a transition \((a,b)\to(b,c)\) of weight

\[
T_{(a,b),(b,c)}(x,y)=x^{\mathbf1_{a=c}+\mathbf1_{b=c}}y^{\mathbf1_{c=0}},
\]

and all other matrix entries are zero. Closing a length-\(N\) walk in the pair-state space accounts for every consecutive and next-nearest-neighbour edge exactly once, including the cyclic closure. Each vertex contributes its colour marker exactly once. Hence, as a polynomial identity for every \(N\ge6\),

\[
Z_N(x,y)=\sum_{c\in\{0,1,2\}^{N}}x^{B(c)}y^{K(c)}=\operatorname{tr}\bigl(T(x,y)^N\bigr).
\]

This identity supplies all defect counts, not just a numerical recurrence. Write \(D(t,x,y)=\det(I-tT(x,y))=D_0+xD_1+x^2D_2+O(x^3)\), and \(q=t^3y\). Direct symbolic elimination of this explicitly specified nine-by-nine matrix gives

\[
D_0=(1-q)^2,\qquad D_1=-2t^4y(y+2)(1-q).
\]

The portion of \(D_2\) containing powers \(t^k\) with \(k\equiv2\pmod3\) is

\[
D_{2,[2]}=t^2(2y+1)(-1-4q+4q^2).
\]

These three *finite polynomial identities* are reproduced by the enclosed exact symbolic checker, which constructs the entries of \(T\) directly and verifies each equality by full polynomial subtraction, without interpolation or an asymptotic assumption. The formal power-series identity

\[
\sum_{N\ge1} Z_N(x,y)t^N=-t\partial_t\log D(t,x,y)
\]

follows from \(\log\det(I-tT)=-\sum_{N\ge1}\operatorname{tr}(T^N)t^N/N\). Thus the coefficients of the **smallest available powers of** \(x\) in each length class can be recovered exactly from the displayed determinant coefficients.

At defect order zero, \([x^0]\log D=2\log(1-q)\), and therefore \([x^0]Z_N\) equals \(6y^{N/3}\) if \(3\mid N\), and zero otherwise. At defect order one,

\[
[x^1]\log D=-\frac{2t^4y(y+2)}{1-q},
\]

so \([x^1]Z_N=2Ny^{(N-1)/3}(2+y)\) for \(N\equiv1\pmod3\), and zero for \(N\equiv2\pmod3\).

Finally, the \(t\)-exponent-congruence-two contribution to \([x^2]\log D=D_2/D_0-\tfrac12(D_1/D_0)^2\) is exactly

\[
 t^2\frac{-(2y+1)-4(2y+1)q-(2y^2+4)q^2}{(1-q)^2}.
\]

Use \((1-q)^{-2}=\sum_{j\ge0}(j+1)q^j\). For \(N=3m+2\) with \(N\ge6\), necessarily \(m\ge2\), and the coefficient at \(t^N\) in the preceding expression is

\[
-y^m\bigl((9m-3)+(10m+2)y+(2m-2)y^2\bigr).
\]

Multiplying by \(-N\) as required by the logarithmic-derivative identity gives the third formula. Each exhibited lowest-defect coefficient is strictly positive for the allowed lengths, and every lower order has been shown to vanish in that length class. These are therefore exactly the minimum-energy sectors, with all multiplicities included. Setting \(y=1\) gives \(6,6N,N(21m-3)=N(7N-17)\), completing the proof.

## Verification

Run `python verify.py` with Python 3 and SymPy. The checker forms the entire nine-by-nine matrix from the colour rule, evaluates its determinant symbolically, and certifies the three needed polynomial identities. It also independently compares the answer with exact min-plus enumeration for \(6\le N\le34\), direct exhaustive enumeration of all \(3^N\) colourings for \(6\le N\le10\), and direct transfer traces for \(6\le N\le9\). These finite comparisons are supplementary; the generating-function argument proves every allowed length.

## Relationship to prior work

Salas and Sokal established transfer-matrix machinery for Potts antiferromagnets and analysed chromatic polynomials of square-lattice strips. The antiprism's graph-square realization and chromatic polynomial are established. Lopez-Bonilla, Allagan and Morgan studied antiprism chromatic-root loci through a zero-temperature proper-colouring transfer. Proper-colouring counts recover the defect-zero component but do not determine the one- and two-monochromatic-edge ground-state occupancy distributions required for the other two congruence classes. The distinction between fixed-colour marking and an unmarked chromatic polynomial is also essential. No claim of novelty is made for the general transfer-matrix identity or the proper-colouring formula.

## Limitations

The theorem assumes three named colours, a homogeneous positive nearest- and next-nearest-edge penalty, a periodic even cycle of at least six sites, and **zero field**. It does not compute the full positive-field ground-state envelope, finite-temperature thermodynamics, or a bulk phase transition. Priority has been compared with accessible published results, but an earlier unindexed equivalent finite-range Potts calculation cannot be conclusively excluded without independent bibliographic review. The exact checks are reproducible but do not constitute independent scientific validation.

## References

1. J. Salas and A. D. Sokal, *Transfer Matrices and Partition-Function Zeros for Antiferromagnetic Potts Models I. General Theory and Square-Lattice Chromatic Polynomial*, first public 19 April 2000, https://arxiv.org/abs/cond-mat/0004330 .
2. R. Lopez-Bonilla, J. D. Allagan and G. C. Morgan, *Quartic Equimodular Curves and Spectral Reductions in Prism-Derived Chromatic Polynomials*, *Symmetry* **18** (2026), 1180, https://doi.org/10.3390/sym18071180 .
3. E. W. Weisstein, *Antiprism Graph*, MathWorld, https://mathworld.wolfram.com/AntiprismGraph.html .
