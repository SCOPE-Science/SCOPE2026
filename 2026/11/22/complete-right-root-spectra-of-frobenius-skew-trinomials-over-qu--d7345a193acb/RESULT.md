# Complete right-root spectra of Frobenius skew trinomials over quadratic finite fields

## Finding

Let \(q\) be an odd prime power, \(K=\mathbb F_{q^2}\), and \(\sigma(c)=c^q\). In the Ore ring \(K[X;\sigma]\) write
\[
f_{n,a}(X)=X^{2n}+aX^n+1,\qquad n\ge1,\quad a\in K.
\]
A *right root* is \(u\in K\) for which \(f_{n,a}\) is right divisible by \(X-u\); let \(R_{n,q}(a)\) denote the number of distinct such elements.

**Odd exponents.** Suppose \(n\) is odd. Define \(g=\gcd(n,q-1)\), \(L=(q-1)/g\), and \(\epsilon=1\) when \(L\) is even, \(0\) otherwise. Among the \(q^2-1\) **nonzero** coefficients \(a\), the right-root histogram is
\[
\begin{array}{c|c}
R_{n,q}(a)&\#\{a\ne0:R_{n,q}(a)\text{ has this value}\}\\\hline
g&q+1\\
2g&(q+1)(L-1-\epsilon)/2\\
0&q^2-1-(q+1)\bigl(1+(L-1-\epsilon)/2\bigr).
\end{array}
\]
The remaining coefficient has \(R_{n,q}(0)=g(q+1)\epsilon\). The displayed zero-count multiplicity is nonnegative and all nonzero-coefficient classes are disjoint.

**Even exponents.** Suppose \(n\) is even. Define \(h=\gcd(n/2,q-1)\), \(L=(q-1)/h\), and \(\epsilon=1\) when \(L\) is even, \(0\) otherwise. Across **all** \(q^2\) coefficients \(a\in K\), the histogram is
\[
\begin{array}{c|c}
R_{n,q}(a)&\#\{a:R_{n,q}(a)\text{ has this value}\}\\\hline
h(q+1)&1+\epsilon\\
2h(q+1)&(L-1-\epsilon)/2\\
0&q^2-(1+\epsilon)-(L-1-\epsilon)/2.
\end{array}
\]
Every coefficient giving a nonzero root count lies in \(\mathbb F_q\), a sharp field-of-definition distinction from the odd case. The count with \(h(q+1)\) roots consists of \(a=-2\), and additionally \(a=2\) exactly when \(\epsilon=1\).

In both cases, the total right-root incidence is \(\sum_{a\in K}R_{n,q}(a)=q^2-1\).

## Assumptions and scope

All statements concern **distinct right roots in the coefficient field** \(K\), not roots in an algebraic closure, not left roots, and not multiplicities or irreducible-factor counts. The Ore multiplication is \(Xc=\sigma(c)X\). For a nonzero \(u\), define \(N_j(u)=\prod_{i=0}^{j-1}\sigma^i(u)\) and \(N_0(u)=1\). Right evaluation is \(\sum_i c_iN_i(u)\) for a polynomial \(\sum_i c_iX^i\). Since the constant term of \(f_{n,a}\) is \(1\), zero is never a right root. Let \(t=u^{q+1}\in\mathbb F_q^\times\) denote the norm.

## Proof

**1. Ore evaluation and the odd case.** Because \(\sigma^2=1\), if \(n=2m+1\) then \(N_{2n}(u)=t^n\) and \(N_n(u)=t^m u\). The right-root condition is therefore
\[
t^n+a t^m u+1=0.
\]
If \(a=0\), the condition is \(t^n=-1\). The cyclic group \(\mathbb F_q^\times\) has \(g\) solutions precisely when \(-1\) belongs to the subgroup \(H=(\mathbb F_q^\times)^n\), of size \(L\). Each norm value has exactly \(q+1\) preimages in \(K^\times\); and \(-1\in H\) is equivalent to \(2\mid L\). This proves \(R_{n,q}(0)=g(q+1)\epsilon\).

For \(a\ne0\), the displayed equation determines \(u\) uniquely from \(t\):
\[
u=-\frac{t^n+1}{a t^m}.
\]
A necessary and sufficient condition for this value to have norm \(t\) is
\[
(t^n+1)^2=\operatorname N_{K/\mathbb F_q}(a)\,t^n.
\]
This follows by taking the norm of the expression for \(u\), and is also sufficient because it makes that expression nonzero and norm-consistent. (If \(t^n=-1\), the equation would force \(a=0\); hence such \(t\) cannot arise here.) Write \(z=t^n\in H\) and \(B=\operatorname N(a)\ne0\). Each \(z\in H\) has exactly \(g\) choices of \(t\), giving
\[
R_{n,q}(a)=g\#\{z\in H:(z+1)^2=Bz\}.
\]
The map \(z\mapsto B(z)=(z+1)^2/z=z+2+z^{-1}\) identifies exactly inversion pairs \(\{z,z^{-1}\}\). Its fixed points in \(H\) are \(z=1\) and (only if \(\epsilon=1\)) \(z=-1\). The first yields \(B=4\ne0\) with one solution \(z\), while the second yields the forbidden \(B=0\). All \(L-1-\epsilon\) other elements form inverse pairs, giving distinct nonzero \(B\), each with exactly two solutions \(z\). Every \(B\in\mathbb F_q^\times\) is the norm of exactly \(q+1\) nonzero coefficients \(a\). These facts prove the odd-case histogram.

**2. Even case.** Let \(n=2m\). Now \(N_n(u)=t^m\), \(N_{2n}(u)=t^{2m}\), and the right-root condition is
\[
t^{2m}+a t^m+1=0.
\]
A solution necessarily has \(a\in\mathbb F_q\). Set \(J=(\mathbb F_q^\times)^m\), so \(|J|=L\) and each \(y\in J\) has \(h\) preimages \(t\in\mathbb F_q^\times\). The equation becomes \(a=-(y+y^{-1})\). Distinct values correspond exactly to inverse pairs in \(J\): the fixed points \(y=1\) and, iff \(\epsilon=1\), \(y=-1\), give \(1+\epsilon\) coefficients, each with \(h(q+1)\) right roots. The remaining \(L-1-\epsilon\) elements pair off, each pair giving \(2h(q+1)\) right roots. All other coefficients give none. This completes the even-case count.

**3. Total incidence and boundaries.** For every \(u\in K^\times\), the evaluation equation uniquely determines one coefficient \(a\), since \(N_n(u)\ne0\). Consequently \(\sum_aR_{n,q}(a)=q^2-1\). The two histograms satisfy this exact identity. All arguments use only cyclic norm fibers, inversion orbits, and \(\sigma^2=1\), so remain valid for odd nonprime prime powers, for characteristic dividing \(n\), and for every \(n\ge1\).

## Verification

The standalone script `CHECK.py` constructs \(\mathbb F_{p^2}\) as a nonsquare quadratic extension of \(\mathbb F_p\), explicitly computes each Ore right evaluation using the twisted-factor recurrence, and checks both the coefficientwise right-root count and the claimed histogram. It passes \(100\) cases, using \(p=3,5,7,11,13\) and \(1\le n\le20\), comprising exactly \(918720\) evaluations. Run `python CHECK.py` using Python 3 without external dependencies. This is a finite error-detection check, not a proof for arbitrary prime powers; the infinite proof is in the preceding section.

## Relationship to prior work

Hayata and Tsushima, *Counting irreducible skew polynomials \(X^{2n}+aX^n+1\)* (first submitted November 3, 2026, arXiv:2611.04767), count coefficients giving **irreducible skew polynomials** using reduced norms, for general coefficient-field degrees. The present claim instead classifies the number of **right linear factors** over quadratic extensions for every coefficient and every exponent, including reducible instances. Neither the irreducible-coefficient formula nor its specializations give this right-root histogram.

The primary manuscript cites Tsushima's 2026 work on the full fiber distribution of \(x\mapsto x^{p^j}+x^{-1}\), which covers the corresponding **unrestricted** reciprocal-Frobenius map. In the odd case here, the relevant change of variable has image a subgroup of index \(\gcd(n,q-1)\). A full-field fiber histogram alone does not count intersections of each fiber with that subgroup. The present norm/inversion argument resolves this subgroup restriction for the one-parameter skew trinomial family. That cited work was not available as full text for direct comparison; possible unindexed or implicit subgroup refinements are a residual originality risk. The case \(n=1\) is a classical baseline and is **not separately claimed as new**. General right-root evaluation is standard Ore theory.

## Limitations

This does not count irreducible factors of degree greater than one, determine left-root histograms, or describe right roots over larger field extensions. The independent audit status is not performed. The new contribution claimed is the complete parameter-dependent quadratic-extension family profile, not the basic skew evaluation identity, norm-fiber cardinality, inversion pairing, or the known full-field reciprocal-map profile.

## References

1. T. Hayata and T. Tsushima, *Counting irreducible skew polynomials \(X^{2n}+aX^n+1\)*, arXiv:2611.04767, first public version November 3, 2026. https://arxiv.org/abs/2611.04767
2. T. Tsushima, *The Distribution of \(x^{p^n}+x^{-1}\) over Finite Fields and Self-Adjoint Irreducible Polynomials*, Zenodo preprint, 2026, DOI:10.5281/zenodo.23878333. https://doi.org/10.5281/zenodo.23878333
3. T. Baumbaugh and F. Manganiello, *Matroidal Root Structure of Skew Polynomials over Finite Fields*, arXiv:1706.04283. https://arxiv.org/abs/1706.04283
4. X. Caruso and J. Le Borgne, *A new faster algorithm for factoring skew polynomials over finite fields*, J. Symbolic Comput. 79 (2017), 411–443. https://doi.org/10.1016/j.jsc.2016.02.016
