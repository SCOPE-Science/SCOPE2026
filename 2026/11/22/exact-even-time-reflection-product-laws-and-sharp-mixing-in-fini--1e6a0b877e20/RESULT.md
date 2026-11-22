# Exact even-time reflection-product laws and sharp mixing in finite special linear groups

## Finding

Let \(q\ge 3\) be any odd prime power, \(K=\mathbb F_q\), and \(H=\operatorname{SL}_2(K)\). Put
\[
\mathcal R=\{r\in\operatorname{GL}_2(K):r^2=I_2,\ \operatorname{tr}(r)=0\}.
\]
These are precisely the noncentral involutions in \(\operatorname{GL}_2(K)\), and each has determinant \(-1\). They form one conjugacy class with \(|\mathcal R|=q(q+1)\). For independent uniform \(r_1,r_2,\ldots\in\mathcal R\), let \(P_k=r_1r_2\cdots r_{2k}\), for every integer \(k\ge1\). Thus \(P_k\in H\).

Write \(\chi\) for the quadratic character of \(K\), extended by \(\chi(0)=0\). For \(g\in H\), set \(\Delta(g)=(\operatorname{tr}g)^2-4\). Define two class functions by the following exhaustive cases:

| Type of \(g\) | \(S(g)\) | \(C(g)\) |
|---|---:|---:|
| \(g=I_2\) or \(g=-I_2\) | \(q\) | \((q-3)(q+1)^2/4\) |
| \(\Delta(g)=0\), \(g\ne\pm I_2\) | \(0\) | \((q-3)(q+1)/4\) |
| \(\chi(\Delta(g))=1\) | \(1\) | \(-(q+1)\) |
| \(\chi(\Delta(g))=-1\) | \(-1\) | \(0\) |

When \(q=3\), the split-regular case is empty. The **complete prescribed-target law** is, for every \(g\in H\) and every \(k\ge1\),
\[
\boxed{\Pr(P_k=g)=\frac{1+q^{1-2k}S(g)+(2/(q+1))^{2k}C(g)}{q(q^2-1)}.}
\]
Every target occurs already after two reflections. More precisely, the number of ordered pairs \((r,s)\in\mathcal R^2\) with \(rs=g\) is
\[
N(g)=\begin{cases}
q(q+1),&g=\pm I_2,\\
2q,&g\ne\pm I_2\text{ and }\Delta(g)=0,\\
q-\chi(\Delta(g)),&\Delta(g)\ne0.
\end{cases}
\]

The total-variation distance to the uniform law \(U_H\), **at every time**, is
\[
\boxed{d_{\mathrm{TV}}(\mathcal L(P_k),U_H)
=\frac{2q^{1-2k}}{q^2-1}
+\frac{(q-3)(q+1)}{2(q-1)}\left(\frac{2}{q+1}\right)^{2k}.}
\]
The corresponding exact chi-square divergence is
\[
\boxed{\chi^2(\mathcal L(P_k)\Vert U_H)
=q^{2-4k}+\frac{(q-3)(q+1)^2}{4}\left(\frac{2}{q+1}\right)^{4k}.}
\]
For \(q>3\), the sharp per-pair asymptotic total-variation factor is \(4/(q+1)^2\), with the displayed positive coefficient. At \(q=3\), the second summand is identically zero and the sharp factor is \(1/9\). At time \(k=1\), total variation is \(2/q+O(q^{-2})\) as odd \(q\to\infty\).

## Assumptions and scope

All matrices are over an arbitrary finite field of odd order, including nonprime extension fields. All sampling is independent, with replacement and uniform on the **single split-reflection conjugacy class** \(\mathcal R\), not on every order-two matrix (which would include the center). The products contain an even positive number of factors and therefore lie in \(H\). No claim is made for even characteristic or arbitrary reflection-biased sampling. Total variation means one half the sum of absolute differences of singleton probabilities, and chi-square is \(\sum_g(\Pr(P_k=g)-1/|H|)^2/(1/|H|)\).

## Proof

**1. Two-factor fibers.** By Cayley–Hamilton, every \(r\in\mathcal R\) has the form \(\bigl(\begin{smallmatrix}a&b\\c&-a\end{smallmatrix}\bigr)\) with \(a^2+bc=1\); counting its two eigenspaces gives \(|\mathcal R|=q(q+1)\). If \(g\in H\), the equation \(rs=g\) requires \(s=rg\), and the second factor belongs to \(\mathcal R\) precisely when \(\operatorname{tr}(rg)=0\). For \(g=\pm I_2\) this holds for every \(r\).

For nonscalar \(g\), conjugate it in \(\operatorname{GL}_2(K)\) to \(\bigl(\begin{smallmatrix}0&-1\\1&t\end{smallmatrix}\bigr)\), with \(t=\operatorname{tr}g\). Then \(\operatorname{tr}(rg)=0\) forces \(c=b-at\), and \(r^2=I_2\) becomes
\[
a^2+b^2-tab=1.
\]
For \(t=\pm2\), this is \((a\mp b)^2=1\), giving \(2q\) solutions. For \(t^2-4\ne0\), elementary nonsingular binary-quadric counting gives \(q-\chi(t^2-4)\). This proves the fiber formula; in particular, every fiber is nonempty.

**2. Even-convolution spectrum.** Let \(G=\operatorname{GL}_2(K)\) and let \(\mu\) be uniform on \(\mathcal R\). Since \(\mathcal R\) is a conjugacy class, convolution by \(\mu\) acts by the scalar \(\psi(r)/\psi(1)\) in every complex irreducible representation \(\psi\) of \(G\). The complete standard character table of \(\operatorname{GL}_2(K)\) gives the following eigenvalues on this class: for determinant characters they are \(\pm1\); for Steinberg twists of degree \(q\), \(\pm1/q\); for distinct-character principal series of degree \(q+1\), they are \(0\) or \(\pm2/(q+1)\), and the nonzero case occurs exactly when both inducing characters have equal value at \(-1\); for cuspidal characters they are zero. Both parities occur among the \(q-1\) multiplicative characters of \(K^\times\), equally often.

Fourier inversion on \(G\), restricted to \(H\) after \(2k\) steps, shows that determinant characters contribute the uniform term, Steinberg twists together contribute \(q^{1-2k}S(g)\), where \(S(g)\) is the projective-line permutation character minus one, and equal-parity principal series contribute \((2/(q+1))^{2k}C(g)\). The function \(S(g)\) counts fixed points of \(g\) on \(\mathbb P^1(K)\), minus one; its values are precisely the listed four cases. At \(k=1\), substituting the independently computed two-factor fibers \(N(g)\) determines \(C(g)\) in the table. Since the whole surviving principal-series sector has the same even-step scalar, these values remain valid for every \(k\). The group order \(|H|=q(q^2-1)\) supplies the normalization.

**3. Exact distances.** The cardinalities of the four types are respectively \(2\), \(2(q^2-1)\), \(q(q+1)(q-3)/2\), and \(q(q-1)^2/2\). From the displayed probability formula, the deviations from uniform are nonnegative on the central and noncentral-unipotent types and negative on both regular semisimple types. For split-regular matrices this follows from
\[
q^{1-2k}<(q+1)\left(\frac2{q+1}\right)^{2k}
\]
for \(k\ge1\); nonsplit matrices have only a negative Steinberg deviation. Therefore total variation equals the sum of the positive deviations. Using the first two type counts gives precisely its asserted two-term formula. The two nonconstant functions are orthogonal under the uniform measure and satisfy
\[
\mathbb E_{U_H}S^2=1,\quad
\mathbb E_{U_H}C^2=\frac{(q-3)(q+1)^2}{4},\quad
\mathbb E_{U_H}SC=0.
\]
Squaring the density gives the chi-square identity. The two decay bases are distinct for \(q>3\), and the second coefficient is then strictly positive, proving sharpness. For \(q=3\), that coefficient vanishes.

## Verification

The standalone Python file `verify.py` independently constructs every matrix in \(H\) and every reflection in \(\mathcal R\) over prime fields of orders \(3,5,7,11\) and the nonprime field \(\mathbb F_9\). It performs direct multiplication, checks every two-factor target count, forms actual repeated pair-product convolutions, and compares every target probability, total variation and chi-square with the asserted rational formulas. The run checks \(k\le4\) for \(q=3\), \(k\le3\) for \(q=5\), \(k\le2\) for \(q=7,9\), and \(k=1\) for \(q=11\). See `verification_output.txt`. Enumeration is finite corroboration, not a proof for all finite fields or times; the character and conic arguments above establish the universal statement.

## Relationship to prior work

The distinction between reality and strong reality, and the existence of involution decompositions, appear in Wonenburger's foundational work and in Singh–Thakur's treatment of algebraic groups. These do **not** give prescribed pair multiplicities or repeated-product mixing distributions. The classical character table in Digne–Michel, Section 15.9, and in the published tabulation of Pantangi–Sin, does provide the representation-theoretic input, but not the reduced four-stratum all-length formula, its sign decomposition or the sharp exact distances. Buell and collaborators describe generalized symmetric spaces for the same rank-two linear groups, rather than convolution powers of one conjugacy class. Ballantyne–Rowley examine odd-order products of involutions in **even characteristic**, a different class geometry. The double-coset Markov-chain literature covers random **unipotent transvections**, not semisimple determinant-negative reflections.

## Limitations

The novelty assertion is limited to the displayed complete explicit formulas after comparison with located sources; it is not a proof that an unindexed earlier result does not exist. The underlying character table and existence of two-involution factorizations are classical and are not claimed as new. The formulas are confined to the uniform split-reflection walk in degree two, odd characteristic and even times. No independent audit has been performed.

## References

- A. Singh and M. Thakur, *Reality Properties of Conjugacy Classes in Algebraic Groups*, arXiv:0804.1245 (first public version 2008-04-08), especially Sections 3.1–3.2.
- F. Digne and J. Michel, *Representations of Finite Groups of Lie Type*, Cambridge University Press, 1991, Section 15.9, character table of \(\operatorname{GL}_2(\mathbb F_q)\).
- C. Buell, A. G. Helminck, V. Klima, J. Schaefer, C. Wright, and E. Ziliak, *On the Structure of Generalized Symmetric Spaces of \(\operatorname{SL}_2(\mathbb F_q)\) and \(\operatorname{GL}_2(\mathbb F_q)\)*, *Note di Matematica* 37 (2017), doi:10.1285/i15900932v37n2p1.
- J. Ballantyne and P. Rowley, *Odd Order Products of Conjugate Involutions in Linear Groups over \(GF(2^a)\)*, MIMS preprint (deposited 2016-07-26), https://eprints.maths.manchester.ac.uk/2487/.
- V. R. T. Pantangi and P. Sin, *Perfect State Transfer in Graphs Related to Linear Groups in Two Dimensions*, *Algebraic Combinatorics* 9 (2026), doi:10.5802/alco.469, Section 3.1 (standard rank-two character table).
- *Double Coset Markov Chains*, *Forum of Mathematics, Sigma* (2023), https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/double-coset-markov-chains/65900A56DB1DBD6F6FDBA258DD5EA7B8.
