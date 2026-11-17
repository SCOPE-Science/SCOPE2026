# Dense-range restoration of the one-time stable-codimension criterion for \(h\)-dichotomies

## Finding
For noninvertible evolution families with dense-range forward propagators, one finite-codimension hypothesis **at initial time only** suffices for the equivalence of \(h\)-dichotomy, \(h\)-expansiveness, and uniform \(h\)-noncriticality. This removes the all-time stable-codimension hypothesis in Theorem 3 of Dragičević [1] for this substantial class of non-surjective evolution families.

More precisely, if \(d=\operatorname{codim}\mathcal{S}(0)<\infty\), then under uniform \(h\)-noncriticality the equality
\[
\operatorname{codim}\mathcal{S}(s)=d\qquad (s\ge 0)
\]
holds. Together with Theorem 3 of [1], this proves the equivalence.

## Assumptions and scope
Let \(X\) be a real or complex Banach space. Let \(h:[0,\infty)\to[1,\infty)\) be continuous, strictly increasing, onto its range, satisfy \(h(0)=1\), and diverge to infinity. Let \(T(t,s)\), \(t\ge s\ge0\), be a bounded-operator evolution family, strongly continuous in each time variable as defined in [1], with \(T(s,s)=I\) and \(T(t,r)T(r,s)=T(t,s)\). Assume \(h\)-bounded growth: constants \(K,\omega>0\) satisfy
\[
\|T(t,s)\|\le K(h(t)/h(s))^\omega\quad(t\ge s).
\]
For every \(s\ge0\), let \(\mathcal{S}(s)=\{v\in X:\sup_{t\ge s}\|T(t,s)v\|<\infty\}\). The two further standing assumptions are \(d=\dim(X/\mathcal{S}(0))<\infty\) and \(\overline{T(s,0)X}=X\) for every \(s\ge0\). Neither operator invertibility nor surjectivity is assumed.

Use the standard \(h\)-dichotomy and \(h\)-expansivity definitions of [1, Definitions 4–5]. Explicitly, \(h\)-expansivity means the existence of \(L,\beta>0\) such that
\[
\|T(t,a)v\|\le L\big[(h(t)/h(a))^{-\beta}\|v\|+(h(b)/h(t))^{-\beta}\|T(b,a)v\|\big]
\]
for every \(a\le t\le b\) and \(v\in X\). Uniform \(h\)-noncriticality means \(\theta\in(0,1)\), \(C>0\) exist such that, for \(u=h^{-1}(e^Ch(s))\) and \(w=h^{-1}(e^{2C}h(s))\),
\[
\|T(u,s)v\|\le\theta\sup_{s\le r\le w}\|T(r,s)v\|
\]
for every \(s\ge0\), \(v\in X\). As in [1], an \(h\)-dichotomy is an invariant splitting with forward \(h\)-contraction on the stable projection and invertible backwards \(h\)-contraction on the complementary finite-dimensional unstable bundle.

## Proof
**Step 1: Uniform stable-space bound and closedness.** Assume uniform \(h\)-noncriticality. Rescale time by \(\tau=\log h(t)\): define \(U(\tau,\sigma)=T(h^{-1}(e^\tau),h^{-1}(e^\sigma))\). The rescaled evolution family has exponential bounded growth and uniform noncriticality with the same \(C,\theta\), as in [1, Propositions 3–4]. Fix \(\sigma\ge0\) and a vector \(v\) with bounded future \(U\)-orbit; let \(M=\sup_{r\ge\sigma}\|U(r,\sigma)v\|<\infty\). For each \(r\ge\sigma+C\), apply noncriticality at \(r-C\) to \(U(r-C,\sigma)v\):
\[
\|U(r,\sigma)v\|\le\theta\sup_{r-C\le z\le r+C}\|U(z,\sigma)v\|\le\theta M.
\]
Hence the supremum \(M\) must be attained on \([\sigma,\sigma+C]\) in the sense \(M=\sup_{\sigma\le r\le\sigma+C}\|U(r,\sigma)v\|\); otherwise \(M\le\max(\theta M,\sup_{[\sigma,\sigma+C]}\cdots)<M\). Exponential bounded growth now yields \(M\le Ke^{\omega C}\|v\|\). Passing to limits of sequences inside the bounded-orbit subspace shows that every \(\mathcal{S}(s)\) is a **closed** linear subspace. This is the initial bound in the proof of Lemma 3 of [1], which requires no codimension hypothesis.

**Step 2: Dense range propagates the finite codimension.** Fix \(s\ge0\). By the cocycle identity and local boundedness on \([0,s]\),
\[
\mathcal{S}(0)=T(s,0)^{-1}\mathcal{S}(s).
\]
Choose a \(d\)-dimensional complement \(Z\) to the closed finite-codimensional space \(\mathcal{S}(0)\). Then \(T(s,0)Z\cap\mathcal{S}(s)=\{0\}\), and \(T(s,0)|_Z\) is injective (both follow from the displayed preimage identity). Hence \(\dim T(s,0)Z=d\). Moreover,
\[
T(s,0)X\subset\mathcal{S}(s)+T(s,0)Z.
\]
The right-hand side is closed because it is the sum of a closed space and a finite-dimensional space. The left-hand side is dense by assumption, so \(X=\mathcal{S}(s)\oplus T(s,0)Z\). Thus \(\operatorname{codim}\mathcal{S}(s)=d\) for every \(s\ge0\).

**Step 3: Equivalence.** The already established implications \(h\)-dichotomy \(\Rightarrow\) \(h\)-expansivity \(\Rightarrow\) uniform \(h\)-noncriticality are [1, Theorem 3 and its proof]. Under the last condition, Steps 1–2 establish its missing all-time codimension hypothesis, and [1, Theorem 3] yields the \(h\)-dichotomy. This closes the cycle of implications.

**Genuinely non-surjective example.** Set \(X=\ell^2(\mathbb N)\oplus\mathbb R\), and for \(q=h(s)/h(t)\in(0,1]\) let
\[
T(t,s)((x_n)_{n\ge1},y)=((q^n x_n)_{n\ge1},q^{-1}y).
\]
Every positive-time operator has dense range (all finitely supported sequences plus the real coordinate occur in the range) but is not surjective: when \(q<1\), \((q^{n/2})_{n\ge1}\in\ell^2\) has no \(\ell^2\) preimage. The bounded-orbit space is \(\ell^2\oplus\{0\}\), of codimension one. The constant splitting is an \(h\)-dichotomy with \(D=\lambda=1\). This demonstrates that the criterion is not merely the invertible case in disguise.

## Verification
The argument is entirely analytic; no numerical computation, finite enumeration, or infinite certificate is invoked. Direct checkpoints are the preimage identity, the uniform stable-orbit bound, closedness of the finite-dimensional sum, and the explicit dense-but-non-surjective diagonal semigroup. Each is reproduced above. The final implication uses the stated all-time-codimension theorem from the primary source [1].

## Relationship to prior work
Dragičević [1, Theorems 2–3] proves the three-way characterization under a constant finite codimension of \(\mathcal{S}(s)\) **for every time**, and its Example 1 shows that a finite-codimension condition at time zero alone fails for noninvertible propagators. The present result identifies a different, natural density condition that recovers the one-time hypothesis without requiring surjectivity. Unlike the earlier invertible theory discussed in [1], it also applies to compact smoothing semigroups whose positive-time maps are never onto. The novel assertion is the dense-range propagation step, not the general characterization of [1].

## Limitations
Dense range is sufficient, not asserted necessary. Without uniform noncriticality the closure of \(\mathcal{S}(s)\) is not established by this argument. The theorem is confined to positive half-time evolution families with the stated bounded growth, finite initial unstable codimension, and the precise definitions of [1]. It does not cover the negative-time dual characterization or arbitrary non-dense propagators. No claim of priority beyond the examined sources is made.

## References
[1] D. Dragičević, *\(h\)-dichotomies via uniform noncriticality and expansiveness for noninvertible evolution families*, arXiv:2611.08451, first publicly submitted 2026-11-05, https://arxiv.org/html/2611.08451v2, especially Definitions 3–6, Propositions 3–4, Theorems 2–3, Lemma 3, and Example 1.
