# A sharp four-torsion bifurcation in Peirce spectra of finite abelian core quandles

## Finding

Let \(G\) be any finite abelian group, possibly trivial. Equip the complex vector space \(\mathcal A_G=\mathbb C[\operatorname{Core}(G)]\) with the basis \(\{e_g:g\in G\}\) and bilinear product \(e_xe_y=e_{2y-x}\). For each nonzero idempotent \(u\in\mathcal A_G\) (meaning \(u^2=u\)), define the **right Peirce operator** \(\rho_u(v)=vu\). The Peirce spectrum \(\Sigma(G)\) is the union of the eigenvalue sets of all these operators.

**Theorem.** Every \(\rho_u\) is diagonalizable over \(\mathbb C\). Moreover,
\[
\Sigma(G)=\begin{cases}
\mathbb C,&\text{if }G\text{ has an element of order }4;\\
\{0,1,-1\},&\text{if }G\text{ has no element of order }4\text{ but has an element of odd order }>1;\\
\{1\},&\text{if }G\text{ has exponent dividing }2.
\end{cases}
\]
The alternatives are exhaustive. In particular, for dihedral quandles of even order \(R_{2m}=\operatorname{Core}(\mathbb Z/(2m))\), the spectrum is \(\mathbb C\) precisely when \(m\) is even, and is \(\{0,1,-1\}\) when \(m>1\) is odd; \(R_2\) has spectrum \(\{1\}\).

For a constructive witness of the first case, choose any character \(\chi:G\to\{1,-1,i,-i\}\) of exact order four. Then, for **every** \(\lambda\in\mathbb C\),
\[
u_\lambda=\frac1{|G|}\sum_{g\in G}\bigl(1+\lambda\chi(g)^2\bigr)e_g
\]
is a nonzero idempotent, and \(\lambda\) and \(-\lambda\) are eigenvalues of \(\rho_{u_\lambda}\).

## Assumptions and scope

All groups are finite **abelian** groups, including the one-element group. The coefficient field is \(\mathbb C\); no analogous statement over arbitrary characteristics is asserted. A nonzero idempotent is required in defining \(\Sigma(G)\), in line with the Peirce-spectrum convention in the motivating literature. If the zero idempotent were admitted, it would contribute the eigenvalue zero even for a trivial quandle. An element of order four exists exactly when the exponent of the Sylow-two subgroup is at least four. For groups with no element of order four, the Sylow-two subgroup is elementary abelian, and a nontrivial odd-order subgroup exists precisely in the middle case.

## Proof

**1. Fourier multiplication and idempotency.** Write the character group multiplicatively as \(\widehat G\), and for \(v=\sum_g v_g e_g\) put \(\widehat v(\psi)=\sum_gv_g\psi(g)\). The product is the group-ring transport of \(\operatorname{Core}(G)\): its two exponent maps are inversion and doubling. Therefore for all \(v,u\in\mathcal A_G\),
\[
\widehat{vu}(\psi)=\widehat v(\psi^{-1})\widehat u(\psi^2).
\tag{1}
\]
This also follows directly by summing the basis products \(e_{2y-x}\). Set \(c_\psi=\widehat u(\psi)\). Idempotency is equivalent to
\[
c_\psi=c_{\psi^{-1}}c_{\psi^2}\qquad(\psi\in\widehat G).
\tag{2}
\]
Equation (2) immediately implies that \(c_\psi\ne0\) if and only if \(c_{\psi^{-1}}\ne0\). The reverse implication follows by applying (2) to \(\psi^{-1}\). Also \(c_1\in\{0,1\}\).

**2. Uniform diagonalizability.** Fourier transform is an invertible linear change of coordinates. In the coordinate pair \(\{\psi,\psi^{-1}\}\), when \(\psi\ne\psi^{-1}\), equation (1) gives the matrix
\[
\begin{pmatrix}0&c_{\psi^2}\\c_{\psi^{-2}}&0\end{pmatrix}.
\tag{3}
\]
The two off-diagonal entries are simultaneously zero or simultaneously nonzero by the support implication in step 1. The zero matrix is diagonalizable. In the nonzero case the two eigenvalues are the distinct numbers \(\pm\sqrt{c_{\psi^2}c_{\psi^{-2}}}\), so the block is diagonalizable. If \(\psi=\psi^{-1}\), then \(\psi^2=1\), and the single coordinate has scalar eigenvalue \(c_1\). All blocks are diagonalizable, proving the first assertion.

**3. The no-four-torsion upper bound.** Suppose \(G\) has no element of order four. The two-primary part of \(\widehat G\) then has exponent at most two. Let \(H\) be the odd-order subgroup of \(\widehat G\). Every square \(\psi^2\) lies in \(H\). We show that for every \(\eta\in H\),
\[
P_\eta:=c_\eta c_{\eta^{-1}}\in\{0,1\}.
\tag{4}
\]
If \(c_\eta=0\), this is clear. Otherwise (2) shows that both \(c_{\eta^{-1}}\) and \(c_{\eta^2}\) are nonzero. Therefore the nonzero support of \(c\), restricted to \(H\), is preserved by squaring. Squaring is a permutation of finite \(H\); its nonzero support is consequently a union of full squaring cycles. Multiplying (2) at \(\eta\) and \(\eta^{-1}\) gives \(P_\eta=P_\eta P_{\eta^2}\). Since the entire cycle has nonzero \(P\), this forces \(P=1\) on every member of the cycle, establishing (4). Each block in (3) consequently has eigenvalues in \(\{0,1,-1\}\), while the one-coordinate blocks have eigenvalues \(0\) or \(1\). Thus \(\Sigma(G)\subseteq\{0,1,-1\}\).

**4. Attainment and the exponent-two boundary.** If \(G\) has exponent dividing two, then \(2y-x=x\) for every \(x,y\); the quandle is trivial. Writing \(\varepsilon(u)=\sum_g u_g\), we have \(vu=\varepsilon(u)v\). A nonzero idempotent requires \(\varepsilon(u)=1\), so every \(\rho_u\) is the identity and \(\Sigma(G)=\{1\}\), including the one-element group.

Otherwise, still assuming no element of order four, suppose that \(G\) has a nontrivial odd-order element \(a\). The basis idempotent \(e_0\) has \(\rho_{e_0}(e_0)=e_0\) and \(\rho_{e_0}(e_a-e_{-a})=-(e_a-e_{-a})\); hence \(1,-1\in\Sigma(G)\). The uniform element \(\omega=|G|^{-1}\sum_g e_g\) is an idempotent because each basis right translation permutes \(G\) and therefore \(\omega e_y=\omega\) for all \(y\). Since \(2G\) contains a nonzero element \(b\), the two images \(\rho_\omega(e_0)\) and \(\rho_\omega(e_b)\) are the same uniform sum over \(2G\). Thus \(\rho_\omega(e_0-e_b)=0\), proving \(0\in\Sigma(G)\). The middle alternative is exact.

**5. Four-torsion forces the full complex plane.** Suppose \(G\) has an element of order four. The structure theorem for finite abelian groups supplies a character \(\chi\) of exact order four. Put \(\eta=\chi^2\), a nontrivial character taking values in \(\{1,-1\}\). For an arbitrary \(\lambda\in\mathbb C\), define \(u_\lambda\) as in the statement. Character orthogonality gives \(\varepsilon(u_\lambda)=1\), \(\widehat{u_\lambda}(1)=1\), and \(\widehat{u_\lambda}(\eta)=\lambda\). For every \(y\in G\), \(\eta(2y-x)=\eta(x)\); hence each right translation fixes \(u_\lambda\): \(u_\lambda e_y=u_\lambda\). Therefore \(u_\lambda^2=\varepsilon(u_\lambda)u_\lambda=u_\lambda\ne0\). For the Fourier pair \(\chi,\chi^{-1}\), (3) is
\[
\begin{pmatrix}0&\lambda\\\lambda&0\end{pmatrix},
\]
which has eigenvalues \(\pm\lambda\). Arbitrary \(\lambda\in\mathbb C\) therefore belongs to \(\Sigma(G)\), proving \(\Sigma(G)=\mathbb C\). The theorem is proved.

## Verification

The standalone script `verify.py` evaluates the actual multiplication tables \(e_xe_y=e_{2y-x}\) using exact SymPy arithmetic, independently of the Fourier proof. It checks basis and uniform idempotents, their Peirce spectra, explicit \(\pm1\) and zero eigenvectors at the indicated boundaries, and the formula for \(u_\lambda\) and both associated eigenvectors at six test values (including a nonreal parameter) for every tested four-torsion group. The 14 tested group presentations range in size from 1 to 12 and include cyclic and noncyclic mixed-primary examples. The recorded output is `verification_output.txt`; its terminal line is `VERIFY_OK configurations=14 exact_assertions=188 all_verified=yes`. Finite checks are corroboration, not a substitute for the all-groups proof.

## Relationship to prior work

Zhang (arXiv:2610.08204, first posted 2026-10-06), Proposition 5.1 and Theorem 5.5, establishes Fourier multiplication and the right Peirce spectrum \(\{0,1,-1\}\) for nontrivial **odd-order** abelian cores. The multiplication identity and odd-order result are used as established background; neither is new here. The new work covers all groups with even-order components, shows that elementary-two extensions retain the three-point spectrum when an odd component is present, and proves the sharp jump to the **entire complex plane** at four-torsion, as well as diagonalizability for all finite abelian cores.

Elhamdadi–Nunez–Singh (arXiv:2207.09257, §7) gives small-order Peirce calculations and proves that a particular non-Latin quandle of order three has full complex spectrum; it does not claim that all non-Latin core quandles do. Kaur–Singh (arXiv:2206.03162, §2) decomposes right modules for even dihedral quandles and describes parity-sensitive constituents but does not state a Peirce-spectrum classification over **all** idempotents. Their later Takasaki-module-decomposition work (arXiv:2303.06948, §§6.1–6.3, Theorems 6.3, 6.9, 6.12) decomposes regular right representations for arbitrary odd and even finite abelian groups. Its complete stated results concern irreducible constituents and orbit representations, not the eigenvalue union over all complex idempotents; this representation theorem supports the availability of small blocks but does not itself imply the three-case Peirce-spectrum classification. The manuscript was inspected through its final theorem and references. Elhamdadi–Ta–Virgin (arXiv:2609.03799) and Churchill–Churchill–Fernando–Kousik (arXiv:2608.09149) study idempotents and Fourier methods in the same family, especially integral coefficients; their available abstracts do not state the complex even-core Peirce classification, but full-text comparison was inaccessible and remains an explicit historical-priority risk. No uniqueness or priority is inferred merely from unsuccessful searches.

## Limitations

The result is confined to finite abelian cores over \(\mathbb C\), with **right** multiplication and **nonzero** idempotents. It does not determine all idempotents, their multiplicities, or Peirce spectra of general nonabelian cores, arbitrary Alexander quandles, or positive-characteristic coefficient fields. Prior work on representations and decomposition of Takasaki quandle rings supplies relevant semisimple modules that may subsume parts of the block decomposition; two plausible 2026 papers on Fourier methods and core-quandle idempotents could not be inspected in full text. The principal historical-priority risk is an equivalent even-core Peirce trichotomy under representation-theoretic terminology. Independent expert assessment has not been performed.

## References

1. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1 (2026-10-06), https://arxiv.org/abs/2610.08204 (especially §§2.1, 5.1, 5.3).
2. M. Elhamdadi, B. Nunez and M. Singh, *Enhancements of link colorings via idempotents of quandle rings*, arXiv:2207.09257v1 (2022-07-19), https://arxiv.org/html/2207.09257v1 (especially §§3, 7).
3. D. Kaur and P. Singh, *Decomposition of quandle rings of dihedral quandles*, arXiv:2206.03162 (2022-06-07), https://arxiv.org/abs/2206.03162 (especially §2).
4. D. Kaur and P. Singh, *Decomposition of quandle rings of Takasaki quandles*, arXiv:2303.06948 (2023-03-13), https://arxiv.org/abs/2303.06948.

5. M. Elhamdadi, L. Ta and B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799 (2026-09-03), https://arxiv.org/abs/2609.03799 (abstract consulted; full text unavailable during this review).
6. G. Churchill, I. R. Churchill, N. Fernando and B. Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149 (2026-08-10), https://arxiv.org/abs/2608.09149 (abstract consulted; full text unavailable during this review).
