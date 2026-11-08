# Fourier-null rigidity of residue-deformed cubic moment curves over prime-square rings

## Finding
For every prime \(p\), put \(R=\mathbb Z/p^2\mathbb Z\). Let \(h_1,h_2,h_3:\mathbb F_p\to\mathbb F_p\) be **arbitrary** functions, interpreted using representatives in \(\{0,\ldots,p-1\}\). Define
\[
E_{\mathbf h}=\{(x+p h_1(\bar x),\ x^2+p h_2(\bar x),\ x^3+p h_3(\bar x)):x\in R\}\subset R^3.
\]
Every such set has \(p^2\) points. Let \(T_{\mathbf h}\) be unnormalized additive convolution by \(\mathbf1_{E_{\mathbf h}}\) on functions \(R^3\to\mathbb C\). Its Fourier-zero set and convolution rank are **independent of all three functions** \(h_j\).

For a frequency \(\xi=(u,v,w)\in R^3\), let \(\bar u,\bar v,\bar w\in\mathbb F_p\) be the reduced coefficients. If \((\bar u,\bar v,\bar w)\ne(0,0,0)\), then
\[
\widehat{\mathbf1}_{E_{\mathbf h}}(\xi)=0
\quad\Longleftrightarrow\quad
\{r\in\mathbb F_p:\bar u+2\bar v r+3\bar w r^2=0\}=\varnothing.
\]
If \(u=pU,v=pV,w=pW\), with \(U,V,W\in\mathbb F_p\), then
\[
\widehat{\mathbf1}_{E_{\mathbf h}}(\xi)=0
\quad\Longleftrightarrow\quad
r\longmapsto Ur+Vr^2+Wr^3\text{ permutes }\mathbb F_p.
\]
Consequently the exact convolution nullity is
\[
\dim\ker T_{\mathbf h}=Z_p:=
\begin{cases}
20,&p=2,\\
168,&p=3,\\
p^3\left(p-1+\frac{p(p-1)^2}{2}\right)
+(p-1)\left(1+p\mathbf1_{p\equiv2\ (\mathrm{mod}\ 3)}\right),&p\ge5,
\end{cases}
\]
and \(\operatorname{rank}T_{\mathbf h}=p^6-Z_p\). For primes tending to infinity, the ratio \(\operatorname{rank}T_{\mathbf h}/p^6\) tends to \(1/2\). For example, ranks are \(44,561,10101,72367\) at \(p=2,3,5,7\), respectively.

In particular, keeping \(h_1=0\) and varying \(h_2,h_3\) produces \(p^{2p}\) **distinct** embedded cubic-curve perturbations with the same Fourier-zero set and the same convolution rank.

## Assumptions and scope
All assertions hold for every rational prime \(p\ge2\) and every triple of set-theoretic functions \(h_j:\mathbb F_p\to\mathbb F_p\), with no polynomial or smoothness assumption. The characters of \(R^3\) are \(x\mapsto\exp(2\pi i\langle\xi,x\rangle/p^2)\). The Fourier transform is the **unnormalized sum** over the indicated curve, so the convolution operator acts on a space of dimension \(p^6\). Frequency elements are understood modulo \(p^2\). Only the **zero set**, not the nonzero values or singular values, is claimed to be perturbation invariant.

## Proof
**1. Injectivity and exact stationary-phase identity.** If two curve points have equal first coordinates modulo \(p^2\), then their input residues modulo \(p\) agree, since the first-coordinate perturbation is divisible by \(p\). On a fixed residue fibre the perturbations are constant, so equality of first coordinates forces equality of the inputs. Thus \(|E_{\mathbf h}|=p^2\).

Let \(\zeta=\exp(2\pi i/p^2)\), let \(f(X)=uX+vX^2+wX^3\), and write \(x=r+pt\), where \(r,t\in\{0,\ldots,p-1\}\). The binomial formula modulo \(p^2\) gives
\[
f(r+pt)\equiv f(r)+pt f'(r)\pmod{p^2},
\qquad f'(r)=u+2vr+3wr^2.
\]
Each perturbation term \(p(u h_1(r)+v h_2(r)+w h_3(r))\) is independent of \(t\) modulo \(p^2\). Orthogonality of the \(p\)-th roots of unity in the sum over \(t\) therefore yields the exact identity
\[
\widehat{\mathbf1}_{E_{\mathbf h}}(u,v,w)
=p\!\sum_{\substack{r\in\mathbb F_p\\f'(r)=0\ ({\rm mod}\ p)}}
\zeta^{f(r)+p\left(u h_1(r)+v h_2(r)+w h_3(r)\right)}.
\tag{1}
\]
In the exponent, use any chosen integer lifts of residue arguments; the expression is well-defined modulo \(p^2\) once those lifts are fixed.

**2. Primitive-frequency zero criterion, odd primes at least five.** If the reduced frequency is nonzero and \(p\ge5\), the reduced derivative is a **nonzero** polynomial of degree at most two. There are zero, one, or two critical residues. The sum (1) vanishes if there are no such residues. If there is one, it is a single nonzero root of unity. If there are two, a sum of two \(p^2\)-th roots cannot vanish: their ratio would need to equal \(-1\), impossible for odd-order roots. This proves the first equivalence in this range, including complete invariance under \(\mathbf h\).

**3. Small-prime primitive frequencies.** At \(p=2\), the reduced derivative is \(\bar u+\bar w r\). If it has two roots (is the zero polynomial) for a primitive frequency, then \(\bar u=\bar w=0\) and \(\bar v=1\). The two exponents in (1) have different parity because the reduced original polynomial equals \(r^2=r\). Therefore their fourth roots cannot sum to zero: two fourth roots cancel only when their exponents differ by two, which preserves parity. Otherwise there are at most one critical residue. At \(p=3\), the reduced derivative is \(\bar u+2\bar v r\). If it vanishes identically for a primitive frequency, then \(\bar u=\bar v=0\) and \(\bar w\ne0\). Here the original polynomial modulo three is \(\bar w r^3=\bar w r\), so the three exponents in (1) occupy **three distinct** residue classes modulo three. A sum of three ninth roots of unity vanishes only if their exponents are congruent modulo three: divisibility by \(\Phi_9(z)=1+z^3+z^6\) forces the exponent-count polynomial to equal \(z^j\Phi_9(z)\) for some \(j\in\{0,1,2\}\). Thus (1) cannot vanish. In every other primitive case there is at most one critical residue. The primitive criterion consequently holds also at \(p=2,3\).

**4. Imprimitive-frequency zero criterion.** If \((u,v,w)=p(U,V,W)\), all perturbation exponents are multiples of \(p^2\), and
\[
\widehat{\mathbf1}_{E_{\mathbf h}}(pU,pV,pW)
=p\sum_{r\in\mathbb F_p}\exp\!\left(\frac{2\pi i}{p}(Ur+Vr^2+Wr^3)\right).
\tag{2}
\]
Let \(c_j\) count the residues \(r\) for which the cubic takes value \(j\). Equation (2) vanishes precisely when \(\sum_{j=0}^{p-1}c_j z^j\) is divisible by \(\Phi_p(z)=1+z+\cdots+z^{p-1}\). Its degree is less than \(p\), so all \(c_j\) must be equal. Their sum is \(p\), and hence each is one: the polynomial is a permutation. This proves the second equivalence in all characteristics.

**5. Counting rootless derivatives.** For \(p\ge5\), a nonzero polynomial of degree at most two in the form \(U+2Vr+3Wr^2\) has no root if it is a nonzero constant (\(p-1\) choices), or a quadratic with nonsquare discriminant. There are \(p(p-1)\) nonzero-leading quadratics with each of the \((p-1)/2\) nonsquare discriminants, hence \(p(p-1)^2/2\) rootless quadratics. No nonconstant linear polynomial is rootless. Thus the rootless triple count is \(p-1+p(p-1)^2/2\). At \(p=2,3\), direct examination of the reduced derivative gives respectively \(2\) and \(6\) rootless primitive triples. Each reduced triple has exactly \(p^3\) lifts to a frequency in \(R^3\).

**6. Counting permutation cubics.** For \(p=2\), the function is \((U+V+W)r\), giving four permutation triples. For \(p=3\), it is \((U+W)r+Vr^2\), which permutes precisely when \(V=0\) and \(U+W\ne0\); there are six triples.

For \(p\ge5\), if \(W=0\), a quadratic can permute only when \(V=0\) and \(U\ne0\), giving \(p-1\) triples. If \(W\ne0\), translation of the input and scaling of the output reduce the cubic to \(r^3+cr\), where \(c=(U-V^2/(3W))/W\); translations and scalings do not change permutation status. If \(c=0\), the cubic permutes precisely if \(\gcd(3,p-1)=1\), i.e. \(p\equiv2\pmod3\), and then there are \(p(p-1)\) triples (choose \(V,W\ne0\) freely and impose \(U=V^2/(3W)\)).

If \(c\ne0\), it never permutes: an equality \(x^3+cx=y^3+cy\) with \(x\ne y\) is equivalent to \(x^2+xy+y^2=-c\). Writing \(y=tx\), \(t\ne1\), one needs \(\chi(1+t+t^2)=\chi(-c)\) with \(1+t+t^2\ne0\), where \(\chi\) is the Legendre symbol. The standard conic count \(\sum_{t\in\mathbb F_p}\chi(t^2+t+1)=-1\) holds for \(p\ne3\): after completing the square, it counts pairs of factors with fixed nonzero product. There are at most two zero summands, so for \(p\ge7\) both signs occur at least twice among all \(t\), and removing \(t=1\) retains both signs. For \(p=5\), direct values at \(t=0,2\) are \(1,2\), representing both signs. Therefore a collision exists in every case \(c\ne0\). The total number of permutation triples for \(p\ge5\) is \((p-1)(1+p\mathbf1_{p\equiv2\pmod3})\).

**7. Rank and distinct deformations.** Add the disjoint counts of Fourier-zero primitive and imprimitive frequencies from Steps 5–6 to obtain \(Z_p\). Fourier characters diagonalize every convolution on the finite abelian group \(R^3\), so the rank is exactly \(p^6-Z_p\). The leading term in the nullity at \(p\ge5\) is \(p^6/2\), establishing the limit. Finally fixing \(h_1=0\) and independently varying \(h_2,h_3\) gives distinct curves: in each first-coordinate fibre \(x\), the second and third coordinates recover the corresponding values of the functions. Thus \(p^{2p}\) distinct curves have the common zero set.

## Verification
The accompanying executable `verify.py` conducts exact arithmetic tests without floating-point approximations. It forms the actual exponent histogram of every relevant character sum and reduces it modulo the cyclotomic polynomial \(\Phi_{p^2}(z)=1+z^p+\cdots+z^{(p-1)p}\). It exhaustively checks the residue rootless/permutation counts for \(p=2,3,5,7,11,13\), all Fourier frequencies for every deformation in the indicated binary family and for three ternary examples, full Fourier tables for unperturbed \(p=5,7\) and a perturbed \(p=5\) example, and deterministic pseudorandom frequency checks for perturbed \(p=7,11\). Run `python3 verify.py` (standard library only). Expected terminal marker: `ALL_EXACT_CUBIC_MOMENT_CHECKS_OK`. Finite verification does not replace the proof in Steps 1–7.

## Relationship to prior work
Prime-power stationary-phase expansions for polynomial exponential sums, including the fibre expansion used in Step 1, are established classical methods (Cochrane–Zheng, 1999). Earlier published work on prime-square cubic graphs classifies orthogonal exponential bases for the **two-coordinate** set \(\{(t,t^3)\}\) using a related derivative test and permutation cubics; those statements concern a different ambient character space and do not provide the present three-coordinate zero spectrum or its perturbation-invariance rank count. Haessig (2006) studies cubic exponential sums over prime fields and their symmetric powers, not prime-square Fourier nullity. Segers–Zúñiga-Galindo (2009) provide general local exponential-sum estimates rather than this exact all-frequency classification. The present result synthesizes elementary known ingredients into a complete, characteristic-uniform spectral invariant for a natural prime-square moment curve and all of its residue-digit deformations; no claim of discovering stationary phase or permutation-polynomial theory is made.

## Limitations
The assertion is confined to the modulus \(p^2\), the three-coordinate cubic moment curve and arbitrary first-digit deformations of the displayed type. It does not classify nonzero Fourier multipliers, singular values, operator norms, higher prime-power levels or more general polynomial parametrizations. The rank law follows from exact zero-set rigidity and does not assert equality of the full Fourier transforms among deformations. General stationary-phase and permutation-polynomial literature could imply an equivalent specialization; priority beyond the inspected sources is not independently established. No independent audit or validation has been performed.

## References
1. C. D. Haessig, *L-functions of symmetric powers of cubic exponential sums*, arXiv:math/0608521v1, first submitted 2006-08-21, especially the introduction on cubic finite-field sums. https://arxiv.org/abs/math/0608521
2. T. Cochrane and Z. Zheng, *Pure and mixed exponential sums*, Acta Arithmetica **91** (1999), 249–278, DOI: 10.4064/aa-91-3-249-278, especially Theorem 2.1 and its proof. https://doi.org/10.4064/aa-91-3-249-278
3. D. Segers and W. A. Zúñiga-Galindo, *Exponential Sums and Polynomial Congruences Along \(p\)-adic Submanifolds*, arXiv:0910.1887v1 (2009), Sections 5–6. https://arxiv.org/abs/0910.1887
4. *All exponential spectra of the cubic graph over prime-square cyclic rings*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-all-exponential-spectra-of-the-cubic-graph-over-prime-square-cyc--a783058468ac, especially proof Step 1 (prime-square stationary phase and cubic permutations).
5. *Isotropic quadratic stability at the uniform finite-field moment-curve extremizer*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-isotropic-quadratic-stability-at-the-uniform-finite-field-moment--49b4f93ca348, for a distinct finite-field moment-curve Fourier-extension invariant.
