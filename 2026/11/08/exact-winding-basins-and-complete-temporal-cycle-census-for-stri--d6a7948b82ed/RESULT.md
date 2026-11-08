# Exact winding basins and complete temporal-cycle census for striped cyclic-dominance tori

## Finding

For every integer \(L\ge4\), consider the three-color cyclic successor automaton on the periodic \(L\times L\) square lattice, with synchronous Moore-radius-one updates and the requirement of at least three of the eight neighbors having the successor color. Its invariant sector of configurations constant along every row has a complete explicit dynamical classification.

Write the row colors as \(s=(s_0,\ldots,s_{L-1})\in(\mathbb Z/3\mathbb Z)^L\). Let \(d_i\in\{-1,0,1\}\) be the unique signed representative of \(s_{i+1}-s_i\pmod3\) (indices modulo \(L\)); define the integer winding \(w(s)=\frac13\sum_i d_i\). Every row-constant initial condition eventually becomes either spatially uniform (exactly when \(w=0\)) or a rigidly translating wave with precisely \(3|w|\) directed color walls (when \(w\ne0\)). Positive winding travels one row per step in one direction, and negative winding in the opposite direction.

The number of initial row-constant states whose eventual dynamics has winding \(w\) is exactly

\[
B_{L,w}=3[z^{3w}](z^{-1}+1+z)^L,
\qquad -\lfloor L/3\rfloor\le w\le\lfloor L/3\rfloor.
\]

Set \(A_m=\sum_{k=0}^{\lfloor m/3\rfloor}\binom{m}{3k}=\bigl(2^m+2\cos(m\pi/3)\bigr)/3\). The **complete number of recurrent row-constant states** is

\[
R_L=6A_L-3=2^{L+1}+4\cos(\pi L/3)-3.
\]

There are exactly three fixed temporal cycles. For each divisor \(p>1\) of \(L\), the number of distinct primitive temporal cycles of exact period \(p\), with configurations *not* identified under lattice translation or color rotation, is

\[
C_{L,p}=\frac6p\sum_{d\mid p}\mu(p/d)A_d.
\]

No other primitive temporal periods occur in the row-constant sector. In particular \(C_{L,L}\sim2^{L+1}/L\) as \(L\to\infty\), so this sector supports exponentially many exact traveling-wave cycles, although its recurrent states constitute an exponentially vanishing proportion of all \(3^L\) row-constant states. Higher winding generates waves with six, nine, or more fronts; they are not restricted to three bands.

## Assumptions and scope

The lattice has indices \((i,j)\in\mathbb Z_L^2\) with \(L\ge4\), ensuring all eight radius-one Moore neighbors are distinct. A site with color \(c\in\{0,1,2\}\) changes to \(c+1\pmod3\) if at least three of those neighbors have this successor color; otherwise it keeps \(c\). The theorem concerns **only the invariant row-constant sector** \(s_{i,j}=s_i\); it does not classify all two-dimensional configurations or their basins. A periodic orbit is counted once per cycle with labeled lattice sites and colors; cycles related by symmetry are counted separately unless literally the same orbit.

When a full row has color \(s_i\), each adjacent row with successor color contributes three successor neighbors; the remaining two neighbors belong to its own row. Thus the exact induced rule is

\[
(Fs)_i=s_i+u_i\pmod3,\qquad
u_i=\mathbf1\{s_{i-1}=s_i+1\pmod3\ \text{or}\ s_{i+1}=s_i+1\pmod3\}.
\]

## Proof

**1. Integer wall identity and winding conservation.** For the signed color differences \(d_i\), a successor on the right is equivalent to \(d_i=1\), while a successor on the left is equivalent to \(d_{i-1}=-1\). Consequently

\[
u_i=\mathbf1\{d_i=1\ \text{or}\ d_{i-1}=-1\}.
\]

The update satisfies the exact *integer*, not merely mod-three, identity

\[
d_i'=d_i+u_{i+1}-u_i.
\]

Indeed if \(d_i=1\) then \(u_i=1\), so the right side is in \(\{0,1\}\); if \(d_i=-1\) then \(u_{i+1}=1\), so it lies in \(\{-1,0\}\); if \(d_i=0\), the right side is already in \(\{-1,0,1\}\). These are the correct signed representatives of the updated color differences. Summation over the ring telescopes, proving \(w(Fs)=w(s)\).

**2. Monotone walls and exhaustion of opposite directions.** Let \(P\) and \(M\) be the sets of indices with \(d_i=1\) and \(d_i=-1\), respectively. The local identity yields precisely

\[
\begin{aligned}
d_i'=1&\iff d_{i+1}=1\ \text{and}\
[d_i=1\ \text{or}\ (d_i=0\ \text{and}\ d_{i-1}\ne-1)],\\
d_i'=-1&\iff d_{i-1}=-1\ \text{and}\
[d_i=-1\ \text{or}\ (d_i=0\ \text{and}\ d_{i+1}\ne1)].
\end{aligned}
\]

Thus each positive wall can only shift one position to the left or disappear; each negative wall can only shift one position to the right or disappear. Both wall counts are nonincreasing and their difference is \(3w\). Suppose a periodic trajectory retained both signs. Its wall counts must be constant, so all positive walls shift left by one and all negative walls shift right by one on every step. Fix one initial positive and one initial negative wall with indices \(a,b\). Their relative index after \(t\) steps is \(a-b-2t\pmod L\). Among residues \(1\) and \(2\), at least one lies in this arithmetic progression (the step has greatest common divisor at most two with \(L\)). At that time a negative wall is either directly to the left of a positive wall or separated from it by one edge. For separation one, the positive wall has a negative wall immediately to its left and cannot execute its required left shift. For separation two, its intervening edge is negative, zero, or positive: in the first case the positive wall is blocked; in the second it is blocked by the negative wall across the zero edge; and in the third the intervening positive wall is blocked by the negative wall. In each case at least one positive wall fails to shift, forcing a wall disappearance at the next update. This contradicts the assumed constant wall counts. All periodic states therefore have walls of only one sign. Since the state space is finite, every initial state eventually reaches such a periodic state.

**3. Rigidity of the recurrent waves.** If every \(d_i\in\{0,1\}\), then \(u_i=d_i\), and \((Fs)_i=s_{i+1}\). If every \(d_i\in\{0,-1\}\), then \(u_i=\mathbf1\{d_{i-1}=-1\}\), and \((Fs)_i=s_{i-1}\). Such words shift rigidly and hence are periodic; those with no walls are exactly the three spatially uniform fixed states. Conversely Step 2 excludes every other recurrent state. Since a periodic color word has \(\sum_i d_i\in3\mathbb Z\), a pure-sign recurrent word with winding \(w\ne0\) has exactly \(3|w|\) walls. This also proves the claimed dependence of the attracting family on initial winding.

**4. Winding-basin coefficient formula.** Every signed wall vector \(d\in\{-1,0,1\}^L\) with \(\sum_i d_i\in3\mathbb Z\) gives exactly three color words: fix \(s_0\) freely and integrate the differences around the ring. These are all row words, with no repetitions. The number at winding \(w\) is therefore \(3[z^{3w}](z^{-1}+1+z)^L\). Since every trajectory becomes pure and conserves winding, this counts exactly the initial states converging to the uniform set (\(w=0\)) or to the traveling-wave set with \(3|w|\) walls (\(w\ne0\)). It does not subdivide the basin among individual cycles of fixed winding.

**5. Exact periodic-state and orbit counts.** A pure-positive word is specified by its first color (three choices) and a binary wall vector with \(j\) ones, where closure requires \(3\mid j\). It follows that there are \(3A_L\) pure-positive words, and also \(3A_L\) pure-negative words. Their intersection consists only of the three uniform states. Inclusion-exclusion gives \(R_L=6A_L-3\). The roots-of-unity filter gives \(3A_m=2^m+2\cos(m\pi/3)\).

For a fixed \(p\mid L\), a pure-positive word whose spatial period divides \(p\) is a repeat of one of the \(3A_p\) valid length-\(p\) words. Möbius inversion gives \(3\sum_{d\mid p}\mu(p/d)A_d\) pure-positive words with *least* spatial period \(p\). For \(p>1\), none is pure-negative, so the two directional families contribute twice this number. The update is a unit shift, hence least temporal and spatial periods agree. Division by \(p\) counts cycles and proves the formula; the three uniform states account for period one. Finally \(A_L=2^L/3+O(1)\), while all proper divisors of \(L\) are at most \(L/2\). The contribution from proper divisors in the Möbius sum is \(O(L2^{L/2})\), proving \(C_{L,L}\sim2^{L+1}/L\).

## Verification

A standalone standard-library checker, `verify.py`, is supplied. It exhaustively reconstructs the directed graph of all \(3^L\) stripe words for every \(4\le L\le10\), checks the wall conservation and wall-count inequalities edge by edge, and confirms the predicted exact period census, recurrent-state count, and winding-sector counts. For \(4\le L\le6\) it also independently implements the full eight-neighbor two-dimensional update on each stripe state and checks equality with the reduced rule. Exact finite roots-of-unity identities are checked for \(1\le L\le100\). A seven-row, six-wall period-seven example is \((0,1,2,0,1,2,2)\). These finite tests are corroboration; Steps 1–5 supply the proof for all admissible \(L\).

For example, at \(L=10\), there are \(2043\) recurrent stripe states, comprising three fixed cycles, twelve cycles of primitive period five, and 198 cycles of primitive period ten. Among all \(59049\) initial stripe words, exactly \(26859\) have zero winding and therefore eventually become uniform.

## Relationship to prior work

Muñoz and Nuño (2026, arXiv:2610.37990v1, model Sec. II and traveling-wave discussion Sec. V.4) define and sample the same threshold-three torus automaton, report symmetry-quotient periods, and describe the observed three-band waves. Their sampled-wave catalogue and general divisibility laws do not give a complete classification of all periodic stripe states, all-length exact cycle counts, or initial-winding basin sizes. Multi-front exact waves need not appear in a finite sampled catalogue; the theorem is about all mathematically admissible stripe states.

Hellouin de Menibus and Le Borgne (2019, arXiv:1903.12622, introduction and Sec. 1.2) explicitly give the same one-dimensional successor rule and the classical ballistic wall-annihilation mechanism on the bi-infinite line. The particle mechanism in Step 2 is **not claimed to be new**. Their principal results concern Bernoulli initial laws and asymptotic behavior on the infinite line rather than this exact labeled finite-ring temporal-cycle census and winding-resolved basin formula.

Jen (1988, DOI:10.1007/BF01221109) gives general matrix/recurrence methods for finite-cylinder cellular-automaton cycles, and Fisch, Gravner and Griffeath (1991/1993, arXiv:patt-sol/9304001) establish traveling-band criteria in excitable cellular automata. These are important structural precursors. The inspected available statements do not supply the closed formulas here; general computability of periodic points is not by itself a statement of the exact counts. The full text of Jen's article and of the older band-test paper was not completely inspected, so historical priority remains subject to that risk.

## Limitations

The result covers only configurations constant along one lattice axis for the specified threshold-three, radius-one three-color rule. It does not describe arbitrary two-dimensional recurrent states, their full-space basins, or the subdivision of a winding sector among individual cycles. The direction/winding sector counts are counts of labeled initial stripe configurations, not random full-torus outcomes. Earlier particle-annihilation theory and general finite-cellular-automaton counting methods are acknowledged; the novelty assessment is based on the inspected mathematical statements and accessible prior records, not exhaustive priority certification.

## References

1. F. J. Muñoz and J. C. Nuño, *Symmetry-resolved periods in a cyclic-dominance automaton: separating intrinsic from lattice-induced periodicity*, arXiv:2610.37990v1 (first public 2026-10-27), https://arxiv.org/html/2610.37990v1.
2. B. Hellouin de Menibus and Y. Le Borgne, *Asymptotic behaviour of the one-dimensional “rock-paper-scissors” cyclic cellular automaton*, arXiv:1903.12622 (2019), https://arxiv.org/pdf/1903.12622.
3. E. Jen, *Cylindrical cellular automata*, Communications in Mathematical Physics 118 (1988), 569–590, DOI:10.1007/BF01221109.
4. R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing 1 (1991), 23–39; arXiv:patt-sol/9304001 (1993 preprint).
