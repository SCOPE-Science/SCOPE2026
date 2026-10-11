# A full weak-limit ball for the diagonal WMP witness on \(X_c\)
## Finding
Fix \(0<c<1\) and write \(\delta_c=\sqrt{1-c^2}\). Let \(X_c\) be the reflexive sequence space of García--Maestre--Pinasco--Zalduendo, with canonical basis \((e_n)_{n\geq0}\), and let \(D_c\) be their diagonal operator satisfying \(D_c e_0=0\) and \(D_c e_n=\frac{n}{n+1}e_n\) for \(n\geq1\). For a fixed \(x\in X_c\), discard at most one index for which \(x+e_n=0\), and define
\[
u_n(x)=\frac{x+e_n}{\|x+e_n\|}.
\]
Then \((u_n(x))\) is a maximizing sequence for \(D_c\) if and only if
\[
\|x\|\leq\delta_c.
\]
Whenever this holds,
\[
u_n(x)\rightharpoonup x.
\]
Hence every point of the closed ball \(\delta_c B_{X_c}\) is the weak limit of an explicit maximizing sequence for the same non-norm-attaining operator \(D_c\).

## Assumptions and scope
The construction and notation are those of arXiv:2609.23198v1. The space \(X_c\) has property \((M)\), its canonical basis is shrinking, and therefore \(e_n\rightharpoonup0\). Its recursively defining two-dimensional norm is
\[
N_{n,c}(s,t)=\left((1-c^{2n})|t|^{2n}+(s^2+c^2t^2)^n\right)^{1/(2n)}.
\]
The operator \(D_c\) has norm one and satisfies \(\|D_cx\|<\|x\|\) for every nonzero \(x\), so it does not attain its norm.

The exact threshold proved here is for the canonical one-spike family \(u_n(x)\). The finding does not assert that \(\delta_c B_{X_c}\) is the complete set of weak limits of all maximizing sequences for \(D_c\).

## Proof
For \(a\geq0\), define
\[
L_c(a)=\max\{1,\sqrt{a^2+c^2}\}.
\]
We first prove that every fixed \(x\in X_c\) satisfies
\[
\lim_{n\to\infty}\|x+e_n\|=L_c(\|x\|).
\]
Let \(a=\|x\|\). Property \((M)\), applied to \(x\) and \(a e_0\), gives equality of the corresponding limsups after addition of the weakly null sequence \((e_n)\). The recursion is stationary through the zero coordinates between positions zero and \(n\), so
\[
\|a e_0+e_n\|
 =\left((1-c^{2n})+(a^2+c^2)^n\right)^{1/(2n)}
 \longrightarrow L_c(a).
\]
This initially determines the limsup. It determines the full limit as well: the same property-\((M)\) argument applies to every subsequence \((e_{n_k})\), while the displayed explicit expression has the same limit along every subsequence. A subsequence realizing a smaller liminf would therefore contradict the corresponding subsequential limsup identity.

Put \(b=\|D_cx\|\) and \(d_n=n/(n+1)\). Since \(\|e_n\|=1\),
\[
\big|\|D_cx+d_ne_n\|-\|D_cx+e_n\|\big|\leq1-d_n\longrightarrow0.
\]
Applying the first limit formula to \(D_cx\) yields
\[
\lim_{n\to\infty}\|D_c(x+e_n)\|=L_c(b).
\]
Consequently
\[
\lim_{n\to\infty}\|D_cu_n(x)\|=\frac{L_c(b)}{L_c(a)}.
\]

If \(a\leq\delta_c\), then \(a^2+c^2\leq1\), while \(b\leq a\) because \(D_c\) is a contraction. Hence \(L_c(a)=L_c(b)=1\), so \((u_n(x))\) is maximizing for the norm-one operator \(D_c\). Moreover \(\|x+e_n\|\to1\) and \(e_n\rightharpoonup0\), which gives \(u_n(x)\rightharpoonup x\).

Conversely, suppose \(a>\delta_c\). Then \(x\neq0\), and Proposition 4.1 of the source gives \(b<a\). Now \(L_c(a)=\sqrt{a^2+c^2}>1\). If \(b\leq\delta_c\), then \(L_c(b)=1<L_c(a)\). If \(b>\delta_c\), then
\[
L_c(b)=\sqrt{b^2+c^2}<\sqrt{a^2+c^2}=L_c(a).
\]
Thus in either case \(L_c(b)/L_c(a)<1\), so \((u_n(x))\) is not maximizing. This proves the threshold and the closed-ball inclusion.

## Verification
The proof uses four source facts that were checked in the full arXiv text: \(X_c\) has property \((M)\); the canonical basis is shrinking and hence \(e_n\rightharpoonup0\); the displayed formula for \(N_{n,c}\); and Proposition 4.1, which gives strict norm decrease under \(D_c\) on every nonzero vector. The source's Lemma 3.5 is recovered at the boundary point \(x=\delta_c e_0\), where the source's special maximizing sequence is exactly this construction.

The only limiting step not stated verbatim in the source is the arbitrary-center formula for \(\|x+e_n\|\). Its limsup follows directly from property \((M)\), and the passage from limsup to limit is justified by applying the same argument to every subsequence. No finite computation is used as a substitute for this argument.

## Relationship to prior work
García--Maestre--Pinasco--Zalduendo construct \(X_c\), prove property \((M)\), define \(D_c\), prove that \(D_c\) does not attain its norm, and exhibit one non-weakly-null maximizing sequence converging weakly to \(\delta_c e_0\). The present finding shows that the same single operator has explicit maximizing sequences converging weakly to every point of the entire infinite-dimensional closed ball \(\delta_c B_{X_c}\), and identifies the exact radius for the natural one-spike family.

Earlier work on the weak maximizing property supplies general sufficient conditions and permanence or failure mechanisms, but the inspected sources do not give this arbitrary-center weak-limit ball or the exact threshold for these \(X_c\) spaces. Claim-level searches for weak limits of maximizing sequences, the parameter \(\sqrt{1-c^2}\), and this diagonal witness found no covering statement.

## Limitations
The result is tied to the concrete family \(X_c\) and the concrete diagonal operator \(D_c\). It classifies only the sequences obtained by adding one canonical basis spike to a fixed center and normalizing. It does not classify all maximizing sequences of \(D_c\), and it does not prove that the complete weak-limit set equals \(\delta_c B_{X_c}\). Because the focal preprint is recent and the argument from property \((M)\) is short, an equivalent unindexed observation remains a residual originality risk.

## References
1. D. García, M. Maestre, D. Pinasco, I. Zalduendo, *The weak maximizing property, compact perturbations and duality*, arXiv:2609.23198v1, 2026.
2. M. Han, S. K. Kim, *M-ideals of compact operators and Norm attaining operators*, arXiv:2402.12070, 2024.
3. S. Dantas, M. Jung, G. Martínez-Cervantes, *Some remarks on the weak maximizing property*, arXiv:2103.10288, 2021.
