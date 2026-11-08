# Sharp transform ordering and exponential mean gap among reset-neutral gambler's-ruin laws

## Finding

In the biased gambler's-ruin walk with independent geometric resetting, all reset laws that preserve the original absorption-side probability admit a **strict, universal ranking of absorption-time transforms**. The known reset-neutral endpoint-reflection pairs are ranked entirely by their distance from the center. The outermost pair uniquely minimizes mean absorption time within the full neutral class, and the central pair uniquely maximizes it, for every resetting probability. Their expected absorption times can differ exponentially in the interval length, even though their probabilities of exiting on the left are identical.

Precisely, for \(a\ge4\), \(p,\gamma\in(0,1)\), and \(1\le x\le\lfloor a/2\rfloor\), let \(r=q/p\), \(q=1-p\), \(m=a/2\), and

\[
\pi_x(x)=\frac{r^{m-x}}{1+r^{m-x}},\qquad
\pi_x(a-x)=\frac1{1+r^{m-x}}.
\]

For the midpoint when \(a\) is even, interpret the pair as one point mass. Let \(T_x\) be the absorption time starting from \(\pi_x\), with the same law used at every reset. For \(0<z<1\),

\[
\mathbb E[z^{T_1}]>\mathbb E[z^{T_2}]>\cdots>
\mathbb E[z^{T_{\lfloor a/2\rfloor}}].
\]

The order is strict for every bias and reset probability. Convex mixtures of the pairs give **all** reset-neutral laws, so the endpoints are the unique simultaneous extremizers within that complete class. In particular,

\[
\mathbb E[T_1]<\mathbb E[T_2]<\cdots<
\mathbb E[T_{\lfloor a/2\rfloor}].
\]

## Assumptions and scope

Fix an integer \(a\ge4\). The state space is \(\{0,1,\ldots,a\}\), with absorbing states \(0,a\). From an interior point, each discrete time step independently resets, with probability \(\gamma\in(0,1)\), to an independent draw from a fixed interior law \(\pi\); otherwise it jumps one unit to the right with probability \(p\in(0,1)\) and left with probability \(q=1-p\). Reset steps each count one time unit; \(X_0\) is drawn from \(\pi\). The absorption time \(T_\pi\) is almost surely finite.

A distribution \(\pi\) is **reset-neutral** when the probability of absorption at \(0\) is independent of \(\gamma\) throughout \((0,1)\). Write \(r=q/p>0\), \(m=a/2\), and \(H=\frac12\log r\). For integer \(x\) in the range \(1\le x\le\lfloor a/2\rfloor\), \(\pi_x\) is the reflected-pair distribution in Finding, including the single midpoint at even \(a\). The geometric-reset independence and the requirement that the starting law equal the reset law are essential.

## Proof

**Step 1: characterize the admissible laws (previously established neutral structure, reproved for completeness).** Let \(\tau\) be the no-reset hitting time of either endpoint, and for each interior position \(i\) and \(0<v<1\) put

\[
u_i(v)=\mathbb E_i[v^\tau\mathbf1_{\{X_\tau=0\}}],\qquad
b_i(v)=\mathbb E_i[v^\tau\mathbf1_{\{X_\tau=a\}}].
\]

A nearest-neighbor path from \(i\) to \(a\) has \(a-i\) more right than left jumps. Reversing the path about the midpoint gives the exact identity

\[
b_{a-i}(v)=\left(\frac pq\right)^i u_i(v).
\]

Also \(u_i(v)=q^iv^i+O(v^{i+2})\) as \(v\downarrow0\). Consequently the functions \(u_1,\ldots,u_{a-1}\) are linearly independent, as their smallest nonzero powers are distinct. By renewal at the first reset, the full reset-walk left-exit probability is

\[
\frac{U_\pi(1-\gamma)}{U_\pi(1-\gamma)+B_\pi(1-\gamma)},
\qquad U_\pi(v)=\sum_i\pi_i u_i(v),\quad B_\pi(v)=\sum_i\pi_i b_i(v).
\]

This ratio is constant for all \(\gamma\in(0,1)\) if and only if there exists a constant \(R>0\) with \(U_\pi(v)=R B_\pi(v)\) for all \(v\in(0,1)\). By the reflection identity and linear independence, this is equivalent to

\[
\pi_i=R\left(\frac pq\right)^i\pi_{a-i}
\quad(1\le i<a).
\]

Applying this constraint to \(i\) and \(a-i\) forces \(R^2=(q/p)^a\), hence \(R=r^m\). Thus \(\pi_i=r^{m-i}\pi_{a-i}\); every such law is a convex mixture \(\pi=\sum_x\alpha_x\pi_x\), with \(\alpha_x\ge0\) and \(\sum_x\alpha_x=1\). Its common probability of left exit is \(r^m/(1+r^m)\). This classification is background from the motivating work, not an originality claim here.

**Step 2: compute the previously unused scalar hitting-time transform.** Let \(s_i(v)=\mathbb E_i[v^\tau]\), so \(s_0=s_a=1\) and

\[
s_i(v)=v\,[p\,s_{i+1}(v)+q\,s_{i-1}(v)].
\]

Put \(h=\sqrt{q/p}=e^H\) and \(s_i=h^i f_i\). The recurrence becomes

\[
f_{i+1}+f_{i-1}=2\cosh(\eta_v)f_i,
\qquad \eta_v=\operatorname{arcosh}\frac{1}{2v\sqrt{pq}},
\]

with \(f_0=1\), \(f_a=h^{-a}\). Its unique solution is a linear combination of \(\cosh((i-m)\eta_v)\) and \(\sinh((i-m)\eta_v)\). The symmetric coefficient equals \((1+h^{-a})/(2\cosh(m\eta_v))\). Averaging \(s_x\) and \(s_{a-x}\) with their specified pair weights cancels the antisymmetric coefficient and gives exactly

\[
S_x(v):=\mathbb E_{\pi_x}[v^\tau]
=\frac{\cosh(mH)}{\cosh(m\eta_v)}
\frac{\cosh((m-x)\eta_v)}{\cosh((m-x)H)}.
\tag{1}
\]

Since \(0<v<1\), \(\eta_v>|H|\ge0\). The function \(d\mapsto \cosh(d\eta_v)/\cosh(d|H|)\) has strictly positive logarithmic derivative for \(d>0\):

\[
\eta_v\tanh(d\eta_v)-|H|\tanh(d|H|)>0.
\]

Therefore \(S_1(v)>S_2(v)>\cdots>S_{\lfloor a/2\rfloor}(v)\) for every \(v\in(0,1)\). This also holds when the innermost distance equals zero.

**Step 3: renewal at geometric resets.** Set \(v=(1-\gamma)z\), \(0<z<1\), and \(S_\pi(v)=\sum_x\alpha_xS_x(v)\). During a cycle, the contribution from absorption without a reset is \(S_\pi(v)\). The contribution from a reset before absorption is

\[
\sum_{k\ge0}\gamma z[(1-\gamma)z]^k\Pr_\pi(\tau>k)
=\frac{\gamma z(1-S_\pi(v))}{1-v}.
\]

Because after a reset the process restarts independently with law \(\pi\), its probability-generating function \(F_\pi(z)=\mathbb E[z^{T_\pi}]\) satisfies a scalar renewal equation, yielding

\[
F_\pi(z)=\frac{(1-v)S_\pi(v)}{1-z+\gamma z S_\pi(v)}.
\tag{2}
\]

At fixed \(z,\gamma\), the derivative of the displayed rational expression with respect to \(S_\pi(v)\) is

\[
\frac{(1-v)(1-z)}{(1-z+\gamma zS_\pi(v))^2}>0.
\]

Thus (1) implies the **strict simultaneous transform ordering**, and linearity in \(\pi\) makes \(\pi_1\) and \(\pi_{\lfloor a/2\rfloor}\) the unique extreme laws over all neutral mixtures. Differentiation of (2) at \(z=1\), or the expected number of regenerative cycles, gives

\[
\mathbb E[T_\pi]=\frac{1-S_\pi(1-\gamma)}{\gamma S_\pi(1-\gamma)}.
\tag{3}
\]

Since the right side is strictly decreasing in \(S_\pi\), (1) yields the strict reversed ordering of the means. A transform order is not asserted to imply ordinary stochastic domination.

**Step 4: sharp long-interval contrast.** Fix \(p,\gamma\in(0,1)\) and define \(\eta=\eta_{1-\gamma}\), \(\Delta=\eta-|H|>0\). As \(a\to\infty\), equation (1), with \(x=1\) and \(d=m-1\), yields \(S_1(1-\gamma)\to e^{-\Delta}\). Equations (1) and (3) then imply

\[
\mathbb E[T_1]\longrightarrow\frac{e^{\Delta}-1}{\gamma}.
\tag{4}
\]

For \(x=\lfloor a/2\rfloor\), the distance \(d=m-x\) equals zero or one half. Its hyperbolic-cosine ratio stays bounded above and below independently of \(a\), while \(\cosh(mH)/\cosh(m\eta)=\exp(-m\Delta+O(1))\). Therefore (3) gives

\[
\lim_{a\to\infty}\frac1a\log\mathbb E[T_{\lfloor a/2\rfloor}]=\frac\Delta2>0.
\tag{5}
\]

The endpoints have the same absorption-side probability for every finite interval, but radically different absorption-time scales.

## Verification

A standalone checker, `check_reset_neutral.py`, uses exact rational Gauss–Jordan solutions of the full absorbing-chain equations, independently of the renewal formulas. It covers even domain sizes \(4,6,8,10\) and odd sizes \(5,7,9\), multiple rational biases, three resetting rates and three generating-function arguments. It verifies normalization, reset-neutral left-exit probabilities, discounted channel ratios, renewal probability-generating functions, expected times and strict transform ranking. Run `python3 check_reset_neutral.py` (Python standard library only). The recorded result was **2,382 exact rational assertions passed**. Finite checks support, but do not establish, the infinite parameter-range result: that is supplied by the preceding proof.

For illustration, when \(a=6\), \(p=1/2\), and \(\gamma=1/3\), the three free absorption transforms \(S_1(2/3),S_2(2/3),S_3(2/3)\) are respectively \(7/18,1/6,1/9\); by (3), their reset means are \(33/7,15,24\). All have left-exit probability \(1/2\).

## Relationship to prior work

Vega Coso (2026) derives the spectral duality and symmetric-pair classification that preserves gambler's-ruin splitting probabilities across geometric resetting. Those neutral pairs and their common exit probability are **not** new claims here. The present result adds a sharp, model-wide ordering of absorption-time generating functions across that entire neutral class, an exact restart mean identity, and exponential asymptotic separation between its best and worst times. The inspected full text of the motivating article did not state this comparison. Earlier multi-site resetting studies by González–Riascos–Boyer (2021) and Wang–Chen–Huang (2021) treat network first-passage statistics, but not the complete symmetric-pair neutrality constraint and its universal extremizers. Companion works on reset-distribution geometry and resolvent duality remain a historical-priority risk because complete texts could not be inspected.

## Limitations

Only nearest-neighbor homogeneous walks on finite intervals are treated, with independent state-independent geometric resets and a starting distribution identical to the reset law. The conclusions concern the complete reset-neutral class, **not** arbitrary reset laws, arbitrary target sets, general initial laws, or general renewal resetting. The theorem proves Laplace-transform ordering and means, not stochastic domination. It gives sharp exponential growth rates, not a complete limiting distribution of absorption times. Historical priority and all scientific conclusions require independent mathematical assessment; the included checks are finite examples.

## References

1. J. A. Vega Coso, *Spectral Duality and Reset-Neutral Distributions in Random Walks with Multi-Site Geometric Resetting*, arXiv:2605.00657, first public May 1, 2026. https://arxiv.org/abs/2605.00657
2. L. González, A. P. Riascos, and D. Boyer, *Diffusive transport on networks with stochastic resetting to multiple nodes*, arXiv:2104.00727 (2021). https://arxiv.org/abs/2104.00727
3. S. Wang, H. Chen, and F. Huang, *Random walks on complex networks with multiple resetting nodes: a renewal approach*, arXiv:2105.08323 (2021). https://arxiv.org/abs/2105.08323
4. J. A. Vega Coso, *Separatrix structure and the geometry of reset distributions*, arXiv:2607.10717 (2026), abstract consulted; full text unavailable at review. https://arxiv.org/abs/2607.10717
5. J. A. Vega Coso, *Resolvent intertwining and spectral duality in Markov chains with geometric resetting*, arXiv:2608.15140 (2026), abstract consulted; full text unavailable at review. https://arxiv.org/abs/2608.15140
