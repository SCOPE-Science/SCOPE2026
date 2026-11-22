# Lie cohomology realizes the weight enumerators of binary cyclic codes

## Finding
Fix an integer \(d\ge2\). For \(K=\mathbb F_{2^d}\) and an element \(\alpha\in K\) of degree exactly \(d\) over \(\mathbb F_2\), define the \((d+1)\)-dimensional almost-abelian Lie algebra
\[
L_\alpha=\mathbb F_2t\ltimes K,\qquad [t,v]=\alpha v,\quad [v,w]=0\quad(v,w\in K).
\]
Let
\[
C_\alpha=\bigl\{(c_0,\ldots,c_{d-1})\in\mathbb F_2^d:\sum_{i=0}^{d-1}c_i\alpha^{2^i}=0\bigr\}
\]
and write \(W_{C_\alpha}(z)=\sum_{c\in C_\alpha}z^{\mathrm{wt}(c)}\) for its ordinary integer-valued binary Hamming-weight enumerator. Then \(C_\alpha\) is a cyclic code with no nonzero word of weight one or two, and the full trivial-coefficient Chevalley–Eilenberg Betti polynomial is
\[
\boxed{P_{L_\alpha}(z)=\sum_{j=0}^{d+1}\dim_{\mathbb F_2}H^j(L_\alpha;\mathbb F_2)z^j=(1+z)W_{C_\alpha}(z).}
\]
Conversely, **every** binary cyclic code \(C\subseteq\mathbb F_2^d\) whose nonzero words have Hamming weight at least three (including the zero code) is exactly \(C_\alpha\) for some element \(\alpha\) of degree \(d\). Thus the complete set of attainable Betti polynomials for this natural Lie-algebra family is precisely
\[
\bigl\{(1+z)W_C(z): C\text{ a binary cyclic code of length }d,\ \min\mathrm{wt}(C\setminus\{0\})\ge3\bigr\}.
\]
Here the zero code is understood to have infinite minimum distance.

In particular, \(H^2(L_\alpha;\mathbb F_2)=0\) always, and all cohomology groups in degrees at least two vanish **if and only if** \(\alpha\) is a normal basis generator of \(K/\mathbb F_2\). If \(C_\alpha\ne0\) has minimum distance \(\delta\), the first nonzero higher group is \(H^\delta\), with dimension equal to the number of words of weight \(\delta\). Moreover \(\sum_j\dim H^j=2^{1+\dim C_\alpha}\), so total cohomology dimension detects the normal-basis defect.

At degree \(d=3\), taking \(\alpha\) as a root of \(X^3+X+1\) gives \(C_\alpha=\{000,111\}\) and \(P_{L_\alpha}=1+z+z^3+z^4\); a root \(\beta\) of \(X^3+X^2+1\) gives \(C_\beta=0\) and \(P_{L_\beta}=1+z\). Both roots are primitive elements of \(\mathbb F_8\), but their four-dimensional Lie algebras are not isomorphic, since their invertible adjoint operators have different irreducible characteristic polynomials. Thus multiplicative order alone does not determine the cohomology.

## Assumptions and scope
All Lie algebras and cohomology groups are over \(\mathbb F_2\), with **trivial coefficients**; \(d\) is any integer at least two. The Lie algebra has the indicated bracket, which is alternating in characteristic two. Degree exactly \(d\) means \(\mathbb F_2(\alpha)=\mathbb F_{2^d}\). Cohomology means the ordinary alternating Chevalley–Eilenberg complex, not restricted cohomology or cohomology of enveloping algebras. Hamming enumerators count binary codewords with ordinary nonnegative integer coefficients.

## Proof
**1. Two-term Lie differential.** Put \(V=K\) as a \(d\)-dimensional vector space and let \(T:V\to V\) be multiplication by \(\alpha\). Let \(\tau\) be the covector dual to \(t\). For each \(0\le r\le d\), the ordinary exterior cochain space decomposes as
\[
\bigwedge^r L_\alpha^*=\bigwedge^rV^*\oplus \tau\wedge\bigwedge^{r-1}V^*,
\]
with negative and out-of-range exterior powers zero. Direct substitution into the Chevalley–Eilenberg differential shows that the differential of \(\tau\wedge\eta\) is zero, while the differential of \(\omega\in\bigwedge^rV^*\) is \(\tau\wedge D_r\omega\), where \(D_r\) is the derivation of the exterior algebra induced by \(T^*\). (The sign is irrelevant in characteristic two.) Thus
\[
\dim H^r=\dim\ker D_r+\dim\operatorname{coker}D_{r-1}
=\dim\ker D_r+\dim\ker D_{r-1},
\]
because each \(D_r\) is a square matrix. For \(r=0\), \(D_0=0\) on a one-dimensional space.

**2. Diagonalization and binary subset sums.** Over \(K\), multiplication by \(\alpha\) on the separable extension \(K/\mathbb F_2\) has the \(d\) **distinct** eigenvalues
\[
\alpha,\alpha^2,\alpha^{2^2},\ldots,\alpha^{2^{d-1}}.
\]
The induced derivation \(D_r\), *not the multiplicative exterior-power map*, has eigenvalue \(\sum_{i\in S}\alpha^{2^i}\) on the wedge of eigenvectors indexed by an \(r\)-element subset \(S\). Scalar extension preserves rank and nullity. Therefore \(\dim\ker D_r\) is exactly the number of weight-\(r\) vectors in \(C_\alpha\). Summing the preceding dimension identity over \(r\) proves \(P_{L_\alpha}(z)=(1+z)W_{C_\alpha}(z)\).

**3. The cyclic condition and minimum distance.** A cyclic shift of \(c\in C_\alpha\) corresponds to squaring \(\sum c_i\alpha^{2^i}\); the last power returns to \(\alpha\) because \(\alpha^{2^d}=\alpha\). Hence the code is cyclic. No conjugate \(\alpha^{2^i}\) is zero, so there are no weight-one words. A zero sum of two conjugates in characteristic two makes them equal; their equality at distinct positions would contradict degree \(d\). Thus the minimum nonzero weight is at least three.

**4. Every such cyclic code occurs.** Choose a normal basis generator \(\nu\) of the extension, and write \(\sigma(v)=v^2\). The normal-basis theorem gives an isomorphism of \(\mathbb F_2[X]\)-modules
\[
R=\mathbb F_2[X]/(X^d-1)\ \xrightarrow{\ \cong\ }\ K,\qquad h(X)\longmapsto h(\sigma)\nu.
\]
Every binary cyclic code of length \(d\) is an ideal \(C=(g)\) of \(R\), for one monic divisor \(g\mid X^d-1\). Set \(h=(X^d-1)/g\) and \(\alpha=h(\sigma)\nu\). The definition of \(C_\alpha\) identifies its polynomial codewords with the annihilator of \(h\) in \(R\), which equals \((g)\): indeed \((X^d-1)\mid c(X)h(X)\) is equivalent in the polynomial domain to \(g(X)\mid c(X)\). Thus \(C_\alpha=C\). If \(\alpha\) lay in a proper subfield, some two distinct Frobenius conjugates would coincide, and \(C_\alpha\) would have a word of weight two (or \(\alpha=0\), giving weight one). The assumed minimum distance excludes this. Hence \(\alpha\) has degree \(d\), as required. This argument also works when \(X^d-1\) has repeated factors; no semisimplicity assumption is used.

**5. Cohomological consequences.** The zero code has enumerator one; by definition it occurs exactly when the \(d\) Frobenius conjugates are \(\mathbb F_2\)-linearly independent, i.e. when \(\alpha\) is normal. The minimum-weight coefficient and the total Betti sum follow directly from the polynomial identity. The absence of words of weights one and two gives the universal \(H^2\)-vanishing. The two cubics are irreducible; the roots are nonidentity elements of \(\mathbb F_8^\times\), whose order is seven, and the traces of the respective roots are zero and one. In dimension three the only possible nonzero codeword has weight three, proving both listed polynomials. Nonisomorphism follows because the derived ideal of \(L_\alpha\) is the characteristic ideal \(K\); over \(\mathbb F_2\), any Lie-algebra isomorphism must conjugate the multiplication operators, which have different minimal polynomials.

## Verification
The attached standalone `verify.py` constructs multiplication by the generator in polynomial bases of \(\mathbb F_{2^d}\), builds all Chevalley–Eilenberg exterior differentials as binary matrices, and computes their ranks directly. Independently it enumerates the binary Frobenius-relation codes and compares the Betti vectors. It checks all 21 monic irreducible binary defining polynomials of degrees two through six. A separate realization test enumerates all cyclic codes with minimum distance at least three in those lengths and compares them to the codes obtained from all full-degree field elements. All tests pass. These finite checks corroborate but do not replace the general proof.

Run with `python3 verify.py`. Expected success marker: `BINARY_FROBENIUS_CODE_COHOMOLOGY_VERIFIED`.

## Relationship to prior work
Vilca Rodríguez, Schneider and Usefi study metabelian Lie algebras with a codimension-one abelian ideal and isomorphism invariants of their enveloping algebras (arXiv:1903.06915, first posted 16 March 2019). The present claim concerns the ordinary modular Lie-cohomology profile, not the isomorphism type of the enveloping algebra. Classical Chevalley–Eilenberg theory supplies the two-term differential; this computation is fully credited as the starting mechanism. Work on cyclic codes and the Frobenius action, including Winterhof (1999), supplies the known coding-theory framework. The additional statement here is the **bidirectional, all-degree correspondence** between the exact cohomology profiles of irreducible binary almost-abelian Lie algebras and *all* binary cyclic code weight enumerators with minimum distance at least three, including normality detection and a primitive-element boundary example. Generalized almost-abelian cohomology discussed by de Andrade Pinto et al. (arXiv:2610.20153) is formulated over complex/real fields and does not assert this characteristic-two cyclic-code realization theorem.

## Limitations
The theorem determines the Betti polynomial and attainable profiles, not the complete graded cup-product algebra or classification of isomorphism classes realizing each profile. Distinct cyclic codes can share a weight enumerator, and the cohomology polynomial does not recover the full code. No assertion is made about characteristic other than two, restricted cohomology, or arbitrary noninvertible adjoint actions. Historical priority against unindexed work joining normal bases, cyclic codes and modular Lie cohomology is not fully settled; the result is not independently certified.

## References
1. J. L. Vilca Rodríguez, C. Schneider, H. Usefi, *The isomorphism problem for universal enveloping algebras of four-dimensional solvable Lie algebras*, arXiv:1903.06915 (first posted 2019-03-16). https://arxiv.org/abs/1903.06915
2. A. Winterhof, *Cyclic codes and the Frobenius automorphism*, Archiv der Mathematik (1999). https://doi.org/10.1007/S000130050301
3. M. de Andrade Pinto, L. C. do Brasil Maia, L. F. Cavenaghi, P. A. Muniz Martins, *On the generalized cohomologies of almost abelian solvmanifolds*, arXiv:2610.20153 (2026). https://arxiv.org/abs/2610.20153
4. S. Yang, X. Kong, X. Shi, *Complete weight enumerators of a class of linear codes over finite fields*, Advances in Mathematics of Communications 15 (2021), 99–112 (first available 2019-11-20). https://doi.org/10.3934/amc.2020045
