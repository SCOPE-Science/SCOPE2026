# Complete proper-degree collision classification for pair-punctured Steiner triple systems

## Finding
Let \(S=(V,\mathcal B)\) be a Steiner triple system of order \(v\ge7\), and let \(a,b\in V\) be distinct. Write \(A_{a,b}=S|_{V\setminus\{a,b\}}\) for the induced partial Steiner triple system on the surviving, individually named points. Let \(E_{a,b}(z)=\sum_k e_k(a,b)z^k\), where \(e_k(a,b)\) counts **labelled induced one-point relational extensions** of \(A_{a,b}\) adding exactly \(k\) new triples through one fresh point. Set \(N=v-3\) and \(d=N/2\).

For **any two** pairs of punctures (possibly in different Steiner triple systems of the same order), if their extension coefficients agree in all proper degrees \(0\le k<d\), then either their entire polynomials agree, or \(N\ge8\) is divisible by four and their old-point cycle graphs have precisely the two profiles
\[
C_N\qquad\text{and}\qquad C_{N/2}\sqcup C_{N/2},
\]
with the spectra differing **only** by \(2z^d\):
\[
E_{\mathrm{two}}(z)-E_{\mathrm{one}}(z)=2z^d.
\]
Thus a single omitted highest-degree count is the **only** possible obstruction to reconstructing the full extension spectrum from its lower-degree coefficients. The theorem classifies the spectral obstruction; it does not claim that every design order admits both cycle profiles.

The obstruction first occurs **within one Steiner triple system** at order \(v=15\), and this lower bound is sharp. An explicit 35-triple design on \(\{1,\ldots,15\}\), given in the verification code, has cycle graph \(C_{12}\) after puncturing \(\{1,2\}\) and \(C_6\sqcup C_6\) after puncturing \(\{3,13\}\). Their labelled one-point extension polynomials are, respectively,
\[
\begin{aligned}
E_{1,2}(z)&=1+12z+54z^2+112z^3+105z^4+36z^5+2z^6,\\
E_{3,13}(z)&=1+12z+54z^2+112z^3+105z^4+36z^5+4z^6.
\end{aligned}
\]
The two induced parameter structures are not isomorphic because their leave graphs have different numbers of connected components. This is a statement about finite relational extension diagrams, **not** about complete types in the functional theory of Steiner quasigroups.

## Assumptions and scope
A Steiner triple system is a finite set with three-element blocks such that every distinct unordered pair lies in exactly one block. The induced deletion retains precisely the blocks fully contained in the surviving point set. An induced one-point extension is a partial Steiner triple system obtained by adjoining one new distinguished point and zero or more triples containing it, adding no block entirely on the old set. Old points are labelled and fixed pointwise; the new point is distinguished. The rank is the number of new triples. A cycle graph refers to the conventional graph for a puncture pair: if \(\{a,b,c\}\) is the unique old block through \(\{a,b\}\), its vertices are \(V\setminus\{a,b,c\}\) and its edges are the pairs belonging to a block through \(a\) or through \(b\), excluding their common block. It is a disjoint union of even cycles of length at least four.

No isomorphism-quotient, functional one-point completion, or higher-arity extension assertion is made. The two compared systems are assumed to have the same order \(v\). The maximal proper degree is \(d-1\), including the constant coefficient; degree \(d\) is the number of maximal matchings of full size (perfect matchings on the nonisolated leave graph).

## Proof
**1. Pair-puncture leave decomposition.** Let \(c\) be the unique third point of the block through \(a,b\). The pair \(\{c,x\}\) is covered in a surviving block for every \(x\notin\{a,b,c\}\): its original completing point cannot be \(a\) or \(b\), since \(\{a,c\}\) and \(\{b,c\}\) already belong to \(\{a,b,c\}\). Hence \(c\) is isolated in the leave of \(A_{a,b}\). For every other surviving \(x\), the old pairs \(\{x,y\}\) whose completing point was \(a\) and \(\{x,z\}\) whose completing point was \(b\) yield exactly two distinct leave edges; they are distinct because the unique block through \(\{a,x\}\) differs from that through \(\{b,x\}\) outside the \(\{a,b,c\}\) block. The two edge sets separately form perfect matchings; alternating their colours proves that the \(N=v-3\) nonisolated vertices form disjoint even cycles of length at least four.

**2. Extension polynomials.** A new triple through a fresh point corresponds to an uncovered pair of old points. Different such triples may not use a common old point, so legal collections are exactly matchings of the leave. The one-to-one rank-preserving identification is classical and is explicitly present in the prior 2026 result cited below. Consequently, if the cycle graph has even component-length multiset \(\{m_1,\ldots,m_r\}\), then
\[
E_{a,b}(z)=\prod_{i=1}^r Q_{m_i}(z),\qquad Q_m(z)=\sum_{k=0}^{m/2}\frac{m}{m-k}\binom{m-k}{k}z^k.
\]
The isolated point does not contribute matching edges. The total of the component lengths equals \(N\).

**3. Triangular recovery of short cycle multiplicities.** Work over the formal power series ring \(\mathbb Q[[z]]\). Let
\[
\lambda_\pm(z)=\frac{1\pm\sqrt{1+4z}}2,\qquad q(z)=\frac{\lambda_-(z)}{\lambda_+(z)}=-z+O(z^2).
\]
The cycle recurrence or its two-state transfer matrix gives \(Q_m(z)=\lambda_+(z)^m+\lambda_-(z)^m\). If \(c_m\) is the multiplicity of cycles of length \(m\), then
\[
\log E(z)-N\log\lambda_+(z)
=\sum_{\substack{m\ge4\\m\ \mathrm{even}}} c_m\log(1+q(z)^m).
\]
For even \(m\), \(\log(1+q(z)^m)=z^m+O(z^{m+1})\). Hence the coefficient of degree \(m\) on the left, after removing the terms for smaller even lengths, is **exactly** \(c_m\). It follows inductively that equality of extension coefficients through degree \(d-1\) forces equality of cycle multiplicities for every even \(m<d\). This is an exact formal-power-series argument, not a numerical extrapolation.

**4. Classifying the remaining cycles.** Remove the common multiset of cycles shorter than \(d\) from both graphs, leaving \(R\) vertices in each. Every remaining cycle has length at least \(d\), while \(R\le N=2d\). If any short cycle was removed, then \(R<2d\), so at most one long cycle remains; its length must equal \(R\), making the complete cycle multisets equal. If no short cycle was removed, a partition of \(N=2d\) into parts each at least \(d\) can be either the single part \(2d\) or two parts \(d,d\). The second is allowed only when \(d\) is even and at least four, because every cycle length is even and at least four. Thus the two prescribed cycle profiles are the only possible *different* profiles.

**5. The exact missing coefficient.** For \(d\) even, set \(A=\lambda_+^d\), \(B=\lambda_-^d\). Since \(\lambda_+\lambda_-=-z\),
\[
Q_d(z)^2-Q_{2d}(z)=(A+B)^2-(A^2+B^2)=2AB=2z^d.
\]
This establishes equality of every proper-degree coefficient and a difference of exactly two at the top degree. The unrestricted full matching polynomial determines the even-cycle partition, a known graph-theoretic fact; the present theorem classifies the strictly weaker proper-degree ambiguity.

**6. Sharp first within-design example.** Admissible nontrivial Steiner orders below 15 are \(v=7,9,13\). Their respective values \(N=v-3\) are \(4,6,10\), none admitting the two possible distinct cycle profiles because \(N\) is not divisible by four with \(N\ge8\). For \(v=15\), the explicitly listed 35 triples in `verify.py` cover all \(\binom{15}{2}=105\) old pairs exactly once. Deleting \(\{1,2\}\) yields one 12-cycle, while deleting \(\{3,13\}\) yields two 6-cycles. The exact polynomial coefficients then follow from Step 2 or directly enumerating matchings. This is an existence certificate at the least admissible order, not an exhaustive classification of all Steiner systems of order 15.

## Verification
The standalone `verify.py` uses only the Python standard library. It (i) confirms all old pairs occur once in the explicit 35-block witness; (ii) constructs leaves independently by scanning surviving blocks, and verifies their degree and cycle structure; (iii) enumerates all matchings independently by a disjoint-edge recursion and compares the resulting coefficient vectors with the cycle-factor product; (iv) processes all 105 puncture pairs of the 15-point witness, with cycle signatures occurring 56, 4, 42 and 3 times for \((12)\), \((4,4,4)\), \((4,8)\), and \((6,6)\); (v) checks the formal-series full-cycle inversion on all those cases and on a 7-, 9-, and 13-point Steiner system; and (vi) enumerates every partition into even cycles of length at least four for each even \(N\le32\), verifying the precise proper-degree classification. The actual command and results are in `VERIFICATION.md` and `verify_output.txt`. Finite checks do **not** replace Steps 1–5, which apply to all eligible orders.

## Relationship to prior work
Grannell, Griggs and Murphy (1999) define precisely these two-puncture cycle graphs, study perfect Steiner triple systems, and identify the single-cycle case. The matching-correspondence and real-rooted polynomial of **all** partial Steiner triple-system one-point diagrams are already established in the published *Real-rooted one-point extension spectra of partial Steiner triple systems* (2026); they are prerequisites, not claimed discoveries. The formula for the matching polynomial of an individual cycle and its quadratic-characteristic recurrence is also classical. The 2008 literature on matchings in regular graphs and Wang's 2021 discussion of matching-unique disjoint unions of cycles already cover full-polynomial reconstruction. None of these full-polynomial facts alone resolves the precise one-coefficient-loss problem, its complete converse, or supplies an explicit same-system sharp 15-point certificate. Related work on unrestricted three-variable logic over once-punctured Steiner triple systems addresses a different invariant.

The retained contribution is the global **proper-degree** collision classification together with the sharp first within-system order and fully displayed witness. Searches for truncated matching-polynomial equivalence, two-puncture extension spectra, and the two cycle profiles in both indexed and primary literature did not reveal a stronger covering statement. Priority remains provisional because not every older graph-theory treatment of near-equivalent matching polynomials could be examined in full.

## Limitations
The claim fixes a pair of punctures, individually labelled old parameters, and finite induced relational extension diagrams. It does not assert complete types of Steiner quasigroups, realization of both profiles at every later admissible order, classification of all Steiner triple systems exhibiting the collision, or isomorphism rigidity of bases having the same complete extension polynomial. The polynomial-level classification is a consequence of classical cycle identities plus a new tailored truncation argument; no new general theorem about graph matching polynomials is claimed. Historical priority and independent mathematical review remain open.

## References
1. M. J. Grannell, T. S. Griggs and J. P. Murphy, *Some New Perfect Steiner Triple Systems*, Journal of Combinatorial Designs 7 (1999), 327–330, DOI 10.1002/(SICI)1520-6610(1999)7:5<327::AID-JCD3>3.0.CO;2-S (first published 29 July 1999).
2. Masood Aryapoor, *The Pasch Configuration and Steiner Triple Systems*, arXiv:1306.1257 (5 June 2013).
3. *Real-rooted one-point extension spectra of partial Steiner triple systems*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-real-rooted-one-point-extension-spectra-of-partial-steiner-tripl--9599713a6632 (previously established finite-diagram/matching correspondence).
4. S. Friedland et al., *On the Number of Matchings in Regular Graphs*, 2008, https://homepages.math.uic.edu/~friedlan/enmat12.1.08.pdf.
5. Xiaoling Wang, *The Number of Matching Equivalent for the Union Graph of Vertices and Cycles*, 2021, https://www.scirp.net/journal/paperinformation?paperid=110069 (recalls known uniqueness of cycle unions by the full matching polynomial).
6. *Three-variable collapse and sharp deletion boundary for finite Steiner triple systems*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-three-variable-collapse-and-sharp-deletion-boundary-for-finite-s--6caaf1b445ef.
