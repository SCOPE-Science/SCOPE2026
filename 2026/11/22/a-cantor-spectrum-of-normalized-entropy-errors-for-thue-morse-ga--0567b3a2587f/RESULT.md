# A Cantor spectrum of normalized entropy errors for Thue–Morse gap-shift covers

## Finding
Let \(\tau_d\) be the Thue–Morse digits, \(\tau_0=0\), \(\tau_d\equiv s_2(d)\pmod 2\). Let \(X\) be the bilateral binary gap shift in which the distance \(d\) between successive occurrences of the symbol 1 is permitted precisely when \(\tau_d=1\). Let \(X_N\) be its canonical length-\(N\) finite-type cover, and put \(h=h_{\mathrm{top}}(X)\) and \(h_N=h_{\mathrm{top}}(X_N)\), always using natural logarithms.

Let \(\lambda\) be the Komornik–Loreti constant, characterized by
\[
\sum_{d\ge1}\tau_d\lambda^{-d}=1,\qquad
\lambda\approx1.787231650182966,
\]
and set \(S=\sum_{d\ge1}d\tau_d\lambda^{-d}>0\). Define the one-sided Thue–Morse shift orbit closure \(\Omega=\overline{\{\sigma^N\tau:N\ge1\}}\subset\{0,1\}^{\mathbb N_0}\) and the continuous map
\[
\Phi(u)=\frac1S\sum_{j\ge0}(1-u_j)\lambda^{-j}.
\]
Then, **uniformly over every integer \(N\ge1\) as \(N\to\infty\)**,
\[
\boxed{\lambda^N(h_N-h)=\Phi(\sigma^N\tau)+O(N\lambda^{-N}).}
\]
The exact set of subsequential limits of \(\lambda^N(h_N-h)\) is \(\Phi(\Omega)\), a nonempty, compact, perfect, nowhere-dense, uncountable subset of the real line with Hausdorff dimension zero. In particular, the normalized entropy error has neither a limit nor a countable phase spectrum.

Moreover, for every \(N\ge1\), the two consecutive covers agree **if and only if** \(\tau_N=1\):
\[
X_N=X_{N+1}\quad\Longleftrightarrow\quad\tau_N=1.
\]
At stages with \(\tau_N=0\), the inclusion is strict and \(h_{N+1}<h_N\). Thus the exact plateau/strict-drop pattern itself is the Thue–Morse word.

## Assumptions and scope
The full alphabet is \(\{0,1\}\), the shift is two-sided, and a *return distance* \(d\ge1\) denotes the length between consecutive 1s, corresponding to the connecting word \(10^{d-1}1\). As usual, the closure of configurations with infinitely many 1s includes points with finite one-sided collections of 1s and the all-zero point. The set of allowed distances is \(D=\{d\ge1:\tau_d=1\}\). For \(N\ge1\), the canonical length-\(N\) cover consists of all configurations all of whose length-\(N\) words occur in \(X\); equivalently, one forbids every word of length at most \(N\) absent from \(X\). All assertions refer to these specific shifts, not arbitrary substitution systems or all automatic gap sequences.

The entropy \(h=\log\lambda\) and the fact that 1 has a **unique binary expansion** at \(\lambda\), namely \((\tau_d)_{d\ge1}\), are known results from the noninteger-base literature. The claimed new content is the uniform finite-cover entropy error, the complete **perfect zero-dimensional** accumulation set, and its exact automatic plateau law. The elementary renewal entropy equation itself is not claimed as new.

## Proof
**1. Exact finite-cover language.** A finite word belongs to \(\mathcal L(X)\) precisely when every distance \(d\) between consecutive internal 1s satisfies \(\tau_d=1\): the forward direction follows from the definition, while the reverse follows by extending the word using arbitrarily many allowed distances \(d=1\) on both sides. Therefore the minimal forbidden words are exactly \(10^{d-1}1\) for \(\tau_d=0\). Such a word has \(d+1\) symbols and is forbidden by the length-\(N\) cover exactly if \(d<N\). Consequently \(X_N\) is the gap shift with permitted distances
\[
D_N=\{d<N:\tau_d=1\}\cup\{N,N+1,N+2,\ldots\}.
\]
This is a mixing finite-type shift because distance 1 remains allowed. The return-loop renewal equation for its entropy gives \(h_N=\log\lambda_N\), with \(\lambda_N>1\) the unique root of
\[
\sum_{1\le d<N}\tau_d\lambda_N^{-d}
+\frac{\lambda_N^{-N}}{1-\lambda_N^{-1}}=1.
\]
For the limiting shift, the standard renewal identity gives \(h=\log\lambda\), where \(\lambda\in(1,2)\) is uniquely determined by \(\sum_{d\ge1}\tau_d\lambda^{-d}=1\). The value is the Komornik–Loreti constant by the classical theorem on the unique expansion of 1. Since infinitely many distances are missing, \(h_N>h\) for all finite \(N\).

**2. Uniform finite-cover entropy correction.** Set \(q=\lambda^{-1}\), \(u=\log\lambda\), and define
\[
F(v)=\sum_{d\ge1}\tau_de^{-dv},\qquad
F_N(v)=\sum_{d<N}\tau_de^{-dv}+\sum_{d\ge N}e^{-dv}.
\]
The relevant roots are \(F(u)=1\) and \(F_N(u_N)=1\), where \(u_N=h_N\). At \(u\), the exact error is
\[
F_N(u)-F(u)=\sum_{d\ge N}(1-\tau_d)q^d
=q^N A_N,\qquad A_N=\sum_{j\ge0}(1-\tau_{N+j})q^j.
\]
The coefficients satisfy \(0<A_N\le(1-q)^{-1}\), uniformly in \(N\): strict positivity follows because each Thue–Morse tail contains zeros. Furthermore,
\[
F'(u)=-S,\qquad F_N'(u)=-S+O(Nq^N),
\]
and the second derivatives of \(F_N\) are uniformly bounded for \(v\) in a fixed neighborhood of \(u>0\). This last bound follows from comparison with \(\sum d^2e^{-dv}\), uniformly for \(v\) bounded away from zero. Monotonicity and the mean-value theorem give \(u_N-u=O(q^N)\). Taylor expansion of \(F_N(u_N)=1\) at \(u\) now yields
\[
0=q^N A_N-S(u_N-u)
+O(Nq^N|u_N-u|)+O(|u_N-u|^2),
\]
hence
\[
u_N-u=\frac{q^N A_N}{S}+O(Nq^{2N}).
\]
Multiplying by \(q^{-N}=\lambda^N\) proves the uniform boxed assertion.

**3. Exact accumulation set.** The one-sided Thue–Morse word is uniformly recurrent and not eventually periodic, by its primitive constant-length substitution \(0\mapsto01,1\mapsto10\). Its orbit closure \(\Omega\) is therefore compact and minimal; every element of \(\Omega\) is the limit of a subsequence of \(\sigma^N\tau\) with \(N\to\infty\). The series defining \(\Phi\) converges uniformly, so \(\Phi\) is continuous. The error in Step 2 tends to zero. Thus the complete cluster set of the normalized entropy errors is exactly \(K=\Phi(\Omega)\).

**4. No isolated phases: the univoque argument.** We first prove that the real numbers \(\Phi(\sigma^n\tau)\), \(n\ge1\), are pairwise distinct. If \(\Phi(\sigma^n\tau)=\Phi(\sigma^m\tau)\) for \(1\le n<m\), the constant contributions from the complements cancel, and therefore
\[
\sum_{j\ge0}\tau_{n+j}q^j
=\sum_{j\ge0}\tau_{m+j}q^j.
\]
Splicing the later digit tail \(\tau_m\tau_{m+1}\cdots\) in place of the tail beginning at \(\tau_n\) in the series \(1=\sum_{d\ge1}\tau_dq^d\) would give a second binary expansion of 1 at the Komornik–Loreti base. The two expansions differ, since equality of these tails as digit sequences would make \(\tau\) eventually periodic with period \(m-n\). This contradicts the known univoque property. Hence all orbit values are distinct.

Suppose \(y\in K\) were isolated in \(K\). The set \(\Phi^{-1}(\{y\})\) would then be a nonempty open subset of \(\Omega\). Density and uniform recurrence of the Thue–Morse orbit imply that this open subset is visited infinitely often by \(\sigma^n\tau\), giving repeated orbit values \(\Phi(\sigma^n\tau)=y\). This contradicts their pairwise distinctness. Therefore \(K\) has no isolated points and, being nonempty compact, is perfect and uncountable.

**5. Hausdorff dimension zero.** Fix \(r\ge1\), and choose a power of two \(L\) with \(r\le L<2r\). The Thue–Morse word is partitioned into length-\(L\) substitution blocks, each of only two possible types, the images of 0 and 1. Every length-\(r\) factor is contained in at most two consecutive blocks; there are at most four ordered block-type pairs and fewer than \(L\) starting offsets. Its factor complexity therefore obeys \(p_\tau(r)\le4L<8r\). For any two \(u,v\in\Omega\) with the same first \(r\) digits,
\[
|\Phi(u)-\Phi(v)|\le\frac{q^r}{S(1-q)}.
\]
The compact set \(K\) is thus covered by at most \(8r\) intervals of diameters \(q^r/(S(1-q))\). For every real \(s>0\), their total \(s\)-dimensional content is at most \(8r(q^r/[S(1-q)])^s\to0\). Hence \(\dim_HK=0\). In particular \(K\) has empty interior and is nowhere dense. A nonempty compact perfect nowhere-dense subset of \(\mathbb R\) is a Cantor set, finishing the phase-spectrum proof.

**6. Exact plateau pattern.** Passing from \(X_N\) to \(X_{N+1}\) adds the potential forbidden return word \(10^{N-1}1\). If \(\tau_N=1\), it is allowed in \(X\) and no new forbidden word is introduced, giving equality. If \(\tau_N=0\), the periodic configuration \((10^{N-1})^{\mathbb Z}\) lies in \(X_N\) but not \(X_{N+1}\). The latter is a proper subshift of the mixing SFT \(X_N\), so its entropy is strictly smaller. Both assertions follow for all \(N\ge1\).

## Verification
The self-contained `check.py` uses only the Python standard library. Execute `python check.py` from the directory containing the file. It calculates 85-digit decimal approximations to \(q\), \(h\), and \(S\), solves the finite-cover return equations for 22 specified cover lengths up to 160, and compares each normalized entropy excess with the corresponding Thue–Morse tail phase. In a separate finite-language test, it compares direct return-distance membership with a finite-state presentation over all binary words of lengths 1 through 12 and cover lengths 1 through 10: **81,900** word-membership comparisons. All completed successfully. Finite decimal work truncates infinite series at 360 digits and is only corroboration; the proof for all cover lengths is the analytic and symbolic argument above. Numerical values are \(h\approx0.580667858544257\) and \(S\approx1.806195500658231\).

## Relationship to prior work
Coles–Cyr–Kra–Pavlov (2026) develop canonical finite-type covers and characterize entropy stability, but do not give the Thue–Morse finite-cover error spectrum. Baker–Ghenciu (2014), §4.1, connect gap-shift entropy to noninteger expansions and explicitly identify the Komornik–Loreti Thue–Morse instance; these results establish the base and uniqueness used in Step 4, not its cover-error spectrum. Classical Thue–Morse theory supplies the minimality, aperiodicity, and linear factor complexity used in Steps 3–5.

The published *A countable entropy-phase spectrum in finite-type covers of geometric gap shifts* (2026) obtains a countable cluster set for return distances \(1,b,b^2,\ldots\). Its hypotheses do not include the non-eventually-periodic Thue–Morse allowed-distance set. The present claim differs not in the generic renewal Taylor formula, but in the **perfect uncountable, dimension-zero** cluster set forced by an aperiodic substitution and a univoque base, and in the automatic exact plateau pattern. Previously established residue-phase calculations for *eventually periodic* return-distance sets produce finite clusters and likewise do not imply this Cantor structure.

## Limitations
The theorem treats one specific Thue–Morse gap shift and its canonical length covers. It does not classify all automatic or low-complexity distance sets, establish uniqueness of maximal-entropy measures, or assert that \(\Phi\) is injective on the entire orbit closure (only distinctness of the forward orbit values is proved and needed). The dimension-zero property concerns the real normalized-error **cluster set**, not the entropy or dimension of the underlying symbolic system. Known univoque expansion and renewal facts are quoted with attribution. No independent audit or exhaustive historical-priority guarantee is claimed.

## References
1. S. Coles, V. Cyr, B. Kra, R. Pavlov, *Stable covers of subshifts*, arXiv:2602.04097v1, first made public 2026-02-04, §§2.2 and 3.3. https://arxiv.org/abs/2602.04097
2. S. Baker, A. E. Ghenciu, *Dynamical properties of S-gap shifts and other shift spaces*, arXiv:1411.7167v1, 2014-11-26, Proposition 2.1 and §4.1, Theorem 4.7. https://arxiv.org/html/1411.7167v1
3. V. Komornik, P. Loreti, *Unique developments in non-integer bases*, American Mathematical Monthly 105 (1998), 636–639; the univoque fact is also explicitly stated in [2].
4. *A countable entropy-phase spectrum in finite-type covers of geometric gap shifts*, public research record, 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-countable-entropy-phase-spectrum-in-finite-type-covers-of-geom--1fd88ee11f52
5. J.-P. Allouche, J. Shallit, *The ubiquitous Prouhet–Thue–Morse sequence*, in *Sequences and their Applications* (1999), 1–16, for substitution and factor structure.
