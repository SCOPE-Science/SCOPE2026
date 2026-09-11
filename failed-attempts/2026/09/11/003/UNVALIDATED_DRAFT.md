# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A grade-vanishing disproof of the p=5 V(1) stem-56 filtration-2 survival claim

## Abstract
The target claims that at $p=5$, on $V(1)=S/(5,v_1)$, the ANSS $E_2$ class
$c=\beta_{4/2}$ in bidegree $(t-s=56,s=2)$ is a permanent cycle detecting a
nonzero $v_2$-periodic class in $\pi_{56}(V(1))$.
We prove this is false as stated: $E_2^{2,58}=0$ by an $8$-divisibility grade
argument, so no such $c$ exists, no permanent-cycle certificate exists at that
bidegree, and the stated $d_9$ source (and its $d_9$ target) are both empty.

## 1. Setup and conventions
- Work $5$-locally. $BP_*=\mathbf{Z}_{(5)}[v_1,v_2,\dots]$, $|v_i|=2(5^i-1)$.
- $BP_*BP=BP_*[t_1,t_2,\dots]$, $|t_i|=2(5^i-1)$.
- ANSS bidegree convention: $E_2^{s,t}=\mathrm{Ext}^{s,t}_{BP_*BP}(BP_*,BP_*(X))$,
  stem $=t-s$, filtration $=s$. Differential
  $d_r:E_r^{s,t}\to E_r^{s+r,t+r-1}$.
- $V(0)=S/5=\mathrm{cof}(S\xrightarrow{5}S)$,
  $V(1)=\mathrm{cof}(\Sigma^8V(0)\xrightarrow{v_1}V(0))$ where $|v_1|=2(5-1)=8$.
- Since $5$ is a non-zerodivisor on $BP_*$ (torsion-free) and $v_1$ is a
  non-zerodivisor on $BP_*/5\cong\mathbf{F}_5[v_1,v_2,\dots]$ (polynomial ring),
  $(5,v_1)$ is a regular sequence, and the cofiber sequences give
  $$BP_*(V(0))\cong BP_*/(5),\qquad BP_*(V(1))\cong BP_*/(5,v_1)
    \cong\mathbf{F}_5[v_2,v_3,\dots].$$

## 2. Grade lemma
**Lemma.** Every generator of $BP_*$ and $BP_*BP$ over $\mathbf{Z}_{(5)}$ has
degree divisible by $q=2(p-1)=8$ at $p=5$. Hence every homogeneous element of
$BP_*(V(1))$ and every term of the $BP_*BP$-cobar complex
$C^s=BP_*(V(1))\otimes_{BP_*}\overline{\Gamma}^{\otimes s}$
($\overline{\Gamma}$ the augmentation ideal of $BP_*BP$) has internal degree
$0\bmod 8$. Consequently $E_2^{s,t}(V(1))=0$ unless $8\mid t$.

*Proof.* $|v_i|=|t_i|=2(5^i-1)$. Since $5\equiv1\bmod4$, $4\mid(5^i-1)$, so
$8\mid2(5^i-1)$. Explicitly $|v_1|=8$, $|v_2|=48$, $|v_3|=248$, etc.
$BP_*(V(1))=\mathbf{F}_5[v_2,\dots]$ is generated in such degrees, so it is
concentrated in degrees $0\bmod8$. The cobar term $C^s$ is spanned by monomials
$m\otimes\gamma_1\otimes\cdots\otimes\gamma_s$ whose total internal degree is a
sum of such generator degrees, hence $0\bmod8$. The cobar differential preserves
internal degree, so cohomology (the $E_2$-term) inherits the vanishing. ∎

Machine check: `output/artifacts/grade_check.py` verifies the generator degrees
$8,48,248,1248,6248$ are $0\bmod8$ and exhausts $960$ cobar-monomial degree sums
in the window, all $0\bmod8$ (emits `VERIFY_OK`).

## 3. Main result (target is false)
**Theorem.** At $p=5$, for $X=V(1)$, $E_2^{2,58}=0$. In particular there is no
$E_2$ class $c=\beta_{4/2}$ in bidegree $(t-s=56,s=2)$, no permanent cycle there,
and no nonzero $v_2$-periodic class detected in filtration $2$ stem $56$ via
such a $c$. The Toda-bracket-plus-operation witness package attached to $c$ is
vacuous: it cannot witness a nonexistent class.

*Proof.* Bidegree $(t-s=56,s=2)$ means $t=56+2=58$. Since $58\bmod8=2\neq0$,
the Lemma gives $E_2^{2,58}=0$. Hence $E_r^{2,58}=0$ for all $r\ge2$; no cocycle,
no permanent cycle, no detection. ∎

**Corollary (the $d_9$ window is empty at both ends).**
$d_9:E_9^{2,58}\to E_9^{11,66}$. Both source $t=58\equiv2\bmod8$ and target
$t=66\equiv2\bmod8$ (stem $55$) vanish by the Lemma. So no $d_9$ differential is
supported on, or lands in, the pinned bidegrees.

## 4. What is and is not shown
- Shown: the target as literally pinned (stem $56$, filtration $2$, $t=58$) is
  impossible by grading alone; the falsification is unconditional and needs no
  chart lookup.
- Not shown: anything about neighboring bidegrees with $8\mid t$ (e.g. stems
  $56\pm k$ with $t\equiv0\bmod8$), the actual group $\pi_{56}(V(1))$, or whether
  a differently-graded $\beta$-class survives. The disproof targets only the
  exact pinned claim.
- Standards used: regular-sequence identification of $BP_*(V(1))$ (classical
  complex-orientation / generalized-Moore-spectrum fact) and the degree formula
  $|v_i|=2(p^i-1)$; both are textbook (e.g. Ravenel, Complex Cobordism).
  No undigitized chart is invoked.

## 5. Reproducibility
Run `python3 output/artifacts/grade_check.py` (stdlib only); expect `VERIFY_OK`.
The script prints generator degrees mod $8$, the $t=58$ obstruction line, the
exhaustion count, and the $d_9$-target check $t=66\equiv2\bmod8$.
