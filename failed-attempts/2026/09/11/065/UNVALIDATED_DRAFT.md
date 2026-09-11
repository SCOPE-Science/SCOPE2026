# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# The stated stem-70 Ctau-boundary transfer is impossible as written

## Abstract
The literal target claim — that for a class $p \in \pi_{70,w}(C\tau)$ the
composite "tau-cofiber boundary followed by Betti realization" is a nonzero
element $2\cdot x \in \pi_{70}(S^{\mathrm{cl}})$ — is false for every weight
$w$, by bigraded degree and by Betti naturality. The composite lands in
$\pi_{69}^{\mathrm{cl}}$, never $\pi_{70}^{\mathrm{cl}}$, and it is
identically zero. A stem-71 Ctau input would be needed to land in
$\pi_{70}^{\mathrm{cl}}$. This falsifies the literal conjunction; it does
not rule out a stem-70 hidden extension proved by any other route.

## 1. Theorem (TARGET disproof)
For every weight $w$ and every $p \in \pi_{70,w}(C\tau)$:
- (a) $\mathrm{Re}(d_*(p)) \in \pi_{69}(S^{\mathrm{cl}})$, so the literal
  equality $\mathrm{Re}(d_*(p)) = 2\cdot x$ with $x$ detected in
  $\pi_{70}(S^{\mathrm{cl}})$ is ill-typed across distinct groups;
- (b) $\mathrm{Re}(d_*(p)) = 0$ in $\pi_{69}(S^{\mathrm{cl}})$, so the
  "nonzero" clause is independently impossible.

Here $d_*$ is the tau-cofiber boundary and $\mathrm{Re}$ is 2-complete
Betti realization.

## 2. Cofiber sequence and named LES segment
Work 2-completely over $\mathbb{C}$. Let $\tau: S^{0,-1}\to S$ and
$C\tau = \mathrm{cof}(\tau)$. The cofiber sequence
$$S^{0,-1} \xrightarrow{\;\tau\;} S \xrightarrow{\;c\;}
  C\tau \xrightarrow{\;d\;} S^{1,-1} = \Sigma^{1,-1}S$$
induces, with $\pi_{s,w}(-) = [S^{s,w},-]$, the exact segment (all maps named)
$$\cdots \to \pi_{70,w}(S) \xrightarrow{c_*}
  \pi_{70,w}(C\tau) \xrightarrow{d_*}
  \pi_{69,w+1}(S) \xrightarrow{\tau_*}
  \pi_{70,w}(S) \to \cdots$$
because $[S^{s,w},S^{1,-1}] \cong \pi_{s-1,w+1}(S)$.
In particular $d_*: \pi_{70,w}(C\tau)\to\pi_{69,w+1}(S_{\mathrm{mot}})$:
topological stem drops by exactly one. This uses only the cofiber
identification, no charts.

## 3. Betti degrees
Betti realization $\mathrm{Re}$ sends $S^{p,q}\mapsto S^p$ and
$\mathrm{Re}_*: \pi_{s,w}(S_{\mathrm{mot}})\to\pi_s(S^{\mathrm{cl}})$:
stem preserved, weight forgotten. Hence for $s=70$ and any $w$,
$$\pi_{70,w}(C\tau) \xrightarrow{d_*} \pi_{69,w+1}(S_{\mathrm{mot}})
  \xrightarrow{\mathrm{Re}} \pi_{69}(S^{\mathrm{cl}}).$$
The composite lands in classical stem 69 for every $w$; equality with an
element of $\pi_{70}^{\mathrm{cl}}$ compares elements of distinct groups
$\pi_{69}\ne\pi_{70}$. This proves (a), weight-independently. The only
source stem that could land in classical stem 70 is $s=71$.

## 4. Vanishing via naturality
$\mathrm{Re}$ is exact symmetric monoidal and $\mathrm{Re}(\tau)=1$,
so $\mathrm{Re}(C\tau)\simeq *$. Naturality of the LES under $\mathrm{Re}$:
$$\begin{CD}
\pi_{70,w}(C\tau) @>{d^{\mathrm{mot}}}>> \pi_{69,w+1}(S_{\mathrm{mot}})\\
@V{\mathrm{Re}}VV @V{\mathrm{Re}}VV\\
\pi_{70}(\mathrm{Re}\,C\tau)=0 @>{d^{\mathrm{cl}}}>> \pi_{69}(S^{\mathrm{cl}})
\end{CD}$$
commutes, so
$\mathrm{Re}(d^{\mathrm{mot}}(p)) = d^{\mathrm{cl}}(\mathrm{Re}(p)) = d^{\mathrm{cl}}(0)=0$.
This proves (b): the composite is identically zero, contradicting
"nonzero". The two obstructions are independent: (a) is a degree mismatch,
(b) is a value mismatch.

## 5. Bounded recovery test (no reindexing saves the literal claim)
Machine check `output/artifacts/verify.py` (stdlib only, `VERIFY_OK`):
- composite stem $=69$ for all weights $w\in[-10,30)$;
- weight-independence of the classical output stem;
- source stem 71 is the unique adjacent stem landing in classical 70;
- $69\ne70$ as groups.
Reversing the order (Betti-then-boundary) does not help: $\mathrm{Re}(p)=0$
since $\mathrm{Re}(C\tau)\simeq*$, and there is no motivic-to-classical
boundary in that order. MW-stem or Adams–Novikov regradings change the
filtration bookkeeping, not the topological-stem shift of $d$.

## 6. What is and is not shown
- Shown: the target conjunction as stated (stem-70 Ctau input, boundary-then-Betti,
  nonzero element $2x$ in $\pi_{70}$) is impossible. Proof vs computation:
  Sections 2–4 are proofs from the cofiber sequence and $\mathrm{Re}$;
  Section 5 is a computed certificate of the degree arithmetic.
- Not shown: no claim about whether $\pi_{70}$ carries a hidden 2-extension by
  other means, nor about any stem-71 Ctau transfer, nor about the tabulated
  Ctau product itself. Those remain open.
- Conjecture (not claimed): the intended transfer likely mis-indexed the source
  stem by one; a stem-71 Ctau class is the natural repair candidate — stated
  only as direction, not as result.

## 7. Reproducibility
Run `python3 output/artifacts/verify.py`; expect `VERIFY_OK`.
No external charts, no network, no hidden hypotheses beyond the standard
cofiber sequence $S^{0,-1}\to S\to C\tau\to S^{1,-1}$ and
$\mathrm{Re}(\tau)=1$.
