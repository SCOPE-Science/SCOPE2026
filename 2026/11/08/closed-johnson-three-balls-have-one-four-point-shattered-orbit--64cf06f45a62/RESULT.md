# Closed Johnson-three balls have one four-point shattered orbit

## Finding
For every integer \(n\ge3\), let \(J(n,3)\) be the Johnson graph on the three-element subsets of \([n]\). The concept class is **exactly** its inclusive radius-one balls
\[
\mathcal B_n=\bigl\{B_C:C\in\tbinom{[n]}3\bigr\},\qquad
B_C=\bigl\{Q\in\tbinom{[n]}3:|Q\cap C|\ge2\bigr\}.
\]
No empty, open-only, or other-radius concepts are added. A query is a three-set \(Q\), answered by whether \(Q\in B_C\).

**Exact maximum stratum.** A four-element query support \(S\) is VC-shattered by \(\mathcal B_n\) if and only if it consists of
\[
S=\bigl\{\{v,a,c\},\{v,a,d\},\{v,b,e\},\{v,b,f\}\bigr\},
\]
where the seven symbols \(v,a,b,c,d,e,f\) are all distinct. Thus all shattered four-supports constitute one isomorphism orbit, and their exact number is
\[
s_4(n)=\begin{cases}
0,&3\le n\le6,\\
 n\binom{n-1}{2}\binom{n-3}{2}\binom{n-5}{2},&n\ge7.
\end{cases}
\]
In particular, \(s_4(7)=630\), \(s_4(8)=5040\), and \(s_4(9)=22680\). The corresponding exact VC dimensions are
\[
\operatorname{VCdim}(\mathcal B_n)=
\begin{cases}
0,&n=3,4,\\
2,&n=5,\\
3,&n=6,\\
4,&n\ge7.
\end{cases}
\]

## Assumptions and scope
All objects are finite, undirected, and simple. The Johnson adjacency is intersection of size exactly two; the inclusive closed ball also contains its center, making membership equivalent to intersection of size **at least** two. A support is shattered if its traces under the stated ball family give all binary labelings. The formula counts unordered supports, not labelings or centers. The computationally finite classification used below is converted into an all-\(n\) assertion by an explicit finite-pattern stabilization lemma, rather than extrapolation from small graphs.

## Proof
**1. Five-point upper bound.** Two query triples with intersection of size one have exactly four common positive centers: if the triples are \(\{z,a,b\}\) and \(\{z,c,d\}\), a center positive on both must be \(\{z,x,y\}\) with \(x\in\{a,b\}\), \(y\in\{c,d\}\). Two disjoint query triples have no common center. In a shattered five-support, every pair must have at least eight common positive centers, one for each labeling of the remaining three queries. Consequently every two distinct query triples must intersect in exactly two symbols. A pairwise-intersecting-in-two family of at least five distinct triples necessarily has a fixed common pair: take two triples \(\{a,b,c\}\), \(\{a,b,d\}\); any triple outside the \(\{a,b\}\)-star belongs to the four triples of the top \(\binom{\{a,b,c,d\}}3\), and a family containing such a top element has size at most four. Thus a hypothetical shattered five-support is \(\{\{a,b,x_i\}:1\le i\le5\}\). A center containing both \(a,b\) has all five positive labels; a center not containing both has at most two of them. The labeling with exactly three positives is impossible. No five-support is shattered.

**2. Finite-pattern stabilization.** A four-support comprises four distinct triples and therefore involves at most twelve ground symbols. Its trace at an arbitrary center \(C\) depends only on \(C\)'s intersection with these symbols. Any center involves at most three additional outside symbols, so an ambient set of fifteen symbols realizes all possible center-trace patterns of **every** four-support type. Enlarging the ambient ground set never destroys an existing shattered support. Consequently classification of all four-triple isomorphism types on fifteen symbols proves the global classification: supports on smaller universes cannot introduce new types, and for universes of size at least fifteen the trace patterns have stabilized.

**3. Exhaustive four-triple type lemma.** The attached standalone `check.py` is also a finite proof certificate. It starts with the first triple \(\{0,1,2\}\), then adds a second, third and fourth distinct triple. In each extension it allows any old symbols together with at most three new, consecutively numbered symbols. Every four-triple hypergraph can be relabeled by first occurrence to appear in this list. The complete isomorphism invariant used for deduplication is the count of ground vertices with each of the fifteen nonzero four-bit incidence patterns, minimized under all twenty-four permutations of the four query triples. These counts characterize isomorphism because vertices having the same incidence pattern are interchangeable. The enumeration produces respectively \(7\), \(151\), and \(6328\) rooted enumerator states after two, three, and four triples, and exactly **66** unrooted four-triple isomorphism types. For each type, the checker enumerates all \(\binom{15}{3}\) possible centers and computes the complete sixteen-bit trace set. Exactly **one** type attains all sixteen labels, represented by
\[
\{\{0,1,2\},\{0,1,3\},\{0,4,5\},\{0,4,6\}\}.
\]
The checker separately verifies that this representative already realizes all sixteen labelings on seven symbols. The combination of type exhaustiveness and stabilization proves the if-and-only-if assertion for every \(n\).

**4. Exact coefficient.** The four supports in the displayed unique type have a unique common symbol \(v\); after removing it, their other symbols have degree pattern \(2,2,1,1,1,1\). Thus their two repeated partners \(a,b\) and the unordered two-element leaf sets attached to each are uniquely determined (apart from interchange of \(a,b\)). Choose \(v\) in \(n\) ways, the unordered pair \(\{a,b\}\) in \(\binom{n-1}{2}\) ways, then choose two distinct leaves for a canonically ordered first partner and two from the remainder for the second. This gives \(n\binom{n-1}{2}\binom{n-3}{2}\binom{n-5}{2}\) supports, without overcounting. Seven distinct ground symbols are necessary.

**5. Low-parameter boundary.** For \(n=3,4\), all inclusive radius-one balls are identical and full, so no singleton is shattered. For \(n=5\), the pair \(\{\{0,1,2\},\{0,1,3\}\}\) is shattered; an exhaustive 3-support check reduces by vertex transitivity to the seven points in one fixed closed neighborhood, finding no shattered triple. For \(n=6\), the three queries \(\{0,1,2\},\{0,1,3\},\{0,1,4\}\) are shattered; the four-support classification excludes any shattered quadruple because it requires seven symbols. For \(n\ge7\), the classified four-support exists and the five-point obstruction proves maximality.

## Verification
Run `python3 check.py` in the package directory, using standard Python only. The script checks the type generator, exact incidence-signature quotient, stable traces on fifteen symbols, uniqueness and an explicit seven-symbol witness, and independent fixed-ball enumerations for \(n=5,6,7,8,9\). It verifies the coefficient for \(n=7,8,9\). Successful output is preserved verbatim in `check_output.txt` and ends with `JOHNSON_3_CLOSED_BALL_FOUR_SUPPORT_PASS`. The analytic five-support obstruction, stabilization argument, and counting proof establish the unrestricted assertions; the program's finite loops are a complete certificate for the finite type lemma, not a heuristic sample of arbitrarily large graphs.

## Relationship to prior work
Adler, Benediktsson and Macpherson (first arXiv version 2020-07-31) determine the VC dimension of **open** Johnson neighborhoods (edge relation) and prove that it is at most four generally; they say boundedness follows for **closed** neighborhoods, but do not classify the latter's four-supports or give the above coefficient and sharp \(n=7\) threshold. Their displayed open-neighborhood example on \(J(6,3)\) shatters four queries, whereas the inclusive closed-ball class there has VC dimension three. Coudert, Csikós, Ducoffe and Viennot (first arXiv version 2024-05-13) study computational graph VC dimension with the inclusive closed-neighborhood convention, but do not state this Johnson-three family classification. The distinction between adjacency and inclusive intersection at least two is essential; neither of the cited open-neighborhood claims implies the support orbit law established here.

## Limitations
This result does not classify shattered supports of sizes one through three beyond the stated small-parameter checks, and does not compute Littlestone dimension or extend the support-orbit theorem to Johnson rank other than three. The finite type computation is proof-critical: it must be run or independently verified to substantiate the complete four-support classification. Publication priority beyond the two primary sources and identified comparisons has not been exhaustively certified. No independent mathematical audit has been performed.

## References
1. I. Adler, B. G. Benediktsson, and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1, publicly posted 2020-07-31; *Discrete Applied Mathematics* 312 (2022), 29–44. https://arxiv.org/abs/2007.16042
2. D. Coudert, M. Csikós, G. Ducoffe, and L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588v1, publicly posted 2024-05-13; SEA 2024. https://arxiv.org/abs/2405.07588
