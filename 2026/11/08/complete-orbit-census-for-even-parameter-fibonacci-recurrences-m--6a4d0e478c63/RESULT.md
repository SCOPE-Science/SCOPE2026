# Complete orbit census for even-parameter Fibonacci recurrences modulo powers of two

## Finding

For every integer \(K\ge 2\) with \(K\equiv 2\pmod4\) and every \(r\ge1\), consider the bijection
\[
T_{K,r}(x,y)=(Kx+y,x)\pmod {2^r}
\]
on the \(2^{2r}\) states of \((\mathbb Z/2^r\mathbb Z)^2\). Thus every state corresponds to a uniquely determined, bi-infinite, second-order recurrence with arbitrary initial values, rather than only the standard initial values \((0,1)\).

Every least cycle length is a power of two, and **all** powers \(1,2,4,\ldots,2^r\) occur. Let \(c_r(j)\) be the number of distinct orbits of least length \(2^j\). Then
\[
c_r(0)=2,\qquad c_r(1)=1,
\]
\[
c_r(2)=\begin{cases}3,&r=2,\\7,&r\ge3,\end{cases}
\]
and, when \(r\ge3\),
\[
c_r(j)=\begin{cases}
3\cdot2^{j-1},&3\le j<r,\\
2^{r-1},&j=r.
\end{cases}
\]
For \(r=1\), only \(c_1(0)=2\) and \(c_1(1)=1\) apply. In particular, the **total number of cycles** is
\[
\boxed{\begin{cases}
3,&r=1,\\
2^{r+1}-2,&r\ge2.
\end{cases}}
\]
The entire cycle census is independent of the odd integer \(K/2\).

Equivalently, the exact periodic-point counts for \(j\ge0\) are
\[
N_r(0)=2,\quad N_r(1)=4,\quad
N_r(j)=2^{\min(r,j)+\min(r,j+1)}\ (j\ge2),
\]
where \(N_r(j)=\#\{v:T_{K,r}^{2^j}(v)=v\}\). The last formula applies for all \(j\ge2\), including \(j>r\).

## Assumptions and scope

The integer parameter \(K\) is strictly positive and exactly divisible by \(2\) but not \(4\); \(r\) is any positive integer. Both initial coordinates range freely over the entire residue ring. The ordered coordinates \((x,y)\) correspond to two successive recurrence terms, with update \((x,y)\mapsto(Kx+y,x)\). A cycle is an orbit of this permutation, and its least length is its primitive period. Distinct cycles are counted without distinguished start points. The definition applies to the zero state as well.

## Proof

Put \(K=2u\), where \(u\) is odd, and write
\[
A=\begin{pmatrix}K&1\\1&0\end{pmatrix}\in\mathrm{GL}_2(\mathbb Z),
\qquad A^2=KA+I.
\]
Since \(\det A=-1\), its reduction modulo \(2^r\) is invertible. Every state is therefore periodic, not eventually periodic with a transient.

We compute the \(2\)-adic Smith invariant valuations of the integer matrices \(A^{2^j}-I\). For any integral \(2\)-by-\(2\) matrix \(M\) with nonzero determinant, the first Smith valuation is the minimum of the \(2\)-adic valuations of its four entries and the sum of the two Smith valuations equals \(\nu_2(\det M)\). These follow directly from the gcd-of-minors characterization of the Smith normal form.

First,
\[
A-I=\begin{pmatrix}K-1&1\\1&-1\end{pmatrix},
\qquad\det(A-I)=-K.
\]
It contains a unit entry and \(\nu_2(K)=1\), so its two valuations are \((0,1)\). Next
\[
A^2-I=KA=2uA,
\]
whose invariant valuations are \((1,1)\) because \(A\) is unimodular.

For the first nontrivial doubling,
\[
A^4-I=(A^2-I)(A^2+I)
=4uA(I+uA).
\]
The matrix \(B=I+uA\) has an odd off-diagonal entry \(u\) and
\[
\det B=1+u\operatorname{tr}A+u^2\det A
=1+2u^2-u^2=1+u^2.
\]
Every odd square is \(1\pmod8\), so \(\nu_2(1+u^2)=1\). Hence \(B\) has Smith valuations \((0,1)\). Multiplying by the \(2\)-adic units \(u\) and \(A\), and then by \(4\), proves that \(A^4-I\) has valuations \((2,3)\).

Inductively, suppose \(j\ge2\) and \(A^{2^j}=I+2^jM_j\) with \(M_j\) having Smith valuations \((0,1)\). Squaring gives
\[
A^{2^{j+1}}-I
=2^{j+1}M_j(I+2^{j-1}M_j).
\]
Since \(j\ge2\), the last factor is congruent to \(I\) modulo \(2\), and hence is invertible over \(\mathbb Z_2\). Multiplication by it preserves the Smith valuations of \(M_j\). Therefore \(M_{j+1}\) also has valuations \((0,1)\). By induction, the valuations of \(A^{2^j}-I\) are exactly \((j,j+1)\) for every \(j\ge2\).

For a matrix over \(\mathbb Z_2\) with Smith valuations \((a,b)\), its kernel modulo \(2^r\) has precisely
\[
2^{\min(a,r)+\min(b,r)}
\]
elements: the scalar congruence \(2^a z=0\pmod{2^r}\) has \(2^{\min(a,r)}\) solutions, and the invertible Smith transformations do not change kernel size. The three Smith cases above give exactly the stated \(N_r(j)\).

For \(r=1\), \(A^2\equiv I\pmod2\), and for \(r\ge2\), the just-proved Smith valuations imply \(A^{2^r}\equiv I\pmod{2^r}\). Hence every least period divides \(2^r\). Let \(E_r(0)=N_r(0)\), and for \(j\ge1\) let \(E_r(j)=N_r(j)-N_r(j-1)\). These are exactly the numbers of states whose least periods equal \(2^j\). Dividing by the orbit length gives
\[
c_r(0)=N_r(0),\qquad c_r(j)=\frac{N_r(j)-N_r(j-1)}{2^j}\quad (1\le j\le r).
\]
Substitution yields the asserted piecewise formulas. In particular, for \(r\ge3\) the count at \(2^2\) is \((32-4)/4=7\), each interior length \(2^j\) with \(3\le j<r\) has \((2^{2j+1}-2^{2j-1})/2^j=3\cdot2^{j-1}\) cycles, and the terminal length \(2^r\) has \((2^{2r}-2^{2r-1})/2^r=2^{r-1}\) cycles. Direct summation gives the total stated above. Every \(E_r(j)\) is positive for \(0\le j\le r\), proving the complete length spectrum. \(\square\)

## Verification

The accompanying `verify_cycles.py` implements two independent exact checks: (i) integer matrix squaring plus the valuations of the gcd of entries and determinant, for \(j=0,\ldots,8\); and (ii) full, non-sampled traversal of all \(2^{2r}\) states for each \(r=1,\ldots,7\), counting cycles of each least length. Both checks were run for \(K\in\{2,6,10,14,18,22\}\), with complete comparisons to the displayed formula. This is a finite regression check only; the infinite proof is the argument above.

Run with `python3 verify_cycles.py`. The recorded standard output is `checker_output.txt`.

## Relationship to prior work

Benfield and Lippard (2024) study the Pisano period \(\pi_K(m)\) for the standard \(K\)-Fibonacci initial conditions \((0,1)\) and classify moduli fixed under that period map. In particular, for \(K\equiv2\pmod4\), their period analysis includes powers of two. Such a period result bounds the lengths of orbits under \(A\), but does not determine their **number, multiplicities, or entire spectrum** over arbitrary initial states. The present theorem computes all of these via two-adic Smith invariants.

Fiebig, Mbirika, and Spilker (2024) compare periods, entry points, and orders of two distinguished Lucas sequences \(U\) and \(V\). Their Section 3.2 and discussion of Wall's earlier criterion for arbitrary starting terms are period comparisons, not an all-seed cycle census. The classical Fibonacci integer-cycle tables concern coefficient \(K=1\), not this \(K\equiv2\pmod4\) family.

## Limitations

The theorem does not classify \(K\) divisible by four, odd \(K\), odd-prime-power moduli, or arbitrary second recurrence coefficients. It gives cycle counts, not an explicit list of representatives for each cycle. The formulas are rigorous and unconditional; originality remains subject to the possibility of an equivalent previously published but unindexed matrix-dynamics classification. Independent validation has not been carried out.

## References

1. Brennan Benfield and Oliver Lippard, *Fixed Points of K-Fibonacci Sequences*, arXiv:2404.08194 (first submitted 12 April 2024), https://arxiv.org/html/2404.08194v2.
2. Morgan Fiebig, aBa Mbirika, and Jürgen Spilker, *Period patterns, entry points, and orders in the Lucas sequences: theory and applications*, arXiv:2408.14632 (first submitted 26 August 2024), https://arxiv.org/html/2408.14632v2.
3. D. D. Wall, *Fibonacci Series Modulo m*, Amer. Math. Monthly **67** (1960), 525–532, https://doi.org/10.2307/2309169.
4. OEIS A015134, *Number of Fibonacci integer cycles mod n*, https://oeis.org/A015134. (The coefficient here is one, and is not the same family.)
