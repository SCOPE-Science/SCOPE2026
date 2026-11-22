# Cospectral friendship twins have different characteristic-three wave orbit censuses

## Finding
Cioabă, Haemers, Vermette and Wong identified a nonisomorphic adjacency-cospectral mate of the friendship graph with sixteen triangles. For that exact graph pair, the **reversible finite-field wave permutations have the same sharp global period but different numbers of fixed configurations, already at the first update**.

Write \(F\) for the graph comprising sixteen triangles sharing one central vertex (33 vertices total). Write \(E\) for the 13-vertex graph with the following block adjacency matrix, with consecutive vertex groups of sizes \(3,5,5\):
\[
A_E=\begin{pmatrix}
J_3-I_3&J_{3,5}&0\\
J_{5,3}&0&J_5-I_5\\
0&J_5-I_5&0
\end{pmatrix}.
\]
Here \(J_{a,b}\) is the all-one \(a\)-by-\(b\) matrix, \(J_a=J_{a,a}\), and \(I_a\) is the identity. Set \(H=E\sqcup 10K_2\), so \(F\) and \(H\) each have 33 vertices. Their common **integer** adjacency characteristic polynomial is
\[
\chi(z)=(z+1)^{16}(z-1)^{15}(z^2-z-32).
\]

For either graph \(G\), let \(A_G\) be the loopless adjacency matrix over any finite field \(\mathbb F_q\), where \(q=3^f\) and \(f\ge1\), and define the two-time-level reversible wave
\[
T_G(u,v)=(A_Gu-v,u),\qquad (u,v)\in\mathbb F_q^{33}\times\mathbb F_q^{33}.
\]
Every state is periodic at time zero and both permutations have **exact order 18**. Yet, for every positive integer \(t\), if \(s_t=3^{\nu_3(t)}\), \(a_t=\min(2,s_t)\), \(b_t=\min(4,s_t)\), \(c_t=\min(6,s_t)\), and \(\epsilon_t=1\) when \(t\) is even and \(0\) otherwise, then
\[
\boxed{\#\operatorname{Fix}(T_F^t)=q^{b_t+16a_t+15\epsilon_t a_t},\qquad
\#\operatorname{Fix}(T_H^t)=q^{c_t+15a_t+15\epsilon_t a_t}.}
\]
In particular, the time-one counts are \(q^{17}\) and \(q^{16}\), and the time-three counts are \(q^{35}\) and \(q^{33}\), respectively. The complete primitive-period census is obtained by Möbius inversion from these formulas. For example, the numbers of labelled states of **least period 18** are, respectively,
\[
\boxed{P_F(18)=(q-1)(q^{65}-q^{35}),\qquad
P_H(18)=(q^3-1)(q^{63}-q^{33}).}
\]
Divide by 18 for the corresponding temporal-orbit counts. Thus the two graph waves are **not conjugate even as permutations**, although their adjacency spectra and sharp global temporal clocks agree. The novel comparison is the modular wave behavior of the exceptional cospectral mate; the friendship-side wave formula is an already known special case of the general friendship-graph wave census.

## Assumptions and scope
Both graphs are undirected, simple, and individually vertex-labelled. The disjoint union \(10K_2\) consists of ten independent edges. The fields are exactly finite fields of characteristic three, \(q=3^f\), \(f\ge1\). Fixed-state counts distinguish labelled field configurations, not graph-automorphism orbits. The update is synchronous neighbor summation minus the previous time row; the graph adjacency has no self-loops. The formula is for **every positive integer time** and therefore determines the exact primitive temporal periods through the order-18 property. No statement is asserted for other field characteristics or nonlinear update rules.

## Proof
**1. The source graph pair and ordinary cospectrality.** The explicit block graph \(E\), its disjoint ten-edge extension, and the friendship graph \(F\) are the cospectral exception stated in Theorem 2 and Corollary 2 of Cioabă et al. The adjacency spectrum gives the displayed common integer polynomial. It is also independently checked by exact integer characteristic-polynomial arithmetic in `check_spectral.py`. Reducing modulo three makes the polynomial
\[
(z+1)^{18}(z-1)^{15},
\]
but *that polynomial alone does not determine the required modular Jordan blocks*.

**2. Modular Jordan structure of the friendship graph.** Write the central basis vector as \(h\), the two leaf vectors of petal \(i\) as \(e_i,f_i\), and introduce \(s_i=e_i+f_i\) and \(d_i=e_i-f_i\) for \(1\le i\le16\). Because two is invertible in characteristic three, these are a basis with \(h\). Direct adjacency gives
\[
A_Fd_i=-d_i,\qquad A_Fs_i=s_i+2h,\qquad A_Fh=\sum_{i=1}^{16}s_i.
\]
On the sixteen-dimensional \(s\)-space, the fifteen-dimensional coefficient-sum-zero subspace is a semisimple \(+1\) eigenspace. In the remaining two dimensions, \(-1\) has algebraic multiplicity two and geometric multiplicity one: solving \((A_F+I)(\alpha h+\sum_i\beta_i s_i)=0\) gives \(\beta_i=\alpha\) for all \(i\), and the hub equation holds since \(16\equiv1\pmod3\). Thus, writing \(J_m(\lambda)\) for a Jordan block of size \(m\),
\[
A_F\sim J_2(-1)\oplus J_1(-1)^{\oplus16}\oplus J_1(1)^{\oplus15}.
\]

**3. A different modular Jordan structure for the 13-vertex exceptional component.** Represent a vector on the three groups of \(E\) as \((x,y,z)\in\mathbb F_q^3\oplus\mathbb F_q^5\oplus\mathbb F_q^5\), and let \(X=\sum x_i\), \(Y=\sum y_i\), \(Z=\sum z_i\). Put \(B=A_E+I\). Because \(3=0\) and \(5=2\) in the field,
\[
B(x,y,z)=\big((X+Y)\mathbf1_3,\ (X+Z)\mathbf1_5+y-z,\ Y\mathbf1_5+z-y\big).
\]
Successive substitution yields the following *necessary and sufficient* kernel descriptions (all equations are in \(\mathbb F_q\)):
\[
\begin{aligned}
\ker B &: X=Y=Z=0,\quad z=y;\\
\ker B^2 &: X=0,\quad Z=-Y,\quad y-z=Y\mathbf1_5;\\
\ker B^3 &: X+Y+Z=0,\quad y-z=(X-Z)\mathbf1_5.
\end{aligned}
\]
Consequently their dimensions are \(6,7,8\). Solving \((A_E-I)(x,y,z)=0\) similarly gives \(X=0\), \(x=-Y\mathbf1_3\), \(Z=Y\), and \(z=Y\mathbf1_5-y\), with arbitrary \(y\in\mathbb F_q^5\); its dimension is five. The integer characteristic polynomial of \(E\) has characteristic-three eigenvalue multiplicities eight for \(-1\) and five for \(+1\). These nullities therefore force
\[
A_E\sim J_3(-1)\oplus J_1(-1)^{\oplus5}\oplus J_1(1)^{\oplus5}.
\]
Each of the ten independent \(K_2\) components adds one simple \(-1\) and one simple \(+1\) block. Hence
\[
A_H\sim J_3(-1)\oplus J_1(-1)^{\oplus15}\oplus J_1(1)^{\oplus15}.
\]
This length-three rather than length-two modular block is the structural source of the dynamical distinction.

**4. From adjacency Jordan blocks to wave Jordan blocks.** The wave matrix is
\[
W_G=\begin{pmatrix}A_G&-I\\I&0\end{pmatrix},\qquad
W_G^{-1}=\begin{pmatrix}0&I\\-I&A_G\end{pmatrix}.
\]
It is invertible over every field. For an adjacency Jordan block \(J_m(\lambda)\) with \(\lambda\in\{-1,1\}\), the corresponding \(2m\)-dimensional wave block has characteristic polynomial \((t^2-\lambda t+1)^m\). In characteristic three this is \((t-1)^{2m}\) for \(\lambda=-1\), and \((t+1)^{2m}\) for \(\lambda=1\). Moreover the eigenvectors of the wave at \(t=1\) correspond exactly to \(\ker(A+I)\), and those at \(t=-1\) correspond to \(\ker(A-I)\). A single adjacency Jordan block has one such eigenvector, so the temporal block is exactly one Jordan block of length \(2m\), not a nontrivial split. Therefore
\[
\begin{aligned}
W_F&\sim J_4(1)\oplus J_2(1)^{\oplus16}\oplus J_2(-1)^{\oplus15},\\
W_H&\sim J_6(1)\oplus J_2(1)^{\oplus15}\oplus J_2(-1)^{\oplus15}.
\end{aligned}
\]

**5. Exact periods and fixed-space dimensions.** For any unipotent Jordan block of size \(m\) in characteristic three, the dimension of the kernel of its \(t\)-th power minus identity is \(\min(m,3^{\nu_3(t)})\). For a \(-1\) temporal block the kernel is zero if \(t\) is odd, and the same expression applies if \(t\) is even. Applying this rule to the preceding decompositions proves both fixed-point formulas. The largest \(+1\) blocks have lengths four and six, requiring the factor nine for the sharp order; the \(-1\) blocks require the factor two, so both orders are exactly \(\operatorname{lcm}(9,2)=18\). Since the state spaces are finite and the maps invertible, no transient states occur. For each positive divisor \(d\mid18\), the exact population of primitive period \(d\) is
\[
P_G(d)=\sum_{e\mid d}\mu(d/e)\#\operatorname{Fix}(T_G^e),
\]
where \(\mu\) is the number-theoretic Möbius function. Other primitive periods are impossible. Substituting the values at times three, six, nine, and eighteen yields the displayed two period-18 expressions. The discrepancy already at period one proves nonconjugacy, since conjugate permutations have equal fixed-point counts.

## Verification
The standalone `verify_wave.py` constructs both 33-vertex adjacency matrices directly from their edge definitions, computes modular ranks for the first four powers of \(A\pm I\), and independently computes nullities of \(T^t-I\) at all six divisors of 18 using full 66-by-66 matrices over \(\mathbb F_3\). It verifies the claimed order and fixed-space formulas with exact Gaussian elimination. The separate `check_spectral.py` reconstructs both graphs independently and checks their full integer characteristic polynomials against the stated expression, using symbolic arithmetic. The two computations were executed successfully. Their finite-field checks take place over \(\mathbb F_3\); the proof's Jordan decompositions explain why the same exponents hold for every extension \(\mathbb F_{3^f}\).

The computed nullities for time \(t=1,2,3,6,9,18\) are respectively \((17,32,35,65,36,66)\) for \(F\), and \((16,31,33,63,36,66)\) for \(H\). The adjacency \(-1\) nullity sequences for successive powers are \((17,18,18,18)\) and \((16,17,18,18)\); both have constant \(+1\) nullity 15. These computations corroborate, but do not replace, the all-field algebraic argument.

## Relationship to prior work
Cioabă et al. (arXiv:1310.6529, initially public 2013-10-24), especially their Theorem 2 and Corollary 2, **already establish the nonisomorphic cospectral graph pair** and its ordinary adjacency spectra; these are not new graph-construction claims. Vlasov (arXiv:1311.4297, initially public 2013-11-18) describes the general second-order reversible cellular-automaton construction; reversibility is not new. The previously established exact characteristic-three friendship-wave census already covers the \(F\)-side formula. The distinctive claim here is the exceptional companion's **different modular Jordan block**, the resulting full companion-side temporal census, and the exact nonconjugacy comparison for this classical 33-vertex cospectral pair.

A published result on strongly regular graphs in characteristic two gives other examples of cospectral graphs with different reversible-wave orbit counts. That result is conceptually related but does not imply the present characteristic-three calculation: neither member of this pair falls under the required nontrivial strongly regular graph hypotheses, the relevant modular Jordan sizes are different, and the full companion matrix must be analyzed. The earlier result on matching integer characteristic polynomials but differing binary nilpotent behavior on lollipop graphs likewise concerns a different dynamics and graph family. No examined earlier work states the exact companion Jordan profile or temporal formulas above.

## Limitations
This is an exact result for one distinguished pair of 33-vertex graphs, not a classification of every cospectral graph pair or of all field characteristics. The original spectral exception is prior work. The friendship-side wave population formula is prior work; the novelty rests on the independently proved companion-side modular structure and comparison. The computational scripts verify the prime field and integer characteristic polynomials; the extension-field claim rests on the written proof. Unknown or unindexed older modular-cospectral studies may contain equivalent information. No independent mathematical validation has been carried out.

## References
1. S. M. Cioabă, W. H. Haemers, J. R. Vermette, W. Wong, *The graphs with all but two eigenvalues equal to ±1*, arXiv:1310.6529v1, first publicly submitted 2013-10-24, https://arxiv.org/abs/1310.6529 ; especially Theorem 1(vi), Theorem 2, and Corollary 2.
2. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first publicly submitted 2013-11-18, https://arxiv.org/abs/1311.4297 ; especially Section 3, equation (2).
3. *Three universal wave periods and spectrally invisible orbit counts on strongly regular graphs*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-universal-wave-periods-and-spectrally-invisible-orbit-coun--6be21916ed4f ; characteristic-two comparison, not a result on this pair.
