# Dominating-matching enumerators and six-class minimum-witness census for cycle prisms

## Finding

Let \(P_n=C_n\square K_2\) be the two-layer circular ladder with \(n\ge3\) labelled rungs. A **dominating matching** is a matching whose endpoint set dominates the graph. Equivalently, it is a paired-dominating vertex set together with a specified perfect-matching witness. Distinct matchings with identical endpoint sets count separately.

Let \(Q_n(z)=\sum_{M}z^{|M|}\), over all dominating matchings of \(P_n\), and let \(\mu_n\) be the number of minimum-cardinality dominating matchings. Then \(Q_n(z)\) admits the explicit 34-state transfer formula in the proof below, and

\[
\gamma_{\mathrm{pr}}(P_n)=2\left\lceil\frac n3\right\rceil.
\]

Moreover, the exact number of **matching witnesses** of this minimum is

\[
\mu_n=\begin{cases}
3+6\mathbf{1}_{6\mid n},&n\equiv0\pmod3,\\
(3j+2)(2j+3),&n=3j+2,\ j\ge1,\\
\dfrac{(3j+2)(16j^3+72j^2+110j+63)}3,&n=6j+4,\ j\ge0,\\
\dfrac{(6j+1)(8j^3+24j^2+25j+6)}3,&n=6j+1,\ j\ge1.
\end{cases}
\]

For example \((\mu_3,\ldots,\mu_{10})=(3,42,25,9,147,56,3,435)\). The count is eventually a six-residue quasi-polynomial; in the two residue classes congruent to one modulo three it is quartic.

## Assumptions and scope

Graphs are undirected and simple. Each of the \(2n\) vertices is a pair \((i,r)\), where \(i\) is a rung index modulo \(n\) and \(r\in\{0,1\}\). The edges are the rung pairs \((i,0)(i,1)\) and the two cyclic rows \((i,r)(i+1,r)\). The vertices and rungs are labelled; no quotient by graph automorphisms is taken. A paired-dominating set has an induced perfect matching, but \(\mu_n\) counts all such **specified matchings**, not distinct dominating vertex sets. The two numbers can differ (at \(n=4\), there are \(42\) minimum matching witnesses but only \(36\) distinct minimum paired-dominating vertex sets).

## Proof

**A sharp lower bound.** Each edge's two endpoints jointly dominate at most six vertices of a cubic graph. Thus the \(k\) edges of any dominating matching on \(P_n\) cover at most \(6k\) vertices, giving \(k\ge\lceil n/3\rceil\). Conversely, choose vertical rungs indexed \(0,3,6,\ldots\), omitting indices beyond \(n-1\). These \(\lceil n/3\rceil\) disjoint rung edges dominate both layers because each cycle column is at cyclic distance at most one from a chosen rung. The paired-domination number is twice the minimum matching size.

**Transfer for every cardinality.** The ten column symbols are
\[
\Sigma=\{(a,b):a,b\in\{0,L,R\}\}\cup\{(V,V)\}.
\]
Here \(0\) means an unmatched vertex, \(L\) and \(R\) mean matched to the preceding and following column in that row, and \((V,V)\) means the vertical rung edge is selected. A vertex is in the matching endpoint set exactly when its symbol is nonzero. Adjacent columns \(a,b\) are *compatible* when, in each row, \(a_r=R\) if and only if \(b_r=L\). Define the weight
\[
w(b)=\mathbf1_{b=(V,V)}+\#\{r:b_r=R\}.
\]
It counts the vertical edge in the column or the horizontal matching edges going right. A middle column \(b\) is dominated given previous \(a\) and next \(c\) if, for each row \(r\) with \(b_r=0\), at least one of \(b_{1-r},a_r,c_r\) is nonzero.

There are exactly 34 compatible ordered pairs \((a,b)\). Index them in lexicographic order and define the 34-by-34 polynomial matrix \(T(z)\) by
\[
T(z)_{(a,b),(b,c)}=\begin{cases}z^{w(b)},&\text{if }b,c\text{ are compatible and }b\text{ is dominated by }a,b,c,\\0,&\text{otherwise.}\end{cases}
\]
All other entries are zero. There are 101 nonzero directed transitions. Each closed length-\(n\) state walk corresponds bijectively to a dominating matching on the labelled circular ladder: compatibility ensures that every selected horizontal edge has both endpoints and that no matching edges meet; the middle-column condition ensures domination; the exponents count each selected edge once. Conversely each dominating matching uniquely determines the symbols. Therefore, without any asymptotic or experimental assumption,
\[
\boxed{Q_n(z)=\operatorname{tr}(T(z)^n)}\qquad(n\ge3).
\]
This already determines every coefficient of the full witness enumerator, beyond the minimum term.

**Defect transfer and the rational minimum series.** Replace the exponent \(w(b)\) on every directed edge by \(3w(b)-1\). The exponent of any closed walk is then \(3|M|-n\). The 34-state integer potential \(h\) constructed explicitly by Bellman--Ford relaxations in the accompanying \(\texttt{verify.py}\) satisfies \(3w(b)-1+h(a,b)-h(b,c)\ge0\) on all 101 transitions. Its reweighted edges have respective cost counts \(44,24,29,4\) for costs \(0,1,2,4\). Since potentials cancel on closed walks, all the traces retain the original defect exponents. Let \(A_d\) be the zero-one adjacency matrix of the cost-\(d\) edges, and put
\[
A(u)=A_0+uA_1+u^2A_2+u^4A_4,\qquad
F(x,u)=\sum_{m\ge1}\operatorname{tr}(A(u)^m)x^m.
\]
The zero-cost graph has 27 strongly connected components, precisely two of which are nontrivial directed cycles (lengths three and six). Every other component is acyclic. Thus
\[
D(x)=\det(I-xA_0)=(1-x^3)(1-x^6).
\]
Write \(R=(I-xA_0)^{-1}\). The resolvent expansion gives, exactly as rational formal power series,
\[
\begin{aligned}
F_0(x)&=[u^0]F=\operatorname{tr}(R-I),\\
F_1(x)&=[u^1]F=x\operatorname{tr}(RA_1R),\\
F_2(x)&=[u^2]F=x\operatorname{tr}(RA_2R)+x^2\operatorname{tr}(RA_1RA_1R).
\end{aligned}
\]
The following **three rational identities** hold:
\[
\boxed{F_0(x)=\frac{3x^3(1+3x^3)}{1-x^6}},\qquad
\boxed{F_1(x)=\frac{x^2(6+7x^3-x^6)}{(1-x^3)^3}},
\]
\[
\boxed{F_2(x)=\frac{x(1+39x^3+22x^6+41x^9-17x^{12}+15x^{15}-6x^{18}+x^{21})}{(1-x^3)^5(1+x^3)^2}}.
\]
Here is a finite **exact proof certificate** for these identities, rather than an extrapolation from finite graph sizes. Every entry of \(\operatorname{adj}(I-xA_0)\) has polynomial degree at most 33, and \(D\) has degree nine. Multiplying the three resolvent expressions by \(D,D^2,D^3\) respectively yields polynomial numerators of degrees at most \(33,67,101\). Each proposed denominator divides the corresponding \(D,D^2,D^3\). The accompanying exact-integer verifier independently computes all trace coefficients of cost \(0,1,2\) through \(x^{103}\) by 34-state path enumeration and matches these with coefficients of the stated rational forms obtained by independent denominator recurrences. Since the difference after multiplication by the relevant \(D^j\) is a polynomial of degree at most \(33,67,101\), agreement through \(x^{101}\) forces that difference to be identically zero. This supplies an exhaustive finite algebraic certificate for the rational identities at every order.

For \(n\equiv0,2,1\pmod3\), a minimum matching has defect \(0,1,2\) respectively. Thus \(\mu_n\) is the coefficient of \(x^n\) in \(F_0,F_1,F_2\) according to the residue class. The formal transfers at lengths one and two are not simple prism graphs; they contribute just \(x+6x^2\) to the relevant series, which are excluded by the stated \(n\ge3\) range. Expanding the three rational functions by the binomial theorem gives precisely the displayed six-residue formulas. This completes the proof.

## Verification

The fully self-contained Python 3 program \(\texttt{verify.py}\) uses exact integer arithmetic and no external packages. It reconstructs the ten symbols, all 34 states and 101 transitions; finds a feasible integer potential by relaxation; checks all reweighted costs and the two zero-cost cycles; computes exact defect trace coefficients for lengths through 103; and checks both the rational recurrences and the closed quasi-polynomial formulas. Its independent graph-level checker enumerates actual matchings and tests domination on labelled prisms for lengths three through twelve at minimum size, and independently checks the entire matching polynomial for lengths three through six; it also checks the rung construction through length 120. A successful full replay ends with \(\texttt{VERIFY\_OK}\). The logical extension to every length is supplied by the rational-denominator degree certificate and the graph/transfer bijection, not by assuming the finite tests continue indefinitely.

## Relationship to prior work

Lu and Wu (2026) study upper bounds for paired domination in cubic bipartite graphs, including the general bound for cubic bipartite graphs; it does not state this minimum *matching-witness* count or the full prism transfer polynomial. Mynhardt and Schurch (2011) study paired domination in graph prisms and associated structural bounds, not this cyclic-ladder counting theorem. Allagan et al. (2026) enumerate **ordinary** dominating sets in prism graphs by congruence class, without requiring a specified perfect matching of selected vertices; those numbers are mathematically different. The definition of paired domination traces to Haynes and Slater. The unrestricted minimum matching count and generating function presented here were not located in the material inspected, but unindexed equivalent formulas remain a historical-priority risk.

## Limitations

The counting theorem is for the two-layer cycle prism with labelled rungs and simple cycles of length at least three. It counts dominating matchings, equivalently paired-dominating sets **with a chosen perfect-matching witness**; it does not count distinct paired-dominating vertex subsets, and it makes no claim about general cubic graphs or a graph's unlabelled automorphism orbits. The coefficient certificate verifies an exact finite matrix identity; it is not an independent mathematical audit, and historical priority is provisional.

## References

- C. Lu and Q. Wu, *Paired Domination in Cubic Bipartite Graphs*, arXiv:2609.30152 (first publicly submitted 2026-09-24).
- C. M. Mynhardt and M. Schurch, *Paired domination in prisms of graphs*, Discussiones Mathematicae Graph Theory 31 (2011), 5–23, DOI:10.7151/dmgt.1526.
- J. Allagan and collaborators, *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words*, arXiv:2601.03488 (2026).
- T. W. Haynes and P. J. Slater, *Paired-domination in graphs* (1998).
