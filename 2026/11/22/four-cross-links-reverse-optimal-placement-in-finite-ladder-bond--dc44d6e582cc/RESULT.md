# Four cross-links reverse optimal placement in finite ladder bond percolation

## Finding
For independent bond percolation on two parallel finite rails with exactly four selected stochastic cross-links, the layout maximizing opposite-corner connection changes qualitatively with cross-link reliability: with perfect cross-links the three spacings are as equal as possible, whereas at any fixed imperfect cross-link reliability and sufficiently reliable rails the unique best spacings are \(1,L-2,1\). Four is the smallest cross-link count permitting this reversal. A sharp joint high-reliability expansion additionally gives a complete finite-size quadratic optimization and an exact endpoint-clustering threshold.

## Assumptions and scope
Take two vertex-disjoint paths \(P_{L+1}\), labelled top and bottom, with columns \(0,1,\dots,L\), where \(L\ge5\). Every horizontal rail bond is independently open with probability \(p\in(0,1)\). Exactly \(k\) distinct vertical bonds are installed at columns \(0\le s_1<\cdots<s_k\le L\), each independently open with probability \(q\in(0,1]\); no other vertical bonds exist. Let \(R_{L,k}(s;p,q)\) denote the probability that top column \(0\) connects to bottom column \(L\) by open bonds. Optimization is over the \(k\) installed columns, not over post-failure rewiring. All vertices are reliable.

For each nonempty index subset \(S=\{j_1<\dots<j_t\}\subseteq\{1,\dots,k\}\), set \(w(S)=q^t(1-q)^{k-t}\). The exact reliability law is
\[
R_{L,k}(s;p,q)=p^L\sum_{S\ne\varnothing}w(S)\prod_{u=1}^{t-1}\left(2-p^{s_{j_{u+1}}-s_{j_u}}\right).
\]
This includes the empty-product value \(1\) for \(t=1\). For \(k\ge2\) every maximizing configuration has \(s_1=0\) and \(s_k=L\). For \(k=3\), the middle cross-link is at one of the central columns \(\lfloor L/2\rfloor,\lceil L/2\rceil\), for every permitted \(p,q\). For \(k=1\), all columns give the same reliability \(qp^L\).

For \(k=4\), write the strictly positive gaps as \((a,b,c)=(s_2-s_1,s_3-s_2,s_4-s_3)\), with \(a+b+c=L\). The following are exact conclusions:

1. For \(q=1\) and all \(0<p<1\), the optimal triples, and only those triples, have gaps differing by at most one.
2. For every fixed \(0<q<1\), for all \(p<1\) sufficiently close to \(1\), the unique optimal triple is \((1,L-2,1)\).
3. With \(p=1-\varepsilon\), \(q=1-\lambda\varepsilon\) and fixed \(\lambda\ge0\), as \(\varepsilon\downarrow0\) through admissible probabilities,
\[
R_{L,4}=1-\varepsilon^2\bigl(a^2+b^2+c^2+\lambda(a+c)\bigr)+O_{L,\lambda}(\varepsilon^3).
\]
Thus the complete leading-order minimizer is obtained by choosing \(b\in\{1,\dots,L-2\}\) minimizing
\[
\Phi_L(b;\lambda)=b^2+\left\lfloor\frac{L-b}{2}\right\rfloor^2+\left\lceil\frac{L-b}{2}\right\rceil^2+\lambda(L-b),
\]
then choosing \(a,c\) as equal as possible, in either order. The clustered triple \((1,L-2,1)\) is the unique leading-order optimizer precisely when \(\lambda>2L-8\); it ties with \((1,L-3,2)\) and \((2,L-3,1)\) at \(\lambda=2L-8\), and is suboptimal when \(0\le\lambda<2L-8\). At ties, this second-order statement alone does not decide the exact finite-\(\varepsilon\) optimum.

## Proof
**Condition on the open cross-links.** If the open vertical bonds occur at \(s_{j_1}<\cdots<s_{j_t}\), the initial top segment of length \(s_{j_1}\) and final bottom segment of length \(L-s_{j_t}\) must each work. Between successive open bonds separated by \(d\), at least one of the two edge-disjoint length-\(d\) rail segments must work, an event of probability \(2p^d-p^{2d}=p^d(2-p^d)\). The intervals use disjoint bonds, so multiplying and using the telescoping exponent \(L\) proves the displayed formula. An empty set of working cross-links cannot connect the terminals.

**Endpoints and minimality.** Moving the leftmost installed link to column \(0\) strictly increases the factor \(2-p^d\) for every open-link subset containing that link and at least one later link; no other factor decreases. Likewise moving the rightmost link to \(L\). Thus every optimizer with \(k\ge2\) uses both endpoints. For \(k=3\) and endpoints \((0,x,L)\), the only \(x\)-dependent term in \(R/p^L\) is \(-q^2(1+q)(p^x+p^{L-x})\). Strict convexity of \(x\mapsto p^x\) proves the central placement claim. The single-link expression is immediate. Hence no system with fewer than four cross-links exhibits a reversal between endpoint clustering and equal-gap optimization.

**Perfect cross-links.** At \(q=1\), the exact expression is \(R=p^L(2-p^a)(2-p^b)(2-p^c)\). For \(0<p<1\), the real function \(x\mapsto\log(2-p^x)\) has second derivative \(-2p^x(\log p)^2/(2-p^x)^2<0\). Strict integer balancing at fixed sum \(a+b+c=L\) proves the complete perfect-link optimizer set.

**Fixed imperfect cross-links.** For \(p=1-\varepsilon\), each factor is \(2-p^d=1+d\varepsilon+O(\varepsilon^2)\). Summing over independent working links, the coefficient of a gap equals the probability that at least one link works on either side. For four links, the exterior gaps have coefficient \(w_{\rm out}=q[1-(1-q)^3]\), while the central gap has coefficient \(w_{\rm mid}=[1-(1-q)^2]^2\). Their difference is \(w_{\rm mid}-w_{\rm out}=q^2(1-q)>0\). Hence \(R/p^L=1-(1-q)^4+\varepsilon[w_{\rm out}(a+c)+w_{\rm mid}b]+O(\varepsilon^2)\). The unique maximizer of this linear coefficient has \(a=c=1\), \(b=L-2\). There are finitely many layouts, so this is the exact optimizer for all sufficiently small positive \(\varepsilon\).

**Joint nearly ideal bonds.** Under \(p=1-\varepsilon\), \(q=1-\lambda\varepsilon\), with fixed four-link layout including endpoints, connection cannot fail after only one missing edge. To quadratic order the exhaustive failure types are: one failed horizontal bond on each rail in the same gap, giving \(a^2+b^2+c^2\) ordered pairs; or failure of an endpoint cross-link together with one rail bond in its adjacent gap, contributing \(\lambda(a+c)\). Two failed cross-links still leave the terminal path connected if all rail bonds work; an interior cross-link plus a single failed rail bond likewise does not disconnect. Terms involving three or more failures are \(O(\varepsilon^3)\), proving the expansion.

For fixed central gap \(b\), the strictly convex quadratic in \(a,c\) is minimized by near equality, giving \(\Phi_L\). It is discrete convex in \(b\), because \(b^2\) is strictly convex and \(\lfloor t/2\rfloor^2+\lceil t/2\rceil^2\) is convex in integer \(t\). The final two permissible values give \(\Phi_L(L-3;\lambda)-\Phi_L(L-2;\lambda)=\lambda-(2L-8)\). Discrete convexity proves the sharp endpoint-clustering threshold and all tied cases. For any strict leading-order optimizer, finite layout count makes it an exact optimizer for all sufficiently small \(\varepsilon\) away from ties.

## Verification
The supplied standalone Python program \(\texttt{verification/verify_ladder.py}\) uses only the standard library. One implementation conditions on the chosen open cross-links. A separate implementation enumerates all open/closed horizontal and vertical edges and tests two-terminal graph connectivity by union–find. Their exact rational results agree in 42 independent parameter/layout cases with rail lengths \(3,4,5\). Further checks compare 70 small-failure optimizers with the derived quadratic coefficient, test 64 parameter instances around the clustering threshold, and test 24 balanced-versus-clustered and three-cross-link configurations. These checks are finite validation of, not substitutes for, the symbolic proof above.

Run: \(\texttt{python3 verification/verify_ladder.py}\). Expected final line: \(\texttt{PASS}\).

## Relationship to prior work
Tanguy, *Exact solutions for the two- and all-terminal reliabilities of a simple ladder network* (arXiv:cs/0612143, first posted 28 December 2006), gives a general heterogeneous transfer-matrix method. The conditional-link formula here is an elementary specialization of broader reliability methodology; that basic computability is not new. The assessed result is the sharp optimization reversal at four installed cross-links, its minimum-size property, and the coupled-failure layout staircase. Szabó and Valesin (2019), *Inhomogeneous Percolation on Ladder Graphs*, analyze critical thresholds on infinite ladders, a different observable and limit. Other nearby ladder results optimize effective resistance or weighted spanning-tree sums, not two-terminal Bernoulli connection probability. No directly implying placement theorem was found in the material inspected; a general rearrangement theorem in less accessible reliability literature remains a priority risk.

## Limitations
The result concerns only two perfectly reliable rails, independent homogeneous horizontal failures, identical installed-link reliabilities, exactly fixed link count and the specified opposite-corner terminals. It does not determine optimal layouts for arbitrary numbers of links or general series-parallel networks. The coupled-limit threshold describes the quadratic failure coefficient, and does not resolve higher-order tie breaking at \(\lambda=2L-8\). Historical priority is assessed on examined evidence rather than certified by exhaustive literature discovery; independent external validation is not claimed.

## References
- C. Tanguy, *Exact solutions for the two- and all-terminal reliabilities of a simple ladder network*, arXiv:cs/0612143 (first public preprint 2006-12-28), https://arxiv.org/abs/cs/0612143.
- R. Szabó and D. Valesin, *Inhomogeneous Percolation on Ladder Graphs*, *J. Theor. Probab.* 33 (2020), 992–1010; first journal publication 2019-03-29, https://doi.org/10.1007/s10959-019-00896-y.
- F. S. Boland, F. Proschan and Y. L. Tong, *Optimal arrangement of components via pairwise rearrangements*, *Naval Research Logistics* 36 (1989), 807–821, https://doi.org/10.1002/1520-6750(198912)36:6%3C807::AID-NAV3220360606%3E3.0.CO;2-I. Full text not reviewed; cited as possible relevant priority material.
