# Gaussian fluctuations of the deepest drawdown's duration rank in a biased simple random walk

## Finding

Fix \(p\in(1/2,1)\), write \(q=1-p\), and consider independent nonzero drawdown episodes of a random walk with \(+1\) increments of probability \(p\) and \(-1\) increments of probability \(q\). Let \((H_i,L_i)\) be the maximum loss and total duration in the \(i\)-th episode. Among the first \(n\) episodes let \(I_n\) be the first index with maximum depth, and let \(R_n\) be its descending duration rank, breaking ties by smaller episode index.

Set
\[
\delta=p-q,\qquad \alpha=\log(p/q),\qquad
\beta=-\log(2\sqrt{pq}),\qquad
\rho=\frac{2\beta}{\delta\alpha}\in(0,1),\qquad
\sigma^2=\frac{8pq}{\delta^3\alpha}.
\]
Then the *joint second-order duration/rank law* is
\[
\boxed{\left(\frac{L_{I_n}-\frac{2}{\delta\alpha}\log n}{\sqrt{\log n}},
\frac{\log R_n-(1-\rho)\log n}{\sqrt{\log n}}\right)
\ \Longrightarrow\ (Z,-\beta Z),\quad Z\sim N(0,\sigma^2).}
\]
In particular the logarithmic rank has nondegenerate Gaussian fluctuations of variance \(8pq\beta^2/(\delta^3\alpha)\). More precisely, the rank satisfies the sharp random-threshold relation
\[
\boxed{\log R_n=\log n-\beta L_{I_n}-\tfrac32\log L_{I_n}+O_{\mathbb P}(1).}
\]
The \(O_{\mathbb P}(1)\) assertion is for each fixed \(p\); it is not claimed to hold uniformly as \(p\) approaches either endpoint.

## Assumptions and scope

For clarity, define one episode entirely from the loss process \(Y=-X\). Begin at loss level \(1\) after a forced first \(+1\) loss step, then take independent steps \(+1\) with probability \(q\) and \(-1\) with probability \(p\) until the first return to level \(0\). Its total duration \(L\) includes that forced first step, and \(H\) is its highest visited positive level. Since \(p>q\), the return occurs almost surely. The pairs \((H_i,L_i)\), \(i\ge1\), are independent copies of this pair. These are the positive-length recovery excursions obtained by discarding zero-length record advances in the original positive-drift walk.

For \(n\ge1\), define \(H_n^*=\max_{i\le n}H_i\) and \(I_n=\min\{i:H_i=H_n^*\}\). Define \(R_n=1+\#\{j\ne I_n:L_j>L_{I_n}\}+\#\{j<I_n:L_j=L_{I_n}\}\). The definition makes all rankings unambiguous, including height and duration ties. All statements concern \(n\to\infty\) with \(p\) fixed, the number of complete nonzero episodes rather than a deterministic calendar-time horizon.

## Proof

**1. Exact maximum-height generating function.** Let \(T_0\) be the first hit of zero from loss level one and \(T_{h+1}\) the first hit of level \(h+1\). For \(0<z\le1\) set
\[
F_h(z)=\mathbb E_1[z^{T_0};\ T_0<T_{h+1}],\quad F_0(z)=0.
\]
The first-step recurrence for the hitting transform \(f_j\), \(1\le j\le h\), is \(f_j=z(pf_{j-1}+qf_{j+1})\) with \(f_0=1\) and \(f_{h+1}=0\). Define
\[
r_\pm(z)=\frac{1\pm\sqrt{1-4pqz^2}}{2qz},\qquad u(z)=\frac{r_-(z)}{r_+(z)}.
\]
Solving the two-boundary recurrence yields
\[
F_h(z)=r_-(z)\frac{1-u(z)^h}{1-u(z)^{h+1}}.
\]
The excursion has maximum at most \(h\) exactly on \(T_0<T_{h+1}\). Because the total duration includes the initial forced step, its joint height/duration transform is therefore
\[
D_h(z):=\mathbb E[z^L;H=h]
=z\,[F_h(z)-F_{h-1}(z)]
=z r_-(z)\frac{u(z)^{h-1}(1-u(z))^2}{(1-u(z)^h)(1-u(z)^{h+1})},\quad h\ge1.
\]
At \(z=1\), \(r_-(1)=1\) and \(u(1)=q/p=:r\); hence
\[
\mathbb P(H=h)=\frac{r^{h-1}(1-r)^2}{(1-r^h)(1-r^{h+1})},\quad
\mathbb P(H\ge h)=\frac{r^{h-1}(1-r)}{1-r^h}.
\]
In particular the depth tail is bounded above and below by positive multiples of \(e^{-\alpha h}\), uniformly for all positive integers \(h\). Standard union and lower-tail bounds for \(n\) independent copies imply
\[
H_n^*=\frac{\log n}{\alpha}+O_{\mathbb P}(1).
\]
The tightness follows directly: the upper deviation bound is \(O(e^{-\alpha a})\), and the lower deviation probability is at most \(\exp(-c e^{\alpha a})\) when the integer threshold is shifted by \(a\).

**2. Conditional duration central limit theorem.** Take \(z=e^s\) with real \(s\) near zero; the discriminant is strictly positive at zero and all expressions are analytic near zero. Write \(K(s)=\log u(e^s)\). Since \(u(1)=q/p<1\), the exact expression in step 1 gives an analytic \(C(s)\), nonzero at zero, and \(\vartheta\in(0,1)\) such that uniformly for sufficiently small real \(s\),
\[
\mathbb E[e^{sL}\mid H=h]
=\frac{D_h(e^s)}{D_h(1)}
=C(s)\exp\{h[K(s)-K(0)]\}\bigl(1+O(\vartheta^h)\bigr).
\]
The identity \(K'(s)=2/\sqrt{1-4pq e^{2s}}\) gives
\[
K'(0)=\frac2\delta,\qquad K''(0)=\frac{8pq}{\delta^3}.
\]
Putting \(s=t/\sqrt h\), subtracting the centering \(2h/\delta\), and using Taylor's theorem in the conditional moment generating function proves
\[
\left.\frac{L-2h/\delta}{\sqrt h}\ \right|\ (H=h)
\ \Longrightarrow\ N\left(0,\frac{8pq}{\delta^3}\right)
\quad(h\to\infty).
\]
In this conditional statement the random variable is drawn from the law of \(L\) conditional on \(H=h\); there is no assertion that the duration and height are independent.

The selection index \(I_n\) is a measurable function of the height vector alone. Conditional on all heights, the episode durations are independent with conditional laws determined by their individual heights. In particular, the conditional law of \(L_{I_n}\) is that of \(L\) given \(H=H_n^*\). Combining the preceding conditional normal convergence with the depth tightness and \(H_n^*/\log n\to1/\alpha\), and noting that \(H_n^*-(\log n)/\alpha=O_{\mathbb P}(1)\), yields
\[
\frac{L_{I_n}-\frac{2}{\delta\alpha}\log n}{\sqrt{\log n}}
\ \Longrightarrow\ N\left(0,\frac{8pq}{\delta^3\alpha}\right).
\]
In particular \(L_{I_n}/\log n\to c:=2/(\delta\alpha)\) in probability.

**3. Exact duration tail and uniform empirical ranks.** A positive excursion of duration \(2m\) is one of the \(C_{m-1}\) primitive Dyck paths, where \(C_j=(j+1)^{-1}\binom{2j}{j}\). Every such path has \(m\) downward loss steps (probability \(p\)) and \(m-1\) additional upward loss steps (probability \(q\)) after the forced first step. Thus
\[
\mathbb P(L=2m)=C_{m-1}p^m q^{m-1},\quad m\ge1.
\]
Stirling's formula and the geometric ratio \(4pq<1\) imply the *two-sided*, parity-aware tail estimate, for even \(t\to\infty\),
\[
\mathbb P(L>t)=\Theta\bigl(t^{-3/2}e^{-\beta t}\bigr),\qquad
\mathbb P(L\ge t)=\Theta\bigl(t^{-3/2}e^{-\beta t}\bigr).
\]
Consequently, the logarithms of both tails equal \(-\beta t-\tfrac32\log t+O(1)\). The constants and the bounded remainder may depend on \(p\) but are uniform over even \(t\) tending to infinity.

The strict inequality \(\rho=\beta c<1\) is elementary: put \(x=\alpha/2>0\). Then \(\delta=\tanh x\), \(\beta=\log\cosh x\), and \(\rho=\log\cosh x/(x\tanh x)\). The function \(x\tanh x-\log\cosh x\) vanishes at zero and has derivative \(x/\cosh^2x>0\), proving \(0<\rho<1\). Fix \(\epsilon>0\) small enough that \(\beta(c+\epsilon)<1\). Let \(\mathcal T_n\) contain all even integers between \((c-\epsilon)\log n\) and \((c+\epsilon)\log n\). For every deterministic \(t\in\mathcal T_n\), the counts
\[
N_n^>(t)=\#\{i\le n:L_i>t\},\qquad
N_n^\ge(t)=\#\{i\le n:L_i\ge t\}
\]
are binomial, with expectations uniformly bounded below by a positive power of \(n\). Chernoff bounds and a union bound over \(O(\log n)\) deterministic thresholds show simultaneously, with probability tending to one, that both counts divided by their own expectations lie between \(1/2\) and \(2\) for every \(t\in\mathcal T_n\). This uniform event does **not** require independence between the adaptive selected threshold and the other episode durations: it is established for every deterministic possible threshold first.

By its definition, the rank obeys \(N_n^>(L_{I_n})<R_n\le N_n^\ge(L_{I_n})\), with the lower endpoint enlarged by one if desired. Since \(L_{I_n}\in\mathcal T_n\) with probability tending to one, substitution into the uniform concentration and the two tail estimates gives
\[
\log R_n=\log n-\beta L_{I_n}-\tfrac32\log L_{I_n}+O_{\mathbb P}(1).
\]
The \(O_{\mathbb P}(1)\) term includes finite parity and tie effects, not the logarithmic correction itself.

**4. Joint limit.** Because \(L_{I_n}/\log n\to c>0\), one has \(\log L_{I_n}=O_{\mathbb P}(\log\log n)=o_{\mathbb P}(\sqrt{\log n})\). Also \(\beta c=\rho\). Center the identity in step 3 by \((1-\rho)\log n\) and divide by \(\sqrt{\log n}\): the second coordinate is \(-\beta\) times the first-coordinate fluctuation plus an \(o_{\mathbb P}(1)\) error. The conditional-duration CLT from step 2 and Slutsky's theorem give exactly the displayed joint Gaussian limit.

## Verification

Run `python3 verify.py` with the Python 3 standard library; it completes \(424\) finite assertions for rational choices of \(p\) and \(z\). The script independently solves finite tridiagonal first-passage systems in exact rational arithmetic, compares their solutions against the closed hitting and height generating functions, enumerates first-return masses by exact rational dynamic programming and compares them with Catalan coefficients, and checks elementary derivatives and positivity numerically. It does not simulate an infinite limit or attempt to certify a Gaussian convergence claim by finite experimentation. All limiting statements are justified by the analytic steps above.

## Relationship to prior work

Wu, *When is the deepest drawdown also the longest?* (arXiv:2610.41990v1, first posted 2026-10-30), establishes first-order duration-rank asymptotics for general light-tailed loss excursions, including the two-point model and the exponent \(1-\rho\). It does not present a square-root-logarithmic Gaussian rank law or the logarithmic empirical rank expansion proved here. The first-order exponent and the qualitative separation of deepest and longest drawdowns are therefore prior results, not claimed anew.

Perfilev and Wachtel, *Local tail asymptotics for the joint distribution of length and of maximum of a random walk excursion* (arXiv:1907.02578v1, 2019), obtain conditional central and local limit theorems for a **single** large-height excursion under appropriate hypotheses. Their conditional-duration theory is closely relevant and anticipates the normal fluctuation mechanism in proof step 2. The present contribution is the complete, explicitly normalized, **extreme-selected duration-rank** CLT, including the empirical rank approximation at the adaptive threshold; these do not appear as a result of either cited paper. The explicit two-point generating function yields a self-contained proof without invoking their aperiodic local theorem for this lattice case.

## Limitations

The result applies only to the fixed-bias two-point positive-drift walk, independently sampled nonzero complete episodes, and the growing **number of episodes**, not deterministic physical time. The duration variable is necessarily even, and tie rules are fixed as above. No uniformity as \(p\downarrow1/2\) or \(p\uparrow1\), no functional central limit theorem, no Gaussian or heavy-tailed increment extension, and no independent scientific audit are claimed. The novelty comparison is bounded by the accessible literature and may be superseded by an undiscovered equivalent theorem or a broader prior rank-CLT principle.

## References

1. Yinhao Wu, *When is the deepest drawdown also the longest?*, arXiv:2610.41990v1 (first public version 2026-10-30). https://arxiv.org/html/2610.41990v1
2. Elena Perfilev and Vitali Wachtel, *Local tail asymptotics for the joint distribution of length and of maximum of a random walk excursion*, arXiv:1907.02578v1 (first public version 2019-07-04). https://arxiv.org/abs/1907.02578
