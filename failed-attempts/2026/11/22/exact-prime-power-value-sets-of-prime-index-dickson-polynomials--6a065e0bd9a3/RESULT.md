# Exact prime-power value sets of prime-index Dickson polynomials

## Finding

Let \(p\ge 5\) be prime and \(a\in\mathbb Z\) satisfy \(p\nmid a\). Define the first-kind Dickson polynomials by
\[
D_0(X,a)=2,\qquad D_1(X,a)=X,\qquad
D_{n+1}(X,a)=X D_n(X,a)-aD_{n-1}(X,a).
\]
For \(k\ge1\), let \(V_k(p,a)\) be the image of \(D_p(X,a)\) in \(\mathbb Z/p^k\mathbb Z\). Write \(\chi_p(a)\) for the Legendre symbol, which is \(1\) or \(-1\) under the unit assumption. Then
\[
|V_k(p,a)|=\begin{cases}
p,&k=1,\\
p,&k=2,\\
p^{k-1},&k\ge3,\ \chi_p(a)=-1,\\
(p^2-2p+2)p^{k-3},&k\ge3,\ \chi_p(a)=1.
\end{cases}
\]
For \(k\ge3\), if \(\chi_p(a)=-1\), every attained residue has precisely \(p\) preimages modulo \(p^k\). If \(\chi_p(a)=1\), exactly \((p-2)p^{k-2}\) attained residues have \(p\) preimages, and exactly \(2p^{k-3}\) attained residues have \(p^2\) preimages. At \(k=1\) every residue has one preimage; at \(k=2\) there are \(p\) attained residues, each with \(p\) preimages.

The \(p\)-adic image is a disjoint union of full residue balls. For a nonsquare unit parameter it consists of \(p\) balls of radius \(p^{-2}\), one above each residue modulo \(p\). For a square unit parameter, it consists of \(p-2\) balls of radius \(p^{-2}\) and two balls of radius \(p^{-3}\). Consequently its normalized Haar measure is
\[
\mu\bigl(D_p(\mathbb Z_p,a)\bigr)=
\begin{cases}
1/p,&\chi_p(a)=-1,\\
(p^2-2p+2)/p^3,&\chi_p(a)=1.
\end{cases}
\]
In the square case, if \(a=b^2\) with \(b\in\mathbb Z_p^\times\), the two exceptional output balls are centered at \(\pm2b^p\) modulo \(p^3\).

## Assumptions and scope

The prime \(p\) is any prime at least \(5\), the parameter \(a\) is any integer prime to \(p\), and the exponent \(k\) is any positive integer. The assertions concern the values and individual fiber sizes of the polynomial function on the complete residue ring, not values over the finite field \(\mathbb F_{p^k}\). A ball \(c+p^j\mathbb Z_p\) denotes all \(p\)-adic integers congruent to \(c\) modulo \(p^j\); its Haar measure is \(p^{-j}\). For square \(a\), the square root \(b\) exists in \(\mathbb Z_p^\times\) by Hensel's lemma.

The restriction \(p\ge5\) is substantive. At \(p=3\), \(a=1\), \(k=4\), direct exact enumeration gives \(13\) values modulo \(81\), whereas extending the square-parameter formula would predict \(15\).

## Proof

**1. Frobenius reduction and derivative.** The recurrence or the functional identity
\[
D_n(z+a/z,a)=z^n+(a/z)^n
\]
implies the polynomial congruence \(D_p(X,a)\equiv X^p\pmod p\). Thus the integer polynomial \(A(X)=D_p'(X,a)/p\) is well defined, with degree \(p-1\) and leading coefficient one. The Dickson derivative identity gives
\[
(X^2-4a)A(X)^2=D_p(X,a)^2-4a^p.
\]
Reducing modulo \(p\), using \(4^p\equiv4\pmod p\), and cancelling \(X^2-4a\) in \(\mathbb F_p[X]\), yields
\[
A(X)^2\equiv(X^2-4a)^{p-1}\pmod p.
\]
Both \(A\) and \((X^2-4a)^{(p-1)/2}\) are monic and of the same degree, so
\[
\boxed{D_p'(X,a)/p\equiv(X^2-4a)^{(p-1)/2}\pmod p.}
\]
In particular, the normalized derivative is a unit at each residue \(r\pmod p\) for which \(r^2\not\equiv4a\pmod p\).

**2. All ordinary branches are exact balls.** Fix an integer representative \(r\in\{0,\ldots,p-1\}\) with \(r^2\not\equiv4a\pmod p\). Taylor expansion of \(D_p\), using the divisibility by \(p\) of every nonleading coefficient and \(p\ge5\), shows that
\[
G_r(u)=\frac{D_p(r+pu,a)-D_p(r,a)}{p^2}\in\mathbb Z[u]
\]
and, writing \(c_r=(r^2-4a)^{(p-1)/2}\not\equiv0\pmod p\), that
\[
G_r(u)\equiv c_r u\pmod p,\qquad G_r'(u)\equiv c_r\pmod p.
\]
For every \(v\in\mathbb Z_p\), the congruence \(G_r(u)\equiv v\pmod p\) has exactly one root. Its derivative is a unit, so Hensel lifting gives a unique root in \(\mathbb Z_p\) of \(G_r(u)=v\). Therefore the complete image of this input branch is exactly
\[
D_p(r+p\mathbb Z_p,a)=D_p(r,a)+p^2\mathbb Z_p.
\]
Moreover, modulo \(p^k\), for \(k\ge2\), this image branch contains \(p^{k-2}\) outputs, each with \(p\) input preimages. Since \(D_p(r,a)\equiv r\pmod p\), branches attached to distinct \(r\)'s have disjoint output sets.

**3. The two exceptional branches occur exactly for square parameters.** If \(\chi_p(a)=-1\), the congruence \(r^2\equiv4a\pmod p\) has no solutions; step 2 covers all \(p\) branches.

If \(\chi_p(a)=1\), fix \(b\in\mathbb Z_p^\times\) with \(b^2=a\). Homogeneity gives
\[
D_p(by,b^2)=b^pD_p(y,1),
\]
so it suffices to study the input branches \(y\equiv\pm2\pmod p\) for parameter one.

Put \(m=(p-1)/2\) and define the monic integral polynomial
\[
P_p(Y)=1+\sum_{j=1}^{m}D_j(Y,1).
\]
The Dickson functional identity, after substituting \(Y=z+z^{-1}\), proves the polynomial factorization
\[
D_p(Y,1)-2=(Y-2)P_p(Y)^2.
\]
We have \(P_p(2)=1+2m=p\). Reduction modulo \(p\) and the Frobenius congruence from step 1 give \((Y-2)P_p(Y)^2\equiv(Y-2)^p\pmod p\). Since \(P_p\) is monic, it follows that
\[
P_p(Y)\equiv(Y-2)^m\pmod p.
\]
Here \(m\ge2\), so \(P_p'(2)\equiv0\pmod p\). Consequently \(E(u)=P_p(2+pu)/p\) belongs to \(\mathbb Z[u]\) and satisfies \(E(u)\equiv1\pmod p\). The exceptional branch therefore has the exact form
\[
D_p(2+pu,1)=2+p^3uE(u)^2.
\]
The polynomial \(H(u)=uE(u)^2\) obeys \(H(u)\equiv u\pmod p\) and \(H'(u)\equiv1\pmod p\). Hensel's lemma again makes \(H\) a bijection of \(\mathbb Z_p\). Hence
\[
D_p(2+p\mathbb Z_p,1)=2+p^3\mathbb Z_p.
\]
As \(D_p\) is odd for odd \(p\), the negative branch has image \(-2+p^3\mathbb Z_p\). Scaling by \(b^p\) gives the two exceptional balls for arbitrary square unit \(a\). Each such branch has exactly \(p^{k-3}\) outputs with \(p^2\) preimages modulo \(p^k\), for \(k\ge3\).

**4. Count the disjoint branches.** The reduction \(D_p(r,a)\equiv r\pmod p\) ensures one output residue class for each of the \(p\) input classes, so there are no cross-branch collisions. For nonsquare \(a\), sum \(p\) ordinary branches of size \(p^{k-2}\). For square \(a\), sum \(p-2\) ordinary branches and two exceptional branches, of sizes \(p^{k-2}\) and \(p^{k-3}\) respectively. The assertions for \(k=1,2\), all fiber multiplicities, and the Haar densities follow directly. This proves every stated formula for all the indicated primes, parameters, and exponents.

## Verification

A standalone, standard Python script with SymPy (`verify_prime_dickson.py`) checks the discriminant derivative congruence and exceptional polynomial identity symbolically at five primes; it independently enumerates image and fiber distributions for \(108\) unit-parameter/prime-power cases, as well as the excluded \(p=3\) boundary. Run it using:

```bash
python verify_prime_dickson.py
```

It checks, for example, that \(D_5(X,1)\) has \(17\) distinct outputs modulo \(125\), with fifteen fibers of size \(5\) and two of size \(25\), whereas \(D_5(X,2)\) has \(25\) outputs, all with fiber size \(5\). These finite checks supplement but do not replace the all-prime proof above.

## Relationship to prior work

Bremser and Gómez-Calderon (1991) studied Dickson value sets over Galois rings. Their Theorem 5 evaluates the ordinary (non-parabolic) fibers, while their Lemmas 9–10 and Theorem 11 bound the exceptional contributions for indices divisible by the residue characteristic; they explicitly describe difficulties obtaining complete value-set sizes. The result here fixes the natural prime-index case \(d=p\), determines those exceptional branches *exactly*, and gives the missing value sets and complete fiber distributions on \(\mathbb Z/p^k\mathbb Z\) for every unit parameter and every \(p\ge5\). The 1991 estimates are not themselves an explicit statement of this classification.

Shang's preprint (2023) gives sharp *universal upper bounds* for images of non-permutation polynomials on integer residue rings. These bounds do not determine the image or fibers of a specified Dickson polynomial. Brazelton, Harrington, Litman, and Wong (2021/2022) treat Dickson residue sums and image sizes over **finite fields**; a field of cardinality \(p^k\) is not the residue ring \(\mathbb Z/p^k\mathbb Z\). Neither result implies the two distinct prime-adic image densities proved here.

## Limitations

The theorem does not classify the prime \(p=3\), nonunit parameters \(p\mid a\), degree indices other than \(p\), or Dickson maps on higher-degree Galois rings. The comparison with Bremser and Gómez-Calderon's author-posted full-text transcription is limited by imperfect transcription of some displayed formulas; the verbal statements, hypotheses, and scope of the relevant theorems were inspected. No claim of absolute literature uniqueness or independent certification is made. All exact counts are mathematical consequences of the given proof; the finite verification cases are not substitutes for it.

## References

- Priscilla S. Bremser and Javier Gómez-Calderon, *Value sets of Dickson polynomials over Galois rings*, Journal of Number Theory 38 (1991), 240–250, DOI: https://doi.org/10.1016/0022-314X(91)90087-R . Author-posted full-text transcription: https://www.academia.edu/48986625/Value_sets_of_Dickson_polynomials_over_Galois_rings .
- Shikui Shang, *Value sets of non-permutation polynomials over the residue class rings of integers*, arXiv:2310.20226, first posted 2023-10-31, https://arxiv.org/abs/2310.20226 .
- Thomas Brazelton, Joshua Harrington, Matthew Litman, and Tony W. H. Wong, *Residue sums of Dickson polynomials over finite fields*, arXiv:2103.09119, first posted 2021-03-16, https://arxiv.org/html/2103.09119v3 .
