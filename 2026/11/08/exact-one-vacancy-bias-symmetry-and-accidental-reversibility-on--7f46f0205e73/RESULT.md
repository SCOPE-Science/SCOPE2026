# Exact one-vacancy bias symmetry and accidental reversibility on disordered exclusion rings

## Finding

Fix any integer \(L\geq3\), site-departure rates \(a_i>0\) indexed modulo \(L\), and an exclusion process with exactly \(L-1\) particles. At a vacant neighbor, an occupied site \(i\) sends a particle clockwise at rate \(a_i p\) and counterclockwise at rate \(a_i q\), where \(p=(1+\varepsilon)/2\), \(q=(1-\varepsilon)/2\), and \(-1<\varepsilon<1\). The stationary clockwise **particle current per bond** is exactly

\[
 J_L(\varepsilon)=\frac{p^L-q^L}{H_L(p,q)},\quad
 H_L(p,q)=\sum_{k=0}^{L-1}h_k p^kq^{L-1-k},\quad
 h_k=\sum_{i=0}^{L-1}\frac{a_i}{a_{i+k}a_{i+k+1}}.
\]

All denominators are positive. Full bias-reversal symmetry, \(J_L(\varepsilon)=-J_L(-\varepsilon)\) **for every** \(-1<\varepsilon<1\), holds if and only if \(h_k=h_{L-1-k}\) for every \(0\leq k<L\). In particular, every three-site one-vacancy process has this symmetry for arbitrary positive departure rates.

For \(L=4\), put \(\Delta=h_2-h_1\). Then

\[
\Delta=\frac{(a_0-a_2)(a_1-a_3)(a_0+a_2-a_1-a_3)}{a_0a_1a_2a_3}.
\]

Thus the four-site one-vacancy response is exactly odd **if and only if** one of the three displayed numerator factors vanishes. Whenever \(\Delta\ne0\), the even response \(J_4(\varepsilon)+J_4(-\varepsilon)\) has the strict sign of \(-\Delta\) for every \(0<|\varepsilon|<1\), with zero even response at \(\varepsilon\in\{-1,0,1\}\) by continuous extension. The four-site ring is the smallest simple periodic ring exhibiting one-vacancy rectification. A non-reflection-symmetric, all-distinct-rate example of exact bias symmetry is \((a_0,a_1,a_2,a_3)=(1,2,4,3)\), for which

\[
J_4(\varepsilon)=\frac{48\varepsilon(1+\varepsilon^2)}{25(3\varepsilon^2+5)}.
\]

A rectifying example \((1,2,3,4)\) has \(\Delta=-1/3\) and

\[
J_4(\varepsilon)=\frac{12\varepsilon(1+\varepsilon^2)}{\varepsilon^3+20\varepsilon^2-\varepsilon+30}.
\]

## Assumptions and scope

The configuration space is the ring of \(L\geq3\) labeled sites with exactly one vacancy; clocks are independent continuous-time exponential clocks and only exclusion-permitted nearest-neighbor particle jumps occur. Rates \(a_i\) are fixed arbitrary positive real numbers, not sampled or refreshed in time. At \(|\varepsilon|<1\) the finite state chain is irreducible, so its stationary distribution and bond current are unique. The formulas extend continuously to the totally asymmetric endpoints \(\varepsilon=\pm1\); at either endpoint the vacancy still traverses the entire ring and has a unique stationary distribution. The orientation is clockwise increasing site index; \(J_L\) counts particle transfers, not vacancy transfers. No infinite-volume or many-vacancy limit is asserted.

## Proof

**1. Reduction to one vacancy.** If the vacancy is at \(i\), it jumps clockwise to \(i+1\) when the particle at \(i+1\) jumps counterclockwise, at rate \(R_i=q a_{i+1}\). It jumps counterclockwise to \(i-1\) at rate \(S_i=p a_{i-1}\). Put \(A=\prod_{i=0}^{L-1}a_i>0\). This is a nearest-neighbor continuous-time Markov chain on one ring. A clockwise vacancy crossing is a counterclockwise particle crossing, so the respective stationary bond currents are negatives.

**2. Directed spanning trees and the exact normalization.** For a finite irreducible continuous-time Markov chain, the stationary probability of vertex \(i\) is proportional to the sum \(\tau_i\) of directed spanning-tree products rooted at \(i\). On a cycle every tree arises by deleting exactly one undirected edge. If the removed edge is between \(i+k\) and \(i+k+1\), then exactly \(k\) of its directed steps toward root \(i\) are counterclockwise and \(L-1-k\) are clockwise. Products of destination-site factors along the tree give

\[
\tau_i=A a_i\sum_{k=0}^{L-1}\frac{p^k q^{L-1-k}}{a_{i+k}a_{i+k+1}}.
\]

This identity remains valid when the root is adjacent to the removed edge: all destination factors but the other endpoint occur once, agreeing with the same expression. Consequently \(\sum_i\tau_i=A H_L(p,q)\). The standard unicyclic flux identity, obtained by substituting these tree weights into \(R_i\tau_i-S_{i+1}\tau_{i+1}\) and cancelling internal tree terms, is

\[
J_{\mathrm{vac}}=\frac{\prod_i R_i-\prod_i S_i}{\sum_i\tau_i}.
\]

Since \(\prod_i R_i=q^L A\) and \(\prod_i S_i=p^L A\), the asserted \(J_L=-J_{\mathrm{vac}}\) follows. As a second verification, the ordinary one-particle departure-rate ring has stationary weights proportional to \(a_i^{-1}\) and current \((p-q)/(\sum_i a_i^{-1})\), which should **not** be substituted for the one-vacancy chain's destination-rate walk.

**3. Necessary and sufficient general symmetry criterion.** Replacing \(\varepsilon\) by \(-\varepsilon\) interchanges \(p,q\). The numerator \(p^L-q^L\) is odd, and nonzero away from \(\varepsilon=0\). Therefore \(J_L(\varepsilon)=-J_L(-\varepsilon)\) for all biases exactly when \(H_L(p,q)=H_L(q,p)\) for all positive \(p,q\) with \(p+q=1\). The \(L\) polynomials \(p^k(1-p)^{L-1-k}\), \(0\le k<L\), form a basis of the degree-at-most-\(L-1\) polynomials (the Bernstein basis up to nonzero factors). Thus equality is equivalent to the coefficient palindrome \(h_k=h_{L-1-k}\). In every length, \(h_0=h_{L-1}=\sum_i a_i^{-1}\) by cyclic reindexing. At \(L=3\) these are the only distinct edge coefficients, so symmetry always holds. The only other three-site particle sectors are empty, full, and one particle; the last is also exactly odd by the final observation in step 2.

**4. Four-site classification.** For \(L=4\) the only potentially unequal mirror pair is \(h_1,h_2\). Directly expanding the two four-term sums over the common positive denominator \(A\), then collecting differences, gives

\[
A(h_2-h_1)=(a_0-a_2)(a_1-a_3)(a_0+a_2-a_1-a_3).
\]

Set \(\Delta=h_2-h_1\). The denominator asymmetry factors exactly as

\[
 H_4(p,q)-H_4(q,p)=\Delta\,pq(p-q)=\Delta\,pq\varepsilon.
\]

Consequently

\[
J_4(\varepsilon)+J_4(-\varepsilon)
=-\frac{\Delta\,pq\varepsilon^2(p^2+q^2)}{H_4(p,q)H_4(q,p)}.
\]

Its sign is strictly \(-\operatorname{sgn}(\Delta)\) at every nonzero interior bias. For all-distinct rates \((1,2,4,3)\) the alternating sum of opposite-pair rates vanishes, yet no spatial reflection fixes the rate profile; the formula is therefore a genuine nongeometric symmetry. For \((1,2,3,4)\) the factorization gives \(\Delta=-1/3\); substituting the rates into \(H_4\) yields the displayed rational current and a strictly positive even part at all nonzero interior biases. This proves the sharp three-to-four-site threshold in the one-vacancy class.

## Verification

The companion `checker.py` independently constructs the exact full \(L\)-state exclusion generator, solves its stationary equations and evaluates the current, then compares it with the tree formula for several positive rate lists on rings of length three through seven and six rational biases. It also checks the four-site symbolic factor identity, both closed-form examples and the even-response sign. It passes **239 exact symbolic or rational assertions** with Python 3 and SymPy. These finite and symbolic computations corroborate, but do not replace, the all-length spanning-tree and polynomial-basis arguments above.

## Relationship to prior work

Sakai and Akimoto, arXiv:2512.03316v1 (public on 2025-12-03), provide the heterogeneous exclusion model, a general relation between bias-reversal and particle-hole response symmetries, single-particle oddness, and an inversion-correspondence sufficient condition. Their Supplemental Material treats the current and inversion correspondence, but does not give the one-vacancy coefficient-palindrome classification or the four-site additive-cancellation surface. Their conjectural expectation of a quadratic even response when neither a uniform bond-bias ratio nor inversion correspondence holds does not cover the all-distinct exact-symmetry example here; the latter is a boundary to that expectation rather than a challenge to their proven sufficient conditions.

Derrida's 1983 exact drift formula for a general periodic nearest-neighbor walk already covers the underlying unicyclic random-walk current and is **not** claimed as new. The contribution here is its specialization to the exclusion vacancy, the necessary-and-sufficient all-length bias-response criterion, and the fully factorized four-site nongeometric equality and sign classification. A prior finite four-site **two-particle** disordered ring analysis identifies rectification and quadratic-cancellation curves in a different particle-number sector; it does not imply the full one-vacancy criterion or the exact all-bias oddness surface derived here.

## Limitations

This is a stationary finite-volume theorem restricted to exactly one vacancy with site-departure disorder. It does not establish corresponding criteria at intermediate densities or in an infinite system, and it does not claim that all disorder yields rectification. The general periodic-walk current is classical; only the explicitly distinguished coefficient and symmetry structure is proposed as new. Literature discovery cannot exclude an unindexed earlier characterization of the same four-site cancellation surface. Independent mathematical review has not been performed.

## References

1. I. Sakai and T. Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316v1 (2025-12-03), https://arxiv.org/pdf/2512.03316 .
2. B. Derrida, *Velocity and Diffusion Constant of a Periodic One-Dimensional Hopping Model*, Journal of Statistical Physics **31** (1983), 433–450, https://doi.org/10.1007/BF01019492 ; author's copy https://www.lps.ens.fr/~derrida/PAPIERS/1983/jsp1983-vitesse.pdf .
3. G. Lakatos, T. Chou and A. Kolomeisky, *Steady-state properties of a totally asymmetric exclusion process with periodic structure*, Physical Review E **71** (2005), 011103, https://doi.org/10.1103/PhysRevE.71.011103 (related but different periodic TASEP setting).
