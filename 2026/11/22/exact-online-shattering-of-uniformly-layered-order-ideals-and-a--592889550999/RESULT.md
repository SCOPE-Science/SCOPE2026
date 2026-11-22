# Exact online shattering of uniformly layered order ideals and a sharp five-level entropy gap

## Finding
For every pair of integers \(w,h\ge 1\), let \(P_{w,h}=A_1\oplus\cdots\oplus A_h\) be the finite ordinal sum of \(h\) antichains, each of cardinality \(w\). All points of an earlier level are less than all points of a later level; distinct points within one level are incomparable. Write \(\mathcal J(P_{w,h})\) for the family of all lower subsets (including the empty subset), viewed as Boolean membership hypotheses on the points. Then
\[
\boxed{\operatorname{Ldim}(\mathcal J(P_{w,h}))=w-1+\lfloor\log_2(h+1)\rfloor,\quad \operatorname{VCdim}(\mathcal J(P_{w,h}))=w.}
\]
The hypothesis count is \(N_{w,h}=1+h(2^w-1)\). For \(w\ge2\), the difference between its counting bound \(\lfloor\log_2 N_{w,h}\rfloor\) and its exact Littlestone rank is always either zero or one. It vanishes at heights \(1,2,3,4\), and is exactly one at height \(5\), so five levels is the sharp first height at which the entropy bound fails for **every** width at least two. In particular, at every fixed \(w\), the static dimension remains \(w\) while the adaptive dimension grows unboundedly and logarithmically with height.

The same statement computes the finite-trace online rank of the definable concept family \(\{\{p\in P_{w,h}:p<y\}:y\in\mathbb P\}\), where \(\mathbb P\) is the countable homogeneous universal poset and \(P_{w,h}\) is a named induced finite subposet.

## Assumptions and scope
A complete binary membership mistake tree of depth \(d\) is shattered when every branch-label sequence of length \(d\) has a realizing member of \(\mathcal J(P)\), with the query point at a node allowed to depend on previous answers. The Littlestone dimension is the maximum such depth, and a one-element hypothesis class has dimension zero. The finite order is strict; for \(p<y\), \(p\) and \(y\) are distinct. No probabilities or large-order asymptotic assumptions are required. The conclusion concerns the finite trace class, not the unrestricted rank over the entire homogeneous poset.

## Proof
**1. Trace identification and counting.** If \(y\) is a new point of a poset extending \(P\), then \(I_y=\{p\in P:p<y\}\) is downward closed. Conversely, for any lower set \(I\subseteq P\), adjoining a new point \(y\) above precisely the members of \(I\) and incomparable with every other member of \(P\) gives a finite poset: downward closure is exactly the necessary transitivity condition. The extension property of the homogeneous universal poset realizes this configuration. Thus the definable traces are exactly \(\mathcal J(P)\).

For \(P_{w,h}\), an ideal has some number of completely filled initial levels, optionally followed by a proper nonempty subset of the next level; all subsequent levels are empty. Equivalently, the ideal lattice is the *ordinal sum of \(h\) Boolean \(w\)-cubes*, with each preceding top identified with the next bottom. Each cube adds \(2^w-1\) new ideals, giving \(1+h(2^w-1)\) hypotheses. Every antichain of points in \(P\) can be shattered by its downsets; a comparable pair cannot be shattered because the upper point cannot be included without the lower. Hence the VC dimension is the maximum antichain size, namely \(w\).

**2. An exact residual-state recurrence.** For positive integers \(q_1,\ldots,q_s\), consider a chain of \(s\) Boolean cubes of dimensions \(q_1,\ldots,q_s\) glued top-to-bottom, with its independent coordinate queries at each cube. Call its rank \(R(q_1,\ldots,q_s)\). A zero-dimensional cube contributes only an identified endpoint and may be deleted; \(R(\varnothing)=0\). A query at a coordinate of cube \(j\) produces a zero branch consisting of all earlier cubes followed by a cube of dimension \(q_j-1\), and a one branch consisting of this \(q_j-1\) cube followed by all later cubes. Indeed, on the zero branch later cubes are impossible; on the one branch earlier cubes are impossible. Consequently the complete-tree root recurrence is exact:
\[
R(q_1,\ldots,q_s)=1+\max_{1\le j\le s}\min\bigl\{R(q_1,\ldots,q_{j-1},q_j-1),R(q_j-1,q_{j+1},\ldots,q_s)\bigr\}.
\]
Here the maximum is over nontrivial queries and all zero entries are deleted. For a nonempty cube list, every such query splits the current hypothesis set in two, so the recurrence applies without empty-branch exceptions.

**3. Boundary-cube induction.** Fix \(w\ge1\). Let \(R_w^{a,b}(t)\) be the rank of a chain of \(t\) full cubes of dimension \(w\), with an optional cube of dimension \(w-1\) at the left (\(a=1\)) and at the right (\(b=1\)). Degenerate zero-dimensional cubes are deleted. We prove, simultaneously by induction on \(w\), then on \(t\), that
\[
R_w^{a,b}(t)=w-1+\lfloor\log_2(t+1)\rfloor\quad(t\ge1;\ a,b\in\{0,1\}),
\]
and that \(R_w^{a,b}(0)=w-1\) whenever \(a+b\ge1\). The exceptional empty list \(R_w^{0,0}(0)=0\) is not asserted to obey this formula.

For \(w=1\), the boundary cubes have dimension zero and disappear. A chain of \(t\) one-dimensional cubes has precisely \(t+1\) threshold hypotheses. Its rank is \(\lfloor\log_2(t+1)\rfloor\): the number of hypotheses bounds the depth from above and a balanced threshold query recursively achieves this depth. The boundary-only cases have rank zero.

For \(w\ge2\), the \(t=0\) case with just one boundary cube has Boolean-cube rank \(w-1\). With two boundary cubes, the class is two consecutive Boolean cubes of dimension \(w-1\); by the induction hypothesis at width \(w-1\), its rank is \((w-2)+\lfloor\log_2 3\rfloor=w-1\).

Now let \(t\ge1\), assume the assertions for smaller numbers of full cubes at the same \(w\), and allow either boundary cube to be present. Querying a coordinate of a present end cube leaves on its *outer* branch only one \((w-2)\)-dimensional Boolean cube. That branch has rank \(w-2\), so such a root query yields depth at most \(w-1\). By contrast, querying a coordinate of the \(j\)-th full \(w\)-cube, for \(1\le j\le t\), splits into classes having \(j-1\) and \(t-j\) full cubes, respectively, each with at least one boundary cube of dimension \(w-1\) and at most two. The induction hypothesis therefore makes their ranks
\[
w-1+\lfloor\log_2 j\rfloor\qquad\text{and}\qquad w-1+\lfloor\log_2(t-j+1)\rfloor.
\]
Because \(\min(j,t-j+1)\) is maximal and equals \(\lfloor(t+1)/2\rfloor\) for a middle query, the best full-cube query has depth
\[
w+\left\lfloor\log_2\left\lfloor\frac{t+1}{2}\right\rfloor\right\rfloor
=w-1+\lfloor\log_2(t+1)\rfloor.
\]
This is at least \(w\), exceeding the depth available from an end-cube query. Hence the displayed rank formula holds for every boundary choice; the induction is complete. Taking \(a=b=0\) and \(t=h\) proves the claimed Littlestone formula.

**4. The sharp entropy gap.** Let \(s=\lfloor\log_2(h+1)\rfloor\) and \(L=w-1+s\). For \(w\ge2\), we have \(h\ge2^s-1\) and \(h<2^{s+1}-1\). The lower bound \(N_{w,h}\ge2^L\) follows from the exact nonnegative difference
\[
1+(2^s-1)(2^w-1)-2^{w+s-1}=(2^s-2)(2^{w-1}-1)\ge0.
\]
Also \(N_{w,h}<2^{w+s+1}=2^{L+2}\), so its integer-logarithmic upper bound exceeds \(L\) by at most one. At \(h=1,2,3,4\), direct substitution gives \(\lfloor\log_2 N_{w,h}\rfloor=L\) for every \(w\ge2\). At \(h=5\), \(N_{w,5}=5\cdot2^w-4\ge2^{w+2}\) while \(N_{w,5}<2^{w+3}\), so the entropy bound is \(w+2\) and the exact rank is \(w+1\). For \(w=1\), \(N_{1,h}=h+1\), so the entropy bound is always attained. This proves all sharpness statements.

## Verification
Run `python3 verify.py` with Python 3 and no external packages. It independently enumerates literal downsets as bitmasks and computes their rank directly on residual version-space subsets, separately from a cube-sequence recursion. Every width \(1\le w\le4\) and height \(1\le h\le7\) agrees between those methods and the closed formula (28 direct instances; 19,180 visited residual states). The cube-sequence recurrence then agrees with the formula on an additional 155 instances with \(1\le w\le5\) and \(1\le h\le31\). Widths two through five are checked to have their first entropy deficit at five levels. The actual expected console result is supplied in `verification_output.txt`. These finite checks corroborate but do not replace the all-parameter proof above.

## Relationship to prior work
Littlestone's 1988 paper introduces complete mistake trees and the optimal online mistake bound; binary-search ranks of chains and the information bound are established background. The 2014 online-learning textbook chapter also concerns general online dimensions, not exact weak-order ideal spectra. A previously published bounded-width ideal-rank result gives a polynomial-state dynamic program for all bounded-width posets and an exact dyadic result for product-order grids, but neither solves the displayed closed formula for ordinal sums of antichains nor locates the uniform first entropy gap. Another published exact result concerns a root with independent two-edge arms, a distinct comparability structure. Both already establish applicable generic recurrences, which are credited. The present claim is their explicit solution on the layered homogeneous-poset trace class, including the sharp all-width height threshold; no claim is made that the generic recurrence itself is new.

## Limitations
The closed formula assumes every level has the same positive width; nonuniform weak orders and arbitrary finite posets are not classified. Only Boolean membership traces and their adaptive/static shattering dimensions are treated. The result does not assign a finite unrestricted global online rank to the homogeneous poset. Historical originality is based on identified sources and searches, not a proof of priority; equivalent results might appear under order-ideal or ordinal-sum terminology. Independent validation has not been performed.

## References
1. N. Littlestone, *Learning Quickly When Irrelevant Attributes Abound: A New Linear-threshold Algorithm*, Machine Learning 2 (1988), 285–318, https://homepages.math.uic.edu/~lreyzin/papers/littlestone88.pdf.
2. S. Shalev-Shwartz and S. Ben-David, *Understanding Machine Learning*, Chapter 21: Online Learning, Cambridge University Press, published online 5 July 2014, https://www.cambridge.org/core/books/abs/understanding-machine-learning/online-learning/A43CEEF3F7F18953B592C983087C8A36.
3. *Online ranks of finite order-ideal classes: bounded-width exact computation and dyadic saturation*, publicly accessible proof, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-online-ranks-of-finite-order-ideal-classes-bounded-width-exact-c--68248a42b6fd/RESULT.md.
4. *A leaf erases the online-shattering excess of rooted two-edge arms*, publicly accessible proof, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-leaf-erases-the-online-shattering-excess-of-rooted-two-edge-ar--e81fb3128ebc/RESULT.md.
