# Sharp ten-point failure of two-arity class-profile recovery in a tournament wreath product

## Finding
Let \(\mathcal T\) be the countable homogeneous tournament, and let \(\mathcal W\) be the countable structure obtained by replacing each point of a copy of \(\mathcal T\) with a further copy of \(\mathcal T\). The language has the tournament orientation and an equivalence relation \(E\) whose classes are these inner copies; every edge between two classes is oriented as the corresponding quotient edge. For a finite, pointwise named substructure \(A\), let \(t_r(A)\) be the number of complete types of ordered \(r\)-tuples of **pairwise distinct points outside** \(A\). Write \(\lambda(A)=(m_1,\ldots,m_k)\) for the unordered list of positive sizes of the \(E\)-classes meeting \(A\), and \(n=\sum_i m_i\).

**Sharp reconstruction threshold.** For every \(0\le n\le9\), the pair \((t_1(A),t_2(A))\), together with \(n\), uniquely determines \(\lambda(A)\). At \(n=10\) there is exactly one pair of *different class-size partitions* with the same two counts:
\[
\lambda=(1,1,2,2,4),\qquad \mu=(1,1,3,5),
\qquad (t_1,t_2)=(60,4984).
\]
Their ordered three-type counts are respectively \(619552\) and \(616352\). Thus the first failure of two-arity numerical recovery is repaired by arity three.

Moreover, this ambiguity persists at **every** larger base size. For each integer \(t\ge0\), enlarge a common class in each profile and set
\[
\boxed{\lambda_t=(1,1+t,2,2,4),\qquad \mu_t=(1,1+t,3,5),\quad t\ge0.}
\]
For \(q=2^{t+1}\) their exact counts satisfy
\[
\boxed{t_1(\lambda_t)=t_1(\mu_t)=q+58,\qquad
 t_2(\lambda_t)=t_2(\mu_t)=(q+58)^2+q^2+1380,}
\]
while
\[
\boxed{t_3(\lambda_t)-t_3(\mu_t)=3200.}
\]
Hence for every \(n\ge10\) there are different \(E\)-class-size profiles on \(n\) named points indistinguishable by their one- and two-type counts, but distinguished by their three-type counts.

The counts ignore the tournament orientations already present on \(A\); the reconstruction statements concern the **class-size profile**, not the full isomorphism type of \(A\).

## Assumptions and scope
Finite tournaments in the inner and outer factors have arbitrary orientations. The equivalence relation \(E\) is named in the language, and orientations between different \(E\)-classes are constant. The described age amalgamates by making independent consistent orientation choices within old/new classes and between quotient classes; its homogeneous limit has the claimed extension property. Every finite consistent diagram of new, distinct points over a finite base is realized. All counting series below are **formal exponential generating series** and are not asserted to converge analytically away from zero.

For \(m\ge0\), set
\[
B_m(z)=\sum_{a\ge0}2^{ma+\binom a2}\frac{z^a}{a!},\qquad
W(z)=B_0(z)-1.
\]
Then the general exact type spectrum is
\[
\boxed{\sum_{r\ge0}t_r(A)\frac{z^r}{r!}
=\left(\prod_{i=1}^k B_{m_i}(z)\right)
\sum_{s\ge0}\frac{2^{ks+\binom s2}}{s!}W(z)^s.}
\tag{1}
\]
This is a special marked-base instance of familiar wreath-product orbit composition; originality is not claimed for the general composition principle. The claim here is the exact sharp two-arity class-profile cutoff and its persistent, third-arity-separated collision family.

## Proof
**1. Exact extension enumeration.** Assign each new coordinate to one of the \(k\) old \(E\)-classes or to a newly formed \(E\)-class. If \(a\) new labelled coordinates join an old class of size \(m\), there are \(2^{ma+\binom a2}\) choices for their orientations to old members and among themselves. If \(s\) new nonempty classes are formed, there are \(2^{ks+\binom s2}\) choices for quotient orientations involving these classes, and a new class of size \(a\) admits \(2^{\binom a2}\) internal orientations. A set of \(s\) unlabeled new classes is represented by the labelled-set construction with factor \(1/s!\). This gives (1), with no restrictions omitted or double counting. Homogeneity identifies these finite diagrams with complete types.

**2. First three coefficients.** Define
\[
u=2^k,\quad b=\sum_i2^{m_i},\quad c=\sum_i4^{m_i},\quad d=\sum_i8^{m_i}.
\]
Expanding (1) through order three gives
\[
\begin{aligned}
t_1&=u+b,\\
t_2&=(u+b)^2+c+u^2+2u,\\
t_3&=b^3+3bc+4d+3u(b^2+c)
+3b(2u+2u^2)+8u+12u^2+8u^3.
\end{aligned}
\tag{2}
\]
For example, the terms \(b^3+3bc+4d\) enumerate three new coordinates all belonging to old classes: all distinct classes, exactly two in one class, or all three in one class. The remaining terms enumerate one, two, or three new quotient classes.

**3. Exact cutoff through ten points.** Each class-size profile is a nondecreasing partition of \(n\) into positive parts. The recurrence
\[
\mathsf P(N,a)=\bigcup_{j=a}^N \{(j)\mathbin{\|}\pi:\pi\in\mathsf P(N-j,j)\},\qquad
\mathsf P(0,a)=\{()\},
\]
produces each such partition exactly once, where \(\|\) denotes concatenation. Evaluate the first two expressions in (2) on each partition, grouping equal pairs. For \(n=1,2,\ldots,10\), the numbers of partitions are
\[
1,2,3,5,7,11,15,22,30,42,
\]
and the numbers of distinct numerical \((t_1,t_2)\)-signatures are
\[
1,2,3,5,7,11,15,22,30,41.
\]
The only nonsingleton fiber is at \(n=10\), with the two partitions displayed under Finding. The complete 139-row integer certificate `profile_certificate.csv` and its independent generator/checker `verify.py` make this finite exhaustive step reproducible: the recurrence exhausts partitions, and no experimental extrapolation to larger \(n\) is used. Substituting the two partitions into (2) yields \(t_3=619552\) and \(t_3=616352\).

**4. Persistent obstruction.** Let \(\lambda_t=(1,1+t,2,2,4)\), \(\mu_t=(1,1+t,3,5)\), and \(q=2^{t+1}\). For the first profile, \((u,b,c)=(32,q+26,q^2+292)\); for the second, \((u,b,c)=(16,q+42,q^2+1092)\). The first two formulas in (2) immediately give the common expressions displayed above. For the third coefficient, the values of \(d\) are \(q^3+4232\) and \(q^3+33288\). Substitution into the third formula in (2), followed by cancellation of the cubic, quadratic and linear terms in \(q\), leaves exactly \(3200\), independently of \(t\). The profiles have different numbers of classes and hence are distinct. Since both contain \(10+t\) points, this proves the assertion for every \(n\ge10\). \(\square\)

## Verification
The standard-library checker `verify.py` exhausts all partitions for \(1\le n\le10\), matches the entire `profile_certificate.csv` rather than a selection of rows, independently computes the first three coefficients by rational formal-series multiplication, and directly enumerates canonical assignments of new tuple coordinates to old and new classes for the two critical profiles. It additionally tests the all-size family identities at \(0\le t\le19\). Actual output is in `verification_output.txt`. The symbolic proof in Steps 1–4 establishes the infinite family; finite tests do not substitute for it.

## Relationship to prior work
The random tournament, the oligomorphic wreath-product construction and its unmarked orbit-series composition are established background; see Cameron's *Oligomorphic Permutation Groups* (1990) and his account in *Infinite permutation groups* (2007, §4.4). The latter explicitly discusses the imprimitive wreath action and its orbit-series substitution. Our claim does not repackage those results as a new general counting principle. The additional issue here is whether low-arity type counts over **pointwise named finite bases**, conditional on base size, reconstruct the finite equivalence-class partition, and the exact first failure and persistent third-arity separation.

Related finite-base spectra for the countable grid with two equivalence relations and for random-bipartite reducts involve different structures and invariants. Database/search summaries of those related results were considered, but their full texts were not available in the current inspection. Neither summary states a ten-point class-profile collision for the tournament wreath product. The prior literature may contain an equivalent small-parameter census under a different description; historical priority is therefore provisional.

## Limitations
Reconstructing the class-size partition is weaker than reconstructing the full named tournament base: all internal and quotient orientation patterns are invisible to these numerical type counts. The uniqueness statement is exhaustive only for \(n\le10\); beyond that, an explicit collision family is proved, but no classification of all larger fibers is claimed. Counts concern ordered distinct new coordinates and include the named equivalence relation.

## References
1. P. J. Cameron, *Oligomorphic Permutation Groups*, London Mathematical Society Lecture Note Series 152, Cambridge University Press, print publication June 29, 1990. https://www.cambridge.org/core/books/oligomorphic-permutation-groups/6800CDD438C175EB8C077DDAA37CCD2B
2. P. J. Cameron, “Infinite permutation groups,” in *Groups St Andrews 2005*, Cambridge University Press, 2007, §4.4. Accessible text: https://dokumen.pub/groups-st-andrews-2005.html
3. published-finding corpus published research record, “Arity-two saturation and unbounded collisions in finite-base type spectra of the countable grid,” 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-arity-two-saturation-and-unbounded-collisions-in-finite-base-typ--801562567ff1 (comparison by available title and summary only).
4. published-finding corpus published research record, “Marked-base orbit spectra and a sharp single-parameter recovery threshold for random bipartite reducts,” 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-marked-base-orbit-spectra-and-a-sharp-single-parameter-recovery--1ceb9535794d (comparison by available title and summary only).
