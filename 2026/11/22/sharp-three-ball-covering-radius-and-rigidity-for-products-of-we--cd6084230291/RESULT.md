# Sharp three-ball covering radius and rigidity for products of weighted four-cycles

## Finding
For a four-cycle \(X_{a,b}\) with successive positive edge lengths \(a,b,a,b\), let \(Y=X_{a,b}\times X_{a,b}\) have the \(\ell^p\)-product of the shortest-path metrics. If \(1\le p<\infty\), the exact three-center covering radius is
\[
R_{3,p}(Y)=\min_{\substack{S\subset Y\\|S|=3}}\max_{z\in Y}\min_{s\in S}d_p(z,s)=(a^p+b^p)^{1/p}.
\]
For \(1<p<\infty\), the number of unordered optimal triples is \(32\) if \(a\ne b\), and \(96\) if \(a=b\). At equality of the edge lengths, the configurations have exactly two isometry orbits, containing \(32\) and \(64\) triples. When \(a\ne b\), every optimizer has the explicit complementary-pair form described below. In particular, for all \(a,b>0\) and \(p>1\), at radius \(R_{3,p}\) the individual factors require two covering balls but their product requires exactly three, not four.

## Assumptions and scope
The four vertices carry the *vertex-set* shortest-path metric of the weighted graph cycle, not the continuous metric-graph space. Every covering-ball center is required to be one of the sixteen product points. The exponent is finite and \(1\le p<\infty\); the counts apply only to \(p>1\). We work with closed balls, including threshold endpoints. Write \(a\ge b\) by relabeling the alternating edges if necessary.

Identify the four-cycle with \(\{0,1\}^2\), with metric \(d((u,v),(u',v'))=a|u-u'|+b|v-v'|\). A point of its product is \((A,B)\), with long-edge bits \(A=(u_1,u_2)\in\{0,1\}^2\) and short-edge bits \(B=(v_1,v_2)\in\{0,1\}^2\). This representation is an isometry, so no graph-distance approximation is involved.

## Proof
**Lower bound, including the endpoint \(p=1\).** Set \(R=(a^p+b^p)^{1/p}\). For any radius \(r<R\), the ball around \((A,B)\) is contained in the six-point set
\[
E(A,B)=\{(A,D):D\in\{0,1\}^2\}\;\cup\;\{(C,B):\operatorname{dist}_{H}(A,C)=1\}.
\]
Indeed, changing both long-edge bits costs \(2^{1/p}a\ge R\); changing one long bit and any short bit costs at least \(R\) if the bits belong to different factors and costs \(a+b\ge R\) if they belong to the same factor. Thus only the stated possibilities remain. Any three centers use at most three of the four long-bit fibers. If three distinct long-bit fibers occur, the omitted fiber is adjacent in the long-bit square to only two centers and receives at most two of its four short-bit labels. If at most two fibers occur, an omitted fiber receives at most three labels. In either case it cannot be covered. Consequently \(R_{3,p}\ge R\).

**Attainment.** Choose the three centers
\[
(A,B)=(00,00),\quad(00,11),\quad(11,00).
\]
The fibers with long-bit labels \(00\) and \(11\) are fully covered because all short-bit differences cost at most \(2^{1/p}b\le R\). In a remaining fiber \(01\) or \(10\), the first two centers cover the two complementary pairs of short-bit labels: changing one long bit and the short bit in the other factor costs exactly \(R\), while leaving that short bit fixed costs only \(a\). Therefore the entire product is covered at radius \(R\).

**Exact three-ball rather than two-ball minimum.** When \(a>b\) and \(p>1\), an \(R\)-ball comprises exactly eight points: its own full four-point long-bit fiber and one two-point line in each neighboring long-bit fiber. Every pair of such balls intersects: for equal long-bit centers the common full fiber has four points; for adjacent or opposite long-bit centers one of the intermediate fibers supplies a common point. Two eight-point balls therefore cannot cover sixteen points. For \(a=b\), an \(R\)-ball is a nine-point \(3\times3\) king neighborhood in the \(4\times4\) toroidal grid, and two such neighborhoods intersect in at least four points, so two again cannot suffice.

**Rigidity for unequal edge lengths.** Suppose \(a>b\) and \(p>1\). A ball centered at long-bit label \(A\) covers all four short labels in its own fiber, no point of the opposite fiber, and one short-bit line of two points in each adjacent fiber. If three distinct long-bit center labels are used, the omitted long-bit fiber receives two perpendicular lines from its two neighboring center labels; their union has only three of its four points. If exactly two distinct center labels are adjacent, one omitted fiber can only be reached from the first group and another only from the second, forcing at least two centers in each group; impossible with three centers. Hence the two occupied long-bit labels must be opposite and one has two centers. Covering both missing fibers forces the short-bit labels of this duplicated pair to differ in *both* coordinates, i.e. be complementary. Conversely any such triple covers by the attainment argument. There are four choices for the doubled long-bit label, two unordered complementary short-bit pairs, and four labels for the remaining center, hence exactly \(4\cdot2\cdot4=32\) optimal triples.

**Rigidity for equal edge lengths.** For \(a=b\), the optimal-radius neighborhood is exactly the \(3\times3\) toroidal king neighborhood. A self-contained integer-mask enumeration of all \(\binom{16}{3}=560\) unordered center triples in `checker.py` confirms precisely \(96\) coverings and, under the complete order-\(128\) product-square isometry group, two orbits of sizes \(32\) and \(64\). Its exact enumeration loops over every candidate triple and every point, rather than sampling.

**Covering-number consequence.** For finite \(p>1\), strict Minkowski inequality gives \(\max(a,b)\le R<a+b\). Hence \(X_{a,b}\) needs exactly two radius-\(R\) balls, while its square needs exactly three, contradicting a putative product lower bound of four. At \(p=1\), \(R=a+b\), so the factor itself is covered by one ball and this mechanism disappears.

## Verification
The included dependency-free `checker.py` enumerates all 560 unordered triples exactly using sixteen-bit integer masks, checks the two-ball lower bound, verifies the precise counts 32 and 96, checks the long/short-bit characterization of all 32 asymmetric optimizers, and computes the two square-case isometry orbits. It also checks the universal strict-radius six-point envelope and its maximum three-center union size of 14. Running `python checker.py` prints `PASS`. The continuous-parameter inequalities and the six-point-envelope argument above—not numerical sampling—establish the result for every permitted \(a,b,p\).

## Relationship to prior work
Cieliebak and Cieliebak, *Covering numbers of metric spaces* (arXiv:2611.15599v1), Example 3.4, exhibit the equal-edge four-cycle as a three-ball counterexample for \(p>1\) and Lemma 3.5 treats the sum-metric boundary. The present contribution is the exact sharp radius for **every** alternating positive edge weighting, the explicit rigidity description for unequal weights, and the complete square equality spectrum and orbit count. Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph* (2024), studies combinatorial domination of several graph products, but its torus is the Cartesian grid and its king graph is the nonperiodic grid; neither source supplies the weighted metric covering radius or all its equality configurations.

## Limitations
This theorem concerns only two-fold products of alternating weighted four-cycles and finite \(p\), with centers constrained to the finite vertex set. It does not prove or disprove the general sum-metric covering-number conjecture. The equal-edge classification uses a finite exhaustive certificate; it is not extrapolated to larger cycles. Historical priority beyond the inspected literature is not independently certified.

## References
1. K. Cieliebak and M. Cieliebak, *Covering numbers of metric spaces*, arXiv:2611.15599v1 (first public 2026-11-11), https://arxiv.org/html/2611.15599v1, especially Example 3.4 and Lemma 3.5.
2. S. Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, Journal of Integer Sequences 27 (2024), Article 24.7.6, https://cs.uwaterloo.ca/journals/JIS/VOL27/Mertens2/mertens12.html.
