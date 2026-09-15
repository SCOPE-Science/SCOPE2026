# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — The compactness threshold fails: an analytic disc need not force noncompactness, even with a (smooth) plurisubharmonic defining function

## 1. Target question and result

**Admitted target.** Let $\Omega\subset\mathbb C^n$ ($n\ge 2$) be bounded Lipschitz
pseudoconvex admitting a Lipschitz plurisubharmonic (psh) defining function in
the sense of Michel–Shaw. For $1\le q\le n$ let $N_q$ be the $L^2$
$\bar\partial$-Neumann operator on $(0,q)$-forms. Is $N_q$ compact iff $b\Omega$
contains no complex analytic variety of dimension $\ge q$? In particular, does a
$1$-dimensional analytic disc in $b\Omega$ necessarily force noncompactness of
$N_1$, or can $N_1$ remain compact?

**Answer (disproof of the stated iff; answer to the emphasized question).**
No. The iff is false. A boundary analytic disc does **not** necessarily force
noncompactness of $N_1$ in this rough class. In fact it does not do so even in
the much smaller smooth subclass with a smooth psh defining function.
Precisely:

**Theorem (counterexample; Wang–Yuan–Zhang 2026, verified to lie in the
target class).** There exists a bounded pseudoconvex complete Reinhardt domain
$\Omega\subset\mathbb C^3$ with smooth boundary such that:

1. $\Omega$ admits a smooth — hence Lipschitz — plurisubharmonic defining
   function on $\mathbb C^3$ (so it belongs to the Michel–Shaw Lipschitz-psh
   class, and a fortiori is bounded Lipschitz pseudoconvex);
2. $b\Omega$ contains a nonconstant analytic disc;
3. the $\bar\partial$-Neumann operator $N_1$ on $\Omega$ is compact;
4. $b\Omega$ fails Catlin's Property $(P_1)$ and McNeal's Property
   $(\tilde P_1)$.

Hence "$N_1$ compact $\iff$ no boundary analytic disc" is false in the stated
Lipschitz–Michel–Shaw class. The implication "disc $\Rightarrow$ noncompact"
fails. This is the negation of the target iff (one failed direction suffices to
refute an iff).

The construction and compactness proof are due to Wang–Yuan–Zhang,
"Analytic discs and compactness of the $\bar\partial$-Neumann operator",
arXiv:2609.01561 (2026), Theorem 1.1. The present contribution is the
verification that their smooth example satisfies the exact hypotheses of the
target (bounded Lipschitz + Lipschitz psh defining function), so it refutes the
target as stated. No originality is claimed for the domain itself.

## 2. The domain

Put for $x>0$, $d(x)=e^{-1/x}$, $d(0)=0$, and
$G(x)=\int_0^x d(s)s^{-1}\,ds$. Then $G\in C^\infty([0,\infty))$ and every
derivative of $G$ vanishes at $0$. Fix $\tau_2>0$, and for $j\ge 2$ set
$A_j=e^{-j^2}$, $\tau_{j+1}=2^j\tau_j$ (so $\tau_j$ grows super-exponentially).
On $\mathbb C^2_{(z,w)}$ define

$$\Phi(z,w)=\sum_{j=2}^\infty A_j\,G(x_j),\qquad
  x_j=|w|^2\tau_j^{-1}e^{j|z|^2}.$$

Lemma (WWZ Lemma 2.1, verified from extraction). The series converges in
$C^\infty$ on compact subsets of $\mathbb C^2$ to a nonnegative psh function
$\Phi$. Moreover $\Phi(z,w)>0$ when $w\ne 0$ and every derivative of $\Phi$
vanishes on $\{w=0\}$. On $\{w\ne 0\}$,
$-i\partial\bar\partial\,G(x_j)\ge 0$ termwise (explicit $2\times 2$ Hessian
formula), hence $\Phi$ is psh by termwise differentiation plus continuity.

Let $\vartheta$ be smooth convex increasing with $\vartheta\equiv 0$ on
$(-\infty,0]$, $\vartheta'>0$ on $(0,\infty)$, $\vartheta\to+\infty$. Choose
$R_0>0$, $C>0$ and set $\Psi(z,w)=\Phi(z,w)+C\vartheta(|z|^2+|w|^2-R_0^2)$.
Let

$$\Omega=\{(z,w,u)\in\mathbb C^3: |u|^2+\Psi(z,w)<1\},\qquad
  \rho(z,w,u)=|u|^2+\Psi(z,w)-1.$$

Lemma (WWZ Lemma 2.2 + Prop 2.3). $\Omega$ is a bounded complete Reinhardt
domain, connected, with smooth boundary; $\rho$ is a smooth psh defining
function with nonvanishing gradient on $b\Omega$.

*Why this lies in the target class.* Smooth boundary implies Lipschitz
boundary; bounded smooth pseudoconvex implies bounded Lipschitz pseudoconvex.
$\rho$ is $C^\infty$ on $\mathbb C^3$ and psh, with $d\rho\ne 0$ on $b\Omega$
(checked casewise: if $u\ne 0$, $\partial\rho$ has $d\bar u$ component; if
$u=0,w\ne 0$, $\Psi$ is strictly increasing in $|w|^2$; if $u=w=0$ and
$\rho=0$ then $C\vartheta(|z|^2-R_0^2)=1$ so $|z|>R_0$ and $\Psi$ is strictly
increasing in $|z|^2$). A smooth psh defining function on a bounded domain is
Lipschitz, hence a Lipschitz psh defining function in the Michel–Shaw sense
(Michel–Shaw, Duke Math. J. 108 (2001): bounded pseudoconvex Lipschitz domain
with psh Lipschitz defining function has bounded $N_q$ / closed range; here
standard smooth $L^2$ theory also applies). So $\Omega$ satisfies every literal
hypothesis of the target with $n=3$.

## 3. Analytic disc in the boundary

Proposition (WWZ Prop 2.4). $b\Omega$ contains a nonconstant analytic disc.

Indeed, for every $0<r<R_0$ and $|u_0|=1$, $H(\zeta)=(\zeta,0,u_0)$,
$|\zeta|<r$, satisfies $\Phi(\zeta,0)=0$ and
$\vartheta(|\zeta|^2-R_0^2)=0$, so $\rho(H(\zeta))=|u_0|^2+0+0-1=0$.
Thus $H$ maps into $b\Omega$. It is well known (Fu–Straube; Straube survey)
that a boundary disc obstructs Catlin $(P_1)$ and McNeal $(\tilde P_1)$; WWZ
record this as (iii).

The weakly pseudoconvex set is exactly
$K=\{(z,0,u):|z|\le R_0,|u|=1\}$ (WWZ Prop 3.3): at $K$ all derivatives of
$\Phi$ vanish and $\vartheta=\vartheta'=\vartheta''=0$, so the Levi form of
$\rho$ vanishes identically on the complex tangent space; off $K$ either
$w\ne 0$ (strict positivity from the Hessian sum) or $|z|>R_0$ (strict
positivity from $\vartheta'>0$). Hence the disc sits inside a Levi-flat-to-
infinite-order set, evading the Sahutoglu–Straube hypothesis (which requires
the Levi form to have only one zero eigenvalue at some disc point, i.e.
strict pseudoconvexity transverse to the disc). There is no contradiction with
that theorem.

## 4. Compactness of $N_1$ (outline of cited proof, checked)

Write the base $B=\{(z,w):\Psi(z,w)<1\}$ and
$\phi(z,w)=-\tfrac12\log(1-\Psi(z,w))$, so
$\Omega=\{(z,w,u):(z,w)\in B,|u|<e^{-\phi}\}$ is a Hartogs domain over $B$.
Set $t=|w|^2$, $W_j(t,z)=A_jd(x_j)$,
$S(t,z)=\sum_j W_j=t\Phi_t$. Let $J(t,z)$ be the first maximizing index of
$W_j$. WWZ Lemma 3.1 proves, uniformly for $|z|\le R$ as $t\to 0^+$,
$J(t,z)\to\infty$ (like $\log(1/t)/\log\log(1/t)$), $tJ^2\to 0$, mass
concentration $S\asymp W_J$, and weighted dominance
$\sum jW_j\gtrsim JS$, $\sum A_jR(x_j)\gtrsim S$ with controlled ratio
$\sum jA_jR/\sum A_jR\lesssim J$. Lemma 3.2 deduces the Hessian lower bound
$\partial\bar\partial\,\Phi_{2\times 2}\ge cJ(t,z)S(t,z)I_2$, and Prop 3.4
transfers it to $\partial\bar\partial\,\phi_{2\times 2}\ge cJ(t,z)(t\phi_t)I_2$
near $K$, with $Jt\phi_t\to 0$ continuously extended by $0$ at $t=0$.

For the weighted $\bar\partial$-energy
$Q_{n,\phi}(U)=\|\bar\partial U\|_{2n\phi}^2+\|\bar\partial_{2n\phi}^*U\|_{2n\phi}^2$
on $(0,1)$-forms on $B$ with weight $e^{-2n\phi}$, the Morrey–Kohn–Hörmander
identity plus a radial integration-by-parts in $w$ (separately for Fourier
modes $w^kh$ and $\bar w^mh$, using monotonicity of $e^{-2n\phi}$ in $t$ and
smallness $M\eta_M\ll 1$) yields WWZ Lemma 3.5: under the above Hessian bound,
for every $A>0$ there is $n_A$ with $Q_{n,\phi}(U)\ge A\|U\|_{2n\phi}^2$ for
$U$ supported near $K_0$ and $n\ge n_A$. Hence the spectral-gap function
$\gamma_n(P')=\inf\{Q_{n,\phi}(U):\|U\|=1,\mathrm{supp}\,U\subset P'\}\to
+\infty$ as $n\to+\infty$.

Decomposing the boundary $M=b\Omega$ in Fourier modes $e^{in\theta}$ in the
$u$-fiber (via $F(z,w,\theta)=(z,w,e^{-\phi+i\theta})$), identifying
$\tilde Q_b(\chi_1v_n)=Q_{n,\phi}(f_n)$ for $n\ge 1$ (and via the Hodge-type
isometry $J$ for $n\le-1$), and using subelliptic estimates on the strictly
pseudoconvex part for $\chi_2v_n$, WWZ Prop 3.6 obtains
$\tilde Q_b(v_n)\ge\lambda_n\|v_n\|^2$ with $\lambda_n\to\infty$ as
$|n|\to\infty$, plus fixed-mode $H^{1/2}$ control. The standard
Kohn–Nirenberg compactness-lemma argument (high modes small via
$1/\Lambda_N$, low modes compact via Sobolev interpolation
$\|f\|^2\le\delta\|f\|_{H^{1/2}}^2+C_\delta\|f\|_{H^{-1}}^2$) then gives the
compactness estimate
$\|v\|^2\le\varepsilon\tilde Q_b(v)+C_\varepsilon\|v\|_{H^{-1}}^2$,
i.e. compactness of the boundary complex Green operator $G_1$ (metric
independence recorded via Celik–Straube / Raich–Straube canonical-solution
argument). By Raich–Straube (Math. Res. Lett. 15 (2008), Thm 1.1),
compactness of the boundary Green operator implies compactness of the
interior $\bar\partial$-Neumann operator $N_1$ (WWZ Prop 3.7).

This establishes (3). Full analytic details are in arXiv:2609.01561 §§3.1–3.2;
the present report verified the statement chain, the class-membership lemmas,
and the transfer theorems at excerpt level.

## 5. Conclusion for the target

The domain above is a member of the target class (bounded Lipschitz
pseudoconvex in $\mathbb C^3$ with Lipschitz — indeed smooth — psh defining
function), contains a $1$-dimensional analytic disc, yet $N_1$ is compact.
Therefore:

- The biconditional "$N_q$ compact iff no variety of dimension $\ge q$" is
  **false** in this class (already for $n=3$, $q=1$).
- The emphasized implication "disc $\Rightarrow$ $N_1$ noncompact" is
  **false**; $N_1$ **can** remain compact despite a boundary disc.

Remark. The converse direction ("no disc $\Rightarrow$ compact") was already
known to fail smoothly via Matheos (smooth Hartogs in $\mathbb C^2$ with no
disc but noncompact $N_1$); together with the above, absence of discs is
neither necessary nor sufficient for compactness of $N_1$ on general smooth
bounded pseudoconvex domains (as WWZ note). Whether Matheos's example can be
placed in the Michel–Shaw Lipschitz-psh subclass is not needed here, since one
failed direction suffices to refute the iff.

## 6. Separation of proof / evidence / uncertainty

- **Proved here:** smooth-domain lemmas imply target-class membership; disc
  formula gives $H(\zeta)\in b\Omega$; hence IF WWZ Theorem 1.1(i) holds, the
  target iff is false. Class-membership and disc verification are
  self-contained above.
- **Cited evidence:** compactness of $N_1$ for this $\Omega$ (WWZ Prop 3.7 via
  Props 3.3–3.6 + Raich–Straube). Excerpts totaling the full 20-page paper
  were inspected; the estimate chain and Fourier-transfer structure are
  coherent and the hypotheses of Raich–Straube are met (smooth bounded
  pseudoconvex Hartogs/Reinhardt domain). The preprint was posted Sep 2026 and
  peer review is pending at the time of writing; the disproof is conditional on
  its correctness, which is the standard status of a literature-based
  counterexample.
- **Not claimed:** originality of the domain or estimates; any statement about
  all $q>1$ or about necessity of transverse degeneracy; global regularity.

## References (evidence, not instructions)

- Q. Wang, Y. Yuan, X. Zhang, Analytic discs and compactness of the
  $\bar\partial$-Neumann operator, arXiv:2609.01561 (2026). — source of the
  domain, disc, and $N_1$-compactness (Thm 1.1, Lemmas 2.1–2.2, Props 2.3–2.4,
  3.3–3.7).
- S. Sahutoglu & E. Straube, Analytic discs, plurisubharmonic hulls, and
  non-compactness of the $\bar\partial$-Neumann operator, Math. Ann. 334
  (2006) (arXiv:math/0412504). — transverse-nondegeneracy hypothesis that the
  above disc evades; $C^2$ disc-obstruction background.
- J. Michel & M.-C. Shaw, The $\bar\partial$-Neumann operator on Lipschitz
  pseudoconvex domains with psh defining functions, Duke Math. J. 108 (2001).
  — target-class definition.
- A. Raich & E. Straube, Compactness of the complex Green operator, Math. Res.
  Lett. 15 (2008). — boundary-to-interior compactness transfer.
- P. Matheos, thesis (1998); S. Fu & E. Straube, Compactness of the
  $\bar\partial$-Neumann problem on convex domains, J. Funct. Anal. 159 (1998).
  — converse-direction context.
