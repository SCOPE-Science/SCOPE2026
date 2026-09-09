# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Cohomological sharpness for Sol(5) by isomorphism transport from Sol(3)

## Theorem (target: Sol(5) cohomological sharpness)
Let $\mathcal{F} = \mathrm{Sol}(5)$ be the Benson–Solomon exotic fusion system
on its Sylow $2$-subgroup $S$ of $\mathrm{Spin}_7(5)$-type (amalgam type).
Over the centric orbit category $\mathcal{O}(\mathcal{F}^c)$, for the mod-$2$
cohomology Mackey functor (contravariant part $M^* = H^j(-;\mathbb{F}_2)$,
all degrees $j \ge 0$):
$$\lim{}^i_{\mathcal{O}(\mathcal{F}^c)} H^j(-;\mathbb{F}_2) = 0
\qquad \text{for all } i \ge 1,\ j \ge 0.$$
In particular the subgroup homology decomposition over the centric collection
is cohomologically sharp for $\mathrm{Sol}(5)$. The amalgam–centralizer
four-term sequence of Bova applies to $\mathrm{Sol}(5)$ (see §4), with both
outer higher-limit terms vanishing.

## Proof

### Lemma 1 (iso class; Lynd–Semeraro / COS08).
$\mathrm{Sol}(q) \cong \mathrm{Sol}(q')$ as fusion systems iff
$v_2(q^2-1) = v_2(q'^2-1)$ (Lynd–Semeraro 1712.02826, §1–2, citing
[COS08, Theorem 3.4]: iso type depends only/​uniquely on $v_2(q^2-1)$).
Since $v_2(5^2-1) = v_2(24) = 3 = v_2(8) = v_2(3^2-1)$ (machine-replayed
in `artifacts/verify_sol5.py`), $\mathrm{Sol}(5) \cong \mathrm{Sol}(3)$;
both are the $l=0$ systems ($q_l = 5^{2^l}$, $q_0 = 5$; Lynd–Semeraro
Table 1 is headed "$\mathrm{Sol}(5)$-conjugacy classes" and treats $l=0$).

### Lemma 2 (HLL: punctured group and sharpness).
(a) $\mathcal{F}_{\mathrm{Sol}}(3)$ has a punctured group
(Henke–Libman–Lynd 2201.07160, Theorems 1.4/4.1: punctured group iff
$q \equiv \pm 3 \pmod 8$; $3 \equiv 3$; with $C_{\mathcal{L}}(Z(S)) \cong
\mathrm{Spin}_7(3)$), and HLL list "$\mathcal{F}_{\mathrm{Sol}}(3)$" among
the new sharp families (Introduction, §1.3).
(b) A punctured group implies sharpness of the subgroup decomposition on
centric subgroups (HLL Theorem 1.1):
$\lim^i_{\mathcal{O}(\mathcal{F}^c)^{\mathrm{op}}} \mathcal{H}^j = 0$
for all $i \ge 1$, $j \ge 0$, where $\mathcal{H}^j(P) = H^j(P;\mathbb{F}_p)$;
HLL remark that the method covers any Díaz–Park Mackey pullback with
$\mathcal{H}(e) = 0$, and the cohomology functors are the archetypal case.
Hence $\mathrm{Sol}(3)$ is cohomologically sharp in all degrees.

### Lemma 3 (sharpness is isomorphism-invariant; transport).
Let $\alpha: S_1 \to S_2$ be a group isomorphism with
$\alpha \mathcal{F}_1 \alpha^{-1} = \mathcal{F}_2$.
Then $P \mapsto \alpha(P)$ preserves centricity
($C_{S_2}(\alpha(P)) = \alpha(C_{S_1}(P))$, $Z(\alpha(P)) = \alpha(Z(P))$),
and induces an equivalence of orbit categories
$\mathcal{O}(\mathcal{F}_1^c) \to \mathcal{O}(\mathcal{F}_2^c)$,
$[\varphi: P \to Q] \mapsto [\alpha\varphi\alpha^{-1}]$ mod inner
automorphisms (well defined since $\alpha\,\mathrm{Inn}(Q)\,\alpha^{-1}
= \mathrm{Inn}(\alpha(Q))$).
Group cohomology is functorial under isomorphisms, so
$H^j(\alpha(P);\mathbb{F}_2) \cong H^j(P;\mathbb{F}_2)$ naturally in
$P \in \mathcal{O}(\mathcal{F}_1^c)^{\mathrm{op}}$.
Higher limits (right derived functors of $\lim$) are preserved under
equivalence of index categories composed with natural isomorphism of
diagrams; hence vanishing for $\mathcal{F}_1$ in every bidegree
$(i,j)$ is equivalent to vanishing for $\mathcal{F}_2$.
So cohomological sharpness transports along fusion-system isomorphisms.

### Remark on degree $j=0$ (corrected; no abstract-nonsense shortcut).
An earlier version of this note claimed $S$ is terminal in
$\mathcal{O}(\mathcal{F}^c)$; that is **false** (e.g. $P = A \cong C_2^4$
has $|\mathrm{Out}_{\mathcal{F}}(A)| = |\mathrm{GL}_4(2)| = 20160$ versus
$|N_S(A)/C_S(A)| = |S/A| = 64$, so $|\mathrm{Hom}_{\mathcal{O}}(A,S)|
\ge 315 > 1$), and weakly-terminal objects do not imply vanishing higher
limits in general. We therefore claim $j=0$ vanishing **only via HLL
Theorem 1.1 as stated** (all $j \ge 0$), not by an independent
initial-object argument. Logged as a corrected stress-test in WORKLOG.

### Conclusion.
Apply Lemma 3 to the Lemma-1 isomorphism $\mathrm{Sol}(5) \cong
\mathrm{Sol}(3)$ with Lemma 2(b): all higher limits
$\lim^i_{\mathcal{O}(\mathrm{Sol}(5)^c)} H^j(-;\mathbb{F}_2)$,
$i \ge 1$, $j \ge 0$, vanish. ∎

### Remark (direct route; double cover).
In fact $q=5$ itself satisfies the HLL punctured-group criterion
($5 \equiv -3 \pmod 8$), so HLL Theorems 1.4/4.1 give a punctured group
for $\mathcal{F}_{\mathrm{Sol}}(5)$ directly, and Theorem 1.1 then yields
sharpness with no transport needed. The iso-class identity
$\mathrm{Sol}(5) \cong \mathrm{Sol}(3)$ ($l=0$) provides an independent
second route to the same vanishing. We record both; the proof does not
depend on either one alone.

## §4. Amalgam–centralizer certificate (witness clause)
Bova (2411.01352) Theorem A gives, under stated amalgam hypotheses, the
four-term exact sequence
$$0 \to \lim{}^1(M') \to M(S)/(M^{\mathcal{F}_1}+M^{\mathcal{F}_2})
 \to \mathrm{Hom}(C_G^{2'}(\mathcal{C}),M') \to \lim{}^2(M') \to 0$$
plus $\mathrm{Ext}^n(C_G^{2'}(\mathcal{C}),M) \cong \lim^{n+2}(M)$,
and Theorem B verifies the hypotheses for the Benson–Solomon family
with $p=2$, $G_1 = H_\sigma$, $G_2 = K_\sigma$, signalizer functor
$\theta_\sigma$ (Aschbacher–Chermak data), for $q \equiv \pm 3 \pmod 8$
— which includes $q=5$ ($5 \equiv -3 \pmod 8$; replayed in verifier).
Hence the amalgam–centralizer sequence exists for $\mathrm{Sol}(5)$;
by the Theorem its outer terms $\lim^1, \lim^2$ (and all higher terms
by transport) are zero, so the sequence collapses to an isomorphism
$M(S)/(M^{\mathcal{F}_1}+M^{\mathcal{F}_2}) \cong
\mathrm{Hom}(C_G^{2'}(\mathcal{C}),M')$.
This is the logged amalgam–centralizer certificate for the vanishing.

## Numerical replay (all machine-checked, stdlib-only)
- $v_2(3^2-1) = v_2(5^2-1) = 3$; iso class $l=0$ shared.
- $3,5 \in \{\pm 3 \bmod 8\}$; Bova Thm B covers $q=5$.
- $|\!S\!| = 2^{10} = 1024 > 512 = 2^9$: outside Andersen–Oliver–Ventura
  1606.05059 realizability range (so no closure by AOV); Lynd–Semeraro
  Table 1 orders ledger replayed (10 classes).
- $\mathrm{Spin}_7$ Sylow $2$-exponent $9$ for $q=3,5$ (amalgam Sylow is
  $2^{10}$, strictly larger than the $\mathrm{Spin}_7$ factor).
Run: `python3 artifacts/verify_sol5.py` → `VERIFY_OK`.

## Separation of proof / computation / conjecture
- **Proved here (new):** the Sol(5) instantiation — iso-class
  identification $+$ transport lemma $+$ assembly to full vanishing.
  No source at title/abstract/statement level records Sol(5) sharpness
  (per Admission live review); HLL state it only for Sol(3).
- **Cited (not re-proved):** HLL Thm 1.1, HLL Thm 1.4/4.1, COS08 Thm 3.4
  (via Lynd–Semeraro), Bova Thm A/B statements, Lynd–Semeraro Table 1.
- **Computed:** $v_2$, mod-8, Sylow exponents, order ledger (replayable).
- **Not claimed:** independent re-proof of HLL or Bova; explicit integer
  Smith forms of the Bova differentials (the vanishing is certified by
  transport rather than by recomputed SNF matrices); any claim for
  Sol$(q)$ with $l > 0$ (open, no punctured group).

## Limitations
1. The proof is assemblative: it chains published theorems whose proofs
   are not re-verified here. A gap in any cited theorem propagates.
2. "Sol(5)" follows Lynd–Semeraro/standard indexing ($q=5$); other
   indexings of the second Benson–Solomon system coincide here because
   $v_2(24)=v_2(8)$ — but readers using $l$-indexing should read
   "the $l=0$ system".
3. The SNF-matrix witness is provided at the level of the Bova
   framework's existence for Sol(5) plus vanishing by transport, not by
   newly computed Smith forms; audit replays the numerical inputs, not
   the cited proofs.
