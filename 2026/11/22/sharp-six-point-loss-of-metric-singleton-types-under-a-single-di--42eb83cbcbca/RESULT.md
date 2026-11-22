# Sharp six-point loss of metric singleton types under a single distance elongation

## Finding

Let \(\mathbb U_3\) be the countable universal homogeneous metric space with positive distances \(\{1,2,3\}\). For a finite nonempty metric parameter space \(A\) with these distances, name every point and write \(N(A)\) for the number of complete **nonalgebraic singleton types** over those parameters. Let \(a,b\) be distinct points of \(A\) with \(d_A(a,b)=1\), and suppose that changing only their mutual distance to \(3\) produces another metric \(A^+\). Write \(\Delta(A;a,b)=N(A^+)-N(A)\).

**Sharp finite threshold.** For every switchable pair on \(2\le |A|\le5\) points, \(\Delta(A;a,b)>0\); the exact smallest changes at orders \(2,3,4,5\) are \(1,2,2,2\). At six points there are exactly \(24\) labelled metrics with \(a=0,b=1\) and \(\Delta<0\), out of \(401476\) labelled switchable metrics with that fixed distinguished pair. Every one has \(\Delta=-2\). There are exactly \(96\) ties and \(401356\) strict increases. The \(24\) strict decreases form three pointed-isometry classes, of labelled sizes \(6,12,6\). They are precisely the six-point instances of the family below, with each satellite shore of size two.

**All-order two-shore law.** Partition the parameter set as \(\{a,b\}\sqcup X\sqcup Y\), where \(|X|=p\ge1\) and \(|Y|=q\ge1\). Set
\[
\begin{gathered}
d(a,b)=1,\qquad d(a,x)=1,\quad d(b,x)=2\quad(x\in X),\\
d(a,y)=2,\quad d(b,y)=1\quad(y\in Y),\qquad d(x,y)=1\quad(x\in X,y\in Y).
\end{gathered}
\]
Choose every remaining internal distance within \(X\) or \(Y\) independently from \(\{1,2\}\). Both the indicated space and the one obtained by setting \(d(a,b)=3\) are metrics. The exact change is independent of all internal choices and equals
\[
\boxed{\Delta(A;a,b)=2-(2^p-2)(2^q-2).}
\]
Consequently it is negative precisely when \(p\ge2\) and \(q\ge2\). In particular, for every \(n\ge6\) there is an \(n\)-point example with \(p=2\), \(q=n-4\), for which
\[
\boxed{N(A^+)-N(A)=6-2^{n-3}<0.}
\]
Thus raising one old distance from one to three, while preserving all triangle inequalities, can **strictly reduce** the number of complete nonalgebraic one-point types. The loss can increase exponentially with the number of named parameters.

## Assumptions and scope

The language has one binary relation naming each possible positive distance; all parameters are named pointwise. The finite metric spaces involved are arbitrary \(\{1,2,3\}\)-metrics, rather than just subspaces of a fixed geometric embedding. Every such finite metric embeds into \(\mathbb U_3\). Each valid map \(f:A\to\{1,2,3\}\), interpreted as prospective distances from a new point, determines exactly one nonalgebraic type by ultrahomogeneity. The algebraic types corresponding to the named old points are excluded; including them would add \(|A|\) to both sides and not affect \(\Delta\).

The phrase *six-point classification* fixes the ordered pair \((a,b)=(0,1)\). Isometry classes are taken under permutations preserving the unordered distinguished pair. The claim that the three pointed-isometry classes have \(6,12,6\) labelled presentations applies with this fixed pair; it is not a count over all possible marked pairs in an unlabelled metric.

## Proof

**1. Exact admissibility and defect identity.** The triangle inequalities for a new point with distance vector \(f\) are
\[
|f(u)-f(v)|\le d(u,v)\le f(u)+f(v)
\qquad(u\ne v\in A).
\]
For old distance \(1\) they forbid exactly the ordered label pairs \((1,3),(3,1)\); distance \(2\) imposes no restriction; distance \(3\) forbids exactly \((1,1)\). It follows that, if \(C_{ij}\) denotes the number of distance-label assignments to \(A\setminus\{a,b\}\) that satisfy all unchanged constraints and give labels \(i,j\) to \(a,b\), the exact cancellation identity is
\[
\boxed{\Delta(A;a,b)=C_{13}+C_{31}-C_{11}.}
\]
Here the three counts impose all constraints other than the constraint on \(\{a,b\}\). In the full old metric, \((1,1)\) is allowed but \((1,3),(3,1)\) are not; in the full new metric the reverse is true. Every other label pair is admitted or forbidden in both metrics in the same way.

An alternative exact total-count identity, useful for independent finite verification, is obtained from the distance-one and distance-three graphs \(G_1(A)\) and \(G_3(A)\). The support \(L=f^{-1}(1)\) must be independent in \(G_3(A)\), and the points allowed to receive label three are exactly those outside \(L\) and outside its open \(G_1\)-neighbourhood. Therefore
\[
N(A)=\sum_{\substack{L\subseteq A\\ L\text{ independent in }G_3(A)}}
2^{|A\setminus(L\cup N_{G_1(A)}(L))|}.
\]
This is proved directly by summing independently over the label-three support once the label-one support is fixed; all other points take label two.

**2. Validity of the two-shore family.** A triangle meeting both \(a,b\) and a satellite point has side lengths \((1,1,2)\) before the switch and \((3,1,2)\) after it. Other triangles have all side lengths in \(\{1,2\}\). Every such triple satisfies the metric triangle inequalities, so both constructions are genuine metrics for every choice of internal shore distances.

**3. Exact two-shore change.** For \((f(a),f(b))=(1,1)\), each satellite has either label one or two, with no additional restrictions, giving \(C_{11}=2^{p+q}\). For \((f(a),f(b))=(1,3)\), each point of \(X\) has label one or two and each point of \(Y\) has label two or three. The only forbidden cross-shore combination is a label-one point of \(X\) with a label-three point of \(Y\), because their old distance is one. There are \((2^p-1)(2^q-1)\) choices with both kinds present. Hence
\[
C_{13}=2^{p+q}-(2^p-1)(2^q-1)=2^p+2^q-1.
\]
By symmetry \(C_{31}=2^p+2^q-1\). Substituting in the defect identity yields the stated factorized expression. For positive integer \(p,q\), the factor \((2^p-2)(2^q-2)\) is zero if either shore has one point and at least four otherwise. This proves the exact sign boundary and the all-order examples.

**4. Exact finite completeness and six-point classification.** The remaining sharpness assertion is a finite exhaustive theorem, proved by the attached `artifacts/verify.cpp`. For each \(n=2,3,4,5,6\), the verifier fixes \(d(0,1)=1\) and traverses **every** one of the \(3^{\binom n2-1}\) assignments of the other distances. It checks all \(\binom n3\) triangles twice (before and after the change). No classification by a guessed graph family is used in candidate generation. For each pair of valid metrics, it evaluates the exact subset formula above for **all** \(2^n\) choices of \(L\), using integer bitsets and no rounding or probabilistic sampling.

Its exhaustive counts are:

| \(n\) | Switchable labelled metrics | \(\Delta>0\) | \(\Delta=0\) | \(\Delta<0\) | Minimum \(\Delta\) |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 0 | 0 | 1 |
| 3 | 6 | 6 | 0 | 0 | 2 |
| 4 | 98 | 98 | 0 | 0 | 2 |
| 5 | 4036 | 4036 | 0 | 0 | 2 |
| 6 | 401476 | 401356 | 96 | 24 | -2 |

For each negative six-point instance, the verifier also checks that the four remaining vertices split into two ordered pairs \(X,Y\) as specified above; all cross distances are one and each internal distance is one or two. Exactly \(6\) such presentations have neither internal distance two, \(12\) have exactly one and \(6\) have both. These are the three pointed-isometry classes because every permutation of the four satellites preserving their two-shore structure acts transitively within each of the three internal patterns, and interchanging \(a,b\) exchanges the shores. This proves both completeness and the classification.

Three explicit representatives, with the fifteen distances listed in lexicographic pair order \((0,1),(0,2),\ldots,(4,5)\), are

| Distance word | \(N(A)\) | \(N(A^+)\) |
|---|---:|---:|
| `111222211111111` | 139 | 137 |
| `111222211111112` | 145 | 143 |
| `111222211211112` | 151 | 149 |

Their counts are checked again independently by `artifacts/verify.py`, which directly tests all \(3^6\) distance-label vectors rather than using the subset formula. It also confirms \((C_{11},C_{13},C_{31})=(16,7,7)\) for all three representatives. The separate analytic two-shore calculation proves the infinite family without extrapolating from this finite enumeration.

## Verification

`artifacts/verify.cpp` is a standalone C++17 exact exhaustive verifier; compile and run with `g++ -O2 -std=c++17 artifacts/verify.cpp -o verify && ./verify`. The output is recorded in `artifacts/verified_output.txt`. The independent Python 3 checker runs with `python3 artifacts/verify.py` and uses direct vector enumeration instead of the bitset independent-support method. Both were run on the actual packaged source files and printed `VERIFY_OK`.

The finite claim of **all** switchable metric pairs through six points is justified by the explicit ternary encoding of every unspecified pair, complete triangle validity tests, and the exact finite support enumeration. Enumeration by itself proves no statement for seven or more points; the all-order assertion is instead established analytically in Proof part 3.

## Relationship to prior work

Sauer's 2011 preprint, subsequently published in 2013, establishes the general Urysohn distance-set setting, realizes Katětov functions and gives the defining triangle inequalities. Those facts are prerequisites and are not claimed as new. A previous published enumeration identifying certain \(\{1,2\}\)-parameter metrics with Widom–Rowlinson partition functions gives an exact model for bases having no old distance-three pairs. Its full statement and proof concern that graph-metric slice; the present deformation compares it with a base containing a distance-three pair and supplies the exact change, strict sign reversal, complete first-boundary census and all-order sign law. General support enumerators and classical homomorphism formulas are acknowledged as prior tools.

Earlier calculations for equilateral, capped-cycle, capped-tree and disconnected parameter metrics likewise address other fixed bases or distance changes; they do not assert this sharp one-to-three perturbation classification. Indexed search results and directly inspected literature did not reveal an earlier theorem implying this specific all-order sign law or sharp six-point classification. This is a best-knowledge historical comparison, not a claim of independently established absolute priority.

## Limitations

The sharp no-decrease bound is proved only through five named parameters; the classification of **all** negative instances is proved only at six. The infinite family supplies examples at larger orders but does not classify them. The result concerns discrete distances exactly \(1,2,3\), complete nonalgebraic *singleton* types over pointwise named finite parameters, and a single metric-preserving elongation from \(1\) to \(3\). It does not assert monotonicity or a first threshold for different distance alphabets, simultaneous changes or higher-arity types. The six-point classification is computer-exhaustive and reproducible; a different direct-vector implementation checks the three canonical representatives. No claim of a complete higher-order census or settled historical priority is made.

## References

1. N. W. Sauer, *Distance sets of universal and Urysohn metric spaces*, arXiv:1107.4794, first submitted 2011-07-24, https://arxiv.org/abs/1107.4794. See especially the section on type functions, restricted Katětov functions and extension realizability. Published as *Distance Sets of Urysohn Metric Spaces*, *Canadian Journal of Mathematics* **65** (2013), 222–240, doi:10.4153/CJM-2012-022-4.
2. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, published finding, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989. The \(\{1,2\}\)-graph-metric identity and local three-label constraint table are prior results.
