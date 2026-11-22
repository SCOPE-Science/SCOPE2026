# The characteristic-two Pascal-line fiber formula and complete rational-line coverage

## Finding

Let \(q=2^m\) with \(m\ge3\), and let \(K\subset\mathbb P^2_{\mathbb F_q}\) be a smooth conic. From every six-element subset of \(K(\mathbb F_q)\), form all sixty unoriented cyclic hexagons, with arrangements identified under rotation and reversal. Assign to each arrangement its Pascal line, retaining multiplicity when different hexagons yield the same line. Put
\[
\rho_q=\#\{u\in\mathbb F_q:u^2+u+1=0\}
=\begin{cases}0,&m\text{ odd},\\2,&m\text{ even}.\end{cases}
\]

**Theorem.** Every rational line has a strictly positive number of Pascal preimages. That number depends only on whether the line is tangent to, secant to, or exterior to \(K\), and is respectively
\[
\begin{aligned}
T_q&=\frac{q(q-1)(q-2)(q-4)}{12},\\
S_q&=\frac{(q-1)\bigl((q-2)(q-5)(q-6)-2\rho_q\bigr)}{12},\\
E_q&=\frac{(q+1)\bigl((q-2)(q^2-5q+2)+2\rho_q\bigr)}{12}.
\end{aligned}
\]

In particular, \(q=8\) is the smallest even prime power with at least six conic points, and already every one of its 73 rational projective lines occurs. The per-line multiplicities at \(q=8\) are \((T_8,S_8,E_8)=(112,21,117)\); at \(q=16\) they are \((3360,1920,3536)\).

## Assumptions and scope

A conic is smooth and geometrically integral. Over a finite field such a conic is projectively equivalent to \(XZ=Y^2\) and has \(q+1\) rational points. For a six-tuple of distinct points \((A,B,C,D,E,F)\) in cyclic order, the Pascal line is the line through \(AB\cap DE\) and \(BC\cap EF\), equivalently through \(CD\cap FA\). These two defining intersections are distinct: otherwise their common point would be \(B\), which cannot belong to \(DE\) or \(EF\) since all six conic points are distinct. No generic-position or pairwise-distinct-Pascal-line assumption is imposed; repeated output lines are counted with multiplicity.

Because the base field is perfect and characteristic two, every rational projective line is tangent (one geometric intersection with multiplicity two), secant (two rational conic intersections), or exterior (its two conic intersections are conjugate over \(\mathbb F_{q^2}\)). The respective numbers of such lines are \(q+1\), \(q(q+1)/2\), and \(q(q-1)/2\). The projective conic automorphism group \(\operatorname{PGL}_2(\mathbb F_q)\) is transitive on each class.

## Proof

Identify the conic with \(P_t=[1:t:t^2]\) for \(t\in\mathbb F_q\), and \(P_\infty=[0:0:1]\). The automorphism group is sharply triply transitive on ordered triples of distinct conic points, and has cardinality \(q(q^2-1)\). Normalize the first three vertices of an ordered hexagon to \((a,b,c)=(\infty,0,1)\); write the remaining vertices \((d,e,f)\) as pairwise distinct elements of \(U=\mathbb F_q\setminus\{0,1\}\). There are \((q-2)(q-3)(q-4)\) such triples. Direct joins and intersections give the Pascal line
\[
L(d,e,f)=\left[de:\,1+\frac{d(1+e+f)}f:\,1\right]. \tag{1}
\]
This is a triple of line coefficients \([A:B:C]\), meaning \(AX+BY+CZ=0\). Thus the intersection with the parametrized conic is the quadratic
\[
t^2+\left(1+\frac{d(1+e+f)}f\right)t+de=0.\tag{2}
\]
There is never an intersection at \(P_\infty\). In characteristic two, a quadratic with nonzero quadratic coefficient has exactly one geometric root if and only if its linear coefficient vanishes; otherwise it has zero or two rational roots. Let \(N_T,N_S,N_E\) denote the numbers of normalized triples giving the respective line classes.

The linear coefficient in (2) vanishes exactly when \(f=d(1+e)/(1+d)\). For each \(d,e\in U\) with \(d\ne e\), this is nonzero and differs from \(d,e\); it equals \(1\) precisely when \(de=1\). There are exactly \(q-2\) such excluded pairs, since \(d\ne d^{-1}\) in \(U\). Hence
\[
N_T=(q-2)(q-3)-(q-2)=(q-2)(q-4).\tag{3}
\]

To count the total number \(R\) of pairs consisting of a normalized triple \((d,e,f)\) and a rational conic point on its Pascal line, solve (2) for \(f\). The putative root \(t\) cannot be \(0,1,\infty\), as substituting \(t=0\) contradicts \(de\ne0\), and substituting \(t=1\) forces \(f=1\). For every \((d,e,t)\in U^3\) with \(d\ne e\), put
\[
P=t^2+t+td+de,\qquad N=td(1+e)\ne0.
\]
The unique candidate is \(f=N/P\). This candidate is valid exactly when the four events
\[
P=0,\qquad P=N,\qquad dP=N,\qquad eP=N\tag{4}
\]
all fail, corresponding respectively to forbidden \(f=\infty,1,d,e\). These four events are disjoint: \(N\ne0\), and coincidence of two of the latter three events would force \(d=1\), \(e=1\), or \(d=e\).

The cardinalities of the four exceptional events, in the order displayed in (4), are
\[
(q-2)(q-5)+\rho_q,\quad(q-2)(q-4),\quad 2(q-2)(q-3),\quad(q-2)(q-5)+\rho_q.\tag{5}
\]
We derive each, including the two non-polynomial corrections.

For \(P=N\), the defining relation reduces to \((t+1)(t+de)=0\); since \(t\ne1\), it gives \(t=de\). For each \(d\in U\), choose \(e\in U\setminus\{d,d^{-1}\}\), giving \((q-2)(q-4)\). For \(dP=N\), the relation is \((t+d)(t+e)=0\), giving two choices of \(t\) for every ordered distinct pair \((d,e)\), hence \(2(q-2)(q-3)\).

For \(P=0\), solve \(e=t(t+1+d)/d\) with \(d,t\in U\). The excluded values \(e=0\) and \(e=1\) occur at \(t=d+1\) and \(t=d\), each in \(q-2\) cases. The excluded coincidence \(e=d\) becomes \(t^2+(1+d)t+d^2=0\). Putting \(k=t/d\) yields
\[
d=\frac{k}{k^2+k+1},\qquad t=\frac{k^2}{k^2+k+1}.
\]
Exactly \(q-2-\rho_q\) values of \(k\in\mathbb F_q^\times\) work: omit \(k=1\) and the \(\rho_q\) roots of \(k^2+k+1\). These three exclusions are disjoint. Thus the first count in (5) is \((q-2)^2-2(q-2)-(q-2-\rho_q)\).

For \(eP=N\), solve \(d=et(t+1)/(e^2+t)\) with \(e,t\in U\). Exclude \(t=e^2\) (zero denominator) and \(t=e\) (which gives \(d=e\)), each in \(q-2\) cases. The remaining forbidden event \(d=1\) is
\[
e^2+e(t^2+t)+t=0.\tag{6}
\]
Write \(e=1+u\) and \(t=1+v\). Equation (6) becomes \(u^2+uv+v^2+uv^2=0\). Since \(e,t\in U\), the slope \(k=v/u\) is nonzero; substitution gives
\[
u=\frac{1+k+k^2}{k^2},\qquad v=\frac{1+k+k^2}{k}.
\]
Exactly \(q-2-\rho_q\) values work: again exclude \(k=1\) and the roots of \(k^2+k+1\). The three forbidden events are disjoint, giving the last count in (5). Notice that (6) is a singular cubic with a rational node at \((e,t)=(1,1)\); its two tangent directions produce precisely the \(\rho_q\) correction.

There are \((q-2)^2(q-3)\) initially admissible triples \((d,e,t)\). Subtracting (5), we obtain
\[
R=(q-2)(q^2-10q+26)-2\rho_q.
\]
A tangent line contributes one rational intersection, a secant two, and an exterior line zero. Therefore \(R=N_T+2N_S\), so (3) gives
\[
N_S=\frac{(q-2)(q-5)(q-6)-2\rho_q}{2},\qquad
N_E=\frac{(q-2)(q^2-5q+2)+2\rho_q}{2}.
\]

Finally undo the normalization: every normalized ordered triple represents \(q(q^2-1)\) ordered sextuples. Each unoriented cyclic hexagon is represented twelve times. Because the group acts transitively on the three classes of lines, dividing the totals by their class sizes gives the multipliers
\[
T_q=\frac{q(q-1)}{12}N_T,\qquad
S_q=\frac{q-1}{6}N_S,\qquad
E_q=\frac{q+1}{6}N_E.
\]
Substitution yields the asserted formulas. All are positive for \(q\ge8\). For \(q=2,4\) there are fewer than six conic points, so the sharp first field is \(q=8\). \(\square\)

## Verification

The standalone script `verify_even_pascal.py` performs two separate exact enumerations. Its normalized-parameter route checks all four exceptional-event counts, their disjointness, and the final formulas over fields of sizes \(8,16,32,64,128,256\). Its direct geometry route independently constructs all rational conic points and lines, evaluates all sixty cyclic arrangements per six-subset, and checks the complete line multiplicity distributions for \(q=8,16\). Both checks passed. In particular, the latter verifies all \(73\) rational lines at \(q=8\) and all \(273\) at \(q=16\). These finite checks support but do not replace the parameter-count proof for all powers of two.

The counts also satisfy the global identity
\[
(q+1)T_q+\frac{q(q+1)}2S_q+\frac{q(q-1)}2E_q
=60\binom{q+1}{6}.
\]

## Relationship to prior work

The classical Pascal construction and its sixty arrangements are discussed by Abdesselam–Chipalkatti (2016), Chipalkatti–Da Silva (2022), and Chipalkatti (2023). The latter two analyze geometric degenerations and enumerative constraints over the complex numbers, respectively; the former reconstructs a sextuple from four prescribed Pascals. The inspected results do not give characteristic-two finite-field line-fiber multiplicities. A separate previously established finite-field result provides formulas in characteristic at least five; its hypotheses exclude the binary-field case, in which all conic tangents are concurrent and the tangent/secant/exterior formulas change. The present theorem supplies this exceptional characteristic uniformly, including the precise \(\mathbb F_4\)-subfield correction and the first possible full-surjectivity threshold.

## Limitations

The theorem counts **unoriented cyclic hexagons with multiplicity**, not distinct Pascal lines for one fixed six-subset; these may coincide. It neither classifies the projective orbits of six-subsets nor treats odd characteristic, singular conics, or nonrational hexagon vertices. The proof establishes formulas only for the stated characteristic-two finite fields, not for arbitrary characteristic-two infinite fields. An unnoticed older equivalent result in finite-projective-geometry literature remains possible.

## References

- Abdelmalek Abdesselam and Jaydeep Chipalkatti, *On the reconstruction problem for Pascal lines*, arXiv:1608.05056 (first posted 17 August 2016), https://arxiv.org/html/1608.05056v1.
- Jaydeep Chipalkatti and Sergio Da Silva, *Degenerations of Pascal Lines*, arXiv:2202.12975 (first posted 25 February 2022), https://arxiv.org/html/2202.12975v1.
- Jaydeep Chipalkatti, *On the Enumerative Geometry of Pascal's Hexagram*, arXiv:2303.10319 (first posted 18 March 2023), https://arxiv.org/html/2303.10319.
