# Unbounded logarithmic resonance depth in Jordan-block invariant graphs

## Finding

For every integer \(m\ge1\), every integer \(k\ge2\), and every real \(0<\lambda<1\), consider the analytic, globally invertible polynomial map with an attracting fixed point
\[
F(x,y)=\bigl(\lambda x,\,\lambda^k(I+N)y+x^k v\bigr),
\]
where \(x\in\mathbb R\), \(y,v\in\mathbb R^m\), and \(N\) is the nilpotent forward shift defined by \((Ny)_i=y_{i+1}\) for \(1\le i<m\) and \((Ny)_m=0\). Denote the last coordinate of \(v\) by \(v_m\).

The following conditions are equivalent:

1. \(v_m=0\).
2. A real-analytic invariant graph \(y=h(x)\) tangent to the \(x\)-axis exists near \(x=0\).
3. A \(C^{k-1,1}\) invariant graph tangent to the \(x\)-axis exists near \(x=0\).

For **every** \(v\), an explicit invariant graph \(h_*\) is \(C^{k-1,\alpha}\) for each \(0<\alpha<1\). When \(v_m\ne0\), no invariant graph can be \(C^{k-1,1}\); moreover, on either side of zero, **every continuous invariant graph** has the universal leading asymptotic
\[
\lim_{x\to0^\pm}
\frac{h_1(x)}{x^k(\log|x|)^m}
=\frac{v_m}{\lambda^k m!(\log\lambda)^m}.
\]
In particular, quadratic forcing \(k=2\) can require an arbitrarily high power \(m\) of a logarithm in the **first resonant order** merely by increasing the transverse Jordan-chain length.

For every initial \(x_0\ne0\) and arbitrary \(y_0\), the orbit \((x_n,y_n)=F^n(x_0,y_0)\) obeys
\[
\lim_{n\to\infty}\frac{(y_n)_1}{\lambda^{kn}n^m}
=\frac{x_0^k v_m}{\lambda^k m!}.
\]
This orbit-level limit is independent of \(y_0\).

## Assumptions and scope

The parameters \(m,k,\lambda,v\) have exactly the ranges above, with no sign restriction on \(v\), and all statements concern the analytic polynomial map on \(\mathbb R^{m+1}\). A graph is locally forward invariant when \(h(\lambda x)=\lambda^k(I+N)h(x)+x^kv\) for all sufficiently small real \(x\). Tangency means \(h(0)=0\) and \(h'(0)=0\). Continuous invariant graphs in the logarithmic-asymptotic statement need only be continuous on each punctured interval \(0<x<\varepsilon\) or \(-\varepsilon<x<0\), with the graph equation holding there. The Hölder class \(C^{k-1,1}\) denotes a Lipschitz \((k-1)\)-st derivative. The derivative of \(F\) at the fixed point is invertible and has one slow eigenvalue \(\lambda\) and one transverse Jordan block with eigenvalue \(\lambda^k\).

## Proof

Put \(J=I+N\) and \(t=\log|x|/\log\lambda\) for \(x\ne0\), so that \(t(\lambda x)=t(x)+1\). For a graph of the form \(h(x)=x^k P(t)\), the invariance equation is exactly
\[
P(t+1)=JP(t)+\lambda^{-k}v.\tag{1}
\]
For every nonnegative integer \(r\) and real \(t\), define the falling-factorial polynomial \(\binom{t}{r}\), with \(\binom{t}{0}=1\). The polynomial vector
\[
P_*(t)=\lambda^{-k}\sum_{r=1}^{m}\binom{t}{r}N^{r-1}v\tag{2}
\]
solves (1). Indeed, Pascal's identity gives \(\binom{t+1}{r}-\binom{t}{r}=\binom{t}{r-1}\), so \(P_*(t+1)-P_*(t)=NP_*(t)+\lambda^{-k}v\), since \(N^m=0\). Thus \(h_*(x)=x^kP_*(\log|x|/\log\lambda)\) for \(x\ne0\), extended by \(h_*(0)=0\), is a two-sided invariant graph. Each component is a finite linear combination of \(x^k(\log|x|)^r\) with \(r\le m\). Differentiating on the two half-lines shows that its derivatives through order \(k-1\) extend continuously by zero, and its \((k-1)\)-st derivative is \(\alpha\)-Hölder for every \(\alpha<1\): the derivative is \(O(|x|(1+|\log|x||)^m)\), while the next derivative is \(O((1+|\log|x||)^m)\). The usual near-zero/far-from-zero two-case mean-value estimate yields the asserted Hölder bound.

For the universal asymptotic, let \(h\) be any continuous graph satisfying the functional equation on a punctured positive or negative half-neighborhood. Set \(P(t)=h(x)/x^k\) for \(x\) of a fixed sign and \(t=\log|x|/\log\lambda\). The values of \(P\) on any compact unit interval \([T,T+1]\) are bounded. Iterating (1) for any \(t=T+s+n\), \(s\in[0,1]\) and integer \(n\ge0\), gives the **exact finite identity**
\[
P(T+s+n)=J^nP(T+s)+\lambda^{-k}\sum_{r=1}^{m}\binom{n}{r}N^{r-1}v.\tag{3}
\]
Because \(J^n=\sum_{j=0}^{m-1}\binom{n}{j}N^j\), the first term on the right is uniformly \(O(n^{m-1})\) as \(n\to\infty\), and the forcing sum has first coordinate \(\lambda^{-k}v_m n^m/m!+O(n^{m-1})\). Hence \(P_1(t)=\lambda^{-k}v_m t^m/m!+O(t^{m-1})\). Replacing \(t\) by \(\log|x|/\log\lambda\) proves the universal graph asymptotic, including its sign and normalization, with no smoothness assumption away from the punctured interval beyond continuity.

Suppose now that \(h\) were a \(C^{k-1,1}\) invariant graph. Its Taylor coefficients \(a_j\) at zero for \(0\le j\le k-1\) satisfy \(\lambda^j a_j=\lambda^k J a_j\) by differentiating the graph equation up to order \(k-1\) (the forcing contributes only at order \(k\)). Since every eigenvalue of \(J\) equals one and \(\lambda^j\ne\lambda^k\), all these coefficients vanish. Taylor's theorem for a Lipschitz \((k-1)\)-st derivative then gives \(h(x)=O(|x|^k)\). If \(v_m\ne0\), the universal limit just proved contradicts this bound, because \(|\log|x||^m\to\infty\). Thus condition 3 implies condition 1.

Conversely, if \(v_m=0\), the vector \(v\) belongs to \(\operatorname{ran}N\). Choose \(a\in\mathbb R^m\) with \(Na=-\lambda^{-k}v\). Then \(h(x)=a x^k\) is an analytic invariant graph: \(\lambda^k a=\lambda^k Ja+v\). This proves condition 1 implies condition 2, while condition 2 trivially implies condition 3, completing the equivalence.

Finally, the orbit equation gives \(x_n=\lambda^n x_0\) and, after dividing the transverse equation by \(\lambda^{k(n+1)}\),
\[
y_n=\lambda^{kn}\left[J^n y_0+\lambda^{-k}x_0^k\sum_{r=1}^{m}\binom nr N^{r-1}v\right].\tag{4}
\]
Its first coordinate has leading coefficient \(\lambda^{-k}x_0^k v_m n^m/m!\), while the homogeneous term has degree at most \(m-1\). This proves the orbit-level limit. All identities hold for every permitted integer \(m,k\) and real \(\lambda,v\); no finite enumeration is invoked to extend the proof to arbitrary order.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic with \(\lambda=1/2\). It checks the polynomial cohomological identity (1), the orbit formula (4), and the range-of-shift condition for all Jordan-chain lengths \(1\le m\le8\), orders \(2\le k\le6\), and the stated finite tests. Run it as `python3 verify.py`; the expected terminal status begins `VERIFY_OK`. These checks corroborate the algebra only. Pascal's identity, the nilpotence formula, the continuity argument, and the Hölder/Taylor reasoning prove the full result for arbitrary admissible parameters.

## Relationship to prior work

Kogelbauer and de la Llave's 2026 study [1], first publicly available September 16, 2026, proves resonant spectral-submanifold regularity with a **semisimple** linearization and exhibits simple and higher-order logarithms. Its Proposition 4.10 bounds logarithmic degree at order \(k\) by \(k-1\) in that semisimple construction; Remark 1.4 and its conclusion explicitly leave Jordan-block extensions untreated. The present calculation instead fixes the resonant forcing order at \(k=2\) while allowing arbitrary logarithmic degree through the nilpotent block. It supplies a sharp analytic/Lipschitz boundary and a trajectory-level coefficient for this exact triangular family; it is **not** a general nonsemisimple existence theorem.

Homburg [2] gives generic resonance obstructions to smooth invariant manifolds and existence results in other smoothness classes, but its inspected main results do not provide the present all-length exact logarithmic coefficient and regularity equivalence. Bonckaert, Naudot, and Yang [3] investigate logarithmic normal-form conjugacies of resonant vector fields, an important earlier related mechanism. Its full text was not accessible for direct comparison, so priority over results potentially implied by that framework remains an explicit risk.

## Limitations

The finding concerns only a special globally invertible triangular polynomial family with a single chosen slow eigenline and transverse nilpotent Jordan chain; it does not solve the 2026 paper's general nonsemisimple analytic problem. The universal leading graph asymptotic assumes continuity on a punctured half-neighborhood and does not imply that every continuous invariant graph is itself Hölder smooth; only the constructed canonical graph enjoys the stated regularity. Polynomial-logarithmic asymptotics do not exclude nonanalytic or nonunique invariant graphs when \(v_m=0\). The finite exact checker is not a universal certificate. Historical priority is provisional, particularly relative to older resonant normal-form literature.

## References

[1] F. Kogelbauer and R. de la Llave, *Existence and Regularity of Stable Resonant Spectral Submanifolds and Linearization Maps*, arXiv:2609.18236 (first posted 2026-09-16), especially Theorem 1.1, Proposition 4.10, Example 6.1, Remark 1.4, and the conclusion. https://arxiv.org/abs/2609.18236

[2] A. J. Homburg, *Invariant manifolds near hyperbolic fixed points*, Journal of Difference Equations and Applications 12 (2006), 1057–1068, Theorem 2.1. https://staff.science.uva.nl/~alejan/Files/contribution.pdf

[3] P. Bonckaert, V. Naudot, and J. H. Yang, *Linearization of hyperbolic resonant germs*, Dynamical Systems 18 (2003), 69–88. https://doi.org/10.1080/1468936031000080821
