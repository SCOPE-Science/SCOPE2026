# Finite lacunary clusters preserve the Hilbert–Schmidt composition-symbol threshold

## Finding
Let \(F\subset\mathbb Z_{\ge0}\) be a fixed finite set of at least two offsets containing zero, and let \(\{N_j\}_{j\ge1}\) be strictly increasing positive integers satisfying \(N_{j+1}\ge qN_j\) for a fixed \(q>1\). Set
\[
\Lambda_F=\bigcup_{j\ge1}(N_j+F).
\]
Let \(\beta=(\beta_n)_{n\ge0}\) be positive with \(0<\beta_n\le1\), \(\inf_{n\notin\Lambda_F}\beta_n>0\), and \(\liminf_{n\to\infty}\beta_n^{1/n}\ge1\). On the analytic coefficient space \(H^2(\beta)\), put \(\|f\|_\beta^2=\sum_{m\ge0}\beta_m|\widehat f(m)|^2\). For an analytic disk self-map \(\varphi\), write \(\varphi\in\operatorname{HS}(\beta)\) when \(C_\varphi:f\mapsto f\circ\varphi\) is Hilbert–Schmidt on this space.

**Theorem.** For every fixed offset pattern \(F\) of at least two positions, including patterns with adjacent exceptional coefficient indices, and for every \(q>1\),
\[
\operatorname{HS}(\beta)=\operatorname{HS}(\mathbf1)
\quad\Longleftrightarrow\quad
\inf_{n\in\Lambda_F}n\beta_n>0.
\]
All indices in \(\Lambda_F\) are positive. Equality means equality of composition-symbol sets; no universal comparison constant for the Hilbert–Schmidt norms is asserted. In particular, taking \(F=\{0,1,2\}\), \(N_j=2^{j+3}\), and \(\beta_n=(n+1)^{-1}\) on \(\Lambda_F\) and one otherwise gives equality of the Hilbert–Schmidt symbol sets despite arbitrarily small weights on *three consecutive indices per lacunary scale*.

## Assumptions and scope
The coordinates \(N_j+F\) may overlap for finitely many initial \(j\). Because \(q>1\) and \(F\) is finite, all sufficiently late clusters are disjoint, and changing finitely many coefficients neither changes the threshold nor the Hilbert–Schmidt symbol sets. Positive weights and the root condition guarantee the analytic coefficient-space interpretation and bounded evaluation at disk points. The theorem concerns all analytic maps \(\varphi:\mathbb D\to\mathbb D\), not just maps fixing the origin.

Write \(P\) for the coefficient projection onto \(\Lambda_F\), and \(Q=I-P\) on classical \(H^2\). If \(c=\inf_{n\notin\Lambda_F}\beta_n>0\), then \(\|Qf\|_\beta^2\ge c\|Qf\|_2^2\). For each disk self-map,
\[
\|C_\varphi\|_{\operatorname{HS}(\beta)}^2
=\sum_{n\ge0}\frac{\|\varphi^n\|_\beta^2}{\beta_n},
\qquad
\|C_\varphi\|_{\operatorname{HS}(\mathbf1)}^2=\sum_{n\ge0}\|\varphi^n\|_2^2,
\]
where divergence is allowed and membership means finiteness.

## Proof
**1. Bounded Paley projection for a finite cluster template.** For every fixed \(r\in F\), the shifted sequence \(\{N_j+r\}_j\) is eventually Hadamard lacunary: the ratio of consecutive terms is bounded below by a fixed number greater than one. Paley's classical coefficient inequality for lacunary sets therefore bounds the \(\ell^2\)-norm of the coefficients on this shift by \(C_r\|f\|_{H^1}\), after adjusting a finite initial segment. Summing over the finitely many shifts gives
\[
\|Pf\|_2\le C_F\|f\|_{H^1},\qquad f\in H^1.
\]
This is the only ingredient from the Paley theorem needed below.

**2. A block lower bound for the high exceptional coefficients.** Let \(h\in H^\infty\) have first nonzero Taylor coefficient \(h_\ell\) in positive degree \(\ell>\max F-\min F\) (as \(0\in F\), it is enough that \(\ell>\max F\)). For all large \(j\), the output indices \(N_j+\ell+F\) are pairwise distinct and lie outside \(\Lambda_F\). Let \(R\) project onto those output indices and let \(P_{\ge J}\) project onto exceptional clusters numbered at least \(J\). The matrix of \(RM_hP_{\ge J}\), with input cluster coordinates \(N_j+r\) and output coordinates \(N_j+\ell+s\), is a block-diagonal operator plus a cross-cluster remainder. Its identical diagonal blocks are
\[
H=(h_{\ell+s-r})_{s,r\in F}.
\]
In increasing offset order, \(H\) is lower triangular, because \(h_t=0\) for \(t<\ell\), and every diagonal entry is \(h_\ell\ne0\). Hence its least singular value \(\sigma>0\).

For clusters \(j>k\), a cross-block matrix entry is \(h_{N_j-N_k+\ell+s-r}\); for \(j<k\) the entry is zero on a sufficiently late tail because multiplication is analytic. There is a uniform bound on the multiplicity of a positive difference \(d=N_j-N_k\): indeed \(N_k\le N_j/q\) forces
\[
d\le N_j\le\frac{q}{q-1}d,
\]
and this multiplicative interval contains at most \(1+\lceil\log_q(q/(q-1))\rceil\) members of the lacunary sequence. For fixed \(r,s\), the off-diagonal sum of squares is therefore bounded by that constant times \(\sum_{t\ge0}|h_t|^2\); finite \(F\) only multiplies the bound by \(|F|^2\). Consequently the cross-cluster remainder is Hilbert–Schmidt and therefore compact. Its restriction to sufficiently high input clusters has norm smaller than \(\sigma/2\). Thus
\[
\frac{\sigma}{2}\|P_{\ge J}f\|_2\le\|RQ(hP_{\ge J}f)\|_2,
\]
for every \(f\in H^2\) and sufficiently large \(J\), with the output projection restricted to high good rows. Writing \(P=P_{<J}+P_{\ge J}\), using \(\|hQf\|_2\le\|h\|_\infty\|Qf\|_2\), and bounding the finitely many low exceptional modes yields
\[
\|Pf\|_2\le A_h\bigl(\|Q(hf)\|_2+\|Qf\|_2+\|P_{<J}f\|_2\bigr)
\]
for a finite constant \(A_h\) independent of \(f\).

**3. Inclusion from the weighted space to the usual Hardy space.** Assume \(\varphi\in\operatorname{HS}(\beta)\). If \(\varphi\) is constant, its output is a one-dimensional space, and the root condition on \(\beta\) gives \(\sum_{n\ge0}|\varphi(0)|^{2n}/\beta_n<\infty\); therefore both composition operators are Hilbert–Schmidt. Otherwise let \(d\ge1\) be the smallest positive degree whose Taylor coefficient of \(\varphi\) does not vanish. Choose an integer \(k\) with \(\ell=kd>\max F\) and put \(h=(\varphi-\varphi(0))^k\). Its first nonzero term has degree \(\ell\), and \(h\in H^\infty\). Expand
\[
h\varphi^n=\sum_{t=0}^k\binom{k}{t}(-\varphi(0))^{k-t}\varphi^{n+t}.
\]
Applying the estimate from step 2 to \(f=\varphi^n\) shows that \(\|P\varphi^n\|_2\) is bounded by a fixed linear combination of \(\|Q\varphi^{n+t}\|_2\), \(0\le t\le k\), and \(\|P_{<J}\varphi^n\|_2\). Since \(\beta_m\le1\) and \(\beta_m\ge c\) off \(\Lambda_F\),
\[
\sum_{n\ge0}\|Q\varphi^n\|_2^2\le c^{-1}\|C_\varphi\|_{\operatorname{HS}(\beta)}^2<\infty.
\]
For each fixed low coefficient index \(m\), Cauchy's coefficient estimate on any circle \(|z|=\rho<1\) with \(\sup_{|z|=\rho}|\varphi(z)|=u<1\) gives \(|\widehat{\varphi^n}(m)|\le\rho^{-m}u^n\). Because \(P_{<J}\) has finite rank, \(\sum_n\|P_{<J}\varphi^n\|_2^2<\infty\). Squaring and summing the step-2 bound now proves \(\sum_n\|P\varphi^n\|_2^2<\infty\); together with the good coefficients this yields \(\varphi\in\operatorname{HS}(\mathbf1)\).

**4. Sufficiency of the weight threshold in the reverse direction.** Suppose \(\tau=\inf_{m\in\Lambda_F}m\beta_m>0\). For \(\varphi\in\operatorname{HS}(\mathbf1)\), set \(b_n=\|\varphi^n\|_2^2\). This is nonincreasing because \(|\varphi|\le1\) on the boundary. For \(m=N_j+r\) with \(r\in F\), \(1/\beta_m\le m/\tau\le(N_j+\max F)/\tau\). The lacunary window estimate
\[
\sum_j(N_j+\max F)b_{N_j+r}\le C(q,F,N_1)\sum_{n\ge0}b_n
\]
follows by charging the term at \(N_j+r\) to the disjoint interval of preceding indices \((N_{j-1},N_j]\), of length at least \((1-1/q)N_j\); finitely many initial indices are harmless. Summing over \(r\in F\), and using the uniform positive lower bound for other \(\beta_n\), gives \(\sum_n\|\varphi^n\|_\beta^2/\beta_n<\infty\). Thus \(\operatorname{HS}(\mathbf1)\subseteq\operatorname{HS}(\beta)\).

**5. Necessity of the weight threshold.** Suppose \(\inf_{m\in\Lambda_F}m\beta_m=0\). Select distinct exceptional indices \(p_k\to\infty\), sufficiently sparse that \(p_{k+1}\ge2p_k\) and \((p_k\beta_{p_k})^{-1}\ge4^k\). Choose disjoint boundary sets \(E_k\) with normalized Lebesgue masses \(\varepsilon/(2^kp_k)\), where \(\varepsilon>0\) is small. Define a boundary modulus by \(\rho^2=1-1/p_k\) on \(E_k\) and \(\rho^2=1/4\) elsewhere; take its bounded outer function \(\varphi\). Then
\[
\sum_{n\ge0}\|\varphi^n\|_2^2=\int_{\partial\mathbb D}\frac{dm}{1-\rho^2}
=\frac43(1-m(E))+\varepsilon\sum_k2^{-k}<\infty.
\]
Write \(I_k=\int_E\rho^{2p_k}dm\), so \(I_k\ge\tfrac14m(E_k)\). Cauchy–Schwarz gives
\[
\|\varphi^{p_k}\|_{H^1}\le m(E)^{1/2}I_k^{1/2}+2^{-p_k}.
\]
By step 1 and the choice of small \(\varepsilon\), for all large \(k\), \(\|P\varphi^{p_k}\|_2^2\le I_k/2\): the squared right-hand side is at most \(2C_F^2m(E)I_k+2C_F^2 4^{-p_k}\), and the second term is negligible compared with \(I_k\ge\varepsilon/(4\cdot 2^kp_k)\). Hence \(\|Q\varphi^{p_k}\|_2^2\ge\tfrac12 I_k\ge m(E_k)/8\). Therefore,
\[
\sum_n\frac{\|\varphi^n\|_\beta^2}{\beta_n}
\ge\frac{c\varepsilon}{8}\sum_k\frac{1}{2^kp_k\beta_{p_k}}
\ge\frac{c\varepsilon}{8}\sum_k2^k=\infty.
\]
This exhibits \(\varphi\in\operatorname{HS}(\mathbf1)\setminus\operatorname{HS}(\beta)\) and completes the equivalence.

## Verification
The analytic proof isolates its critical estimates: finite-union Paley inequality, uniformly bounded lacunary-difference multiplicity, invertibility of a finite triangular Toeplitz block, Hilbert–Schmidt compactness of off-block couplings, monotone lacunary charging, and the outer-modulus counterexample. The accompanying standalone Python program uses only exact rational arithmetic to corroborate block diagonalization, gap arithmetic and finite-coefficient identities in several sample finite templates. Running it with Python 3 prints `LACUNARY_CLUSTER_EXACT_BLOCK_CHECK_OK 1518`. These finite calculations are corroboration, not proof of the theorem for all sequences or symbols.

## Relationship to prior work
Cruz-Zamorano, Dellepiane and Seco prove in arXiv:2610.40148v1, Theorem 1.3(b), a sharp Hilbert–Schmidt symbol threshold for a *single* Hadamard-lacunary exceptional set when \(q>2\). Their use of the sum-free projection identity fails when the indices are grouped into finite clusters or the gap ratio drops below two. The present theorem covers any fixed finite offset pattern and all \(q>1\); the new coercivity mechanism is the uniformly invertible finite Toeplitz block plus compact off-block interactions. The earlier work of Lefèvre, Li, Queffélec and Rodríguez-Piazza gives bounded-composition classifications and does not directly settle equality of Hilbert–Schmidt symbol classes in this clustered sparse-weight regime.

## Limitations
The offsets must form a fixed finite pattern; this proof does not handle cluster widths growing with the lacunary scale, arbitrary sparse sets lacking finite-shift structure, or general Schatten classes \(p\ne2\). The norm comparison for the weighted-to-unweighted inclusion may depend on the composition symbol, and a uniform two-sided norm comparison is not asserted. Classical block-Toeplitz or lacunary-space arguments could contain equivalent statements under different terminology; publication priority has not been independently certified.

## References
1. F. J. Cruz-Zamorano, E. Dellepiane and D. Seco, *Compact and Hilbert–Schmidt composition operators on weighted Hardy spaces*, arXiv:2610.40148v1 (first posted 2026-10-29), https://arxiv.org/html/2610.40148v1 (Theorem 1.3, §4.2, Proposition 4.6, Paley projection).
2. P. Lefèvre, D. Li, H. Queffélec and L. Rodríguez-Piazza, *Characterization of weighted Hardy spaces on which all composition operators are bounded*, arXiv:2312.03482 (2023), https://arxiv.org/abs/2312.03482.
3. R. E. A. C. Paley, classical lacunary Fourier-coefficient inequality for \(H^1\), used as stated and discussed in reference 1, §4.
