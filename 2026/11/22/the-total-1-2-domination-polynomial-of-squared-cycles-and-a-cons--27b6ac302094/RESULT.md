# The total \([1,2]\)-domination polynomial of squared cycles and a constant-width optimum exclusion

## Finding
Let \(G_n=C_n^2\) on the labelled vertices \(\mathbb Z/n\mathbb Z\), with \(n\ge5\). A total \([1,2]\)-dominating set \(S\) is a vertex subset such that every vertex (including those in \(S\)) has between one and two neighbors in \(S\). Define the complete cardinality polynomial
\[
P_n(z)=\sum_{\substack{S\subseteq V(G_n)\\1\le |N(v)\cap S|\le2\ \forall v}}z^{|S|}.
\]
For the sixteen binary words \(a b c d\), let \(T(z)\) be the matrix with entries
\[
T_{abcd,bcde}(z)\mathrel{+}=z^e\quad(e\in\{0,1\})
\]
whenever \(1\le a+b+d+e\le2\); all other entries are zero. Then, for every \(n\ge5\),
\[
\boxed{P_n(z)=\operatorname{tr}(T(z)^n).}
\]
This determines the number of feasible configurations at **every** cardinality, not just their minimum. Write \(n=7q+r\), \(0\le r\le6\). The minimum nonzero degree is
\[
\delta_n=2q+\begin{cases}0&r=0,\\1&r=1,2,\\2&r=3,4,5,6.\end{cases}
\]
Its extremal coefficients satisfy
\[
[z^{\delta_n}]P_n(z)=\begin{cases}
7&r=0,\\
(2q-1)n&r=1,\\
n&r=2,\\
2n&r=6.
\end{cases}
\]
Only valid cases with \(n\ge5\) are intended; thus \(q\ge1\) in the first three displayed residue classes. In the structurally distinctive class \(n=7q+1\), precisely \(2n\) of the \((2q+1)n\) ordinary minimum **total** dominating sets fail the extra at-most-two-neighbors condition. All other ordinary optimal configurations in that class remain feasible. The scalar total domination optimum and some ordinary minimum-set counts are antecedent results; the load-capped polynomial and sharp exclusion are the findings here.

## Assumptions and scope
The base cycle is simple, labelled, and has at least five vertices, so its square has four distinct neighbors per vertex, at displacements \(-2,-1,1,2\). There is no independence requirement on \(S\). The upper neighbor-count limit includes selected vertices. Polynomials count labelled vertex subsets, not their dihedral equivalence classes.

## Proof
**1. Exact finite-state enumerator.** Write the selection indicator as a cyclic binary word \((x_i)_{i\in\mathbb Z/n\mathbb Z}\). At site \(i\) its selected-neighbor count is \(x_{i-2}+x_{i-1}+x_{i+1}+x_{i+2}\). A path of \(n\) successive transitions in the sixteen-state fourth-order de Bruijn graph closes exactly when its final four-bit state equals its initial one. It tests precisely these inequalities at every site; a transition appends \(e\) and contributes \(z^e\). For \(n\ge5\), a closed walk uniquely determines the indexed cyclic word, including periods dividing \(n\), and contributes \(z^{\sum_i x_i}\). The trace identity follows without limiting or asymptotic argument.

**2. A sharp lower bound on the support size.** List the \(k=|S|\ge2\) selected vertices in increasing cyclic order and let \(d_1,\ldots,d_k\) be their positive clockwise gaps, summing to \(n\). The weaker ordinary total-domination condition implies: each gap is at most five (else an interior vertex lies at cycle distance at least three from every selected vertex), and no two consecutive gaps are both at least three (else the intervening selected vertex has no selected neighbor). Call gaps at least three *long*. If \(L\) is their number then \(L\le\lfloor k/2\rfloor\), whence
\[
n\le 5L+2(k-L)\le 2k+3\lfloor k/2\rfloor.
\]
The inverse bound yields the stated \(\delta_n\) for the seven residue classes. This condition also characterizes ordinary total domination, since each omitted vertex between consecutive selections is within two of one endpoint when its gap is at most five, and each selected vertex has a selected neighbor when its two adjacent gaps are not both long.

**3. Constructive sharpness under the upper cap.** Let short gaps have length two and long gaps initially have length five, in alternating cyclic order. At residue \(r=0\), use \(q\) copies of \((2,5)\). For \(r=1,2\), use \(q\) such pairs plus one extra short gap, and replace one long five by a four only for \(r=1\). For \(r=3,4,5,6\), use \(q+1\) alternating pairs; replace respectively two long fives by threes, one by three and one by four, one by three, or one by four. These all sum to \(n\) and have the claimed \(\delta_n\) selected vertices. Every selected pair is separated by a gap at least two, so at most two of the four open neighbors of any site can be selected: among three of positions \(-2,-1,1,2\), there is always a pair of adjacent cyclic positions. (For \(n=5\), the same assertion can be checked directly.) Their gaps obey the ordinary total-domination criterion, so all have between one and two selected open neighbors. This proves attainability of the lower bound for every \(n\ge5\).

**4. Optimum multiplicities for residues zero, two, six.** When \(n=7q\), all inequalities in Step 2 are equalities, forcing alternating gap lengths \((2,5)^q\), with precisely seven distinct labelled rotations. When \(n=7q+2\), the unique optimal gap multiset consists of \(q\) long fives and \(q+1\) short twos; the single consecutive short-short junction anchors one distinct optimum at each of the \(n\) vertices. When \(n=7q+6\), there are \(q+1\) long and \(q+1\) short gaps alternating, with exactly one unit of deficit from the all-\((2,5)\) pattern. It may be a long four or a short one. Both choices respect the upper load cap (in particular, the shortened gap of length one has a long gap on either side). The unique defect and its type anchor exactly \(n\) labelled configurations each. Therefore the asserted coefficients are \(7\), \(n\), and \(2n\).

**5. The sharp exclusion at residue one.** Let \(n=7q+1\) and \(k=2q+1\). The gap bound forces exactly \(q\) long gaps, since \(q-1\) long gaps could cover at most \(7q-1\) positions. There are therefore \(q+1\) short gaps, and the unique long-separated cyclic arrangement has one double-short junction. The maximum total gap length with these counts is \(7q+2\); to attain \(7q+1\), **exactly one** gap is shortened by one. Ignoring the upper cap, there are \(q\) choices of a long five becoming four and \(q+1\) choices of a short two becoming one, for \((2q+1)n\) ordinary total-dominating optima: the uniquely doubled short junction supplies a canonical label among the \(n\) vertices.

A long-gap shortening creates no extra adjacency among the selections and is always feasible. Of the short-gap shortenings, precisely the two shorts touching the doubled junction create three selections in open distance-two neighborhood of one vertex. Indeed, the forbidden local short gaps \((1,2)\) or \((2,1)\) put selected vertices at offsets \((-2,-1,1)\) or \((-1,1,2)\) around a site. All remaining short shortenings are isolated between long gaps of length five; no other three selections occupy any four-site open neighborhood. Thus exactly two of the \(2q+1\) defects at each anchored junction are inadmissible. The valid count is \((2q-1)n\), and exactly \(2n\) ordinary optima are excluded. For \(q=1\), the two forbidden shorts exhaust the two short choices, leaving only the long-four case. This completes the proof.

## Verification
The companion program `verify_transfer.py` constructs the exact polynomial by integer weighted walks, verifies the sharp minimum and the stated four coefficient formulas for all \(5\le n\le80\), and checks explicitly constructed minimizers against every neighbor-count condition. A separately implemented adjacency-bitset C++ program `verify_direct.cpp` exhausts all \(2^n\) labelled subsets for each \(5\le n\le21\); it reproduces the same coefficients and totals. `compare_total.py` separately counts unconstrained total-dominating minimum sets through size twenty-one and checks the stated \(2n\) exclusion for the relevant cases. These computations are independent finite consistency checks; Steps 1–5 prove the all-order assertions.

## Relationship to prior work
Chellali and collaborators' 2013 introduction of \([1,2]\)-sets explicitly poses total \([1,2]\)-domination as a variant (Question 14); subsequent general bounds by Lv and Wu do not give this family enumerator. Premala and Sekar (2014) study the **ordinary** total-domination polynomial of the same squared cycles, with no upper limit of two selected neighbors. Earlier specific seven-periodic ordinary total-domination and optimum-exchange classifications are antecedents, not claims here. Ordinary scalar results, ordinary subset counts, and other regular-set classifications do not imply the load-capped cardinality polynomial: already at \(n=8\), the ordinary optimum family has twenty-four configurations but the load-capped family has only eight. At \(n=15\), the respective counts are seventy-five and forty-five. No source inspected here states the all-size load-capped trace enumerator or the universal \(2n\) optimum exclusion.

## Limitations
This is an exact enumerative and structural result for square cycles, not all graph powers or general regular graphs. The transfer formula is finite-dimensional and algorithmic rather than a factored closed rational expression. The four explicit coefficient formulas do not purport to exhaust simplified symbolic formulas for the other three residues; their coefficients remain exactly determined by the trace. Searches and accessible full texts cannot rule out all unindexed historical prior work. No independent scholarly audit has been performed.

## References
1. Chellali et al., *[1,2]-sets in graphs*, Discrete Applied Mathematics 161 (2013), doi:10.1016/j.dam.2013.06.012 (online 28 June 2013), https://doi.org/10.1016/j.dam.2013.06.012.
2. X. Lv and B. Wu, *Total [1,2]-domination in graphs*, arXiv:1503.04939v1 (17 March 2015), https://arxiv.org/abs/1503.04939.
3. T. Premala and C. Sekar, *Total Dominating Sets and Total Domination Polynomials of Square of Cycles*, IOSR Journal of Mathematics 10(4), 78–85 (2014), https://www.iosrjournals.org/iosr-jm/papers/Vol10-issue4/Version-5/M010457885.pdf.
