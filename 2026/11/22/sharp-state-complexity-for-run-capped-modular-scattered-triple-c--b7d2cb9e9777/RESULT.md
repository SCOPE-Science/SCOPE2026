# Sharp state complexity for run-capped modular scattered-triple counters

## Finding
For integers \(m\ge2\) and \(r\ge2\), define the binary regular language
\[
\mathcal L_{m,r}=\left\{w\in\{0,1\}^*:1^r\text{ is not a contiguous factor of }w,\quad \binom{w}{001}\equiv0\pmod m\right\}.
\]
Here \(\binom{w}{001}\) counts increasing triples of positions spelling `001`, not necessarily consecutive. The minimum number of states in a **complete deterministic finite automaton** recognizing \(\mathcal L_{m,r}\) is exactly
\[
\kappa(\mathcal L_{m,r})=
\begin{cases}
r m^2+1,&m\text{ odd},\\
2r m^2+1,&m\text{ even}.
\end{cases}
\]
All states, including the single rejecting sink, are necessary. The parity jump follows from the exact period of the residue sequence \(\binom{z}{2}\bmod m\). In particular, imposing the cap on one-runs retains every combination of modular counter data and permitted run length: the natural product bound is sharp for every pair of parameters.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). The input is read left to right; `001` is a scattered subsequence, whereas \(1^r\) is a *contiguous* forbidden factor. The empty word is accepted. The automaton is complete and deterministic, and only its state count is minimized. Every quantifier in the theorem ranges over integers \(m,r\ge2\); there is no restriction to prime moduli or to bounded input lengths. This theorem does not concern nondeterministic, reversible, weighted, or two-way automata.

Set \(c(z)=\binom z2\bmod m\) for nonnegative integers \(z\), and let
\[
P=\begin{cases}m,&m\text{ odd},\\2m,&m\text{ even}.\end{cases}
\]
The function \(c\) has exact positive period \(P\). Indeed,
\[
\binom{z+d}{2}-\binom z2=dz+\binom d2.
\]
Any period \(d\) forces \(d\equiv0\pmod m\), by subtracting at consecutive \(z\), and \(\binom d2\equiv0\pmod m\), by evaluating at \(z=0\). Conversely these two conditions suffice. They give the least positive \(d=m\) if \(m\) is odd, and \(d=2m\) if \(m\) is even.

## Proof
**1. A recognizing automaton.** Use the state set
\[
Q=\bigl(\mathbb Z/P\mathbb Z\bigr)\times\bigl(\mathbb Z/m\mathbb Z\bigr)\times\{0,1,\ldots,r-1\}\;\sqcup\;\{\bot\}.
\]
The initial state is \((0,0,0)\), and the accepting states are precisely the triples with second coordinate zero. The sink \(\bot\) loops on both letters. The transitions on nonsink states are
\[
\begin{aligned}
\delta((z,t,j),0)&=(z+1,t,0),\\
\delta((z,t,j),1)&=\begin{cases}(z,t+c(z),j+1),&j<r-1,\\\bot,&j=r-1.\end{cases}
\end{aligned}
\]
The first coordinate is read modulo \(P\) and the second modulo \(m\). On appending a one to a prefix with \(z\) zeros, each pair of those zeros yields exactly one new scattered `001`; hence the count increases by \(\binom z2\). The third coordinate records the number of trailing ones and precisely detects \(1^r\). This proves recognition and the upper bound \(|Q|=rPm+1\).

**2. Reachability.** Every nonsink state \((z,t,0)\) is reached by a word of the form
\[
0^2(10^P)^q0^a,
\]
where \(q\in\{0,\ldots,m-1\}\) represents \(t\pmod m\) and \(a\ge1\) satisfies \(2+a\equiv z\pmod P\). Every one in the repeated block sees a number of preceding zeros congruent to two modulo \(P\), so it contributes exactly one modulo \(m\). The word ends in zero and has no adjacent ones. For arbitrary \(j\in\{1,\ldots,r-1\}\), first reach \((z,t-jc(z),0)\) by this construction, then append \(1^j\). The sink is reached by \(1^r\). Thus all \(rPm+1\) states are reachable.

**3. A separation device.** Write \(f(a)=c(z+a)\) and \(g(a)=c(z'+a)\) for two residues \(z,z'\pmod P\). If \(z\not\equiv z'\pmod P\), choose \(B_0\in\{1,\ldots,P\}\) with \(z+B_0\equiv2\pmod P\), so \(f(B_0)=1\), and put \(C=g(B_0)\). There exists \(b\in\{1,\ldots,P\}\) with
\[
g(b)-C f(b)\not\equiv0\pmod m.
\]
Otherwise \(g(a)=Cf(a)\) for all positive \(a\), by periodicity. Taking second forward differences gives \(1=C\pmod m\), since the second difference of \(\binom{z+a}{2}\) is one. Equality \(g(a)=f(a)\) for all positive \(a\) would then make \(z'-z\) a period of \(c\), contradicting its exact period \(P\).

Choose \(B>B_0\) by adding a sufficient multiple of \(P\) so that \(B>b\). For \(u\in\{0,1\}\), and any \(q\in\{0,\ldots,m-1\}\), the legal suffix
\[
S(u,q)=0^b(10^P)^u0^{B-b}(10^P)^q
\]
starts with a zero and adds exactly \(u f(b)+q f(B)=u f(b)+q\) to the scattered count from a state with first coordinate \(z\); from first coordinate \(z'\) it adds \(u g(b)+q C\). The formula follows from the period \(P\), and all marker ones in this suffix are separated by zeros.

**4. Myhill–Nerode separation.** Consider two distinct nonsink states. If their third coordinates differ, say \(j<j'\), use first the suffix \(1^{r-j'}\), which kills the state with run \(j'\) but not the state with run \(j\). Follow it by at least one zero to reach zero-count residue two, then append \((10^P)^q\) with \(q\) chosen to make the latter state's residue zero. This accepts from one state but not the other.

If the run coordinates agree and the zero-count residues are equal but the count residues differ, start with at least one zero to obtain zero-count residue two, and append \((10^P)^q\) to cancel the count residue of the first state. This suffix accepts from exactly one.

Finally, if the zero-count residues differ, apply the separation device. From a first state \((z,t,j)\), choose \(q_u\equiv-t-u f(b)\pmod m\), represented between zero and \(m-1\), for \(u=0,1\). Both suffixes \(S(u,q_u)\) are accepted from that state. From the second state \((z',t',j')\), the resulting count residues differ by the **nonzero** value \(g(b)-C f(b)\), so at least one of these two suffixes rejects. Initial zero symbols clear any legal trailing-one run. This proves the states inequivalent. From every nonsink state some accepted continuation exists by calibration at residue two; no continuation from \(\bot\) is accepted. Therefore all \(rPm+1\) states are pairwise distinguishable, proving the claimed exact state count.

## Verification
The included standalone `checker.py` uses only the Python standard library. Executing `python checker.py` constructs and minimizes 44 complete automata for \(2\le m\le12\), \(2\le r\le5\), checks 14,226 enumerated states, and confirms the exact formula in every case. For \(2\le m\le5\), \(2\le r\le4\), it constructs explicit distinguishing suffixes for 25,680 unordered pairs of nonsink states. It separately compares direct occurrence counting with state-machine acceptance for 98,292 binary words through length twelve. These finite checks are reproducibility tests, not substitutes for the all-parameter proof above.

## Relationship to prior work
Lejeune, Rigo and Rosenfeld [1] study binomial equivalence and Parikh-matrix signatures of finite words; Leroy, Rigo and Stipulanti [2] investigate binomial coefficients of words modulo primes. Salomaa, Salomaa and Smith [3] survey descriptional and operational state complexity. These establish the motivation and surrounding machinery, but the inspected material does not give an exact minimal-state formula for this run-capped modular scattered-triple language. The full text of an unrestricted modular \(0^d1\) counter theorem [4] gives exactly \(mP\) states in the special case \(d=2\). Its separation argument exploits unrestricted suffixes with arbitrarily long consecutive blocks of ones, which cannot be used in the run-capped language. Its upper-bound counter and the standard run automaton yield our product upper bound, but neither theorem proves the constrained intersection has that many distinct right languages. The present run-safe two-level calibration and run-killing suffixes supply the missing lower bound for every \(m,r\).

## Limitations
This is a result in deterministic state complexity for the exact language as stated. No claims are made for arbitrary forbidden factors, other scattered patterns, alternate residue targets, or other machine models. Priority against unindexed literature has not been independently established. The complete publicly accessible RESULT.md of [4] was inspected; it concerns unrestricted counting and gives no run-capped state-minimality theorem. Historical priority against other unindexed material remains uncertain. Independent mathematical validation has not been performed.

## References
[1] M. Lejeune, M. Rigo, M. Rosenfeld, *On the binomial equivalence classes of finite words* (first public 2020-01-31), https://arxiv.org/abs/2001.11732 .

[2] J. Leroy, M. Rigo, M. Stipulanti, *Generalized Pascal triangle for binomial coefficients of words* (first public 2017-05-23), https://arxiv.org/abs/1705.08270 .

[3] A. Salomaa, K. Salomaa, T. J. Smith, *Descriptional Complexity of Finite Automata — Selected Highlights* (first public 2023-01-09), https://arxiv.org/abs/2301.03708 .

[4] *Exact state complexity of modular scattered zero-power–one counts*, indexed public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-state-complexity-of-modular-scattered-zero-power-one-count--9df1828ce330 ; the complete RESULT.md was inspected.
