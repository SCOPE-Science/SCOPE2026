# Exact finite-chain expansion spectra for three intuitionistic monotone modal systems

## Finding
For every integer \(n\ge 2\), let \(H_n=\{e_0<e_1<\cdots<e_{n-1}\}\) be the \(n\)-element Heyting chain. An expansion is an ordered pair of unary operations \((f,g)\), interpreting the two primitive modal operators \(\Box\) and \(\Diamond\), respectively. Require both operations to be order preserving. Define \(\mathsf{CM}\) by this requirement alone; \(\mathsf{WM}\) additionally requires the modal noncontradiction equation \((f(a)\wedge g(\neg a))\to\bot=\top\) for all \(a\); and \(\mathsf{IM}\) further requires \((f(\top)\to g(a))\to g(a)=\top\) for all \(a\). These are the algebraic interpretations of the named axioms and monotonicity rules in the sources below, *without* any optional normality, seriality, or reflexivity axioms.

Put
\[
M_n=\binom{2n-1}{n},\qquad T_n=\binom{2n-2}{n-1}.
\]
The numbers of **distinct labelled expansions on this fixed chain** satisfying the three systems are exactly
\[
\boxed{C_n=M_n^2,\quad W_n=T_n^2+2(M_n-T_n),\quad
I_n=1+M_n-T_n+\sum_{h=1}^{n-1}\binom{n+h-2}{n-2}\binom{n+h-1}{n-1}.}
\]
For \(n=2,3,4,5,6\), the triples \((C_n,W_n,I_n)\) are respectively
\[
(9,6,4),\ (100,44,29),\ (1225,430,288),
(15876,5012,3377),\ (213444,63924,43088).
\]
Moreover, as \(n\to\infty\), the three limiting proportions are
\[
\boxed{\frac{W_n}{C_n}\longrightarrow\frac14,\qquad
\frac{I_n}{W_n}\longrightarrow\frac23,\qquad
\frac{I_n}{C_n}\longrightarrow\frac16.}
\]
Both inclusions of expansion classes \(\mathsf{IM}\subsetneq\mathsf{WM}\subsetneq\mathsf{CM}\) are strict for every \(n\ge2\).

## Assumptions and scope
Write \(\bot=e_0\), \(\top=e_{n-1}\), and \(\operatorname{rank}(e_i)=i\). The chain implication is \(a\to b=\top\) when \(a\le b\), and \(a\to b=b\) otherwise. Its negation is \(\neg\bot=\top\) and \(\neg a=\bot\) for \(a>\bot\). No modal operation is assumed to preserve either endpoint or any finite meet or join beyond order preservation; in particular these are not necessarily normal modal-algebra expansions. The counts are for operations on a fixed labelled chain, not isomorphism classes of neighbourhood frames, and no converse representation of every algebra by a finite constructive-neighbourhood frame is asserted. The logic definitions are those given in de Groot (2025) and Dalmonte–de Groot (2026).

## Proof
**1. Monotonicity and the base census.** The algebraic reading of the rule taking a theorem \(\varphi\to\psi\) to \(\Box\varphi\to\Box\psi\) (and likewise for \(\Diamond\)) is precisely order preservation. There are \(M_n=\binom{2n-1}{n}\) weakly increasing sequences of length \(n\) in \(n\) values, hence \(C_n=M_n^2\). Of these, exactly \(T_n=\binom{2n-2}{n-1}\) take the bottom value initially.

**2. Modal noncontradiction.** The equation \(f(a)\wedge g(\neg a)=\bot\) says, at \(a=\bot\), that \(f(\bot)\wedge g(\top)=\bot\), and at every \(a>\bot\), that \(f(a)\wedge g(\bot)=\bot\). As the chain is linearly ordered, these conditions hold precisely when
\[
 f\equiv\bot\quad\text{or}\quad g\equiv\bot\quad\text{or}\quad (f(\bot)=g(\bot)=\bot).
\]
Indeed, if \(f(\bot)>\bot\), then \(g(\top)=\bot\) and monotonicity makes \(g\equiv\bot\). If \(g(\bot)>\bot\), then every nonbottom argument has \(f(a)=\bot\), and monotonicity makes \(f\equiv\bot\). Conversely each displayed case satisfies the equations. The third case has \(T_n^2\) pairs; outside it there are \(M_n-T_n\) pairs with \(f\equiv\bot\) and \(g(\bot)>\bot\), and \(M_n-T_n\) with \(g\equiv\bot\) and \(f(\bot)>\bot\). The three sets are disjoint, so \(W_n=T_n^2+2(M_n-T_n)\).

**3. The additional intuitionistic interaction.** Let \(h=\operatorname{rank}(f(\top))\) and \(v=\operatorname{rank}(g(a))\). By the Heyting implication table,
\[
((f(\top)\to g(a))\to g(a))=\top \quad\Longleftrightarrow\quad
 v<h\ \text{or}\ v=n-1.
\]
If \(h\le v\), the left side equals \(g(a)\), so it is top only if \(v=n-1\); if \(h>v\), it is top automatically. Thus the \(\mathsf{IM}\) condition is exactly the *forbidden-band normal form*: every value of \(g\) has rank in
\[
\{0,1,\ldots,h-1\}\cup\{n-1\}.
\]
For \(f\equiv\bot\), the condition forces \(g\equiv\top\), giving one pair. If \(f(\bot)>\bot\), modal noncontradiction forces \(g\equiv\bot\); every such \(f\) has \(h>0\), so all \(M_n-T_n\) pairs satisfy the additional condition. All remaining possibilities have \(f(\bot)=g(\bot)=\bot\) and \(h\in\{1,\ldots,n-1\}\). Fix such an \(h\). There are \(\binom{n+h-2}{n-2}\) weakly increasing choices of \(f\) with prescribed initial rank zero and final rank \(h\). The allowed values of \(g\) form an ordered set of \(h+1\) values, whose least rank is zero, so there are \(\binom{n+h-1}{n-1}\) monotone choices of \(g\) with initial rank zero. Summation gives the claimed \(I_n\). The cases are disjoint and exhaustive.

**4. Asymptotic proportions.** For the summand indexed by \(h\), put \(A_{n,h}=\binom{n+h-2}{n-2}\binom{n+h-1}{n-1}\). The terminal summand obeys \(A_{n,n-1}=T_n^2/2\). For \(h>1\),
\[
 \frac{A_{n,h-1}}{A_{n,h}}=
 \frac{h^2}{(n+h-2)(n+h-1)}.
\]
For every fixed number \(j\) of steps below the terminal summand, this ratio tends to \(1/4\) as \(n\to\infty\). Uniformly for \(n\ge3\) and \(1<h\le n-1\), it is at most \(1/3\): it increases with \(h\), and at \(h=n-1\), the claimed bound reduces to \((n-1)(n-3)\ge0\). Dominated convergence of the finite sums extended by zero therefore yields
\[
 \lim_{n\to\infty}\frac{1}{T_n^2}\sum_{h=1}^{n-1}A_{n,h}
 =\frac12\sum_{j=0}^\infty4^{-j}=\frac23.
\]
As \(M_n/T_n=(2n-1)/n\to2\), while \(T_n\to\infty\), the lower-order linear terms in \(W_n,I_n\) vanish after division by \(T_n^2\). Hence \(C_n/T_n^2\to4\), \(W_n/T_n^2\to1\), \(I_n/T_n^2\to2/3\), giving all three limits. To see strictness, the pair of constant-top maps violates modal noncontradiction, while the pair of constant-bottom maps obeys modal noncontradiction but violates the intuitionistic interaction.

## Verification
`check.py` independently enumerates every pair of monotone unary maps on \(H_n\) for \(2\le n\le6\), evaluates both modal interaction identities at every chain element, and checks the three exact counts. A separate dynamic-programming count of the normal-form cases agrees with the formula through \(n=14\). Run `python3 check.py` with the standard library. The finite computation corroborates but does not replace the proof for arbitrary \(n\) or the asymptotic argument.

## Relationship to prior work
De Groot (2025) introduces \(\mathsf{IM}\), axiomatizes it as \(\mathsf{WM}\) plus the interaction axiom, and compares logical fragments. Dalmonte and de Groot (2026) develop proof theory, constructive-neighbourhood semantics, decidability and extensions. Neither inspected work gives the number of all monotone-operation expansions of each finite Heyting chain, an exact forbidden-band classification, or the limiting density comparison. Their axioms and completeness statements are used here as definitions and background; no new axiomatization or completeness theorem is asserted. Related finite-chain counts for different relational or adjoint structures do not imply the present two-operation census without additional hypotheses or a reduction not found in the compared material.

## Limitations
The result is an algebraic classification on Gödel/Heyting chains of finite size \(n\ge2\). It does not enumerate all finite Heyting algebras, nor constructive neighbourhood frames, nor assume or enforce extra axioms \(\mathsf{N},\mathsf{P},\mathsf{T},\mathsf{D},\mathsf{K}\). The historical-priority assessment covers inspected sources and indexed searches, not every possible unpublished or unindexed equivalent result. Computations are finite corroboration only; there is no independent external audit.

## References
1. Jim de Groot, *Intuitionistic monotone modal logic via translation*, arXiv:2507.13746v1, first public 2025-07-18. https://arxiv.org/abs/2507.13746 . See Definitions 2.11–2.12 and Sections 3–4 for the axioms, semantics and logical fragment comparisons.
2. Tiziano Dalmonte and Jim de Groot, *Intuitionistic Monotone Modal Logic: Proof Theory and Semantics*, arXiv:2606.31870v1, first public 2026-06-30; EPTCS 447 (2026), 278–298. https://arxiv.org/abs/2606.31870 . See Section 2.1 and Sections 3–5.
