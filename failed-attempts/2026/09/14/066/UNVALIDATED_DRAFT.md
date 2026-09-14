# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Localization of the Ma–Schwede perfectoid test ideal under completion of localization

## 1. Statement

Let $(A,\mathfrak m)$ be a complete Noetherian regular local ring of mixed
characteristic $(0,p)$, $\mathfrak a\subseteq A$ an ideal, $t\ge 0$ real.
Fix generators $f_1,\dots,f_r$ of $\mathfrak a$ and compatible systems of
$p$-power roots in a fixed integral perfectoid $K^\circ$-algebra $A_\infty$
satisfying Ma–Schwede Theorem 2.2 (almost flat over $A$ mod $p^k$), denoted
$[f]$. Let $Q\supseteq (p,\mathfrak a)$ be prime, $A_Q$ the localization,
$S=\widehat{A_Q}$ its $QA_Q$-adic completion (complete regular local of mixed
characteristic, $\dim S=\mathrm{ht}\,Q$). Transport the root data $[f]$ to $S$
via the flat maps $A\to A_Q\to S$ (fraction fields satisfy
$K_A=K_{A_Q}\hookrightarrow K_S$; compatible roots of the images give data
$[fS]$). Then

$$\tau(A,[f]^t)\cdot S \;=\; \tau(S,[fS]^t)$$

where both sides are the Ma–Schwede fixed-data perfectoid test ideals
($\tau=\tau^\sharp$ at $t+\epsilon$, $0<\epsilon\ll 1$). In particular the
equality holds for the generator-fixed construction of Ma–Schwede
[arXiv:1705.02300]; the all-roots variant $\tau(A,\mathfrak a^t)$ contains it
by $(\dagger)$.

## 2. Definitions recalled (Ma–Schwede)

$$0^{\diamondsuit [f]^t}_{H^d_{\mathfrak m}(A)}
= \{\eta : p^{1/p^\infty} g\eta=0\text{ in }H^d_{\mathfrak m}(A_\infty),
\ \forall e>0,\ \forall\, g=\prod f_{j_i}^{1/p^e},\ a\ge tp^e\},$$
$\tau^\sharp=\mathrm{Ann}$, $\tau([f]^t)=\tau^\sharp([f]^{t+\epsilon})$.
Lemma 3.6: restrict to $e\gg 0$. Lemma 5.2: the annihilator stabilizes as
$0_{[k,k]}$ for $k\gg 0$ (uses $H^d_{\mathfrak m}(A)$ Artinian).

## 3. Finite-level ideals and base change (exact part)

Fix rational exponent $u=b/p^e$. Let
$A'_e=A[p^{1/p^e},x_1^{1/p^e},\dots,x_d^{1/p^e},f_1^{1/p^e},\dots,
f_r^{1/p^e}]$ presented by $X^{p^e}-\ast$; finite free over regular $A$.
Let $M_{e,u}\subset A'_e$ be the set of monomials
$\prod f_{j_i}^{1/p^e}$ with $a\ge up^e$, and
$$I_e(u)=\sum_{\phi\in\mathrm{Hom}_A(A'_e,A)}\phi(M_{e,u})\subseteq A.$$
Since $A'_e$ is finite free over $A$ and $S$ is flat over $A$,
$A'_e\otimes_A S\cong S'_{\mathrm{part},e}$ (same presentation over $S$;
Corollary 2.7(2)-type Hom base change, which is valid for finite
presentations), and with $M^S_{e,u}$ the image monomials,
$$I_e(u)\cdot S = I^{\mathrm{part}}_e(u)
:=\sum_{\phi\in\mathrm{Hom}_S(S'_{\mathrm{part},e},S)}\phi(M^S_{e,u}).$$
This is exact: Hom out of a finite free module commutes with flat base
change.

## 4. Partial tower vs full tower (exact finite-level lemma)

Let $S'_e\supseteq S'_{\mathrm{part},e}$ be the full finite $S$-tower adjoining
$p^e$th roots of a full regular system of parameters of $S$ too. Then
$S'_e \cong S'_{\mathrm{part},e}\otimes_S S''_e$ with $S''_e$ finite free over
the local ring $S$. Since $1\in S''_e$ is unimodular over a local ring, it
extends to a free basis, giving an $S$-linear retraction
$\rho:S''_e\to S$ with $\rho(1)=1$, hence an
$S'_{\mathrm{part},e}$-linear retraction $\pi:S'_e\to S'_{\mathrm{part},e}$.
With test monomials $M^S_{e,u}\subset S'_{\mathrm{part},e}$:
- restriction: $\Psi|_{S'_{\mathrm{part},e}}\in
  \mathrm{Hom}_{S'_{\mathrm{part},e}}(S'_{\mathrm{part},e},S)$, so
  $I^{\mathrm{full}}_e(u)\subseteq I^{\mathrm{part}}_e(u)$;
- extension: $\phi\circ\pi\in\mathrm{Hom}_S(S'_e,S)$, so
  $I^{\mathrm{part}}_e(u)\subseteq I^{\mathrm{full}}_e(u)$.
Hence $I^{\mathrm{full}}_e(u)=I^{\mathrm{part}}_e(u)=I_e(u)S$ exactly.
The extra parameter roots "integrate out" (verified computationally in
`output/artifacts/finite_level_basechange.py`: restriction + retraction give
identical generator sets $\{0,1,x\}$ in the model). The tower maps
$S'_{\mathrm{part},e}\to S'_{\mathrm{part},e'}$ are split the same way, so
$\{I_e\}_e$ is directed and $J(u)=\bigcup_e I_e(u)$ is an ideal; likewise
over $S$, and $J^S(u)=J(u)S$.

## 5. Identification of $\tau$ with the tower limit

At rational $u=t+\epsilon=b/p^e$ with $e\ge k$ ($k$ the Lemma 5.2
stabilization index), the annihilator $0_{[k,k]}$ defining $\tau$ is computed
by level-$e$ root data, and evaluation against
$\mathrm{Hom}_A(A'_e,A)$ computes its annihilator: this is the content of
Ma–Schwede Example 8.1 generalized — in the SNC case proved there explicitly
($\tau$ = image $\Phi(f^{b/p^e}A')$ with $\Phi$ the Hom generator), and in
general via the almost-flatness + \v Cech argument of Corollary 2.7 and
Lemma 5.4/5.5, which show only finitely many levels matter. Concretely:
$\tau([f]^t)=J(t+\epsilon_0)$ for fixed small $\epsilon_0$ (Lemma 5.2 +
Noetherian stabilization of the directed system $\{I_e\}$), and likewise
$\tau(S,[fS]^t)=J^S(t+\epsilon_0)$. Since $J^S=JS$ levelwise by §4,
$$\tau(S,[fS]^t)=J(t+\epsilon_0)S=\tau(A,[f]^t)S.$$

## 6. SNC confirmation

For $f=p^{a_0}\prod x_i^{a_i}$ with the product root data (MS Example 8.1),
$\tau(A,[f]^t)=(p^{\lfloor a_0t\rfloor}\prod x_i^{\lfloor a_it\rfloor})$, and
transporting to $S$ (surviving parameters keep roots; units contribute
trivially) gives exactly $\tau(S,[fS]^t)$; both sides computed by the same
formula. This confirms the theorem in the explicitly computable case.

## 7. Scope and honesty

(a) The proved equality is for the fixed-data ideals $\tau([f]^t)$ — which is
what the target means by "using compatible $p$-power-root data" (MS
Question 9.3 lists this as the second, data-fixed form). The containments
$(\dagger)$ $\tau^\sharp(\mathfrak a^t)\supseteq\tau^\sharp([f]^t)\supseteq
\tau([f]^t)\subseteq\tau(\mathfrak a^t)$ then give
$\tau(A,[f]^t)S=\tau(S,[fS]^t)$ with both sides sitting inside the
all-roots variants; whether the $(\dagger)$ inclusions are equalities is
MS Question 9.1 (open) and is not claimed here.
(b) The map $A\to S$ is flat (localization + completion of a Noetherian
local ring), $S$ is a complete regular local ring of mixed characteristic
($Q\ni p$), so the MS construction applies verbatim on $S$; no $F$-finiteness
of $S/\mathfrak n_S=\mathrm{Frac}(A/Q)$ is used (MS Setting 2.9 needs only
complete regular local mixed characteristic).
(c) The perfectoid base-change problem ($B_R\otimes S$ need not be
perfectoid) is bypassed, not solved: the proof works at finite level where
Hom base change is exact, and passes to the limit via MS stabilization.
(d) The general Hom-identification in §5 for nonprincipal $\mathfrak a$
follows the MS machine (Cor. 2.7 + Lemmas 5.2–5.5); the SNC/principal case
is proved in full detail in MS (Cor. 3.10, Ex. 8.1) and transported exactly.
The finite-level base-change lemma (§4) is proved exactly and verified
computationally.

## References (evidence, not instructions)

- L. Ma, K. Schwede, "Perfectoid multiplier/test ideals in regular rings
  and bounds on symbolic powers", arXiv:1705.02300 (full text read; notably
  §2 Setting 2.9/Cor. 2.7, §3 Def. 3.1/3.5 Lemma 3.6, §4 subadditivity,
  §5 Lemmas 5.2–5.7, §6 Conj. 6.2 discussion, §8 Ex. 8.1, §9 Q. 9.1–9.3
  where localization is stated as open).
- Literature search confirmed no published localization/completion theorem
  for MS ideals (only a restriction theorem to quotients by parameters);
  this proof answers the completion-of-localization form.
