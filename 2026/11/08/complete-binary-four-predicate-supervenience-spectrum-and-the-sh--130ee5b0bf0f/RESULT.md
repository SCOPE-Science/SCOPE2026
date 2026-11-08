# Complete binary four-predicate supervenience spectrum and the sharp six-world boundary

## Finding
Let \(V=\{A,B,C,D\}\). For each nonempty Boolean team \(T\subseteq\{0,1\}^{V}\), let \(\gamma_T\) be its functional-dependence closure operator, defined below. There are exactly **221** distinct functions \(\gamma_T:2^V\to2^V\), and exactly **32** equivalence classes under permutations of the four named predicates.

The least number of distinct worlds needed to realize a given profile has the following **complete distribution** among the 221 labelled profiles:

| Least number of worlds | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| Number of profiles | 1 | 15 | 35 | 67 | 95 | 8 |
| Predicate-renaming classes | 1 | 4 | 6 | 10 | 9 | 2 |

Thus **six worlds suffice for every realizable four-predicate binary supervenience theory, and six are necessary for exactly eight labelled theories**. These eight theories form two predicate-renaming classes of four members each. Representatives have precisely the following nontrivial generating implications:

\[\{B,C,D\}\Rightarrow\{A\},\]

and

\[\{A,B,D\}\Rightarrow\{C\},\quad \{A,C,D\}\Rightarrow\{B\},\quad \{B,C,D\}\Rightarrow\{A\}.\]

Here “generating” means that every other valid implication follows from trivial implications and Armstrong's closure laws. Explicit six-world teams witnessing these two types, in bit-mask notation \(A=1,B=2,C=4,D=8\), are respectively

\[\{1,2,4,6,8,10\}\quad\text{and}\quad\{0,3,5,6,11,12\}.\]

For comparison, of the **2,480** closure operators on a four-element labelled set, only these **221** are realizable by Boolean-valued teams. At three or fewer predicates, the numbers of Boolean-realizable profiles are \(2,5,19\) and the maximum minimum world counts are \(2,3,4\), respectively. Four is the first predicate count at which some realizable dependence theory needs more than one extra world beyond the number of predicates.

## Assumptions and scope
A Boolean world is a valuation \(v:V\to\{0,1\}\). A nonempty team \(T\) is a **set of distinct valuations**; repeated worlds with equal valuations do not change the dependence theory. For \(X,Y\subseteq V\), put

\[X\Rightarrow_T Y\iff\forall v,w\in T\;\bigl(v|_X=w|_X\Longrightarrow v|_Y=w|_Y\bigr).\]

Define \(\gamma_T(X)=\{y\in V:X\Rightarrow_T\{y\}\}\). A profile is this **entire** closure map, not one chosen implication or only its keys. The group \(S_4\) acts by permuting the predicate names, not by replacing dependency theories with arbitrary closure systems.

The semantics is also the singleton-domain restriction of modal global supervenience: take four unary predicate extensions, each either empty or the unique individual at a world, and a root whose set of successor valuations is \(T\). The result concerns **these binary singleton-domain models**, not arbitrary predicate extensions on a larger domain, not all inquisitive formulas, and not independently sampled random teams.

## Proof
**1. Exact difference-set criterion.** Encode each valuation by a four-bit integer. For any team \(T\), let

\[\Delta(T)=\{v\oplus w:v,w\in T,\ v\ne w\}\subseteq\{1,\ldots,15\}.\]

For each mask \(X\subseteq V\), a coordinate \(y\) fails to belong to \(\gamma_T(X)\) if and only if some \(d\in\Delta(T)\) is disjoint from \(X\) and contains \(y\). Hence the exact bit-mask identity is

\[\gamma_T(X)=V\setminus\bigcup_{\substack{d\in\Delta(T)\\d\cap X=\varnothing}}d.\tag{1}\]

This proves directly that the computed object is the **full** implication closure, including empty antecedents and all 16 antecedent sets. It also shows that all profiles satisfy extensivity, monotonicity, and idempotence.

**2. Exhaustive reduction.** For every \(t\in T\), translating all team valuations by \(t\) (bitwise XOR) leaves \(\Delta(T)\), and hence the entire closure map, unchanged. Every nonempty team is therefore equivalent to one containing valuation \(0\). Exactly \(2^{15}=32,768\) teams contain \(0\), obtained by freely choosing any subset of the other fifteen valuations. Formula (1) assigns a deterministic, complete 16-entry closure tuple to each. Because every possible binary team translates to one of these, this is an **exhaustive finite classification**, not a sample.

The standalone `checker.py` enumerates all 32,768 anchored teams, deduplicates their 16-entry closure tuples, and obtains exactly 221. For every closure tuple it tracks the least cardinality of an anchored realizing team; XOR translation does not change that cardinality. The resulting exact histogram is the six-column table in the finding. In particular the maximum minimum size is six, with eight exceptions to a five-world upper bound. Concrete representatives of both exception types are displayed above and are checked to realize precisely the stated closure tuples. The calculation also verifies the smaller-variable profiles \(2,5,19\) and maxima \(2,3,4\).

**3. Independent exhaustion and isomorphisms.** As a separate enumeration, `checker.py` loops through **all** \(2^{16}-1=65,535\) nonempty teams, computing each closure by a second algorithm: for every pair of distinct team rows it marks every antecedent contained in their agreement-coordinate set, and records their disagreement coordinates as nonconsequences. This produces exactly the same set of 221 profiles as (1). This exhaustive agreement test independently checks both the reduction and the difference-based implementation.

A permutation \(\pi\in S_4\) acts by \((\pi\gamma)(\pi X)=\pi(\gamma(X))\). For each of the 221 tuples, the checker constructs all 24 transformed tuples and chooses their lexicographically least encoding. Exactly 32 distinct canonical encodings occur. More explicitly, the numbers of profiles fixed by a representative of the five permutation cycle types \((1,1,1,1)\), \((2,1,1)\), \((2,2)\), \((3,1)\), and \((4)\) are \(221,55,25,14,5\), respectively. Burnside's formula independently gives

\[\frac{221+6(55)+3(25)+8(14)+6(5)}{24}=32.\]

The corresponding minimum-world histogram is \(1,4,6,10,9,2\); in particular the eight profiles needing six worlds have orbit sizes four and four, with the two generating implication patterns listed above.

**4. Comparison with all closure theories.** An arbitrary closure operator on \(V\) is equivalent to its family of fixed points, which contains \(V\) and is closed under intersections. Conversely every such Moore family determines a closure operator by intersection of fixed points containing a given set. Enumerating the \(2^{15}\) families of subsets containing \(V\) and testing pairwise intersection closure gives exactly 2,480. Hence only 221 of the 2,480 unrestricted closure operators are representable by the specified **binary-valued worlds**. This enumeration is separately verified in `checker.py` and the total of 2,480 is independently known in the closure-systems literature.

There is no extrapolation from finitely many cases to a claim about arbitrarily many predicate names: **the theorem is exact for four names and the explicitly checked smaller counts only**.

## Verification
Run `python3 checker.py` using only the Python 3 standard library. A successful run prints `BOOLEAN_FOUR_SUPERVENIENCE_CERTIFICATE_OK` and the exact universe sizes, 221 profiles, 32 classes, 2,480 unconstrained closures, and the six-world maximum. The checker is included in full as a standalone artifact and performs assertions for all counts, both exceptional orbit representatives, the independent agreement enumeration, and the small-variable comparison. The finite universe is exactly exhausted, not randomly sampled.

The exact output in the reviewed execution was:

```text
BOOLEAN_FOUR_SUPERVENIENCE_CERTIFICATE_OK all_nonempty_teams=65535 anchored_teams=32768 realizable_profiles=221 attribute_relabelling_classes=32 arbitrary_closure_systems=2480 worst_case_minimum_worlds=6
```

## Relationship to prior work
Armstrong's functional-dependency axioms and the existence of Armstrong relations are classical. Beeri, Dowd, Fagin and Statman (1984) study their structure and bounds on minimum tuple count and domain size. Their Theorem 6.10 explicitly implies that **some** functional-dependency theories cannot have a zero-one-valued Armstrong relation, making Boolean realizability a genuine restriction. They do not provide this exact **four named binary attributes / 221 closure profiles / 32 renaming classes / sharp six-world classification** in the inspected text. The unconstrained four-set closure-system total 2,480 is also prior literature and is used here only as a benchmark, not claimed as new.

Ciardelli and Conti (first public version June 30, 2026) study labelled sequents for inquisitive first-order modal logic and explain that global supervenience represents functional dependence among predicate extensions across accessible worlds. Their work supplies the contemporary semantic motivation, but develops proof theory rather than an exact finite classification of four singleton-domain predicate-extension profiles. The present contribution is the finite binary-realizability spectrum and its optimal world-size refinement, not the underlying concept of functional dependence or its modal encoding.

## Limitations
The result is limited to four **named** Boolean observables (plus the indicated smaller cases), nonempty finite teams, and equality-of-extension supervenience. It neither determines the corresponding spectrum for five predicates nor covers general multi-individual predicate extensions. Its correctness is reducible to a fully exhaustive finite classification with a transparent independent algorithm, not an infinite-dimensional theorem. A historically prior specialized census of binary database dependence profiles could exist outside the inspected indexed literature; historical uniqueness and independent review have not been established.

## References
1. I. Ciardelli and S. Conti, *Labelled Sequents for Inquisitive First-Order Modal Logic*, first public preprint June 30, 2026, arXiv:2606.31868, DOI:10.4204/EPTCS.447.14. https://arxiv.org/abs/2606.31868
2. C. Beeri, M. Dowd, R. Fagin and R. Statman, *On the Structure of Armstrong Relations for Functional Dependencies*, J. ACM **31** (1984), 30–46. DOI:10.1145/2422.322414.
3. P. Colomb, A. Irlande and O. Raynaud, *Counting of Moore Families for n=7* (2010), DOI:10.1007/978-3-642-11928-6_6. Its introduction records 2,480 Moore families on four elements.
4. A. Berry, E. SanJuan and A. Sigayret, *Generalized Domination in Closure Systems*, Discrete Applied Mathematics **154** (2006), 1064–1084, DOI:10.1016/j.dam.2005.04.009.
