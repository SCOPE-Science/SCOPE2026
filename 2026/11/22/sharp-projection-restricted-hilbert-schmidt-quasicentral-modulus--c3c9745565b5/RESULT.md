# Sharp projection-restricted Hilbert–Schmidt quasicentral modulus of shift pairs

## Finding

Let \(S\) be the unilateral shift on \(\ell^2(\mathbb N_0)\). For integers \(p,q\ge0\), \(p+q\ge1\), put
\[
H_{p,q}=\ell^2(\mathbb N_0)^{\oplus(p+q)},\qquad
T_{p,q}=S^{\oplus p}\oplus(S^*)^{\oplus q}.
\]
For a bounded operator \(T\) on a separable Hilbert space, define the *projection-restricted Hilbert–Schmidt quasicentral modulus*
\[
\kappa^{\mathrm{proj}}_2(T)=
\inf_{(P_n)}\liminf_{n\to\infty}\|[T,P_n]\|_2,
\]
where each \(P_n\) is a finite-rank orthogonal projection and \(P_n\to I\) strongly. Compare the usual \(k_2(T)\) obtained by allowing finite-rank positive contractions \(0\le R_n\le I\).

**Theorem.** For every Hilbert–Schmidt perturbation \(K\in\mathcal S_2(H_{p,q})\),
\[
\boxed{\kappa^{\mathrm{proj}}_2(T_{p,q}+K)=\sqrt{|p-q|},\qquad k_2(T_{p,q}+K)=0.}
\]
The same value of \(\kappa^{\mathrm{proj}}_2\) results if the defining projections are required to satisfy \(P_n\le P_{n+1}\). The Fredholm index of \(T_{p,q}+K\) equals \(q-p\), so the positive projection gap is exactly the square root of the absolute index.

## Assumptions and scope

The Hilbert space is complex; the shift has multiplicity one in each summand, and the total multiplicity \(p+q\) is finite but arbitrary. The perturbation \(K\) is an arbitrary bounded Hilbert–Schmidt operator, with no normality or block-diagonal assumption. Hilbert–Schmidt norms use \(\|B\|_2^2=\operatorname{Tr}(B^*B)\), without dimension normalization. There is no assertion for general essentially unitary Fredholm operators or perturbations merely compact but not Hilbert–Schmidt.

## Proof

**1. A finite-projection trace obstruction.** For any bounded \(T\) and finite-rank orthogonal projection \(P\), decompose relative to \(P H\oplus(I-P)H\) and set
\[
B=PT(I-P),\quad C=(I-P)TP,\quad F=T^*T-TT^*.
\]
Finite-dimensional cyclicity of the trace in the \(P H\) corner gives
\[
\operatorname{Tr}(PFP)=\|C\|_2^2-\|B\|_2^2,
\qquad
\|[T,P]\|_2^2=\|B\|_2^2+\|C\|_2^2.
\]
Consequently,
\[
\|[T,P]\|_2^2\ge |\operatorname{Tr}(PFP)|.
\tag{1}
\]
For \(T=T_{p,q}\), \(F\) is the finite-rank difference of \(p\) rank-one initial-coordinate projections and \(q\) such projections with negative signs. Thus \(\operatorname{Tr}F=p-q\). For any strongly exhaustive projections \(P_n\), finite rank of \(F\) implies \(\operatorname{Tr}(P_nFP_n)\to p-q\). From (1),
\[
\liminf_n\|[T_{p,q},P_n]\|_2\ge\sqrt{|p-q|}.
\tag{2}
\]

**2. A matched forward/backward pair costs asymptotically nothing.** Identify the Hilbert space of \(S\oplus S^*\) with \(\ell^2(\mathbb Z)\): the forward copy corresponds to sites \(j\ge0\), the backward copy to sites \(j\le-1\). If \(U\delta_j=\delta_{j+1}\) is the bilateral shift, then
\[
U=(S\oplus S^*)+E,
\]
where \(E\) is the rank-one bridge mapping the backward initial vector to the forward initial vector. Under Fourier transform, \(U\) is multiplication by \(z\) on \(L^2(\mathbb T)\) with normalized Haar measure.

For \(N=2^m\), let \(Q_N\) project onto the \(N\)-dimensional space of functions constant on each of \(N\) equal arcs. These are nested finite-rank orthogonal projections, and \(Q_N\to I\) strongly. Each normalized arc indicator has mean multiplier of modulus \(\sin(\pi/N)/(\pi/N)\), so the two off-diagonal blocks of the multiplication operator give the exact identity
\[
\|[U,Q_N]\|_2^2=2N\left[1-\left(\frac{\sin(\pi/N)}{\pi/N}\right)^2\right]
=\frac{2\pi^2}{3N}+O(N^{-3})\longrightarrow0.
\tag{3}
\]
As \(E\) is Hilbert–Schmidt and \(Q_N\to I\) strongly, \(\|[E,Q_N]\|_2\to0\). Therefore matched copies of \(S\) and \(S^*\) admit nested strongly exhaustive finite-rank projections with commutator Hilbert–Schmidt norm tending to zero.

**3. Each excess shift costs exactly one squared unit.** For any remaining unpaired \(S\) or \(S^*\), let \(D_N\) be projection onto its first \(N\) basis vectors. Then \(D_N\uparrow I\) and
\[
\|[S,D_N]\|_2^2=\|[S^*,D_N]\|_2^2=1.
\tag{4}
\]
Take the direct sum of the \(\min(p,q)\) projections from (3) and the \(|p-q|\) coordinate projections from (4). These form a nested strongly exhaustive sequence. Orthogonality of direct-sum blocks yields the upper bound \(\sqrt{|p-q|}\), matching (2).

**4. Stability under Hilbert–Schmidt perturbations.** If \(K\in\mathcal S_2\) and bounded self-adjoint contractions \(R_n\to I\) strongly, then both \(\|(I-R_n)K\|_2\) and \(\|K(I-R_n)\|_2\) tend to zero, first for finite-rank \(K\) and then by Hilbert–Schmidt approximation. Thus \(\|[K,R_n]\|_2\to0\). It follows that every candidate sequence for either modulus has unchanged asymptotic cost after adding \(K\). This proves the projection formula for \(T_{p,q}+K\).

**5. Ordinary positive-contraction modulus.** For \(N\ge1\), let \(R_N\) be diagonal with entries \(r_j=\max(1-j/N,0)\) on each unilateral copy. Then \(0\le R_N\le I\), \(R_N\to I\) strongly, and
\[
\|[T_{p,q},R_N]\|_2^2=\frac{p+q}{N}\longrightarrow0.
\]
The Hilbert–Schmidt perturbation argument proves \(k_2(T_{p,q}+K)=0\). Finally, \(S\) has Fredholm index \(-1\), its adjoint index \(+1\), and Hilbert–Schmidt perturbations are compact, proving the index statement.

## Verification

Equation (1) follows by expanding the two off-diagonal blocks. In (3), the normalized arc indicators are orthonormal, and \(\|UQ_N\|_2^2=\|U^*Q_N\|_2^2=N\). Their diagonal compression has squared Hilbert–Schmidt norm \(N(\sin(\pi/N)/(\pi/N))^2\). Taylor expansion of \(\sin x/x\) proves the displayed asymptotic. Equation (4) has exactly one boundary-crossing matrix unit per unpaired copy. The optional diagnostic script checks the finite-dimensional trace identity and the decay in (3); it does not constitute a proof of the infinite-dimensional theorem.

## Relationship to prior work

Liu and Zhao proved in 2026 that the ordinary Hilbert–Schmidt quasicentral modulus vanishes for all almost normal bounded operators, using finite-rank **positive contractions** [1]. The present theorem addresses a stricter approximation class—orthogonal projections—and detects a nonvanishing sharp Fredholm-index obstruction within an almost-normal model family. The conventional zero-modulus conclusion is not presented as new. Voiculescu's survey uses the same positive-contraction definition and explains ideal perturbation invariance [2]. Davidson's 1988 work supplies classical Hilbert–Schmidt quasicentral approximation for normal operators [3]; the vanishing cost of the balanced sector is compatible with, and not claimed to supersede, that theory. The new assessed statement is the **complete sharp projection-only quantitative law for all finite shift multiplicities and their Hilbert–Schmidt perturbations**, not the trace-block identity or the elementary bilateral normal approximation separately.

## Limitations

The formula is restricted to the specified shift/direct-sum model up to Hilbert–Schmidt perturbation. It does not establish a projection-restricted modulus formula for arbitrary almost normal or essentially unitary operators. The original quantitative combination has not received an independent mathematical audit; an older unnamed index-theoretic equivalence remains a bibliographic possibility. A related 2019 paper by V. Lauric was accessible only through its abstract, which concerns a different commutator implication; no conclusion about its unread full text is asserted. Numerical tests validate only finite identities and convergence samples, never the universal theorem.

## References

[1] Shiqi Liu and Hongyin Zhao, *Quasicentral modulus for almost normal operators*, arXiv:2611.15604v1, first public 11 November 2026, https://arxiv.org/abs/2611.15604.

[2] Dan-Virgil Voiculescu, *Perturbations of operators and non-commutative condensers, an update on the quasicentral modulus*, arXiv:2503.23248v1 (2025), https://arxiv.org/abs/2503.23248.

[3] Kenneth R. Davidson, *Normal operators are diagonal plus Hilbert Schmidt*, Journal of Operator Theory 20 (1988), 241–249, https://jot.theta.ro/jot/archive/1988-020-002/1988-020-002-003.pdf.

[4] Vasile Lauric, *Some consequences of quasicentral approximate units modulo Hilbert-Schmidt class*, Mathematica Slovaca 69 (2019), 433–436, https://doi.org/10.1515/ms-2017-0235 (abstract inspected only).
