# Joint value limits on multiplicatively pseudorandom sets
## Finding
Let \(R\subseteq\mathbb N\) be multiplicatively pseudorandom, let \(K\) be a compact metrizable abelian group, and let \(F:(\mathbb N,\times)\to K\) be a semigroup homomorphism. Put
\[
H=\overline{F(\mathbb N)}.
\]
Then the limit-point set of \(F(n)\) along \(n\in R\) is exactly \(H\).

For a finite tuple \(f_1,\ldots,f_r\) of unimodular completely multiplicative functions this gives
\[
\omega\bigl((f_1(n),\ldots,f_r(n))_{n\in R}\bigr)
=
\overline{\{(f_1(n),\ldots,f_r(n)):n\in\mathbb N\}}
\subseteq \mathbb T^r.
\]
Thus every target compatible with the algebraic relations among the coordinates occurs as a joint limit. For example, if the closed subgroup on the right is all of \(\mathbb T^r\), then every point of \(\mathbb T^r\) is approached along arbitrarily large elements of \(R\).

The same conclusion holds on the full Piatetski--Shapiro set \(\mathcal P_c\) for \(1<c<6/5\), and on every regular irrational nil-Bohr set.

## Assumptions and scope
Multiplicative pseudorandomness is exactly Definition 1.2 of Leung's arXiv:2610.00843v1. The target group \(K\) is assumed compact, metrizable, and abelian; metrizability is used only to phrase the conclusion as a sequential limit-point statement. No claim is made for nonabelian compact targets.

The Piatetski--Shapiro conclusion uses the source's Theorem 1.3, which provides a multiplicatively pseudorandom subset \(\mathcal P_c\cap\mathcal S_\delta\) for \(1<c<6/5\). The nil-Bohr conclusion uses Theorem 1.4, which says every regular irrational nil-Bohr set is multiplicatively pseudorandom.

## Proof
The closure of a subsemigroup of a compact group is a subgroup, so \(H\) is a compact abelian subgroup. Let \(m_H\) denote Haar probability measure on \(H\). For the multiplicative Følner sets \(\Phi_L\) used by the source, define
\[
\nu_{L,N}
=
\mathbb E_{Q\in\Phi_L}
\mathbb E_{\substack{n\le N\\Qn\in R}}
\delta_{F(Qn)}.
\]
This is a probability measure on \(H\) whenever the source's infinitude condition makes the inner averages defined.

Fix a character \(\chi\in\widehat H\). The scalar function
\[
g_\chi(n)=\chi(F(n))
\]
is unimodular and completely multiplicative. If \(\chi\) is nontrivial on \(H\), density of \(F(\mathbb N)\) in \(H\) implies \(g_\chi\not\equiv1\). Its Fourier coefficient against \(\nu_{L,N}\) is
\[
\widehat\nu_{L,N}(\chi)
=
\mathbb E_{Q\in\Phi_L}g_\chi(Q)
\mathbb E_{\substack{n\le N\\Qn\in R}}g_\chi(n).
\]
For fixed \(L\), multiplicative pseudorandomness replaces the inner mean uniformly over the finite set \(\Phi_L\) by the corresponding mean over \(n\in R\), up to a term tending to zero with \(N\). Hence
\[
\limsup_{N\to\infty}|\widehat\nu_{L,N}(\chi)|
\le
\left|\mathbb E_{Q\in\Phi_L}g_\chi(Q)\right|.
\]
Leung's Lemma 2.1 gives convergence of the right-hand side to zero as \(L\to\infty\) for every nontrivial \(\chi\). For the trivial character, the coefficient is exactly one. These are precisely the Fourier coefficients of \(m_H\).

Characters separate points of a compact abelian group, and their finite linear span is uniformly dense in \(C(H)\). Therefore, for every continuous \(\varphi:H\to\mathbb C\),
\[
\lim_{L\to\infty}\limsup_{N\to\infty}
\left|\int_H\varphi\,d\nu_{L,N}-\int_H\varphi\,dm_H\right|=0.
\]
Now let \(U\subseteq H\) be nonempty and open. Choose continuous \(\varphi\ge0\), not identically zero, with support contained in \(U\). Haar measure has full support, so \(\int_H\varphi\,dm_H>0\). It follows that for some fixed sufficiently large \(L\) and arbitrarily large \(N\), the measure \(\nu_{L,N}\) assigns positive \(\varphi\)-mass to \(U\).

To exclude the possibility that this mass comes only from finitely many small elements of \(R\), use the source's estimate (6.3): for every fixed cutoff \(x\) and fixed \(L\), the proportion of atoms with \(Qn<x\) tends to zero as \(N\to\infty\). Consequently, for every \(x\) there is an \(m\in R\) with \(m\ge x\) and \(F(m)\in U\). Every point of \(H\) is therefore a limit point along \(R\). The reverse inclusion is immediate because every value \(F(n)\) lies in \(H\).

For a tuple \((f_1,\ldots,f_r)\), take \(K=\mathbb T^r\) and \(F(n)=(f_1(n),\ldots,f_r(n))\). For \(\mathcal P_c\), apply the result to the pseudorandom subset \(\mathcal P_c\cap\mathcal S_\delta\); density of the limit set along that subset forces the same limit set along the larger set \(\mathcal P_c\). For a regular irrational nil-Bohr set, apply the theorem directly.

## Verification
The character reduction is exact: every \(\chi\circ F\) satisfies the scalar hypotheses used in Definition 1.2 and Lemma 2.1. The only non-source input is standard compact-abelian harmonic analysis: Haar measure has Fourier transform one at the trivial character and zero elsewhere, characters separate points, and their finite linear combinations are uniformly dense in continuous functions.

The source's tail estimate (6.3) was checked because weak convergence of the auxiliary measures alone would not guarantee arbitrarily large indices. The proof uses the same fixed-Følner-set-then-large-cutoff order as the source and does not interchange uncontrolled limits.

## Relationship to prior work
Leung's Theorem 6.1 determines scalar limit points for one unimodular completely multiplicative function: the finite cyclic group generated by its values in finite order, or the full circle in infinite order. Corollary 1.2 gives simultaneous approximation of finitely many such functions only near the identity. The finding above combines the characterwise version of the source's Fourier argument with compact-abelian harmonic analysis to identify the entire compatible joint limit subgroup, including targets away from the identity and algebraic relations between coordinates.

Leung's earlier arXiv:2608.27418 treats scalar value distribution along linear fractional sequences. Tardy's arXiv:2608.26814 concerns shifted two-point correlations of multiplicative functions. Neither inspected statement gives the compact-group or finite-tuple subgroup limit-set conclusion above.

## Limitations
The argument is qualitative: it proves arbitrarily large hits in every nonempty open subset of \(H\), but gives no rate and no positive relative density of such hits. It does not establish joint equidistribution of the tuple along \(R\); the source's scalar equidistribution criteria require additional non-pretentiousness hypotheses, and a multivariate equidistribution theorem would require corresponding conditions for all nontrivial characters of \(H\).

The novelty comparison is necessarily limited by indexing and the very recent date of the focal preprint; an unindexed equivalent compact-group formulation or a later revision could reduce originality.

## References
Sun-Kai Leung, *Multiplicative recurrence of Piatetski--Shapiro and nil-Bohr sets*, arXiv:2610.00843v1, 2026-09-30. Relevant material: Definition 1.2, Corollary 1.2, Theorems 1.3, 1.4, and 6.1, Lemma 2.1, equation (6.3), Appendix A.

Sun-Kai Leung, *Value distribution of multiplicative functions along linear fractional sequences*, arXiv:2608.27418, 2026.

Néo Tardy, *Two-point correlations of multiplicative functions*, arXiv:2608.26814, 2026.
