# Perron–Lucas and Fibonacci laws for periodic images of elementary Rule 126

## Finding

For every integer \(n\ge1\), let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be Wolfram Rule 126 on indexed periodic rings, and set \(a_n=|\operatorname{im}F_n|\). Set \(a_0=1\) solely for generating-function notation. Then

\[
\sum_{n\ge0}a_nz^n=\frac{P(z)}{Q(z)},
\]
where
\[
P(z)=1-3z+4z^2-5z^3+6z^4-4z^5+z^6-2z^7+2z^8-z^9+z^{10}+z^{11}+z^{12},
\]
\[
Q(z)=1-4z+6z^2-5z^3+z^4+5z^5-7z^6+6z^7-2z^8-z^9+z^{10}-z^{11}.
\]

A shorter exact formula uses \(R_0=3,R_1=2,R_2=2\), \(R_n=2R_{n-1}-R_{n-2}+R_{n-3}\) for \(n\ge3\), and the Lucas numbers \(L_0=2,L_1=1,L_n=L_{n-1}+L_{n-2}\). For every \(n\ge1\),

\[
 a_n=R_n-\frac{L_n}2+\cos\frac{n\pi}3-\cos\frac{n\pi}2+\mathbf{1}_{2\mid n}-\mathbf{1}_{n=1}.
\]

The first counts, at lengths \(1\) through \(12\), are \(1,2,2,6,12,23,37,66,119,217,387,693\). Writing \(\lambda\) for the unique real root greater than one of \(t^3-2t^2+t-1=0\), and \(\varphi=(1+\sqrt5)/2\), this gives the sharp two-term asymptotic
\[
a_n=\lambda^n-\frac12\varphi^n+O(1),\quad \lambda=1.75487766624669\ldots,\quad \log_2\lambda=0.81137046275\ldots.
\]

## Assumptions and scope

A configuration is a labeled binary vector, not an orbit under cyclic rotation or complementation. Indices lie in \(\mathbb Z/n\mathbb Z\), including the repeated-neighbor rings of lengths one and two. The rule is exactly
\[
(F_n(x))_i=f(x_{i-1},x_i,x_{i+1}),\qquad f(a,b,c)=\mathbf{1}_{1\le a+b+c\le2}.
\]
In Wolfram's triple ordering this is rule \(126=01111110_2\). Only one synchronous time step is counted. The entropy above describes the exponential growth of distinct one-step *periodic images* as ring length grows, not the long-time trajectory entropy of an individual configuration.

## Proof

**1. Labeled predecessor relation.** Name four pair states \(00,01,10,11\), indexed \(0,1,2,3\). For each output label \(y\in\{0,1\}\), the labeled edge \((a,b)\to(b,c)\) is present exactly when \(f(a,b,c)=y\). Represent an edge relation by the tuple of four four-bit outgoing row masks. The two relations, in that order, are
\[
 B_0=(1,0,0,8),\qquad B_1=(2,12,3,4).
\]
For any cyclic output \(y\), a predecessor exists if and only if the Boolean product of its labeled relations has a diagonal entry equal to one: a closed walk is precisely the sequence of overlapping predecessor pairs. For rings of lengths one and two the same closed-walk condition applies without exception.

**2. Finite exact-state reduction.** Starting with the identity relation \((1,2,4,8)\), close under right multiplication by \(B_0,B_1\). There are exactly \(45\) reachable Boolean relations. Let \(M\) be the \(45\)-state directed edge-count matrix, with one transition for each label, and let \(v\) be the vector marking relations with any diagonal entry. If \(e\) selects the identity, then
\[
a_n=e^\mathsf T M^n v\qquad(n\ge0),
\]
where the artificial zero-length value is one. The provided ordinary Python program reconstructs all states and transitions from the two displayed generators.

**3. Annihilating the entire transfer sequence.** Expand \(Q(z)=\sum_{j=0}^{11}q_jz^j\) with
\[
(q_0,\ldots,q_{11})=(1,-4,6,-5,1,5,-7,6,-2,-1,1,-1).
\]
Set \(V_k=M^kv\) and \(w=\sum_{j=0}^{11}q_jV_{11-j}\). Exact forty-five-coordinate integer arithmetic gives the exceptionally small supports
\[
w=e_0+e_2,\qquad Mw=e_0,\qquad M^2w=0,
\]
where state 0 is the identity relation and state 2 is the relation \((2,12,3,4)\) in breadth-first state order. Thus every coefficient of \(Q(z)\sum_{n\ge0}a_nz^n\) of degree at least thirteen is zero, without invoking a guessed finite-prefix recurrence. Direct multiplication of the first thirteen transfer values gives the displayed degree-twelve polynomial \(P(z)\); therefore the rational identity is proved for all lengths.

**4. Closed form and asymptotics.** Algebraic partial fractions give
\[
\frac{P(z)}{Q(z)}=-z-2+\frac{3-4z+z^2}{1-2z+z^2-z^3}-\frac{2-z}{2(1-z-z^2)}+\frac{2-z}{2(1-z+z^2)}-\frac1{1+z^2}+\frac1{2(1+z)}+\frac1{2(1-z)}.
\]
The first rational fraction after the polynomial is the root-power sum for \(t^3-2t^2+t-1\), and the next is minus half the Lucas generating function. The other summands are periodic sequences with periods dividing twelve; the polynomial corrects just lengths zero and one. This proves the displayed closed formula. The other two cubic roots have absolute value less than one, whereas the Fibonacci secondary root has modulus less than one. The displayed sharp two-term asymptotic follows directly.

## Verification

Run `python3 verify.py` with Python 3 (standard library only). It independently constructs all \(45\) reachable Boolean relations from the specified local rule, verifies the complete vector-annihilation identity \(M^2w=0\), verifies every numerator coefficient, exhaustively compares all periodic inputs for each length from 1 through 12, and checks the rational recurrence against independent transfer counts through length 79. The actual replay prints `VERIFY_OK states=45, vector_annihilation=M^2, brute=1..12, recurrence=0..79`.

## Relationship to prior work

Wolfram's historical work establishes elementary Rule 126 and studies its observed evolutions, including random and special initial conditions; these are not the one-step images of *every* indexed periodic input. MathWorld's Rule 126 entry and its OEIS-linked literature concern specific seed evolutions. The closely titled Macfarlane (2016) generating-function work is identified by OEIS A267365 and A071051 as treating sequences along single-seed cellular automaton evolutions, not the periodic image-cardinality sequence here; its PostScript full text could not be inspected directly. Schreiber's 2007 Garden-of-Eden demonstration visualizes finite periodic unreachable states; it does not provide the present all-length root-power law on the accessible page. Kari and Taati (2015) provide general entropy and surjectivity theory, not a Rule 126 counting formula. The Boolean relation and finite-state transfer method is standard; novelty is sought only for the specific all-length closed form and its exact secondary asymptotic.

## Limitations

The result is for one elementary rule and one synchronous update on indexed periodic binary rings. It gives neither individual-output predecessor multiplicities nor the time-iterated attractor distribution. Only finite state construction and exact integer identities prove the all-length claims; numerical brute-force checks by themselves do not. The closest historical priority risk is an unindexed equivalent formula or a passage in the inaccessible Macfarlane PostScript; the present comparison does not assert a complete historical search. Independent validation has not been performed.

## References

- Stephen Wolfram, *A New Kind of Science* (2002), pages 55, 226 and 267, published May 14, 2002. https://www.wolframscience.com/nks/p55--more-cellular-automata/ ; https://www.wolframscience.com/nks/p226--the-emergence-of-order/ ; https://wolframscience.com/nks/p267--special-initial-conditions/
- Eric W. Weisstein, “Rule 126,” MathWorld. https://mathworld.wolfram.com/Rule126.html
- A. J. Macfarlane, “Generating Functions for Integer Sequences Defined by the Evolution of Cellular Automata with Even Rule Numbers,” 2016. https://www.damtp.cam.ac.uk/user/ajm25/Papers2016/GFsForCAsOfEvenRuleNo.ps
- OEIS A267365, single-seed Rule 126 generations, mentioning Macfarlane's Fig. 3. https://oeis.org/A267365
- Michael Schreiber, “Garden of Eden States,” Wolfram Demonstrations Project (2007). https://demonstrations.wolfram.com/GardenOfEdenStates/
- Jarkko Kari and Siamak Taati, “Statistical Mechanics of Surjective Cellular Automata,” *Journal of Statistical Physics* 160 (2015), 1198–1243. https://link.springer.com/article/10.1007/s10955-015-1281-2
