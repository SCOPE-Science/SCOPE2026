# Sharp sink-polynomial root transitions in clique bouquets

## Finding

For integers \(r\ge3\) and \(a_1,\ldots,a_r\ge1\), let
\[
G(\mathbf a)=K_1\vee\left(K_{a_1}\sqcup\cdots\sqcup K_{a_r}\right),\qquad C=\prod_{i=1}^r a_i!.
\]
Each clique is joined to the same hub vertex, and the peripheral cliques have no edges between them. Let \(S_G(z)=\sum_{\mathcal O}z^{s(\mathcal O)}\), where \(\mathcal O\) ranges over all acyclic orientations and \(s(\mathcal O)\) is the number of vertices of outdegree zero. Let \(e_j=e_j(a_1,\ldots,a_r)\) be the elementary symmetric polynomial, with \(e_0=1\). Then the **entire sink polynomial** is
\[
\boxed{S_G(z)=C\left[\prod_{i=1}^r(1+a_i z)+z-1\right]=Cz\left[(1+e_1)+e_2z+\cdots+e_rz^{r-1}\right].}
\]
All \(r\) positive coefficients are strictly log-concave: writing \(S_G(z)=\sum_{j=1}^{r}c_jz^j\),
\[
\boxed{c_j^2>c_{j-1}c_{j+1}\quad(2\le j\le r-1).}
\]
For **exactly three peripheral clique blocks**, let \((a_1,a_2,a_3)=(a,b,c)\). The sink polynomial is real-rooted **if and only if**
\[
\boxed{(ab+ac+bc)^2\ge4abc(1+a+b+c).}
\]
Equivalently the complete sharp real-rootedness boundary is
\[
\boxed{a^2(b-c)^2-2abc(b+c+2)+b^2c^2\ge0.}
\]
For fixed unequal block sizes \(b\ne c\), the boundary has two explicit endpoints
\[
\alpha_- = \frac{bc}{(\sqrt{b+1}+\sqrt{c+1})^2},\qquad
\alpha_+ = \frac{bc}{(\sqrt{b+1}-\sqrt{c+1})^2}.
\]
It is real-rooted exactly when \(a\le\alpha_-\) or \(a\ge\alpha_+\), and is nonreal-rooted for every \(\alpha_-<a<\alpha_+\). Thus **real-rootedness can disappear and then reappear** as one block grows: with \(b=5,c=6\), it holds for positive integers exactly at \(a=1\) and \(a\ge779\), but not at \(2\le a\le778\).

If the two blocks of sizes \(b=c=k\) agree, this specializes to the sharp integer transition
\[
\boxed{a\le\left\lfloor\frac{k^2}{4(k+1)}\right\rfloor.}
\]
Thus \((a,b,c)=(1,5,5)\) is real-rooted whereas \((2,5,5)\) is not. Both graphs have induced claws. For homogeneous bouquets \(a_1=\cdots=a_r=a\), the polynomial has exactly one real root, namely zero, when \(r\ge3\) is odd; it has exactly two distinct real roots (zero and one negative root) when \(r\ge4\) is even. In particular every such homogeneous bouquet with \(r\ge3\) has nonreal zeros despite its strictly log-concave coefficient sequence.

## Assumptions and scope

Graphs are finite, simple, undirected, and have labeled vertices. Each \(a_i\) is the number of *peripheral* vertices in clique block \(i\); the complete block including the common hub has \(a_i+1\) vertices. Different blocks intersect in the hub and nowhere else. A sink has outdegree zero. One acyclic orientation is counted once, independent of the number of topological orderings of its directed graph. The coefficient classification applies to all \(r\ge3\), while the discriminant and re-entrant phase classifications apply precisely to \(r=3\), and the homogeneous-root count to all homogeneous \(r\ge3\).

## Proof

**Block independence.** Every undirected simple cycle in a clique bouquet lies entirely inside one of the complete blocks: a simple cycle crossing two blocks would have to visit the unique common hub twice. Therefore an orientation of the entire graph is acyclic exactly when each block is oriented acyclically. An acyclic orientation of a clique is a transitive tournament, with a unique sink and a unique corresponding total order. Thus the \(i\)-th block has \((a_i+1)!\) acyclic orientations. Of these, \(a_i!\) put the hub last, and \(a_i a_i!\) put one of the \(a_i\) peripheral vertices last.

A peripheral vertex can be a global sink only when it is its block sink, because it has no edges outside that block. The hub is a global sink if and only if it is the sink in *every* block. Let a formal variable \(z\) mark a peripheral sink in each block. Independence of the block orientations yields the product \(C\prod_i(1+a_i z)\). Its constant term \(C\) counts precisely the orientations in which all blocks have the hub as their sink; each such orientation has one global sink (the hub) rather than zero. Replacing this contribution by \(Cz\) proves the displayed all-coefficient identity. In particular \(S_G(1)=\prod_i(a_i+1)!\), giving the full orientation count.

**Strict log-concavity.** The positive coefficient sequence, after dividing by \(C\), is \((1+e_1,e_2,e_3,\ldots,e_r)\). Newton's inequalities for the elementary symmetric functions of positive \(a_i\) give, for \(2\le j\le r-1\),
\[
\frac{e_j^2}{e_{j-1}e_{j+1}}\ge
\frac{\binom rj^2}{\binom r{j-1}\binom r{j+1}}>1.
\]
This already proves each internal log-concavity inequality beyond the first affected one. For the affected inequality at \(j=2\), Newton gives
\[
 e_2^2\ge\frac{3(r-1)}{2(r-2)}e_1e_3.
\]
Since \(e_1\ge r\ge3\), we have
\[
\left(\frac{3(r-1)}{2(r-2)}-1\right)e_1
=\frac{r+1}{2(r-2)}e_1>1.
\]
Hence \(e_2^2>(1+e_1)e_3\), proving strict log-concavity at the remaining index. (When \(r=3\), this is its only internal index.)

**Sharp three-block real-rootedness.** For \(r=3\), the formula factors as
\[
S_G(z)=Cz\bigl((1+a+b+c)+(ab+ac+bc)z+abc z^2\bigr),
\]
where \(C=a!b!c!>0\). Thus the two nonzero roots are real if and only if the quadratic discriminant
\[
\Delta=(ab+ac+bc)^2-4abc(1+a+b+c)
\]
is nonnegative. Direct expansion yields the equivalent expression in the statement. All quadratic coefficients are positive, so real roots must be strictly negative. With \(b=c=k\),
\[
\Delta=k^2\bigl(k^2-4a(k+1)\bigr),
\]
which proves the exact integer threshold. For unequal \(b,c\), the discriminant quadratic factors as
\[
\Delta=(b-c)^2(a-\alpha_-)(a-\alpha_+),
\]
where the two endpoints are given in the statement. This identity follows by evaluating their sum and product:
\[
\alpha_-+\alpha_+=\frac{2bc(b+c+2)}{(b-c)^2},\qquad
\alpha_-\alpha_+=\frac{b^2c^2}{(b-c)^2}.
\]
For \(b=5,c=6\), the exact quadratic is \(\Delta(a)=a^2-780a+900\): it is positive at \(a=1\), negative at \(a=2\) and \(a=778\), and positive at \(a=779\). Since the quadratic is convex with only two roots, this yields the exact two disjoint integer real-rooted regimes in the statement. For \((a,b,c)=(1,5,5)\), the reduced quadratic is \(12+35z+25z^2\), with discriminant \(25\) and roots \(-3/5,-4/5\). For \((2,5,5)\) it is \(13+45z+50z^2\), whose discriminant is \(-575\). Both graphs contain an induced \(K_{1,3}\), by taking the hub and one vertex from each of the three peripheral cliques.

**Homogeneous-root count.** If all \(a_i=a\), the unscaled sink polynomial is
\[
f(z)=(1+az)^r+z-1,
\]
which has the root \(z=0\). If \(r\ge3\) is odd, then \(f'(z)=ra(1+az)^{r-1}+1>0\) on the real line, giving exactly one real root. If \(r\ge4\) is even, then \(f''(z)=r(r-1)a^2(1+az)^{r-2}\ge0\); its derivative increases from \(-\infty\) to \(+\infty\), so \(f\) decreases once and then increases once. As \(f(z)\to+\infty\) when \(z\to-\infty\), while \(f(0)=0\) and \(f'(0)>0\), there is exactly one additional negative real root. No other real roots exist. Both are simple. Because \(\deg f=r\ge3\), nonreal roots occur in every homogeneous case. This finishes the proof.

## Verification

Run `python3 artifacts/verify.py` from the extracted package root. The standard-library program independently enumerates orientations of the actual graph edges, tests directed acyclicity using topological elimination, and records the outdegree-zero vertices. It compares the resulting coefficients with the theorem for 168 clique-size vectors using at most 14 edges. Further integer calculations test the normalized polynomial and strict log-concavity on 21,824 profiles, the discriminant identity for all triples with sizes from 1 through 44, and the two-equal-block threshold for parameters from 1 through 54, as well as the re-entrant integer phase for block sizes 5 and 6 across 1 through 1000. Expected terminal line: `VERIFY_OK`.

The finite checks corroborate the proof but do not establish unrestricted correctness or independent mathematical certification. The unrestricted statements depend on the displayed bijections, Newton inequalities, discriminant algebra, and derivative arguments.

## Relationship to prior work

Alexandersson and Maia Leite (2026) prove real-rootedness of the acyclic sink polynomial for chordal **claw-free** graphs and give a sink-set expansion for arbitrary graphs. Our clique bouquets are chordal but, for \(r\ge3\), contain an induced claw, so the cited theorem does not cover them. Its general expansion is a starting framework but does not state the coefficient formula, universal strict log-concavity, three-block real-rootedness locus, or homogeneous root count. Hwang and collaborators (2019) develop general acyclic orientation polynomials and their recurrences; Gebhard and Sagan (1999) study unique-sink orientation counts. The current exact family-level boundary and coefficient conclusions are not supplied by those stated results. A relevant previously published result concerning sink distributions of crown graphs treats a different graph family; clique bouquets are not matching-deleted complete bipartite graphs.

## Limitations

The three-parameter discriminant criterion and two-regime phase boundaries are only an all-parameter real-rootedness characterization for *three* peripheral blocks. For arbitrary heterogeneous \(r\ge4\), the polynomial is determined, but its complete real-rootedness region is not classified. Graphs with more complicated block-intersection trees are not covered. The claim of historical priority is provisional because unindexed earlier graph-specific work could contain an equivalent specialization. Independent mathematical audit has not been performed.

## References

1. P. Alexandersson and L. Saud Maia Leite, "Sink polynomials of line graphs and weighted matching polynomials", arXiv:2610.41502v1, first submitted 2026-10-30, Sections 1–3, especially Proposition 2.4 and Theorem 3.1. https://arxiv.org/abs/2610.41502
2. B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh and S.-H. Yu, "Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions", arXiv:1910.10920, 2019, Definition 2.1 and Theorem 3.10. https://arxiv.org/abs/1910.10920
3. D. D. Gebhard and B. E. Sagan, "Sinks in Acyclic Orientations of Graphs", arXiv:math/9907078, 1999, Theorems 1.1–1.2. https://arxiv.org/abs/math/9907078
