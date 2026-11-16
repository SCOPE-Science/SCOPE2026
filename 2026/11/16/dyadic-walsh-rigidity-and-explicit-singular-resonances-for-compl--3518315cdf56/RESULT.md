# Dyadic Walsh rigidity and explicit singular resonances for complete-graph matchings

## Finding
For each integer \(n\ge 2\), consider the complete graph \(K_n\) with edge set \(E_n\), the finite abelian group \(G_n=(\mathbb F_2)^{E_n}\), and the indicator \(f_n\) of the edge-incidence vectors of **all** matchings of \(K_n\), including the empty matching. For any frequency graph \(H\subseteq K_n\), put
\[
 W_n(H)=\sum_{M\text{ matching in }K_n}(-1)^{|M\cap E(H)|}.
\]
Let \(I_0=I_1=1\) and \(I_k=I_{k-1}+(k-1)I_{k-2}\) for \(k\ge2\); these are the counts of involutions of a \(k\)-element set. Let \(m_j(H)\) count the size-\(j\) matchings contained in \(H\). Then, for every \(n\ge2\) and \(H\),
\[
\boxed{W_n(H)=\sum_{j=0}^{\lfloor n/2\rfloor}(-2)^j m_j(H)I_{n-2j}.}
\]
Write \(n=4q+r\), \(0\le r\le3\), and define \(\alpha_n=q\) for \(r=0,1\) and \(\alpha_n=q+1\) for \(r=2,3\). Every multiplier is divisible by \(2^{\alpha_n}\), and the following residue law is uniform over all frequency graphs:
\[
\boxed{
2^{-\alpha_n}W_n(H)\equiv
\begin{cases}
 1& r=0,1,\\
 1+|E(H)|&r=2,\\
 |E(H)|&r=3
\end{cases}
\pmod 2.}
\]
In particular, the greatest common divisor of the entire set of Walsh multipliers is exactly \(2^{\alpha_n}\). For \(n\equiv0,1\pmod4\), all multipliers are nonzero and convolution \(C_n g=f_n*g\) is invertible. For \(n\equiv2,3\pmod4\), at least half of all Walsh multipliers are nonzero, so \(\operatorname{rank}C_n\ge2^{\binom n2-1}\).

Moreover, for **every integer** \(s\ge1\), at \(n=s^2+2\) there is an explicitly constructible frequency \(H_s\) with \(W_n(H_s)=0\). Hence each member of this infinite square-shifted family has singular convolution. The positive spectral gap is at least \(2^{\alpha_n}\) in every dimension, giving the Hilbert-space bound \(\|C_n^\dagger\|_{2\to2}\le2^{-\alpha_n}\); when \(n\equiv0,1\pmod4\), the same bound applies to \(C_n^{-1}\).

## Assumptions and scope
All graphs have labelled vertices, all matchings include the empty matching, and frequency graphs may contain arbitrary sets of edges. Convolution and Fourier coefficients are **unnormalized** on the finite binary edge group; equivalently \((f_n*g)(x)=\sum_{y\in G_n}f_n(y)g(x-y)\). The corresponding characters are \(\chi_H(x)=(-1)^{\sum_{e\in E(H)}x_e}\), so \(\widehat f_n(H)=W_n(H)\). Rank and \(\ell^2\) norms refer to the full \(2^{\binom n2}\)-dimensional operator. No assertion of singularity is made for *all* dimensions congruent to two or three modulo four; the exhibited singular subfamily is \(n=s^2+2\).

## Proof
**Exact character expansion.** For every matching \(M\),
\[
(-1)^{|M\cap E(H)|}=\prod_{e\in M}(1-2\mathbf 1_{e\in E(H)})
=\sum_{F\subseteq M\cap E(H)}(-2)^{|F|}.
\]
A selected \(j\)-edge set \(F\) is possible precisely when it is a matching of \(H\), and it is contained in exactly \(I_{n-2j}\) matchings of \(K_n\) (freely match the remaining vertices). Summing over \(M\) and \(F\) gives the boxed expansion.

**Uniform two-adic residue.** The known involution valuation formula [1, Theorem 4.1] is
\[
 \nu_2(I_{4a})=\nu_2(I_{4a+1})=a,\quad
 \nu_2(I_{4a+2})=a+1,\quad
 \nu_2(I_{4a+3})=a+2.
\]
Here \(\nu_2\) denotes the exponent of two in a nonzero integer. It follows by direct consideration of \(j\) modulo two that for \(j\ge2\), every nonzero summand \((-2)^j m_j(H)I_{n-2j}\) is divisible by \(2^{\alpha_n+1}\). For \(j=0\), the exact two-adic order of \(I_n\), relative to \(\alpha_n\), is respectively \(0,0,0,1\) for \(r=0,1,2,3\). For \(j=1\), the term is \(-2|E(H)|I_{n-2}\): after division by \(2^{\alpha_n}\), its parity is zero when \(r=0,1\) and equals \(|E(H)|\) when \(r=2,3\). These observations establish the stated congruence. Taking \(H\) empty in classes \(r=0,1,2\) and taking \(H\) to have one edge in class \(r=3\) exhibits exact valuation \(\alpha_n\), proving the gcd assertion. When \(r=2,3\), exactly half the frequency graphs have even edge count and half have odd edge count; the congruence makes at least one of those two halves nonzero. For \(r=0,1\), every multiplier has exact valuation and none can vanish.

**Infinite singular family.** Fix \(s\ge1\) and \(n=s^2+2\). Distinguish two vertices \(a,b\), and put \(R=V(K_n)\setminus\{a,b\}\), so \(|R|=s^2\). Choose signs \(t_v\in\{+1,-1\}\) for \(v\in R\) satisfying \(\sum_{v\in R}t_v=s\); such signs exist because \(s^2\equiv s\pmod2\) and \(|s|\le s^2\). Give the edge \(ab\) weight \(-1\); edges \(av\) weight \(t_v\), edges \(bv\) weight \(-t_v\), and every edge within \(R\) weight \(+1\). These weights define the frequency graph \(H_s\) by taking exactly the negatively weighted edges.

Evaluate its signed matching sum by how \(a\) and \(b\) are covered. The contributions with neither distinguished vertex covered and with \(ab\) chosen cancel, because they are \(+I_{s^2}\) and \(-I_{s^2}\). Contributions in which exactly one of \(a,b\) is matched to a vertex of \(R\) cancel pairwise, using \(t_v+(-t_v)=0\). If both are matched separately to distinct \(u,v\in R\), the combined signed weight for the two possible assignments is \(-2t_ut_v\). For \(|R|\ge2\), the remaining vertices admit \(I_{s^2-2}\) matchings, hence
\[
 W_n(H_s)=-2I_{s^2-2}\sum_{u<v}t_ut_v
 =I_{s^2-2}\left(s^2-\Big(\sum_{v\in R}t_v\Big)^2\right)=0.
\]
For \(s=1\), no distinct pair \(u,v\) exists, so the preceding cancellation already gives zero. This proves all square-shifted singularities.

**Operator consequences.** The characters form an orthogonal eigenbasis for convolution, with eigenvalues \(W_n(H)\). Rank is the number of nonzero multipliers, and \(\|C_n^\dagger\|_{2\to2}\) is the reciprocal of their minimum positive absolute value. Divisibility gives the asserted gap and inverse-norm bound.

## Verification
The accompanying standalone Python checker constructs the complete matching indicator and runs an exact-integer fast Walsh transform for each \(2\le n\le7\), verifying \(2{,}131{,}018\) multipliers against the claimed parity residues. A separately coded negative-edge matching enumerator verifies every coefficient for \(n\le6\) and twelve distinct coefficients for \(n=7\). Exact involution valuations are tested through order 70. A separate dynamic program evaluates the explicit square witnesses for \(s=1,2,3,4\), corresponding to orders \(3,6,11,18\), with sum zero. The checker reports \(6{,}825\) zero frequencies at order six and \(269{,}577\) at order seven. Execute `python3 check_matching_fourier.py` with Python 3 and NumPy. These tests corroborate, but do not replace, the all-order proof.

## Relationship to prior work
The two-adic valuations of involution numbers used above are due to Amdeberhan and Moll [1], and classical monomer-dimer partition-function methods provide the background [2,3]. The exact all-frequency Walsh residue, the consequent inversion/rank laws, and the square-shifted explicit cancellation construction are the claims examined here. A separately indexed result on perfect matchings of \(K_8\) addresses a different, fixed-cardinality support, while a complete-graph monomer-dimer precision result concerns inverse covariance rather than Walsh convolution. Neither implication is asserted for their full texts when access was limited. The novelty assessment is bounded and not an exhaustive historical-priority certification.

## Limitations
The exact number of vanishing multipliers is not classified for every dimension congruent to two or three modulo four. The lower bound on nonzero multiplier magnitude may not be sharp in every dimension. The proof does not determine \(\ell^1\) or \(\ell^\infty\) endpoint projection constants, complex perturbations, or arbitrary base graphs. Historical overlap remains a possibility, and no independent mathematical review has been performed.

## References
[1] T. Amdeberhan and V. H. Moll, *Involutions and their progenies*, arXiv:1406.2356 (first posted 2014-06-09), especially Theorem 4.1.

[2] O. J. Heilmann and E. H. Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics 25 (1972), 190–232.

[3] A. Giuliani, I. Jauslin, and E. H. Lieb, *A Pfaffian formula for monomer-dimer partition functions*, arXiv:1510.05027 (first posted 2015-10-16).
