# Full Walsh support and exact dyadic spectral gap for primitive binary words

## Finding
For every integer \(n\ge 2\), let \(P_n\subseteq\mathbb F_2^n\) be the set of binary words having least cyclic period exactly \(n\). Put \(r=\operatorname{rad}(n)\), the product of the distinct prime divisors of \(n\), and \(m=n/r\). For \(b\in\mathbb F_2^n\), define the **unnormalized** Walsh multiplier
\[
W_n(b)=\sum_{x\in P_n}(-1)^{\langle b,x\rangle}.
\]
Let \(V_m\subseteq\mathbb F_2^n\) denote the \(m\)-dimensional linear subspace of words repeated with period dividing \(m\), and let \(H_m=V_m^\perp\). Then
\[
\boxed{W_n(b)\ne0\quad\Longleftrightarrow\quad b\in H_m,\qquad \nu_2(W_n(b))=m\text{ whenever }b\in H_m.}
\]
Here \(\nu_2\) denotes the ordinary exponent of two dividing a nonzero integer; its value is not defined for zero.

In particular, there are exactly \(2^{n-m}\) nonzero multipliers and \(2^n-2^{n-m}\) zeros. Moreover,
\[
\boxed{\min_{b:W_n(b)\ne0}|W_n(b)|=\gcd\{W_n(b):W_n(b)\ne0\}=2^m.}
\]
The full additive translation stabilizer of \(P_n\), not merely a subgroup thereof, equals \(V_m\). Thus the convolution operator \(C_nf=f*\mathbf1_{P_n}\) on \(\ell^2(\mathbb F_2^n)\), with counting-measure and unnormalized convolution, has rank \(2^{n-m}\), and its Moore–Penrose inverse has exact operator norm \(2^{-m}\). Its condition number restricted to its nonzero spectral subspace equals \(|P_n|/2^m\), with \(|P_n|=\sum_{d\mid n}\mu(n/d)2^d\).

## Assumptions and scope
The alphabet is exactly \(\mathbb F_2\); a word is primitive if it is not a repetition of any shorter block, equivalently its least rotation period is \(n\). Coordinate indices are \(0,\dots,n-1\). For a divisor \(d\mid n\), write
\[
V_d=\{x\in\mathbb F_2^n:x_i=x_{i\bmod d}\text{ for every }i\},\qquad H_d=V_d^\perp.
\]
Thus \(b\in H_d\) precisely when \(\sum_{i\equiv j\ (\mathrm{mod}\ d)}b_i=0\pmod2\) for every \(j=0,\dots,d-1\). The arithmetic function \(\mu\) is the ordinary Möbius function. The Fourier transform and convolution are both unnormalized. No assertions concern representative Lyndon words rather than all primitive labelled words.

## Proof
**Möbius decomposition.** Every binary word has a unique least period dividing \(n\), and the divisor-sublattice Möbius inversion identity is an equality of indicator functions:
\[
\mathbf1_{P_n}=\sum_{d\mid n}\mu(n/d)\mathbf1_{V_d}.
\]
Character orthogonality on the \(d\)-dimensional subspace \(V_d\) gives
\[
W_n(b)=\sum_{d\mid n}\mu(n/d)2^d\mathbf1_{H_d}(b).\tag{1}
\]

**Radical reduction.** The condition \(\mu(n/d)\ne0\) holds exactly for \(d=mt\) with \(t\mid r\), where \(r=\operatorname{rad}(n)\) and \(m=n/r\). Since \(V_m\subseteq V_{mt}\), their annihilators satisfy \(H_{mt}\subseteq H_m\). Therefore every summand in (1) vanishes when \(b\notin H_m\).

**No cancellation inside the support.** For \(b\in H_m\), the term at \(d=m\) in (1) is \(\mu(r)2^m\), and \(\mu(r)\) is odd. Every other nonzero term has \(d=mt\ge2m\), hence is divisible by \(2^{m+1}\). Consequently
\[
W_n(b)\equiv\mu(r)2^m\pmod{2^{m+1}},
\]
so \(\nu_2(W_n(b))=m\), for every \(b\in H_m\). This is an integer congruence, not a computational estimate, and proves exact full Fourier support.

**Sharpness and rank.** The frequency \(b=e_0+e_m\) exists because \(n\ge2m\). It belongs to \(H_m\), while it belongs to no \(H_{mt}\) for \(t>1\), since its two nonzero coordinates have distinct residues modulo \(mt\). Equation (1) therefore gives the exact witness \(W_n(e_0+e_m)=\mu(r)2^m\). Since \(H_m\) has dimension \(n-m\), the support cardinality is \(2^{n-m}\). Together with universal divisibility, the witness gives the displayed minimum and gcd.

**Stabilizer and operator consequences.** For any subset \(S\) of a finite binary vector group, a translation \(a\) stabilizes \(S\) if and only if \((-1)^{\langle b,a\rangle}=1\) for every \(b\) with \(\widehat{\mathbf1_S}(b)\ne0\). Here the support is exactly \(H_m\); thus the stabilizer is \(H_m^\perp=V_m\), with equality. Walsh characters diagonalize unnormalized convolution and have eigenvalues \(W_n(b)\). The pseudoinverse therefore has norm equal to the reciprocal of the smallest positive multiplier magnitude, \(2^{-m}\). The spectral radius is \(W_n(0)=|P_n|\), because \(\mathbf1_{P_n}\) is nonnegative and \(|W_n(b)|\le |P_n|\) by the triangle inequality. This proves the condition-number statement.

## Verification
The standalone `verify.py` uses direct period tests to construct the indicator of \(P_n\), and then computes every integer Walsh coefficient by a fast Walsh–Hadamard butterfly, **independently of equation (1)**. For every \(2\le n\le16\) it compares all coefficients with (1), checks exact support, sharp gap, the explicit witness, and the valuation congruence. For \(2\le n\le8\) it also enumerates all translations and verifies that the stabilizer is exactly \(V_m\). Running `python3 verify.py` gives `PRIMITIVE_BINARY_WALSH_EXACT_PASS lengths=2..16; all frequencies and stabilizers<=8`.

These finite checks corroborate the exact identity but do not prove its all-length statement. The infinite proof is the preceding Möbius/orthogonality/divisibility argument.

## Relationship to prior work
The classical Möbius primitive-word count \(|P_n|=\sum_{d\mid n}\mu(n/d)2^d\) is explicitly recalled in Domaratzki and Rampersad (2010), Section 7. It is the zero-frequency specialization of (1), and is not asserted to be new. The contribution assessed here is the **full multi-frequency support and valuation classification**, the exact minimum, and maximal translation stabilizer; none follows from the numerical count alone without the signed subspace analysis.

Vajnovszki (2007) studies Gray-code orderings for Lyndon words and primitive necklaces, which are **one representative per rotation orbit**, rather than all labelled primitive words; the main theorem concerns their enumeration order, not Walsh character sums. Goresky, Klapper and Washington (2000) study **univariate cyclic discrete Fourier transforms of a fixed periodic sequence** and its 2-adic span, not the \(2^n\)-point Boolean-cube transform of the indicator of the set of all primitive words. In particular, neither published statement gives the displayed radical-dependent Fourier support.

## Limitations
The result concerns primitive labelled binary words and the unnormalized Walsh transform, not individual Lyndon representatives or arbitrary alphabet groups. It determines the zero set and the uniform 2-adic order of nonzero coefficients, **not** every multiplier magnitude or its distribution. The published literature comparison was bounded; an unidentified earlier equivalent signed Möbius/necklace transform identity remains possible. Independent mathematical validation has not been performed.

## References
- M. Domaratzki and N. Rampersad, *Abelian Primitive Words*, arXiv:1006.4104, first submitted 2010-06-21, especially Section 7: primitive-word Möbius counting formula. https://arxiv.org/abs/1006.4104
- V. Vajnovszki, *Gray code order for Lyndon words*, Discrete Mathematics & Theoretical Computer Science 9 (2007), 145–152. DOI:10.46298/dmtcs.393. https://dmtcs.episciences.org/en/articles/393
- M. Goresky, A. Klapper and L. Washington, *Fourier Transforms and the 2-adic Span of Periodic Binary Sequences*, IEEE Transactions on Information Theory 46 (2000), 687–691. DOI:10.1109/18.825843. https://www.cs.engr.uky.edu/~klapper/pdf/fourier.pdf
