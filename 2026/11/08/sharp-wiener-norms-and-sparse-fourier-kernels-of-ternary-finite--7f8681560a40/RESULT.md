# Sharp Wiener norms and sparse Fourier kernels of ternary finite-field quadratic shells

## Finding

Let \(q=p^s\), where \(p\) is an odd prime and \(s\geq1\). Let \(A\) be any nonsingular symmetric \(3\times3\) matrix over \(F=\mathbb F_q\), put \(Q(x)=x^{\mathsf T}Ax\), and choose any \(r\in F^\times\). Set \(S_r=\{x\in F^3:Q(x)=r\}\). Write \(\eta\) for the quadratic multiplicative character, let \(\varepsilon=\eta(-r\det A)\in\{-1,1\}\), and define
\[
 C_p=\sum_{j=0}^{p-1}\left|\cos(2\pi j/p)\right|.
\]
For the Fourier projection \(P_{S_r}\) onto the characters indexed by \(S_r\), the **exact sharp endpoint norms**, with counting-measure \(\ell^1\) and \(\ell^\infty\), are
\[
 \boxed{\|P_{S_r}\|_{\ell^1\to\ell^1}=\|P_{S_r}\|_{\ell^\infty\to\ell^\infty}
 =\frac{q+\varepsilon}{p}C_p+\frac{1-\varepsilon}{q}-\frac{1-\varepsilon}{q^2}.}
\]
In particular, the two types give respectively \((q+1)C_p/p\) and \((q-1)C_p/p+2/q-2/q^2\). These values are independent of the particular form, nonzero radius, and nontrivial additive character except through \(\varepsilon\) and the field characteristic.

For any nontrivial additive character \(\psi:F\to\mathbb C\), define the unnormalized Fourier sum \(F_r(\xi)=\sum_{x\in S_r}\psi(-\xi^{\mathsf T}x)\), and \(Q^*(\xi)=\xi^{\mathsf T}A^{-1}\xi\). Its **complete pointwise formula** is
\[
 F_r(0)=q^2+\varepsilon q,\qquad
 F_r(\xi)=q\varepsilon\!\sum_{v\in F:\ v^2=rQ^*(\xi)}\!\psi(v)
 \quad (\xi\ne0).
\]
Consequently, the Fourier sum vanishes at exactly \(q(q-1)(q-\varepsilon)/2\) of the \(q^3\) spatial points, namely those for which \(\eta(rQ^*(\xi))=-1\). No other zeros occur for odd \(p\).

**Hermitian projector corollary.** Let \(K=\mathbb F_{q^2}\), and let \(\mathcal P\) be the rank-one self-adjoint idempotents in the additive group of Hermitian \(2\times2\) matrices over \(K/F\). The Fourier projection onto \(\mathcal P\) has the exact endpoint norm
\[
 \boxed{\|P_{\mathcal P}\|_{\ell^1\to\ell^1}=\|P_{\mathcal P}\|_{\ell^\infty\to\ell^\infty}=
 \frac{q-1}{p}C_p+\frac2q-\frac2{q^2}.}
\]
Its convolution kernel has exactly \(q^2(q^2-1)/2\) zeros in the ambient group of size \(q^4\). The formula gives the all-characteristic-prime and all-extension-degree sharp spectral-amplification constant of this natural unitary orbit.

## Assumptions and scope

All fields have odd characteristic. The quadratic form must be nondegenerate and its level \(r\) must be nonzero. A primitive choice of \(\psi\) is unnecessary: any nontrivial additive character yields the same norm. The Fourier transform is \(\widehat f(\xi)=q^{-3}\sum_{x\in F^3}f(x)\psi(-\xi^{\mathsf T}x)\); the spectral projection is \(P_{S_r}f(x)=\sum_{\xi\in S_r}\widehat f(\xi)\psi(\xi^{\mathsf T}x)\). The norm is the **operator norm**, not a normalized surface-extension constant.

## Proof

**1. Nondegenerate quadratic point counts.** Write \(\delta=\det A\), let \(G=\sum_{u\in F^\times}\eta(u)\psi(u)\), and recall \(G^2=\eta(-1)q\). Orthogonality of characters and completing three quadratic squares give, for every \(c\in F\),
\[
 \#\{x:Q(x)=c\}
 =\frac1q\left(q^3+\eta(\delta)G^3\sum_{t\ne0}\eta(t)\psi(-tc)\right).
\]
For \(c\ne0\) the inner sum is \(\eta(-c)G\); for \(c=0\) it vanishes. Thus the shell cardinality is \(q^2+\varepsilon q\), and the zero-level cardinality is \(q^2\). The same argument applies to \(Q^*\), whose determinant is \(\delta^{-1}\), hence its nonzero-level counts are \(q^2+q\eta(-\delta)\eta(c)\).

**2. The requisite exact Salié identity.** For arbitrary \(a\ne0\) and \(b\in F\),
\[
 \sum_{t\ne0}\eta(t)\psi(at+b/t)
 =\eta(a)G\sum_{v^2=4ab}\psi(v).
\]
This holds in every odd finite field. For a short proof, take the unnormalized Fourier transform in \(b\). For any \(y\ne0\), the left transform is \(q\eta(y)\psi(a/y)\); the right transform is
\(\eta(a)G\sum_v\psi(v-yv^2/(4a))\), which equals the same expression after one completed square and \(G^2=\eta(-1)q\). Both transforms vanish at \(y=0\). Invertibility of finite Fourier transform proves the identity, including \(b=0\).

**3. Exact Fourier character sums.** Inserting the orthogonality representation of the shell, followed by quadratic completion, gives for \(\xi\ne0\)
\[
 F_r(\xi)=\frac{\eta(\delta)G^3}{q}
 \sum_{t\ne0}\eta(t)\psi(-rt-Q^*(\xi)/(4t)).
\]
Apply step 2 with \(a=-r\) and \(b=-Q^*(\xi)/4\). Because \(G^4=q^2\), the scalar is \(q\eta(-r\delta)=q\varepsilon\), and \(4ab=rQ^*(\xi)\). This proves the stated pointwise formula. For \(\xi=0\), step 1 gives the claimed cardinality. A nonzero isotropic frequency has coefficient \(q\varepsilon\); a frequency with \(\eta(rQ^*(\xi))=-1\) has coefficient zero; a frequency with \(rQ^*(\xi)=v^2\ne0\) has coefficient \(q\varepsilon(\psi(v)+\psi(-v))\).

**4. Multiplicities and absence of hidden zeros.** The number of nonzero isotropic frequencies is \(q^2-1\). For each \(v\in F^\times\), the level \(Q^*(\xi)=v^2/r\) contains \(q^2+\varepsilon q\) frequencies. Each such level is represented twice as \(v\) ranges over \(F^\times\), via \(v\) and \(-v\). The remaining frequencies with nonsquare \(rQ^*(\xi)\) number
\[
 \frac{q-1}{2}(q^2-\varepsilon q)=\frac{q(q-1)(q-\varepsilon)}2.
\]
For the canonical additive character, \(\psi(v)+\psi(-v)=2\cos(2\pi\operatorname{Tr}_{F/\mathbb F_p}(v)/p)\). This cannot vanish: \(p\) is odd and none of the sampled angles gives a right angle. Any other nontrivial additive character gives a permutation of these values. Hence the displayed zero count is exact.

**5. Sharp endpoint projection norm.** The convolution kernel of \(P_{S_r}\) is \(K(z)=q^{-3}\sum_{\xi\in S_r}\psi(\xi^{\mathsf T}z)\). Young's inequality shows \(\|P_{S_r}\|_{\ell^1\to\ell^1}\le\sum_z|K(z)|\) and \(\|P_{S_r}\|_{\ell^\infty\to\ell^\infty}\le\sum_z|K(z)|\). Both are equalities: use a point mass for \(\ell^1\), and a function aligned with the complex conjugate kernel for \(\ell^\infty\). The sum \(\sum_z|K(z)|\) equals \(q^{-3}\sum_z|F_r(z)|\) by the nondegenerate trace pairing. Steps 1–4 therefore yield
\[
 \begin{aligned}
 q^3\sum_z|K(z)|&=(q^2+\varepsilon q)+q(q^2-1)
    +q(q^2+\varepsilon q)\sum_{v\in F^\times}|\cos(2\pi\operatorname{Tr}(v)/p)|.
 \end{aligned}
\]
Every fiber of the absolute field trace has \(q/p\) elements, so the final sum is \((q/p)C_p-1\). Simplification gives the boxed exact norm. In particular, for fixed \(p\) the norm divided by \(q\) tends to \(C_p/p\) along extensions, and as the odd characteristic \(p\) grows (with any extension degrees), the ratio tends to \(2/\pi\) by Riemann-sum convergence.

**6. Hermitian specialization.** Every Hermitian rank-one idempotent has trace one. Writing \(P=I_2/2+X\) with \(\operatorname{tr}(X)=0\), the equation \(P^2=P\) is equivalent to \(X^2=I_2/4\). In a basis \(K=F(\sqrt d)\) with \(d\) nonsquare, the traceless Hermitian matrix \(X=\left(\begin{smallmatrix}u&z\\z^q&-u\end{smallmatrix}\right)\) obeys \(X^2=(u^2+z^{q+1})I_2\). Writing \(z=x+y\sqrt d\), the form becomes \(u^2+x^2-dy^2\), of determinant \(-d\). Hence the level \(1/4\) has \(\varepsilon=\eta(d)=-1\). The full four-dimensional Hermitian trace pairing is nondegenerate, and the extra scalar Fourier direction merely repeats each traceless-shell coefficient \(q\) times, up to a unit-modulus phase. Therefore the four-dimensional projection norm is exactly the three-dimensional norm computed above; the kernel-zero count is multiplied by \(q\).

## Verification

The attached `checker.py` independently constructs the fields with orders \(3,5,7,11,9,25,27\), evaluates both discriminant classes for each field, and computes full finite Fourier transforms using multidimensional FFTs on the underlying additive prime-field groups. All \(14\) cases passed exact frequency-sector multiplicity, shell-size, Parseval-energy, complete coefficient and sharp-norm comparisons, with maximum numerical error below \(6\times10^{-14}\). Run `python checker.py` after installing `requirements.txt`. These finite checks are corroboration, not an infinite proof; the proof above is algebraic and applies to all odd prime powers.

## Relationship to prior work

Iosevich–Koh established general finite-field quadratic-surface Fourier formulas and restriction/extension estimates (2007, 2008), including a Salié-sum expression for the transform. Green–Sanders (2006) studies Wiener/spectral norms of Boolean functions and the general idempotent framework. The present result uses these classical ingredients but computes the **full sum of Fourier absolute values exactly** for every nondegenerate three-variable shell, obtains a two-type closed formula depending on \(p\), and deduces an exact kernel-zero count and the Hermitian-idempotent specialization. The cited primary papers do not state this exact norm or these two-class formulas. Priority is assessed only against the explicitly inspected literature and public mathematical search results; an unlocated equivalent calculation may exist.

## Limitations

This theorem requires odd characteristic, nonzero shell radius and a nondegenerate three-variable form. It does not address higher-dimensional quadrics or nonlinear phase retrieval. The exact norm follows from classical quadratic Gauss and Salié identities; it is not claimed that these underlying identities are new. No independent mathematical audit has been carried out, and exhaustive historical-priority review has not been completed.

## References

1. B. Green and T. Sanders, *Boolean functions with small spectral norm*, first public arXiv version 2006-05-18, arXiv:math/0605524. In particular, introduction and Theorem 1.3.
2. A. Iosevich and D. Koh, *Extension theorems for spheres in the finite field setting*, first public arXiv version 2007-12-11, arXiv:0712.1627. In particular, Section 3, Lemma 4.
3. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, first public arXiv version 2008-04-28, arXiv:0804.4505. In particular, Section 2 and Lemma 9.
