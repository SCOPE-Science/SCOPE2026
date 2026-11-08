# Hub-induced Jordan anomalies and exact transient populations for parity waves on wheel graphs

## Finding

For every integer \(n\ge5\), and every finite field \(\mathbb F_Q\) of characteristic two with \(Q=2^f\), consider the labelled wheel \(W_{n+1}=K_1\vee C_n\). The hub has value \(a\), the cyclic rim has values \(x_i\), and every vertex synchronously takes the sum of its neighboring values, without retaining its own value:
\[
F_n(a,x)=\left(\sum_{i=0}^{n-1}x_i,\ (x_{i-1}+x_{i+1}+a)_{i\in\mathbb Z/n\mathbb Z}\right).
\]
Write \(h=2^{\nu_2(n)}\). If \(n\) is odd, \(F_n\) is bijective and all states have first-periodic-entry time zero. If \(n\) is even, its complete zero-primary Jordan form is
\[
\mathcal J_0(F_n)=
\begin{cases}
J_3(0),&h=2,\\
J_3(0)\oplus J_1(0)^{\oplus2},&h=4,\\
J_{h/2}(0)^{\oplus2}\oplus J_1(0),&h\ge8.
\end{cases}
\]
Here \(J_s(0)\) is a nilpotent Jordan block of size \(s\). The invariant complement is invertible and has dimension \(n-h\). Let \(d_0=0\), and for each nonnegative integer \(t\) let \(d_t\) be the sum of \(\min(t,s)\) over these nilpotent block sizes. Then the exact number \(E_t\) of labelled configurations with least nonnegative entrance time \(t\) into an eventual temporal cycle is
\[
E_0=Q^{n-h},\qquad
E_t=Q^{n-h+d_t}-Q^{n-h+d_{t-1}}\quad(t\ge1).
\]
Thus the maximum entrance time is \(3\) when \(h\in\{2,4\}\), and \(h/2\) when \(h\ge8\); for odd \(n\), \(E_0=Q^{n+1}\) and all other \(E_t=0\). In particular, a wheel with even rim always has nonperiodic states, but adjoining its hub creates an exceptional three-step transient at the smallest two even two-adic scales.

## Assumptions and scope

The wheel has one hub adjacent to all \(n\) rim vertices and the rim induces the simple undirected cycle \(C_n\). There are no self-loops, and all additions are in \(\mathbb F_Q\), characteristic two. Vertices are labelled; configuration counts do not quotient by graph symmetry. Time is discrete, nonnegative, and synchronous. The exact entrance time of a state \(y\) is the smallest integer \(t\ge0\) such that \(F_n^t(y)\) belongs to a temporal cycle. Finite-field linear dynamics admits a Fitting decomposition, so this time is controlled precisely by its nilpotent component. The claimed family starts at \(n=5\); the exceptional rims of length three and four are not part of the novelty claim.

## Proof

**Polynomial representation and invariant splitting.** Identify the rim vector space with
\[
R=\mathbb F_Q[z]/(z^n-1)
\]
by sending the \(i\)-th rim coordinate to the coefficient of \(z^i\). Define \(e=1+z+\cdots+z^{n-1}\), \(c=z+z^{-1}\), and \(\epsilon(f)=f(1)\). The wheel update is precisely
\[
F_n(a,f)=(\epsilon(f),\,cf+ae).
\]
Write \(n=hm\) with \(m\) odd, and set \(t=z+1\). In characteristic two,
\[
z^n-1=(z^m-1)^h=t^h g(z)^h,
\qquad g(z)=\frac{z^m-1}{z+1},\qquad g(1)=1.
\]
Since \(t\) and \(g\) are coprime, the Chinese remainder theorem gives invariant spaces \(R_0\cong\mathbb F_Q[t]/t^h\) and \(R_1\cong\mathbb F_Q[z]/g(z)^h\), of respective dimensions \(h\) and \(n-h\). The map \(\epsilon\) annihilates \(R_1\), and \(e\) has zero \(R_1\)-projection. On \(R_1\), \(c=t^2/z\) is a unit, so \(F_n\) acts invertibly. On \(R_0\), Frobenius yields \(g(1+t)^h\equiv g(1)^h=1\pmod{t^h}\), whence the local projection of \(e=t^{h-1}g(z)^h\) is exactly \(t^{h-1}\). Thus the remaining operator, on a vector space of dimension \(h+1\), is
\[
N_h(a,f)=\left(f(0),\,\frac{t^2}{1+t}f+a t^{h-1}\right),
\quad f\in\mathbb F_Q[t]/t^h.
\]

**Odd rim.** When \(h=1\), the local multiplier \(t^2/(1+t)\) is zero and \(N_1(a,f)=(f,a)\). It is invertible, as is the \(R_1\) component. Hence the whole wheel update is invertible; over its finite state space it is a permutation, so all states are periodic.

**Even rim: local power formula.** Assume \(h\ge2\). Put \(c_0=t^2/(1+t)\) and \(e_0=t^{h-1}\). Both \(\epsilon(c_0f)\) and \(\epsilon(e_0)\) vanish, and \(c_0e_0=0\). Direct multiplication gives
\[
N_h^2(a,f)=(0,c_0^2 f+f(0)e_0),
\qquad N_h^j(a,f)=(0,c_0^j f)\quad(j\ge3).
\]
For \(h=2\), \(c_0=0\), while \(e_0=t\). Therefore \(\operatorname{rank}N_2=2\), \(\operatorname{rank}N_2^2=1\), and \(N_2^3=0\): its sole Jordan block has length three. For \(h=4\), \(c_0=t^2+t^3\); the hub coordinate is tied to the coefficient of \(t^2\) in the rim output, so \(\operatorname{rank}N_4=2\). Moreover \(c_0^2=0\) but \(f(0)e_0\) can be nonzero, so \(\operatorname{rank}N_4^2=1\) and \(N_4^3=0\). On the five-dimensional local space, the Jordan partition is \((3,1,1)\).

For \(h\ge8\), the image of \(N_h\) is the graph of the linear functional extracting the coefficient of \(t^2\) from the ideal \(t^2R_0\). Because \(e_0\in t^2R_0\), its dimension is \(h-2\). The image of \(N_h^2\) is all of \(t^4R_0\), since \(e_0\in t^4R_0\), hence it has dimension \(h-4\). For \(j\ge3\), the power formula shows that its image is exactly \(t^{2j}R_0\), because \((1+t)^{-j}\) is a unit. Consequently
\[
\operatorname{rank}N_h^j=\max(h-2j,0)\quad(j\ge1).
\]
The Jordan-partition recovery formula says the number of blocks of length at least \(j\) is \(\operatorname{rank}N_h^{j-1}-\operatorname{rank}N_h^j\), with rank at power zero equal to \(h+1\). It gives three blocks at level one, and exactly two at all levels from two through \(h/2\). Hence the Jordan partition is \((h/2,h/2,1)\). This completes the classification and also proves that no nonzero eigenvalues occur on the local block.

**Entrance-time populations.** Under the Fitting decomposition the invertible summand contributes a free factor of size \(Q^{n-h}\). A configuration in the nilpotent summand has entered the periodic set by time \(t\) exactly when it belongs to \(\ker N_h^t\). Its dimension is \(d_t\). Therefore the number of states whose entrance time is at most \(t\) is \(Q^{n-h+d_t}\), and consecutive differences give the exact populations above. Since each listed largest nilpotent Jordan block contains a vector of full height, the largest entrance time is sharp. \(\square\)

## Verification

The self-contained exact-arithmetic programs `verify/check_wheel_matrix.py` and `verify/check_local_module.py` are supplied. The first constructs the full labelled binary adjacency matrix, checks 673 matrix-power nullities for circumferences 3 through 100 and five further large circumferences, and independently enumerates all \(262128\) states for circumferences 3 through 16 using functional-graph indegree peeling. The second constructs the truncated-polynomial local operator without using the graph adjacency matrix, verifies all predicted Jordan nullities up to saturation for seven powers of two through 128, and checks the exact cubic power formula on each basis vector, for 536 tests. Their captured outputs are `verify/check_wheel_matrix.out` and `verify/check_local_module.out`. The exhaustive finite checks corroborate, but are not substituted for, the all-length proof.

## Relationship to prior work

Wolfram's early cellular-automaton program and Martin–Odlyzko–Wolfram's algebraic study establish the finite-ring Rule 90 framework and its polynomial approach. Their inspected analysis treats unmodified cyclic arrays and periodic lattices, rather than the characteristic-two zero-primary block created by a wheel's hub. Lettieri–Stevens–Thomas extend minimal-polynomial analysis of the original one-dimensional Rule 90 and 150 setting. Cipta calculates ordinary wheel adjacency spectra over the complex numbers; those eigenvalues do not determine Jordan block lengths modulo two. This theorem relies on standard polynomial module and Fitting techniques, not claims of inventing them. Its new target is the complete wheel-specific zero-primary Jordan partition and exact first-entry-time population across all circumference parameters and all finite fields of characteristic two.

## Limitations

The result does not determine primitive temporal periods on the invertible subspace or classify variants with self-inclusive updates, asynchronous rules, or other characteristics. The literature comparison found no covering wheel-specific characteristic-two transient census in inspected sources and mathematical research-record searches, but cannot exclude an unindexed equivalent specialization. The derivation of the local Jordan partition is analytical; computational checks remain finite. No independent audit has been performed.

## References

1. S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics **55** (1983), 601–644. https://doi.org/10.1103/RevModPhys.55.601.
2. O. Martin, A. M. Odlyzko, S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258. https://doi.org/10.1007/BF01223745. Author-accessible PDF: https://content.wolfram.com/sw-publications/2020/07/algebraic-properties-cellular-automata.pdf.
3. H. Cipta, *The Spectrum Of Wheel Graph Using Eigenvalues Circulant Matrix*, International Journal of Mathematics Trends and Technology **66** (2020), 198–204. https://doi.org/10.14445/22315373/IJMTT-V66I6P520.
4. S. Lettieri, J. G. Stevens, D. M. Thomas, *Characteristic and Minimal Polynomials of Linear Cellular Automata*, Rocky Mountain Journal of Mathematics **36** (2006), 1077–1092. https://doi.org/10.1216/rmjm/1181069447.
