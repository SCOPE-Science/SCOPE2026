# Perrin–transfer periodic-orbit census for cyclic Rule 3

## Finding
For each integer \(n\ge3\), let \(X_n=\{0,1\}^{\mathbb Z/n\mathbb Z}\), let \((Sx)_i=x_{i-1}\), and let the synchronous elementary Rule 3 map be
\[
 (F_nx)_i=(1-x_{i-1})(1-x_i).
\]
Define the integer matrices (rows and columns ordered \(00,01,10,11\))
\[
 U=\begin{pmatrix}1&1&0&0\\0&0&1&1\\1&0&0&0\\0&0&1&1\end{pmatrix},\qquad
 V=\begin{pmatrix}0&1&0&0\\0&0&1&0\\1&1&0&0\\0&0&0&0\end{pmatrix},
\]
and \(a_j=\operatorname{tr}(U^j)\), \(p_j=\operatorname{tr}(V^j)\) for positive integers \(j\). Thus \(a_j\) counts cyclic binary words avoiding the consecutive pattern \(101\), and \(p_j\) is the Perrin number (the number of maximal independent sets of a \(j\)-cycle for \(j\ge3\)); in particular \(a_1=2\), \(a_2=2\), \(p_1=0\), \(p_2=2\).

**Exact all-time periodic-point theorem.** For every \(n\ge3\) and \(m\ge1\), the number of states fixed by the \(m\)-fold Rule 3 update is
\[
 \Phi_n(m):=|\operatorname{Fix}(F_n^m)|=
 \begin{cases}
 a_{\gcd(n,m/2)},&m\text{ even},\\
 p_{\gcd(n,m)},&m\text{ odd}.
 \end{cases}
\]
The total number of already-periodic states is exactly \(a_n\); the remaining \(2^n-a_n\) states become periodic after **exactly one update**. Every eventual least period divides \(2n\). For each positive \(m\mid 2n\), the exact number of primitive temporal orbits of least period \(m\) is
\[
 \frac1m\sum_{d\mid m}\mu(m/d)\Phi_n(d),
\]
with zero orbits at other periods. In particular there are no fixed points, and precisely one primitive two-cycle (the all-zero/all-one pair). Every odd temporal fixed-point count is a Perrin number indexed by a greatest common divisor, an exact relationship between Rule 3 recurrence and maximal independent sets on a cycle.

The recurrent population grows as \(a_n\sim\lambda^n\), where \(\lambda\in(1,2)\) is the unique positive real root of \(\lambda^3-2\lambda^2+\lambda-1=0\); therefore the proportion of recurrent initial states tends to zero exponentially.

## Assumptions and scope
The sites form a **labelled, synchronous, periodic** binary ring, and Rule 3 is the one-sided two-input NOR rule above (the right neighbor is ignored). Only \(n\ge3\) is claimed as an ordinary elementary cellular-automaton ring; auxiliary traces at lengths one and two are defined by cyclic words, not by the simple-graph cycle convention. First-periodic-entry time is the least \(t\ge0\) for which \(F_n^t(x)\) is periodic. Primitive temporal orbits are distinct cycles of labelled configurations, not quotiented by spatial rotations. Statements apply to every integer \(m\ge1\) and every length \(n\ge3\).

## Proof
**1. A square-root-of-shift identity.** Boolean arithmetic gives
\[
 (F_n^2x)_i=x_{i-1}\lor(x_i\land x_{i-2}).
\]
Applying the NOR rule again and simplifying yields
\[
 (F_n^3x)_i=(1-x_{i-1})(1-x_{i-2})=(SF_nx)_i.
\]
Because \(F_n\) commutes with the spatial shift, \(F_n^{2k+1}=S^kF_n\) for all \(k\ge0\) and \(F_n^{2k}=S^{k-1}F_n^2\) for \(k\ge1\).

**2. Exact recurrent set.** Set \(R_n=\{y\in X_n:\text{no cyclic occurrence of }101\}\). The formula for \(F_n^2\) shows that \(F_n^2y=Sy\) precisely when \(y_i=y_{i-2}=1\) never occurs with \(y_{i-1}=0\), so precisely when \(y\in R_n\). For every \(y=F_nx\), the identity \(F_n^3=SF_n\) gives \(F_n^2y=Sy\), hence \(\operatorname{im}F_n\subseteq R_n\). Conversely, if \(y\in R_n\), then \(y=S^{-1}F_n^2y=F_n(S^{-1}F_ny)\). Thus \(\operatorname{im}F_n=R_n\). On this set \(F_n^2=S\), and since \(S^n=I\), \(F_n^{2n}=I\) on \(R_n\). Thus every image state is periodic, all others enter after exactly one update, and all periods divide \(2n\).

**3. Even temporal iterates.** Let \(m=2k\ge2\). A state fixed by \(F_n^{2k}\) is in \(R_n\), where \(F_n^{2k}=S^k\). Spatial fixed points of \(S^k\) repeat a word of length \(g=\gcd(n,k)\). Avoidance of cyclic \(101\) is exactly the same in this shorter word. Therefore \(\Phi_n(2k)=a_g\).

**4. Odd temporal iterates and maximal independent sets.** Let \(m\) be odd and let \(x=F_n^mx\). Then \(x\in R_n\), so \(S^mx=F_n^{2m}x=x\). Write \(g=\gcd(n,m)\), which is odd; \(x\) repeats a word on a \(g\)-site ring. On recurrent states of that ring, \(F_g^{2g}=I\), and since \(m/g\) is odd, \(F_n^mx=x\) is equivalent to \(F_g^gx=x\) on the repeating base word. For \(g=1\), Rule 3 interchanges both constant words, hence there are no fixed points. For \(g=2r+1\ge3\), the identity from step 1 gives the coordinate equations
\[
 x_i=(1-x_{i-r})(1-x_{i+r})\qquad (\bmod g).
\]
Since \(\gcd(r,g)=1\), the edges between indices differing by \(r\) form one \(g\)-cycle. The displayed equations say exactly that the sites labelled one form an independent *dominating* set, equivalently a maximal independent set, of that cycle. By the Perrin-cycle count, there are \(p_g\) such configurations. Hence \(\Phi_n(m)=p_g\).

**5. Trace and primitive-orbit formulas.** A closed length-\(j\) walk in the two-block de Bruijn transition graph for \(U\) corresponds bijectively to a cyclic length-\(j\) word avoiding \(101\); thus its trace counts \(a_j\). The same construction with the local equation \(x_i=(1-x_{i-1})(1-x_{i+1})\) yields \(V\), counting maximal independent sets and therefore Perrin numbers. The characteristic polynomials are
\[
 \det(zI-U)=z(z^3-2z^2+z-1),\qquad
 \det(zI-V)=z(z^3-z-1).
\]
In particular, \(a_1=a_2=2\), \(a_3=5\), and \(a_j=2a_{j-1}-a_{j-2}+a_{j-3}\) for \(j\ge4\); and \(p_0=3\), \(p_1=0\), \(p_2=2\), and \(p_j=p_{j-2}+p_{j-3}\) for \(j\ge3\). If \(E_n(m)\) is the number of states of *least* period \(m\), then \(\Phi_n(m)=\sum_{d\mid m}E_n(d)\). Möbius inversion gives the stated formula and division by \(m\) converts states to temporal orbits.

**6. Asymptotic.** The characteristic polynomial of \(U\) has a real root \(\lambda\in(1,2)\), and the other two nonzero roots have modulus strictly smaller than \(\lambda\) (by strict Perron–Frobenius theory on its irreducible nonzero component, or by the cubic). The trace formula gives \(a_n=\lambda^n+o(\lambda^n)\); dividing by \(2^n\) proves exponential scarcity of recurrent states.

## Verification
The standalone scripts `verify_rule3.py` and `verify_independent.py` use only Python's standard library. Run both with `python3 verify_rule3.py` and `python3 verify_independent.py` from this package. The first independently enumerates all \(2^n\) configurations for each \(3\le n\le14\), verifies image/forbidden-word equivalence, the cubic shift identity, and **204** predicted temporal fixed-point counts up to \(2n\) iterates. The second directly counts forbidden words and maximal independent sets for \(1\le n\le18\), checks both transfer traces and the Perrin recurrence, and checks nonnegative integral Möbius orbit populations summing to \(a_n\) for rings \(3\le n\le19\). Captured outputs are included. These tests are finite corroboration; the preceding proof establishes the unbounded quantifiers.

## Relationship to prior work
Wolfram's 1983 foundational paper introduced systematic elementary-cellular-automaton dynamics. Binder (1991) proves a rule-3 period-two global attractor under **fixed zero boundary conditions**; that setting does not cover periodic rings, where temporal periods can grow with circumference. Fukś (2003) studies preimage numbers, including Rule 3; his later online formula gives pointwise time iterates of Rule 3, from which the square-root-of-shift behavior follows. That pointwise solution is not claimed new. Bisdorff and Marichal (arXiv 2007) record the preexisting Perrin count of maximal independent sets of cycles; the Perrin sequence and its enumeration are also not claimed new. The present exact **even/odd gcd-dependent temporal fixed-point and primitive-orbit census**, built by identifying *odd temporal fixed points* with maximal independent sets, is the assessed contribution. Špale and Stehlík (2025) explicitly illustrate Rule-3 two-profile spatial translation but study reaction–diffusion automata rather than this periodic-ring census.

## Limitations
This is a theorem about **one specified synchronous elementary rule**, not a classification of all one-sided binary rules or all spatial boundary conditions. The known pointwise Rule-3 solution supplies significant antecedent information; the enumerative linkage must be distinguished from that antecedent in any priority assessment. No claim is made about independence of verification. Relevant bibliographic searches did not identify a published equivalent all-time Perrin/transfer temporal-orbit census, but an unindexed or differently phrased prior result remains possible. No experimental or finite computation substitutes for the proof.

## References
1. S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics **55**, 601–644 (first published 1983-07-01), DOI `10.1103/RevModPhys.55.601`.
2. P.-M. Binder, *Proof that a cellular automaton has a period-two global attractor*, Journal of Physics A **24**, 1677–1679 (1991), DOI `10.1088/0305-4470/24/7/036`.
3. H. Fukś, *Sequences of Preimages in Elementary Cellular Automata*, Complex Systems **14**, 29–43 (2003), DOI `10.25088/ComplexSystems.14.1.29`; reprint arXiv `1305.6533`.
4. H. Fukś, *Deterministic solution formulae for elementary CA rules*, author-maintained reference page: https://lie.ac.brocku.ca/~hfuks/solvableca.html (Rule 3 formula; page undated).
5. R. Bisdorff and J.-L. Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph*, arXiv `math/0701647` (initially public 2007-01-23).
6. D. Špale and P. Stehlík, *Traveling waves in bistable reaction-diffusion cellular automata*, DOI `10.3934/dcdsb.2025158` (early access 2025-10-09), especially Figure 3.
