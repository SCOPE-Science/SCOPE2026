# Exact one-probe repair and complete phase fibers for Alltop Gabor measurements

## Finding

Let \(q=p^m\) be a prime power of characteristic \(p\ge5\), let \(F=\mathbb F_q\), and let \(A:F\to F\) be an Alltop function: for every \(h\ne0\), the difference \(t\mapsto A(t+h)-A(t)\) is planar, meaning that each of its nonzero additive differences is a permutation of \(F\). Fix any nontrivial additive character \(\psi\) of \(F\). Define the \(q^2\) unit vectors
\[
 v_{h,k}(t)=q^{-1/2}\psi\bigl(A(t-h)+kt\bigr),\qquad h,k,t\in F,
\]
and the phaseless measurements \(\mathcal M_A(x)=(|\langle x,v_{h,k}\rangle|^2)_{h,k\in F}\) on \(\mathbb C^F\).

**Complete phase-fiber theorem.** The measurement family consists of \(q\) mutually unbiased orthonormal bases. Two signals \(x,y\) have equal \(\mathcal M_A\)-data if and only if
\[
 \|x\|_2^2=\|y\|_2^2,
 \qquad x_i\overline{x_j}=y_i\overline{y_j}\quad(i\ne j).
\]
Consequently, modulo a global unimodular factor, the full fiber is: a singleton for the zero signal and for every signal supported on at least three sites; a singleton for two-site signals of equal coordinate magnitudes; exactly two points for two-site signals with unequal coordinate magnitudes (the alternate signal swaps those magnitudes while retaining the two coordinate phases); and exactly \(q\) points for each nonzero one-site signal (the \(q\) possible support locations).

**Sharp one-probe theorem.** For a fixed \(w\in\mathbb C^F\), appending just \(|\langle x,w\rangle|^2\) yields phase retrieval for *every* \(x\in\mathbb C^F\) if and only if the \(q\) real numbers \(\{|w_t|^2:t\in F\}\) are pairwise distinct. One supplemental measurement is necessary and sufficient. The real-linear Hermitian lifting ranks before and after any such supplement are, respectively,
\[
 q^2-q+1\qquad\text{and}\qquad q^2-q+2.
\]
Thus a single supplemental intensity achieves universal nonlinear phase retrieval without recovering arbitrary Hermitian matrices.

**Sharp normalized contrast.** Among unit-norm probes \(\|w\|_2=1\), the greatest possible smallest pairwise squared-amplitude separation is exactly
\[
 \max_{\|w\|_2=1}\min_{s\ne t}\bigl||w_s|^2-|w_t|^2\bigr|
 =\frac{2}{q(q-1)}.
\]
Equality holds precisely when, up to coordinate permutation, the squared magnitudes are \(0,2/[q(q-1)],4/[q(q-1)],\ldots,2/q\); all coordinate phases may be chosen freely. For instance one can choose \(w_j=\sqrt{2j/[q(q-1)]}\), \(0\le j<q\), after labeling \(F\). This is optimal *contrast between otherwise indistinguishable coordinate impulses*, not an asserted optimal global inverse-Lipschitz stability constant.

## Assumptions and scope

The ambient vector-space dimension is \(q=p^m\), not necessarily prime; only characteristic at least five is assumed. Inner products are \(\langle x,v\rangle=\sum_{t\in F}x_t\overline{v_t}\). Signals may have zero coordinates and arbitrary complex amplitudes. Phase retrieval means uniqueness up to multiplication of the entire signal by a scalar of unit modulus, including the zero signal by convention. The square magnitudes of the \(q^2\) baseline measurements determine the norm because each fixed-\(h\) family is an orthonormal basis. The contrast problem constrains the extra probe to have Euclidean norm one; it concerns only pairwise discrimination of basis impulses.

## Proof

**1. Alltop correlations and unbiased bases.** For each fixed \(h\), orthogonality of additive characters gives
\[
 \langle v_{h,k},v_{h,\ell}\rangle=\frac1q\sum_{t\in F}\psi((k-\ell)t)=\mathbf1_{k=\ell}.
\]
For two different shifts, their inner product is, up to a unimodular factor, \(q^{-1}S\), where \(S=\sum_t\psi(B(t)+ct)\), \(c\in F\), and \(B(t)=A(t+u)-A(t)\) for some \(u\ne0\). Because \(B\) is planar,
\[
 |S|^2=\sum_{a,t\in F}\psi\bigl(B(t+a)-B(t)+ca\bigr)
 =q.
\]
Indeed, at \(a=0\) the inner sum equals \(q\); for each \(a\ne0\) the values \(B(t+a)-B(t)\) run once over \(F\), and the inner sum is zero. Thus \(|\langle v_{h,k},v_{h',\ell}\rangle|^2=1/q\) whenever \(h\ne h'\). Also all coordinates of all vectors have magnitude \(q^{-1/2}\).

**2. Exact Hermitian kernel, with no missing directions.** Let \(P_{h,k}=v_{h,k}v_{h,k}^*\). Every \(P_{h,k}\) has diagonal \((1/q,\ldots,1/q)\), so its real span lies in the \(q^2-q+1\)-dimensional space of Hermitian matrices with constant diagonal. To prove equality, set \(Q_{h,k}=P_{h,k}-I/q\). For distinct \(h,h'\), mutual unbiasedness yields \(\operatorname{tr}(Q_{h,k}Q_{h',\ell})=0\). For fixed \(h\), the \(q\) matrices \(Q_{h,k}\) span a \((q-1)\)-dimensional space, because their Gram matrix is \(I_q-J_q/q\). Those \(q\) subspaces are orthogonal; adding \(I\) yields dimension \(1+q(q-1)\), exactly the upper bound. Therefore
\[
 \ker_{\mathrm{Herm}}\mathcal L_A
 =\{\operatorname{diag}(d_t)_{t\in F}:d_t\in\mathbb R,\ \sum_td_t=0\},
\]
where \(\mathcal L_A(H)=(\operatorname{tr}(P_{h,k}H))_{h,k}\). The real kernel dimension is \(q-1\). Consequently equality of intensities for \(x,y\) is exactly equality of the trace and every off-diagonal entry of \(xx^*\) and \(yy^*\), as claimed.

**3. All nontrivial fibers.** If \(x\) has at least three nonzero coordinates, the support is recovered from its nonzero off-diagonal products. For distinct supported indices \(i,j,k\),
\[
 |x_i|^2=\frac{|x_i\overline{x_j}|\,|x_i\overline{x_k}|}{|x_j\overline{x_k}|}.
\]
Thus all magnitudes and all relative phases are recovered and \(y=e^{i\theta}x\). If the support has exactly two sites \(i,j\), their product and the norm determine the unordered pair of squared magnitudes as the two roots of the quadratic with sum \(\|x\|_2^2\) and product \(|x_i\overline{x_j}|^2\). Two distinct roots give exactly the original signal and its coordinate-magnitude swap, up to global phase; a double root yields just one. If all off-diagonal products vanish, a nonzero vector must have exactly one nonzero coordinate, and the measured norm gives its amplitude. Any of the \(q\) coordinate locations is possible, and no other alternatives exist. The zero input is detected by its norm.

**4. Necessary and sufficient one-probe condition.** Equal baseline intensities imply \(D=xx^*-yy^*\) is a traceless diagonal Hermitian matrix. It also has rank at most two. If \(D\ne0\), it must therefore have precisely two diagonal entries \(D_{ii}=a\) and \(D_{jj}=-a\) for some real \(a\ne0\). The extra intensity difference is
\[
 |\langle x,w\rangle|^2-|\langle y,w\rangle|^2
 =\operatorname{tr}(ww^*D)
 =a\bigl(|w_i|^2-|w_j|^2\bigr).
\]
Distinct squared magnitudes make this nonzero for every nontrivial candidate pair, proving universal retrieval. Conversely, if \(|w_i|^2=|w_j|^2\), the two distinct unit coordinate vectors \(e_i,e_j\) already have identical baseline intensities (each is flat on every measured basis) and identical extra intensity; injectivity fails. Thus the criterion and minimality are exact. For a successful probe \(ww^*\) is outside the constant-diagonal Hermitian subspace and adds exactly one rank direction.

**5. Exact maximin impulse contrast.** Put the \(q\) squared magnitudes in increasing order \(0\le z_0<\cdots<z_{q-1}\) and let \(\delta\) be their minimum successive difference. Then \(z_j\ge j\delta\) and
\[
 1=\sum_{j=0}^{q-1}z_j\ge\delta\,q(q-1)/2.
\]
Equality forces \(z_0=0\) and \(z_j=j\delta\) for all \(j\), giving the displayed optimum and complete equality case. The optimal contrast directly maximizes the minimum possible extra measurement separation between distinct unit coordinate impulses, whose baseline data are identical.

## Verification

The standalone script `check_alltop_mub.py` builds the actual vectors over prime fields of orders \(5,7,11\) and the quadratic extension \(\mathbb F_{25}\), using an explicit irreducible quadratic and trace character in the last case. It checks all within- and cross-basis overlaps; Hermitian operator ranks for the three prime fields; explicit two-site collisions, probe obstructions and repairs; and the claimed contrast normalization. Its recorded output is in `check_output.txt`. The general theorem is an algebraic proof for infinitely many dimensions and functions; finite computations are corroborative rather than exhaustive verification of the infinite family.

## Relationship to prior work

Price, Hall, and Bartlett study Alltop functions and their known construction of mutually unbiased bases. Their planar-difference definitions and the two known families supply the natural source framework; those previously known constructions and unbiasedness are not claimed here. The distinguishing statement is the *complete pure-signal fiber classification* of the resulting incomplete Gabor projectors, the sharp necessary-and-sufficient **one**-intensity repair, and the unique sharp squared-coordinate contrast profile.

The general theory of pure-state tomography from a small number of orthonormal bases, including Carmeli and collaborators' five-basis constructions, addresses a different measurement design. Wang and Shang's work considers general rank-one POVM cardinality bounds rather than this Alltop/Gabor fiber structure. A general rank-two-kernel criterion underlies the proof, but the specific kernel, full fibers, correction criterion, and optimized contrast are established explicitly here. Related finite Gabor rank classifications concern other window families and do not imply this exact Alltop statement by substitution.

## Limitations

The result is for characteristic at least five and bona fide Alltop functions, not arbitrary phase functions. It concerns exact noiseless intensity data; the optimal contrast is only for the indistinguishable coordinate-impulse pairs and makes no claim about a globally optimal inverse-Lipschitz constant or reconstruction under noise. The augmented measurements are not linearly informationally complete for general Hermitian input matrices. The background mutually unbiased construction and the general rank-two-kernel principle are standard; a bibliographic equivalent of this particular repair criterion may exist under a different quantum-tomography terminology.

## References

1. A. Price, J. Hall, H. Bartlett, *Refining the search space of Alltop monomials*, Journal of Algebraic Combinatorics 57 (2023), 709–725; first online 2022-11-07. DOI: 10.1007/s10801-022-01187-2.
2. C. Carmeli, T. Heinosaari, M. Kech, J. Schultz, A. Toigo, *Efficient Pure State Quantum Tomography from Five Orthonormal Bases*, 2016 preprint, arXiv:1604.02970.
3. Y. Wang, Y. Shang, *Pure state 'really' informationally complete with rank-1 POVM*, 2017 preprint, arXiv:1711.07585; Quantum Information Processing 17 (2018), article 51.
4. D. McNulty, S. Weigert, *Mutually Unbiased Bases in Composite Dimensions – A Review*, Quantum 10 (2026), 2051, DOI: 10.22331/q-2026-04-01-2051 (background on general MUB structures, not used as a novelty certificate).
