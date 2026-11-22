# Uniform reduced Weierstrass support and Frobenius descent on Bring's genus-four curve

## Finding

Let \(k=\mathbb F_q\) have characteristic \(p\ge 7\). Let \(B/k\) be the smooth projective complete intersection in \(\mathbb P^4_k\)
\[
\sum_{i=1}^5 X_i=\sum_{i=1}^5 X_i^2=\sum_{i=1}^5 X_i^3=0.
\]
Its canonical Weierstrass divisor \(W\) is **reduced of degree \(60\)**, and every geometric point has the same canonical vanishing sequence \((0,1,2,4)\) (Weierstrass gap sequence \((1,2,3,5)\)). Precisely, \(W\) is the disjoint union, over the ten unordered index pairs \(\{i,j\}\), of the six points obtained by putting \(X_i=X_j=1\) and assigning the three distinct roots of
\[
h(U)=U^3+2U^2+3U+4
\]
in all six orders to the remaining three coordinates.

Write \(r_q=\#\{u\in\mathbb F_q:h(u)=0\}\). The discriminant of \(h\) is \(-200\), so \(r_q\in\{0,1,3\}\). The *complete* Frobenius cycle profile of \(W\), including every extension-field point count and the finite-scheme zeta function, is

| \(r_q\) | Polynomial type over \(\mathbb F_q\) | Frobenius cycles | \(Z(W,T)\) |
|---|---|---|---|
| \(3\) | \((1)(1)(1)\) | \(1^{60}\) | \((1-T)^{-60}\) |
| \(1\) | \((1)(2)\) | \(2^{30}\) | \((1-T^2)^{-30}\) |
| \(0\) | \((3)\) | \(3^{20}\) | \((1-T^3)^{-20}\) |

In particular, the number of rational Weierstrass points is **either \(60\) or \(0\)**; in the latter case all points first split over the quadratic or cubic extension. This includes the prime-field examples \(p=7\) (\(2^{30}\)), \(p=11\) (\(3^{20}\)), and \(p=43\) (\(1^{60}\)). The assertion is about Weierstrass points of the *curve*, not all rational points of the curve.

## Assumptions and scope

The characteristic restriction \(p\ge 7\) is essential to the proof: \(2\), \(3\), \(5\) must be invertible, \(h\) must be separable and the canonical degree \(6\) must be smaller than \(p\). The standard power-sum model is fixed; the result makes no claim about arbitrary twists. The ordinary derivative Wronskian here agrees with the canonical ramification divisor because the canonical system is classical in the specified characteristics.

## Proof

**(1) Smooth canonical model.** Eliminate \(\sum X_i=0\) to see \(B\) as a complete intersection of a quadric and a cubic in \(\mathbb P^3\). If a point were singular, the gradients of the three power sums in five coordinates would be linearly dependent. Since \(2,3\) are invertible, a nonzero polynomial of degree at most two would vanish at all five coordinate values. Thus the values would take at most two distinct values, say \(u,v\), with multiplicities \(m,5-m\), where \(1\le m\le4\). The first two power-sum equations imply \(m(5-m)(u-v)^2=0\). Since \(p\ge7\), this forces \(u=v\), and then \(5u=0\), an impossible projective point. If all five coordinates were equal initially the same argument applies. Hence \(B\) is smooth. Adjunction gives \(K_B\cong\mathcal O_B(1)\), \(\deg K_B=6\), and \(g(B)=4\).

**(2) Ten disjoint sextets.** For a fixed pair, say \(X_1=X_2=a\), the remaining values \(b,c,d\) satisfy \(2a+b+c+d=2a^2+b^2+c^2+d^2=2a^3+b^3+c^3+d^3=0\). If \(a=0\), Newton identities force \(b=c=d=0\), so normalize \(a=1\). Newton identities give the elementary symmetric functions \(b+c+d=-2\), \(bc+bd+cd=3\), \(bcd=-4\), hence \(b,c,d\) are the three roots of \(h\). Direct calculation gives \(\operatorname{disc}(h)=-200\) and \(h(1)=10\). In characteristic at least seven these quantities are nonzero, so the roots are distinct and none equals \(1\). Thus each index pair gives exactly six distinct points, and different pairs give disjoint sets: each point has exactly one equal-coordinate pair. Altogether there are \(10\cdot6=60\) geometric points.

**(3) Each point is Weierstrass.** The involution interchanging \(X_1,X_2\) fixes exactly the six points of that sextet. Its other projective eigenspace, the single point \([1:-1:0:0:0]\), does not lie on \(B\) because \(2\ne0\). Tame Riemann–Hurwitz therefore gives genus one for the quotient. Consequently the invariant and anti-invariant subspaces of \(H^0(B,K_B)\) have dimensions \(1\) and \(3\), respectively. At an isolated fixed point there is a local parameter \(t\) in which the involution sends \(t\mapsto-t\). An invariant holomorphic differential has an odd vanishing order, while an anti-invariant one has an even vanishing order (because \(dt\mapsto-dt\)). An adapted basis of the canonical differentials therefore has three distinct even orders and one odd order. The minimal possible increasing sequence is \((0,1,2,4)\), not the generic \((0,1,2,3)\). Every one of the 60 points has positive Weierstrass weight.

**(4) No further points or multiplicities.** A base-point-free linear series of degree less than \(p\) has the classical generic order sequence: by the \(p\)-adic criterion, a generic order \(j<p\) forces every integer from \(0\) through \(j\) to be an order, since all \(\binom{j}{i}\) are nonzero modulo \(p\). Here the canonical degree is \(6<p\); hence its generic sequence is \((0,1,2,3)\). The canonical Wronskian is a nonzero section of \(K_B^{\otimes10}\) and has total zero degree \(10(2g-2)=60\). The 60 distinct positive-weight points exhaust that degree, so every weight is exactly one, each local order sequence is exactly \((0,1,2,4)\), and the whole Weierstrass divisor is reduced.

**(5) Frobenius cycles.** Frobenius fixes every index pair and permutes the three roots of the separable cubic \(h\). On the set of six *ordered* triples, a nonidentity permutation of the roots acts freely. Thus each sextet consists of six fixed points when \(h\) splits, three two-cycles when \(h\) has one linear and one irreducible quadratic factor, or two three-cycles when \(h\) is irreducible. Multiplying by ten proves the table and the zeta functions. In the non-split cases \(W\) has no rational point even when \(h\) has one rational root, because every point uses all three roots.

## Verification

The standalone program `verify.py` reconstructs \(h\)'s discriminant and the geometric count, independently enumerates the cubic's factor types for every prime \(7\le p<1000\), and performs exact finite-field arithmetic for \(p=7,11,43\), enumerating all 60 candidate points, checking the three defining equations and computing their actual Frobenius cycle partitions. It prints `BRING_WEIERSTRASS_P_GE_7_ORDERED_ROOT_SUPPORT_VERIFIED` on success. These finite computations corroborate, but do not replace, the all-characteristic proof above.

## Relationship to prior work

Edge's 1978 paper establishes the 60 Weierstrass points and transposition planes in characteristic zero. Braden and Disney-Hogg (first posted 2022) give their explicit coordinates in terms of \(h\) for the complex Bring curve. Korchmáros, Lia and Timpanella (first posted 2021) establish the smooth positive-characteristic genus-four model for \(p\ge7\) and describe its automorphisms and arithmetic geometry. The present statement concerns the **entire reduced canonical Weierstrass divisor in every such positive characteristic**, including simplicity, precise gap sequence and complete Frobenius splitting over arbitrary finite extensions. That positive-characteristic ramification assertion is not a formal restatement of the characteristic-zero coordinate formula: specialization of Weierstrass divisors can gain weight or change generic order sequence, so a fresh characteristic-uniform weight and classicality argument is required. A published 2026 tritangent-incidence calculation additionally identifies the characteristic-zero Galois \(S_3\) action on the cubic's root labels. Thus the cubic splitting mechanism is also prior-implied: the genuinely additional conclusion here is that it acts on the **entire weight-one canonical Weierstrass divisor for every \(p\ge7\)**, with no new or higher-weight points under reduction. The cubic coordinates and their characteristic-zero arithmetic interpretation are credited, not claimed as new.

## Limitations

There is no classification of all twists, of small-characteristic models, of the whole-curve zeta function, or of every canonical special-point configuration. The proof uses the standard positive-characteristic \(p\)-adic order criterion and tame Riemann–Hurwitz, as explicitly explained above. The literature comparison cannot rule out a less-visible earlier treatment of the same positive-characteristic specialization. The result has not undergone independent mathematical audit.

## References

- W. L. Edge, *Bring's Curve*, Journal of the London Mathematical Society (2) 18 (1978), 539–545, https://webhomes.maths.ed.ac.uk/cheltsov/edge2014/pdf/1978a.pdf (especially p. 541).
- G. Korchmáros, S. Lia, M. Timpanella, *A generalization of Bring's curve in any characteristic*, arXiv:2112.10886, first public 2021-12-20, https://arxiv.org/abs/2112.10886 (Sections 1–2, 8).
- H. W. Braden, L. Disney-Hogg, *Bring's curve: old and new*, arXiv:2208.13692, first public 2022-08-29, https://arxiv.org/abs/2208.13692 (Proposition 3.3); European Journal of Mathematics (2024), https://doi.org/10.1007/s40879-023-00706-0.
- *The Weierstrass tritangent configuration of Bring's curve is the clique geometry of \(A_{5,3}\)*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-the-weierstrass-tritangent-configuration-of-bring-s-curve-is-the--1b90c8a3b779 (root-label Galois \(S_3\) interpretation in characteristic zero).
- K.-O. Stöhr, J. F. Voloch, *Weierstrass points and curves over finite fields*, Proceedings of the London Mathematical Society (3) 52 (1986), 1–19 (standard classical-order criterion).
