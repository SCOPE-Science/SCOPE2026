# Six and only six optimal rational-tangent covers of the first Asgarli–Ghioca curve

## Finding
Let \(C\subset\mathbb P^2_{\mathbb F_{11}}\) be the degree-ten curve
\[
C:\quad X^{10}+Y^{10}+Z^{10}-3(X+Y+Z)^{10}=0.
\]
Let \(\mathcal T\) consist of all distinct \(\mathbb F_{11}\)-lines tangent at a smooth \(\mathbb F_{11}\)-point of \(C\), and call \(W\subseteq\mathcal T\) an *optimal tangent cover* if its union covers all \(\mathbb P^2(\mathbb F_{11})\) using the minimum possible number of lines.

**There are exactly six optimal tangent covers.** All six have eighteen lines and form **one free orbit** under coordinate permutation \(S_3\) acting on \([X:Y:Z]\). In particular every optimal cover is a projective triangle in the dual plane, and the previously exhibited eighteen-line tangent cover generates all the others by permuting coordinates. Each cover has point-multiplicity profile \(1^{90}2^{15}3^{25}7^3\) (numbers of primal points lying on respectively \(1,2,3,7\) selected tangent lines).

The result is a complete classification of optimal **subsets of the actual tangent lines of this fixed equation**, not a classification of all projective triangles in an abstract finite plane. The minimum size eighteen and the existence of one optimal projective triangle were already known; the asserted new part is the exact count **six** and the single free symmetry orbit.

## Assumptions and scope
The field is exactly \(\mathbb F_{11}\), and all projective coordinates, smooth rational tangency points, tangents, covers, and permutations are defined over that field. A line is included once even if it is tangent at multiple rational points. A point \([x:y:z]\) or line coefficient vector \([a:b:c]\) is normalized by making its first nonzero coordinate one. There are \(133\) rational points of the plane, \(90\) rational smooth curve points and \(72\) distinct eligible tangent lines.

The coefficient triple \([a:b:c]\) denotes the line \(aX+bY+cZ=0\); it is not a point of contact. Projective coordinate permutations preserve \(C\) and the set of eligible tangents. No assertion concerns other field sizes, arbitrary degree-ten curves, or all automorphisms of \(C\).

## Proof
**1. The complete rational Gauss image.** Put \(s=x+y+z\). Asgarli and Ghioca show that the rational curve points satisfy \(xyzs\ne0\) and that the unique singular point is \([1:1:1]\). Differentiation in characteristic eleven shows that at any smooth rational point \(Q=[x:y:z]\) the tangent has coefficient triple
\[
\tau(Q)=\bigl[3/s-1/x:3/s-1/y:3/s-1/z\bigr].
\]
The standard-library certificate in `verify.py` enumerates all \(133\) normalized projective points, obtains exactly \(90\) rational smooth points after removing the singular one, and obtains exactly \(72\) different normalized coefficient triples, comprising \(\mathcal T\). The maximum number of these dual points on any dual line is \(11\); the complete incidence histogram is \(1^3 4^6 5^{30}6^{25}7^{24}8^{42}11^3\). Thus \(\mathcal T\), and every subset, contains no complete dual line.

**2. The geometric form of a minimum.** A set of primal lines covers all primal rational points precisely when its points in the dual plane meet every dual rational line. Therefore a tangent cover corresponds to a blocking subset of \(\mathcal T\). By the prime-order Blokhuis bound, any nontrivial blocking set in \(\operatorname{PG}(2,11)\) has at least \(3(11+1)/2=18\) points. A previously published eighteen-tangent projective triangle realizes equality. The Blokhuis–Brouwer–Wilbrink classification for \(p=11\) shows that every blocking set of this minimum size is of Rédei type, and the Lovász–Schrijver characterization of extremal Rédei blocking sets shows that each is projectively equivalent to the standard projective triangle. Consequently any optimal cover has exactly three distinguished dual seven-secants, its triangle sides, with pairwise distinct vertices belonging to \(\mathcal T\).

**3. Four possibilities for any proposed vertex triple.** Choose any ordered noncollinear triangle vertices \(A,B,C\) from the \(72\) dual tangent points and use the projective frame with columns \(A,B,C\). Write the open-side points as
\[
[0:1:u],\quad [1:0:v],\quad [1:w:0],\qquad u,v,w\in\mathbb F_{11}^{\times}.
\]
Let \(S=\{1,3,4,5,9\}\) be the five nonzero squares and \(N=\{2,6,7,8,10\}\) the nonsquares. The usual projective triangle has the three vertices together with five points on each open side. Its projective equivalents with the fixed three vertices are precisely the **four** choices in which the three open-side parameter sets are \(S\) or \(N\), and their quadratic-character signs \(\varepsilon_x,\varepsilon_y,\varepsilon_z\) obey
\[
\varepsilon_z=-\varepsilon_x\varepsilon_y.
\]
Indeed a standard projective triangle is built from square parameters on its sides; a projectivity taking its three vertices to \(A,B,C\) differs from a chosen frame by independent diagonal scalings and a possible permutation. The relation follows from the collinearity equation \(v+uw=0\): the multiplicative characters of the three side ratios have product \(\chi(-1)=-1\). This produces four patterns, since \(\varepsilon_x\) and \(\varepsilon_y\) vary independently.

**4. Exhaustive inclusion test and rigidity.** There are \(\binom{72}{3}=59,640\) unordered distinct tangent-vertex triples, of which \(55,129\) are noncollinear. For each, `verify.py` constructs all four sign-pattern triangle sets by exact modular arithmetic, admitting a candidate only when all eighteen of its points lie in \(\mathcal T\). There are exactly **six distinct** passing subsets. Directly testing their incidences with every one of the \(133\) primal points gives, for each, the multiplicity histogram \(\{1:90,2:15,3:25,7:3\}\), so each is a cover. Every possible optimum was among those tested by Steps 2–3, proving completeness.

Finally the certificate applies all six coordinate permutations to one passing set and obtains the **same six**, with no stabilizer. The previously published eighteen-line witness is one of the six (verified directly). Thus the six constitute one free \(S_3\)-orbit; no other optimal tangent subsets exist.

## Verification
Run `python3 verify.py` with Python 3 (standard library only) in this directory. Its expected completion marker is `SIX_OPTIMAL_TANGENT_COVERS_VERIFIED 6 S3_ORBIT 6 TRIPLES 59640 NONCOLLINEAR 55129`. It reconstructs the tangent image from the defining curve and exact gradient formula, enumerates all triangle vertex triples and four sign patterns, checks every accepted cover against all \(133\) primal points, and verifies the symmetry orbit. The mathematical reduction to projective triangles uses the cited, published blocking-set classification; enumeration alone is not presented as a proof of that reduction.

## Relationship to prior work
Asgarli and Ghioca prove geometric irreducibility and tangent-filling for this curve, along with its rational-point and tangent-line formulas. Blokhuis–Brouwer–Wilbrink and Lovász–Schrijver classify the abstract optimal blocking-set shape. A published study, *An eighteen-tangent projective triangle on the first Asgarli–Ghioca curve*, already proves the exact minimum eighteen, enumerates the same \(72\) tangent lines, and gives **one** explicit optimal eighteen-line set. It expressly leaves classification of all optima and uniqueness unanswered. The present result resolves precisely that remaining incidence-rigidity question, proving there are six coefficient-distinct covers and a unique coordinate-permutation class. These assertions do not follow from the minimum-size or shape theorems alone: those theorems do not count how many triangles fit inside this particular \(72\)-point tangent configuration.

## Limitations
The conclusion is only over the prime field \(\mathbb F_{11}\). This calculation proves uniqueness modulo the visible \(S_3\) subgroup, without classifying the complete projective stabilizer of the curve or the larger field extensions. Exact finite enumeration is supported by the embedded executable proof of its finite claims; the global geometric completeness invokes the identified blocking-set theorems. No independent mathematical audit has been performed. Priority comparisons cover accessible identified literature and research records; an unindexed identical optimal-cover census remains a residual risk.

## References
1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420v1, first public 2023-02-26, Theorem 1.3 and §3. https://arxiv.org/html/2302.13420v2
2. A. Blokhuis, A. E. Brouwer, and H. A. Wilbrink, *Blocking sets in PG(2,p) for small p, and partial spreads in PG(3,7)*, Advances in Geometry special issue (2003), S245–S253, §5.2. https://doi.org/10.1515/advg.2003.2003.s1.245
3. L. Lovász and A. Schrijver, the projective-triangle characterization of extremal Rédei blocking sets, as cited and applied in Reference 2, §1.
4. *An eighteen-tangent projective triangle on the first Asgarli–Ghioca curve*, published result of 2026-10-13 (existing explicit eighteen-line cover and its minimality). https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-an-eighteen-tangent-projective-triangle-on-the-first-asgarli-ghi--6ed9d400dac8
