# Exact variance of fair-input pair synchronization in odd Černý automata

## Finding
Let \(n\ge3\) be odd. Consider the \(n\)-state Černý automaton on \(\{0,\ldots,n-1\}\), with letters \(r\) and \(c\): \(r(i)=i+1\pmod n\), while \(c(n-1)=0\) and \(c(i)=i\) otherwise. Take independent equiprobable letters at each step. Let \(T_n\) be the first time the images of the initial states \(0\) and \((n-1)/2\) agree.

**Theorem.** For every odd integer \(n\ge3\),
\[
\mathbb E[T_n]=\frac{(n-1)^2(2n+1)}2,\qquad
\operatorname{Var}(T_n)=\frac{n(n-1)(4n^4-8n^3+3n^2+7n-14)}6.
\]
In particular, \(\operatorname{Var}(T_n)/n^6\to2/3\) and the coefficient of variation satisfies \(\sqrt{\operatorname{Var}(T_n)}/\mathbb E[T_n]\to\sqrt{2/3}\). The mean formula is the previously established result of Gusev [1]; the exact variance and fluctuation ratio are the contribution here.

## Assumptions and scope
Only **one initial pair** is tracked, not synchronization of all states at once. Letters are independent, fair, and common to both copies; \(T_n\) counts the number of letters, including the one at which the pair coalesces. Coalescence is permanent. The stated formulas hold for every odd \(n\ge3\), including \(n=3\), and only this parity and this pair are claimed.

## Proof
**1. Pair coordinates.** The \(n(n-1)/2\) unordered distinct pairs are bijective with coordinates \((i,\ell)\), where \(0\le i\le n-1\), \(1\le\ell\le h=(n-1)/2\), using the two states \(i\) and \(i+\ell\pmod n\), oriented along the shorter cyclic separation. Under \(r\), \((i,\ell)\mapsto(i+1\pmod n,\ell)\). Under \(c\), all coordinates are fixed except
\[
(0,1)\mapsto\dagger,\quad (0,\ell)\mapsto(1,\ell-1)\ (\ell\ge2),\quad
(n-\ell,\ell)\mapsto(n-\ell,\ell+1)\ (\ell<h),\quad
(h+1,h)\mapsto(1,h),
\]
where \(\dagger\) is the absorbing, synchronized state. This is the oriented pair graph established in [1, Section 3, Lemma 1] after a cyclic state relabeling. It can also be checked directly from the two letter actions.

**2. Moments and an explicit potential.** Write \(M(i,\ell)=\mathbb E_{i,\ell}T\) and \(S(i,\ell)=\mathbb E_{i,\ell}T^2\). Both vanish at \(\dagger\). The first-step identities are
\[
M=1+\tfrac12(M_r+M_c),\qquad
S=2M-1+\tfrac12(S_r+S_c).
\]
The second identity follows by expanding \((1+T')^2\), since \(\mathbb E T' =M-1\). Define for integer \(\ell\)
\[
 f_\ell=2\ell(2n^2-4n+1)-\ell(\ell-1)(4n-2),
\]
and the quartic
\[
\begin{aligned}
g_\ell={}&\frac43(2n-1)^2\ell^4-\frac83(2n-1)(2n^2-2n-1)\ell^3\\
&-\frac23(8n^2-2n-7)\ell^2+\frac43(4n^5-10n^4+8n^3+n^2-7n+2)\ell.
\end{aligned}
\]
In particular \(f_0=g_0=0\). Set \(m_\ell=1+(f_\ell+f_{\ell-1})/2\) and \(s_\ell=2m_\ell-1+(g_\ell+g_{\ell-1})/2\). Define the potentials, at \(i=0\), by
\[
 M(0,\ell)=m_\ell,\qquad S(0,\ell)=s_\ell.
\]
For \(1\le i\le n-\ell\), define
\[
 M(i,\ell)=f_\ell-2(i-1),\quad
 S(i,\ell)=g_\ell-(i-1)(4f_\ell-2)+4(i-1)(i-2).
\]
For \(n-\ell+1\le i\le n-1\), define
\[
 M(i,\ell)=m_\ell+2(n-i),\quad
 S(i,\ell)=s_\ell+(n-i)(4m_\ell-2)+4(n-i)(n-i+1).
\]
These specify all transient states without overlap. The first-step identities at nonexceptional coordinates hold by subtracting successive phase values. At \((0,\ell)\), they hold by the definitions of \(m_\ell,s_\ell\), with \(f_0=g_0=0\) covering \(\ell=1\). At a lower-layer exceptional state \((n-\ell,\ell)\), substitute the expressions for \((n-\ell,\ell+1)\) and \((n-\ell+1,\ell)\). Both resulting polynomial residuals are identically zero. At the maximal-layer exceptional state \((h+1,h)\), substitute \((1,h)\) and \((h+2,h)\); both residuals again vanish. The right-region formulas wrap consistently to \((0,\ell)\) after the rotation at \(i=n-1\). These identities are expanded exactly, for symbolic \(n,\ell,i\), in `verify.py`.

**3. Identification and variance.** All transient coordinates have a path to \(\dagger\), since Černý's automaton is synchronizing. Under the fair input law a common finite positive-probability synchronization block exists, giving an exponentially decaying tail and uniqueness of the finite solutions to both moment systems. Thus the displayed potentials are the genuine moments. The initial pair corresponds to \((1,h)\), whence \(\mathbb E T_n=f_h\) and \(\mathbb E T_n^2=g_h\). Direct symbolic simplification yields
\[
 f_h=\frac{(n-1)^2(2n+1)}2,\quad
 g_h-f_h^2=\frac{n(n-1)(4n^4-8n^3+3n^2+7n-14)}6.
\]
The stated leading terms follow from polynomial degrees. This proves the theorem.

## Verification
Run `python verify.py` with Python 3 and SymPy. The checker tests every algebraic moment recurrence symbolically, including the exceptional pair-graph edges and cyclic wrap, and proves the displayed mean and variance identities as polynomial equalities for arbitrary symbolic \(n\). It separately constructs the original unordered-pair transition matrix and solves both moment systems using exact rational arithmetic for \(n=3,5,7,9\). Expected output ends `SYMBOLIC_ALL_ODD_N_OK`; independent checks produce variances 142, 5320, 49294, 248448. Small-instance solves are checks, not the justification for the all-odd theorem, which is the polynomial recurrence identity plus absorption uniqueness.

## Relationship to prior work
Gusev [1, Theorem 3, Lemma 1, and equations (14)–(19)] establishes the oriented pair automaton, derives \(\mathbb E T\), and motivates pair synchronization as error recovery for stochastic inputs. The first-moment formula and the pair-coordinate method are explicitly **prior work**. The full accessible preprint does not state a formula for \(\mathbb E T^2\) or \(\operatorname{Var}(T)\). Standard absorbing Markov-chain moment recurrences are general methods, not explicit evaluations of this Černý family. Other inspected literature [2,3] emphasizes deterministic reset lengths or synchronization probability, not this fair-input pair's exact second moment. Targeted searches did not identify a stronger published second-moment evaluation; search absence alone does not establish historical priority.

## Limitations
The result does not give the full absorption-time distribution, a sharp tail asymptotic, or the variance for even \(n\), biased letters, other starting pairs, or all-state synchronization. A nonzero limiting coefficient of variation quantifies relative mean-square fluctuations; it is not by itself a proof about convergence in probability. Independent verification and complete historical-priority certification have not been performed. A later textbook discussion of stochastic automata [4] was not available for substantive full-text comparison and is a residual priority risk.

## References
[1] V. V. Gusev, *Synchronizing automata with random inputs*, arXiv:1404.6731v1, April 27, 2014, Sections 1 and 3, Lemma 1 and Theorem 3. https://arxiv.org/abs/1404.6731

[2] A. Kisielewicz, J. Kowalski and M. Szykuła, *A fast algorithm finding the shortest reset words*, Computing and Combinatorics (COCOON 2013), LNCS 7936, pp. 182–196. https://arxiv.org/abs/1203.2822

[3] F. Gonze and R. M. Jungers, *On the synchronizing probability function and the triple rendezvous time for synchronizing automata*, SIAM J. Discrete Math. 30 (2016). https://doi.org/10.1137/15M1024603

[4] N. Privault, *Discrete Stochastic Processes: Tools for Machine Learning and Data Science*, Springer, 2024, chapter “Synchronizing Automata”; full chapter not inspected. https://doi.org/10.1007/978-3-031-65820-4_3
