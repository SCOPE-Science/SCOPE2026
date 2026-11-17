# Complete primitive-cycle census for binary parity dynamics on prism graphs

## Finding
For each integer \(n\ge3\), let \(G_n=C_n\square K_2\) be the simple, undirected prism graph and let \(F_n\) simultaneously replace the binary state at each vertex by the XOR of the states at its three distinct neighbors. **The number of primitive temporal cycles of every possible length is explicit.**

Set \(f_n(z)=z^n+1\), \(q(z)=z^2+z+1\), and \(P_t(z)=q(z)^t+z^t\) in \(\mathbb F_2[z]\), for any integer \(t\ge1\). Write
\[
e_n(t)=\begin{cases}
\deg\gcd(f_n,P_t^2),&t\text{ odd},\\
2\deg\gcd(f_n,P_t),&t\text{ even}.
\end{cases}
\]
Then exactly \(2^{e_n(t)}\) labelled states satisfy \(F_n^t(s)=s\), and the number of distinct **primitive cycles of least temporal period** \(t\) equals
\[
\boxed{\mathcal C_n(t)=\frac1t\sum_{d\mid t}\mu(t/d)\,2^{e_n(d)}.}
\]
This counts cycles rather than simply the periodic points, at arbitrary length and graph size, without assuming a maximum possible period.

A closed-form classification is available for both arithmetic families \(n=2^k\) with \(k\ge2\), and \(n=3\cdot2^k\) with \(k\ge0\). Put \(v=2^k\), and let \(A_j\) be the number of **recurrent** states whose least period divides \(2^j\). For these families,
\[
\boxed{A_0=2^{\min(v,4)},\qquad A_j=2^{2\min(v,2^{j+1})}\quad(j\ge1).}
\]
All recurrent cycle lengths are powers of two. There are \(A_0\) fixed-point cycles, and for \(j\ge1\), exactly
\[
\boxed{\frac{A_j-A_{j-1}}{2^j}}
\]
primitive cycles of length \(2^j\). In particular, the longest temporal period is \(2\) for \(v=1,2\) and \(v/2\) for \(v\ge4\); the largest period really occurs in each case. Thus the entire recurrent-state period distribution agrees for the distinct rim lengths \(v\) and \(3v\) when both define simple prisms, despite the latter graph having three times as many rim vertices.

## Assumptions and scope
All vertices are labelled by a layer \(0,1\) and a site in \(\mathbb Z/n\mathbb Z\). There are undirected edges from each site to the preceding and succeeding sites in its own layer and to its corresponding site across the rung. We require \(n\ge3\), ensuring distinct neighbors. There are no self-loops, multiple edges, stochastic updates or affine offsets. Every update is simultaneous over \(\mathbb F_2\). A periodic point is a labelled configuration that returns to itself; an orbit is counted once regardless of its temporal phase, without quotienting by any spatial automorphism. The gcd is monic in \(\mathbb F_2[z]\) and the degree is zero for a constant gcd. The Möbius function is the ordinary arithmetic one.

## Proof
Write \(R=\mathbb F_2[z]/(z^n+1)\), with \(z\) representing a cyclic shift. A state has two components \((x,y)\in R^2\), and the update is
\[
F_n(x,y)=(Lx+y,x+Ly),\qquad L=z+z^{-1}.
\]
The invertible coordinate change \(u=x+y\), \(w=x\) conjugates \(F_n\) to
\[
T(u,w)=(a u,u+a w),\qquad a=L+1=z^{-1}q(z).
\]
For every positive integer \(t\), because the off-diagonal nilpotent matrix squares to zero and commutes with scalar multiplication,
\[
T^t=\begin{pmatrix}a^t&0\\(t\bmod2)a^{t-1}&a^t\end{pmatrix}.
\]
Let \(b=a^t+1=z^{-t}P_t\). If \(t\) is even, \(T^t-I\) is diagonal with entries \(b\), so its binary kernel dimension is twice \(\deg\gcd(f_n,P_t)\). If \(t\) is odd, \(T^t-I\) has diagonal \(b\) and off-diagonal \(a^{t-1}\). Work at each irreducible factor of \(f_n\). At factors not dividing \(b\), this matrix is invertible. At every factor dividing \(b\), the element \(a\) is a unit (because \(b=0\) implies \(a^t=1\) in the residue field). Hence \(a^{t-1}\) is a local unit. Elementary row and column operations reduce the matrix over this local principal-ideal ring to Smith factors \(1,b^2\) (their product is its determinant \(b^2\)). The local kernel dimension equals the degree of the relevant gcd with \(b^2\), counting multiplicity. Summing local contributions, and removing the unit \(z^{-t}\), proves \(e_n(t)\). The number of fixed configurations is \(2^{e_n(t)}\). Any point fixed by \(F_n^t\) is periodic, and any primitive \(d\)-cycle contributes precisely \(d\) points fixed by \(F_n^t\) when \(d\mid t\). Möbius inversion gives \(\mathcal C_n(t)\) without any assumption about invertibility of the global map.

For the closed families write \(v=2^k\). If \(n=v\), then \(f_n=(z+1)^v\); if \(n=3v\), then \(f_n=(z+1)^v q^v\). In the second case the \(q\)-primary summand is nilpotent under \(T\), so no nonzero state there can be recurrent. The remaining recurrent module is \(R_v^2\), where \(R_v=\mathbb F_2[z]/((z+1)^v)\). On that module \(a=1+s\) with \(s=z^{-1}(z+1)^2\) of exact \((z+1)\)-adic valuation two. Because \(z\) and \(1+s\) are units, \(T\) is invertible there.

For \(j\ge1\), the \(2^j\)-th power has vanishing off-diagonal entry and diagonal \(a^{2^j}=1+s^{2^j}\), using characteristic two. Thus \(T^{2^j}-I\) is diagonal and its two coordinates each contribute \(\min(v,2^{j+1})\) to the kernel dimension. Therefore \(A_j=2^{2\min(v,2^{j+1})}\). For \(j=0\), \(T-I\) has off-diagonal entry one and diagonal \(s\), hence local Smith factors \(1,s^2\), and \(A_0=2^{\min(v,4)}\). Since a sufficiently high power of two kills \(s\), the recurrent map has power-of-two order; no other primitive periods occur. For \(v\ge4\), the highest period is \(v/2\), because the fixed-point population grows strictly from the preceding power-of-two stage; for \(v=1,2\) the off-diagonal Jordan extension produces period two. Subtract successive fixed-point populations and divide by the orbit length. All assertions follow.

## Verification
The accompanying `verify_prism.py` compares exact \(\mathbb F_2\) matrix fixed-point dimensions against the polynomial gcd formula for \(3\le n\le44\), positive times through \(t=34\). Its independent rank tests also check the underlying update implementation. `verify_prism_states.py` exhaustively enumerates labelled trajectories on all prisms with \(3\le n\le8\), checks their periodic-state and orbit counts, and confirms the gcd counts at small sizes. `verify_power_two.py` independently computes the polynomial gcd census on \(n=v\) and \(n=3v\) (where valid), through \(v=256\), and checks the closed power-of-two laws. Captured outputs accompany the source. All computation is exact; finite testing is not used in place of the all-size proof.

For example, on \(C_8\square K_2\) there are 16 fixed states, 120 primitive two-cycles and 16,320 primitive four-cycles. The same recurrent-cycle census holds on \(C_{24}\square K_2\), although the latter also has transient configurations. On \(C_3\square K_2\) the recurrent component has two fixed points and one two-cycle.

## Relationship to prior work
Martin, Odlyzko and Wolfram (1984) establish the general cyclic-polynomial machinery for additive cellular automata, including extensions beyond a single scalar layer; Tadaki (1993, 1994) analyzes scalar periodic rules 90 and 150. Those foundational methods are used here rather than claimed as new. A prior prism-specific result already determines invertibility, zero-primary Jordan blocks, and transient-entry counts for this **same adjacency update**; those claims are not offered as new. The present result instead completes the separate **primitive temporal orbit census**, including the local Smith calculation for odd periods and the evaluated power-of-two cycle populations. This is not a renaming of the previous transient count: two maps can have the same nilpotent Jordan blocks and different orders and orbit counts on their invertible summands. Ogihara and Uchizawa's 2020 work studies XOR graph dynamics primarily through computational complexity, not this family census. The novelty comparison is specific to statements of all-period counts, not to the general availability of polynomial methods.

## Limitations
The theorem applies only to binary XOR dynamics on simple prism graphs. It does not provide an elementary listing of all possible period lengths for arbitrary \(n\); it provides an exact executable gcd/Möbius formula at any queried period and a complete explicit list for two natural infinite subfamilies. It does not improve, redo, or amend the already-established transient/Jordan classification. A broader or unpublished specialized orbit-census formula might cover the calculation; priority remains qualified. The finite checks do not establish universal validity, which is proved algebraically above. Independent scientific validation has not been performed.

## References
1. S. Wolfram, “Statistical mechanics of cellular automata,” *Reviews of Modern Physics* 55 (1983), 601–644, DOI: 10.1103/RevModPhys.55.601 (published 1983-07-01).
2. O. Martin, A. M. Odlyzko and S. Wolfram, “Algebraic properties of cellular automata,” *Communications in Mathematical Physics* 93 (1984), 219–258, DOI: 10.1007/BF01223745.
3. S.-i. Tadaki, “Orbits in one-dimensional finite linear cellular automata,” arXiv:cond-mat/9305012 (submitted 1993-05-14).
4. S.-i. Tadaki, “Periodicity of cylindrical linear cellular automata,” arXiv:patt-sol/9412003 (submitted 1994-12-15).
5. M. Ogihara and K. Uchizawa, “Synchronous Boolean Finite Dynamical Systems on Directed Graphs over XOR Functions,” *MFCS 2020*, DOI: 10.4230/LIPIcs.MFCS.2020.76.
