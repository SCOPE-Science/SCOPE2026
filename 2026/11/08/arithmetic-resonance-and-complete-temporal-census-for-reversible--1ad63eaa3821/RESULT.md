# Arithmetic resonance and complete temporal census for reversible wheel waves

## Finding

Let \(n\ge5\) be an integer, let \(Q=2^f\) for an integer \(f\ge1\), and let \(W_n=K_1\vee C_n\) have a labelled central vertex and a labelled rim of length \(n\). Write \(A\) for its open-neighbor adjacency operator over \(\mathbb F_Q\). The reversible two-time-level wave is
\[
T(u,v)=(Au+v,u),\qquad (u,v)\in\mathbb F_Q^{n+1}\times\mathbb F_Q^{n+1}.
\]
All configurations are periodic immediately. Put \(g=\gcd(n,t)\) and \(b=2^{\nu_2(t)}\) for every integer \(t\ge1\). If \(n\) is even, put \(h=2^{\nu_2(n)}\). The number of configurations fixed by \(T^t\) is exactly \(Q^{E_n(t)}\), where
\[
E_n(t)=\begin{cases}
2(g-1)+2\mathbf1_{3\mid t}\min(b,2),&n\text{ odd},\\
2g+\min(b,6)-2\min(b,2),&h=2,\\
2g+\min(b,6)+2\min(b,2)-2\min(b,4),&h=4,\\
2g+\min(b,2),&h\ge8.
\end{cases}
\]
The exact global permutation order is
\[
L_n=\operatorname{ord}(T)=\begin{cases}
\operatorname{lcm}(6,n),&n\text{ odd},\\
4n,&2\parallel n,\\
2n,&4\parallel n,\\
n,&8\mid n.
\end{cases}
\]
Thus one added hub can multiply the original rim's reversible temporal clock by three (odd rim not divisible by three), four, two, or one, depending on the rim's arithmetic. For every divisor \(d\) of \(L_n\), the exact number of configurations of primitive period \(d\), and the number of corresponding distinct temporal orbits, are respectively
\[
P_n(d)=\sum_{e\mid d}\mu(d/e)Q^{E_n(e)},\qquad O_n(d)=P_n(d)/d.
\]
All other primitive populations vanish. If \(n\) is even, every divisor of \(L_n\) occurs as a primitive period. If \(n\) is odd, the occurring primitive periods are exactly the divisors \(d\mid L_n\) satisfying \(2\nmid d\) or \(3\mid d\): in particular no period divisible by two but not by three occurs.

## Assumptions and scope

The graph has exactly \(n+1\) vertices and is simple and undirected; the rim \(C_n\) has \(n\ge5\) vertices, so its two neighbors are distinct. Field characteristic is exactly two, and \(Q\) can be any power of two. Both ordered time rows count as part of one configuration, and two configurations related by a spatial graph automorphism are **not** identified. Time-zero periodicity means a configuration is already on a cycle, without any transient. \(\mu\) is the classical number-theoretic Möbius function. A formula for fixed points at positive integer times, not merely at divisors of the global order, is asserted.

## Proof

**1. The invertible rim modes.** Let \(S\) cyclically shift the \(n\) rim coordinates and put \(B=S+S^{-1}\). With \(e\) the all-ones column vector and \(\phi(x)=e^\top x\), the full wheel adjacency is
\[
A=\begin{pmatrix}0&\phi\\e&B\end{pmatrix},\qquad Be=0,\quad\phi B=0.
\]
The rim is the \(\mathbb F_Q[s]\)-module \(R=\mathbb F_Q[s]/(s^n-1)\), on which \(S\) multiplies by \(s\) and \(B=s^{-1}(s+1)^2\). Set \(h=2^{\nu_2(n)}\), allowing \(h=1\) for odd \(n\). The primary decomposition gives \(R=R_0\oplus R_*\): the \((s+1)\)-primary space \(R_0\) has dimension \(h\) and is one Jordan block \(J_h(1)\) for \(S\); \(B\) is invertible on \(R_*\). Since \(e\in R_0\), \(\phi\) vanishes on \(R_*\), because \(\phi B=0\) and \(B\) is invertible there. Consequently \(A\) is the direct sum of \(B|_{R_*}\) and an operator \(A_0\) on the hub together with \(R_0\).

On \(R_*\), the wave with adjacency \(B\) is conjugate to \(S\oplus S^{-1}\). Indeed, the invertible coordinate map
\[
(a,b)\longmapsto(a+b,S^{-1}a+Sb)
\]
intertwines \((Sa,S^{-1}b)\) with the wave update; its determinant is \(S+S^{-1}=B\), invertible on \(R_*\). The shift \(S\) on all rim coordinates has \(\dim\ker(S^t-I)=g\), since it permutes coordinates in \(g=\gcd(n,t)\) cycles. Its restriction to \(R_0\) contributes \(\min(b,h)\) fixed dimensions (because \((I+N)^t-I\) has the same kernel as \(N^b\) on \(J_h(1)\)). Thus the two invertible wheel-wave blocks contribute
\[
2\bigl(g-\min(b,h)\bigr)
\]
fixed dimensions, for odd and even \(n\) alike.

**2. The odd-rim hub block.** If \(n\) is odd, \(R_0=\langle e\rangle\) and \(\phi(e)=1\). The hub and \(e\) are interchanged by \(A_0\), so \(A_0\simeq J_2(1)\) in characteristic two. Its four-dimensional reversible wave has characteristic polynomial \(p(X)^2\) with \(p(X)=X^2+X+1\). Moreover \(p(T_0)=(A_0+I)T_0\) has kernel dimension two. Hence this time block is the cyclic \(\mathbb F_Q[X]\)-module \(\mathbb F_Q[X]/p(X)^2\), regardless of whether \(p\) splits over \(\mathbb F_Q\). The polynomial \(p\) divides \(X^t-1\) precisely when \(3\mid t\), with multiplicity \(b\) in that case. The odd-rim hub contributes \(2\mathbf1_{3\mid t}\min(b,2)\) fixed dimensions, proving the odd branch after adding the invertible contribution with \(h=1\).

**3. Even-rim hub blocks.** Now \(n\) is even and \(h\ge2\). On \(R_0\), multiplication by \(B=s^{-1}(s+1)^2\) has exactly two nilpotent Jordan blocks of size \(h/2\), because \(\operatorname{rank}B_0^j=\max(h-2j,0)\). Here \(\phi(e)=0\), so direct multiplication gives
\[
A_0^2(h_0,x)=(0,B_0^2x+\phi(x)e),\qquad
A_0^j(h_0,x)=(0,B_0^jx)\quad(j\ge3).
\]
For \(h=2\), \(B_0=0\) and the nonzero functional \(\phi|_{R_0}\) pairs with \(e\) to produce \(A_0\simeq J_3(0)\). For \(h=4\), the ranks of \(A_0^j\) for \(j=0,1,2,3\) are \(5,2,1,0\): indeed \(e\in\operatorname{im}B_0\), \(\phi\) is in the row space of \(B_0\), and \(B_0^2=0\). Therefore \(A_0\simeq J_3(0)\oplus J_1(0)^{\oplus2}\).

For \(h\ge8\), choose the rim vector \(z\) with repeating eight-bit word \(00001111\). Then \(B^2z=e\) and \(\phi(z)=0\); projection onto \(R_0\) preserves both equalities. Hence \(A_0^2(\alpha,x)=(0,B_0^2(x+\phi(x)z))\), and \(x\mapsto x+\phi(x)z\) is invertible. Also \(\operatorname{rank}A_0=\operatorname{rank}B_0\): the last equation \(e=B_0^2z\) makes the hub output \(\phi(x)\) a fixed linear functional of the rim output \(B_0x+\alpha e\). Consequently the ranks of all positive powers of \(A_0\) equal those of \(B_0\); comparison of nilpotent Jordan rank sequences yields
\[
A_0\simeq J_{h/2}(0)^{\oplus2}\oplus J_1(0)\qquad(h\ge8).
\]

**4. Transfer to temporal Jordan blocks.** For a nilpotent spatial block \(J_k(0)\), the companion wave has characteristic polynomial \((X+1)^{2k}\). Its fixed space at one time step has dimension \(\dim\ker J_k(0)=1\); therefore it is exactly one temporal Jordan block \(J_{2k}(1)\). At time \(t\), this block contributes \(\min(b,2k)\) fixed dimensions. Applying this to the three cases above gives, respectively, the hub contributions
\[
\min(b,6),\qquad \min(b,6)+2\min(b,2),\qquad 2\min(b,h)+\min(b,2).
\]
Adding the invertible-rim contribution \(2(g-\min(b,h))\) proves the three even branches of \(E_n(t)\).

**5. Exact order and support.** In the odd case the hub-time block has exact order six and the invertible-rim shifts have joint order \(n\); hence the global order is \(\operatorname{lcm}(6,n)\). The odd-rim shifts realize every nontrivial odd divisor of \(n\), while the hub realizes periods three and six; least-common-multiple combinations prove exactly the asserted odd-rim period set. In the even cases, the nilpotent hub contributes maximal power-of-two order eight for \(h=2,4\), or \(h\) for \(h\ge8\); the invertible rim modes realize the odd factor \(n/h\) (when nontrivial). This yields the three even-rim order formulas. Each power-of-two divisor up to the hub's maximum appears on a suitable temporal Jordan vector, and each odd divisor of \(n/h\) occurs among the nontrivial shift modes, so their independent direct sums realize every divisor of the even-rim global order. Möbius inversion of fixed-point counts gives the primitive configuration and orbit formulas. \(\square\)

## Verification

`check_matrix.py` constructs the full binary wheel adjacency and doubled reversible transition independently of the proof, uses exact GF(2) bit-matrix multiplication and Gaussian elimination, and compares all global-order divisors plus selected nondivisor times against the formula for every rim size from 3 through 50 (including two smaller boundary checks outside the theorem domain); it also checks that the global permutation order is sharp. Its captured output reports 751 passed exact fixed-space comparisons.

`check_states.py` constructs the wheel update by direct neighbor bit parity and enumerates all \(349440\) labelled paired binary configurations for rim lengths 3 through 8 (the first two are boundary checks). It measures every primitive return time by direct iteration, checks the predicted fixed-point counts at all global-order divisors, and reports no mismatches. Both standalone scripts and captured outputs accompany this result. The unrestricted claim is established by the proof above, not by extrapolation from these finite experiments.

For an explicit example within the theorem domain, \(n=5\) and \(Q=2\) give global order \(30\) and primitive configuration counts at periods \(1,3,5,6,15,30\) of \(1,3,255,12,765,3060\) respectively; periods \(2\) and \(10\) are absent.

## Relationship to prior work

Tadaki's 1994 study treats the ordinary first-order linear rules 90/150 with periodic spatial boundaries, including the special nilpotence of rule 90 at powers-of-two sizes; it does not treat an added wheel hub or reversible paired-time wave populations. Macfarlane's 2004 work develops reversible second-order one-dimensional cellular automata and matrix equivalents, with emphasis on infinite-line seed weights rather than wheel-graph primitive-period populations. Abu-Jeib's 2006 wheel-graph work studies ordinary adjacency eigenvalues and determinants over the reals; these spectral statements do not resolve the modular Jordan degeneracies or reversible time-orbit distribution here. Standard primary-decomposition and Möbius-inversion principles are used without novelty claims. In particular, the new content is not the general reversibility of second-order updates, the ordinary cycle shift census, or the first-order nullity of a wheel, but their nontrivial combination through the hub's modular Jordan blocks yielding the explicit arithmetic period and all-time fixed-point laws.

## Limitations

The theorem concerns the uniform binary-characteristic neighbor-sum rule only; no claim is made for odd characteristic, nonlinear threshold rules, or graphs with missing or weighted spokes. The exact counts distinguish labelled configurations, not spatial-automorphism classes. Novelty comparisons cover the cited primary works and targeted public mathematical searches, but undiscovered earlier treatments of equivalent characteristic-two wheel time dynamics remain a historical-priority risk. No independently performed audit is asserted.

## References

1. Shin-ichi Tadaki, *Periodicity of cylindrical linear cellular automata*, arXiv:patt-sol/9412003v1, first public 1994-12-15, https://arxiv.org/abs/patt-sol/9412003.
2. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A 37 (2004), 10791–10814, doi:10.1088/0305-4470/37/45/006.
3. Iyad T. Abu-Jeib, *The Determinant of the Wheel Graph and Conjectures by Yong*, Missouri Journal of Mathematical Sciences 18 (2006), doi:10.35834/2006/1802142, author-posted full text https://abujeib.com/Research/Papers/abujeib11_conjectures.pdf.
