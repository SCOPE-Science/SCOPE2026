# Maximal additive index below the first cyclotomic subfield threshold

## Finding

Let \(q=p^n\), where \(p\) is prime and \(n\ge 1\). Let \(f:\mathbb F_q\to\mathbb F_q\) be a map for which \(g(x)=f(x)-f(0)\) is nonzero for every \(x\in\mathbb F_q^*\), so that its usual cyclotomic (multiplicative) index \(\ell=\operatorname{Ind}(f)\mid q-1\) is defined. If \(\ell\le p\), then **exactly one** of the following holds:

1. \(f(x)=b+a x^{p^j}\) for some \(a\ne0\), \(b\in\mathbb F_q\), \(0\le j<n\), and \(\operatorname{AddInd}(f)=1\);
2. \(f\) is not of the preceding form and \(\operatorname{AddInd}(f)=q\).

In particular, no intermediate additive index occurs at multiplicative index at most the characteristic. The cutoff is uniform-sharp for every odd prime \(p\): on \(\mathbb F_{p^2}\), a non-Frobenius \(\mathbb F_p\)-linear permutation exists with multiplicative index exactly \(p+1\) and additive index \(1\).

## Assumptions and scope

The multiplicative index is the least divisor \(\ell\mid q-1\) for which, writing \(H=(\mathbb F_q^*)^\ell\), there are an integer \(r\) and nonzero scalars \(a_i\) with \(g(x)=a_i x^r\) on each coset of \(H\). It is assumed that \(g(0)=0\) and \(g(x)\ne0\) for \(x\ne0\). The additive index is the least \(p^k\) such that there exist an \(\mathbb F_p\)-subspace \(U\le\mathbb F_q\) of codimension \(k\) and an \(\mathbb F_p\)-linear map \(L:\mathbb F_q\to\mathbb F_q\) such that \(f-L\) is constant on each coset of \(U\). This is the definition in the cited number-theory literature. No permutation assumption is imposed on \(f\); only the zero-free-on-\(\mathbb F_q^*\) condition required by the cited definition of multiplicative index is used.

## Proof

**1. The period subspace.** Put
\[
T=\{u\in\mathbb F_q: g(x+u)-g(x)\text{ is independent of }x\in\mathbb F_q\}.
\]
Evaluation at \(x=0\) shows that independence is equivalent to \(g(x+u)-g(x)=g(u)\) for every \(x\). This set is an \(\mathbb F_p\)-linear subspace: sums and negatives of periods remain periods, and scalar multiplication by elements of \(\mathbb F_p\) follows from repeated addition. Moreover, if \(U\) satisfies the additive-index definition, every \(u\in U\) is a period, so \(U\subseteq T\). Conversely \(g|_T\) is \(\mathbb F_p\)-linear, hence extends to a linear map \(L\) on the entire \(\mathbb F_q\); then \(g-L\) is constant on cosets of \(T\). Consequently
\[
\operatorname{AddInd}(f)=q/|T|.
\]

**2. Scalar invariance.** For every \(h\in H\) and \(x\in\mathbb F_q\), cyclotomicity gives \(g(hx)=h^r g(x)\), including at \(0\). If \(u\in T\), then
\[
g(x+hu)-g(x)=h^r\bigl(g(h^{-1}x+u)-g(h^{-1}x)\bigr)=h^r g(u),
\]
independent of \(x\); thus \(hu\in T\). Since \(\ell\mid q-1\) and \(\ell\le p\), and \(p\nmid(q-1)\), necessarily \(\ell\le p-1\), whence
\[
|H|=(q-1)/\ell\ge(q-1)/(p-1)=1+p+\cdots+p^{n-1}>p^{n-1}
\]
for \(n\ge2\). For \(n=1\), every nonempty subset of \(\mathbb F_p^*\) spans \(\mathbb F_p\). If \(T\) contains any \(u\ne0\), it contains \(Hu\), hence \(|T|>|\mathbb F_p|^{n-1}\) when \(n\ge2\); since \(T\) is an \(\mathbb F_p\)-subspace, \(T=\mathbb F_q\). For \(n=1\) the same conclusion follows directly. Therefore either \(T=\{0\}\) or \(T=\mathbb F_q\). In the first case \(\operatorname{AddInd}(f)=q\); in the second, \(g\) is \(\mathbb F_p\)-linear.

**3. Classifying the additive case.** For \(n=1\), every \(\mathbb F_p\)-linear map is \(g(x)=a x\); its zero-free condition ensures \(a\ne0\). Suppose \(n\ge2\). The unique reduced polynomial of an \(\mathbb F_p\)-linear map is a linearized polynomial
\[
G(X)=\sum_{j=0}^{n-1}c_j X^{p^j}
\]
of degree at most \(p^{n-1}\). Put \(m=|H|>p^{n-1}\), and choose \(s\) with \(0\le s<m\) congruent to \(r\pmod m\). For each \(h\in H\),
\[
G(h)=g(1)h^s.
\]
The polynomial \(G(X)-g(1)X^s\) has degree at most \(\max(p^{n-1},m-1)<m\) but vanishes at all \(m\) points of \(H\), so it vanishes identically. As \(g(1)\ne0\), comparison with the distinct degrees in the reduced linearized polynomial shows \(s=p^j\) and \(G(X)=g(1)X^{p^j}\) for a unique \(0\le j<n\). Conversely every affine Frobenius monomial has additive index \(1\).

**4. Sharpness at \(p+1\).** Fix an odd prime \(p\), put \(q=p^2\), and choose \(c\in\mathbb F_{p^2}^*\) with field norm \(N_{q/p}(c)\ne1\), possible because \(\mathbb F_p^*\) contains an element other than \(1\). Then
\[
F_c(x)=x+c x^p
\]
is \(\mathbb F_p\)-linear, so \(\operatorname{AddInd}(F_c)=1\). It is a permutation: if \(x\ne0\) belonged to its kernel, then \(x^{p-1}=-c^{-1}\); taking norms would force \(1=N_{q/p}(c)^{-1}\), impossible. For every \(h\in\mathbb F_p^*\), \(F_c(hx)=hF_c(x)\). The subgroup \(\mathbb F_p^*\) has index \(p+1\) in \(\mathbb F_{p^2}^*\), so \(\operatorname{Ind}(F_c)\le p+1\). Its reduced polynomial has two nonzero Frobenius terms, hence is not a single Frobenius monomial; by parts 1–3 its multiplicative index cannot be at most \(p\). As indices are integers, \(\operatorname{Ind}(F_c)=p+1\), proving uniform sharpness.

## Verification

The accompanying standard-library checker `verify.py` independently enumerates all 320 cyclotomic presentations with index \(1\) or \(2\) over \(\mathbb F_9=\mathbb F_3[w]/(w^2+1)\) (64 index-1 and 256 index-2 presentations), tests every additive period against all \(9\) inputs and checks that all nonzero period spaces are Frobenius monomials. It also verifies the index-\(4\), additive-index-\(1\) sharpness example over \(\mathbb F_9\) with a norm-\(2\) coefficient. These are finite sanity checks, not substitutes for the unbounded proof above. Run `python3 verify.py`.

## Relationship to prior work

Bienvenu and Winterhof, *Additive index and Carlitz rank* (arXiv:2604.25414, publicly posted 28 April 2026), §6.2, prove that for a non-Frobenius map either multiplicative index exceeds \(p\) **or** additive index is at least \(p\). Their statement does not force maximal additive index \(q=p^n\) in the entire low-index range and does not identify the sharp \(p+1\) boundary. Their definition and Proposition 2 supply the background. Reis and Wang introduced additive index in 2022. The present proof uses elementary scalar invariance of the whole additive-period subspace, distinct from the degree-based argument used for the cited lower bound. All assertions of novelty concern the exact maximal-index rigidity and sharpness statement, not the underlying definitions, linearized-polynomial representation, or finite-field polynomial root bound.

## Limitations

This theorem applies only to maps for which the multiplicative index is defined in its usual zero-free cyclotomic sense. It does not classify maps of multiplicative index \(\ell\ge p+1\) generally, nor give lower bounds on additive index outside the stated range. The main 2026 preprint is fully readable. The 2022 foundational article was located bibliographically but its full text could not be obtained through available open-access routes, so potential unindexed or inaccessible prior equivalences remain a priority risk. No independent mathematical audit has been performed.

## References

1. P.-Y. Bienvenu and A. Winterhof, *Additive index and Carlitz rank*, arXiv:2604.25414v1 (28 Apr 2026), https://arxiv.org/html/2604.25414 , especially §§1.2, 2.3, 6.2.
2. L. Reis and Q. Wang, *The additive index of polynomials over finite fields*, Finite Fields Appl. **79** (2022), 102002, https://doi.org/10.1016/j.ffa.2022.102002 .
3. L. Işık and A. Winterhof, *Carlitz rank and index of permutation polynomials*, Finite Fields Appl. **49** (2018), 156–165, https://arxiv.org/abs/1611.06361 .
