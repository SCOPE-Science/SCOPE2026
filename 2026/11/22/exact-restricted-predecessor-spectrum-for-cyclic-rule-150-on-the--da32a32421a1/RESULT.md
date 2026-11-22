# Exact restricted-predecessor spectrum for cyclic Rule 150 on the golden-mean language

## Finding

For every integer \(n\geq1\), let \(X_n\) be the set of indexed circular binary words \(x=(x_i)_{i\in\mathbb Z/n\mathbb Z}\) such that \(x_i x_{i+1}=0\) at every cyclic position (the golden-mean or no-adjacent-one constraint). Observe the *unrestricted* binary output of the synchronous parity rule
\[
F_n(x)_i=x_{i-1}\oplus x_i\oplus x_{i+1},
\]
where \(\oplus\) is addition in \(\mathbb F_2\). Sources are restricted to \(X_n\); observed outputs are **not** required to lie in \(X_n\). All input and output positions are indexed, with no quotient by rotation. At sizes one and two, repeated neighbor indices are used literally.

Let \(c_n(y)=|\{x\in X_n:F_n(x)=y\}|\) be the number of admissible predecessors of an indexed output \(y\in\{0,1\}^n\), and let \(A_{n,j}=|\{y:c_n(y)=j\}|\). Let \(L_n\) be the Lucas number, initialized by \(L_0=2,L_1=1\) and \(L_{n+2}=L_{n+1}+L_n\).

**Theorem (complete positive restricted-fiber spectrum).** If \(3\nmid n\), then
\[
A_{n,1}=L_n,\qquad A_{n,j}=0\quad(j\geq2).
\]
If \(n=3k\), \(k\geq1\), then
\[
\boxed{A_{n,3}=1,\qquad A_{n,2}=3\cdot2^{k-1}-3,\qquad A_{n,1}=L_n-3\cdot2^k+3,\qquad A_{n,j}=0\ (j\geq4).}
\]
The unique output with three admissible predecessors is \(y=1^n\), and its predecessors are precisely the three rotations of \((100)^k\) by zero, one or two sites. Consequently, the total number \(R_n\) of distinct attainable outputs is
\[
\boxed{R_n=\begin{cases}L_n,&3\nmid n,\\ L_n-3\cdot2^{n/3-1}+1,&3\mid n.\end{cases}}
\]
For the uniform source on \(X_n\), the exact probability of unique recovery equals \(A_{n,1}/L_n\); this is one when \(3\nmid n\) and is \(1-(3\cdot2^{n/3}-3)/L_n\) when \(3\mid n\). In particular, it approaches one exponentially with \(n\), despite the full-shift Rule 150 map having four labeled preimages when \(3\mid n\).

## Assumptions and scope

This is a single-update, synchronous, radius-one binary cellular-automaton observation of a finite *cyclic* run-length-limited source. A source with a one next to the position obtained by wrapping around is excluded, as is any nonzero one-cell source. The inverse-fiber count concerns the number of distinct original *indexed* configurations, not the number of formal inverse walks, not the number of necklaces, and not the number of deletion or substitution patterns. A full-shift output may contain adjacent ones. Normalization of the Rule 150 update is the displayed three-term XOR; both neighbors are evaluated modulo \(n\), even when indices coincide.

## Proof

**Step 1: exact linear collision kernel.** Suppose \(F_n(x)=F_n(x')\), and write \(d=x\oplus x'\). Then \(d_{i+1}=d_i\oplus d_{i-1}\) for every \(i\), so any infinite solution repeats a block of the form \((a,b,a\oplus b)\). The cyclic boundary condition forces \(d=0\) if \(3\nmid n\). If \(n=3k\), the kernel consists of the zero word and the three nonzero words with repeating blocks \(011\), \(101\), and \(110\). This computation is valid also for sizes one and two, because the recurrence uses the repeated-neighbor convention. When \(3\nmid n\), no distinct permitted sources collide.

**Step 2: classify admissible pairs for each nonzero difference.** Fix \(n=3k\) and the kernel difference \(d=(110)^k\). An admissible pair \(x,x\oplus d\in X_n\) must have opposite bits at the first two sites of each three-site block: if they were equal, one of the two sources would have adjacent ones there. Its third bit must be zero: that bit is not flipped, but it touches flipped bits on both sides across block boundaries, and a one would cause an adjacent-one pair in one of the sources. Conversely every independent choice of \(100\) or \(010\) for each three-site block meets both cyclic no-adjacent-one constraints. Hence exactly \(2^k\) source words \(x\) have \(x\oplus(110)^k\in X_n\), producing \(2^{k-1}\) unordered colliding pairs for that difference. Rotation of the argument gives the same result for each of the three nonzero kernel differences. The full collision graph therefore has \(3\cdot2^{k-1}\) unordered edges.

**Step 3: the only triple fiber.** A word that admits two different nonzero kernel shifts must belong to two of the three prescribed two-block-choice sets from Step 2. For differences \((110)^k\) and \((101)^k\), their intersection consists only of \(x=(100)^k\): the first condition permits the blocks \(100,010\), whereas the second permits \(100,001\). Cyclic shifts give the other two possibilities. Thus the only source words with two nontrivial admissible partners are the three period-three words \((100)^k,(010)^k,(001)^k\). Each produces the all-ones output because every consecutive three-bit window contains exactly one one. They form one fiber of size three. Every other nonsingleton fiber has exactly two members; a size-four fiber is impossible, since every such fiber would have at least one source with two distinct admissible partners outside that unique triple.

**Step 4: solve the exact census.** Every fiber of cardinality \(j\) contributes \(\binom j2\) unordered colliding pairs. Using Step 2 and the unique size-three fiber from Step 3 gives \(A_{n,2}+3=3\cdot2^{k-1}\), hence \(A_{n,2}=3\cdot2^{k-1}-3\) and \(A_{n,3}=1\). The number of cyclic no-adjacent-one words is \(L_n\), since the transfer matrix \(M=\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\) counts legal closed walks and \(|X_n|=\operatorname{tr}(M^n)=L_n\), including the one- and two-cell cases. Therefore \(L_n=A_{n,1}+2A_{n,2}+3A_{n,3}\), yielding the stated singleton census. Summing the positive fiber counts gives the displayed \(R_n\).

**Step 5: recovery probability.** All \(L_n\) allowed source words are equiprobable under a uniform source model. Exactly \(A_{n,1}\) have a unique permitted predecessor. The Lucas identity \(L_n=\varphi^n+\psi^n\), with \(\varphi=(1+\sqrt5)/2\) and \(\psi=(1-\sqrt5)/2\), implies \(2^{n/3}/L_n=O((2^{1/3}/\varphi)^n)\). Since \(2^{1/3}<\varphi\), the nonunique fraction converges to zero exponentially. This proves every assertion.

## Verification

The standalone standard-library script `verify_rule150_hardcore.py` enumerates all allowed indexed circular source words for every ring length from one through twenty-one, applies the actual XOR map, directly constructs all inverse fibers and tests each predicted multiplicity and capacity. It also independently verifies that for each of the three nonzero kernel differences exactly \(2^k\) permitted sources retain the no-adjacent-one constraint after toggling the difference, at every multiple of three in that range. The expected final output is `VERIFY_OK all indexed cyclic inputs n=1..21; kernel-pair counts and fiber spectra`. This is finite evidence; the unbounded theorem rests on the complete combinatorial proof above.

For example, the nonzero histograms \((A_{n,1},A_{n,2},A_{n,3})\) at \(n=3,6,9,12,15,18,21\) respectively are \((1,0,1)\), \((9,3,1)\), \((55,9,1)\), \((277,21,1)\), \((1271,45,1)\), \((5589,93,1)\), and \((24095,189,1)\). These are counts of **outputs**, not of source words.

## Relationship to prior work

Additive Rule 150 is classically studied via polynomial and linear methods; the complete unconstrained indexed preimage kernel (zero or four members) is not new. Dennunzio, Formenti, Grinberg and Margara (2020) establish general algebraic and decision results for additive cellular automata. Frati, Petak and Cheney (first released 2024) investigate networks on *all binary necklaces* for the elementary rules, rather than inverse-fiber sizes for indexed outputs when the input obeys a circular forbidden-factor constraint. A closely related public all-length Rule 150 classification describes the degree of predecessor **necklaces** from unconstrained sources, with positive degrees two or four at multiples of three; its statement neither gives nor entails the present indexed restricted-source multiplicities one, two and three without a separate analysis of the intersection with the no-adjacent-one language. Salo (2022/2023) studies cellular-automaton regularity, including maps on the golden-mean shift, for a different dynamical purpose.

The new claim is the classification of admissible *hard-core* collision pairs and their uniquely exceptional threefold class, the all-length restricted-fiber histogram, and exact distinguishable-output capacity. It does not claim discovery of Rule 150's linear kernel, Lucas enumeration of golden-mean words, or the general concept of restricted coding. Searches and compared texts do not establish absolute literature priority.

## Limitations

No claim is made for nonlinear parity sensors, for other forbidden-factor languages, for more than one update, for finite linear rather than cyclic boundaries, or for output necklaces. The recovery statement assumes the uniform probability distribution on the entire allowed indexed source set. The exact formula is mathematically proved, but identical results may exist under finite-state transducer, constrained linear coding or symbolic-dynamics terminology. No independent mathematical audit has been performed.

## References

1. L. Frati, C. Petak and N. Cheney, *Networks of Binary Necklaces Induced by Elementary Cellular Automata Rules*, first publicly released 2024-09-07, arXiv:2409.04780. https://arxiv.org/abs/2409.04780
2. A. Dennunzio, E. Formenti, D. Grinberg and L. Margara, *From Linear to Additive Cellular Automata*, ICALP 2020, DOI:10.4230/LIPIcs.ICALP.2020.125. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.125
3. V. Salo, *On von Neumann regularity of cellular automata*, arXiv:2209.13373. https://arxiv.org/abs/2209.13373
4. O. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic properties of cellular automata*, Commun. Math. Phys. 93 (1984), 219–258, DOI:10.1007/BF01223745. https://doi.org/10.1007/BF01223745
