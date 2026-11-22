# Equivariant Picard characters of the \(W_{15}\) K3 tail

## Finding
Let \(k=\mathbb C\), and let \(f,g\) be very general weighted-homogeneous sextics in \(\mathbb C[\tau,\alpha,\beta]\) with weights \((1,2,3)\). Let
\[
Y=\{u^2=f(\tau,\alpha,\beta),\ v^2=g(\tau,\alpha,\beta)\}\subset\mathbb P(1,2,3,3,3),
\]
and let \(S\to Y\) be its minimal resolution. Denote by \(a\) and \(b\) the involutions changing the respective signs of \(u\) and \(v\). Then:

1. \(Y\) has exactly four \(A_2\) points and no other singularities; the eight resolution curves are two copies of the regular \(G=(\mathbb Z/2)^2\)-representation on divisor classes.
2. Each of \(a\) and \(b\) fixes exactly one smooth genus-four curve. Their product \(c=ab\) is symplectic and has exactly eight isolated fixed points: six over the intersection of the two branch curves and two over the weight-two orbifold point of \(\mathbb P(1,2,3)\).
3. If \(\chi_{s,t}\) is the rational character with \(\chi_{s,t}(a)=s\) and \(\chi_{s,t}(b)=t\), the full cohomological character is
\[
H^2(S,\mathbb Q)=\mathbf1^{\oplus3}\oplus\chi_{-,+}^{\oplus4}\oplus\chi_{+,-}^{\oplus4}\oplus\chi_{-,-}^{\oplus11}.
\]
4. The geometric Picard number of the very general \(S\) is exactly \(13\), and
\[
\operatorname{NS}(S)\otimes\mathbb Q
=\mathbf1^{\oplus3}\oplus\chi_{-,+}^{\oplus4}\oplus\chi_{+,-}^{\oplus4}\oplus\chi_{-,-}^{\oplus2},\qquad
T(S)\otimes\mathbb Q=\chi_{-,-}^{\oplus9}.
\]
These are rational representation identities, not an integral splitting of the Picard lattice.

## Assumptions and scope
The assertions concern the nonempty Zariski-open set of ordered pairs \((f,g)\) such that each weighted sextic is quasismooth, both avoid the weight-two and weight-three points of \(\mathbb P(1,2,3)\), and their six intersections are simple and avoid the orbifold points. The last two assertions are for a *very general* member of this open set (outside a countable union of proper closed subsets). The group action, cohomology and Picard group are taken over \(\mathbb C\). The corresponding \(W_{15}\) weighted model is introduced in Lee–Scattone–Schaffler, Section 4.4; the degree-six equations and occurrence as an ADE K3 tail are prior work.

## Proof
**1. Quasismoothness and singularities.** The weighted sextic system on \(P=\mathbb P(1,2,3)\) is basepoint free, with seven independent monomials
\(\tau^6,\tau^4\alpha,\tau^2\alpha^2,\alpha^3,\tau^3\beta,\tau\alpha\beta,\beta^2\).
The stated open conditions hold: for example, \(f=\tau^6+\alpha^3+\beta^2\) and \(g=2\tau^6+3\alpha^3+5\beta^2+\tau\alpha\beta\) have six transverse intersections, as seen by the squarefree resultant \(4x^6+x^5+12x^3+x^2+9\) in the affine chart \(\tau=1\); generic Bertini handles individual smoothness. Over the smooth locus of \(P\), the double-double cover is smooth when the branch curves are smooth and transverse. At the weight-two point \([0:1:0]\), the two square-root coordinates are nonzero; the stabilizing \(\mu_2\) acts freely on their four sheets and hence the cover is smooth there. Over \([0:0:1]\) all of \(\beta,u,v\) have weight three, so there are four geometric points \((u/\beta)^2=f(0,0,1)\), \((v/\beta)^2=g(0,0,1)\). The local stabilizer \(\mu_3\) acts on the transverse coordinates \((\tau,\alpha)\) with weights \((1,2)\); each point is therefore a cyclic quotient \(\frac13(1,2)=A_2\). The group \(G\) simply transitively permutes those four points, preserving the two components and order of each exceptional \(A_2\) chain, producing \(2\mathbb Q[G]\) in \(\operatorname{NS}(S)\otimes\mathbb Q\). The resolved surface is K3 by the adjunction formula and crepantness of ADE resolution, as also established in the initiating paper.

**2. Fixed loci.** Let \(B_f=(f=0)\subset P\), \(B_g=(g=0)\). Since \(K_P=\mathcal O_P(-6)\), each is a smooth genus-one anticanonical curve. Their intersection number is \(6\cdot6/(1\cdot2\cdot3)=6\). The fixed curve of \(a\) is \(u=0\), the connected double cover of \(B_f\) branched at those six transverse points, hence has genus four by Riemann–Hurwitz. The same argument applies to \(b\). No other fixed components or points arise: the only nontrivial projective-scaling stabilizers lie over the two orbifold points, and the individual sign changes have no fixed sheet there. None of the four \(A_2\) points is individually fixed by \(a\) or \(b\), hence their resolutions contribute no fixed points. The canonical residue form changes sign under either individual sign change and is invariant under \(c=ab\); therefore \(c\) is symplectic. Its fixed points over the smooth base consist of the six transverse intersections \((u,v)=(0,0)\). At \([0:1:0]\), a weight-two scaling by \(-1\) identifies \((u,v)\) with \((-u,-v)\): the four nominal sheets become two points fixed by \(c\). At the weight-three point \(G\) acts freely on four singular points, so no resolved fixed points occur. These are all the fixed points, giving eight.

**3. Cohomological characters.** For a K3 surface, the topological Lefschetz formula gives \(\operatorname{Tr}(h\mid H^2)=\chi(S^h)-2\). The two genus-four fixed curves yield traces \(-8\) for \(a,b\); the eight isolated points yield trace \(6\) for \(c\); the identity trace is \(22\). The character projector formula gives multiplicities
\[
\frac14(22-8-8+6)=3,\quad
\frac14(22+8-8-6)=4,\quad
\frac14(22-8+8-6)=4,\quad
\frac14(22+8+8+6)=11,
\]
ordered as \((++),(-+),(+-),(--)\). The holomorphic two-form has character \((--)\); consequently all eleven dimensions in the other three character spaces are of pure type \((1,1)\). By the Lefschetz \((1,1)\) theorem, all eleven are rational divisor classes. The two additional \((--)\)-divisor classes arise from the two regular-representation summands of the eight exceptional curves. Hence \(\rho(S)\ge13\).

**4. Exact very-general rank.** The space of ordered branch pairs is an open subset of \(\mathbb P^6\times\mathbb P^6\), of dimension \(12\). The automorphism group of \(P\) has dimension \(5\): graded automorphisms are \(\tau\mapsto A\tau\), \(\alpha\mapsto B\alpha+C\tau^2\), \(\beta\mapsto D\beta+E\tau\alpha+F\tau^3\), with one weighted scalar redundancy. A generic branch pair has finite stabilizer. Therefore the marked family has dimension \(7\). Its map to moduli of quasi-polarized K3 surfaces is generically finite: the pullback \(H\) of \(\mathcal O_P(6)\) is nef and big with \(H^2=24\), and a fixed polarized K3 \((S,H)\) has finite automorphism group; in particular it has only finitely many preserving faithful \(G\)-actions. The quotient by any one such action, together with its two ordered branch divisors, recovers the original pair up to an automorphism of \(P\). Thus the period image has dimension seven. For a seven-dimensional family of polarized complex K3 surfaces, the very-general Picard rank is at most \(20-7=13\) by the local Torelli theorem and the Noether–Lefschetz countability principle. Combined with the preceding lower bound, \(\rho=13\). Only the two exceptional \((--)\) directions can then be algebraic in the \((--)\)-component; the remaining nine form the rational transcendental representation.

## Verification
A standalone exact-arithmetic script `verify_w15_characters.py` checks all seven weighted sextic monomials, the displayed transverse-intersection witness by a squarefree resultant and nonzero discriminant, the weighted intersection and Euler/Lefschetz traces, all four character multiplicities, the eight-curve regular representation, and the seven-dimensional parameter count. These computations verify the finite formulas and nonempty transverse open condition. They do not replace the geometric arguments for generic smoothness, the fixed-point classification, or the period-map argument.

## Relationship to prior work
Lee–Scattone–Schaffler, arXiv:2611.17149v1, Section 4.4, already give the \(W_{15}\) weighted \((6,6)\) ADE K3 complete intersection and rational gluing curve; their Sections 1 and 7 use the symplectic product involution in classifying tails. Iano-Fletcher's classification records this weight system and its \(4A_2\) basket. These are not claimed as discoveries. The distinct additional assertion here is the exact fixed curves and isolated fixed points of the three distinguished involutions, their complete rational cohomology character, and the very-general Picard rank and character splitting. Garbagnati–Penegini's general work on bidouble covers of rational surfaces is related but the accessible abstract does not establish these case-specific invariants; full comparison of its complete text remains a publication-priority risk. Classical Lefschetz, Riemann–Hurwitz, and K3 period theorems are used as established tools.

## Limitations
The Picard-character formula is rational, not integral. The very-general Picard rank is not asserted for every smooth member. The theorem does not calculate the discriminant form of the saturated lattice or the full automorphism group, and no statement of absolute publication priority is made. Complete inspection of older classification material and of the full Garbagnati–Penegini paper remains desirable. The accompanying checker is finite and does not independently verify the Torelli argument.

## References
1. Yongnam Lee, Elisa Scattone, Luca Schaffler, *K3 tails in the KSBA moduli of Kunev surfaces*, arXiv:2611.17149v1 (first public 2026-11-12), especially Sections 4.4 and 7. https://arxiv.org/html/2611.17149v1
2. A. R. Fletcher, *Working with Weighted Complete Intersections*, PhD thesis (1988), classification of codimension-two K3 weights and singularity basket. https://wrap.warwick.ac.uk/id/eprint/106535/1/WRAP_Theses_Fletcher_1988.pdf
3. Alice Garbagnati and Matteo Penegini, *Hodge structures of K3 type of bidouble covers of rational surfaces*, arXiv:2212.11566 (2022), for the general bidouble-cover context. https://arxiv.org/abs/2212.11566
4. V. V. Nikulin, *Finite automorphism groups of Kähler K3 surfaces*, Trans. Moscow Math. Soc. (1980), for background on symplectic involutions.
