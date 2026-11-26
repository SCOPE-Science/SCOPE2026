# Three-scale optimal free-energy stability in the square-gap shift

## Finding

Let \(X_\square\subset\{0,1\}^{\mathbb Z}\) be the bilateral square-gap shift: between consecutive markers \(1\), there are exactly \(j^2\) zeros for some integer \(j\ge1\). For \(L>0\), put \(\phi_L=-L\mathbf1_{[1]}\), and let \(p_L=P_{X_\square}(\phi_L)\). Its unique equilibrium measure \(\mu_L\) has marker frequency \(\rho_L=\mu_L([1])\). For an invariant probability \(\nu\), define the free-energy deficit
\[
\Delta_L(\nu)=p_L-h_\nu(\sigma)+L\nu([1]).
\]
The **optimal global marker-frequency stability constant** and its **infinitesimal counterpart** are
\[
C_L=\sup_{\nu:\,\Delta_L(\nu)>0}\frac{|\nu([1])-\rho_L|}{\sqrt{\Delta_L(\nu)}},\qquad
C_L^{\mathrm{loc}}=\lim_{\epsilon\downarrow0}\sup_{\substack{\nu\text{ invariant}\\0<|\nu([1])-\rho_L|<\epsilon}}
\frac{|\nu([1])-\rho_L|}{\sqrt{\Delta_L(\nu)}}.
\]
Both constants are finite and strictly positive. As \(L\to\infty\),
\[
\boxed{\quad C_L^2=\frac1{2L}+\frac{e^{-3L/2}}{2L^2}+o\!\left(\frac{e^{-3L/2}}{L^2}\right),\qquad
C_L^{\mathrm{loc}}\sim\sqrt{2\pi}\,e^{-L}.\quad}
\]
Moreover, \(C_L\) is attained by an invariant measure for all sufficiently large \(L\), and for every choice of such maximizers their marker frequencies \(t_L^*\) obey
\[
\boxed{\quad t_L^*=\frac12-\frac34 e^{-3L/2}(1+o(1)).\quad}
\]
The equilibrium marker frequency obeys \(\rho_L\sim (\pi/2)e^{-2L}\). Thus the optimum global deviation lies exponentially near the densely marked alternating orbit, on a scale distinct from both the equilibrium density and its local susceptibility. The global leading constant is \(C_L\sim(2L)^{-1/2}\), even though local stability is exponentially stronger.

## Assumptions and scope

All logarithms are natural, entropy is per spatial coordinate, and invariant probabilities may be nonergodic or have an atom at the all-zero fixed point. The shift is the closure of bi-infinite concatenations of \(10^{j^2}\); return lengths are \(R_j=j^2+1\). The observable is the single marker cylinder \(\mathbf1_{[1]}\); the theorem does not claim the same sharp constant for arbitrary Hölder observables. An attaining measure must have maximum entropy among measures at its density. The theorem concerns \(L\to\infty\) in a fixed shift and does not assert uniqueness of the global maximizing density or attainment for every \(L>0\).

## Proof

**1. Renewal pressure and the exact constrained-entropy envelope.** For \(s>0\), write
\[
Z(s)=\sum_{j\ge1}e^{-s(j^2+1)},\quad m(s)=-\frac{d}{ds}\log Z(s),\quad V(s)=\frac{d^2}{ds^2}\log Z(s)>0,\quad t(s)=m(s)^{-1}.
\]
Because \(m'(s)=-V(s)<0\), \(m(s)\downarrow2\) as \(s\to\infty\), and \(m(s)\to\infty\) as \(s\downarrow0\), the parameter \(t(s)\) increases bijectively from \(0\) to \(1/2\). Let \(s(t)\) denote its inverse for \(0<t<1/2\). The maximal invariant entropy at marker frequency \(t\) is
\[
H(t)=s(t)+t\log Z(s(t)),\qquad H(0)=H(1/2)=0.\tag{1}
\]
To see this without assuming ergodicity, split an invariant measure into its all-zero atom and the remaining normalized component. The latter induces on the marker cylinder to a stationary return-length process with mean return \(1/u\), where \(u\) is its own marker density. The induced entropy rate is at most the entropy \(H(q)\) of its one-return distribution \(q\); Abramov's formula multiplies by the total marker frequency \(t\). For every \(s>0\), the relative-entropy inequality against \(q_s(j)=e^{-sR_j}/Z(s)\) gives
\[
 h_\nu(\sigma)\le t H(q)\le t\log Z(s)+s\,t\sum_jq_jR_j\le t\log Z(s)+s.
\]
Equality at an interior \(t\) requires no all-zero atom and iid returns with law \(q_{s(t)}\), and is attained by the stationary renewal lift. The endpoints are respectively the all-zero orbit and the alternating \(10\) orbit. This is the classical renewal variational mechanism, not an asserted new lemma.

The equation
\[
Z(p_L)=e^L\tag{2}
\]
has a unique solution \(p_L>0\). Its renewal lift maximizes \(H(t)-Lt\) and has \(\rho_L=t(p_L)\). In particular, \(H'(\rho_L)=L\), and (1) gives
\[
H'(t)=\log Z(s(t)),\qquad H''(t)=-\frac1{t^3 V(s(t))}<0.\tag{3}
\]
Strict concavity gives uniqueness of the maximizing density and equilibrium measure. Every deficit satisfies
\[
\Delta_L(\nu)\ge D_L(t):=p_L+Lt-H(t),\quad t=\nu([1]),
\]
with equality for the constrained-entropy renewal measures. Consequently
\[
C_L^2=\sup_{0\le t\le1/2,\,t\ne\rho_L}
\frac{(t-\rho_L)^2}{D_L(t)},\tag{4}
\]
where the quotient extends continuously to \(t=\rho_L\) by the value \(2/(-H''(\rho_L))\). The extended quotient has a finite positive maximum on \([0,1/2]\), equal to the supremum in (4). If a maximizing density differs from \(\rho_L\), its entropy-maximizing measure attains (4): the renewal measure at an interior density, or the indicated invariant measure at an endpoint. The extension value at \(\rho_L\) is only a limit of the quotient and does not itself give an attaining measure.

**2. Equilibrium scale and the exact local stability coefficient.** Jacobi's Gaussian transformation yields
\[
\sum_{j\ge1}e^{-sj^2}=\frac12\left(\sqrt{\frac\pi s}-1\right)
+\sqrt{\frac\pi s}\sum_{k\ge1}e^{-\pi^2 k^2/s}.
\]
Thus as \(s\downarrow0\), \(Z(s)\sim\sqrt\pi/(2\sqrt s)\), \(m(s)\sim1/(2s)\), and \(V(s)\sim1/(2s^2)\). Equation (2) therefore yields
\[
p_L\sim\frac\pi4e^{-2L},\qquad \rho_L\sim\frac\pi2e^{-2L},\qquad
\chi_L:=\rho_L^3 V(p_L)\sim\pi e^{-2L}.\tag{5}
\]
The quadratic Taylor expansion of \(D_L(t)\) at \(t=\rho_L\), together with (3), gives the exact identity
\[
C_L^{\mathrm{loc}}=\sqrt{\frac2{-H''(\rho_L)}}=\sqrt{2\chi_L}.
\]
Combined with (5), this proves the local asymptotic.

**3. The global maximizer tends to the densely marked boundary.** The alternating orbit gives
\[
C_L^2\ge\frac{(1/2-\rho_L)^2}{p_L+L/2}\sim\frac1{2L}.\tag{6}
\]
For a competing density \(t\ge L^{-2}\), the binary entropy bound \(H(t)\le -t\log t-(1-t)\log(1-t)\le t(1+\log(1/t))\) implies
\[
D_L(t)\ge t(L-1-2\log L),\quad
\sqrt L\frac{|t-\rho_L|}{\sqrt{D_L(t)}}\le(1+o(1))\sqrt t
\]
uniformly on this range, because \(\rho_L L^2\to0\). For \(t\le L^{-2}\), (3) and the theta asymptotics imply \(-H''(u)\ge1/(3u)\) whenever \(0<u\le L^{-2}\) and \(L\) is large. Taylor's integral remainder around \(\rho_L\) yields
\[
D_L(t)\ge\frac{(t-\rho_L)^2}{6\max\{t,\rho_L\}},
\quad
\sqrt L\frac{|t-\rho_L|}{\sqrt{D_L(t)}}=O(L^{-1/2}),
\]
with the continuous endpoint interpretation. In combination with (6), these bounds force **every** maximizing density \(t_L^*\) to satisfy \(t_L^*\to1/2\).

For each fixed \(L\), \(H'(t)\to-\infty\) as \(t\uparrow1/2\), so the derivative of the squared quotient in (4) is negative sufficiently near \(1/2\). Therefore an interior density has a strictly greater quotient than the endpoint \(1/2\). Since the maximum is not at \(0\) or \(\rho_L\) for large \(L\) by the above bounds, it is attained at \(\rho_L<t_L^*<1/2\), and first-order stationarity is valid.

**4. A second exponential scale from the shortest competing return.** Write \(s_L=s(t_L^*)\to\infty\) and \(q=e^{-3s_L}\). At large \(s\), the two shortest return lengths \(2\) and \(5\) dominate; the next length is \(10\). Directly from the defining series,
\[
\log Z(s)=-2s+q+O(q^2),\quad m(s)=2+3q+O(q^2),\quad
\frac12-t(s)=\frac34q+O(q^2).\tag{7}
\]
Here the omitted \(j\ge3\) return weights total \(O(e^{-8s})=O(q^{8/3})\), smaller than \(q^2\). Differentiating the quotient in (4), with \(D_L'(t)=L-H'(t)\), gives the **exact stationarity equation**
\[
\bigl(t_L^*+\rho_L\bigr)\bigl(L-\log Z(s_L)\bigr)=2(s_L-p_L).\tag{8}
\]
Since \(t_L^*\to1/2\), equations (7)--(8) first give \(s_L/L\to1/2\), then
\[
2s_L-L=O\bigl(L e^{-3s_L}+L\rho_L+p_L\bigr)=o(1).
\]
Therefore \(q=e^{-3L/2}(1+o(1))\). Equation (7) yields the claimed maximizing-density expansion.

**5. The sharp global correction.** Write \(\delta_L=1/2-t_L^*\). From (7) and the entropy identity (1), uniformly as \(\delta\downarrow0\),
\[
H(1/2-\delta)=\frac{2\delta}{3}\left(\log\frac3{4\delta}+1\right)
+O\!\left(\delta^2\log(1/\delta)\right).\tag{9}
\]
As \(\delta_L=(3/4)e^{-3L/2}(1+o(1))\), the logarithm in (9) equals \(3L/2+o(1)\). Expanding the numerator and denominator in (4) at the maximizing density gives
\[
C_L^2=\frac1{2L}+\frac{H(t_L^*)/L-\delta_L}{L}
+O\!\left(\frac{\delta_L^2+\rho_L+p_L/L}{L}\right).
\]
Equation (9) makes its second term \(2\delta_L/(3L^2)(1+o(1))\). The remainder is \(o(e^{-3L/2}/L^2)\) because \(\rho_L,p_L=O(e^{-2L})\) and \(\delta_L=\Theta(e^{-3L/2})\). Substitution proves
\[
C_L^2=\frac1{2L}+\frac{e^{-3L/2}}{2L^2}+o(e^{-3L/2}/L^2).
\]
This completes the global, local, and extremizing-density claims without assuming uniqueness of the finite-\(L\) global optimizer.

## Verification

Run `python verify.py` with `mpmath` installed. The checker evaluates the Gaussian theta transformation against an independent directly summed series; solves the renewal pressure equation at eight fields; checks the density, variance, pressure equality, and candidate ratios; and solves the **separate** global-stationarity equation at seven larger fields, testing the scaled density and sharp correction. It reports actual values and residuals. Its finite tests do **not** establish the infinite uniform estimates or the global maximizing property; those are proved by Steps 3--5.

## Relationship to prior work

Haydarov, Kadyrov, Makhmudov and Mamayusupov (arXiv:2606.17031, first public 2026-06-15) prove effective intrinsic ergodicity with an unspecified potential-dependent square-root coefficient for renewal-type potentials on \(S\)-gap shifts, together with the induced renewal description. Their theorem does not compute the globally optimal coefficient or its strong-marker-penalty asymptotics. *A theta-cubic law for sparse-marker entropy in the square-gap shift* determines the constrained-entropy curve and its near-zero expansion. The local susceptibility asymptotic follows from that curve by pressure maximization and differentiation. The claimed addition is the **sharp global stability law, including its nonzero correction and the nonlocal extremizing-density asymptotics**, contrasted with this local benchmark.

## Limitations

This is a scalar observable-specific result; it does not improve the all-Hölder-observables constant. Attainment of the global supremum is proved in the large-field regime, without uniqueness. The asymptotic remainder is qualitative, rather than an explicit finite-field error bar. The novelty comparison covers the identified relevant public sources and indexed findings, but cannot rule out unpublished or unindexed equivalent estimates. Numerical checks are finite diagnostics, not an infinite certificate.

## References

1. F. Haydarov, S. Kadyrov, M. Makhmudov and K. Mamayusupov, *Effective Intrinsic Ergodicity for renewal-type potentials on S-gap shifts*, arXiv:2606.17031 (first posted 2026-06-15), Sections 1--6, https://arxiv.org/abs/2606.17031.
2. *A theta-cubic law for sparse-marker entropy in the square-gap shift*, 2026-10-25, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-a-theta-cubic-law-for-sparse-marker-entropy-in-the-square-gap-sh--1db74ef026b2.
3. V. Climenhaga and D. J. Thompson, *Intrinsic ergodicity beyond specification: beta-shifts, S-gap shifts, and their factors*, arXiv:1011.2780 (2010), https://arxiv.org/abs/1011.2780.
4. Classical Kac--Abramov inducing identities and the Jacobi theta transformation, used as standard preliminaries.
