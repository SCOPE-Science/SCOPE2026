# Sharp six-step collapse and complete capture-time geometry in an excitable max-plus map

## Finding
Consider the planar max-plus system introduced by Ohmori and Yamazaki,
\[
F_B(X,Y)=\bigl(Y+\max(0,2X),\;B-\max(0,2X)\bigr),\qquad B<0.
\]
Its unique equilibrium is \((B,B)\). For every initial condition in the entire plane, define the **first exact capture time**
\[
\tau_B(X,Y)=\min\{j\ge0:F_B^{\,j}(X,Y)=(B,B)\}.
\]
Then **six is the least global capture index**:
\[
\boxed{F_B^{\,6}(\mathbb R^2)=\{(B,B)\},\qquad F_B^{\,5}(\mathbb R^2)\ne\{(B,B)\}.}
\]
More sharply, the full first-capture-time partition consists of the following half-planes and polygonal strips. Write \(b=-B>0\), and set \(u=X/b\), \(v=Y/b\). When \(u\le0\),
\[
\tau_B(X,Y)=
\begin{cases}
0,&(u,v)=(-1,-1),\\
1,&v=-1,\ (u,v)\ne(-1,-1),\\
2,&v\le0,\ v\ne-1,\\
4,&0<v\le\tfrac12,\\
5,&\tfrac12<v\le\tfrac32,\\
6,&v>\tfrac32.
\end{cases}
\]
When \(u>0\),
\[
\tau_B(X,Y)=
\begin{cases}
3,&v\le-2u,\\
4,&-2u<v\le\tfrac12-u,\\
5,&\tfrac12-u<v\le\tfrac32,\\
6,&v>\tfrac32.
\end{cases}
\]
In particular, the **maximal six-step transient occurs if and only if** the *initial second coordinate* exceeds a single threshold, independently of the initial first coordinate:
\[
\boxed{\tau_B(X,Y)=6\ \Longleftrightarrow\ Y>-3B/2.}
\]
Every time in \(\{0,1,2,3,4,5,6\}\) is attained; the exact capture times do not depend on the size of \(B<0\) after positive scaling. The regions of exact capture time, not just an upper bound, are determined everywhere including switching lines and ties.

## Assumptions and scope
The parameter \(B\) is any strictly negative real number; the state space is all of \(\mathbb R^2\) with no boundedness, genericity or nonzero-coordinate restrictions. The symbol \(\max\) is the ordinary real maximum. The clock counts applications of the original two-coordinate map, beginning with iteration zero. A state already at the equilibrium has time zero; all other times are *first* hitting times. The boundary case \(B=0\), for which a separate homogeneous theory is already available, is **not** included. This result pertains to this precise dissipative ultradiscrete map, not the full discretized Sel'kov differential equations or to arbitrary max-plus maps.

## Proof
**1. Positive scaling and the unique equilibrium.** Set \(b=-B>0\) and \((u,v)=(X/b,Y/b)\). Since \(\max(0,2bu)=b\max(0,2u)\), the normalized map is
\[
F(u,v)=\bigl(v+2u_+,\,-1-2u_+\bigr),\qquad u_+=\max\{u,0\}.
\]
The normalized target is \((-1,-1)\), and \(F_B\) is conjugate to \(F\) under multiplication by \(b\). If \(u\le0\), a fixed point satisfies \((u,v)=(v,-1)\), hence \((u,v)=(-1,-1)\). If \(u>0\), the fixed-point equations yield \(v=-u\) and then \(u=-1\), impossible on this branch. Thus the fixed point is unique.

**2. Global six-step bound by exhaustive branch algebra.** Let \(x_j\) denote the first coordinate of \(F^j(u,v)\), and let \(y_j\) denote its second coordinate. For every \(j\ge0\),
\[
x_{j+1}=y_j+2(x_j)_+,\qquad y_{j+1}=-1-2(x_j)_+.
\]
Consequently \(y_j\le-1\) for every \(j\ge1\). We prove \(x_4<0\) by four exhaustive cases.

If \(x_1\le0\), then \(x_2=-1-2u_+<0\), \(x_3=-1\), and \(x_4=-1\). If \(x_1>0\) but \(x_2\le0\), then \(x_3=-1-2x_1<0\) and \(x_4=-1\). If \(x_1>0\), \(x_2>0\) and \(x_3\le0\), then \(x_4=-1-2x_2<0\). Finally, if \(x_1,x_2,x_3\) are all positive, direct substitution gives
\[
\begin{split}
x_2&=-1-2u_++2x_1,\\
x_3&=-1-2x_1+2x_2,\\
x_4&=-1-2x_2+2x_3=-5-4u_+<0.
\end{split}
\]
These cases also cover equality on every switching line. Because \(x_4<0\), one has \(F^5(u,v)=(y_4,-1)\). Since \(y_4=-1-2(x_3)_+\le-1<0\), one further iterate gives \(F^6(u,v)=(-1,-1)\), **for every real** \((u,v)\).

**3. Complete partition and earliest arrival.** First suppose \(u\le0\). The first state is \(F(u,v)=(v,-1)\). If \(v\le0\), a second step gives \((-1,-1)\). The first step is itself the target precisely when \(v=-1\); the initial point is the target precisely when \((u,v)=(-1,-1)\). These yield the time-zero, time-one and time-two strata with the stated exceptions. For \(v>0\), the next first coordinate is \(x_2=2v-1\). If \(0<v\le1/2\), it is nonpositive, and the target is reached for the first time at step four: the earlier state \(F^3(u,v)=(-1-2v,-1)\) differs from the target. If \(v>1/2\), then \(x_2>0\), and the next first coordinate is \(x_3=2v-3\). For \(1/2<v\le3/2\), this is nonpositive, so capture is first attained at step five (the prior state has first coordinate \(-1-2x_2<-1\)). For \(v>3/2\), \(x_3>0\), so the state at step five has first coordinate \(y_4=-1-2x_3<-1\), and capture occurs exactly at step six.

Now suppose \(u>0\). The first coordinate after one step is \(x_1=v+2u\). If \(v\le-2u\), then \(x_1\le0\); the next state has first coordinate \(x_2=-1-2u<-1\), and step three is the first arrival at the target. If \(v>-2u\), the next first coordinate is
\[
x_2=-1-2u+2(v+2u)=2(u+v)-1.
\]
If \(v\le1/2-u\), then \(x_2\le0\) and \(x_3=-1-2x_1<-1\), so step four is the first arrival. Otherwise \(x_2>0\), and
\[
x_3=-1-2x_1+2x_2=2v-3.
\]
If \(v\le3/2\), then \(x_3\le0\), the fourth first coordinate is \(-1-2x_2<-1\), and the first capture is step five. If \(v>3/2\), then \(x_3>0\), and the fifth first coordinate is \(-1-2x_3<-1\), so the first capture is step six. These disjoint cases exhaust all points and prove the displayed partition.

**4. Sharpness and attained times.** In normalized units, the seven witness initial states
\[
(-1,-1),\quad(0,-1),\quad(0,-2),\quad(1,-3),\quad(0,1/4),\quad(0,1),\quad(0,2)
\]
have first-capture times \(0,1,2,3,4,5,6\), respectively, by Step 3. In particular, \((0,2)\) is not captured by step five; hence six is the *smallest* global collapse index. Combining the two exhaustive partitions also yields \(\tau_B(X,Y)=6\) precisely when \(v>3/2\), equivalently \(Y>3b/2=-3B/2\).

## Verification
The accompanying standalone program `verify_capture.py` performs exact-rational first-hit and six-step composition checks for 16,353 prescribed rational test cases across five different negative parameter scales and extra boundary/outlier cases. It independently computes direct iterates and checks the partition formula. It covers all seven possible first-capture values and prints `CHECK_OK`. Run it using Python 3: `python3 verify_capture.py`. The finite tests are **not** claimed as proof of the all-real theorem; the exhaustive sign argument in Steps 1–4 establishes the universal statement.

## Relationship to prior work
Ohmori and Yamazaki [1, equations (1)–(3), discussion (i-a)–(i-c)] introduce exactly this map, prove that the negative and zero input regimes have a unique stable fixed point, and give a **seven-step upper bound** for initial states in their region II-2 (positive initial second coordinate, nonpositive first coordinate). They also discuss the associated excitable transient but do not state a sharp six-step global bound, the full first-hitting-time partition, or the horizontal threshold separating maximal transients. The result here makes those first-passage quantities exact for every negative input and every initial state. The contemporaneous Sel'kov-specific derivation [6, equations (13)–(14) and discussion (i-a)–(i-c)] repeats the same seven-step sufficient bound. The follow-up Poincaré-map study [2] assumes positive input and studies attractor basins there, not the present negative-input capture law. The later generalized family [5, §3.2] discusses negative-input excitable trajectories and their eventual sink capture, but does not give the exact uniform index or planar first-hitting-time strata at its special slice with equal coefficients two.

A published separate zero-input result [3] obtains the exact global nilpotence exponent of a **homogeneous** generalized map; its special case with coefficients two and two is six. The forcing term in the present negative-input map cannot be removed through that homogeneous theorem, and a coinciding number six does **not** imply the exact negative-input capture partition. Another reported result [4] concerns escape from the expanding branch for **positive** input and has a geometric tail; it does not cover the globally nilpotent negative-input dynamics.

## Limitations
These exact hitting-time statements are for \(B<0\) and the unsmoothed deterministic map only. They do not establish robustness to perturbations, physical time in the originating continuous biochemical models, an exact law for any selected random distribution of initial states, or priority over inaccessible/unindexed publications. A first-capture classification for the distinct homogeneous borderline input \(B=0\) is not asserted.

## References
1. S. Ohmori and Y. Yamazaki, *A simple model for ultradiscrete Hopf bifurcation*, arXiv:2103.16777v1, first public 31 March 2021, especially equations (1)–(3) and region II-2 discussion. https://arxiv.org/html/2103.16777v1
2. S. Ohmori and Y. Yamazaki, *Poincare Map Method for Limit Cycles in a Max-Plus Dynamical System*, arXiv:2204.00745v1, first public 2 April 2022, sections 2–4 (positive-input assumption). https://arxiv.org/html/2204.00745v1
3. *Sharp extinction and persistence at the homogeneous max-plus border collision*, published-finding corpus published research record `2026/10/11/SCOPE-sharp-extinction-and-persistence-at-the-homogeneous-max-plus-bor--a2b1d9a86864`, zero-input family. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-extinction-and-persistence-at-the-homogeneous-max-plus-bor--a2b1d9a86864
4. *Exact geometric first-exit law for the ultradiscrete Sel'kov map*, published-finding corpus published research record `2026/10/11/SCOPE-exact-geometric-first-exit-law-for-the-ultradiscrete-sel-kov-map--013f8b0ac9e5`, positive-input system. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-geometric-first-exit-law-for-the-ultradiscrete-sel-kov-map--013f8b0ac9e5
5. S. Ohmori and Y. Yamazaki, *A Generalization for Ultradiscrete Limit Cycles in a Certain Type of Max-Plus Dynamical Systems*, arXiv:2402.06230v1, first public 9 February 2024, especially section 3.2 (negative-input trajectories). https://arxiv.org/html/2402.06230v1
6. S. Ohmori and Y. Yamazaki, *Dynamical properties of max-plus equations obtained from tropically discretized Sel'kov model*, arXiv:2107.02435v1, first public 6 July 2021, discussion (i-a)–(i-c). https://arxiv.org/html/2107.02435v1
