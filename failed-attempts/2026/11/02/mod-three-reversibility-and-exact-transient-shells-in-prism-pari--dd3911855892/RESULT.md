# Mod-three reversibility and exact transient shells in prism parity dynamics

## Finding

For every integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the labelled prism, with two cyclic layers and one rung joining corresponding sites. Under the synchronous neighbor-XOR rule on binary vertex states, every configuration is periodic from time zero **if and only if** \(3\nmid n\). Otherwise write \(n=2^s m\) with \(m\) odd and \(e=2^s\). Exactly \(2^{2n-4e}\) of the \(2^{2n}\) configurations are periodic, so the periodic fraction is \(2^{-4e}\).

Write \(T(x)\) for the least nonnegative integer such that \(F^{T(x)}(x)\) lies on a periodic orbit. For \(3\mid n\), put \(P=2^{2n-4e}\). If \(e=1\), the complete first-entry counts are
\[
\#\{T=0\}=P,\qquad \#\{T=1\}=3P,\qquad \#\{T=2\}=12P.
\]
If \(e\ge2\), the complete distribution is
\[
\#\{T=0\}=P,\qquad
\#\{T=t\}=15P\,16^{t-1}\quad(1\le t\le e).
\]
All other shells are empty. In particular, the maximal first-entry time is exactly \(2\) when \(n\) is an odd multiple of three, and exactly \(e\) when \(n\) is an even multiple of three.

A complementary exact orbit census holds for \(n=2^s\), \(s\ge2\). Every state is periodic with period dividing \(n/2\). There are exactly \(16\) fixed configurations and, for every integer \(1\le j\le s-1\), the number of distinct orbits of primitive period \(2^j\) is
\[
\boxed{\frac{2^{2^{j+2}}-2^{2^{j+1}}}{2^j}.}
\]
All displayed orbit types occur; no other periods occur. Without the rung edges, the same two cyclic layers under neighbor-XOR reach zero by time \(n/2\), whereas adding those rungs makes the coupled dynamics a bijection.

## Assumptions and scope

The rim length is an integer \(n\ge3\). The vertex set is \(\{(i,a):i\in\mathbb Z/n\mathbb Z,\ a\in\{0,1\}\}\) and each \((i,a)\) is adjacent to \((i-1,a)\), \((i+1,a)\), and \((i,1-a)\). All vertex states lie in \(\mathbb F_2\). The update is simultaneous and excludes self-loops. Periodic points are labelled configurations, while a primitive orbit is identified modulo temporal rotation, not graph automorphisms. First-entry time is measured from the original configuration, with time zero allowed. The claims are about this linear parity rule, not threshold-majority dynamics.

## Proof

**Polynomial representation.** Put \(R=\mathbb F_2[z,z^{-1}]/(z^n-1)\), where \(z\) cyclically shifts a ring configuration. Let \(A=z+z^{-1}\). In the two-layer basis, the update is
\[
F=\begin{pmatrix}A&1\\1&A\end{pmatrix}.
\]
Over \(\mathbb F_2\), swapping the layers has a nontrivial Jordan block with sole eigenvalue one. Therefore \(F\) is similar, over \(R\), to
\[
\begin{pmatrix}B&1\\0&B\end{pmatrix},\qquad
B=1+A=z^{-1}(z^2+z+1).
\]
The polynomial \(q=z^2+z+1\) is irreducible over \(\mathbb F_2\), and \(q\mid z^n-1\) precisely when \(3\mid n\). Consequently \(F\) is invertible exactly when \(3\nmid n\). An invertible map on a finite state space makes every state periodic.

**Primary decomposition and exact first-entry shells.** Suppose \(3\mid n\). Write \(n=e m\) with \(e=2^s\) and \(m\) odd. Because \(z^n-1=(z^m-1)^e\) in characteristic two, the multiplicity of \(q\) is exactly \(e\). By the Chinese remainder theorem, \(R\) splits as its \(q\)-primary component \(R_q=\mathbb F_2[z]/(q^e)\), having binary dimension \(2e\), and a complementary component on which \(F\) is invertible. The full nilpotent primary summand \(R_q^2\) therefore has binary dimension \(4e\). The periodic states are exactly those with zero primary component, giving \(P=2^{2n-4e}\).

On \(R_q^2\), the conjugated matrix \(N\) has diagonal entry \(B\), with \(B\) a unit times \(q\). For even \(t\), the off-diagonal terms cancel and \(N^t=B^t I\), whence
\[
\dim_{\mathbb F_2}\ker N^t=4\min(t,e).
\]
For odd positive \(t\), the matrix has entries \(B^t,B^{t-1},0,B^t\), and its local Smith invariants are \(B^{t-1}\) and \(B^{t+1}\). Thus
\[
\dim_{\mathbb F_2}\ker N^t
=2\left(\min(e,t-1)+\min(e,t+1)\right).
\]
For \(e=1\) this is \(2\) at \(t=1\), and the nilpotent kernel reaches dimension \(4\) at \(t=2\). For \(e\ge2\), necessarily even, both formulas simplify for every nonnegative \(t\) to \(4\min(t,e)\). The number of states entering the periodic set by time \(t\) is \(P\,|\ker N^t|\); subtraction of successive cumulative counts gives precisely the claimed shells. Their positivity proves sharpness of the maximal entry times.

**Power-of-two rims and primitive periods.** Let \(n=2^s\ge4\), so \(z^n-1=(z+1)^n\). Set \(u=z+1\). Then \(A=z^{-1}u^2\), hence \(A^{n/2}=0\). The identity \(F^2=(1+A^2)I\) yields \(F^{n/2}=I\). For \(j\ge1\),
\[
F^{2^j}-I=A^{2^j}I=z^{-2^j}u^{2^{j+1}}I.
\]
Therefore \(\dim_{\mathbb F_2}\ker(F^{2^j}-I)=\min(2^{j+2},2n)\). For period one, conjugation gives \(F-I\sim\left(\begin{smallmatrix}A&1\\0&A\end{smallmatrix}\right)\). Its local Smith invariants are one and \(A^2\), giving exactly \(2^4=16\) fixed configurations. Since every orbit period divides \(n/2\), the positive powers of two are the only possibilities. Differences of the counts fixed by consecutive powers of two, divided by their primitive periods, yield the displayed orbit formula. In particular the \(n/2\)-period class is nonempty, so the maximal period is sharp. On the disconnected pair of rim cycles, the update is \(A\oplus A\), which becomes zero at time \(n/2\). This completes the comparison.

## Verification

The standalone standard-library program `prism_parity_verify.py` was run directly from its delivered directory, producing `prism_parity_verify.out` and terminating with the exact marker `PRISM_PARITY_VERIFY_OK`. It independently enumerates all configurations on prisms of rim sizes \(3\) through \(8\), a total of \(87{,}360\) labelled configurations, and checks complete first-entry histograms. It separately computes binary ranks of the actual update matrices for rim sizes \(3,4,5,6,7,8,9,10,12,15,18,24\), as well as fixed-space dimensions and orbit counts for all power-of-two rim sizes from \(4\) to \(128\). The proof above, not the finite tests, establishes the results for all \(n\).

## Relationship to prior work

Classical additive cellular-automaton literature, including Cordovil–Dilão–Noronha da Costa (1986) and Ward (2000), develops the polynomial viewpoint and temporal periodic-point methods. Boyle–Lee studies jointly periodic one-dimensional automata; Dennunzio–Di Lena–Margara (2012) studies strictly temporally periodic points for broader shift systems. Those methods motivate the question but their inspected statements do not present the exact \(C_n\square K_2\) neighbor-XOR mod-three reversibility dichotomy or the first-entry shell sizes above. These general methods and periodic-point themes are not claimed as new.

## Limitations

This theorem concerns one fixed deterministic linear rule on the indicated labelled prisms. It does not determine every primitive period at arbitrary rim lengths (the full orbit census is given only for dyadic rim lengths), nor does it describe perturbations to other cellular rules. The originality comparison is based on accessible sources; an equivalent result in unindexed or inaccessible earlier linear-automata literature cannot be excluded. Numerical checks do not replace the all-size algebraic argument.

## References

1. R. Cordovil, R. Dilão and A. Noronha da Costa, “Periodic Orbits for Additive Cellular Automata,” *Discrete & Computational Geometry* **1** (1986), 277–288. DOI: 10.1007/BF02187700.
2. T. B. Ward, “Additive Cellular Automata and Volume Growth,” *Entropy* **2** (2000), 142–167. DOI: 10.3390/e2030142.
3. M. Boyle and B. Lee, “Jointly Periodic Points in Cellular Automata: Computer Explorations and Conjectures,” *Experimental Mathematics* **16** (2007), 293–302. DOI: 10.1080/10586458.2007.10129005.
4. A. Dennunzio, P. Di Lena and L. Margara, “Strictly Temporally Periodic Points in Cellular Automata,” 2012, arXiv:1208.2770v1 (publicly submitted 2012-08-14); DOI: 10.4204/EPTCS.90.18.
5. W. Chin, B. Cortzen and J. Goldman, “Linear Cellular Automata with Boundary Conditions,” *Linear Algebra and Its Applications* **322** (2001), 193–206. DOI: 10.1016/S0024-3795(00)00227-5 (full text not inspected).
