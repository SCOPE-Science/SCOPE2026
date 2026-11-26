# A twisted-seam transient law for binary parity dynamics on cubic ladders

## Finding
For every integer \(n\ge3\), compare the two connected cubic graphs on \(2n\) vertices: the circular prism \(P_n=C_n\square K_2\) and the Möbius ladder \(M_{2n}\), formed by closing an \(n\)-rung ladder with a crossed seam. Let \(F_P,F_M\) synchronously replace each binary vertex state by the sum of its three *distinct open-neighbour states* in \(\mathbb F_2\). Define \(\tau_F(x)\) as the smallest nonnegative time at which the trajectory of \(x\) enters a periodic orbit. Set \(k=2^{\nu_2(n)}\), the largest power of two dividing \(n\).

If \(3\nmid n\), both maps are bijections: all \(2^{2n}\) states are periodic. If \(3\mid n\), both maps have exactly \(2^{2n-4k}\) periodic states, and every image fibre after the maximal transient has exactly \(2^{4k}\) elements. Nevertheless their *sharp maximal* entrance times differ:
\[
\begin{array}{c|cc}
&F_P&F_M\\\hline
n\text{ odd}&2&1\\
n\text{ even}&k&2k.
\end{array}
\]
Thus a crossed boundary seam preserves the number of eventual states and the uniform eventual-phase fibre cardinality but halves the odd-case transient and doubles the even-case transient.

More precisely, if \(3\mid n\), put \(Q_F(t)=\#\{x:\tau_F(x)\le t\}\) for each integer \(t\ge0\). For \(n\) odd,
\[
Q_P(t)=2^{2n-4+2\min(t,2)},\qquad Q_M(t)=2^{2n-4+4\min(t,1)}.
\]
For \(n\) even,
\[
Q_P(t)=2^{2n-4k+4\min(t,k)},\qquad
Q_M(t)=2^{2n-4k+2\min(t,2k)}.
\]
The exact number of configurations with entrance time \(t\ge1\) is \(Q_F(t)-Q_F(t-1)\), and exactly \(Q_F(0)\) configurations start periodic. In particular, when \(n\) is even and divisible by three, exactly three quarters of all configurations on \(M_{2n}\) need the maximal \(2k\) steps, whereas fifteen sixteenths require the maximal step on \(M_{2n}\) when \(n\) is odd and divisible by three.

For each integer \(r\ge1\), the exact number of temporal fixed points of \(F_M^r\) is
\[
\#\operatorname{Fix}(F_M^r)=2^{\deg\gcd\bigl(z^{2n}+1,(1+z^2+z^{n+1})^r+z^r\bigr)},
\]
with gcd over \(\mathbb F_2[z]\). The number of distinct primitive \(r\)-cycles is therefore \(\frac1r\sum_{d\mid r}\mu(r/d)\#\operatorname{Fix}(F_M^d)\). This gives the complete period census for every Möbius-ladder size, without enumerating its states.

## Assumptions and scope
Label the vertices of \(M_{2n}\) by \(\mathbb Z/(2n)\) and join \(j\) to \(j-1,j+1,j+n\) modulo \(2n\). Label the vertices of \(P_n\) by \((j,\epsilon)\in\mathbb Z/n\times\{0,1\}\), joining \((j,\epsilon)\) to \((j\pm1,\epsilon)\) and \((j,1-\epsilon)\). The listed three neighbours are distinct for \(n\ge3\). The rule is simultaneous, self-exclusive, and unweighted; all algebra below is over the field \(\mathbb F_2\). The count \(Q_F(t)\) refers to first entry into *any* periodic orbit, not to a chosen periodic phase. A phase fibre means the preimage of a specified recurrent configuration under \(F^T\) for an integer \(T\) at least the stated sharp maximal entrance time; it does not mean the union of the basins of all phases in a cycle.

## Proof
Write \(\Phi(z)=z^2+z+1\). For any monic polynomial \(h\) and any polynomial \(p\) over \(\mathbb F_2\), multiplication by \(p\) on \(R=\mathbb F_2[z]/(h)\) has kernel dimension \(\deg\gcd(p,h)\). Indeed, writing \(g=\gcd(p,h)\), the equation \(h\mid pa\) is equivalent to \(h/g\mid a\), and its residue classes form a \(\deg g\)-dimensional space. Applying the Chinese remainder decomposition to the factors of \(h\), multiplication by \(p\) is nilpotent on precisely the primary factors dividing \(p\) and invertible on the complementary summand. The latter summand consists entirely of periodic states, because it is finite and invertible. If the nilpotent summand has dimension \(d\), every stable-image phase fibre has cardinality \(2^d\).

**Möbius ladder.** Put \(h_M=z^{2n}+1\) and identify binary configurations with \(R_M=\mathbb F_2[z]/(h_M)\). The update is multiplication by \(a_M=z+z^{-1}+z^n=z^{-1}f\), where \(f=1+z^2+z^{n+1}\); the factor \(z^{-1}\) is a unit. Let \(\lambda\) be any root of \(h_M\) in an algebraic closure. Since the characteristic is two, \(\lambda^n=1\). Consequently \(f(\lambda)=\lambda^2+\lambda+1\). Thus \(a_M\) has a zero among the roots of \(h_M\) if and only if \(3\mid n\), and all such zeros belong to \(\Phi\); no other factor may contribute a transient.

Suppose \(3\mid n\), and write \(n=km\) with \(m\) odd and \(k=2^{\nu_2(n)}\). Since \(z^{2n}+1=(z^m+1)^{2k}\) and \(3\mid m\), the exponent of \(\Phi\) in \(h_M\) is *exactly* \(2k\). Its contribution to \(R_M\) has dimension \(2\cdot2k=4k\).

The multiplicity of \(\Phi\) in \(f\) is \(e=1\) when \(n\) is even and \(e=2\) when \(n\) is odd. For even \(n\), the formal derivative \(f'=(n+1)z^n=z^n\) is nonzero at every root of \(\Phi\), so the zeros are simple. For odd \(n\), the derivative vanishes; the second Hasse derivative at a primitive cube root \(\lambda\) equals \(1+\binom{n+1}{2}\lambda^{n-1}\). If \(n\equiv3\pmod4\), this is \(1\). If \(n\equiv1\pmod4\), this is \(1+\lambda^{-1}=\lambda\). Either way it is nonzero, proving exact multiplicity two. Hence the kernel of \(F_M^t\) on its nilpotent primary component has dimension \(2\min(et,2k)\), and the sharp nilpotent index is \(\lceil2k/e\rceil\), namely \(1\) for odd \(n\) and \(2k\) for even \(n\). The complementary periodic subspace has dimension \(2n-4k\). Multiplying its size by the nilpotent-kernel sizes proves the formulas for \(Q_M(t)\), the sharpness, and the eventual-phase fibres.

**Circular prism.** Put \(R_P=\mathbb F_2[z]/(z^n+1)\) and represent the two rows as \(R_P^2\). With \(u=z+z^{-1}\), the update matrix is
\[
B=\begin{pmatrix}u&1\\1&u\end{pmatrix},\qquad
B^2=(u+1)^2I=\left(\frac{\Phi(z)}z\right)^2I.
\]
Its determinant is \((\Phi(z)/z)^2\), so it is invertible when \(3\nmid n\). Otherwise \(\Phi\) occurs with exponent exactly \(k\) in \(z^n+1\), and the primary summand of \(R_P^2\) at \(\Phi\) has dimension \(4k\); the complement is invertible. Set \(q=\Phi(z)/z\), a unit times \(\Phi\). Since an entry of \(B\) is the unit \(1\) and its determinant is \(q^2\), its Smith invariant factors over the local principal ring at \(\Phi\) are \((1,q^2)\). From \(B^{2r}=q^{2r}I\), the rank loss on the primary component at even time \(2r\) is \(4\min(2r,k)\); from \(B^{2r+1}=q^{2r}B\), the loss at odd time \(2r+1\) is \(2[\min(2r,k)+\min(2r+2,k)]\). If \(k=1\), these losses are \(0,2,4\) at times \(0,1,2\), so the exact maximal transient is two. If \(k\ge2\) (necessarily an even power of two), the loss at each \(0\le t\le k\) is \(4t\), attaining \(4k\) for the first time at \(t=k\). Thus the sharp maximal transient is \(k\) and the claimed \(Q_P(t)\) follows. Both graphs have the same recurrent-space dimension \(2n-4k\), completing the comparison.

**Temporal orbit counts.** On \(R_M\), \(F_M^r-I\) multiplies by the unit \(z^{-r}\) times \(f^r+z^r\). The kernel-dimension lemma above gives the displayed fixed-point count. Every fixed point of \(F_M^r\) belongs to a genuine periodic orbit with period dividing \(r\), even when \(F_M\) is not bijective on the full configuration space. Möbius inversion gives the exact number of primitive cycles, without any claim that the raw cycle counts are bounded uniformly in \(n\).

## Verification
The accompanying standalone program `verify.py` computes the two adjacency operators directly from three-neighbour lists and tests ranks of every power through one beyond the predicted maximal transient for all \(3\le n\le128\). It separately updates every individual binary configuration for all \(3\le n\le9\), constructs the full recurrent image set, and compares the first-entry distribution to the formulas. The recorded output reports `VERIFY_OK`, 909 rank comparisons, 14 complete finite-state graph instances, and 699008 direct state evaluations. These calculations are finite checks supporting, not replacing, the all-size polynomial proof.

Examples: for \(n=6\), both graphs have 16 periodic states and eventual-phase fibres of size 256, but the sharp maximal transients are 2 (prism) and 4 (Möbius). For \(n=12\), both have 256 periodic states and eventual-phase fibres of size 65536, while the maximal transients are 4 and 8.

## Relationship to prior work
Polynomial and minimal-polynomial descriptions of finite linear cellular automata and their periodic or transient components are classical; in particular, Martin, Odlyzko and Wolfram (1984) develop algebraic state-transition methods for finite cyclic cellular automata, and Lettieri, Stevens and Thomas (2006) analyze Rule 90 and Rule 150, including general minimal-polynomial methods and finite-cycle properties. Chang and Su's public 2016 preprint investigates reversibility of linear cellular automata with periodic boundary conditions on Cayley trees, a different graph family. The present claim concerns the *specific cubic prism/Möbius pair* with the same local parity rule, including exact equalities of recurrent and fibre counts and the opposite sharp transient responses to one crossed seam. These conclusions require the explicit \(\Phi\)-adic multiplicities of the two different update operators, rather than their shared general linearity alone.

## Limitations
This is a deterministic finite-field statement, not a claim about stochastic excitation, real-valued diffusion, asynchronous updating, or general cubic graphs. The primitive-period formula is an exact gcd expression rather than a closed characterization of which integers occur as primitive periods for arbitrary \(n\). Historical equivalence in unindexed literature cannot be excluded; in particular, two adjacent general additive-automata sources were available only through abstracts at the time of comparison. The result has not undergone independent audit.

## References
1. O. Martin, A. M. Odlyzko, S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258. DOI: 10.1007/BF01223745.
2. S. Lettieri, J. G. Stevens, D. M. Thomas, *Characteristic and Minimal Polynomials of Linear Cellular Automata*, Rocky Mountain Journal of Mathematics **36** (2006), 1077–1092. DOI: 10.1216/rmjm/1181069447.
3. C.-H. Chang and J.-Y. Su, *Reversibility of Linear Cellular Automata on Cayley Trees with Periodic Boundary Condition*, public preprint arXiv:1603.01679, first submitted 2016-03-05.
4. R. A. Dow, *Additive Cellular Automata and Global Injectivity*, Physica D **110** (1997), 67–91. DOI: 10.1016/S0167-2789(97)00074-2.
5. N. Ganguly, B. K. Sikdar, P. Pal Chaudhuri, *Exploring Cycle Structures of Additive Cellular Automata*, Fundamenta Informaticae **87** (2008), 137–154. DOI: 10.3233/FUN-2008-87202.
