# A sharp arithmetic bias in least gaps of regular partitions

## Finding

Fix integers \(\ell\ge3\) and \(r\ge1\). For a uniformly selected partition \(\lambda\) of \(n\) into parts not divisible by \(\ell\), let \(M_{\ell,r}(\lambda)\) be the smallest positive integer not divisible by \(\ell\) occurring fewer than \(r\) times in \(\lambda\). Set
\[
\rho_\ell=1-\frac1\ell,\qquad
\mu_\ell=\frac{\pi^2\rho_\ell}{6},\qquad
C_{\ell,r}=\frac{\sqrt{\pi r}\,\mu_\ell^{1/4}}{2^{3/2}\ell^2\rho_\ell^{3/2}}>0.
\]
For each admissible residue \(s\in\{1,\ldots,\ell-1\}\), the following **sharp residue-bias law** holds as \(n\to\infty\):
\[
\boxed{\Pr\{M_{\ell,r}\equiv s\pmod\ell\}
=\frac1{\ell-1}+(\ell-2s)C_{\ell,r}\,n^{-1/4}
+o_{\ell,r}(n^{-1/4}).}
\]
Consequently, for every fixed \(1\le s<t\le\ell-1\),
\[
\Pr\{M_{\ell,r}\equiv s\pmod\ell\}
-\Pr\{M_{\ell,r}\equiv t\pmod\ell\}
=2(t-s)C_{\ell,r}\,n^{-1/4}+o_{\ell,r}(n^{-1/4})>0
\]
for all sufficiently large \(n\). Thus all permitted residues are equidistributed to first order, but their probabilities are eventually **strictly decreasing in residue order**, with an explicit nonzero separation at scale \(n^{-1/4}\). In the degenerate case \(\ell=2\) the only allowed residue is always \(1\).

The underlying **uniform local correction** is as follows. Let \(t=n^{-1/4}\), \(y=mt\), \(s\equiv m\pmod\ell\) with \(1\le s\le\ell-1\), and \(\gamma_{\ell,r}=r\rho_\ell\sqrt{\mu_\ell}/2\). For every fixed \(T>0\), uniformly over allowed integers \(1\le m\le Tn^{1/4}\),
\[
\boxed{\Pr\{M_{\ell,r}=m\}
=t\,r\sqrt{\mu_\ell}\,y e^{-\gamma_{\ell,r}y^2}
+t^2\frac{\mu_\ell r^2(\ell-2s)}{2\ell}y^2e^{-\gamma_{\ell,r}y^2}
+O_{\ell,r,T}(t^3).}
\]
The correction changes sign across the middle of the allowed residue range; it is not visible in the usual continuous Rayleigh limit.

## Assumptions and scope

All integers \(\ell\ge3\) and \(r\ge1\) are fixed while \(n\to\infty\). The random partition is uniform over \(\mathcal P_\ell(n)\), whose elements exclude multiples of \(\ell\); multiplicities of allowed parts are unrestricted. Define \(p_\ell(N)=|\mathcal P_\ell(N)|\) for \(N\ge0\) and \(p_\ell(N)=0\) for negative \(N\). The local remainder is uniform over a fixed compact interval on the \(n^{1/4}\) scale. The residue asymptotic is for fixed \(\ell,r\), not parameters growing with \(n\). No claim of exact finite-\(n\) ordering is made.

## Proof

**1. Exact displacement and local mass.** Define
\[
A_\ell(m)=\sum_{\substack{1\le j\le m\\\ell\nmid j}}j.
\]
Requiring \(M_{\ell,r}>m\) forces \(r\) copies of every permitted part at most \(m\); removing them bijects with \(\mathcal P_\ell(n-rA_\ell(m))\). Hence, for all \(m\ge0\),
\[
F_n(m):=\Pr(M_{\ell,r}>m)=\frac{p_\ell(n-rA_\ell(m))}{p_\ell(n)}.
\]
For \(\ell\nmid m\), the point mass is exactly \(F_n(m-1)-F_n(m)\). If \(m=\ell q+s\), \(0\le s<\ell\), direct subtraction of multiples of \(\ell\) gives
\[
A_\ell(m)=\frac{\rho_\ell m^2}{2}+\frac{s}{\ell}m+\frac{s}{2}-\frac{s^2}{2\ell}.
\tag{1}
\]
In particular \(A_\ell(m)-A_\ell(m-1)=m\) for permitted \(m\).

**2. A uniform quotient expansion.** The dominant term of the classical Rademacher/Hagis expansion for \(p_\ell\) (or the uncoloured specialization of Agarwal--Garg--Maji) and the asymptotic of the modified Bessel function \(I_1\) imply, for fixed \(\ell\), constants \(K_\ell>0\) and \(d_\ell\),
\[
p_\ell(N)=K_\ell N^{-3/4}e^{2\sqrt{\mu_\ell N}}
\left(1+d_\ell N^{-1/2}+O_\ell(N^{-1})\right).
\tag{2}
\]
The remaining cusps have strictly smaller exponential rate. The first correction in (2) is needed: a bare equivalent would not justify the required second-order quotient. By expanding logarithms of (2), uniformly for \(0\le h\le B\sqrt{n\log n}\) with fixed \(B\),
\[
\log\frac{p_\ell(n-h)}{p_\ell(n)}
=-\sqrt{\mu_\ell}\frac h{\sqrt n}
+\frac{3h}{4n}
-\frac{\sqrt{\mu_\ell}\,h^2}{4n^{3/2}}
+O_{\ell,B}\left(\frac{(1+\log n)^2}{n}\right).
\tag{3}
\]
The difference of the \(d_\ell N^{-1/2}\) terms is \(O_\ell(hn^{-3/2})\), while the two controlled remainders in (2) contribute \(O_\ell(n^{-1})\). The cubic Taylor remainder of the square root is \(O_\ell(h^3n^{-5/2})\), within the displayed bound. All these bounds hold as long as \(n-h>0\), which holds eventually in the specified window.

**3. Arithmetic local expansion.** Put \(t=n^{-1/4}\), \(y=mt\), and write \(s=m\bmod\ell\). Using (1), write \(h=rA_\ell(m)=a\sqrt n+b n^{1/4}+c\), where
\[
a=\frac{r\rho_\ell y^2}{2},\quad b=\frac{rsy}{\ell},\quad
c=\frac r2\left(s-\frac{s^2}{\ell}\right).
\]
Equation (3), exponentiated, yields, uniformly for \(m\le Tn^{1/4}\),
\[
F_n(m)=e^{-\sqrt{\mu_\ell}a}
\left[1-\sqrt{\mu_\ell}b\,t+
\left(-\sqrt{\mu_\ell}c+\frac{3a}{4}
-\frac{\sqrt{\mu_\ell}a^2}{4}+\frac{\mu_\ell b^2}{2}\right)t^2+O_{\ell,r,T}(t^3)\right].
\tag{4}
\]
For permitted \(m\), the preceding argument \(m-1\) has scaled coordinate \(y-t\) and residue \(s-1\). Taylor-expand (4) at these two coordinates and subtract. The order-\(t\) terms combine to \(r\sqrt{\mu_\ell}y e^{-\gamma_{\ell,r}y^2}\). At order \(t^2\), the constant pieces cancel exactly, and the remaining coefficient simplifies to
\[
\frac{\mu_\ell r^2}{2\ell}(\ell-2s)y^2e^{-\gamma_{\ell,r}y^2}.
\]
This proves the local formula, including its uniform remainder. The cancellation and the linear dependence on \(s\) are the key nonleading arithmetic features.

**4. Summation over a residue class.** To justify summing, take a cutoff \(m_{\max}=\lfloor B n^{1/4}\sqrt{\log n}\rfloor\), with a sufficiently large constant \(B=B(\ell,r)\). Equations (1)--(3) give \(F_n(m_{\max})=O_{\ell,r}(n^{-2})\). Thus the omitted tail contributes \(o(n^{-1/4})\) to every residue probability. The Taylor expansions in step 3 extend through this cutoff with a remainder bounded by \(O_{\ell,r}(t^3(1+\log n)^K)\) for some fixed \(K\). Summing at most \(O(t^{-1}\sqrt{\log n})\) permitted terms contributes \(O_{\ell,r}(t^2(1+\log n)^{K+1})=o(t)\).

For a fixed residue \(s\), put \(g(y)=r\sqrt{\mu_\ell}y e^{-\gamma y^2}\) and \(v_s(y)=\mu_\ell r^2(\ell-2s)y^2 e^{-\gamma y^2}/(2\ell)\), where \(\gamma=\gamma_{\ell,r}\). Standard shifted Euler--Maclaurin summation, noting \(g(0)=0\), gives
\[
t\sum_{\substack{m\ge1\\m\equiv s\ (\bmod\ell)}}g(mt)
=\frac1\ell\int_0^\infty g(y)\,dy+O_{\ell,r}(t^2),
\]
\[
t^2\sum_{\substack{m\ge1\\m\equiv s\ (\bmod\ell)}}v_s(mt)
=\frac t\ell\int_0^\infty v_s(y)\,dy+O_{\ell,r}(t^2).
\]
Since \(\int_0^\infty y e^{-\gamma y^2}\,dy=1/(2\gamma)\) and \(\int_0^\infty y^2e^{-\gamma y^2}\,dy=\sqrt\pi/(4\gamma^{3/2})\), the first integral divided by \(\ell\) equals \(1/(\ell-1)\), and the second divided by \(\ell\) equals \((\ell-2s)C_{\ell,r}\). This establishes the claimed residue law and its strict eventual ordering. Finally \(\sum_{s=1}^{\ell-1}(\ell-2s)=0\), consistent with total probability one.

## Verification

The accompanying `verify.py` calculates \(p_\ell(n)\) from Euler's pentagonal recurrence, compares exact first-gap survivor and mass identities with direct partition enumeration for all \(0\le n\le22\), \(2\le\ell\le7\), and \(1\le r\le3\), and checks the first two local terms and the class probabilities for several cases at \(n=40000\). The program gives `VERIFY_OK`. This finite work verifies the combinatorial formula and illustrates convergence; the infinite error control uses the analytic argument above and the published coefficient asymptotic.

## Relationship to prior work

Tejash Priya, Bhowmick, and Meher (arXiv:2611.07871v1, November 5, 2026) introduced the least multiplicity-gap statistic in \(\ell\)-regular partitions and gave its two-variable generating function, together with first-order estimates of its aggregate sum for selected \(\ell\). The exact point probabilities and the mandatory-part shift are equivalent to their Proposition 2.2; neither is claimed new here.

The published *Joint least-multiplicity-gap laws for regular partitions* proves the exact joint survivor count and leading running-minimum Rayleigh law. That fully covers the marginal leading asymptotic and its first-order equidistribution implication, but does not give the nonzero \(n^{-1/4}\) residue-dependent correction, the local second-order formula, or the eventual strict class ordering. Agarwal, Garg, and Maji (arXiv:2511.05907v1, November 8, 2025) provide the exact Rademacher expansion used for the partition coefficients; applying it by itself does not produce the stated least-gap class bias. Other work on congruence-class biases counts all parts or a different ensemble, not the first deficient allowed part. The argument here combines the known ingredients with uniform two-scale expansion and summation, so an implicit antecedent remains possible.

## Limitations

Parameters \(\ell,r\) remain fixed; there are no bounds uniform in growing parameters and no assertion of a precise finite onset of strict ordering. The result uses the classical exact eta-quotient partition asymptotic, not a new circle-method theorem. It has no independent mathematical audit. An implicit derivation in earlier works on smallest gaps, especially Wagner's or Hagis's broader analyses, remains a priority risk. A previously known exact formula in principle permits this expansion, but the explicit signed residue bias is the statement assessed here.

## References

- T. Priya, S. Bhowmick, and N. K. Meher, *The minimal excludant and the least r-gaps of ell-regular partitions*, arXiv:2611.07871v1, first posted 2026-11-05, https://arxiv.org/html/2611.07871v1.
- A. Agarwal, M. Garg, and B. Maji, *Rademacher-type exact formula and higher order Turan inequalities for r-colored ell-regular partitions*, arXiv:2511.05907v1, first posted 2025-11-08, https://arxiv.org/html/2511.05907v1.
- *Joint least-multiplicity-gap laws for regular partitions*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-joint-least-multiplicity-gap-laws-for-regular-partitions--a7d5664f9d36.
- S. Wagner, *Limit distributions of smallest gap and largest repeated part in integer partitions*, Ramanujan J. 25 (2011), 229--246, https://doi.org/10.1007/s11139-010-9264-z.
- K. Bringmann and S. H. Man, *Asymptotics of parity biases for partitions into distinct parts via Nahm sums*, Proc. Lond. Math. Soc. 129 (2024), https://doi.org/10.1112/plms.70010 (related residue-bias context, not the same statistic).
