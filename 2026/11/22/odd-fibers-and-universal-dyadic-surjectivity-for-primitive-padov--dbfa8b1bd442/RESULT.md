# Odd fibers and universal dyadic surjectivity for primitive Padovan recurrences

## Finding

Let \(u_0,u_1,u_2\in\mathbb Z\) not all be even, and define \(u_{n+3}=u_{n+1}+u_n\) for \(n\ge0\). For every integer \(k\ge3\), put \(T_k=7\cdot2^{k-1}\) and
\[
N_k(y)=\#\{0\le n<T_k:u_n\equiv y\pmod{2^k}\},\qquad y\in\mathbb Z/2^k\mathbb Z.
\]
Then \(T_k\) is the least period of the complete three-term state modulo \(2^k\), and
\[
\boxed{N_k(y)\equiv1\pmod2\quad\text{for every }y\in\mathbb Z/2^k\mathbb Z.}
\]
In particular, every scalar residue occurs at least once per complete state period, for **every** primitive initial triple; equivalently each primitive Padovan recurrence has full image modulo every power of two and is dense in \(\mathbb Z_2\). At the two lower precisions the exceptional laws are: \(N_1(0),N_1(1)\) are \(3,4\) in some order, and all four values \(N_2(y)\) are even.

## Assumptions and scope

The initial triple is *primitive* exactly when it is nonzero modulo two. All fibers are counted with multiplicity in one complete index period, not just as distinct attained residues. The least period assertion refers to the full state \((u_n,u_{n+1},u_{n+2})\); no assertion is made about the least period of the scalar coordinate alone. The theorem concerns the fixed third-order integral recurrence and moduli \(2^k\), not arbitrary companion matrices, nonprimitive initial states, or odd primes.

Let
\[
Q=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix},\qquad
B=\begin{pmatrix}0&1&1\\1&1&1\\1&2&1\end{pmatrix},\qquad
D=\begin{pmatrix}2&4&3\\3&5&4\\4&7&5\end{pmatrix}.
\]
Write \(v=(u_0,u_1,u_2)^\mathsf T\), \(e=(1,0,0)\), so \(u_n=eQ^nv\). Let \(\nu_2(h)\) be the power-of-two valuation of nonzero integer \(h\).

## Proof

**1. Matrix lifting and the state period.** Direct integer multiplication gives
\[
Q^7=I+2B,\qquad Q^{14}=I+4D,\qquad \det B=\det D=1.
\]
The characteristic polynomial \(X^3+X+1\) of \(Q\) is irreducible over \(\mathbb F_2\); hence \(Q\bmod2\) cycles transitively through the seven nonzero three-vectors, with order seven. For each nonzero integer \(h\), let \(r=\nu_2(h)\). Repeated squaring of these displayed identities and then taking an odd power shows that
\[
\frac{Q^{7h}-I}{2^{r+1}}\equiv
\begin{cases}B\pmod2,&r=0,\\D\pmod2,&r\ge1.
\end{cases}
\]
For positive \(h\) this is an integral quotient; the same valuation comparison for negative differences follows by interchanging indices. Since \(B,D\) are unimodular, \(Q^{7h}v-v\) has at least one coordinate of exact valuation \(r+1\) whenever \(v\) is primitive. Times not divisible by seven cannot fix a primitive state modulo two. Thus the complete state has precisely the least period \(T_k=7\cdot2^{k-1}\) modulo \(2^k\).

**2. The seven parity types.** For \(0\le j<7\), put
\[
a_j=eQ^jv\bmod2,\qquad b_j=eBQ^jv\bmod2,\qquad d_j=eDQ^jv\bmod2.
\]
Because \(Q\) permutes the seven nonzero parity vectors transitively, the multiset of triples \((a_j,b_j,d_j)\), independent of the primitive \(v\), equals
\[
\{(1,0,0),(0,1,1),(0,1,0),(1,1,1),(0,0,1),(1,0,1),(1,1,0)\}.
\]
This is checked by substituting \(v=(1,0,0)^\mathsf T\) and using the transitive orbit. In particular there are exactly two branches with \(b_j=d_j=1\), one of each output parity, two branches with \(b_j=0,d_j=1\), and three branches with \(d_j=0\).

**3. Branching with exact fibers.** Define \(f_j(t)=eQ^{j+7t}v\bmod2^k\) on \(t\in\mathbb Z/2^{k-1}\mathbb Z\). The matrix lifting in Step 1 applies to differences of two indices, because \(B,D\) commute with \(Q\). For distinct \(s,t\) in that range, with \(r=\nu_2(t-s)\): if \(r=0\) and \(b_j=1\), then \(\nu_2(f_j(t)-f_j(s))=1\); if \(r\ge1\) and \(d_j=1\), then \(\nu_2(f_j(t)-f_j(s))=r+1\). Here differences are interpreted as integer representatives; congruence conclusions do not depend on those choices.

For each of the two branches with \(b_j=d_j=1\), this isometry makes \(f_j\) a bijection onto all \(2^{k-1}\) outputs of parity \(a_j\). Since their parities differ, *exactly one* of these two branches maps to each residue \(y\).

For a branch with \(b_j=0,d_j=1\), the odd-step difference is divisible by four; consequently all outputs \(f_j(t)\) have the same residue modulo four. On each of the two input parity classes \(t=2z+\epsilon\), the even-step difference identity says
\[
\nu_2(f_j(2z+\epsilon)-f_j(2w+\epsilon))=2+\nu_2(z-w).
\]
Each class therefore bijects onto exactly the same mod-four output ball, with exactly one preimage per attained residue; the whole branch has fibers either two or zero (for \(k\ge3\)).

Finally, if \(d_j=0\) and \(k\ge3\), translating \(t\) by \(2^{k-2}\) changes its output by a multiple of \(2^k\) (the leading matrix is \(D\)). This fixed-point-free translation pairs all inputs having any given output, so every fiber of such a branch is even. Adding the seven branches, each residue \(y\) receives one contribution from the two isometric branches and an even contribution from all the others. Therefore \(N_k(y)\equiv1\pmod2\), as claimed.

For \(k=2\), the four branches with \(b_j=1\) together contribute two to each residue of the appropriate parity; the three \(b_j=0\) branches contribute zero or two. For \(k=1\), the seven nonzero binary states give three zero first coordinates and four one first coordinates. These prove the small-precision statements.

## Verification

The accompanying `verify.py` uses only the Python standard library. It checks \(Q^7=I+2B\), \(Q^{14}=I+4D\), determinant identities, all seven parity types, and exact matrix-leading terms for ten dyadic valuations. It exhaustively verifies all primitive initial triples and all fibers modulo \(2^k\) for \(1\le k\le5\), and checks five representative primitive initial triples for \(6\le k\le12\). Executing `python3 verify.py` prints `VERIFY_OK`. Infinite validity rests on the explicit matrix lifting, isometry, and pairing proof, not on finite experimentation.

## Relationship to prior work

Taş–Karaduman study the periodicity of Padovan sequences in finite groups and establish period-lifting phenomena, without an all-initial-state parity classification of scalar residue fibers. Rowland–Yassawi establish a general p-adic interpolation and limiting *image-density* framework for constant-recursive sequences, but do not determine the finite-level fiber multiplicities of primitive Padovan sequences. Kamlovskii's studies supply general frequency theory and bounds over Galois rings, but the inspected statements do not give this exact odd-fiber conclusion. A closely related published result determines the average and variance of **zero-hit counts over primitive Padovan cycles**, not the value parity of *every scalar fiber in every individual primitive cycle*; its period proof uses the same companion-matrix identities, so the distinction is in the finer seven-branch residue analysis and its universal quantifiers.

## Limitations

The theorem determines only the parity of each fiber for \(k\ge3\), not its full integer multiplicity or distribution over primitive cycles. It does not classify nonprimitive states or other primes. Earlier general recurrence-frequency results could encode an equivalent fact implicitly; this remains a genuine historical-priority risk. The finite checker is a reproducibility aid, not an infinite certificate. Independent mathematical review has not been performed.

## References

1. S. Taş and E. Karaduman, *The Padovan Sequences in Finite Groups*, Chiang Mai J. Sci. **41** (2014), 456–462. https://www.thaiscience.info/journals/Article/CMJS/10932734.pdf
2. E. Rowland and R. Yassawi, *\(p\)-adic asymptotic properties of constant-recursive sequences*, arXiv:1602.00176, first posted 31 January 2016. https://arxiv.org/abs/1602.00176
3. O. V. Kamlovskii, *Frequency Characteristics of Linear Recurrence Sequences over Galois Rings*, Sbornik Math. **200** (2009), 499–519. https://www.mathnet.ru/eng/sm4528
4. O. V. Kamlovskii, *Frequency Characteristics of Coordinate Sequences of Linear Recurrences over Galois Rings*, Izvestiya Math. **77** (2013), 1130–1154. https://geodesic.mathdoc.fr/item/IM2_2013_77_6_a2/
5. *Exact zero-hit variance for primitive Padovan orbits modulo powers of two*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-zero-hit-variance-for-primitive-padovan-orbits-modulo-powe--3b25687bed0c
