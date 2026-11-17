# Exact one-sweep reachability and image entropy for asynchronous Rule 184

## Finding

For every integer \(n\ge 3\), consider the labelled binary ring \(\mathbb Z/n\mathbb Z\). In each sweep, update sites \(0,1,\ldots,n-1\) once, immediately replacing the current bit by elementary cellular-automaton Rule 184,
\[
f(\ell,c,r)= (\ell\wedge\neg c)\vee(c\wedge r).
\]
Let \(S_n\) be the resulting full-sweep map and \(I_n=|S_n(\{0,1\}^n)|\). A word \(y=(y_0,\ldots,y_{n-1})\) belongs to the image **if and only if** all three tests hold:

1. The cyclic word \(y\) contains no cyclic occurrence of \(101\); that is, \((y_i,y_{i+1},y_{i+2})\ne(1,0,1)\) for every \(i\in\mathbb Z/n\mathbb Z\).
2. \(y_{n-1}\le y_0\).
3. \((y_0,y_1,y_{n-2},y_{n-1})\ne(0,1,1,0)\).

The exact number of distinct one-sweep outputs has generating function
\[
\boxed{\sum_{n\ge3}I_nz^n=\frac{z^3(3+z+2z^2)}{1-2z+z^2-z^3}.}
\]
In particular,
\[
(I_3,I_4,I_5,I_6,I_7,I_8,I_9,I_{10})=(3,7,13,22,38,67,118,207),
\]
and \(I_n=2I_{n-1}-I_{n-2}+I_{n-3}\) for every \(n\ge6\), with the displayed initial values. (The recurrence also holds at \(n=5\) if formally extended with \(I_2=2\).)
The image growth base is the unique real root greater than one of
\[
\lambda^3-2\lambda^2+\lambda-1=0,
\qquad\lambda=1.75487766624669\ldots.
\]
Thus the asymptotic one-sweep image entropy is \(\log\lambda=0.56239914864592\ldots\) nats per site, equivalently \(0.81137046275165\ldots\) bits per site.

## Assumptions and scope

The update order is the fixed **left-to-right simple sequential sweep** \(0,1,\ldots,n-1\). At site \(0\), both neighbors still have their initial values; at internal sites \(1\le i\le n-2\), the left neighbor has already been updated and the right neighbor has not; at site \(n-1\), both neighbors have already been updated. The output coordinates remain labelled; rotation of a word is not a change to the update order. All statements concern **one** sweep, not the eventual periodic set, all possible scan orders, or the synchronous Rule-184 map. In particular, the familiar synchronous number-conservation law need not survive the sweep: on any \(n\ge3\), the single initial one at site \(0\) can disappear during the sweep.

## Proof

Write the input as \(x=(x_0,\ldots,x_{n-1})\), and its sweep output as \(y\). By the prescribed ordering, the defining equations are
\[
\begin{aligned}
y_0&=f(x_{n-1},x_0,x_1),\\
y_i&=f(y_{i-1},x_i,x_{i+1})\quad(1\le i\le n-2),\\
y_{n-1}&=f(y_{n-2},x_{n-1},y_0).
\end{aligned}
\tag{1}
\]
As \(f(a,0,b)=a\) and \(f(a,1,b)=b\), each site simply selects a neighbor. Whenever an internal output changes from \(y_{i-1}=1\) to \(y_i=0\), equation (1) forces \(x_i=1\) and \(x_{i+1}=0\), so the next output is \(y_{i+1}=y_i=0\) (including the last-site equation if \(i=n-2\)). Hence no output can contain \(101\) with a center at sites \(1,\ldots,n-2\). At the last site, \(y_{n-2}=1\), \(y_{n-1}=0\), \(y_0=1\) is impossible because either choice of \(x_{n-1}\) produces one. This excludes the crossing pattern centered at \(n-1\).

If \(y_0=0\) and \(y_{n-1}=1\), the final equation requires \(x_{n-1}=0\) and \(y_{n-2}=1\). Working backward, the internal equations force successively \(x_{n-2}=0,y_{n-3}=1\), then \(x_{n-3}=0,y_{n-4}=1\), and so on, until \(x_1=0,y_0=1\), a contradiction. This proves test 2 and also excludes \(101\) centered at site \(0\). Finally, if \(y_0=0,y_1=1\), the first internal equation forces \(x_1=1\). The site-0 equation then forces \(x_0=x_{n-1}=0\). If also \(y_{n-2}=1,y_{n-1}=0\), the last equation would give \(y_{n-1}=y_{n-2}=1\); contradiction. Thus all three tests are necessary.

For sufficiency, take a target \(y\) satisfying the tests, and set
\[
x_i=y_{i-1}\vee y_i\qquad(1\le i\le n-2).
\tag{2}
\]
Choose the two remaining input bits according to the exhaustive cases:
\[
(x_0,x_{n-1})=
\begin{cases}
(1,y_{n-1}),&y_0=1,\\
(0,0),&y_0=0,\ y_{n-2}=0,\\
(1,1),&y_0=0,\ y_{n-2}=1.
\end{cases}
\tag{3}
\]
The third case necessarily has \(y_1=0\) by test 3, and in the second and third cases \(y_{n-1}=0\) by test 2. For an internal site with \(x_i=0\), equation (2) gives \(y_{i-1}=y_i=0\), so its output is correct. If \(x_i=1\), its output is \(x_{i+1}\); equation (2) makes that bit equal to \(y_i\), except potentially when \(y_{i-1}=1,y_i=0,y_{i+1}=1\), which test 1 forbids. At the final internal site, the same check uses the boundary choice (3); the only potential conflict \(y_{n-3}=1,y_{n-2}=0,y_{n-1}=1\) is also excluded by test 1. Direct substitution of the three cases of (3) into the first and final equations of (1) verifies both boundary outputs: in the first case, \(y_{n-1}=0\) implies \(y_{n-2}=0\) by cyclic \(101\)-avoidance, and in the third case \(y_1=0\) is already known. Thus (2)–(3) provide an explicit predecessor for every permitted \(y\), proving sufficiency.

To count the image, use pair states in the order \(00,01,10,11\) and the four-state adjacency matrix for cyclic avoidance of \(101\):
\[
T=\begin{pmatrix}1&1&0&0\\0&0&1&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
\]
For \(n\ge3\), \(\operatorname{tr}(T^n)\) counts labelled cyclic \(101\)-free words. The words violating test 2 are counted by \((T^n)_{10,10}\), using the pair \((y_{n-1},y_0)=(1,0)\). Among the remaining words, those violating test 3 are counted by \((T^{n-2})_{01,10}\). The two subtraction classes are disjoint. Therefore
\[
I_n=\operatorname{tr}(T^n)-(T^n)_{10,10}-(T^{n-2})_{01,10}.
\tag{4}
\]
Set \(R(z)=(\mathrm{Id}-zT)^{-1}\). Matrix geometric-series identities and the values of the formal coefficients for lengths one and two give
\[
\begin{aligned}
\sum_{n\ge3}I_nz^n={}&\operatorname{tr}(zTR(z))-(R(z)_{10,10}-1)\\
&-z^2R(z)_{01,10}-2z-2z^2\\
={}&\frac{z^3(3+z+2z^2)}{1-2z+z^2-z^3}.
\end{aligned}
\]
Here the formula with the subtractions also defines the auxiliary length-one and length-two coefficients to be \(2\) and \(2\); no physical one-cell or two-cell dynamics is needed for the theorem. Since \(\det(\mathrm{Id}-zT)=1-2z+z^2-z^3\), the recurrence follows. The matrix \(T\) is primitive (it is strongly connected with a self-loop). Its Perron root is the stated \(\lambda\); the rational numerator is strictly positive at the corresponding positive pole \(z=1/\lambda\), so there is no cancellation. This proves the exponential growth and entropy claims.

## Verification

The self-contained source `checks/sweep184.cpp` independently evaluates all \(2^n\) inputs and all \(2^n\) proposed outputs for every \(3\le n\le18\), checks the three language tests and verifies the explicit predecessor construction at every reachable output. `checks/transfer.py` independently constructs the four-state transfer and checks (4) and the recurrence through \(n=34\). `checks/symbolic.py` checks the exact determinant and the rational generating function using symbolic integer arithmetic. Recorded outputs are included alongside the source programs. These finite checks are corroboration; the preceding algebraic proof, not finite enumeration, establishes the all-size theorem.

## Relationship to prior work

Macauley, McCammond and Mortveit (arXiv:0707.2360, first publicly posted 2007-07-16) study cyclic asynchronous elementary cellular automata. Their Proposition 6.3 treats Rule 184 as an update-order-independent system in the **eventual periodic-state** sense; it does not provide a one-sweep image language or its growth rate. Hazari and Das (2014) analyze number conservation across asynchronous update patterns and give examples for Rule 184, but do not give this fixed-sweep reachability criterion or exact all-length image count. Donoso-Leiva and collaborators (arXiv:2505.10645) analyze cycle lengths under several update modes, including sequential Rule 184, rather than one-sweep image reachability. Previously published cyclic Rule-184 image results concerning the forbidden word \(1100\) are for **synchronous simultaneous** updates, not the in-place sweep defined here. The present image is neither that cyclic language nor a corollary of its count: its three boundary-sensitive tests depend on the labelled scan origin.

## Limitations

The classification uses a specific scan order and does not assert a formula for arbitrary site permutations, multiple sweeps, inverse-fiber sizes or the full attractor basins. Nor does it transfer the synchronous conservation law to asynchronous dynamics. Results on unindexed or inaccessible historical literature may affect priority, although the compared accessible works do not imply the theorem. No independent mathematical review is asserted.

## References

1. M. Macauley, J. McCammond and H. S. Mortveit, *Order Independence in Asynchronous Cellular Automata*, arXiv:0707.2360, version 1 dated 2007-07-16, https://arxiv.org/abs/0707.2360 (see Proposition 6.3 in later full text).
2. R. Hazari and S. Das, *Number Conservation Property of Elementary Cellular Automata under Asynchronous Update*, *Complex Systems* 23 (2014), 177–195, https://doi.org/10.25088/ComplexSystems.23.2.177.
3. I. Donoso-Leiva, E. Goles, M. Ríos-Wilson and S. Sené, *Impact of (a)Synchronism on ECA: Towards a New Classification*, arXiv:2505.10645 (2025), https://arxiv.org/abs/2505.10645.
4. Published record *Exact one-step reachability, inversion, and density spectrum of the cyclic traffic automaton*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-one-step-reachability-inversion-and-density-spectrum-of-th--5a87e3038c99 (synchronous Rule 184, comparison only).
