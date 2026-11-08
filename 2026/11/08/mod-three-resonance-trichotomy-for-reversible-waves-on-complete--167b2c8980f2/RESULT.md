# Mod-three resonance trichotomy for reversible waves on complete bipartite graphs

## Finding

Let \(a,b\ge2\), \(n=a+b\), and \(q=3^f\) with \(f\ge1\). On the labelled complete bipartite graph \(K_{a,b}\), let \(A\) be its adjacency matrix over \(\mathbb F_q\). The reversible, second-order neighbor-sum update is
\[
 T(u,v)=(Au-v,u),\qquad (u,v)\in\mathbb F_q^n\times\mathbb F_q^n.
\]
All states are periodic at time zero. The exact order of this permutation, its fixed-point counts at **every** positive time, and its complete primitive-orbit populations depend only on \(ab\bmod3\).

Define \(E(t)=\dim_{\mathbb F_q}\ker(T^t-I)\), for an integer \(t\ge1\), and let \([P]\) denote one if the proposition \(P\) is true and zero otherwise. Then \(|\mathrm{Fix}(T^t)|=q^{E(t)}\), where
\[
 E(t)=\begin{cases}
 [4\mid t]\bigl(2n-4+4[3\mid t]\bigr),&3\mid ab,\\
 2(n-2)[4\mid t]+(1+[2\mid t])\bigl(1+[3\mid t]\bigr),&ab\equiv1\pmod3,\\
 2(n-2)[4\mid t]+4[8\mid t],&ab\equiv2\pmod3.
 \end{cases}
\]
The exact global periods, including all attainable positive primitive periods, are respectively
\[
\begin{array}{c|c|c}
ab\pmod3&\operatorname{ord}(T)&\text{attainable primitive periods}\\\hline
0&12&1,4,12\\
1&12&1,2,3,4,6,12\\
2&8&1,4,8
\end{array}.
\]
In particular, the resonance phase \(ab\equiv1\pmod3\) creates nonzero fixed points and primitive periods two, three, and six, whereas the other two phases do not. For any permitted positive divisor \(d\) of the global period, the exact number of states with least period \(d\) and the number of distinct temporal orbits are
\[
 P_d=\sum_{e\mid d}\mu(d/e)q^{E(e)},\qquad O_d=P_d/d.
\]
No other primitive periods occur. The formulas hold for every extension degree \(f\), and no quotient by graph automorphisms, phase exchange, or translation is taken.

## Assumptions and scope

A state consists of two independent vertex-label vectors over the finite field \(\mathbb F_q\); vertices of both shores are distinguishable. The graph is loopless, undirected, and has all cross-shore edges. Throughout, \(a,b\ge2\), \(q=3^f\), \(f\in\mathbb Z_{\ge1}\), and \(t\in\mathbb Z_{\ge1}\). Every fixed-space dimension is over \(\mathbb F_q\). The update uses subtraction in the field; replacing it by addition is a different dynamical model outside the present statement.

## Proof

**1. Reversibility and reduction.** Directly, \(T^{-1}(u,v)=(v,Av-u)\). Thus the finite-state permutation has no transients. Write \(V=\mathbb F_q^n=U\oplus W\), where \(U\) and \(W\) are the coordinate spaces of the two shores. Denote the shore sums by \(\sigma_U,\sigma_W\), and the two all-ones vectors by \(\mathbf1_U,\mathbf1_W\). Then
\[
 A(u,w)=(\sigma_W(w)\mathbf1_U,\sigma_U(u)\mathbf1_W),\quad
 \operatorname{rank}A=2,\quad A^3=abA.
\]
Furthermore, the two-row matrix \(T\) satisfies the exact identity
\[
 T^2+I=T\operatorname{diag}(A,A),
\]
and \(T\) commutes with \(\operatorname{diag}(A,A)\). The identity follows by multiplying the displayed block matrices, not from spectral approximation.

**2. Nonresonant shore sizes.** When \(3\nmid ab\), both shore-sum kernels have complementary constant vectors. Their direct sum, of dimension \(n-2\), is the zero-eigenspace of \(A\), and the complementary two-dimensional invariant space is the pair of constant shore vectors. On that space \(A\) has matrix \(\left(\begin{smallmatrix}0&b\\a&0\end{smallmatrix}\right)\). The first part contributes \(n-2\) copies of the two-dimensional \(T\)-block with characteristic polynomial \(X^2+1\), all of order four. The remaining four-dimensional block has characteristic polynomial
\[
 (X^2+1)^2-abX^2=X^4+(2-ab)X^2+1.
\]
If \(ab\equiv1\pmod3\), the factorization is \((X-1)^2(X+1)^2\). The two distinct adjacency eigenlines each lift to a nonscalar two-dimensional block of \(T\) with one repeated eigenvalue; hence there is exactly one size-two Jordan block at each of \(1\) and \(-1\). In characteristic three, their generalized eigenspaces contribute dimensions \(1+[3\mid t]\) each when the corresponding eigenvalue is fixed by time \(t\); the negative eigenvalue contributes only for even \(t\). This produces the middle formula for \(E(t)\), and the core has exact order six. The zero-adjacency part has order four, so the full order is twelve.

If \(ab\equiv2\pmod3\), the four-dimensional factor is \(X^4+1\). Its derivative \(X^3\) has no common root with the factor, so this block is semisimple over a splitting field; every root obeys \(X^4=-1\) and has exact multiplicative order eight. Thus its fixed dimension is four exactly at multiples of eight, yielding the third formula and global order eight.

**3. Resonant shore sizes.** When \(3\mid ab\), the adjacency matrix is nilpotent and its Jordan partition is determined by its ranks. It always has rank two. If exactly one of \(a,b\) is divisible by three, then \(\operatorname{rank}A^2=1\) and \(A^3=0\), so its Jordan blocks have sizes \(3,1^{n-3}\). If both are divisible by three, then \(A^2=0\), so the blocks have sizes \(2,2,1^{n-4}\). On the \(T\)-module associated with each nilpotent adjacency block of size \(k\), the identity in step one implies that \(X^2+1\) acts nilpotently with exact index \(k\). Since the module has dimension \(2k\), its invariant-factor polynomial is exactly \((X^2+1)^k\), with a single corresponding primary block. Here \(X^2+1\) is irreducible over \(\mathbb F_3\) and each of its roots has multiplicative order four. For \(4\mid t\), the multiplicity of this factor in \(X^t-1\) is \(3^{\nu_3(t)}\), giving a fixed-space contribution \(2\min(k,3^{\nu_3(t)})\). Otherwise that contribution is zero. Inserting either Jordan partition above gives \(2n-4\) fixed dimensions at \(4\mid t\), \(3\nmid t\), and \(2n\) at \(12\mid t\), exactly the first displayed formula. The full order is twelve.

**4. Least periods.** In each case, the fixed-point formula follows by the usual linear-algebra nullity calculation for primary blocks and remains valid after extension to \(\mathbb F_{3^f}\). Möbius inversion of \(|\mathrm{Fix}(T^d)|=\sum_{e\mid d}P_e\) gives the asserted populations. Nonnegativity is strict for all listed nontrivial periods: in the resonant case \(P_4=q^{2n-4}-1\) and \(P_{12}=q^{2n}-q^{2n-4}\); in the order-eight case \(P_4=q^{2n-4}-1\), \(P_8=q^{2n}-q^{2n-4}\). For \(ab\equiv1\), the six populations, in period order \(1,2,3,4,6,12\), are
\[
 q,\quad q^2-q,\quad q^2-q,\quad q^{2n-2}-q^2,\quad q^4-2q^2+q,\quad q^{2n}-q^{2n-2}-q^4+q^2.
\]
All are positive because \(q\ge3\) and \(n\ge4\). The table of realized periods and exact maximal orders therefore follows without relying on experiments. \(\square\)

## Verification

The package contains two executable standard-library Python programs. Running `python check_matrix.py` verifies 1,176 exact matrix-power nullities over \(\mathbb F_3\) for the 49 ordered pairs \((a,b)\) with \(2\le a,b\le8\), for time indices \(1\le t\le24\); it also checks the asserted global-order identity in all 49 cases. Running `python check_direct.py` performs direct neighbor-by-neighbor updates of all 597,051 states of \(K_{2,2}\), \(K_{2,3}\), and \(K_{2,4}\) over \(\mathbb F_3\), calculating least periods independently of matrix powers.

In the three tests, the least-period populations are respectively \((1:3,2:6,3:6,4:720,6:66,12:5760)\), \((1:1,4:728,12:58320)\), and \((1:1,4:6560,8:524880)\). The files `matrix_output.txt` and `direct_output.txt` contain actual successful replay outputs. These finite tests corroborate but do not replace the unrestricted proof.

## Relationship to prior work

Second-order reversible cellular automata are a standard construction: Toffoli–Margolus (1990, §5.4, equations (12)–(17)) already gives the generic previous-state subtraction recurrence, and Vlasov (2013, §3, §6.2) explicitly presents the ternary version on general cell spaces. The claim here is neither the reversibility construction nor the graph spectrum alone, but the characteristic-three resonance classification, complete fixed-space formula for all times, sharp least-period support, and orbit census on every \(K_{a,b}\). The finite-field characteristic is essential: characteristic-two bipartite waves with previous-state addition have a different primary-polynomial structure. In particular, earlier results concerning complete multipartite binary waves do not imply the present ternary formulas without a new characteristic-three analysis.

## Limitations

The statement is only for the specific neighbor-sum second-order rule, complete bipartite graphs with shore sizes at least two, and fields of characteristic three. It does not address arbitrary weights, other characteristics, or nonlinear local updates. The published-literature search was finite; a corresponding result in unindexed or inaccessible work cannot be ruled out. No external independent audit has been performed.

## References

- Alexander Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first public preprint 2013-11-18. https://arxiv.org/abs/1311.4297
- Edward Fredkin and Tommaso Toffoli, *Conservative Logic*, International Journal of Theoretical Physics **21** (1982), 219–253, DOI:10.1007/BF01857727. https://doi.org/10.1007/BF01857727
- Tommaso Toffoli and Norman Margolus, *Invertible cellular automata: A review*, Physica D **45** (1990), 229–253. DOI:10.1016/0167-2789(90)90185-R.
