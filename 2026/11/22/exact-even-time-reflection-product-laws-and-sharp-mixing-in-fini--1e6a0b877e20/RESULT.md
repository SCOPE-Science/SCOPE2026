# Exact even-time reflection-product laws and sharp mixing in finite special linear groups

## Finding

Let \(q\ge 3\) be any odd prime power, \(K=\mathbb F_q\), and \(H=\operatorname{SL}_2(K)\). Put
\[
\mathcal R=\{r\in\operatorname{GL}_2(K):r^2=I_2,\ \operatorname{tr}(r)=0\}.
\]
These are precisely the noncentral involutions in \(\operatorname{GL}_2(K)\), and each has determinant \(-1\). They form one conjugacy class with \(|\mathcal R|=q(q+1)\). For independent uniform \(r_1,r_2,\ldots\in\mathcal R\), let \(P_k=r_1r_2\cdots r_{2k}\), for every integer \(k\ge1\). Thus \(P_k\in H\).

Write \(\chi\) for the quadratic character of \(K\), extended by \(\chi(0)=0\). For \(g\in H\), set \(\Delta(g)=(\operatorname{tr}g)^2-4\). The pointwise law at every positive even time has the following four-stratum form:
\[
\Pr(P_k=g)=\frac{1+q^{1-2k}S(g)+(2/(q+1))^{2k}C(g)}{q(q^2-1)},
\]
where

| Type of \(g\) | \(S(g)\) | \(C(g)\) |
|---|---:|---:|
| \(g=\pm I_2\) | \(q\) | \((q-3)(q+1)^2/4\) |
| \(\Delta(g)=0\), \(g\ne\pm I_2\) | \(0\) | \((q-3)(q+1)/4\) |
| \(\chi(\Delta(g))=1\) | \(1\) | \(-(q+1)\) |
| \(\chi(\Delta(g))=-1\) | \(-1\) | \(0\) |

When \(q=3\), the split-regular case is empty. The **total-variation distance** to the uniform law \(U_H\), at every \(k\ge1\), is
\[
\boxed{d_{\mathrm{TV}}(\mathcal L(P_k),U_H)
=\frac{2q^{1-2k}}{q^2-1}
+\frac{(q-3)(q+1)}{2(q-1)}\left(\frac{2}{q+1}\right)^{2k}.}
\]
The corresponding chi-square divergence is
\[
\chi^2(\mathcal L(P_k)\Vert U_H)
=q^{2-4k}+\frac{(q-3)(q+1)^2}{4}\left(\frac{2}{q+1}\right)^{4k}.
\]
For \(q>3\), the sharp per-pair asymptotic total-variation factor is \(4/(q+1)^2\), with the displayed positive coefficient. At \(q=3\), the second summand is identically zero and the sharp factor is \(1/9\). At time \(k=1\), total variation is \(2/q+O(q^{-2})\) as odd \(q\to\infty\). The contribution claimed here is the evaluated all-time total variation using the four-stratum density and its time-independent pattern of signs. No separate novelty is claimed for the two-factor counts, the eigenvalues, or the chi-square calculation from multiplicities.

## Assumptions and scope

All matrices are over an arbitrary finite field of odd order, including nonprime extension fields. All sampling is independent, with replacement and uniform on the **single split-reflection conjugacy class** \(\mathcal R\), not on every order-two matrix (which would include the center). The products contain an even positive number of factors and therefore lie in \(H\). No claim is made for even characteristic or arbitrary reflection-biased sampling. Total variation means one half the sum of absolute differences of singleton probabilities, and chi-square is \(\sum_g(\Pr(P_k=g)-1/|H|)^2/(1/|H|)\).

## Proof

**1. Two-factor fibers.** By Cayley–Hamilton, every \(r\in\mathcal R\) has the form \(\bigl(\begin{smallmatrix}a&b\\c&-a\end{smallmatrix}\bigr)\) with \(a^2+bc=1\); counting its ordered pair of distinct eigenspaces gives \(|\mathcal R|=q(q+1)\). If \(g\in H\), the equation \(rs=g\) requires \(s=rg\), and the second factor belongs to \(\mathcal R\) precisely when \(\operatorname{tr}(rg)=0\), since \(\det(rg)=-1\). For \(g=\pm I_2\) this holds for every \(r\).

For nonscalar \(g\), conjugate it in \(\operatorname{GL}_2(K)\) to \(\bigl(\begin{smallmatrix}0&-1\\1&t\end{smallmatrix}\bigr)\), with \(t=\operatorname{tr}g\). Then \(\operatorname{tr}(rg)=0\) forces \(c=b-at\), and \(r^2=I_2\) becomes
\[
 a^2+b^2-tab=1.
\]
For \(t=\pm2\), this is \((a\mp b)^2=1\), giving \(2q\) solutions. Otherwise, write the equation as \((a-tb/2)^2-(t^2-4)(b/2)^2=1\). If \(t^2-4\) is a square, factor it into two linear forms whose product is one, giving \(q-1\) solutions. If \(t^2-4\) is nonsquare, it is the norm-one equation in the quadratic extension, with \(q+1\) solutions. Thus the two-factor counts are
\[
N(g)=\begin{cases}
 q(q+1),&g=\pm I_2,\\
 2q,&g\ne\pm I_2\text{ and }\Delta(g)=0,\\
 q-\chi(\Delta(g)),&\Delta(g)\ne0.
\end{cases}
\]
In particular, every fiber is nonempty. This also follows from the prior class-product calculation discussed below.

**2. Even-convolution spectrum and the four-stratum density.** Let \(G=\operatorname{GL}_2(K)\) and let \(\mu\) be uniform on \(\mathcal R\). Since \(\mathcal R\) is a conjugacy class, convolution by \(\mu\) acts by the scalar \(\psi(r)/\psi(1)\) in every complex irreducible representation \(\psi\) of \(G\). The standard character table gives the following eigenvalues: for determinant characters they are \(\pm1\); for Steinberg twists of degree \(q\), \(\pm1/q\); for distinct-character principal series of degree \(q+1\), they are \(0\) or \(\pm2/(q+1)\), and the nonzero case occurs exactly when both inducing characters have the same value at \(-1\); for cuspidal characters they are zero. Both parities occur among the \(q-1\) multiplicative characters of \(K^\times\), equally often.

Fourier inversion on \(G\), restricted to \(H\) after \(2k\) steps, shows that determinant characters contribute the uniform term. Steinberg twists together contribute \(q^{1-2k}S(g)\) to the density relative to this uniform term, because \(|G|=(q-1)|H|\) and all \(q-1\) twists agree on \(H\). Here \(S(g)\) counts fixed points on \(\mathbb P^1(K)\), minus one, and gives the listed four cases. All the surviving principal-series terms decay with the same per-pair factor \(4/(q+1)^2\). Rather than summing their characters individually, use the density at \(k=1\) to recover their combined class function:
\[
C(g)=\frac{(q+1)^2}{4}\left(\frac{|H|N(g)}{|\mathcal R|^2}-1-\frac{S(g)}q\right).
\]
Inserting the four fiber counts gives the displayed table. This determines the contribution for every \(k\ge1\); all sectors with eigenvalue zero have vanished.

**3. Exact distances.** The cardinalities of the four types are respectively \(2\), \(2(q^2-1)\), \(q(q+1)(q-3)/2\), and \(q(q-1)^2/2\). For each repeated eigenvalue \(\pm1\) there is one nonscalar \(G\)-class of size \(q^2-1\). Split regular classes come from the \((q-3)/2\) unordered inverse pairs in \(K^\times\setminus\{\pm1\}\), each of size \(q(q+1)\). Nonsplit regular classes come from the \((q-1)/2\) unordered inverse pairs of norm-one elements of the quadratic extension outside \(K\), each of size \(q(q-1)\).

The deviations from uniform are nonnegative on the central and noncentral-unipotent types and negative on both regular semisimple types. For split-regular matrices this follows from
\[
 q^{1-2k}<(q+1)\left(\frac2{q+1}\right)^{2k},
\]
since the ratio of the left to the right side equals \(\frac q{q+1}\bigl(\frac{q+1}{2q}\bigr)^{2k}<1\). Nonsplit matrices have only a negative Steinberg deviation. Consequently, for all \(k\ge1\), total variation is the sum of the deviations on the fixed set \(\{g:\Delta(g)=0\}\). Using its first two type counts gives the stated two-term formula. For chi-square, the table and the type counts give
\[
 \mathbb E_{U_H}S^2=1,\qquad
 \mathbb E_{U_H}C^2=\frac{(q-3)(q+1)^2}{4},\qquad
 \mathbb E_{U_H}SC=0.
\]
Squaring the centered density gives the claimed formula. When \(q>3\), the second total-variation term has a strictly positive coefficient and a larger decay base. For \(q=3\) its coefficient vanishes, leaving precisely the first exponential. At \(k=1\) the second term simplifies to \(2(q-3)/(q^2-1)\) and the first is \(2/[q(q^2-1)]\), proving the large-field estimate.

## Verification

The standalone Python file `verify.py` directly constructs every matrix in \(H\) and every reflection in \(\mathcal R\) over prime fields of orders \(3,5,7,11\) and the nonprime field \(\mathbb F_9\). It checks every two-factor target count, forms repeated pair-product convolutions, and compares every target probability, total variation and chi-square with the asserted rational formulas. The recorded run checks \(k\le4\) for \(q=3\), \(k\le3\) for \(q=5\), \(k\le2\) for \(q=7,9\), and \(k=1\) for \(q=11\); see `verification_output.txt`. These computations provide finite corroboration, not the general proof.

## Relationship to prior work

Parashar and Patel, *Trilinear Forms for \(\operatorname{GL}_2(\mathbb F_q)\) via Conjugacy Classes*, arXiv:2610.23450v1 (16 October 2026), already give the split-semisimple class-product trace counts in Proposition 3.8(1), with conversion to regular-class multiplicities in Lemma 3.6 and scalar multiplicities in Lemma 3.9. For two copies of the class of \(\operatorname{diag}(1,-1)\), the product with one fixed factor has \(q-1\) choices per trace other than \(\pm2\), and \(2q-1\) at each exceptional trace. Multiplying by the class size \(|\mathcal R|\) counts ordered pairs at each trace. Dividing by the regular class sizes yields \(q-1\) and \(q+1\) per target, respectively. At each exceptional trace subtract the \(|\mathcal R|\) pairs giving the scalar, then divide by the single nonscalar \(G\)-class size \(q^2-1\), to obtain \(2q\). Thus the two-factor law above is a specialization of that prior calculation; the conic proof is included for completeness.

There is also a projectively equivalent two-factor comparison with *Square-class-resolved reflection convolution and the exact two-step law in ternary orthogonal groups* (22 November 2026; no ordering inferred from the shared date). On the traceless space with \(Q=-\det\), conjugation by a matrix reflection fixes its axis and negates its orthogonal complement. The negative of this action is the orthogonal reflection in that norm-square axis. The map from matrix reflections to these axes is two-to-one, and each ordered pair giving the projected target has two lifts giving a prescribed element of \(\operatorname{SL}_2(K)\) over that target. Consequently the fixed-square-class two-factor counts in that work give these same fibers after lifting. Its displayed total variation instead uses both orthogonal reflection types and compares with uniform on \(SO_3(q)\). The corresponding comparison for a single square class is to uniform on the spinor-positive subgroup, the projective image of \(H\).

Involution factorization is classical, and the character table and class-scheme eigenvalue formula already provide the spectral ingredients (Digne–Michel, Section 15.9; Pantangi–Sin, Sections 2.1 and 3.1). Pantangi–Sin's perfect-state-transfer construction uses a union of classes. The projection and mixing results of Diaconis–Ram–Simper for transvections use a different step distribution. The exact total-variation calculation here uses the reduced density and determines its positive part at **every** time, not just a general spectral bound, exponents, or the two-factor law.

## Limitations

No general priority claim is made. The comparisons distinguish the exact all-time total-variation expression from known two-factor fibers and spectral inputs. The formulas are confined to the uniform split-reflection walk in degree two, odd characteristic and even times.

## References

- A. Parashar and S. P. Patel, *Trilinear Forms for \(\operatorname{GL}_2(\mathbb F_q)\) via Conjugacy Classes*, arXiv:2610.23450v1, https://arxiv.org/abs/2610.23450, §3.
- *Square-class-resolved reflection convolution and the exact two-step law in ternary orthogonal groups*, 22 November 2026, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-square-class-resolved-reflection-convolution-and-the-exact-two-s--07f302b07493 .
- A. Singh and M. Thakur, *Reality Properties of Conjugacy Classes in Algebraic Groups*, arXiv:0804.1245, Sections 3.1–3.2.
- F. Digne and J. Michel, *Representations of Finite Groups of Lie Type*, Cambridge University Press, 1991, Section 15.9, character table of \(\operatorname{GL}_2(\mathbb F_q)\).
- V. R. T. Pantangi and P. Sin, *Perfect State Transfer in Graphs Related to Linear Groups in Two Dimensions*, *Algebraic Combinatorics* 9 (2026), doi:10.5802/alco.469, Sections 2.1, 3.1 and 4.1.
- P. Diaconis, A. Ram and M. Simper, *Double-coset Markov Chains*, *Forum of Mathematics, Sigma* 11 (2023), doi:10.1017/fms.2022.106.
