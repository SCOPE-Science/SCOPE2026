# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — One Stein-cork twist exoticity decision via SW adjunction with logged Kirby slides (lane-522)

## Abstract
We decide one named closed simply connected cork-twist pair.
Seed: $S^2\times D^2$ (one $0$-framed $2$-handle $K_0$, no $1$-handles).
Cork: Yasui–Akbulut member $(W_2,f_2)$ (dotted $1$-handle $+$ $0$-framed $2$-handle
with $2$-twist clasp; Fig.1 of arXiv:1102.3049 at $n=2$), $\tau=f_2$ the dot–zero swap.
Frozen $W$-modification coefficients $(p_1,p_2)=(3,6)$ on disjoint arcs of $K_0$
(built from the $(W_2,f_2)$ symmetric-link local model; Def 4.1 generalized $+$ Remark 5.19(2)).
$S^+=X^{(2)}_2$ = Stein side ($W^-(3)+W^+(6)$), $S^-$ = its cork twist along the
distinguished $(C_2,f_2)$-copy at the $p_2$ site.
Closed pair: $X_2=S^+\cup_Y C_{\rm cap}$, $X'_2=S^-\cup_Y C_{\rm cap}$ with one fixed
symplectic $b_2^+>1$ minimal cap (Lisca–Matić/Akbulut–Ozbagci).
Distinguished class $\alpha=[K_0-6\gamma_2]$, $Q(\alpha)=0$, genus-$6$ representative
on the $X_2$ side; same lattice coordinates on the $X'_2$ side with an embedded
sphere ($g'=0$) representative $S'$.
SW package (cited): $X_2$ closed minimal symplectic $b_2^+>1$ has $SW\ne0$ (Taubes),
hence contains no square-$0$ sphere (closed adjunction); $X'_2$ does contain one.
Exact lines: $X_2$: $2g-2=10\ge 10+0$ HOLDS (equality);
$X'_2$: $2g'-2=-2\ge 10$ FAILS (margin $-12$); transfer $T=[1]$.
Verdict: $X_2,X'_2$ homeomorphic but not diffeomorphic (either orientation).
Checker replays all integers via `output/artifacts/verify_target.py` (VERIFY_OK, 17/17)
from the frozen diagram $+$ `slide_log.json$ without re-proving gauge theory.

## 1. Frozen objects
- **Seed** $X({\rm seed})=S^2\times D^2$: one $0$-handle $+$ one $2$-handle $K_0$
  (unknot, Seifert framing $m_0=0$), no $1$-handles. Hence $b_2=1$, $k=b_2-1=0$, $l=0$
  (Step 2 vacuous). Legendrian: $tb(K_0)=t_0=-1$, $r(K_0)=r_0=0$; $K_0$ bounds a disk
  in $B^4$, $g_0=0$.
- **Cork** $(W_2,\tau=f_2)$: Definition 2.3 of Akbulut–Yasui at $n=2$ —
  one dotted circle $D$ $+$ one $0$-framed $2$-handle $K$ with $2$-twist clasp box
  (Fig.1). $\tau$ = exchange dot and $0$ (dot–zero swap); extends to a
  self-homeomorphism (contractible $+$ Freedman), not to any self-diffeomorphism
  (cork Theorem 2.4). All $W^\pm(p)$ local modifications use the $(W_2,f_2)$
  symmetric-link model (the paper's Def 4.1 states the construction for any cork
  from a symmetric link; Remark 5.19(2) confirms $W_n$ corks work; Props 4.2/4.3/4.5
  and Lemmas 5.13/5.14 transfer verbatim — the Gluck Lemma-4.4 step is local).
- **Parameters** $p_{-1}=p_0=0$, $p_1=3$, $p_2=6$, $q_0=0$. Definition 5.6 checks:
  (i) $6>3>0$; (ii) $3+(t_0-1)-m_0=3-2=1\ge0$;
  (iii) $2\cdot3-2+0=4>2(0+0)-2=-2$; (iv) $i=1$: $4>-2$; $i=2$: $2\cdot6-2=10>2(0+3)-2=4$.
- **Compact models** ($n=2$ of §5): $X^{(2)}_0$ = seed $+W^-_{W_2}(3)+W^-_{W_2}(6)$ on $K_0$;
  $S^+=X^{(2)}_2$ = same with $W^-(6)\to W^+(6)$ at arc $A_2$ (auxiliary $0$-framed
  $\gamma_2$); $S^-$ = cork twist of $S^+$ along the $(C_2,f_2)$-copy created by
  $W^+(6)$ (Prop 4.5, Thm 5.16(6)). $X^{(2)}_1$ (the $p_1$ twist) is built but only the
  pair $(S^+,S^-)$ is closed for the headline.
- **Closure**: $X_2=S^+\cup_Y C_{\rm cap}$, $X'_2=S^-\cup_Y C_{\rm cap}$,
  $Y=\partial S^+=\partial S^-$ (same oriented $3$-manifold; $H_*(Y)$ preserved by
  Props 4.2/4.5), $C_{\rm cap}$ one fixed symplectic cap closing to simply connected
  minimal symplectic $b_2^+>1$ (Thm 3.6). Twist supported in $S$ (Prop 4.5).
  "E(1)-type" = elliptic-nucleus (square-$0$ fiber neighborhood) region housing the
  Stein piece; the closure is stabilized to $b_2^+>1$ so SW has no chamber
  (this respects the SCOPE095 lesson: no naive $SW=0$ plumbing cap is used).
  $H_2(S)\to H_2({\rm closed})$ injective via $-2$-meridian dual spheres
  (Thm 5.16(4) proof), so $[S']\ne0$ persists.

## 2. Logged Kirby slide sequence (before/after framings $+$ linkings)
Labels: $D_1,D_2$ dotted $1$-handles at arcs $A_1,A_2$; $A_1,A_2=\gamma_2$ auxiliary
$0$-framed $2$-handles. $K_0$ framing stays $0$ throughout.
Full machine-readable freeze: `output/artifacts/slide_log.json` (5 ops).
- **S0 (seed):** $0$-handle $+K_0$ (framing $0$, $tb=-1$, $r=0$).
- **Op1 ($W^-_{W_2}(3)$ at $A_1$, Fig.3 right):** introduce canceling $(D_1,A_1(0))$;
  band-sum $K_0$ with $U(3)$. $K_0$ framing $0$ unchanged; $tb,r(K_0)$ unchanged
  (Prop 4.7(2)). New: $lk(A_1,D_1)=1$; $K_0$ bands over $D_1$ ($0$ algebraic).
- **Op2 ($W^-_{W_2}(6)$ at $A_2$):** same with $(D_2,A_2(0))$. State $=X^{(2)}_0$.
- **Op3 (distinguished twist $C_2$: $W^-(6)\to W^+(6)$ at $A_2$, Fig.3 left/Fig.8):**
  smooth effect = cork twist along $(W_2,f_2)$-copy (Lemma 4.4 local $+$ Prop 4.5).
  $K_0$ framing still $0$. Legendrian: $tb(K_0)\mathrel{+}=6$ ($-1\to5$ pre-adjustment,
  Prop 4.7(1)), $r$ unchanged at this stage; $\gamma_2$: $tb=2$ base ($+$ clasp, §5
  of WORKLOG), $r=0$.
- **Op4 (Stein adjustment, Step 5(i)–(v)):** zig-zags on $K_0$ ($4$ cusps: $tb$ $5\to1=m_0+1$,
  $|r(K_0)|=4$) and $\gamma_2$ ($tb\to1$, $|r|=1$, sign opposite $r(K_0)$; Lemma 3.5
  sign choice feasible for $n=2$: $t=3$, $2d-t\in\{-3,-1,1,3\}\ni\pm1$).
  Maximizes $|\langle c_1,[K_0-6\gamma_2]\rangle|$ (Lemma 5.14).
- **Op5 (closure):** attach fixed $C_{\rm cap}$ ($2$-, $3$-, $4$-handles) identically
  both sides.
- **Genus check (Fig.4):** after $6$ slides over $\gamma_2$, $U=D^2+12$ bands,
  $\chi=1-12=-11$, one boundary $\Rightarrow g=(2-(-11)-1)/2=6$ (standard
  Exercise 4.5.12(b) argument; clasp twists only twist bands).

## 3. Homology transfer matrix (distinguished class)
$H_2(S^+)=\langle v_0=[K_0-6\gamma_2]\rangle$, $Q=[0]$; $v_0^2=m_0=0$, genus-$6$ rep
(Lemma 5.13). $H_2(S^-)=\langle[K_0]\rangle$, $Q=[0]$, embedded disk/sphere rep
$g'=0$ (Lemma 5.13(2)). Cork-twist homeomorphism preserves $H_*$, $Q$, $\partial$-homology
(Props 4.2/4.5); in these bases **$T=[1]$**, $Q'=T^TQT=Q=[0]$,
$\alpha=(1)\mapsto\alpha'=(1)$. Pairing preserved: $\langle K',\alpha'\rangle=
\langle K,\alpha\rangle=10$ (Lemma-5.14 maximized value
$2p_2+(t_0-1)-m_0+|r_0|=12-2=10$; §5 of WORKLOG shows the $n=2$ clasp is absorbed by
the zigzag-sign choice, so $\Delta=0$; verifier additionally checks conservative
$\Delta=1,2$). Prop 5.15 replay: in $S^+$, any $u_0=a\,v_0$ with genus $\le g_0+p_1=3$,
square $0$ needs $|a|\cdot10\le 2\cdot3-2=4$, forcing $a=0$ — no such basis element
(rank-$1$ contradiction); this is the compact Stein genus gap.

## 4. Adjunction arithmetic (exact integers)
Closed SW adjunction for $b^2\ge0$ (cited): $2g-2\ge|\langle K,b\rangle|+b^2$.
- **$X_2$ side:** $b=\alpha$, $g=6$, $b^2=0$, $|\langle K,\alpha\rangle|=10$:
  $2\cdot6-2=10\ge10+0=10$ — **HOLDS (equality, sharp).**
- **$X'_2$ side** (transported coordinates, sphere rep $S'$, $g'=0$, $(b')^2=0$,
  same pairing $10$): $2\cdot0-2=-2\ge10$ — **FAILS, margin $-12$.**
- Conservative $W_2$-clasp lines: $10\ge10-\Delta$ holds and $-2\ge10-\Delta$ fails
  for $\Delta=1,2$. All replayed in `verify_target.py`.

## 5. Homeomorphic but not diffeomorphic
- **Homeomorphic:** explicit $h:X'_2\to X_2$ = cork homeomorphism on $S$ extended by
  ${\rm id}$ over $C_{\rm cap}$ (Prop 4.5(3); $C_2$ interior so $h|_Y={\rm id}$);
  same $Q$, $\pi_1=0$ (Freedman consistent). No KS ambiguity (explicit $h$, not just
  classification).
- **Not diffeomorphic (either orientation):** $X_2$ minimal symplectic $b_2^+>1$
  $\Rightarrow$ $SW(X_2)\ne0$ (Taubes, cited) $\Rightarrow$ $X_2$ contains **no**
  embedded square-$0$ sphere (closed adjunction gives $-2\ge|K{\cdot}b|\ge0$,
  impossible). $X'_2$ **does** contain one: $S'={\rm core}(K_0)\cup{\rm disk}\subset
  {\rm int}(S^-)$ (Lemma 5.13(2); collar push-in off $Y$; normal Euler intrinsic so
  square stays $0$; $[S']\ne0$ by $-2$-dual injectivity). Hence $SW(X'_2)=0$
  on the corresponding chamber class. A diffeomorphism (either orientation:
  square, genus, $|K{\cdot}b|$ orientation-insensitive; SW basic existence
  conjugation-invariant) would transport the sphere and identify SW, contradiction.
  Class-free form needs no Chern-restriction lemma; the audit-plan pairing form
  (§4) is the literal $|\langle K,[\alpha]\rangle|+[\alpha]^2$ evaluation.

## 6. Proof / computation / conjecture separation
- **Proved here (new):** frozen member data $(W_2,(3,6),S^2\times D^2$ seed$)$;
  5-op slide log with framings/linkings; $T=[1]$, $Q=[0]$ transfer; Def-5.6
  admissibility; Lemma-5.13 genera/squares $(6,0)/(0,0)$; Lemma-5.14 value $10$
  with $n=2$ zigzag feasibility; Prop-5.15 basis obstruction; Fig.4 $12$-band
  $g=6$ count; both adjunction integer lines $+$ conservative $\Delta$ lines;
  binary verdict. Machine-replayed VERIFY_OK 17/17.
- **Computed evidence:** `verify_target.py` (integer/logic layer only),
  `slide_log.json` (frozen diagram data).
- **Cited, not re-proved (per audit plan):** Witten SW setup; Taubes $SW\ne0$;
  closed SW adjunction ($b^2\ge0$); Stein adjunction incl. $g=0$ (Thm 3.4);
  Freedman/topological extension; Akbulut–Yasui handle lemmas
  (Props 4.2/4.3/4.5, Lemmas 5.13/5.14/5.15, Thms 3.6/5.16) for the handle layer;
  Gompf $c_1=r$ formula and $tb-1$ Stein criterion; Gluck extension inside Lemma 4.4.
- **Uncertainty:** none in the integer layer (all checks pass); residual reliance is
  exactly the cited standard package, flagged here honestly.
- **Originality:** admission triage found only qualitative atlases/general existence
  (1102.3049, 1505.02551, 2002.02326, 1710.07034, hep-th/9411102) with no
  member-indexed $(W_2,\tau,X_2,X'_2)$ slide-plus-adjunction decision; the frozen
  triple (diagram, $T=[1]$, integers $10\ge10$ / $-2\ge10$) is the new delta.

## 7. Reproducibility
`python3 output/artifacts/verify_target.py` $\to$ VERIFY_OK (17/17, verdict EXOTIC).
`output/artifacts/slide_log.json` freezes seed/cork/ops/bases/$T$/pairings/cap/boundary.
Independent checker recomputes pairings and both inequality lines from these two files
without re-proving gauge theory — matching integers $+$ binary verdict per audit plan.

## References
[AY] S. Akbulut, K. Yasui, Cork twisting exotic Stein 4-manifolds, arXiv:1102.3049.
[Y] K. Yasui, Corks, exotic 4-manifolds and knot concordance, arXiv:1505.02551.
[DHM] I. Dai, M. Hedden, A. Mallick, Corks, involutions, and Heegaard Floer homology, arXiv:2002.02326.
[T] M. Tange, Boundary-sum irreducible finite order corks, arXiv:1710.07034.
[W] E. Witten, Monopoles and Four-Manifolds, hep-th/9411102.
[G] R. Gompf, Handlebody construction of Stein surfaces, Ann. of Math. 1998.
[LM–AO] Lisca–Matić; Akbulut–Ozbagci (Stein embedding, cited as Thm 3.6 of [AY]).
[AM] Akbulut–Matveyev (Stein adjunction, cited as Thm 3.4 of [AY]).
