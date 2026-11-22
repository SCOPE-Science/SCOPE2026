# A universal square-root pressure fingerprint for Sturmian-decorated renewal shifts

## Finding
Let \(0<\alpha<1\) be irrational. Let \(Y_\alpha\subset\{1,2\}^{\mathbb Z}\) be the Sturmian shift obtained by coding rotation through \(\alpha\), with the frequency of symbol \(2\) equal to \(\alpha\). Form the three-symbol shift \(X_\alpha\) as the closure of all bi-infinite concatenations of codewords \(0u\), where \(u\) is **any** finite word (including the empty word) in the language of \(Y_\alpha\). For activity \(x>0\) and real color field \(t\), let \(P_\alpha(x,t)\) be the topological pressure of the one-site potential
\[
\varphi_{x,t}(z)=(\log x)\mathbf1_{\{z_0=0\}}+t\mathbf1_{\{z_0=2\}}.
\]
For every \(x>0\) and \(t\in\mathbb R\), this potential has a **unique** equilibrium measure \(\mu_{x,t}\), and the pressure is the unique real number \(P>\alpha t\) satisfying
\[
\boxed{1=x\sum_{n\ge0}e^{-(n+1)P}\sum_{u\in\mathcal L_n(Y_\alpha)}e^{t|u|_2}.}\tag{1}
\]
For each fixed real \(t\), as \(x\downarrow0\),
\[
\boxed{P_\alpha(x,t)=\alpha t+C_\alpha(t)\sqrt{x}+o(\sqrt{x}),\quad C_\alpha(t)=e^{-\alpha t/2}\frac{2\sinh(t/2)}{t}.}\tag{2}
\]
The quotient in the formula for \(C_\alpha\) is defined continuously as \(1\) at \(t=0\). Writing \(\rho_{x,t}=\mu_{x,t}([0])\), the exact first-order composition laws are
\[
\boxed{\rho_{x,t}\sim\tfrac12 C_\alpha(t)\sqrt{x},\qquad
\mu_{x,t}([2])=\alpha+\rho_{x,t}\bigl(L(t)-\alpha\bigr)+o(\rho_{x,t}),}\tag{3}
\]
where \(L(t)=\coth(t/2)-2/t\) for \(t\ne0\) and \(L(0)=0\). At zero color field the pressure and marker occupation are, for **all** \(x>0\),
\[
\boxed{P_\alpha(x,0)=2\operatorname{arsinh}(\sqrt{x}/2),\qquad \rho_{x,0}=\frac{\sqrt{x}}{\sqrt{4+x}}.}\tag{4}
\]
Thus all irrational slopes have the same entire marker-only pressure curve, while their two-parameter low-activity fingerprints are different. In fact the slope can be recovered exactly from the first nonzero pressure correction by
\[
\boxed{\alpha=-2\left.\frac{d}{dt}\log C_\alpha(t)\right|_{t=0}.}\tag{5}
\]
This is a distinction between complete unweighted pressure coincidence and a slope-sensitive singular *colored* pressure coefficient, not a claim that the unweighted entropy or renewal equation is new.

## Assumptions and scope
All shifts are bilateral, on a finite alphabet, and use the left shift. \(\mathcal L_n(Y_\alpha)\) denotes the set of distinct length-\(n\) factors, with \(\mathcal L_0=\{\varepsilon\}\), and \(|u|_2\) is the number of symbols \(2\) in \(u\). The word \(0u\) is an entire marker-to-marker return block of length \(n+1\). The empty word is allowed, so adjacent markers occur. The closure adds the marker-free subsystem \(Y_\alpha\), which is minimal and uniquely ergodic, has zero entropy, and has symbol-\(2\) frequency \(\alpha\). The color field \(t\) is fixed as \(x\downarrow0\); no uniformity in unbounded \(t\) is asserted. All asymptotics use natural logarithms.

## Proof
**1. Weighted renewal pressure and uniqueness.** Every invariant measure assigning positive probability to the synchronizing marker has an induced stationary process on the countable alphabet \(\mathcal C=\{0u:u\in\mathcal L(Y_\alpha)\}\). Write \(\ell(0u)=|u|+1\) and \(k(0u)=|u|_2\). Its first-return mean \(\bar\ell\) is finite by Kac's formula. The entropy and energy per spatial symbol are, by the return-map entropy formula,
\[
\frac{h(\eta)+(\log x)+t\mathbb E_\eta k}{\mathbb E_\eta\ell}.
\]
For a candidate \(P>\alpha t\), define positive numbers \(\pi_P(0u)=x e^{t k(0u)-P\ell(0u)}\). Sturmian balance gives \(\bigl|k(0u)-\alpha|u|\bigr|<1\); since \(|\mathcal L_n(Y_\alpha)|=n+1\), the sum of these numbers is finite for every \(P>\alpha t\), decreases strictly from infinity at the left endpoint to zero at infinity, and hence equals one for exactly one \(P\). This is (1); its \(\pi_P\) has exponentially decaying block lengths and finite mean.

For any induced stationary process, its entropy rate is at most the entropy of its one-block marginal \(p\). The Kullback--Leibler inequality then gives
\[
 h(\eta)+\log x+t\mathbb E_\eta k-P\mathbb E_\eta\ell
 \le -D(p\Vert\pi_P)\le0.
\]
Equality holds precisely for the independent block process with distribution \(\pi_P\), giving a unique stationary renewal lift. An invariant measure assigning zero mass to the marker is supported on \(Y_\alpha\), so its free energy is exactly \(\alpha t<P\). Ergodic decomposition therefore establishes both the pressure formula and global uniqueness of \(\mu_{x,t}\).

**2. The distribution of distinct Sturmian factors.** Use a mechanical coding, where the binary indicator for symbol \(2\) at time \(j\) is \(\lfloor(j+1)\alpha+\theta\rfloor-\lfloor j\alpha+\theta\rfloor\). For a word of length \(n\), its number of symbols \(2\) is either \(\lfloor n\alpha\rfloor\) or \(\lceil n\alpha\rceil\). The \(n+1\) distinct words correspond to the cells of the rotation partition with endpoints \(\{-j\alpha\bmod1:0\le j\le n\}\). Let \(q_n=\{n\alpha\}\), and let \(r_n\) be the number of distinct length-\(n\) words with \(\lceil n\alpha\rceil\) symbols \(2\). Such a word occurs for intercepts in the arc \([1-q_n,1)\), whose left endpoint is one of the partition endpoints. Uniform discrepancy for the irrational rotation (valid for moving arcs) implies
\[
 \frac{r_n}{n+1}=q_n+o(1)\quad(n\to\infty).\tag{6}
\]
For fixed \(t\), define
\[
 Q_n(t)=\sum_{u\in\mathcal L_n(Y_\alpha)}e^{t(|u|_2-\alpha n)},\quad
 G_t(q)=(1-q)e^{-tq}+q e^{t(1-q)}.
\]
Equation (6) yields \(Q_n(t)=(n+1)G_t(q_n)+o(n)\), and the same relation after differentiating once in \(t\), because the centered word counts are uniformly bounded by one. Irrational equidistribution of \(q_n\), followed by Abel summation, now proves for \(\delta\downarrow0\)
\[
 H_t(\delta):=\sum_{n\ge0}Q_n(t)e^{-n\delta}\sim\frac{I(t)}{\delta^2},\qquad
 -\partial_\delta H_t(\delta)\sim\frac{2I(t)}{\delta^3},\qquad
 \partial_t H_t(\delta)\sim\frac{I'(t)}{\delta^2},\tag{7}
\]
where
\[
 I(t)=\int_0^1 G_t(q)\,dq
 =\frac{e^t+e^{-t}-2}{t^2}
 =\left(\frac{2\sinh(t/2)}t\right)^2,
\]
with continuous value \(I(0)=1\). The notation \(\partial_tH_t\) holds \(\delta\) fixed, so it does not include any derivative of pressure.

**3. Critical pressure law.** Put \(\delta=P_\alpha(x,t)-\alpha t>0\). Equation (1) becomes
\[
 1=x e^{-\alpha t-\delta} H_t(\delta).
\]
For fixed \(t\), the unique root has \(\delta\downarrow0\) as \(x\downarrow0\); otherwise the right side tends to zero. The first estimate in (7) gives
\[
 \delta^2\sim x e^{-\alpha t}I(t),
\]
which is (2), including the positive branch of the square root.

**4. Occupation laws and slope detection.** Under \(\pi_P\), the mean return length is
\[
 \bar\ell=1+\frac{\sum_{n\ge0}nQ_n(t)e^{-n\delta}}{H_t(\delta)}
 =\frac2\delta(1+o(1)).
\]
The marker density is \(\rho_{x,t}=1/\bar\ell\). The average centered colored count per return block is \(\partial_t H_t(\delta)/H_t(\delta)\to I'(t)/I(t)=L(t)\). Since the colored count of a return block is \(\alpha(\ell-1)\) plus its centered count, its spatial frequency is
\[
 \mu_{x,t}([2])=\alpha(1-\rho_{x,t})+\rho_{x,t}\frac{\partial_t H_t(\delta)}{H_t(\delta)},
\]
which gives (3). At \(t=0\), the factor count \(n+1\) gives the exact renewal series \(\sum_{n\ge0}(n+1)e^{-(n+1)P}=e^{-P}/(1-e^{-P})^2\). Solving \(x e^{-P}/(1-e^{-P})^2=1\) proves the pressure identity (4); differentiating with respect to \(\log x\) or using the return mean proves its marker identity. Finally \(2\sinh(t/2)/t\) is even and equals one at zero, so the derivative in (5) is \(-\alpha/2\). This completes the proof.

## Verification
The standalone standard-library program `verify.py` checks (i) the rotation-partition heavy-factor count against direct languages for lengths one through twelve, (ii) finite renewal sums and the predicted critical coefficients for three color fields at two activities, (iii) the marker and colored-frequency first corrections, and (iv) exact all-activity uncolored identities at the tested activities. It passed six parameter pairs and twelve direct factor lengths. Finite truncation and floating arithmetic are only diagnostics; the universal limits and uniqueness are proved above. Run with `python3 verify.py` from this directory.

## Relationship to prior work
Ramirez and Somers (2025) introduced the \((S,w)\)-gap construction and proved an unweighted entropy root in terms of word complexity. Here that definition is used with **all** lengths and Sturmian decoration; their entropy theorem gives (4) at \(x=1\), but not the two-field pressure amplitude or the colored composition asymptotics. Haydarov, Kadyrov, Makhmudov and Mamayusupov (2026) establish renewal-type equilibrium uniqueness for classical **binary** \(S\)-gap shifts; the induced relative-entropy argument here is an analogous standard mechanism, not claimed as new in itself. Their estimates do not evaluate the color-weighted distribution of **distinct Sturmian words** or the coefficient \(C_\alpha(t)\). The published *Periodic zeta rationality versus Sturmian nonsoficity in decorated gap shifts* proves that the entire unweighted periodic-point zeta and entropy are independent of the Sturmian slope; this is used as motivation and acknowledged. It does not encode the symbol-\(2\) weights. In particular, that same unweighted data cannot imply (2) for \(t\ne0\), since (5) recovers arbitrarily different slopes. The classification of heavy versus light Sturmian factors by rotation partition intervals already appears in Fici, Mignosi and Shallit (2017), Proposition 14; it is a cited combinatorial input, not an originality claim. The new claim is its weighted renewal-pressure consequence, the evaluated square-root coefficient and slope recovery. Classical mechanical-word balance and irrational equidistribution are also prior inputs.

## Limitations
The asymptotic coefficient and composition correction are asserted pointwise in each fixed real color field, not uniformly over unbounded fields or varying slopes. The underlying decoration must be Sturmian, the marker-to-marker set contains every possible length including zero, and the potential is one-site. No conjugacy classification or quantitative convergence rate for arbitrary irrational slopes is claimed. Older multivariate renewal thermodynamic results could contain an equivalent result; although relevant primary papers and the closest indexed result were compared, historical priority is not independently certified.

## References
1. C. Ramirez and A. Somers, *\((S,w)\)-Gap Shifts and Their Entropy*, arXiv:2501.08438v1 (first posted 2025-01-14), Theorem 1.1 and Sections 4–5, published in *The PUMP Journal of Undergraduate Research* 8 (2025), pp. 85–97, https://arxiv.org/abs/2501.08438 and https://journals.calstate.edu/pump/article/download/4115/4628.
2. F. Haydarov, S. Kadyrov, M. Makhmudov and K. Mamayusupov, *Effective Intrinsic Ergodicity for Renewal-Type Potentials on S-Gap Shifts*, arXiv:2606.17031v1 (first posted 2026-06-15), Sections 2–4, https://arxiv.org/abs/2606.17031.
3. *Periodic zeta rationality versus Sturmian nonsoficity in decorated gap shifts*, public research record dated 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-periodic-zeta-rationality-versus-sturmian-nonsoficity-in-decorat--0881e8e9b148.
4. Classical irrational-rotation equidistribution and mechanical characterizations of Sturmian sequences, e.g. M. Lothaire (ed.), *Algebraic Combinatorics on Words*, Cambridge University Press, 2002, Chapter 2.
5. G. Fici, F. Mignosi and J. Shallit, *Abelian-Square-Rich Words*, arXiv:1701.00948 (2017), Section 5, Proposition 14 (heavy/light Sturmian factor intervals), https://arxiv.org/abs/1701.00948.
