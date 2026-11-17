# Sharp logarithmic winding records for sliding Bykov return dynamics

## Finding

Consider the local first-return dynamics near a sliding Bykov cycle under the hypotheses of Theorem B of Cunha and da Silva [1]. For any sufficiently small fixed return section \(U\), let \(\Lambda_U\) be the invariant Cantor-coded set and let \(\mu_U^*\) be the unique return-invariant probability equivalent to its conformal measure. Write \(s_U=\dim_H\Lambda_U\in(0,1)\). Each return has a positive integer branch index \(K_j\), which labels successive spiralling sheets in the natural inverse-branch construction. Put

\[
\kappa=\frac{S b_s+(a_s/a_u)b_u}{\lambda_s}\ne0,
\qquad \beta_U=\frac{2\pi s_U}{|\kappa|}.
\]

There are constants \(0<A_U\le B_U<\infty\) and an integer \(k_U\) such that, for all integers \(k\ge k_U\) and \(n\ge1\), with \(M_n=\max\{K_0,\ldots,K_{n-1}\}\),

\[
(1-B_Ue^{-\beta_U k})^n
\le \mu_U^*\{M_n<k\}
\le (1-A_Ue^{-\beta_U k})^n,
\]

where \(k_U\) is chosen so that \(B_Ue^{-\beta_U k}<1\). Consequently the first waiting time \(T_k=\min\{j\ge1:K_{j-1}\ge k\}\) satisfies

\[
\frac{e^{\beta_U k}}{B_U}
\le\mathbb E_{\mu_U^*}T_k
\le\frac{e^{\beta_U k}}{A_U},
\qquad
\lim_{n\to\infty}\frac{M_n}{\log n}
=\frac{|\kappa|}{2\pi s_U}
\quad \mu_U^*\text{-almost surely}.
\]

The one-return tail and its exponential-moment threshold are sharp:

\[
\lim_{k\to\infty}\frac1k\log\mu_U^*\{K_0\ge k\}=-\beta_U,
\qquad
\mathbb E_{\mu_U^*}e^{tK_0}<\infty
\iff t<\beta_U
\quad(t\in\mathbb R).
\]

In particular, the geometric spiral rate \(2\pi/|\kappa|\) and the Hausdorff dimension of the return invariant set jointly determine the almost-sure logarithmic record coefficient.

## Assumptions and scope

The Filippov field is a \(C^3\) field admitting the sliding Bykov configuration (SB1)–(SB3) of [1], with (P1): local \(C^2\) conjugacies with \(C^2\) inverses at the ordinary saddle-focus and sliding pseudo-saddle-focus; (P2): \(c_s-S c_u\ne0\), where \(c_s=-a_s/b_s\), \(c_u=a_u/b_u\), and \(S=\operatorname{sign}\det L\) for the global-map derivative \(L\); and (P3):

\[
|Q-S c_s c_u|<\sqrt{(1+c_s^2)(1+c_u^2)},
\qquad Q=\frac{\sigma_1^2+\sigma_2^2}{2\sigma_1\sigma_2}\ge1.
\]

Here \(\lambda_s>0\) is the real unstable eigenvalue of the ordinary saddle-focus, \(-a_s\pm ib_s\) are its stable eigenvalues, and \(a_u\pm ib_u\) are the eigenvalues of the sliding pseudo-saddle-focus; \(a_s,a_u>0\), \(b_sb_u\ne0\). All terms follow the notation of [1]. Identify the compact return arc \(I=\overline U\) with an interval; equivalently one may take the sufficiently small arc \(I=\gamma_r\) itself as the local section. The return-section size \(U\) is sufficiently small for the countable conformal inverse-branch system of [1, §5.4] to hold. It remains fixed as \(n\) and \(k\) vary. Its inverse branches \(\psi_k\) are indexed as in [1, equations (17)–(19)], with an arbitrary finite change in initial indexing affecting neither exponential rates nor the logarithmic record coefficient. The probability \(\mu_U^*\) is intrinsic to the fractal return set, not Lebesgue measure on a surrounding section.

## Proof

**Step 1: the exponential geometric input.** The inverse branches \(\psi_k\) of [1, equations (19), (23)] are one-to-one onto pairwise disjoint return intervals and, for all sufficiently large \(k\), satisfy uniform inequalities on the return section \(I\):

\[
0<a e^{-ck}\le |\psi_k'(x)|\le b e^{-ck}
\quad(x\in I),\qquad
c=2\pi/|\kappa|,
\]

where \(a,b>0\) depend on the fixed section, not on \(k\) or \(x\). Any finitely many earlier branches are harmless. The proof of Lemma 5.4 of [1], specifically its verification of CIFS condition (C6), also gives a uniform contraction factor \(0<r<1\) and a uniform Hölder bound on \(\log|\psi_k'|\). The latter follows directly by dividing its relative derivative-difference estimate by the positive infimum of \(|\psi_k'|\) and applying the Lipschitz bound for \(\log\). In particular, for some \(L>0\),

\[
|\log|\psi_k'(x)|-\log|\psi_k'(y)||\le L|x-y|^{\alpha}
\quad\text{for all }k,x,y
\]

with \(\alpha>0\). The finite set of early branches can be absorbed by enlarging \(L\). For a word \(w=(k_1,\ldots,k_m)\), the chain rule and uniform contraction of its suffixes now give

\[
\left|\log\frac{|\psi_w'(x)|}{|\psi_w'(y)|}\right|
\le L\,\operatorname{diam}(I)^\alpha
\sum_{j=0}^{m-1}r^{\alpha j}
\le \frac{L\operatorname{diam}(I)^\alpha}{1-r^\alpha}.
\]

Thus there is a word-length-independent bounded-distortion constant \(D\ge1\) for \(|\psi_w'|\).

**Step 2: conformal and stationary cylinder comparability.** Let \(\nu\) be the probability on the full countable coding space induced by the \(s_U\)-conformal measure, so [1, Proposition C.4] gives

\[
\nu([w])=\int_I|\psi_w'(x)|^{s_U}\,dm_U(x).
\]

Write \(p(w)=\nu([w])\). The chain rule, integration and distortion bound yield, for all finite words \(u,v\),

\[
D^{-s_U}p(u)p(v)\le p(uv)\le D^{s_U}p(u)p(v).
\tag{1}
\]

Since \(\sum_{|u|=j}p(u)=1\), applying (1) and summing prefixes \(u\) shows that the \(j\)-fold shift-pushforward \(\sigma_*^j\nu\) is between \(D^{-s_U}\nu\) and \(D^{s_U}\nu\) on all cylinders and hence on all Borel sets. The Cesàro averages of these pushforwards are uniformly dominated by \(D^{s_U}\nu\), so they possess invariant subsequential limits. Such limits remain between the same bounds and are equivalent to \(\nu\). Uniqueness of the equivalent invariant probability [1, Proposition C.4] identifies them with \(\nu^*\), the symbolic lift of \(\mu_U^*\). Therefore

\[
D^{-s_U}p(w)\le\nu^*([w])\le D^{s_U}p(w)
\quad\text{for every finite word }w.
\tag{2}
\]

In particular, the one-symbol conformal formula and Step 1 imply positive constants \(a_0,b_0\) with

\[
a_0e^{-\beta_U k}\le\nu^*\{K_0=k\}\le b_0e^{-\beta_U k}
\quad\text{for large }k.
\tag{3}
\]

Summing the geometric series proves two-sided exponential bounds for \(\nu^*\{K_0\ge k\}\), their exact logarithmic exponent \(-\beta_U\), and the moment threshold, including divergence at equality \(t=\beta_U\).

**Step 3: uniform conditional rare-event bounds.** For any nonempty prefix word \(u\) and large \(k\), combine (1), (2), and the sum of (3) over all suffix letters \(j\ge k\). This gives constants \(A_U,B_U>0\), independent of the length and content of \(u\), such that

\[
A_Ue^{-\beta_U k}
\le\nu^*\{K_{|u|}\ge k\mid [u]\}
\le B_Ue^{-\beta_U k}.
\tag{4}
\]

The same inequalities hold for the empty prefix by (3). Conditional expectation with respect to successive finite prefix sigma-algebras then bounds the probability of avoiding all branches \(\ge k\) for \(n\) returns by the two powers stated in the theorem. Summing these survival probabilities in \(n\) gives the displayed bounds on \(\mathbb E T_k\).

**Step 4: the sharp almost-sure record coefficient.** For each \(\epsilon\in(0,1)\), put \(n_j=2^j\), and define integer upper and lower thresholds by rounding

\[
k_j^+=\frac{(1+\epsilon)\log n_j}{\beta_U},
\qquad
k_j^-=\frac{(1-\epsilon)\log n_j}{\beta_U}.
\]

Stationarity and the one-symbol tail bound give \(\nu^*\{M_{n_j}\ge k_j^+\}=O(2^{-\epsilon j})\). The avoidance estimate from Step 3 gives \(\nu^*\{M_{n_j}<k_j^-\}\le\exp(-A\,2^{\epsilon j})\) for some \(A>0\), after adjusting for rounding. Both bounds are summable. Borel–Cantelli implies that eventually \(k_j^-\le M_{n_j}<k_j^+\), almost surely. Monotonicity of \(M_n\) and \(\log n_{j+1}/\log n_j\to1\) extend this limit to all \(n\); letting \(\epsilon\downarrow0\) through rational values yields \(M_n/\log n\to1/\beta_U\). The return-map conjugacy transports all statements to \(\Lambda_U\). This completes the proof.

## Verification

No numerical or finite-search certificate is needed. The checkable dependencies are [1, equations (17)–(19) and (23)] for the branch exponent, [1, Lemma 5.4 and condition (C6)] for uniform contraction and distortion, and [1, Theorem B(c), Proposition C.4] for the conformal and equivalent invariant probabilities. Each new probabilistic step is proved above, including the conditional estimate rather than assuming independence. The proof uses the fixed section \(U\); the constants \(A_U,B_U\) are not asserted uniform as \(U\) shrinks. A one-symbol exponential tail alone would not establish the record law; the decisive extra input is the uniform conditional bound (4).

## Relationship to prior work

Cunha and da Silva [1] construct the sliding Bykov countable return shift, prove exponential inverse-branch derivative estimates and give conformal and invariant ergodic measures. Their conclusions concern symbolic conjugacy, Hausdorff dimension, Cantor closure and measure existence, not quantitative tail or maximal-spiral laws. The earlier sliding Shilnikov study [2] proves related fractal and IFS structure but does not analyze this sliding Bykov return measure. The foundational CIFS theory of Mauldin and Urbański [3] supplies the conformal-measure apparatus and bounded-distortion setting. General digit-extreme or dynamical Borel–Cantelli principles could also produce analogous record laws once appropriate hypotheses are verified; the present contribution is the system-specific sharp coefficient and uniform finite-horizon bounds from this Filippov geometry. These generic principles and possible additional sources remain a historical-priority risk.

## Limitations

The law is almost sure under the invariant probability \(\mu_U^*\) on a zero-Lebesgue-measure return invariant set. It is not asserted for Lebesgue-typical ambient initial states, physical elapsed-time records, all Filippov systems, or a neighborhood-size limit. The cylinder and rare-event constants depend on the chosen return section and need not be explicit. These bounds determine the logarithmic record slope but not a unique centered extreme-value limiting distribution. Historical priority remains provisional, and independent mathematical validation has not been performed.

## References

[1] M. G. C. Cunha and P. R. da Silva, *On Bykov Cycles in Filippov Systems*, arXiv:2611.01971v1, first posted 2026-11-01, https://arxiv.org/html/2611.01971v1; §§2.4, 5.3–5.5, Appendix C.

[2] M. G. C. Cunha, D. D. Novaes and G. Ponce, *On the Hausdorff dimension and Cantor set structure of sliding Shilnikov invariant sets*, arXiv:2312.10720, first posted 2023-12-17, https://arxiv.org/abs/2312.10720.

[3] R. D. Mauldin and M. Urbański, *Dimensions and Measures in Infinite Iterated Function Systems*, Proc. London Math. Soc. 73 (1996), 105–154, DOI 10.1112/plms/s3-73.1.105.
