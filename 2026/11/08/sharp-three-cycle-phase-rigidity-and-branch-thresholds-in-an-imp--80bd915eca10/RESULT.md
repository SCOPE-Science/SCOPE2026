# Sharp three-cycle phase rigidity and branch thresholds in an implicit angular map

## Finding
Consider the positive-root angular-velocity map
\[
T_P(\theta,w)=(\theta+2\pi/3\pmod{2\pi},\ R_{P\sin\theta}(w)),\qquad P\in\mathbb R\setminus\{0\},\quad w>0,
\]
where
\[
R_t(w)=\frac{w}{2}\left(1+\frac{t}{w^2}+\sqrt{1+\frac{6t}{w^2}+\frac{t^2}{w^4}}\right)
\]
is defined only when the displayed root is real and the selected output is positive. Put \(a=\sqrt{3}|P|/2\).

**Theorem.** Every positive prime-three orbit of this map has initial angle in the six-point set
\[
\theta_0\in\{0,\pi/3,2\pi/3,\pi,4\pi/3,5\pi/3\}\pmod{2\pi}.
\]
Conversely, each of the two three-point angular cycles in this set carries a nonempty, precisely specified one-parameter family of prime-three orbits. Rotate the cyclic indexing to the unique step with \(\sin\theta_0=0\), and call its entering speed \(w\), so the zero-kick step leaves the speed equal to \(w\). Let \(\varepsilon\in\{-1,+1\}\) be the sign of \(P\sin(\theta_0+2\pi/3)\). The orbit exists for the **positive-root map** exactly when
\[
\boxed{\;w^2\ge a\quad(\varepsilon=+1),\qquad
w^2\ge(3+2\sqrt2)a\quad(\varepsilon=-1).\;}
\]
These inclusive thresholds are sharp. At equality one of the negative-kick quadratic roots is double. The angular coordinate has least period three, so every orbit listed has least period three. Modulo cyclic relabeling there are exactly two half-line families; there are no other admissible prime-three orbits.

## Assumptions and scope
The angle belongs to \(\mathbb R/(2\pi\mathbb Z)\), and the speed is strictly positive. The step size is exactly \(2\pi/3\). The parameter \(P\) is any nonzero real number; in the original angular-velocity model it is the signed physical coefficient. At every iteration choose the **plus** square-root branch, not the small quadratic root. An orbit must have all three updates in the real, positive domain of that branch. Boundary points at which the radical vanishes are included as well-defined states, without asserting differentiability there. There is no assertion about steps of other rational rotations, or about longer-period points.

## Proof
Write
\[
\Phi(u,v)=\frac{uv(v-u)}{u+v},\qquad u,v>0.
\]
The defining implicit recurrence is equivalent to
\[
\Phi(w_k,w_{k+1})=P\sin(\theta_k),\qquad \theta_{k+1}=\theta_k+2\pi/3.
\]
For a hypothetical three-cycle, let \(x=w_0\), \(y=w_1\), \(z=w_2\), \(w_3=x\). The sum of its three sine kicks vanishes. Direct common-denominator expansion gives the exact algebraic identity
\[
\Phi(x,y)+\Phi(y,z)+\Phi(z,x)
=-\frac{(x-y)(x-z)(y-z)(xy+xz+yz)}{(x+y)(x+z)(y+z)}.
\]
Its final fraction vanishes for positive \(x,y,z\) only if at least two speeds coincide. The corresponding step has \(\Phi=0\), so \(P\sin\theta_k=0\); as \(P\ne0\), some angle of the cycle is exactly \(0\) or \(\pi\) modulo \(2\pi\). This is equivalent to the stated six-point phase set, proving global phase necessity even at a branch-discriminant endpoint.

For the converse, rotate the orbit so that \(\sin\theta_0=0\). The first update is \(w\mapsto w\); the other two kicks are \(\varepsilon a\) and \(-\varepsilon a\). For an input \(u>0\), the positive roots of \(\Phi(u,v)=t\) are obtained from \(q=v/u\) and \(\tau=t/u^2\) by
\[
q^2-(1+\tau)q-\tau=0,
\qquad q_+(\tau)=\frac{1+\tau+\sqrt{1+6\tau+\tau^2}}{2}.
\]
If \(t>0\), the quadratic has exactly one positive root \(q_+>1\). If \(t<0\), the larger positive root exists precisely when
\[
-\bigl(3-2\sqrt2\bigr)\le\tau<0;
\]
then its ratio is at least \(\sqrt2-1\), with equality exactly at the double root.

If \(\varepsilon=+1\), write \(v=R_a(w)=zw\), with \(z>1\). The equation reads
\[
\frac a{w^2}=\frac{z(z-1)}{z+1}.
\]
The right side is strictly increasing on \(z>1\). For the next, negative kick to return from \(v\) to \(w\), the inverse ratio \(w/v=1/z\) must be the larger negative-kick root. This holds exactly when \(z\le1+\sqrt2\), equivalently \(a/w^2\le1\). Hence \(w^2\ge a\), including the double-root boundary, is necessary and sufficient.

If \(\varepsilon=-1\), the first nonzero kick is negative. Its positive-root update exists precisely when
\[
-\frac a{w^2}\ge-\bigl(3-2\sqrt2\bigr),
\]
which is \(w^2\ge(3+2\sqrt2)a\). At every such speed it produces \(0<v<w\) with \(\Phi(w,v)=-a\). Thus \(\Phi(v,w)=a\), and the ensuing positive kick has the unique positive root \(w\); so the three-step return is exact. This proves both sharp conditions and exhausts all possibilities.

## Verification
The standalone Python program `verify.py` checks the three-speed factorization symbolically, the exact square-root boundary ratios \(1+\sqrt2\) and \(\sqrt2-1\), 729 rational speed triples, ten interior sample cycles, and twelve off-grid samples. Execute `python verify.py` with Python 3 and SymPy installed. The proof above is analytic for every admissible parameter and does not infer universal truth from these finite checks.

## Relationship to prior work
Khandelwal and Mukherjee, *A Two-Dimensional Map of Arbitrary Period*, arXiv:2412.15002v1 (first posted December 19, 2024), introduce precisely this implicit positive-speed recurrence. Their Theorem 3.5 gives **sufficient** lattice angles for periodicity at general rational steps, with a lower-speed assumption; their conclusion reports loss of periodicity at other angles in simulations. The present theorem gives the converse, the complete phase census, and two **sharp and different** admissible-speed thresholds at the least nontrivial step \(2\pi/3\). It does not claim their established sufficient periodicity mechanism as new. Other generic theorems for second-order difference equations do not imply these source-specific branch conditions merely from their titles or abstract formulations.

## Limitations
The result is complete only for the three-angle rotation and the selected positive quadratic root. It does not classify other rational rotation denominators, other quadratic branches, long-period speed dynamics, or stability under perturbations of the initial angle. At the threshold the map need not have a finite derivative. It does not establish the absence of quasiperiodic or nonperiodic trajectories. Historical priority, beyond the identified literature and mathematical-record search, is not independently certified.

## References
Khandelwal, A., and Mukherjee, R., *A Two-Dimensional Map of Arbitrary Period*, arXiv:2412.15002v1, posted 2024-12-19, especially equations (1), (2), (11), Theorem 3.5, Appendix A and Section 6. https://arxiv.org/abs/2412.15002
