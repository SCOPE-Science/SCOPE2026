# Exceptional-rank sharp sixth moments and exact deficits for the fundamental character of \(\mathrm{SU}(N)\)

## Finding

Let \(N\ge3\) be an integer, let \(G=\mathrm{SU}(N)\) carry probability Haar measure, and write \(X(g)=\operatorname{tr}(g)\) for the *unnormalized* defining character. Its contragredient character is \(\overline{X(g)}\), and these two distinct irreducible characters are orthonormal in \(L^2(G)\). For \(a,b\in\mathbb C\), set \(F_{a,b}=aX+b\overline X\) and \(S=|a|^2+|b|^2\).

**Sharp sixth-moment theorem.** For every \(a,b\in\mathbb C\),
\[
\int_G|F_{a,b}(g)|^6\,dg\le K_N S^3,
\qquad
K_N=\begin{cases}
65/4,&N=3,\\
21,&N=4,\\
61/4,&N=6,\\
15,&N=5\text{ or }N\ge7.
\end{cases}
\]
Every constant is attained. If \(S>0\), equality requires \(|a|=|b|\ne0\), together with the following precise relative-phase condition: \((a\overline b)^3\) must be positive real when \(N=3\) or \(6\); \((a\overline b)^2\) must be positive real when \(N=4\); and there is no relative-phase restriction when \(N=5\) or \(N\ge7\). These are all nonzero equality cases. The zero function trivially gives equality.

More strongly, put \(p=|a|^2\), \(q=|b|^2\), \(w=a\overline b\), and \(M_N=\int_G|F_{a,b}|^6dg\). The **exact complex-coefficient moment polynomial** is
\[
M_N=6S^3+36Spq+
\begin{cases}
10\operatorname{Re}(w^3),&N=3,\\
24S\operatorname{Re}(w^2),&N=4,\\
2\operatorname{Re}(w^3),&N=6,\\
0,&N=5\text{ or }N\ge7.
\end{cases}
\]
Consequently, the **sharp global deficit identity** \(D_N=K_NS^3-M_N\) is
\[
D_N=\begin{cases}
9S(p-q)^2+10\bigl(S^3/8-\operatorname{Re}(w^3)\bigr),&N=3,\\
15S(p-q)^2+24S\bigl(pq-\operatorname{Re}(w^2)\bigr),&N=4,\\
9S(p-q)^2+2\bigl(S^3/8-\operatorname{Re}(w^3)\bigr),&N=6,\\
9S(p-q)^2,&N=5\text{ or }N\ge7.
\end{cases}
\]
Each summand displayed is nonnegative. In particular, the coefficient-balance stability bound \(D_N\ge9S(p-q)^2\) holds for every \(N\ge3\) and is globally exact in the stable ranks; in rank four its balance coefficient improves to \(15\). The rank-dependent sharp constants are nonmonotone: \(K_4>K_3>K_6>K_5=K_7=K_8=\cdots\). The phase optimizer changes from a finite set of relative phases at ranks \(3,4,6\) to a full phase circle in the stable ranks.

## Assumptions and scope

The representation is the ordinary, dimension-*unnormalized* trace of the defining \(N\)-dimensional complex representation; it is not a matrix entry, normalized trace, or adjoint character. The group is the compact *special* unitary group, not \(\mathrm U(N)\). Haar measure is normalized to total mass one. All coefficients are complex, and the restriction \(N\ge3\) is essential because the fundamental representation of \(\mathrm{SU}(2)\) is self-dual. The theorem concerns the two-dimensional complex central Fourier space \(\operatorname{span}\{X,\overline X\}\) and the sixth moment only. Since \(\|F_{a,b}\|_2^2=S\), the inequality is the exact \(L^2\)-to-\(L^6\) norm on that space, with the sixth power of its sharp constant equal to \(K_N\).

## Proof

**1. Tensor-power character moments.** Let \(V=\mathbb C^N\) be the defining representation. For a partition \(\lambda\vdash r\) of length at most \(N\), denote by \(f^\lambda\) the number of standard Young tableaux of shape \(\lambda\), and pad \(\lambda\) with trailing zeros to length \(N\). Schur--Weyl duality gives
\[
X(g)^r=\sum_{\substack{\lambda\vdash r\\\ell(\lambda)\le N}}f^\lambda\,\chi_\lambda(g).
\]
On restriction from \(\mathrm U(N)\) to \(\mathrm{SU}(N)\), two polynomial irreducible characters \(\chi_\lambda\) and \(\chi_\mu\) become equivalent exactly when \(\lambda_i-\mu_i=t\) for one integer \(t\) and all \(i=1,\dots,N\). Indeed their successive highest-weight differences agree if and only if all components differ by the same integer; this corresponds to tensoring by an integral power of the determinant, which is trivial on \(\mathrm{SU}(N)\). Character orthogonality therefore gives the exact formula
\[
\int_G X(g)^r\overline{X(g)}^{\,s}\,dg
=\sum_{\substack{\lambda\vdash r,\,\mu\vdash s\\
\ell(\lambda),\ell(\mu)\le N\\
\lambda_i-\mu_i=(r-s)/N\ \forall i}}
f^\lambda f^\mu,
\]
with the sum empty unless \(N\) divides \(r-s\). The equality criterion of restricted highest weights also makes this formula valid when both sides contain multiple copies.

**2. All moments of total order six.** If \(r+s=6\), the center of \(\mathrm{SU}(N)\) immediately forces the moment to vanish unless \(N\mid(r-s)\). For \(r=s=3\), the partitions \((3)\), \((2,1)\), \((1,1,1)\) contribute \(1^2+2^2+1^2=6\) for every \(N\ge3\). Other contributions are possible only at the following ranks and exponents:
\[
\begin{array}{c|c|c|c}
N& (r,s)& \text{unique relevant partition pair}&\text{moment}\\\hline
3&(6,0),(0,6)&(2,2,2),\varnothing&5\\
4&(5,1),(1,5)&(2,1,1,1),(1)&4\\
6&(6,0),(0,6)&(1,1,1,1,1,1),\varnothing&1.
\end{array}
\]
The hook-length formula \(f^\lambda=r!/\prod_{u\in\lambda}h(u)\) yields the integers \(5,4,1\). There are no additional cases: \(|r-s|\le6\), and \(r-s\) is even, so the center condition leaves precisely ranks \(3,4,6\) aside from \(r=s\). These computations give a complete six-degree moment table, rather than an asymptotic argument.

**3. Exact expansion for arbitrary phases.** Expand
\[
|aX+b\overline X|^6=(aX+b\overline X)^3(\overline a\overline X+\overline bX)^3.
\]
If \(j\) factors of \(aX\) and \(k\) factors of \(\overline a\overline X\) are chosen, the resulting moment is of type \((r,s)=(3+j-k,3-j+k)\). The diagonal \(j=k\) contributes
\[
6\sum_{j=0}^3{3\choose j}^2p^jq^{3-j}
=6S^3+36Spq.
\]
At rank \(3\) and rank \(6\), the only off-diagonal terms are \((j,k)=(3,0),(0,3)\), producing respectively \(10\operatorname{Re}(w^3)\) and \(2\operatorname{Re}(w^3)\). At rank \(4\), the pairs \((2,0),(3,1)\) and their transposes contribute \(24S\operatorname{Re}(w^2)\). At every other rank no off-diagonal moments survive. This proves the claimed moment polynomial.

**4. Global optimization and all equality cases.** Since \(p,q\ge0\) and \(p+q=S\),
\[
S^2-4pq=(p-q)^2,\qquad
\operatorname{Re}(w^k)\le |w|^k=(pq)^{k/2}\le(S/2)^k.
\]
Subtraction of the proposed sharp value \(K_NS^3\) from the exact moment polynomial gives the four explicit deficit identities above, using only the equality \(\bigl|a\overline b\bigr|^2=pq\). Each deficit is nonnegative. For \(S>0\), equality in its positive balance term forces \(p=q=S/2\), and equality in the remaining nonzero phase term forces the stated positive-real condition on \(w^2\) or \(w^3\). Conversely these conditions make every deficit summand vanish, so all are attained. In the stable ranks there is no phase term, hence every balanced pair attains equality. This proves both the sharp constants and the complete equality classification.

## Verification

The accompanying standalone standard-library Python script `check.py` separately computes the integer moments from Schur--Weyl decompositions and by *independent* constant-term integration of the \(\mathrm{SU}(N)\) Weyl denominator. The latter expands the squared Vandermonde determinant over permutations and selects monomials of equal exponent in all \(N\) torus variables; it does not invoke Specht modules or the Schur--Weyl decomposition. The script checks mixed moments at ranks \(3,4,5,6\), all seven total-order-six moments for ranks \(3\) through \(13\), and the global polynomial and deficit identities over a finite grid of Gaussian-integer coefficient pairs. It also checks actual equality and strict-gap witnesses. The recorded run in `check_output.txt` passes **27,695 assertions**. This is reproducible finite corroboration; the proof of the theorem for all \(N\) and all complex coefficients is Steps 1--4, not finite enumeration.

## Relationship to prior work

Schur--Weyl duality, character orthogonality, hook lengths, and Haar trace-moment methods are classical and are used here without novelty claims. Jonnadula--Keating--Mezzadri's 2020 preprint treats the broader symmetric-function framework for trace moments and develops unitary-invariant Hermitian ensemble formulas. Its verified statements and the material inspected do not give this exact two-character \(\mathrm{SU}(N)\) sharp sixth-moment optimization, full relative-phase classification, or global nonnegative deficit. The contribution here is the rank-uniform **sharp optimization and exact stability identity**, with the exceptional rank-four amplification and its nonmonotone behavior; it is not a claim of discovering a new integration method.

Relevant published fourth-moment calculations for small special-unitary character packets, and compact-group moment results for other groups, concern different characters or moment degrees; such results do not imply the all-rank sixth-moment statement above without additional computation and optimization. General trace-moment expansions are substantial prior foundations, and any stronger specialized formula in older literature could affect priority. Originality is assessed on a best-knowledge basis only.

## Limitations

No claim is made for the second-order structure of the complete \(L^6\)-unit sphere outside this two-character central subspace, for noninteger exponents, for arbitrary irreducible \(\mathrm{SU}(N)\) characters, or for \(N=2\). The numerical checker does not independently certify the universal representation-theoretic lemma; it checks it in finite ranks, alongside a genuinely different Weyl integration computation. Independent proof and priority review have not been performed. An undiscovered equivalent special-unitary trace-moment optimization in older literature remains an explicit originality risk.

## References

1. B. Jonnadula, J. P. Keating, and F. Mezzadri, *Symmetric Function Theory and Unitary Invariant Ensembles*, arXiv:2003.02620, first public version 2020-03-05; *Journal of Mathematical Physics* **62** (2021), 093512, DOI 10.1063/5.0048364. This is the dated, relevant trace-moment-framework lead source.
2. P. Diaconis and M. Shahshahani, *On the eigenvalues of random matrices*, *Journal of Applied Probability* **31A** (1994), 49--62. Classical compact-unitary trace moments and representation-theoretic background; not claimed as a new method here.
3. E. S. Meckes, *The Random Matrix Theory of the Classical Compact Groups*, Cambridge University Press, 2019. Background on Haar unitary traces and compact-group moments.
