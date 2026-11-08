# Sharp cyclic–reshuffling rate reversal for a three-line tight Kaczmarz frame

## Finding

A redundant three-row planar tight frame gives an exact, strictly reversed comparison between *short* and *long* Kaczmarz horizons. For the three unit normals
\[
a_1=(1,0),\qquad a_2=(1/2,\sqrt3/2),\qquad a_3=(-1/2,\sqrt3/2),
\]
consider a consistent linear system with these row normals and a unique solution. Every row update uses the same relaxation parameter \(0<\omega<2\). One *epoch* performs exactly three updates. Compare (i) a fixed cyclic order repeated each epoch, (ii) a fresh independent, uniformly distributed permutation of all three rows each epoch, and (iii) three independent uniform row draws with replacement per epoch. Error is measured in squared Euclidean norm.

For every fixed cyclic order, the squared asymptotic worst-case epoch factor is uniquely minimized at
\[
\omega_C=4\sqrt3-6=0.9282032302\ldots,\qquad
c_*=1351-780\sqrt3=0.0003700962\ldots.
\]
For freshly independent random reshuffling, every deterministic initial error \(e_0\) satisfies the **exact**, all-horizon identity
\[
\mathbb E\|e_k\|_2^2=r(\omega)^k\|e_0\|_2^2,
\qquad r(\omega)=(1-\omega)^3+\frac{\omega^6}{32}.
\]
This factor is uniquely minimized at the root \(\omega_R\in(0,1)\) of
\[
\omega_R^5=16(1-\omega_R)^2,
\qquad \omega_R=0.8388699348\ldots,
\qquad r_*=0.0150731506\ldots.
\]
With replacement the exact factor per three independent draws is
\[
u(\omega)=\left(1-\frac{\omega(2-\omega)}2\right)^3,
\qquad u(\omega)-r(\omega)=\frac{3\omega^2(2-\omega)^4}{32}>0.
\]

There is a sharp finite-horizon reversal **when each method uses its own asymptotic-rate-optimal relaxation**: for one epoch, random reshuffling has lower worst-case expected squared error than the fixed cyclic scheme, while for **every integer number of epochs \(k\ge2\)** the fixed cyclic scheme has lower worst-case squared error than optimally reshuffled sampling:
\[
\|S(\omega_C)\|_2^2>r_*;
\qquad \|S(\omega_C)^k\|_2^2<r_*^k\quad(k\ge2).
\]
This compares the fixed cyclic worst-case direction with the reshuffling expectation, which is isotropic. It does not claim that the cyclic relaxation is separately optimal at each finite horizon, or that cycling is universally better for other matrices.

## Assumptions and scope

Let \(A\) be the \(3\times2\) real matrix whose rows are the displayed unit normals, and let \(Ax=b\) be consistent; the unique solution is \(x_*\). The row-normal Gram sum is \(A^{\mathsf T}A=\tfrac32I_2\). For any initial \(x_0\in\mathbb R^2\), put \(e_0=x_0-x_*\). A relaxed Kaczmarz update on row \(i\) is
\[
e\longmapsto P_i(\omega)e,\qquad P_i(\omega)=I_2-\omega a_i a_i^{\mathsf T},\quad 0<\omega<2.
\]
For an order \(\pi\) of the three indices write \(S_\pi=P_{\pi(3)}P_{\pi(2)}P_{\pi(1)}\). Fixed cyclic means the same \(S_\pi\) is iterated; reshuffling means \(\pi\) is independent uniform over the six permutations at each epoch. With-replacement means each of the three update indices is drawn uniformly and independently, also across epochs. Every probability or expectation is over these draws only; there is no measurement noise or inconsistency.

For cyclic updates the **asymptotic worst-case squared factor** means \(\rho(S_\pi)^2\); the finite-horizon worst case is \(\|S_\pi^k\|_2^2\), not in general its spectral-radius power. For both random schemes, factors below are exact conditional second moments, not only bounds.

## Proof

**1. Fixed-cycle characteristic polynomial.** The six row-line directions form a dihedrally symmetric equiangular system. Orthogonal symmetries permute their rank-one projectors transitively over the six row permutations, so all fixed sweeps have the same eigenvalues. For \(S=P_3P_2P_1\), direct multiplication gives
\[
T(\omega)=\operatorname{tr}S=\frac{(\omega-2)(\omega^2+8\omega-8)}8,
\qquad d(\omega)=\det S=(1-\omega)^3.
\]
The characteristic polynomial is \(\lambda^2-T(\omega)\lambda+d(\omega)\), with discriminant
\[
\Delta(\omega)=\frac{\omega^4(\omega^2+12\omega-12)}{64}.
\]
The unique positive zero of \(\omega^2+12\omega-12\) is \(\omega_C=4\sqrt3-6\). When \(0<\omega<\omega_C\), the characteristic roots are complex conjugates and \(\rho(S)^2=d(\omega)=(1-\omega)^3\), strictly decreasing. At \(\omega_C\) the roots coalesce at \(\lambda_C=-\sqrt{d(\omega_C)}\). When \(\omega_C<\omega\le6/5\), \(T(\omega)<0\) and \(T'(\omega)=(3\omega^2+12\omega-24)/8<0\), so \(\rho(S)^2\ge T(\omega)^2/4>T(\omega_C)^2/4=d(\omega_C)\). For \(6/5\le\omega<2\), \(d(\omega)<0\), and \(\rho(S)^2\ge|d(\omega)|\ge1/125>d(\omega_C)\). Therefore \(\omega_C\) is the unique global minimizer. Exact simplification yields \(d(\omega_C)=1351-780\sqrt3\).

**2. Fresh-reshuffle second moment.** The dihedral symmetry permuting the row projectors implies the symmetric matrix
\[
M(\omega)=\frac16\sum_{\pi\in\mathfrak S_3}S_\pi^{\mathsf T}S_\pi
\]
is invariant under planar rotations by \(\pi/3\); it must be a scalar multiple of \(I_2\). Every sweep has the same squared Frobenius norm. Direct multiplication, or simply its trace, gives
\[
\tfrac12\operatorname{tr}(S^{\mathsf T}S)
=(1-\omega)^3+\omega^6/32=r(\omega).
\]
Hence \(M=rI_2\). The reshuffle at the next epoch is independent of the current error; conditionally, \(\mathbb E(\|S_{\pi_k}e_k\|^2\mid e_k)=r\|e_k\|^2\). Iterating proves the stated all-horizon identity.

Differentiate to obtain \(r'(\omega)=\tfrac3{16}[\omega^5-16(1-\omega)^2]\). On \((0,1)\) the bracket is strictly increasing from negative to positive, giving the unique root \(\omega_R\). On \((1,2)\), \(\omega^5/(\omega-1)^2\ge3125/108>16\), so the derivative is positive there as well. This proves global uniqueness on \((0,2)\), and exact rational substitution isolates the root within \(0.83886<\omega_R<0.83888\).

**3. Independent row sampling.** Since \(\sum_i a_i a_i^{\mathsf T}=3I_2/2\),
\[
\frac13\sum_{i=1}^3P_i^{\mathsf T}P_i
=\left(1-\frac{\omega(2-\omega)}2\right)I_2.
\]
Independence at each of three successive rows therefore gives \(u(\omega)\) as stated. Polynomial expansion factors the strict advantage \(u-r=3\omega^2(2-\omega)^4/32\) for all \(0<\omega<2\).

**4. Exactly one epoch reverses the long-horizon ordering.** At \(\omega_C\), put \(S_C=S(\omega_C)\), \(\lambda_C=-\sqrt{c_*}\), and \(N=S_C-\lambda_C I_2\). Exact multiplication gives \(N^2=0\), \(N\ne0\), and \(\|N\|_2=\omega_C^3/4\). Thus
\[
S_C^k=\lambda_C^k I_2+k\lambda_C^{k-1}N.
\]
For a nonzero rank-one nilpotent real \(2\times2\) matrix \(N\), orthogonal coordinates put it in the form \(\bigl(\begin{smallmatrix}0&\|N\|_2\\0&0\end{smallmatrix}\bigr)\), so for every integer \(k\ge1\)
\[
\|S_C^k\|_2^2=c_*^k\left(\sqrt{1+k^2\gamma^2}+k\gamma\right)^2,
\qquad \gamma=\frac{\omega_C^3}{8\sqrt{c_*}}.
\]
At \(k=1\), \(S_C^{\mathsf T}S_C\) is not scalar, so its maximum eigenvalue strictly exceeds half its trace: \(\|S_C\|_2^2>r(\omega_C)>r_*\). For the other direction, the exact radical \(c_*\) obeys \(c_*<1/2500\), \(\sqrt{c_*}<1/50\), and \(\|N\|_2<1/4\). Thus
\[
\|S_C^2\|_2\le c_*+2\sqrt{c_*}\|N\|_2
<1/2500+1/100<3/200<r_*.
\]
In particular \(\|S_C^2\|_2^2<r_*^2\). For \(k\ge2\) let \(F(k)=\sqrt{1+k^2\gamma^2}+k\gamma=\exp(\operatorname{arsinh}(k\gamma))\). The derivative \(\frac{d}{dx}\operatorname{arsinh}(\gamma x)\le1/x\) for \(x>0\) implies \(F(k+1)/F(k)\le(k+1)/k\). Therefore
\[
\frac{\|S_C^{k+1}\|_2^2}{\|S_C^k\|_2^2}
\le c_*\left(\frac{k+1}{k}\right)^2
\le\frac9{4\cdot2500}<\frac3{200}<r_*.
\]
Induction from \(k=2\) proves the strict inequality for all integer \(k\ge2\).

## Verification

`verify.py` uses exact SymPy algebra to reconstruct all six sweep matrices, the two-by-two characteristic discriminant, the averaged reshuffling covariance, the with-replacement difference, rational root brackets, the defective optimum, and the Jordan identity. It also exhaustively averages the six and thirty-six first- and second-epoch matrices at four rational relaxations, as finite consistency checks. Run with Python 3 and SymPy using `python verify.py`; expected stdout is in `verification_output.txt`. These finite tests are **not** substitutes for the all-parameter and all-epoch proofs above. The root brackets and algebraic inequalities use exact expressions, not floating-point certificates.

## Relationship to prior work

Han and Xie [1] establish dimension-independent linear convergence analysis and bounds for randomly reshuffled Kaczmarz, and explicitly compare RRK with independent and cyclic ordering. Their results are broader in matrix dimension but do not compute the present exact three-row mean-square isotropy, the optimally relaxed rates, or their finite-horizon crossing. Oswald and Zhou [2] establish shuffled/preshuffled SOR-type estimates and discuss equiangular planar row families; their planar example has a different even-row structure, and the inspected results do not state this three-line rate reversal. Ferreira, Acebrón and Monteiro [3] survey Kaczmarz variants and comparative experiments but do not supply these exact formulas. The independent-row comparison is aligned with classical randomized Kaczmarz theory [4]. Thus this is a **specific exact benchmark**, not a new Kaczmarz algorithm or a claim that random reshuffling is generally slower. An equivalent result in specialist frame or projection-product literature remains possible and requires independent validation.

## Limitations

The theorem is restricted to one consistent planar redundant tight frame and identical, fixed relaxation \(0<\omega<2\). Reshuffling is independent *between* epochs. Rate optimality is asymptotic for cycling and exact all-horizon for isotropic reshuffling; the finite-horizon result compares these fixed, rate-optimal parameters rather than separately optimizing the cyclic relaxation for each horizon. The results do not cover inconsistent equations, changing relaxation, other row geometries, numerical roundoff, or almost-sure randomized convergence exponents. None of the checks constitutes independent scientific validation.

## References

[1] D. Han and J. Xie, *A simple linear convergence analysis of the randomized reshuffling Kaczmarz method*, first arXiv submission 2024-10-02, arXiv:2410.01140, https://arxiv.org/html/2410.01140 .

[2] P. Oswald and W. Zhou, *Random Reordering in SOR-Type Methods*, first arXiv submission 2015-10-15, arXiv:1510.04727, https://arxiv.org/abs/1510.04727 .

[3] I. A. Ferreira, J. A. Acebrón and J. Monteiro, *Survey of a class of iterative row-action methods: The Kaczmarz method*, published 2024-09-26, https://doi.org/10.1007/s11075-024-01945-2 .

[4] T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, first arXiv submission 2007-02-08, arXiv:math/0702226, https://arxiv.org/abs/math/0702226 .
