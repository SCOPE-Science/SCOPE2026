# Exact scale-transfer and sharpness laws for ultrametric product coverings

## Finding
Let \((X,d_X)\) and \((Y,d_Y)\) be nonempty finite ultrametric spaces, let \(r>0\), and let \(1\le p<\infty\). Equip \(X\times Y\) with the metric
\[
d_p((x,y),(x',y'))=(d_X(x,x')^p+d_Y(y,y')^p)^{1/p}.
\]
Let \(N_s(Z)\) denote the least number of **closed** radius-\(s\) balls whose centers belong to \(Z\) and cover \(Z\). In each factor, closed radius-\(r\) balls partition the space; write \(X=\bigsqcup_i C_i\), \(Y=\bigsqcup_j D_j\). Define \(\Delta_X=\max_i\operatorname{diam}C_i\) and \(\Delta_Y=\max_j\operatorname{diam}D_j\).

**Theorem A (sharp multiplicativity).** For arbitrary finite ultrametric factors,
\[
N_r(X\times_p Y)=N_r(X)N_r(Y)
\quad\Longleftrightarrow\quad
\Delta_X^p+\Delta_Y^p\le r^p.
\]
Otherwise the inequality is strict in the increasing direction. Thus equality has an exact threshold in \(p\), with the maximum metric as the limiting multiplicative case.

**Theorem B (complete scale-transfer formula).** Suppose additionally that each \(C_i\) is an equilateral cluster of cardinality \(m_i\), with common off-diagonal distance \(a_i\in(0,r]\) for \(m_i>1\), and set \(a_i=0\) for singleton clusters. There is no restriction on the internal hierarchical levels of \(D_j\). Put \(t_i=(r^p-a_i^p)^{1/p}\). Then
\[
\boxed{N_r(X\times_pY)=\sum_i\sum_j\min\{m_i,\ N_{t_i}(D_j)\}.}
\]
Each \(N_{t_i}(D_j)\) is a standard single-ultrametric covering number, i.e. the number of closed radius-\(t_i\) classes inside \(D_j\). For any \(r\), this gives a finite, exact evaluation without constructing the product covering graph.

## Assumptions and scope
All spaces are finite and nonempty, all distances are metric (zero only on the diagonal), and ball centers are restricted to the corresponding finite space. Radii are closed, so equality at a distance threshold is included. In Theorem B, distinct \(C_i\) are at distances strictly greater than \(r\); their separation need not be constant. The case \(m_i=1\) uses \(a_i=0\). The value \(p\) is any finite real \(\ge1\), though the exact checker restricts to integer \(p\). Theorem A requires no equilateral-cluster assumption. The maximum-product metric \(d_\infty=\max\{d_X,d_Y\}\) always satisfies multiplicativity, directly by ultrametric ball partitions.

## Proof
**1. Rectangle separation.** In an ultrametric, membership in the same closed radius-\(r\) ball is an equivalence relation: \(x\sim_r x'\) iff \(d_X(x,x')\le r\); the equivalence classes are exactly the nonempty closed radius-\(r\) balls. This also holds in \(Y\). Since \(d_p\ge\max\{d_X,d_Y\}\), a radius-\(r\) product ball centered at \((x,y)\) is entirely contained in the unique rectangle \(C_i\times D_j\) containing its center. Consequently, the minimum number for the whole product is the sum of the independent minimum numbers for these rectangles, and it is at least the number of such rectangles, \(N_r(X)N_r(Y)\).

**2. One center versus a whole rectangle.** For every finite ultrametric class \(C\) and every chosen \(x\in C\),
\[
\max_{u\in C}d_X(x,u)=\operatorname{diam}C.
\]
Indeed, for a diametral pair \(u,v\), the strong triangle inequality yields \(\operatorname{diam}C=d_X(u,v)\le\max\{d_X(u,x),d_X(x,v)\}\); the reverse inequality follows from the definition of diameter. For any center \((x,y)\in C_i\times D_j\), the maximum product distance to points of that rectangle is therefore \((\operatorname{diam}(C_i)^p+\operatorname{diam}(D_j)^p)^{1/p}\), because the maximizing coordinates can be selected independently. It can cover the complete rectangle with one ball exactly when the corresponding sum of powers is at most \(r^p\). Since distinct rectangles cannot share covering balls, equality with one ball per rectangle holds precisely when this condition holds for *every* rectangle. Taking the maximum diameter in each factor gives Theorem A.

**3. Exact equilateral scale-transfer.** Fix \(C_i\times D_j\) with \(m=m_i\), \(a=a_i\) and \(t=(r^p-a^p)^{1/p}\). Because \(D_j\) has diameter at most \(r\), the entire row \(\{x\}\times D_j\) lies in the radius-\(r\) product ball centered at any \((x,y)\) with \(y\in D_j\). Choosing one such center in each of the \(m\) rows gives a cover with \(m\) balls. Alternatively, take a minimum radius-\(t\) covering of \(D_j\), choose all its centers in a *single* row, and use the same centers to cover all other rows: off-row distances are \(a\) and the \(Y\)-distance is at most \(t\), so their product distance is at most \(r\). This gives an upper bound \(N_t(D_j)\).

For the reverse bound, suppose a covering has fewer than \(m\) centers. Then at least one row of \(C_i\times D_j\) contains *no* center. Every center must cover a point \((x_*,z)\) in this absent row through horizontal distance \(a\); hence its \(Y\)-coordinate is within distance \(t\) of \(z\). The centers' \(Y\)-coordinates therefore constitute a radius-\(t\) covering of \(D_j\), forcing at least \(N_t(D_j)\) centers. Any covering thus uses at least \(\min\{m,N_t(D_j)\}\) centers. This also holds for \(m=1\), when the first upper bound is already one. Summing the exact rectangle minima proves Theorem B.

**4. Sharpness and scale example.** If \(X,Y\) are equilateral with respective sizes \(m,n\) and all nonzero distances exactly \(r\), each factor needs one ball but Theorem B gives \(N_r(X\times_pY)=\min\{m,n\}\) for every finite \(p\). Thus the excess over the product of factor covers can be arbitrarily large. For a less degenerate example, take \(r=3\), \(p=1\), let \(X\) have a three-point equilateral class of internal distance 3 and a two-point equilateral class of internal distance 1, with interclass distance 7; let \(Y\) be one four-point class made of two pairs at internal distance 1 and between-pair distance 3. The formula gives \(\min(3,N_0(Y)) + \min(2,N_2(Y))=3+2=5\), whereas \(N_3(X)N_3(Y)=2\).

## Verification
The standalone `checker.py` enumerates exact finite ultrametric examples with independent bitmask-set-cover optimization. It compares the analytic formula with brute-force optimum in 400 hierarchical cases, checks Theorem A in 598 cases (including arbitrary ultrametric factors), and verifies the equilateral extremal and two-scale examples. Integer powers avoid floating-point threshold ambiguities. The proof above, not finite testing, establishes the statements for every finite cardinality and all real \(p\ge1\).

## Relationship to prior work
Cieliebak and Cieliebak (2026) formulate the general sum-metric covering inequality and establish cases involving metric trees; their paper does not state this finite-ultrametric exact equality criterion or the cluster/hierarchy covering sum. Dovgoshey and Martio (2009, Theorem 4.1 and Lemma 4.2) study products and the multiplicativity of covering/packing counts for the **maximum** product metric, not the finite-\(p\) sharp equality threshold. Cartesian-product domination theory includes the special two-equilateral-factor rook-graph pattern; the result above credits this simpler phenomenon and derives an arbitrary-hierarchy scale-transfer formula beyond it. A covering inequality alone does not yield the criterion for equality or the full formula.

## Limitations
The exact value formula in Theorem B requires one factor's radius-\(r\) classes to be equilateral. Theorem A applies to all finite ultrametrics but does not determine every *strictly greater* covering number for arbitrary two hierarchies. The claim does not address arbitrary non-ultrametric factors or infinite spaces. The full historical literature cannot be proven exhausted; earlier terminology for graph domination or metric entropy could conceal a prior equivalent result.

## References
1. K. Cieliebak and M. Cieliebak, *Covering numbers of metric spaces*, arXiv:2611.15599v1, first submitted 2026-11-11, https://arxiv.org/abs/2611.15599 .
2. O. Dovgoshey and O. Martio, *Products of metric spaces, covering numbers, packing numbers, and characterizations of ultrametric spaces*, Revue Roumaine Mathématiques Pures et Appliquées 54 (2009), https://www.csm.ro/reviste/Revue_Mathematique/pdfs/2009/5-6/8Dovgoshey.pdf .
3. A. P. Kazemi, B. Pahlavsay and R. J. Stones, *Cartesian Product Graphs and k-Tuple Total Domination*, Filomat 32 (2018), https://www.pmf.ni.ac.rs/filomat-content/2018/32-19/32-19-16-4805.pdf .
