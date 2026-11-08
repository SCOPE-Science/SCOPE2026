# Global integer-orbit collapse and a four-period plateau in a balanced ultradiscrete predator–prey map

## Finding
For every positive integer \(c\), consider the map \(F_c:\mathbb Z^2\to\mathbb Z^2\)
\[
F_c(x,y)=\bigl(1+x-\max\{0,x,y\},\;y+\max\{0,c+x\}-c\bigr).
\]
This is the balanced parameter family \(T=1\), \(\Gamma=\Delta=c\) of the ultradiscrete predator–prey model in Willox [1]. There is exactly one fixed state, \((0,1)\), and it is its own sole preimage. Every other integer initial state reaches the *same* primitive cycle, containing \((1,2)\), in finitely many iterations. The least cycle period depends only on \(c\):
\[
p(c)=\begin{cases}
18,&c=1,\\
19,&c=2,\\
22,&c=3,\\
24,&c\ge4.
\end{cases}
\]
In fact, the actual cycle states, not merely their period, are independent of \(c\) for all integers \(c\ge4\). In addition, when \(c=1\), the *exact* first-hitting time from \((0,N)\) to \((1,2)\) is
\[
\tau_N=N^2+2N+2\qquad(N\in\mathbb Z,\ N\ge2).
\]
The quadratic transients show that uniform eventual periodicity does not mean uniformly short convergence over the infinite state lattice.

## Assumptions and scope
All variables \(x,y\), the parameter \(c\), and time are integers, with \(c\ge1\). The map acts on the *full integer lattice*, without sign restrictions. The infinite state \(-\infty\), the rational and real state spaces, and unbalanced parameters are not included. “Reaches the cycle” means equality of integer states in finite time; no Euclidean perturbation stability is asserted. A *primitive cycle* is a finite orbit of least positive period.

## Proof
**One-step reduction.** Write \((x',y')=F_c(x,y)\). As \(\max\{0,x,y\}\ge\max\{0,x\}\),
\[
x'\le1+x-\max\{0,x\}\le1.
\]
Thus every orbit enters \(x\le1\) after one update, and this half-plane is forward invariant.

**Absorption into a single representative state.** For integer states in \(x\le1\), the following exhaustive cases apply.

If \(x\le-1\) and \(y>0\), then \(x'=x+1-y\le x\le-1\). Also, because \(c+x\le c-1\), \(y'=y+\max\{0,c+x\}-c\le y-1\). Hence \(y\) becomes nonpositive in finitely many steps, with \(x\le-1\) throughout.

If \(x\le-1\) and \(y\le0\), then \(x'=x+1\) and \(y'\le y\). After exactly \(-x\) steps this state reaches \((0,y_0)\) with \(y_0\le0\). It then moves to \((1,y_0)\).

If \(x=1\), \(y\le1\), then \(F_c(1,y)=(1,y+1)\); it therefore reaches \((1,2)\). If \(x=1\), \(y=2\), it already is that state. If \(x=1\), \(y\ge3\), its successor is \((2-y,y+1)\), in the first case \(x\le-1,y>0\).

If \(x=0\), \(y\ge2\), then \(F_c(0,y)=(1-y,y)\), in the first case. If \(x=0\), \(y\le0\), it moves to \((1,y)\). Finally \((0,1)\) is fixed. These cases show that every orbit not visiting \((0,1)\) reaches \((1,2)\) in finite time.

**Isolation of the fixed state.** If \(F_c(x,y)=(0,1)\), its first coordinate requires \(\max\{0,x,y\}=1+x\), hence \(x\ge-1\). If \(x=-1\), then \(y\le0\) and \(y'=y-1\le-1\), impossible. If \(x=0\), the first coordinate forces \(y=1\). If \(x\ge1\), then \(y=x+1\) and \(y'=2x+1\ge3\), also impossible. So \((0,1)\) is its sole preimage. In particular, all other initial states must reach \((1,2)\).

**Exact primitive cycles.** The self-contained `cycle_certificate.json` gives four finite prefix lists starting at \((1,2)\), ending at \((0,b)\), with
\[
(b,p)=(-5,18),\ (-8,19),\ (-11,22),\ (-13,24)
\]
for \(c=1,2,3,\ge4\), respectively. In each case append the states \((1,j)\) for consecutive integer \(j=b,b+1,\ldots,1\). Substituting every listed pair directly into \(F_c\) verifies the transition to the next pair and closure from \((1,1)\) back to \((1,2)\). All listed pairs are distinct, proving that each displayed period is least. For \(c\ge4\), all listed first coordinates are at least \(-4\); therefore \(\max\{0,c+x\}-c=x\) throughout the same cycle, so the \(c=4\) certificate applies **to every** integer \(c\ge4\), not merely to tested values. Because every nonfixed orbit reaches this cycle, there are no other integer periodic orbits.

**Exact quadratic transient.** For \(c=1\), beginning at \((0,N)\) with integer \(N\ge2\), the first step is \((1-N,N)\). The next \(N\) steps successively decrease the second coordinate through the positive integers to zero, while the first coordinate decreases to \(a=1-N(N+1)/2\). The next \(-a\) steps reach \((0,a)\); one step gives \((1,a)\); and \(2-a\) further vertical steps reach \((1,2)\). No earlier state equals \((1,2)\). Adding the durations yields \(1+N-a+1+(2-a)=N^2+2N+2\).

## Verification
Run `python verify.py` from the directory containing `cycle_certificate.json`. This standard-library program checks that each prefix and vertical tail closes as a primitive orbit, checks the common certificate for many values beyond \(c=4\), tests all states in specified finite integer rectangles for eventual entry, tests the exact transient formula through \(N=80\), and tests fixed-point preimages in finite rectangles. Its observed output is `VERIFY_OK checks=210378`. The proof above, rather than these finite tests, establishes the universal claims.

## Relationship to prior work
Willox [1, §2, equation (9)] derives this ultradiscrete map and illustrates periodic trajectories for unbalanced parameters, including \((\Gamma,\Delta)=(6,5)\) with period 32; the article does not provide this global integer-state classification for the balanced parameter family. Ohmori and Yamazaki [2,3] investigate limit cycles and return mechanisms for a different max-plus map with first component of the form \(Y+\max(0,TX)\) and second component \(B-\max(0,DX)\). Their cycle-period results do not contain the present two-component map or the all-initial-state absorption theorem. The balanced case and finite-time quadratic transient are distinguished from previously reported example orbits. A related older ultradiscretisation paper [4] was identifiable from its abstract but its complete manuscript was not available for comparison; specialized prior work might still imply parts of this result.

## Limitations
The classification is only for integer initial data and positive integer balanced parameters, not the full rational-state model. Finite-time absorption in \(\mathbb Z^2\) is not the same as attraction under small real perturbations. The theorem does not characterize unbalanced parameter regimes, rational periods, or optimal worst-case hitting-time bounds. The 2007 paper [4] was not fully inspected, and broader historical priority has not been independently established.

## References
[1] R. Willox, *A simple strategy for constructing ultradiscrete systems that exhibit the same dynamics as a given continuous model*, arXiv:2607.15627v1 (first posted 2026-07-17), https://arxiv.org/abs/2607.15627 .

[2] S. Ohmori and Y. Yamazaki, *Periodicity of limit cycles in a max-plus dynamical system*, arXiv:2107.09300 (2021), https://arxiv.org/abs/2107.09300 .

[3] S. Ohmori and Y. Yamazaki, *A Generalization for Ultradiscrete Limit Cycles in a Certain Type of Max-Plus Dynamical Systems*, arXiv:2402.06230 (2024), https://arxiv.org/abs/2402.06230 .

[4] R. Willox et al., *From limit cycles to periodic orbits through ultradiscretisation*, Physica A (2007), DOI: 10.1016/j.physa.2007.07.002. Abstract available; complete text not inspected.
