# Sharp finite-world periods for iterated belief disagreement

## Finding
Consider two deterministic doxastic agents on a nonempty finite set of worlds \(W\). Their accessibility relations are graphs of maps \(f,g:W\to W\) satisfying \(f^2=f\) and \(g^2=g\), equivalently each relation is functional and satisfies the serial, transitive, Euclidean (KD45) conditions. Their *strong-disagreement bundle* is
\[
\mathsf D\varphi :=(\Box_f\varphi\wedge\Box_g\neg\varphi)\vee(\Box_g\varphi\wedge\Box_f\neg\varphi).
\]
For a fixed frame, let \(P(f,g)\) be the least positive integer \(t\) for which there is an integer \(K\ge0\) such that, for all \(k\ge K\), all propositional valuations and every formula \(\varphi\), the frame validates \(\mathsf D^{k+t}\varphi\leftrightarrow\mathsf D^k\varphi\). Such a period exists because the frame is finite.

**Theorem (sharp dyadic realization).** For every integer \(r\ge1\), the smallest possible number of worlds of a finite two-agent functional KD45 frame with \(P(f,g)=2^r\) is
\[
\boxed{\,2^{r-1}+2\,}.
\]
An explicit frame of that minimum size has stabilization index one: its iterated disagreement operators are periodic from the first application, with exact period \(2^r\). Therefore no fixed finite modal nesting depth collapses all iterates of strong disagreement over the class of finite functional two-agent KD45 frames. In fact, the formulas \(\mathsf D^j p\), \(j\ge1\), are pairwise inequivalent over that class.

## Assumptions and scope
The finite set \(W\) is nonempty and may contain reflexive accessibility loops. Each agent has exactly one accessible world at each world, and the individual accessibility maps are idempotent. Arbitrary Boolean valuations of propositional letters are allowed. The bundled operator is interpreted recursively, so applying \(\mathsf D\) to a formula uses that formula's current truth set. The minimality theorem concerns **exact powers-of-two eventual periods**; other eventual periods may arise on other frames. It makes no claim about the full nonfunctional KD45 class or any uniform finite-period bound there.

For a finite set of size \(n\), regard truth sets as vectors in \(V=\mathbb F_2^n\), and write the constant-one vector as \(\mathbf 1\). Because the two agents have singleton successor sets, the truth vector of \(\mathsf D\varphi\) is
\[
(Tx)(w)=x(f(w))+x(g(w))\pmod 2.
\]
The sum here is over \(\mathbb F_2\); this identity applies to **any** input formula, not only atomic formulas.

## Proof
**1. Linearization and the period on the stable image.** The operator \(T:V\to V\) is linear. We always have \(T\mathbf1=\mathbf0\); hence \(\dim\operatorname{im}T\le n-1\). Choose \(h\) sufficiently large that \(U=\operatorname{im}T^h=\operatorname{im}T^{h+1}\). Then \(S=T|_U\) is invertible. Its order is exactly \(P(f,g)\): the powers of \(T\) eventually agree if and only if the corresponding powers of \(S\) agree, since each sufficiently large \(T^k\) maps onto \(U\). Formula equivalence for all valuations is equivalent to equality of the corresponding linear operators, since atomic valuations realize every input vector.

**2. Lower bound for dyadic periods.** Suppose \(P(f,g)=2^r\), with \(r\ge1\). In characteristic two, \(S^{2^r}=I\) implies
\[
(S+I)^{2^r}=S^{2^r}+I=0.
\]
But exact order \(2^r\) gives \(S^{2^{r-1}}\ne I\), so \((S+I)^{2^{r-1}}\ne0\). Thus the nilpotent operator \(N=S+I\) on \(U\) has nilpotency index exceeding \(2^{r-1}\). Any nilpotent operator on a vector space of dimension \(d\) satisfies \(N^d=0\). Consequently
\[
2^{r-1}+1\le\dim U\le\operatorname{rank}T\le n-1,
\]
and hence \(n\ge2^{r-1}+2\).

**3. A family meeting the bound.** Put \(m=2^{r-1}+1\) and \(W=\{0,1,\ldots,m\}\). Set \(f(0)=g(0)=0\). For positive even \(i\), set \(f(i)=i\) and \(g(i)=i-1\). For odd \(i\), set \(f(i)=i-1\) and \(g(i)=i\). Every target of \(f\) is even and fixed by \(f\); every target of \(g\) is either zero or odd and fixed by \(g\). Thus \(f^2=f\) and \(g^2=g\). The two relations therefore satisfy KD45.

For \(x\in V\), the disagreement transformation is
\[
(Tx)_0=0,\qquad (Tx)_i=x_i+x_{i-1}\quad (1\le i\le m).
\]
Let \(U=\{x:x_0=0\}\). On \(U\), \(T=I+N\), where \((Nx)_1=0\) and \((Nx)_i=x_{i-1}\) for \(2\le i\le m\). This is a single nilpotent Jordan shift of size \(m\): \(N^m=0\) but \(N^{m-1}\ne0\). Since \(I+N\) is invertible, \(\operatorname{im}T=U\). By the characteristic-two binomial identity,
\[
(I+N)^{2^r}=I+N^{2^r}=I,
\qquad (I+N)^{2^{r-1}}=I+N^{2^{r-1}}\ne I.
\]
Its order is exactly \(2^r\), and this is the eventual period of \(T\) from its first application. The frame has exactly \(m+1=2^{r-1}+2\) worlds.

**4. No global collapse.** Given distinct positive integers \(a,b\), choose \(r\) with \(2^r>|a-b|\). On the constructed frame, \(T^a\ne T^b\), since the powers on \(U\) are distinct modulo \(2^r\), and \(\operatorname{im}T=U\). Some atomic valuation distinguishes \(\mathsf D^a p\) and \(\mathsf D^b p\) at a world. This proves pairwise inequivalence.

## Verification
Running `python checker.py` with Python 3 and no external packages enumerates all pairs of idempotent successor maps on every labelled set of one through four worlds, computes their exact preperiods and periods, and checks the explicit family for exponents \(1\le r\le6\). The expected terminal line is `BUNDLED_DISAGREEMENT_DYADIC_PERIODS_OK`. For one through four worlds the numbers of possible agent-map pairs are respectively \(1,9,100,1681\); periods of length \(2\) first occur at three worlds and of length \(4\) at four worlds. These finite checks are a supplement, not a proof of the all-\(r\) statement.

## Relationship to prior work
Ding and Yang, *A General Theory of Propositional Modal Bundled Modalities*, first public on 2026-03-27, develops the logic and bisimulation theory of bundled modalities. Its Section 5.1 explicitly treats the disagreement-in-group operator on KD45 frames, including the two-agent strong-disagreement case. The present theorem studies a distinct finite-frame *dynamical* invariant: the exact eventual periodicity of iterating that operator, and the sharp number of functional-KD45 worlds required for each dyadic period. Their inspected full text does not state this model-size theorem or its linear-algebraic argument.

Chen and Pan, *Logic for Describing Strong Belief-Disagreement Between Agents* (2018), is earlier directly relevant work on the same operator, with soundness and completeness results. Its freely available abstract and references were examined; full text was not available in the checked open sources. Thus a priority comparison with that paper remains incomplete. A general known fact about unipotent operators over characteristic two is used in a direct proof rather than claimed as new; likewise, individual functional KD45 accessibility maps being idempotent is standard. Related results on binary parity automata or on other finite KD45 semantics do not automatically cover the sharp modal-iteration frame-size law.

## Limitations
The theorem concerns two agents, singleton successor relations, unrestricted valuations, and exact dyadic eventual periods. It does not classify every possible eventual period on arbitrary finite functional KD45 frames and gives no small-model bound for nonfunctional relations. The bound is established by an ordinary mathematical proof, with examples checked computationally; no independent mathematical audit or full historical-priority certification has been conducted. The 2018 source's unavailable full text is a specific remaining originality risk.

## References
1. Y. Ding and Y. Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268, first submitted 2026-03-27, especially Section 5.1. https://arxiv.org/abs/2603.26268
2. J. Chen and T. Pan, *Logic for Describing Strong Belief-Disagreement Between Agents*, *Studia Logica* 106 (2018), 35–47; published online 2017-05-05. DOI: 10.1007/s11225-017-9724-1. https://doi.org/10.1007/s11225-017-9724-1
