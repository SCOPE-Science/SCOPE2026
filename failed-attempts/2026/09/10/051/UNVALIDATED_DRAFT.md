# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Triple overlap-necessity witness for the BMV cubic saddle (committed-scale certificate) with quantitative no-go obstructions for the log-growth target and the literal balance-scale fallback

## 1. Objects and definitions (self-contained)

Let
$$\phi(x,y)=xy+y^3/3,\qquad \Sigma=[0,1]^2,\qquad \xi_0=(1/2,1/2).$$
This is the Buschenhenke–Müller–Vargas (BMV) Sec.1 phase at $\gamma=1$
($\phi_\gamma=xy+\gamma y^3/3$); cubic coefficient $c_3=1/3$.
The extension operator is
$$Eh(x)=\int_\Sigma h(z)\,e^{i(x_1z_1+x_2z_2+x_3\phi(z))}\,dz.$$
For $\delta>0$, $A>0$, $S\subset\Sigma$ is $(\phi,A\delta)$-flat (GMO Def.1.1) if
$$\sup_{u,v\in S}|\phi(v)-\phi(u)-\nabla\phi(u)\cdot(v-u)|\le A\delta.$$
For packets $f_i$ supported in $S_i$, the $L^4$ energy ratio on a ball $B$ is
$$R(f)=\frac{\|Ef\|_{L^4(B)}}{(\sum_i\|Ef_i\|_{L^4(B)}^2)^{1/2}}.$$
$R=1$ is orthogonality; $R=\sqrt3$ is full coherence of 3 equal packets.

**Committed certificate scale.** $\delta_\star=0.005$, $A_0=2$, budget
$A_0\delta_\star=0.01$, committed ball $B_{0.05}$ (also $B_{0.02}$).
This is NOT the literal $c_3^2=1/9$; see §6 for the exact relation.

## 2. Theorem (committed-scale triple witness)

There exist three explicit $(\phi,0.01)$-flat rectangles $S_1,S_2,S_3\subset\Sigma$,
all containing $\xi_0$, with pairwise distinct long directions, no one containing
another (pairwise unions non-flat), each maximal in the sense that stated dilations
break flatness, and disjointly supported packets $P_i\subset S_i$ with
$f_\star=\sum_i|P_i|^{-1}{\bf1}_{P_i}$ satisfying
$$R(f_\star)=\sqrt3=1.7320\ge\sqrt{3/2}\approx1.2247\quad\text{on }B_{0.05}\text{ (and }B_{0.02}\text{)}.$$
Hence every flat decomposition covering $P_1\cup P_2\cup P_3$ by disjoint flat
rectangles misses mass: flat-overlap number $\ge3$ is forced at this scale.

### Coordinates
- $S_1=[0,1]\times[0.4965,0.5035]$ (full-width $x$-band, height $H=0.007$).
- $S_2$: $\xi_0$-centred rectangle in the Hessian-null frame
  $w=(-1,\!2)/\sqrt5$ (unit, $116.57^\circ$), $t=(2,\!1)/\sqrt5$:
  half-length $a=0.10$ along $w$, half-width $b=0.004$ along $t$.
- $S_3$: $\xi_0$-centred rectangle in the $d=(1,\!.25)/|(1,\!.25)|$ frame
  ($14.04^\circ$), $d^\perp$: half-length $c=0.085$, half-width $e=0.004$.
- Pairwise long-direction separations: $63.43^\circ$ (S1–S2), $14.04^\circ$ (S1–S3),
  $77.47^\circ$ (S2–S3).

## 3. Proof: flatness (three sup-norm checks)
Deviation identity: $D(u,v)=\phi(v)-\phi(u)-\nabla\phi(u)\cdot(v-u)$.
- S1: $|D|\le H\cdot1+(1/2+H/2)H^2+H^3/3=0.007025\le0.01$.
- S2: with $\Delta_1,\Delta_2$ the $w,t$ offsets,
  $|D|\le(4ab+2b^2)+4s^3/(5\sqrt5)+8s^3/(15\sqrt5)=0.006694\le0.01$,
  $s=2a+b=0.204$ (linear $T_1=w\!\cdot\!\Delta$ cancels exactly along $w$;
  quadratic/cubic remainders bounded as logged).
- S3: $|D|\le PQ+u_yQ^2+Q^3/3=0.009473\le0.01$ with logged $P,Q,u_y$.
Each bound is verified twice: float/numpy in the script and exact sympy
(rational+$\sqrt5$/$\sqrt{17}$) arithmetic; sampled dense-grid maxima
(0.00702/0.00264/0.00920) confirm tightness. Replay:
`python3 output/artifacts/verify_triple.py` (exit 0).

## 4. Proof: common point, no-containment (junction), maximality
- $\xi_0\in S_1\cap S_2\cap S_3$ by construction (interior point of each).
- Junction (sympy-exact $|D|$ for witness pairs, all $>0.01$):
  S1∪S2: $0.044960$; S1∪S3: $0.012223$; S2∪S3: $0.010849$.
  So no $(\phi,0.01)$-flat rectangle contains any pairwise union; overlap $\ge3$ forced.
- Maximality (dilations break flatness, sympy-exact):
  S1 width 2x: $0.014098$; S2 length 3x: $0.025760$, 2x-diagonal: $0.017076$,
  width 20x: $0.012739$; S3 length 1.5x: $0.017173$, width-corner 3x: $0.012301$;
  S1 length already spans the domain. All $>0.01$.

## 5. Proof: energy ratio $R(f_\star)=\sqrt3\ge\sqrt{3/2}$
Packets: $P_1\subset S_1$ left tail, $P_2\subset S_2$ upper $w$-tail
($\alpha\in[0.045,0.095]$, $|\beta|\le0.92b$), $P_3\subset S_3$ upper $d$-tail,
pairwise disjoint, grid-certified ($2000^2$ common grid: each $P_i$ 100% in own
$S_i$, 0 cross cells). On $B_r$, $r\le0.05$, all packet phases agree to $<0.05$ rad,
so $Ef_i$ are essentially equal positive constants; with area normalization,
$R=(3c)/( \sqrt{3c^2})=\sqrt3=1.7320$ on the $21^3$ grid in $B_{0.05}$ and $B_{0.02}$;
Monte Carlo (seed 7) confirms $1.7320$ at $r=0.05$. Margin over $\sqrt{3/2}$: $0.51$.

## 6. Quantitative obstructions (why the full log target AND the literal fallback fail)
(a) **Fan rigidity (kills TARGET fan leg).** Rotation scan of $(a,b)=(0.10,0.004)$
strips off the null direction: general-pair UB never flat ($0.016$–$0.039>0.01$);
endpoint-pair deviation exceeds budget from $30^\circ$ on. Full-width $x$-bands
$H=\alpha\delta$ pass only for $\alpha\le2$ (UB $=$ endpair $0.00501$ at
$\alpha=1$, $0.01005>0.01$ at $\alpha=2$). Admissible long flat rectangles
collapse onto the two Hessian null rulings: no transverse $N_j\sim j$ fan exists.
(b) **Large-ball washout (kills TARGET transfer leg).** Committed 3-packet ratio
vs ball radius (MC, seed 7): $1.7320\,(0.05)\to1.7314\,(0.3)\to1.7244\,(1.0)
\to1.6707\,(3.0)\to1.4564\,(9)\to1.1700\,(30)\to0.9765\,(200)$, crossing
$\sqrt{3/2}$ downward to the incoherent limit $\sim1$. Nested $v$-family
mass-model ratio $\le1$ ($0.966$/$0.999$): the only surviving $\sqrt N$ growth is
for nested non-maximal families — trivial, not cover-based decoupling gain.
(c) **Literal-fallback no-go.** Literal pins $c_3=1/3$, $\delta_\star=c_3^2=1/9$,
budget $2/9$, $\theta_0=|c_3|^{1/2}=33.08^\circ$, $B_9$: at $\delta=1/9$ the triple's
junction deviations ($0.045/0.053/0.023$) lie strictly BELOW $2/9$ — the
overlap-forcing leg is impossible at literal scale. Uniform shape-rescaling
argument: UB scales as $s^2$, junctions as $s$; feasibility window empty for all
$s\ge1.15$ (feasible only for shrunken $s\le1.1$ at $d\approx0.005$, i.e. the
committed scale). Enlarged-$S_2$ probe ($a=0.20/0.30$): UB explodes to
$0.0426/0.1362$ while junctions grow linearly — dead. Hence the exact
fallback criterion (a)–(c) is unsatisfiable by bounded repair; the committed-scale
witness above is the strongest true statement (it meets the fallback's intent:
overlap 3 + ratio $\ge\sqrt{3/2}$ — at the audited committed scale, not the
literal $c_3^2$ scale).

## 7. Originality and prior-art separation
Admission live retrieval found no BMV triple witness or log lower bound.
GMO proves $O(\log)$-overlap SUFFICIENCY (Thm 2.2) — a lower-bound witness does not
follow; App.5 partition-insufficiency is qualitative (no triple, no ratio).
BMV proves linear restriction only. Bourgain–Demeter (elliptic/cone) and Guo et al.
(quadratics) exclude the cubic cell by hypothesis. The triple coordinates,
sympy-exact flatness/junction/maximality ledger, and $\sqrt3$ small-ball ratio with
the rigidity/washout/literal-no-go quantities are new.

## 8. Replay instructions
- `python3 output/artifacts/verify_triple.py` → exit 0; prints UBs, sympy-exact
  junction/maximality ledger, alignment, $R$ values, T1/T2/T3 blocks; writes
  `output/artifacts/triple_results.json`. Needs: python3, numpy, sympy (no scipy).
- Large-ball MC probe (r=9/30/200, seed 7, n=60000): inline snippet archived in
  `output/target_exit.json` recovery_test.script description; values
  1.4564/1.1700/0.9765.
- McCabe-style audit: recompute §3 UBs by hand from the deviation identity;
  check §4 sympy rationals in the script; regrid §5 alignment at any resolution.

## 9. Limitations (explicit)
- Scale pinned to committed $\delta_\star=0.005\ne c_3^2$; literal $c_3^2$ criterion
  provably unsatisfiable for this shape family (§6c) — claimed as no-go, not proved
  for ALL conceivable shapes.
- Ratio proved on committed small balls $B_{\le0.05}$; large-ball transfer
  disproved for THIS packet family (washout), not for all $f$.
- Full TARGET $D(\delta_j)\ge c\sqrt{\log\delta_j^{-1}}$: neither proved nor
  disproved in general — only the null-frame-fan + rescaling route is blocked.
- S1–S3 separation $14.04^\circ<33.08^\circ$: meets "pairwise distinct" but not the
  literal $\theta_0$ pin.
