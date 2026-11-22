# The complete Hasse–Weil zeta function of a non-liftable characteristic-five Kummer Calabi–Yau threefold

## Finding

For the explicitly defined smooth proper canonical Kummer resolution \(K/\mathbb F_5\) below, every geometric Frobenius eigenvalue on \(H^2_{\acute et}(K_{\overline{\mathbb F}_5},\mathbb Q_\ell)\) is \(5\), and every eigenvalue on \(H^4\) is \(25\). Consequently

\[
Z(K,T)=\frac{1}{(1-T)(1-5T)^{31}(1-25T)^{31}(1-125T)}
\]

and for each integer \(m\ge1\),

\[
\#K(\mathbb F_{5^m})=1+5^{3m}+31(5^m+5^{2m}).
\]

In particular, \(\#K(\mathbb F_5)=1056\). The claim concerns the Frobenius **spectrum** and zeta function, not semisimplicity or a literal scalar endomorphism. The published geometric Betti numbers are antecedents and are not claimed as new.

## Assumptions and scope

Work over \(k=\mathbb F_5\), fix \(\ell\ne5\), and use geometric Frobenius on \(\ell\)-adic cohomology. Let \(S\to\mathbb P^1_k\) be the relatively minimal rational elliptic surface with Weierstrass chart

\[
y^2=4x^3+3t(t+2)^3x+3t^4(t+2)^2.
\]

Its singular fibers are \(\mathrm{III}\) at \(t=0\), \(\mathrm{IV}\) at \(t=3\), and \(\mathrm{I}_5\) at \(t=\infty\). Put \(Y=S\times_{\mathbb P^1} S\), and let \(\iota\) be simultaneous elliptic negation. Following Burek, Chmiel, Cynk and Oczko, choose their \(k\)-defined equivariant smooth proper crepant small algebraic-space resolution \(\widehat Y\to Y\), and define \(K\) to be the smooth proper crepant resolution of \(\widehat Y/\langle\iota\rangle\) given by blowing up the image of the fixed curve. Their Theorem 4.3 and Proposition 5.3 give \(b_2(K)=b_4(K)=31\) and \(b_1=b_3=b_5=0\). This exact model, not arbitrary twists or all crepant models, is the domain of the assertion.

## Proof

**1. Equivariant big resolution.** The cited paper's Lemmas 4.1 and 5.1 construct a projective equivariant big resolution \(B\) whose Betti numbers are \((1,0,43,0,43,0,1)\), and a \(k\)-defined equivariant blowdown \(B=\operatorname{Bl}_{\mathbb P^1}\widehat Y\). The involution is defined over \(k\). Denote its quadratic twist over \(k\) by \(B^{\iota}\): its Frobenius on geometric cohomology is \(\iota\circ\operatorname{Frob}_5\).

**2. Arithmetic of the twisted elliptic fibers.** For \(t=0,1,2,3,4,\infty\), counting the points of the Weierstrass cubics by quadratic characters gives, respectively,

\[
(6,3,4,6,5,7).
\]

The smooth quadratic twists have point counts \(12-n_t\). At the three singular fibers, the cited Lemma 4.1 identifies Frobenius and negation with the **same reflection** of the five-cycle at infinity, and the two nonidentity components of the type-\(\mathrm{IV}\) fiber are exchanged by each. Thus the twisted minimal-fiber point counts, in the same order, are

\[
(11,9,8,16,7,25).
\]

Indeed, the type-\(\mathrm{III}\) fiber has two rational projective lines meeting once, the twisted type-\(\mathrm{IV}\) fiber three rational projective lines meeting at a point, and the twisted type-\(\mathrm{I}_5\) fiber a split cycle of five projective lines. Therefore

\[
\#Y^{\iota}(k)=11^2+9^2+8^2+16^2+7^2+25^2=1196.
\]

**3. Every exceptional correction over \(k\).** At \(\mathrm{IV}\times\mathrm{IV}\), the exceptional smooth cubic is

\[
E:\quad x(x^2-2u^2)-z(z^2-2v^2)=0\ \subset\mathbb P^3,
\]

and negation changes both signs \(u,v\). Its quadratic twist is \(x(x^2-4u^2)-z(z^2-4v^2)=0\). Exhaustive projective enumeration gives \(\#E^{\iota}(k)=51\), replacing one rational point and contributing \(50\). At \(\mathrm{I}_5\times\mathrm{I}_5\), the common Frobenius–negation reflection makes all 25 nodes fixed by twisted Frobenius; each small-resolution exceptional \(\mathbb P^1\) then contributes \(5\). The strict diagonal and graph-of-negation resolutions each contribute another rational projective line and hence \(5\). At the final \(\mathrm{III}\times\mathrm{III}\) node, the big-resolution quadric \(cd=u^2+v^2\) twists to \(cd=2(u^2+v^2)\); both are split, with 36 rational points, giving a replacement correction of \(35\). Thus

\[
\#B^{\iota}(k)=1196+50+25\cdot5+2\cdot5+35=1416.
\]

**4. Maximality determines the entire degree-two spectrum.** Choose an ample class on the projective \(B\) defined over \(k\) and replace it by the sum with its involution pullback; this is again ample, defined over \(k\) and invariant. Hard Lefschetz for this class identifies traces of \(\operatorname{Frob}_5\circ\iota\) on \(H^4(B)\) with five times the traces on \(H^2(B)\). The odd cohomology vanishes, so the Lefschetz trace formula gives

\[
1416=1+5^3+(1+5)\operatorname{Tr}(\operatorname{Frob}_5\circ\iota\mid H^2(B));
\]

hence the trace is \(215=43\cdot5\). Weil purity gives absolute value five for every one of the 43 geometric eigenvalues; equality in the triangle inequality forces every eigenvalue to be the positive real number \(5\). This does not by itself establish semisimplicity. By the equivariant blowup formula, the spectrum of \(\operatorname{Frob}_5\circ\iota\) on \(H^2(\widehat Y)\) is likewise entirely \(5\). Since \(\iota\) acts trivially on its own invariant subspace, ordinary Frobenius has eigenvalue \(5\) on \(H^2(\widehat Y)^\iota\).

**5. The quotient and its seven fixed curves.** The source's Lemma 5.2 proves that \(C=\operatorname{Fix}(\iota|\widehat Y)\) consists of seven disjoint smooth rational curves: five horizontal components with explicit rational equations/parametrizations and two exceptional vertical lines. These are all defined over \(k\), so \(\operatorname{Frob}_5\) acts by one on \(H^0(C)\). The source's Lemma 2.3 supplies a Galois-equivariant direct sum

\[
H^2(K)\simeq H^2(\widehat Y)^\iota\oplus H^0(C)(-1).
\]

The second summand has seven eigenvalues \(5\); the first has \(31-7=24\), all equal to \(5\). Poincaré duality and the vanishing of odd cohomology then give 31 eigenvalues \(25\) in degree four, eigenvalues \(1\) in degree zero and \(125\) in degree six. The stated zeta function and all-extension point counts follow.

**Independent first-field consistency.** Counting the untwisted fibers and exceptional loci similarly gives \(\#B(k)=336\). Blowing up the invariant rational center \(\mathbb P^1\) adds \(5(5+1)=30\) points in either twist, so \(\#\widehat Y(k)=306\) and \(\#\widehat Y^\iota(k)=1386\). The quotient point count is their average \(846\), by tame invariant cohomology. Finally the seven rational fixed curves each contribute \(5(5+1)\) under the transverse blowup, giving \(846+210=1056\).

## Verification

The accompanying `checker.py` counts the six Weierstrass fibers over \(\mathbb F_5\) by exact quadratic characters, independently enumerates the untwisted and twisted cubic and quadric projective points, checks all 25 combinatorial node orbits, and checks the final trace and first-field identities. Its successful exact-arithmetic output is `PASS`, with \(31\) and \(51\) cubic points, \(36\) and \(36\) quadric points, and \(336\), \(1416\) points on the respective big-resolution forms. The infinite-extension statement uses the cohomological proof, not finite enumeration. The quoted Betti and local-resolution theorems are independently inspected inputs from the cited primary preprint.

## Relationship to prior work

Earlier calculations already establish the resolved self-product degree-two Frobenius spectrum (positive five with multiplicity 24, negative five with multiplicity 18), and the two exceptional cubic point counts 31 and 51. They do not give the joint action of Frobenius and involution, nor the zeta function of the Kummer quotient.

Burek–Chmiel–Cynk–Oczko (2026), Theorem 4.3, Lemmas 4.1, 5.1, 5.2, 2.3 and Proposition 5.3, provide the characteristic-five model, the equivariant resolutions, fixed curves, and cohomological dimensions, but do not evaluate its \(\mathbb F_5\)-Frobenius spectrum or Hasse–Weil zeta function. Their published extension-field counts at 25 and 625 are input checks, not substitutes for the new twisted \(\mathbb F_5\) count. Burek (2023/2024) studies zeta functions of a different Kummer family formed from triple products of elliptic curves and finite linear groups. Burek–Cynk (2026) develop resolution and Euler-characteristic methods; their abstract was accessible but a full-text comparison could not be completed. The latter remains a historical-priority qualification. Record searches for this particular self-product, its involution-twist point count and the zeta factors did not identify equivalent coverage.

## Limitations

The theorem determines the canonical smooth proper crepant resolution \(K\) attached to the equivariant small resolution specified above. It does not assert semisimplicity, a scalar Frobenius endomorphism, or the zeta function of every other birational projective model without an additional arithmetic comparison. The algebraic-space to projective-model comparison in the source establishes Betti numbers but does not automatically give isomorphic Frobenius representations. Full text of one plausible antecedent was unavailable; research novelty is therefore best-knowledge, not certified historical uniqueness. The source preprint is recent and not independently refereed in this report.

## References

1. D. Burek, T. Chmiel, S. Cynk, and M. Oczko, *A projective Calabi–Yau threefold in characteristic 5 non-liftable to characteristic 0*, arXiv:2611.15943v1 (2026), https://arxiv.org/html/2611.15943v1, especially §§4–5.
2. D. Burek and S. Cynk, *Crepant resolutions of fiber products and Kummer fibrations of rational elliptic surfaces with non-reduced fibers*, arXiv:2609.12522v1 (2026), https://arxiv.org/abs/2609.12522.
3. D. Burek, *Zeta function of some Kummer Calabi–Yau 3-folds*, arXiv:2112.03970 (2023 version), https://arxiv.org/pdf/2112.03970.
