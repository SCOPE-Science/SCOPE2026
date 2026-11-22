# Exact ternary residue census and a sharp bias for central quadrinomial coefficients

## Finding

Write \(P(x)=1+x+x^2+x^3\) and let the **central quadrinomial coefficient** be
\[
Q_n=[x^{\lfloor 3n/2\rfloor}]P(x)^n \quad(n\ge0).
\]
For \(r\in\{0,1,2\}\) and \(L\ge0\), define
\[
N_r(L)=\#\{0\le n<3^L:Q_n\equiv r\pmod3\},\qquad
S_L=N_1(L)+N_2(L),\quad B_L=N_1(L)-N_2(L).
\]
Then for every nonnegative integer \(L\),
\[
\boxed{\sum_{L\ge0}S_Lz^L=\frac1{1-3z+z^2},\qquad
\sum_{L\ge0}B_Lz^L=\frac{1+3z+2z^2}{1-2z^2-3z^3}.}
\]
Consequently, if \(F_0=0,F_1=1,F_{m+2}=F_{m+1}+F_m\),
\[
\boxed{N_0(L)=3^L-F_{2L+2},\qquad
N_1(L)=\frac{F_{2L+2}+B_L}{2},\quad
N_2(L)=\frac{F_{2L+2}-B_L}{2}.}
\]
Here \(B_0=1,B_1=3,B_2=4\) and \(B_{L+3}=2B_{L+1}+3B_L\). In particular \(B_L>0\) for all \(L\ge0\). Its exact exponential order is \(B_L=\Theta(\rho^L)\), where \(\rho=1.8932891963\ldots\) is the positive root of \(t^3-2t-3\). The support has order \(\big((3+\sqrt5)/2\big)^L\), so among nonzero values the two unit residues are asymptotically equally frequent, with an explicitly quantified secondary bias. All three classes occur for \(L\ge2\).

## Assumptions and scope

The coefficient is that of \(x^{\lfloor3n/2\rfloor}\), not an arbitrary quadrinomial triangle entry. Its two central coefficients are equal when \(n\) is odd by symmetry. All congruences and counts in this note are for the prime modulus \(3\), complete index blocks \(0\le n<3^L\), and \(L\) ranging over **every** nonnegative integer. The claims do not assert a formula for every arbitrary cutoff \(X\), and they do not treat higher powers of three.

## Proof

**1. Ternary-digit coefficient transfer.** Write \(n=\sum_{i=0}^{L-1}d_i3^i\), with \(d_i\in\{0,1,2\}\) and allow leading zeros. Put \(\epsilon=n\bmod2\); since \(3\) is odd, \(\epsilon\equiv\sum_i d_i\pmod2\). Over \(\mathbf F_3[x]\), the Frobenius identity gives
\[
P(x)^n=\prod_{i=0}^{L-1}P(x^{3^i})^{d_i}.
\]
Let \(c_{d,j}=[x^j]P(x)^d\pmod3\). The three coefficient lists for \(d=0,1,2\), before reduction, are
\[
(1),\qquad(1,1,1,1),\qquad(1,2,3,4,3,2,1).
\]
Because \(2\lfloor3n/2\rfloor=3n-\epsilon\), a selected tuple of local exponents \(j_i\) contributes precisely to the central coefficient when
\[
\epsilon+\sum_{i=0}^{L-1}(2j_i-3d_i)3^i=0.
\]
Introduce carries \(r_0=\epsilon\), \(r_{i+1}=(r_i+2j_i-3d_i)/3\), admitting only integral transitions, and demand \(r_L=0\). By induction \(-2\le r_i\le2\) for every contributing path: if \(-2\le r_i\le2\), then \(-8\le r_i+2j_i-3d_i\le8\), so an integral quotient has absolute value at most two. Thus a five-coordinate vector \(v=(v_{-2},\dots,v_2)\in\mathbf F_3^5\) holds the total path weights at the five carries. The exact transition for a digit \(d\) is
\[
(T_dv)_s=\sum_{r=-2}^2\;\sum_{j=0}^{3d}
\mathbf1_{r+2j-3d=3s}\;c_{d,j}v_r\pmod3,
\qquad s\in\{-2,-1,0,1,2\}.
\]
For a fixed \(\epsilon\), start at \(v=e_\epsilon\), update the running digit parity \(p\) by \(p\leftarrow p+d\pmod2\), and after \(L\) digits read the central residue \(v_0\) **only if** \(p=\epsilon\). For a wrong parity, this initial-\(\epsilon\) branch represents no \(n\). Each digit word belongs to exactly one of the two parity branches, and its retained output is exactly \(Q_n\pmod3\).

**2. Complete finite transition graph.** Breadth-first closure under all three explicit \(T_d\) gives exactly eight states for \(\epsilon=0\) and ten for \(\epsilon=1\). In the following tables the state column lists the five residues \((v_{-2},v_{-1},v_0,v_1,v_2)\) without separators, followed by running parity; the next-state triple corresponds to digits \(d=0,1,2\). The output is shown only for the required ending parity. A dash means the state contributes no output in that branch.

\(\epsilon=0\):

| State | Vector | Parity | Next states | Output |
|---:|:---:|---:|:---:|:---:|
|0|00100|0|0,1,2|1|
|1|01010|1|3,4,5|—|
|2|10101|0|0,5,0|1|
|3|00000|1|3,6,3|—|
|4|00200|0|4,5,7|2|
|5|02020|1|3,0,1|—|
|6|00000|0|6,3,6|0|
|7|20202|0|4,1,4|2|

\(\epsilon=1\):

| State | Vector | Parity | Next states | Output |
|---:|:---:|---:|:---:|:---:|
|0|00010|0|1,2,3|—|
|1|00000|0|1,4,1|—|
|2|00100|1|2,5,6|1|
|3|02000|0|1,7,0|—|
|4|00000|1|4,1,4|0|
|5|01010|0|1,7,8|—|
|6|10101|1|2,8,2|1|
|7|00200|1|7,8,9|2|
|8|02020|0|1,2,5|—|
|9|20202|1|7,5,7|2|

All entries follow directly by substituting the three local coefficient lists into \(T_d\); the accompanying `VERIFY.py` reconstructs them from scratch and checks closure and target identity, rather than assuming this table.

**3. From finite automata to infinite identities.** Let \(M\) be the direct sum of the two directed graph adjacency matrices, counting multiple digit edges with their multiplicities. It is an integer matrix of order \(18\). The initial row vector has one unit at state zero of each parity branch. For the support sequence, the terminal column has entry \(1\) exactly when the displayed output is nonzero; for the signed sequence it has entry \(+1\) for output one, \(-1\) for output two, and zero otherwise. Then
\[
S_L=uM^Ls,\qquad B_L=uM^Lb\qquad(L\ge0).
\]
By Cayley–Hamilton each sequence obeys an integer linear recurrence of order at most \(18\) (the characteristic polynomial of \(M\)). Define candidate sequences by
\[
\widetilde S_0=1,\quad\widetilde S_1=3,\quad
\widetilde S_{L+2}=3\widetilde S_{L+1}-\widetilde S_L,
\]
\[
\widetilde B_0=1,\quad\widetilde B_1=3,\quad\widetilde B_2=4,\quad
\widetilde B_{L+3}=2\widetilde B_{L+1}+3\widetilde B_L.
\]
The differences \(S_L-\widetilde S_L\) and \(B_L-\widetilde B_L\) are annihilated, respectively, by the product of the degree-18 characteristic polynomial with a degree-two and a degree-three polynomial. They are therefore integer recurrences of order at most \(20\) and \(21\). Direct exact matrix iteration over the **entire** explicitly listed transition graph verifies the first \(20\) support values and first \(21\) signed values against these candidate recurrences (the portable checker goes through \(L=25\)). An order-\(m\) recurrence with its first \(m\) values zero is identically zero. This yields both claimed all-level recurrence laws without extrapolating from finite data.

**4. Closed forms and growth.** Summing the recurrences gives the two boxed generating functions. The recurrence \(S_{L+2}=3S_{L+1}-S_L\) with \(S_0=1,S_1=3\) is the even-step Fibonacci recurrence, hence \(S_L=F_{2L+2}\). Positivity of \(B_L\) follows from the positive initial three values and the recurrence with positive coefficients. The polynomial \(t^3-2t-3\) has a unique positive root \(\rho>1\); its other two roots form a conjugate pair of smaller absolute value, and the generating function has a nonvanishing numerator at its positive dominant pole. Therefore \(B_L=\Theta(\rho^L)\). Since \(\rho<(3+\sqrt5)/2\), the relative unit-class imbalance tends to zero. Finally \(N_0(L)=3^L-S_L\), and \(N_1,N_2\) follow by solving the two linear equations for \(S,B\).

## Verification

The self-contained `VERIFY.py` needs only Python's standard library. Running `python VERIFY.py` constructs the exact five-carry digit transfer, discovers and closes both reachable state graphs, iterates their exact integer digit-edge counts through \(L=25\), checks the necessary first \(20\) and \(21\) values for the Cayley–Hamilton argument, and independently expands the quadrinomial polynomial modulo three at all \(729\) indices \(0\le n<729\). The beginning of the exact census is:

| \(L\) | \(N_0(L)\) | \(N_1(L)\) | \(N_2(L)\) |
|---:|---:|---:|---:|
|0|0|1|0|
|1|0|3|0|
|2|1|6|2|
|3|6|15|6|
|4|26|36|19|
|5|99|87|57|
|6|352|219|158|
|7|1200|549|438|

These finite calculations verify the transition certificate; the infinite conclusion uses the proved recurrence-order bound, not enumeration alone.

## Relationship to prior work

The central coefficients of the four-term Pascal triangle are classical; the sequence is listed as OEIS A005190. Hoggatt and Smith (1979) study maximal quadrinomial coefficients and ordinary recurrences. Belbachir and Otmani (2023) and Mechacha (2023) study quadrinomial congruences at specially chosen indices, especially prime-square congruences at primes at least five. Neither of the inspected 2023 papers gives this full central-index mod-three three-class census or the signed secondary bias. The generic prime-power automaton methodology of Rowland and Zeilberger makes congruence questions algorithmically accessible; it does not by itself supply these closed all-level formulas. The present claim is **only** the exact ternary-block residue distribution and bias; none of those baseline notions or generic methods is presented as new.

## Limitations

The result is confined to the specific central coefficient sequence, modulus three, and complete ternary index blocks. It neither determines higher three-adic residues nor proves a comparable statement for arbitrary cutoffs. Earlier general recurrence or automata machinery might implicitly encode the result; an undiscovered explicit or equivalent prior formula remains possible. This is an internal, reproducible mathematical verification, not independent certification.

## References

1. M. Mechacha, *Congruences concerning quadrinomial coefficients*, arXiv:2307.16768v1, first submitted 27 July 2023, https://arxiv.org/abs/2307.16768.
2. H. Belbachir and Y. Otmani, *Quadrinomial-Like Versions for Wolstenholme, Morley and Glaisher Congruences*, Integers 23 (2023), article A27, https://math.colgate.edu/~integers/x27/x27.pdf.
3. C. Smith and V. E. Hoggatt, Jr., *A Study of the Maximal Values in Pascal's Quadrinomial Triangle*, 1979.
4. OEIS Foundation, A005190, *Central quadrinomial coefficients*, https://oeis.org/A005190.
5. E. Rowland and D. Zeilberger, *A Case Study in Meta-Automation: Automatic Generation of Congruence Automata For Combinatorial Sequences*, 2014, https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/meta.html.
