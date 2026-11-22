# A finite first-return mean for the one-white Friedman urn walk

## Finding

For the one-dimensional opposite-color Friedman urn walk started from one white ball, the first positive return \(\tau\) to the origin has finite mean. In fact,
\[
\boxed{\mathbb E\tau\le 9999+6400\sqrt{10003/3}<380000.}
\]
This establishes finiteness, not an optimal numerical value. The claim concerns the first return from the original deterministic first step, not a time-homogeneous notion of positive recurrence for the position alone.

## Assumptions and scope

Initially the urn contains one white ball, no blue balls, and a particle at \(0\). At each integer time one uniformly sampled ball is replaced and one ball **of the opposite color** is added. The particle moves \(+1\) for a white sample and \(-1\) for a blue sample. Let \(X_0=0\), and let \(X_n\) be its position after \(n\) samples. Thus \(X_1=1\) almost surely. Define \(\tau=\inf\{n\ge1:X_n=0\}\), with \(\inf\varnothing=\infty\). No assumptions of independent increments or time homogeneity are made.

With \(W_n\) and \(B_n\) denoting the respective draw counts, \(W_n+B_n=n\) and \(X_n=W_n-B_n\). The urn has \(1+B_n\) white and \(W_n\) blue balls after \(n\) steps. Therefore, for an admissible \(x\),
\[
\Pr(X_{n+1}=x+1\mid X_n=x)=\frac{n+2-x}{2(n+1)},\qquad
\mathbb E[X_{n+1}-X_n\mid X_n=x]=\frac{1-x}{n+1}.
\]
On \(\{\tau>n\}\), necessarily \(1\le X_n\le n\), which is the half-line on which the Lyapunov argument is applied.

## Proof

**Step 1 (an explicit time-dependent potential).** For \(z\ge0\), set
\[
F(z)=48z+\frac{16z}{1+z},\qquad V(t,x)=tF(x/\sqrt t)\quad(t\ge1,\ x\ge0).
\]
The potential is nonnegative, \(V(t,0)=0\), and \(V(t,x)\le64\sqrt t\,x\). Its derivatives satisfy
\[
F'(z)=48+\frac{16}{(1+z)^2},\quad F''(z)=-\frac{32}{(1+z)^3},\quad F^{(3)}(z)=\frac{96}{(1+z)^4}.
\]
The time–space differential combination governing the first-order conditional drift is
\[
\mathcal LF(z):=F(z)-\tfrac32zF'(z)+\tfrac12F''(z)
=-24z+\frac{16(z-1)(z^2+\tfrac32z+1)}{(1+z)^3}.
\]
We now verify the **uniform** inequality \(\mathcal LF(z)\le-64/27\) for all \(z\ge0\). If \(0\le z\le1/2\), the numerator factor \(z-1\le-1/2\), the positive quadratic factor is at least \(1\), and \((1+z)^3\le27/8\), so the fraction multiplied by \(16\) is at most \(-64/27\); the term \(-24z\) helps. For \(1/2\le z\le1\), the fraction is nonpositive and \(-24z\le-12\). For \(z\ge1\), comparison of the two cubic polynomials shows \((z-1)(z^2+\tfrac32z+1)/(1+z)^3\le1\); thus \(\mathcal LF(z)\le-24z+16\le-8\).

**Step 2 (a genuine discrete drift inequality).** Put \(t=n+1\) and \(z=x/\sqrt t\). On \(\{\tau>n\}\) we have \(1\le x\le t-1\). For \(\xi=X_{n+1}-X_n\in\{-1,1\}\), Taylor's theorem with \(0\le x+\xi\le t\) yields
\[
\begin{aligned}
\mathbb E[V(t,x+\xi)]-V(t,x)
&\le -zF'(z)+\tfrac1{\sqrt t}F'(z)+\tfrac12F''(z)+\tfrac{16}{\sqrt t},\\
V_t(t,x)&=F(z)-\tfrac12zF'(z).
\end{aligned}
\]
The spatial Taylor remainder is bounded by \(\sup_{u\ge0}|V_{xxx}(t,u)|/6\le16/\sqrt t\). Also
\[
V_{tx}(t,x)=\frac{F'(z)-zF''(z)}{2\sqrt t},\qquad
V_{tt}(t,x)=-\frac{z(F'(z)-zF''(z))}{4t}.
\]
For every \(z\ge0\), \(F'(z)\le64\) and \(F'(z)-zF''(z)\le80\). Indeed the latter follows directly from \(2z/(1+z)^3\le1\). For intermediate times \(s\in[t,t+1]\) and positions \(y=x\pm1\), we have \(0\le y/\sqrt s\le\sqrt t\). Hence \(|V_{tt}(s,y)|\le20/\sqrt t\), while \(|V_t(t,y)-V_t(t,x)|\le40/\sqrt t\). Combining the one-step spatial expansion with the time expansion gives, uniformly on the indicated state range,
\[
\mathbb E[V(t+1,x+\xi)]-V(t,x)
\le\mathcal LF(z)+\frac{64+16+40+10}{\sqrt t}
\le-\frac{64}{27}+\frac{130}{\sqrt t}.
\]
In particular, for \(n\ge9999\) (so \(t\ge10000\)), the right side is at most \(-64/27+13/10<-1\). This is an exact bound on the true discrete transition, not an appeal to a diffusion approximation.

**Step 3 (stopping and integrability).** Define \(Y_n=V(n+1,X_n)\) on \(\{\tau>n\}\), and \(Y_n=0\) on \(\{\tau\le n\}\), for \(n\ge9999\). At a step that hits zero, the potential vanishes. By Step 2 and the fact that \(Y_n\) stays zero after stopping,
\[
\mathbb E[Y_{n+1}\mid\mathcal F_n]\le Y_n-\mathbf1_{\{\tau>n\}}\qquad(n\ge9999).
\]
Summation of expectations up to an arbitrary finite horizon, followed by monotone convergence, gives
\[
\sum_{n=9999}^{\infty}\Pr(\tau>n)\le\mathbb E Y_{9999}.
\]
For \(n\ge1\), the exact drift shows \(\mathbb E X_n=1\). Squaring the increment and conditioning yields
\[
\mathbb E[X_{n+1}^2\mid X_n=x]
=\frac{n-1}{n+1}x^2+\frac{2x}{n+1}+1.
\]
Starting from \(X_2=0\) or \(2\), each with probability \(1/2\), induction gives \(\mathbb E X_n^2=(n+4)/3\) for every \(n\ge2\). Therefore Cauchy–Schwarz and the potential bound imply
\[
\begin{aligned}
\mathbb E\tau
&=\sum_{n\ge0}\Pr(\tau>n)\\
&\le9999+\mathbb E Y_{9999}\\
&\le9999+6400\sqrt{\mathbb E X_{9999}^2}\\
&=9999+6400\sqrt{10003/3}<380000.
\end{aligned}
\]
The bound also implies \(\Pr(\tau<\infty)=1\). This completes the proof.

## Verification

The attached `verify.py` is a self-contained Python standard-library checker. It tests the exact urn transitions and the first and second unconditional moments using rational arithmetic over finite horizons; checks the displayed algebraic identity on rational points; evaluates the finite inequalities and the bound numerically; and verifies the actual discrete Lyapunov drift on representative admissible states. The all-state inequality and the infinite expectation bound are proved in the text, not inferred from the finite checker.

## Relationship to prior work

Balaji and Mahmoud, *Urn-driven random walks* (arXiv:2504.14813), prove recurrence of the one-dimensional Friedman walk and explicitly conjecture finite expected first-return time in Section 5. Their Eulerian-number return probabilities do not establish the mean return time; the bound above resolves that specifically stated conjecture for the one-white urn. Bertoin, *Counting the zeros of an elephant random walk* (arXiv:2105.09569), obtains closely related first-return laws for elephant walks. The present urn process can be viewed as a shifted-level problem for a zero-memory elephant walk, but Bertoin's stated results for **returns to the elephant walk's own origin** do not directly give the first hitting time of that shifted level. Menshikov and Volkov, *Urn-related random walk with drift \(\rho x^\alpha/t^\beta\)* (arXiv:0711.2373), address different urn-driven recurrence regimes. Classical Lyapunov and stopping methods are used; no priority is claimed for those techniques themselves.

## Limitations

The upper bound is intentionally coarse and does not identify the exact mean, a sharp tail asymptotic, or higher-dimensional behavior. This is a first-return statement for a **time-inhomogeneous** position process, not an assertion of a time-homogeneous invariant distribution. Literature comparisons are not a proof of global novelty, and independent mathematical audit has not been performed.

## References

- S. Balaji and H. Mahmoud, *Urn-driven random walks*, arXiv:2504.14813 (first public version 2025-04-21), https://arxiv.org/abs/2504.14813 .
- J. Bertoin, *Counting the zeros of an elephant random walk*, arXiv:2105.09569, https://arxiv.org/abs/2105.09569 .
- M. Menshikov and S. Volkov, *Urn-related random walk with drift \(\rho x^\alpha/t^\beta\)*, arXiv:0711.2373, https://arxiv.org/abs/0711.2373 .
