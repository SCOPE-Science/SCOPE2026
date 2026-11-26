# Uniform weak-composition law for finite-base tuple types of \(S(3)\)

## Finding

Let \(S(3)\) be the homogeneous countable oriented graph whose vertices are a countable dense subset \(D\subset\mathbb R/\mathbb Z\), with no two vertices separated by an integral multiple of \(1/3\); write \(x\to y\) precisely when \(0<(y-x)\bmod 1<1/3\). For any nonempty individually named finite parameter set \(A\), put \(n=|A|\). The number \(t_r(A)\) of complete types over \(A\) of ordered, pairwise distinct, nonparameter \(r\)-tuples is, for all integers \(r\ge0\),

\[
t_r(A)=3^r r!\binom{n+r-1}{r}=3^r n(n+1)\cdots(n+r-1),
\]

where the empty product at \(r=0\) is one. The entire spectrum depends only on \(n\), not on the induced directed graph on \(A\). More precisely, there is a bijection between complete tuple types and labelled, three-coloured total orders separately placed inside the \(n\) quotient gaps described below. Each weak composition \((c_1,\ldots,c_n)\) of \(r\) receives exactly \(3^r r!\) types. Therefore a uniformly sampled complete type has a uniform quotient-gap occupancy composition, equivalently a symmetric Dirichlet-multinomial law with unit parameters.

## Assumptions and scope

All vertices live on the circle \(\mathbb R/\mathbb Z\); the circle model excludes boundary pairs at displacement \(1/3\) or \(2/3\). The countable dense subset may be taken, for example, as \(D=\{q\alpha\bmod1:q\in\mathbb Q\}\) for any fixed irrational \(\alpha\); then no two distinct points of \(D\) differ by \(1/3\). The parameter elements are individually fixed. New coordinates are distinct from each other and from parameters. Complete types in this homogeneous finite relational structure correspond exactly to induced labelled finite digraph extension diagrams. No metric probability measure on \(D\) is involved.

Let \(q(x)=x\bmod (1/3)\) denote projection to the oriented circle of circumference \(1/3\). The \(n\) distinct points \(q(a)\), with \(a\in A\), cut the quotient circle into \(n\) cyclic gaps, each open and nonempty. The distinction between the three possible lifts of a projected coordinate is understood relative to a fixed starting representative of the quotient circle; a different starting representative relabels all lifts coherently and does not affect the counting.

## Proof

**Step 1: complete unary chambers.** For each named point \(a\), the ternary relation of a new point \(x\) to \(a\) changes exactly at the three circles cuts \(a,a+1/3,a+2/3\). No two of the \(3n\) cuts coincide, because parameter projections are distinct. These cuts partition the original circle into \(3n\) open chambers. Each chamber is a lift of one of the \(n\) quotient gaps. The entire ternary relation vector to \(A\) uniquely identifies its chamber: any one coordinate relation confines \(x\) to one open arc of length \(1/3\), and intersecting these arcs gives precisely one chamber. In particular, there are exactly \(3n\) complete nonalgebraic one-types.

**Step 2: pair relations recover the missing orders.** Suppose two new coordinates \(x,y\) project into the same quotient gap and their corresponding chamber lifts have indices \(i,j\) modulo three. In an oriented local coordinate of the gap, their projected separation \(\delta=q(y)-q(x)\) satisfies \(|\delta|<1/3\). The clockwise separation on the original circle is \((j-i)/3+\delta\) modulo one. The three ternary relation sectors distinguish the two alternatives \(\delta>0\) and \(\delta<0\) for every fixed difference \(j-i\bmod3\): for differences \(0,1,2\), the two relation outcomes respectively are (forward, backward), (nonedge, forward), and (backward, nonedge). Thus, from each coordinate's unary chamber and the binary relation between coordinates, we can recover their projected order inside their common quotient gap. If their quotient gaps are different, the cyclic order of the fixed quotient gaps and the lifted-chamber labels already determine their binary relation. Consequently the collection of individual gap/lift choices and the within-gap labelled orders reconstructs every induced finite digraph extension diagram, and is recoverable from it.

**Step 3: realization and counting.** Every choice of gap assignments, three lifts per coordinate, and strict coordinate order within each chosen gap is realizable: choose points of \(D\) in the prescribed lifted open segments, with projected coordinates in the prescribed strict orders. Countability and density of \(D\) with no exact-third pairs ensure corresponding vertices can be chosen in \(D\). Since \(S(3)\) is homogeneous, isomorphic finite labelled extension diagrams are the same complete type over \(A\).

Fix a weak composition \((c_1,\ldots,c_n)\), with \(c_i\ge0\) and sum \(r\). Choose the \(c_i\) labelled coordinates in each gap in \(r!/\prod_i c_i!\) ways, order those coordinates in \(\prod_i c_i!\) ways, and independently give each of the \(r\) coordinates one of three lifts. The total is exactly \(3^r r!\), independent of the composition. There are \(\binom{n+r-1}{r}\) weak compositions. Multiplication proves the displayed formula and uniform-composition statement.

## Verification

The accompanying standalone \(`verify_s3.py`\) uses exact rational arithmetic and independently enumerates **distinct ternary edge-relation fingerprints** of all relevant finite labelled diagrams for four parameter-base sizes, arities one through three, and two additional three-point bases. To make finite sampling exhaustive for the stated arities, it places at least \(r\) distinct projected sample coordinates in every quotient gap, offers every one of the three lifts, and omits combinations with equal projections (which would represent forbidden exact-third boundary pairs). Every geometrically possible finite chamber/order type of that arity has a representative in this sample. The resulting thirteen comparisons agree with the formula; their precise outputs are recorded in \(`verification_output.txt`\). The infinite result follows from the proof, not these finite checks.

For instance, \(t_2(A)=9n(n+1)\) and \(t_3(A)=27n(n+1)(n+2)\). For \(n=2,r=3\) the four gap occupancies each support \(3^3 3!=162\) types, totalling \(648\).

## Relationship to prior work

The circular realization and homogeneity of \(S(3)\) are established background, not new claims. Bodirsky and Nešetřil, *Constraint Satisfaction with Countable Homogeneous Templates*, §7 (author PDF), describe the graph via oriented angles below \(2\pi/3\) and its relation to Cherlin's classification. Macpherson's *A survey of homogeneous structures*, §2.3, describes the family of homogeneous circular structures and discusses orbit growth elsewhere, but the inspected portions do not give this nonempty marked-base uniform weak-composition law. Hamann, *Countable connected-homogeneous digraphs*, arXiv:1311.6016v1, records the digraph among homogeneous examples; the description is used for classification context, while the precise arc definition is taken from Bodirsky–Nešetřil. General circle-order orbit enumeration motivates the counting, but the three synchronized lifts and conditional uniform occupancy law are the distinguishing ingredients.

## Limitations

The theorem is for the pure oriented graph \(S(3)\), a nonempty pointwise-named base, and ordered injective tuples consisting of new vertices. It does not address unnamed-base orbits, the empty parameter base, coordinates equal to parameters, arbitrary expansions/reducts, or a geometric random-point measure. As with any literature-based novelty assessment, an equivalent prior enumeration under alternate terminology may exist; independent external review has not occurred. The first-day attribution to the initiating 2013 arXiv preprint is not a claim to the earliest historical study of the circular structure, which predates it.

## References

1. M. Bodirsky and J. Nešetřil, *Constraint Satisfaction with Countable Homogeneous Templates*, author-hosted full text, https://iti.mff.cuni.cz/series/2005/244.pdf, §7 (background circle definition and homogeneity).
2. H. D. Macpherson, *A survey of homogeneous structures*, *Discrete Mathematics* 311 (2011), 1599–1634, https://paperzz.com/doc/9426993/a-survey-of-homogeneous-structures, §2.3 (homogeneous circular family).
3. M. Hamann, *Countable connected-homogeneous digraphs*, arXiv:1311.6016v1 (first version 2013-11-23), https://arxiv.org/abs/1311.6016v1 (classification context).
4. G. L. Cherlin, *The classification of countable homogeneous directed graphs and countable homogeneous \(n\)-tournaments*, Memoirs of the AMS 621 (1998), https://doi.org/10.1090/memo/0621 (original classification).
