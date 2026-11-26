# Exact quorum reversals in the protective-cost ceiling

## Finding

In the well-mixed collective-risk public-goods model of Li et al., let \(N\ge3\) be group size and \(2\le M\le N-1\) the protection quorum. Put \(n=N-1\), \(h=M-1\), and \(s=n-h\). Each defector contributes a failure-survival factor \(\rho\in(0,1)\); the failure loss is \(L>0\), and activated protection reduces risk proportionally by \(\omega\in(0,1]\). The known sharp ceiling on the extra cost compatible with a positive protective advantage is \(L\omega H_{N,M}(\rho)\), where
\[
B_{n,h}=\binom nh(h/n)^h(s/n)^s,\qquad H_{N,M}(\rho)=B_{n,h}(1-\rho^s).
\]
The following comparative statics hold:

* For fixed \(N\) and \(\rho\), the ceiling is uniquely greatest at the smallest quorum, \(M=2\).
* For any adjacent comparison \(2\le M\le N-2\), if \(2h\le n-1\) then \(H_{N,M+1}(\rho)<H_{N,M}(\rho)\) for all \(0<\rho<1\). If \(2h>n-1\), there is a unique \(\rho_h\in(0,1)\) satisfying
  \[
  \frac{1-\rho_h^{s-1}}{1-\rho_h^s}=\frac{B_{n,h}}{B_{n,h+1}}.
  \]
  The higher quorum has the larger ceiling for \(0<\rho<\rho_h\), an equal ceiling at \(\rho_h\), and a smaller ceiling for \(\rho_h<\rho<1\).

If \(\omega=0\), the normalized comparisons for \(H\) remain valid, but all actual cost ceilings are zero. The conclusions concern the maximum *local payoff advantage* across compositions; they do not rank the critical efficacy for a stable protective equilibrium.

## Model and the known ceiling

Focal and co-player types are ordinary cooperator \(C\), defector \(D\), and protective cooperator \(S\), with population frequencies \(x,y,z\) on the simplex. Co-players are sampled independently. Ordinary and protective cooperators make the same baseline contribution; only \(S\) pays an additional cost \(k>0\) and counts toward the protection quorum. A group with \(j\) defectors faces failure probability \(1-\rho^j\) without protection. Comparing a focal \(S\) with a focal \(C\), only groups with exactly \(h\) protective co-players can change their protection status. The payoff difference is therefore \(-k+L\omega\Psi_M\), with
\[
\Psi_M=\binom nh z^h[(x+y)^s-(x+\rho y)^s].
\]
Indeed the bracket sums the risk-weighted probabilities for the remaining \(s\) nonprotective co-players. For \(0<z<1\), the second base is \(\rho(1-z)+(1-\rho)x\); the unique best choice at fixed \(z\) is \(x=0\). Maximizing \(z^h(1-z)^s\) gives \(z=h/n\); neither endpoint gives a positive value. Thus \(\Psi_M\) has a unique maximizer \((0,s/n,h/n)\). It is also the unique maximizer of the realized benefit \(L\omega\Psi_M\) when \(\omega>0\); at \(\omega=0\) the realized benefit is identically zero. The supremum over strictly interior compositions is the same by continuity, so a positive interior advantage exists precisely when \(k<L\omega H_{N,M}(\rho)\).

## Proof of the quorum comparisons

For \(1\le h\le n-2\), canceling the binomial coefficients and powers gives
\[
Q:=\frac{B_{n,h+1}}{B_{n,h}}
=\frac{(1+1/h)^h}{(1+1/(s-1))^{s-1}}.
\]
The function \(u\mapsto (1+1/u)^u\) is strictly increasing on \((0,1)\) and on all of \((0,\infty)\): the derivative of its logarithm is \(\log(1+1/u)-1/(u+1)>0\), by integrating \(1/t\) between \(1\) and \(1+1/u\). Thus \(Q\le1\) exactly for \(h\le s-1\), or \(2h\le n-1\). The symmetric sequence \(B_{n,h}\) decreases toward its center and then increases, so it attains its maximum at the two ends (one end if \(n=2\)). Because \(1-\rho^{n-h}\) strictly decreases as \(h\) increases, \(H_{N,M}\) is strictly greatest at \(h=1\).

The adjacent ratio of ceilings is \(Q F_s(\rho)\), where
\[
F_s(\rho)=\frac{1-\rho^{s-1}}{1-\rho^s}
=1-\frac{1}{\sum_{i=0}^{s-1}\rho^{-i}},\qquad s\ge2.
\]
The sum in the denominator strictly decreases with \(\rho\in(0,1)\), so \(F_s\) strictly decreases from \(1\) to \((s-1)/s\). If \(Q\le1\) this proves the strict decrease with quorum. If \(Q>1\), then \(Q<s/(s-1)\): the numerator \((1+1/h)^h<e\) follows by \(\log(1+t)<t\) for \(t>0\), while \((1+1/(s-1))^s>e\) follows from \(\log(1+t)>t/(1+t)\) with \(t=1/(s-1)\). The adjacent ratio therefore crosses one strictly once as claimed.

For example, with \(N=5\), the ratio for \(M=4\) versus \(M=3\) is \((9/8)/(1+\rho)\); the reversal is at \(\rho=1/8\). At \(\rho=1/16\) the two ceilings normalized by \(L\omega\) are \(405/1024\) and \(765/2048\), respectively. Since \(765/2048<3/8<405/1024\), at normalized cost \(k/(L\omega)=3/8\) the higher quorum admits compositions with positive protective advantage while the lower quorum does not. This is neither an invasion-from-rarity criterion nor a persistence claim.

## Verification, prior work and limits

The bundled `check.py` is a supplementary exact-rational checker of the pivotal formula, the small-quorum optimum, and sampled adjacent comparisons, including the exact \(N=5\) reversal. It does not establish decay rates or test an infinite parameter range; the proof above gives the uniform comparison for all admissible real \(\rho\).

Li, Li, He, Shi and Szolnoki, [*Bifurcation and Multistability in a Collective-Risk Public Goods Game with Quorum-Activated Protection*](https://arxiv.org/abs/2609.28132), give the model and focal payoff identity. Their Table 2 treats critical protection efficacy for local stability, a different quantity. [*Sharp protective-cost ceiling and singular phase-volume collapse in quorum public goods*](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-sharp-protective-cost-ceiling-and-singular-phase-volume-collapse--017d5b602d4e) already gives the exact risk-weighted payoff ceiling and proves critical-cost exclusion; neither is claimed as new here. Nöldeke and Peña, [*Group size and collective action in a binary contribution game*](https://doi.org/10.1016/j.jmateco.2020.02.003), analyze unweighted binomial pivotal probabilities in a different two-action model. The comparison here concerns the interaction between the binomial peak and the risk factor in the known three-strategy ceiling. It assumes independent group sampling and the stated risk and proportional efficacy laws, and does not establish historical priority over all equivalent quorum comparisons.
