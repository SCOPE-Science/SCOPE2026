# Sharp quadratic-piece budgets for worst-case coordinate-reset control

## Finding

For integer dimension \(n\ge2\), piece budget \(1\le m\le n\), and retention \(0<\rho<1\), let an adversary choose at each time one of \(n\) matrices
\[
A_i=\rho e_i e_i^\top\quad (i=1,\ldots,n),
\]
with quadratic stage cost \(c(x)=\|x\|_2^2\). Define \(\beta=\rho^2/(1-\rho^2)\) and \(r=\lceil n/m\rceil\). The worst-switching infinite-horizon value is exactly
\[
J(x)=\|x\|_2^2+\beta\|x\|_\infty^2.
\]
Among every pointwise-valid max-of-\(m\)-quadratics upper bound, the best possible worst-state multiplicative overestimate is
\[
\boxed{\Gamma_{n,m}(\rho)=\frac{r(1+\beta)}{r+\beta}
=\frac{r}{r-(r-1)\rho^2}.}
\]
This optimum is attained by an explicit \(m\)-node co-complete path-complete graph certificate, not merely by unrestricted quadratic envelopes.

## Assumptions and scope

All vectors and matrices are real, all switches are allowed independently at each discrete time, and the stage cost is charged at time zero as well. The cost-to-go is the supremum over all infinite switching sequences of \(\sum_{k=0}^{\infty}\|x_k\|_2^2\), with \(x_0=x\). Since every mode has operator norm \(\rho<1\), all such series converge.

The admissible upper-bound class is
\[
\mathcal V_m=\left\{V(x)=\max_{1\le j\le m}x^\top P_jx:\ P_j=P_j^\top\succeq0,\ V(x)\ge J(x)\text{ for all }x\in\mathbb R^n\right\}.
\]
The optimization is \(\inf_{V\in\mathcal V_m}\sup_{x\ne0}V(x)/J(x)\). In particular, the infimum permits arbitrary off-diagonal entries in the quadratic matrices; it is **not** restricted to diagonal certificates. For the graph-attainability statement, an edge \((g,h,i)\) means the matrix Bellman inequality \(P_g\succeq I+A_i^\top P_hA_i\). A labeled graph is co-complete when each target node has an incoming edge of every mode label.

## Proof

**1. Exact value.** After choosing mode \(i\) at time zero, the state at time one is \(\rho x_i e_i\). Continuing with mode \(i\) yields subsequent squared costs \(\rho^{2k}x_i^2\) at times \(k\ge1\). Using any other mode at a positive time kills the state, so it cannot produce a larger nonnegative sum. Maximizing over \(i\) gives \(J(x)=\|x\|_2^2+\beta\max_i x_i^2\).

**2. Unconditional lower bound for the number of pieces.** Fix any \(V\in\mathcal V_m\). At each coordinate unit vector \(e_i\), validity gives \(\max_j e_i^\top P_je_i\ge1+\beta\). Assign every coordinate \(i\) to one quadratic form attaining this lower bound. By the pigeonhole principle some piece, say \(j_*\), is assigned at least \(r\) different coordinates. Choose exactly \(r\) of them, comprising a set \(S\). For each sign vector \(\epsilon\in\{-1,+1\}^{S}\), define \(x^{(\epsilon)}_i=\epsilon_i/\sqrt r\) on \(S\) and zero elsewhere. Every such vector has \(\|x^{(\epsilon)}\|_2^2=1\), \(\|x^{(\epsilon)}\|_\infty^2=1/r\), hence \(J(x^{(\epsilon)})=1+\beta/r\). Averaging its quadratic form over all \(2^r\) signs cancels off-diagonal entries exactly:
\[
2^{-r}\sum_{\epsilon}(x^{(\epsilon)})^\top P_{j_*}x^{(\epsilon)}
=\frac1r\sum_{i\in S}(P_{j_*})_{ii}\ge1+\beta.
\]
At least one sign vector therefore has \(V(x^{(\epsilon)})\ge1+\beta\). This proves
\[
\sup_{x\ne0}\frac{V(x)}{J(x)}\ge\frac{1+\beta}{1+\beta/r}.
\]
The argument holds for arbitrary symmetric matrices, including off-diagonal ones, and hence for all allowed positive-semidefinite forms.

**3. Matching construction and global upper bound.** Partition the \(n\) coordinates into \(m\) nonempty blocks \(G_1,\ldots,G_m\), each of cardinality at most \(r\), with at least one block of cardinality exactly \(r\). Put \(D_g=\operatorname{diag}(\mathbf1_{i\in G_g})\) and \(P_g=I+\beta D_g\). Define
\[
V(x)=\|x\|_2^2+\beta\max_g\sum_{i\in G_g}x_i^2.
\]
Each coordinate lies in one block, so \(V\ge J\). For \(x\ne0\), write \(S=\|x\|_2^2\), \(t=\max_i x_i^2/S\), and \(s=\max_g\sum_{i\in G_g}x_i^2/S\). Then \(s\le\min\{1,rt\}\), and
\[
\frac{V(x)}{J(x)}=\frac{1+\beta s}{1+\beta t}
\le\frac{1+\beta\min\{1,rt\}}{1+\beta t}
\le\frac{1+\beta}{1+\beta/r}.
\]
The last expression increases up to \(t=1/r\) and decreases afterward; for \(r=1\) it is identically at most one. Equality is attained by any nonzero vector having equal-magnitude entries on a largest block and zeros outside. This matches the unconditional lower bound.

**4. Explicit co-complete graph.** For every mode \(i\), let \(g(i)\) be its unique block. Place an edge \((g(i),h,i)\) for every target node \(h\in\{1,\ldots,m\}\). Every target has an incoming edge of every label, so the graph is co-complete. For these edges,
\[
A_i^\top P_hA_i=\rho^2\bigl(1+\beta\mathbf1_{i\in G_h}\bigr)e_ie_i^\top.
\]
On coordinate \(i\), the left surplus \(P_{g(i)}-I\) is \(\beta\), while the right term is at most \(\rho^2(1+\beta)=\beta\). On every other coordinate the right term vanishes and the left is nonnegative. Thus \(P_{g(i)}\succeq I+A_i^\top P_hA_i\) for every edge. The graph-based max certificate exactly attains the global optimum.

If \(m=n\), then \(r=1\) and \(V=J\). If \(m<n\), then \(r\ge2\), so \(\Gamma_{n,m}(\rho)>1\) for every \(\rho>0\): no smaller max-of-quadratics family represents \(J\) exactly. Finally, \(\Gamma_{n,m}(\rho)\to r\) as \(\rho\uparrow1\).

## Verification

Run `python3 verify.py` with Python's standard library. The checker uses exact rational arithmetic to test the complete diagonal Bellman inequalities, the claimed optimum, explicit maximizing states, and exhaustive small rational vector probes. It also enumerates coordinate assignments in small dimensions and checks exact Rademacher sign cancellation for a genuinely off-diagonal symmetric form. The checker completed: `PASS: 132 rational graph-and-witness cases; 71991 exhaustive finite assignments; one exact sign-average check`. All-dimensional claims follow from the preceding proof, not from finite enumeration.

## Relationship to prior work

Ninite, Banse, Berger and Jungers (2026, arXiv:2602.04310) introduce path-complete quadratic Bellman certificates for worst-case autonomous switching, including co-complete max constructions, matrix inequalities, and general approximation guarantees. The graph vocabulary, basic upper-bound mechanism, and need for complexity-versus-conservatism analysis are theirs. The present theorem determines a *sharp exact finite piece-budget frontier* for a specified coordinate-reset system, shows that no off-diagonal quadratic pieces can improve it, and gives a matching explicit graph, rather than re-proving their general certificate theorem. Their 2026 controlled extension arXiv:2607.15055 considers policy synthesis and min-max graph certificates, not this autonomous sharp coordinate-reset frontier. Ahmadi and Jungers (2015, arXiv:1504.03761) establish broad complexity obstructions for stability Lyapunov functions; those are neither the same relative-error objective nor this exact formula for a fixed stable family.

## Limitations

The matrices are rank-one coordinate-retention maps; the result does not extend automatically to arbitrary noncommuting dynamics, input design, general state costs, max-min graph combinations, or pointwise absolute additive error. It optimizes worst-case relative *value overestimation* for all nonzero initial states, not the trace of SDP matrices or solver runtime. The example is deliberately a fully solvable benchmark; a practical performance advantage from choosing particular graphs is not demonstrated. Novelty is based on the inspected accessible literature and is not an independent exhaustive priority certificate.

## References

1. L. Ninite, A. Banse, G. O. Berger, R. M. Jungers, *A Path-Complete Approach for Optimal Control of Switched Systems*, arXiv:2602.04310, first posted 2026-02-04. https://arxiv.org/abs/2602.04310
2. L. Ninite, A. Banse, G. O. Berger, R. M. Jungers, *Robust Optimal Control of Arbitrarily Switched Systems: A Path-Complete Framework*, arXiv:2607.15055, first posted 2026-07-16. https://arxiv.org/abs/2607.15055
3. A. A. Ahmadi, R. M. Jungers, *Lower Bounds on Complexity of Lyapunov Functions for Switched Linear Systems*, arXiv:1504.03761, first posted 2015-04-15. https://arxiv.org/abs/1504.03761
