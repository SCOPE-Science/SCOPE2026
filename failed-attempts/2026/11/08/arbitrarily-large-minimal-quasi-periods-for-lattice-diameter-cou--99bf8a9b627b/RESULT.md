# Arbitrarily large minimal quasi-periods for lattice-diameter counts of primitive parallelograms

## Finding
For each integer \(q\ge2\), define the lattice parallelogram
\[
P_q=\operatorname{conv}\{(0,0),(1,q),(q+2,1),(q+3,q+1)\}.
\]
Its four sides are primitive lattice segments. For every positive integer \(k\), write \(k=aq+r\), where \(a\ge0\) and \(0\le r<q\). The lattice diameter of \(kP_q\), defined as one less than the largest number of collinear integer points, is
\[
D_q(k)=(q+2)k-\left\lceil\frac{k}{q}\right\rceil.
\]
Every lattice diameter segment is horizontal. The exact number \(N_q(k)\) of lattice diameter **segments** (equivalently, of lattice diameter lines) is
\[
N_q(k)=
\begin{cases}
(q-1)a+1,&r=0,\\
(q-1)k+1-(r-1)(k-a-1),&1\le r<q.
\end{cases}
\]
Thus \(N_q\) is quasi-linear for every \(k\ge1\), with **minimal eventual quasi-period exactly \(q\)**. Its residue-class linear coefficients are
\[
\gamma_0=\frac{q-1}{q},\qquad
\gamma_r=\frac{(q-1)(q-r+1)}q\quad(1\le r<q).
\]
These \(q\) coefficients are pairwise distinct; their largest-to-smallest ratio is \(q\). Consequently, even among four-vertex centrally symmetric lattice polygons with primitive edges, the least quasi-period is unbounded and the leading coefficients of maximal-lattice-line counts can fluctuate by an unbounded factor. With binary vertex encoding, an explicit table listing all period constituents has exponentially many entries in the bit-length of the input, although the compact formula above has only logarithmic-size parameters.

## Assumptions and scope
The ambient lattice is \(\mathbb Z^2\); integer dilations are about the origin. For any nonzero primitive integer direction \(u\), a segment joining integer points \(x,y\) with \(y-x=mu\) contains exactly \(m+1\) integer points. A *lattice diameter segment* attains the largest possible \(m\) among pairs in the polygon. Different endpoints give different segments; there is one such segment on each lattice diameter line because the segment is maximal on that line. The term *minimal eventual quasi-period* means the least positive period of any quasi-polynomial agreeing with the counting function for all sufficiently large integer dilation factors. The assertion applies to the particular explicit family \(P_q\), not to every parallelogram. The bit-complexity consequence concerns tabular representations listing one polynomial for each residue class; it is not a lower bound for compressed formulas or general algorithms.

## Proof
**1. Horizontal sections and the diameter.** Put \(L=q+2\). Each point of \(kP_q\) has a unique expression
\[
(x,y)=s(1,q)+t(L,1),\quad 0\le s,t\le k.
\]
For a fixed real height \(y\), eliminating \(s\) gives
\[
x=\frac yq+\left(L-\frac1q\right)t,
\quad \max(0,y-qk)\le t\le\min(k,y).
\]
The continuous horizontal width is therefore at most \(W=k(L-1/q)\), with equality precisely when \(k\le y\le qk\). Since the endpoints at height \(y=k\) have abscissas \(k/q\) and \(kL\), this section contains two integers differing by \(kL-\lceil k/q\rceil=\lfloor W\rfloor\). No horizontal integer segment can have more unit steps. Hence the maximal horizontal lattice length is
\[
D=\left\lfloor k\left(L-\frac1q\right)\right\rfloor
=kL-\left\lceil\frac{k}{q}\right\rceil.
\]
In particular, \(D\ge k(q+1)\), because \(\lceil k/q\rceil\le k\).

**2. No nonhorizontal direction is competitive.** A pair of integer endpoints at lattice distance \(m\) in primitive direction \(u=(u_1,u_2)\), with \(u_2\ne0\), has vertical displacement at least \(m\). The full vertical extent of \(kP_q\) is \(k(q+1)\). Therefore \(m\le k(q+1)\le D\). If equality \(m=D\) held, then necessarily \(D=k(q+1)\), \(|u_2|=1\), and the two endpoints would be the unique bottom and top vertices \((0,0)\) and \((k(q+3),k(q+1))\). These would require \(u_1=(q+3)/(q+1)\) to be integral, which is impossible for \(q\ge2\) because \(q+1\) does not divide \(2\). Thus all diameter segments are horizontal.

**3. Only the middle strip can contain a diameter segment.** At integer heights \(y<k\) or \(y>qk\), the continuous horizontal width is at least \(L-1/q>1\) less than \(W\). It is therefore strictly less than \(D=\lfloor W\rfloor\). Every diameter line has integer height \(k\le y\le qk\). Within this strip its horizontal interval is
\[
\left[\frac yq,\ kL+\frac{y-k}{q}\right],
\]
and the largest integer horizontal distance available on that line is
\[
H(y)=kL+\left\lfloor\frac{y-k}{q}\right\rfloor
-\left\lceil\frac yq\right\rceil.
\]
Write \(k=aq+r\), \(0\le r<q\), and \(y=bq+j\), \(0\le j<q\). The elementary floor and ceiling identities give
\[
H(y)=kL-a-\mathbf 1_{j>0}-\mathbf 1_{j<r}.
\]
If \(r=0\), this equals the global diameter precisely for \(j=0\). There are exactly \((q-1)a+1\) such heights between \(k\) and \(qk\). If \(1\le r<q\), the diameter equals \(kL-a-1\), and the only excluded middle-strip residues are \(j=1,\ldots,r-1\). The middle strip has \((q-1)k+1\) integer heights. For each excluded residue there are exactly \(k-a-1\) heights. Subtracting proves the formula for \(N_q(k)\). Every qualifying horizontal line has a unique pair of extremal integer endpoints at lattice distance \(D\), so line and segment counts coincide.

**4. Sharp quasi-period and size consequence.** Substituting \(a=(k-r)/q\) into the exact formulas shows that the constituent slopes are precisely \(\gamma_0,\ldots,\gamma_{q-1}\) displayed above. These slopes are pairwise distinct. If a quasi-polynomial with eventual period \(p\) represented \(N_q\), each residue class modulo \(p\) would have one eventual linear coefficient (higher degrees are impossible since \(N_q(k)=O(k)\)). If \(q\nmid p\), that residue class would contain infinitely many integers from at least two different residue classes modulo \(q\), which have different linear coefficients; contradiction. Thus every eventual period is a multiple of \(q\). The displayed formula already has period \(q\), proving minimality.

Finally, the polygon coordinates are bounded by \(q+3\), and there are only four vertices, so its binary description has \(O(\log q)\) bits. Any tabulation using one constituent polynomial for each class of a valid eventual period must list at least \(q\) entries. This exponential separation does not preclude concise modular or floor-function descriptions, such as the formula in this theorem.

## Verification
The supplied standalone script `verify_diameter_period.py` performs exact integer membership and exhaustive pair enumeration for every \(2\le q\le6\) and \(1\le k\le5\), comparing the resulting lattice diameter, number of diameter segments, and primitive directions against the theorem. In 25 full enumerations all matched, and the unique primitive diameter direction was \((1,0)\). A separate integer-arithmetic section computation checked the exact count for all \(2\le q\le30\) and \(1\le k\le45\), giving 1,305 further matches. No floating-point calculations enter these tests. The general assertion follows from the proof, not from the bounded tests.

For \(q=3\), the polygon is exactly the parallelogram with vertices \((0,0),(1,3),(5,1),(6,4)\) whose period-three example was previously published. The new result is the **all-period sharp minimality**, the explicit full family, and the unbounded multiplicative oscillation/representation consequence, not that individual example.

## Relationship to prior work
Averkov, Brose, De Loera, Lopez-Campos and Torres (arXiv:2508.20009, first posted 2025-08-27, Section 4 of the 2026 revision) proved eventual quasi-polynomial counting of lattice diameter lines for arbitrary lattice polytopes and exhibited the \(q=3\) parallelogram. Their earlier version develops a general block argument giving a period **dividing** a denominator associated with a direction; that existence statement neither proves sharpness of all positive periods nor supplies the unbounded primitive-parallelogram family or its tabular representation lower bound. The case \(q=3\) here is intentionally attributed to them; it is not claimed as new.

Soprunov and Soprunova (arXiv:1412.4404) proved eventual quasi-linearity of the **Minkowski length** of lattice polytopes and recalled that its first value is lattice diameter; they do not enumerate the number of diameter *lines*. A separate search of relevant publicly indexed mathematical research records for lattice diameter segments, arbitrary periods, and primitive parallelograms found no result directly implying the full period-realization statement. These are best-knowledge originality comparisons, not a guarantee of absolute historical priority.

## Limitations
The construction gives one family and establishes no universal optimal bounds on quasi-periods for an arbitrary polygon. Its exponential tabular-size consequence is representation-specific: the displayed modular formula is compact. Prior literature proves a general quasi-polynomial theorem and contains the \(q=3\) base example, so the all-\(q\) extension may be viewed as a short sharpening; potential earlier implicit parameterizations remain a priority risk. There is no independent mathematical audit or claim of external certification.

## References
1. G. Averkov, A. E. Brose, J. A. De Loera, G. Lopez-Campos, A. J. Torres, *On Lattice Diameter Segments: Algorithms and Structure*, arXiv:2508.20009, first public 2025-08-27; revised 2026-10-03. https://arxiv.org/abs/2508.20009 ; https://arxiv.org/html/2508.20009 .
2. I. Soprunov, J. Soprunova, *Eventual Quasi-linearity of the Minkowski length*, arXiv:1412.4404, first public 2014-12-14. https://arxiv.org/abs/1412.4404 .
