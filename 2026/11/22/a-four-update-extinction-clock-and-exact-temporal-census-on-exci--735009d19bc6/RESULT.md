# A four-update extinction clock and exact temporal census on excitable sunlet graphs

## Finding

On the labelled sunlet graph \(S_n=C_n\circ K_1\) (\(n\ge3\)), put three Greenberg–Hastings states \(0,1,2\) at every vertex. A resting vertex enters state \(1\) when **at least two distinct neighbours** are excited, while \(1\mapsto2\mapsto0\) automatically. All updates are simultaneous. For each initial configuration \(z\), let \(\tau(z)=\min\{t\ge0:F^t(z)=0\}\), and let \(N_j(n)=\#\{z:\tau(z)=j\}\).

Let \(\rho_1,\rho_2,\rho_3\) be the roots (with multiplicity) of
\[
R(X)=X^3-9X^2+9X-21,
\]
and \(\lambda_1,\ldots,\lambda_5\) the roots of
\[
P(X)=X^5-9X^4+18X-108.
\]
Define \(H_n=\sum_{a=1}^3\rho_a^n\) and \(V_n=\sum_{a=1}^5\lambda_a^n\). Although defined through algebraic roots, both are nonnegative integers for every \(n\ge3\). **The complete first-extinction census** is
\[
\begin{aligned}
N_0(n)&=1,\\
N_1(n)&=4^n-1,\\
N_2(n)&=H_n-4^n,\\
N_3(n)&=V_n-H_n,\\
N_4(n)&=9^n-V_n.
\end{aligned}
\]
There are no later extinction times. In particular, the sharp maximum is \(3\) for \(n=3\) and \(4\) for every \(n\ge4\). Under independent uniform initial colours,
\[
\Pr(\tau=4)\ge 1-\left(1-\frac{2}{2187}\right)^{\lfloor n/5\rfloor}\longrightarrow 1.
\]
Thus almost every large sunlet requires the **last permissible update**, despite the fact that no pendant vertex can ever become newly excited.

## Assumptions and scope

The graph has core vertices \(u_i\) and pendant vertices \(v_i\), with indices \(i\in\mathbb Z/n\mathbb Z\), edges \(u_i u_{i+1}\) and \(u_i v_i\), no loops, and no parallel edges. Initially every one of the \(2n\) vertices independently assumes any of the three states; the counting is labelled, not up to rotations or reflections. Write \(c_i=X_0(u_i)\) and \(\ell_i=X_0(v_i)\). Excitation threshold is exactly two; a different threshold, extra edges, asynchronous updates, or more colours are **not** covered. A state \(1\) created at update \(t\) becomes \(2\) at \(t+1\), then \(0\) at \(t+2\).

## Proof

**1. The terminal excitation time.** A pendant has only one neighbour, so no pendant becomes newly excited after time zero. Suppose a core \(u_i\) became newly excited at an update \(t\ge3\). Since the leaves have no state \(1\) at time \(t-1\ge2\), the two core neighbours \(u_{i-1},u_{i+1}\) must both have state \(1\) then. They cannot be old excited states, because every state \(1\) at a positive time was newly created at that update. At their creation at update \(t-1\), there were no excited pendant neighbours at time \(t-2\ge1\); consequently, **each** needed \(u_i\) in state \(1\) at time \(t-2\). Hence \(u_i\) was in state \(2\) at time \(t-1\), contradicting the required resting state at the onset of excitation at \(t\). Thus the last possible new state \(1\) is at time \(2\), and all sites are resting by time \(4\).

**2. Local criterion for the last wave.** At update \(2\), a core \(u_i\) becomes excited if and only if the initial configuration has
\[
\begin{split}
c_{i-2}=c_{i+2}=1,\quad c_{i-1}=c_{i+1}=0,\\
\ell_{i-1}=\ell_{i+1}=1,\quad c_i\in\{0,2\}.
\end{split}
\tag{1}
\]
Indeed, the two core neighbours must both become newly excited at update \(1\). With \(c_i\ne1\), the only way either neighbour can be newly excited is to have its other core neighbour and its own leaf initially excited, while its own initial state was zero. Condition (1) also makes \(u_i\) resting at time \(1\): initial colour \(2\) has relaxed; initial colour \(0\) receives no initially excited core neighbour. Conversely those conditions create the two supporting neighbours at time \(1\), so \(u_i\) excites at time \(2\). All configurations with (1) therefore have first all-rest time \(4\), and all others have extinction time at most \(3\). For \(n=3\), the same modular equations demand that a vertex be both \(0\) and \(1\), making (1) impossible. For \(n=4\), its two distance-two endpoints coincide compatibly, so (1) is feasible.

**3. States extinguished by time two.** \(\tau\le1\) occurs exactly when no vertex initially has colour \(1\): there are \(4^n\) such configurations including zero. If an initial excited state exists, it remains refractory at time \(1\). Therefore \(\tau\le2\) if and only if no resting core is newly excited at update \(1\). For a core triple \((a,b,c)\in\{0,1,2\}^3\), the number of allowed colours of its *own* leaf is
\[
w(a,b,c)=\begin{cases}
3,&b\ne0\ \text{or neither neighbour is }1,\\
2,&b=0\ \text{and exactly one neighbour is }1,\\
0,&b=0\ \text{and both neighbours are }1.
\end{cases}
\]
Let \(Q\) be the \(9\times9\) integer matrix indexed by ordered pairs \((a,b)\), with the entry from \((a,b)\) to \((b,c)\) equal to \(w(a,b,c)\), and every other entry zero (parallel values are added). A closed walk of length \(n\) picks a cyclic core word and all independently allowable leaf colours, so
\[
\#\{\tau\le2\}=\operatorname{tr}(Q^n)=H_n.
\]
Direct finite determinant calculation gives
\[
\det(I-zQ)=1-9z+9z^2-21z^3.
\]
The nonzero eigenvalues are the three roots of \(R\); the other six eigenvalues are zero. This proves the stated formula for \(H_n\).

**4. Counting the final wave.** Classify a core-and-leaf pair \((c_i,\ell_i)\) as \(A\) if \(c_i=1\) (three letters), \(B\) if \(c_i=0,\ell_i=1\) (one letter), and \(C\) otherwise (five letters). Criterion (1) becomes exactly the presence of one of the circular five-letter words
\[
ABBBA\qquad\text{or}\qquad ABCBA.
\]
Construct the weighted prefix-avoidance automaton with states \(\epsilon,A,AB,ABB,ABC,ABBB,ABCB\). On reading an \(A,B,C\) letter, it retains the longest suffix which is a proper prefix of either forbidden word and forbids completed words. Letter multiplicities are \(3,1,5\), respectively. In the displayed state order its transition-count matrix is
\[
M=\begin{pmatrix}
6&3&0&0&0&0&0\\
5&3&1&0&0&0&0\\
0&3&0&1&5&0&0\\
5&3&0&0&0&1&0\\
5&3&0&0&0&0&1\\
6&0&0&0&0&0&0\\
6&0&0&0&0&0&0
\end{pmatrix}.
\]
Every circular initial letter word avoiding both patterns has exactly one compatible cyclic prefix-state labelling: the state at a position is the longest matching proper prefix of its left-infinite periodic history (at most four preceding letters are needed). Thus the exact avoidance count is \(\operatorname{tr}(M^n)\), valid also at \(n=3,4\) with modularly repeated positions. Finite determinant calculation gives
\[
\det(I-zM)=1-9z+18z^4-108z^5.
\]
The five nonzero eigenvalues are the roots of \(P\), and the other two are zero, so \(\operatorname{tr}(M^n)=V_n\). There are \(9^n\) initial words in total, proving \(N_4=9^n-V_n\), and subtraction gives all remaining entries. Both determinant identities can be reproduced by the exact-integer checker `VERIFY.py`.

**5. Sharpness and typicality.** On \(C_3\circ K_1\), set a core pattern \((0,1,1)\) and all leaves to zero: its first extinction occurs at time \(3\). For \(n\ge4\), choose one centre with the pattern (1), setting any other sites arbitrarily. At every fixed block of five consecutive site pairs, (1) has exactly \(3\cdot1\cdot6\cdot1\cdot3=54\) satisfying assignments out of \(9^5\), independently across disjoint blocks. Taking \(\lfloor n/5\rfloor\) such blocks yields the stated exponential lower bound. The maximum four updates is consequently both sharp and typical at large length.

## Verification

`VERIFY.py` requires only Python 3 standard libraries. It constructs both finite weighted transfer matrices directly from the local conditions; computes their characteristic polynomials by exact Newton identities; compares the root-sum trace counts against the full-state recurrence; independently evolves every one of \(9^n\) labelled initial states for \(n=3,4,5,6\); and checks the resulting complete histograms at further lengths through \(n=12\). Its captured output is `CHECKS.txt`. In particular the five first-extinction populations at \(n=3,4,5,6\) are

| \(n\) | \(N_0\) | \(N_1\) | \(N_2\) | \(N_3\) | \(N_4\) |
|---|---:|---:|---:|---:|---:|
| 3 | 1 | 63 | 485 | 180 | 0 |
| 4 | 1 | 255 | 4307 | 1926 | 72 |
| 5 | 1 | 1023 | 36425 | 21330 | 270 |
| 6 | 1 | 4095 | 303407 | 221022 | 2916 |

The all-length proof is the local causality argument plus the finite symbolic transfer identities; finite enumeration alone is **not** used as a proof for unbounded \(n\).

## Relationship to prior work

Greenberg and Hastings' excitable-medium model and the systematic threshold-dependent analysis by Durrett and Griffeath [1] establish the underlying model and motivate finite-time questions; [1] concerns periodic wave activity and threshold-range scaling on planar lattices, not the graph family or the exact temporal census here. Gravner, Lyu and Sivakoff [2] develop a theory for **single-contact** three-colour excitation on arbitrary graphs; its defining update in their paper requires one excited neighbour, so its general results do not imply this threshold-two statement. Related published computations on threshold-two excitation on wheel graphs [3] and on open ladders [4] address different neighbourhood structures; neither the four-update sunlet cutoff nor its two root-sum counting polynomials follows as a graph special case. In particular sunlets have one degree-one neighbour at every core site, while wheels have a single universal hub and ladders have cross-rail edges.

## Limitations

No conclusion is claimed for four or more refractory states, nonuniform excitation thresholds, noisy/asynchronous dynamics, or other unicyclic graphs. The exact distribution is for uniformly labelled core–pendant positions, not unlabelled graph colourings. The formula supplies whole-graph extinction times, not the complete joint spatial history. The literature comparison establishes no mathematical uniqueness guarantee: unindexed articles and inaccessible full text could contain equivalent counts. There has been no independent mathematical audit.

## References

1. Richard Durrett and David Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002 (first public submission 1993-03-22); *Experimental Mathematics* **2** (1993), 183–208. https://arxiv.org/abs/patt-sol/9303002 ; DOI:10.1080/10586458.1993.10504277.
2. Janko Gravner, Hanbaek Lyu and David Sivakoff, *Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs*, arXiv:1610.07320 (first submission 2016-10-24); *Annals of Applied Probability* **28** (2018), 3324–3357. https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
3. *Sharp five-step extinction for threshold-two excitation on wheel graphs*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-five-step-extinction-for-threshold-two-excitation-on-wheel--58917bc0decb .
4. *Exact three-rate excitation census on open square ladders*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-three-rate-excitation-census-on-open-square-ladders--9fa61fb1a7f9 .
