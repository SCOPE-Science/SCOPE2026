# A sharp greedy-failure window for harmonic approval committees on a three-bloc triangle

## Finding

Consider three candidate classes \(A,B,C\), each comprising two distinct and otherwise interchangeable candidates. There are three types of approval ballots: \(x\) units of electorate weight approve all candidates in \(A\cup B\), another \(x\) approve all in \(A\cup C\), and \(y\) approve all in \(B\cup C\), where \(x,y>0\). Exactly four of the six candidates are elected. Ordinary unweighted elections correspond to positive integer \(x,y\).

Proportional Approval Voting (PAV) globally maximizes the harmonic satisfaction score; sequential PAV (seq-PAV) adds, one at a time, a candidate having maximum current marginal harmonic score, allowing **every** tied continuation. Write \((a,b,c)\) for elected counts in the three candidate classes. Define

\[
W=\{(2,1,1)\},\quad V=\{(1,2,1),(1,1,2)\},\quad U=\{(0,2,2)\},\quad r=y/x.
\]

Then the **complete phase diagram**, understood as a set of count vectors and valid under every within-class candidate relabeling, is:

| Weight ratio | All seq-PAV outcomes | All maximizing PAV outcomes |
|---|---|---|
| \(0<r<1\) | \(W\) | \(W\) |
| \(r=1\) | \(W\cup V\) | \(W\cup V\) |
| \(1<r<4/3\) | \(V\) | \(V\) |
| \(r=4/3\) | \(V\) | \(V\cup U\) |
| \(4/3<r<3/2\) | \(V\) | \(U\) |
| \(r=3/2\) | \(V\cup U\) | \(U\) |
| \(r>3/2\) | \(U\) | \(U\) |

Thus **every** tie-breaking path of seq-PAV is suboptimal for PAV if and only if

\[
\boxed{\frac43<\frac yx<\frac32.}
\]

In that open interval the exact PAV score deficit is

\[
\boxed{\operatorname{OPT}_{\mathrm{PAV}}-\operatorname{score}_{\mathrm{seqPAV}}=\frac{3y-4x}{12}>0.}
\]

Among all *positive integer* multiplicities of the three triangle ballot types (not assumed symmetric in this last assertion), **17 voters is the sharp minimum for a tie-break-independent failure**. Up to renaming the triangle classes, the only 17-voter witness has ballot multiplicities \((5,5,7)\). Its two seq-PAV composition outcomes are \((1,2,1)\) and \((1,1,2)\), each scoring \(59/2\), whereas PAV uniquely chooses \((0,2,2)\), scoring \(355/12\), a deficit of \(1/12\). Here “uniquely” concerns the composition: candidate labels within each class can be exchanged.

## Assumptions and scope

There are exactly six different candidate identities in three two-member classes and exactly four committee seats. Every voter approves exactly the two classes named on its ballot, so ballots have four approved candidates. PAV evaluates a committee \(T\) by \(\sum_i H_{|T\cap B_i|}\), with \(H_0=0\) and \(H_j=\sum_{s=1}^j1/s\). Seq-PAV selects the maximum PAV-score increase at each round, never retroactively replacing a selected candidate. The result explicitly includes all ways of resolving ties.

The phase diagram requires the first two ballot multiplicities to be equal to \(x\) and the third to equal \(y\); it extends algebraically to positive real weights. The minimal-electorate assertion instead ranges over *all* positive integer triples of ballot multiplicities, with no equality assumption. The three ballot types form a triangle of pairwise overlaps; permuting the three types and their corresponding candidate classes preserves outcomes.

## Proof

**1. Exact committee comparison.** Let \((a,b,c)\in\{0,1,2\}^3\) with \(a+b+c=4\). All committees with the same counts have the same PAV score,

\[
S(a,b,c)=xH_{a+b}+xH_{a+c}+yH_{b+c}.
\]

There are exactly six possible compositions, falling into the following symmetry classes:

| Class | Count vectors | PAV score |
|---|---|---|
| \(W\) | \((2,1,1)\) | \(11x/3+3y/2\) |
| \(V\) | \((1,2,1),(1,1,2)\) | \(10x/3+11y/6\) |
| \(U\) | \((0,2,2)\) | \(3x+25y/12\) |
| \(Z\) | \((2,2,0),(2,0,2)\) | \(43x/12+3y/2\) |

The class \(Z\) is strictly dominated by \(W\) for \(x>0\), since \(S_W-S_Z=x/12\). The remaining comparisons are

\[
S_V-S_W=(y-x)/3,\qquad S_U-S_V=(3y-4x)/12.
\]

These inequalities give exactly the stated PAV maximizing rows, including both tie boundaries. They also give the exact score deficit in the failure interval.

**2. All greedy paths.** The initial candidate marginal scores are \(2x\) in \(A\) and \(x+y\) in either \(B\) or \(C\). If \(y<x\), greedy therefore starts with \(A\). Its second choice can be the other \(A\) candidate when \(y\le x/2\), or a candidate of \(B\) or \(C\) when \(y\ge x/2\). If the first two choices are \((2,0,0)\), the next two add one each from \(B,C\). If they are \((1,1,0)\), the third choice is a second \(A\) candidate for \(y\le2x/3\), or a first \(C\) candidate for \(y\ge2x/3\); the final choice then respectively completes \((2,1,1)\) by choosing \(C\) or \(A\). In all cases, including both marginal-score equalities, the final count vector belongs to \(W\).

If \(y>x\), the first two greedy choices must come one each from \(B,C\), reaching \((0,1,1)\). At this state the marginal scores of a first \(A\) candidate and a second \(B\) or \(C\) candidate are respectively \(x\) and \(x/2+y/3\). The third choice is \(A\) for \(y<3x/2\), \(B\) or \(C\) for \(y>3x/2\), and all three are tied at equality. After a third \(A\), the last choice is from \(B\) or \(C\), since their marginal score is \((x+y)/3>2x/3\), yielding \(V\). After a second \(B\) (symmetrically \(C\)), the last available \(C\) candidate has marginal score \(x/2+y/4\), exceeding the first \(A\) candidate's \(5x/6\) whenever \(y>4x/3\), as required for this branch. Hence that branch yields \(U\). At \(y=x\), a first-choice tie among all classes leads after three rounds to \((1,1,1)\), followed by any one of the three remaining candidates, giving precisely \(W\cup V\). This exhausts all ties and proves the seq-PAV column.

**3. Sharp integer-electorate cutoff.** For a general positive integer multiplicity triple \((u,v,w)\), the same exact aggregate formula is \(S_{u,v,w}(a,b,c)=uH_{a+b}+vH_{a+c}+wH_{b+c}\). Relabeling the triangle transforms any triple into one with \(1\le u\le v\le w\), without changing either voting rule's optimality relationships. The accompanying exact-arithmetic verifier enumerates every such triple with \(u+v+w\le17\), all six feasible four-seat count vectors, and every maximum-marginal greedy branch at each of the four rounds. There are exactly \(123\) triples with fewer than \(17\) voters; none has greedy and optimal outcome sets disjoint. At \(17\) voters, exactly one of the \(24\) sorted triples has disjoint sets: \((5,5,7)\). The verifier additionally independently constructs all \(15\) four-element committees of the six labeled candidates and repeats PAV and all greedy branches with exact rational voter scores. Because the enumerated domain is finite and exhausted, this proves the *finite* minimum; the analytic phase result, not finite sampling, proves the infinite one-parameter claim. Substitution gives the asserted \(355/12\), \(59/2\), and \(1/12\) values.

## Verification

The independent implementations in `verify_triangle.py` use (i) count-vector scores scaled by \(12\) and (ii) the actual six labeled candidates with `fractions.Fraction` and approval-set intersections. They exactly compare both optimizers and all tie-breaking greedy outcomes for the \(147\) sorted positive integer triples with up to \(17\) voters, verifying the \(123+24\) split. A separate rational-ratio test covers \(2684\) ratios for the analytic phase diagram, including every boundary. Executing the file requires only the Python standard library; its assertions must all succeed. Those computational checks are finite certificates of the cutoff and cross-checks of the algebra; the phase result for all positive reals follows from the preceding proof.

## Relationship to prior work

Harmonic PAV and sequential PAV are classical Thiele rules. Dong and Lederer (2023) give axiomatic characterizations of sequential valuation rules, including seq-PAV, rather than a three-bloc sharp phase/cutoff result. Lackner and Skowron's 2022 open textbook chapter already provides an important **general** PAV–seq-PAV discrepancy with only two committee seats (Example 2.5); the present claim is therefore **not** that this is the first discrepancy of the rules. Its new target is the exact tie-breaking-independent failure region and minimal electorate on a specified pairwise-overlapping three-type, six-candidate, four-seat domain. Janson’s detailed 2016 survey (Sections 4 and 13, including Examples 13.3–13.4) also documents earlier disagreements among Thiele’s optimizing, adding, and eliminating methods, and is credited for that general phenomenon; its examples do not give this exact three-ballot-type, four-seat, two-clone threshold or 17-voter cutoff. Delemazure and coauthors (2022/2023) study the more general party-approval framework, including sequential Thiele rules, but their inspected results concern incentive and representation axioms rather than this exact phase and finite cutoff. The overlap and the finite candidate-class capacities prevent reduction to ordinary disjoint-party apportionment examples.

## Limitations

The analytic phase diagram assumes two equal ballot multiplicities; it does not characterize the unbounded-weight region for arbitrary three distinct multiplicities. The finite minimality result does allow unequal weights but is specific to six candidates in three clone pairs and four seats. A generic PAV–seq-PAV separation is known, and the present theorem does not imply that \(17\) is a minimal electorate in the unrestricted approval-voting domain. Publication priority beyond the inspected sources remains uncertain. The finite certificate is not a formal proof assistant or independent external audit.

## References

1. C. Dong and P. Lederer, *Characterizations of Sequential Valuation Rules*, arXiv:2302.11890v1, first posted 23 February 2023, https://arxiv.org/html/2302.11890v1.
2. M. Lackner and P. Skowron, *Multi-Winner Voting with Approval Preferences*, chapter *Dramatis Personae: ABC Rules*, Springer, online 2022, https://doi.org/10.1007/978-3-031-09016-5_2, particularly Rules 4–5 and Example 2.5.
3. T. Delemazure, T. Demeulemeester, M. Eberl, J. Israel, and P. Lederer, *Strategyproofness and Proportionality in Party-Approval Multiwinner Elections*, arXiv:2211.13567 (2022), https://arxiv.org/abs/2211.13567, preprint https://pruvisto.org/pdfs/papp.pdf.
4. S. Janson, *Phragmén’s and Thiele’s Election Methods*, arXiv:1611.08826v1, first posted 27 November 2016, https://arxiv.org/pdf/1611.08826, especially Sections 4 and 13.
5. The accompanying `verify_triangle.py`, an exact self-contained finite enumeration and direct labeled-committee cross-check.
