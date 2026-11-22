# Three-line shattering in the ternary projective plane: four-arcs and collinear facets

## Finding

Let \(P\) be the thirteen-point projective plane \(\operatorname{PG}(2,\mathbb F_3)\), and let \(\mathcal U_3\) be the family of all unions of **exactly three pairwise distinct projective lines**. A support \(S\subseteq P\) is VC-shattered by \(\mathcal U_3\) if and only if either \(|S|\le3\), or \(|S|=4\) and no three of its points are collinear (a *four-arc*). The complete shattered-support polynomial is

\[
\boxed{\Phi_{\mathcal U_3}(z)=1+13z+78z^2+286z^3+234z^4.}
\]

In particular \(\operatorname{VCdim}(\mathcal U_3)=4\). The shattering complex is nonpure: its inclusion-maximal faces are precisely the \(52\) collinear triples and the \(234\) four-arcs. Moreover, the complements of the \(286\) distinct hypotheses in \(\mathcal U_3\) are **exactly these \(286\) maximal shattered supports**, each occurring exactly once. This gives a facet–hypothesis complement duality.

For comparison, the incidence family of unions of exactly two *distinct* projective lines has \(702\) shattered four-point supports (the noncollinear four-sets); the three-distinct-line family shatters only \(234\) four-point supports. Thus increasing the number of required distinct lines need not increase the number of shattered supports, even though both families have VC dimension four.

## Assumptions and scope

Every projective line in \(P\) contains four points; every point lies on four lines; any distinct lines meet once, and any two points determine a unique line. All support sets are unordered sets of distinct projective points. Shattering requires that for **every** subset \(T\subseteq S\), a member \(U\in\mathcal U_3\) satisfy \(U\cap S=T\). A single line, two lines, or a repeated line cannot be used as a hypothesis. The projective plane here is uniquely the order-three plane, not an arbitrary-order plane and not an affine or real Euclidean plane. The result concerns ordinary static VC-shattering, not adaptive Littlestone dimension.

## Proof

**1. Complements of all three-line concepts.** Three distinct lines in a projective plane are either concurrent at one point or have three pairwise distinct intersection points. In the concurrent case, their union has \(1+3\cdot3=10\) points; if \(L\) is the fourth line through their common point, the complement consists of the three points on \(L\) other than that common point. Thus it is a collinear triple.

In the nonconcurrent case the union has \(3\cdot4-3=9\) points, hence the complement \(A\) has four points. Were three points of \(A\) on some line \(M\), then \(M\) could meet the union of the three hypothesis lines in at most one of its four points. But each of those three distinct hypothesis lines meets \(M\), forcing them all through the same fourth point of \(M\), contradiction. Thus \(A\) is a four-arc.

Conversely, a collinear triple \(T\) lies on a unique line \(L\), with a unique unselected fourth point \(o\). The three lines other than \(L\) through \(o\) cover precisely \(P\setminus T\). For a four-arc \(A\), its pairs determine six distinct secant lines. Each arc point has three secants and one tangent, so there are exactly four distinct tangents. The remaining \(13-6-4=3\) projective lines avoid \(A\). Their union lies in the nine-point complement of \(A\); as the union of three distinct lines has at least nine points, it equals that complement. Each complement determines its union uniquely as a point set, and the two complement types have different sizes. Thus precisely \(52+234=286\) distinct hypotheses arise, bijective to the collinear triples and four-arcs.

**2. Shattering all four-arcs.** Fix a four-arc \(A\). Its three exterior lines miss \(A\), while its four tangents meet \(A\) at exactly one point and its six secants meet \(A\) at exactly two points. For a prescribed trace \(T\subseteq A\), take the union of three distinct lines as follows: if \(|T|=0\), use the three exterior lines; if \(|T|=1\), use the corresponding tangent and two exterior lines; if \(|T|=2\), use the corresponding secant and two exterior lines; if \(|T|=3\), use two secants whose intersections with \(A\) cover precisely those three points, and one exterior line; and if \(|T|=4\), use two secants joining disjoint pairs in \(A\), with one exterior line. All indicated lines are distinct. These constructions give every one of the sixteen binary traces, so every four-arc is shattered.

**3. Shattering all triples and their subsets.** For a collinear triple \(T\) on \(L\), let \(o\) be the fourth point on \(L\). The three lines through \(o\) other than \(L\) miss \(T\). For a desired trace \(B\subseteq T\) of size zero, one, or two, choose one non-\(L\) line through each selected point; these lines meet \(T\) in exactly the selected point and are distinct. Fill to three distinct lines with lines through \(o\) other than \(L\). For \(B=T\), take \(L\) and any two other lines. Hence collinear triples are shattered.

For a noncollinear triple \(T\), its three pair-joining lines are distinct and nonconcurrent, with a union of nine points. Any of the four complementary points extends \(T\) to a four-arc. The hereditary property of shattering and Step 2 show that all noncollinear triples are shattered. Each singleton, pair, and the empty support extend to a triple, so are also shattered.

**4. Excluding nonarc four-sets.** Every four-set that is not an arc contains three collinear points on a line \(L\). If the fourth point also lies on \(L\), every projective line intersects that four-point support, so no three-line union can produce the empty trace. Otherwise let \(x\notin L\) be its fourth point and let \(o\) denote the unique point of \(L\) not among the chosen collinear triple. Any projective line avoiding the three selected points of \(L\) must meet \(L\) at \(o\), so the only candidate lines avoiding the four-set are the three non-\(L\) lines through \(o\). Exactly one of those contains \(x\), leaving only **two** lines disjoint from the four-set. A union of three *distinct* lines therefore cannot miss the support entirely. This excludes its empty trace and proves that precisely four-arcs are the shattered four-sets.

**5. No five-set can be shattered.** Any five points in \(P\) contain three collinear points. Indeed, otherwise their ten pairs would determine ten distinct secants. Counting the lines through their points shows that these are the only ten lines meeting the alleged five-arc, leaving three disjoint lines. But three distinct lines have union of size at least nine, whereas the complement of five points has only eight points. Contradiction. Therefore every five-set contains a four-set with three collinear points, and Step 4 plus heredity excludes shattering of the five-set. Larger supports are likewise excluded.

**6. Enumeration of faces and facets.** The four-arc count is \(\binom{13}{4}-13(\binom43\cdot9+1)=715-481=234\): a nonarc four-set has three points of a unique line and its fourth point elsewhere, or consists of a whole line. The collinear triples number \(13\binom43=52\). All \(\binom{13}{k}\) supports with \(k\le3\) are shattered; Step 4 gives the \(234\) shattered quadruples, proving the polynomial. Each collinear triple cannot extend to a shattered four-set, whereas every noncollinear triple extends to a four-arc by Step 3. Hence the facets are exactly the two families already identified as complements in Step 1.

## Verification

Two standalone standard-library Python programs verify the complete finite incidence statement independently. `verify_coordinates.py` constructs projective points and lines from nonzero ternary homogeneous coordinates; `verify_cyclic.py` uses the difference set \(\{0,1,3,9\}\) modulo \(13\), independently generating the same order-three incidence axioms. Each generates all \(286\) three-distinct-line hypotheses and exhausts all \(8192\) point supports by computing their distinct Boolean traces; each verifies the polynomial, facet sizes and the complement correspondence. The coordinate program also checks exactly-two-distinct-line four-support counts. Both output explicit `PASS` markers. The proof above, not finite experiment alone, establishes the geometric characterization.

## Relationship to prior work

Csikós, Kupavskii and Mustafa (2018) treat broad VC-dimension bounds for unions of Euclidean halfspaces, not the support-level classification of three projective lines over \(\mathbb F_3\). Eleftheriou, Papadopoulos and Westhead (first posted 2025) classify maximal shattered configurations for unions of two and three **real Euclidean lines**; their geometric conclusions and dimensions do not imply the present finite-projective answer. An existing finite-projective-plane classification of two-line unions is closer in ground set but uses at most two lines and has different extremal supports. It neither supplies an equivalence to this three-distinct-line family nor its complement–facet duality. Known \(234\) four-arc and \(52\) collinear-triple counts are classical incidence enumerations and are **not** claimed to be new individually; the specific full shattering characterization and its duality are the contribution.

## Limitations

The argument addresses the order-three projective plane and exactly three distinct lines only. It does not establish an analogous classification for other orders, arbitrary 3-line multiplicity conventions, adaptive shattering, or arbitrary unions of projective curves. Prior computation under terminology such as finite incidence traces, projective caps, line covers or maximum classes remains a historical-priority risk. No independent mathematical audit has been performed.

## References

1. M. Csikós, A. Kupavskii and N. H. Mustafa, *Optimal Bounds on the VC-dimension*, arXiv:1807.07924v1, first public 2018-07-20. https://arxiv.org/abs/1807.07924
2. P. E. Eleftheriou, A. Papadopoulos and F. Westhead, *Exact VC-Dimensions of Certain Geometric Set Systems*, arXiv:2501.09847v1, first public 2025-01-16. https://arxiv.org/abs/2501.09847
