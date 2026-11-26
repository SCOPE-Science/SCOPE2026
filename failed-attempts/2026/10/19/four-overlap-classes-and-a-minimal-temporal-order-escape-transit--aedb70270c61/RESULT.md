# Four overlap classes and a minimal temporal-order escape transition for three-stage Markov holes

## Finding

Let \(k\ge 2\) be an integer, and consider the expanding map \(T_k:[0,1)\to[0,1)\), \(T_k(x)=kx\bmod 1\), with initial Lebesgue distribution. For \(a,b\in\{0,\ldots,k-1\}\), let \(H_{ab}\) be the half-open length-two base-\(k\) cylinder whose first two digits are \(a,b\). Fix an ordered triple of words \(w_i=(a_i,b_i)\) and, at time \(n\), remove points when \(T_k^n(x)\in H_{w_{1+(n\bmod 3)}}\). Repetitions of words are permitted.

Write \(S_N\) for survival through times \(0,\ldots,N-1\). Put
\[
 d_i=\mathbf1_{\{b_i=a_{i+1}\}},\quad i=1,2,3,\quad a_4=a_1,
 \qquad r=d_1+d_2+d_3.
\]
The escape exponent exists for every schedule and depends **only** on the integer \(r\in\{0,1,2,3\}\). More precisely, put
\[
 T_r=k^3-3k+r-\mathbf1_{\{r=3\}},\qquad
 \Delta_r=(-1)^r(k-1)^r,
 \qquad \rho_r=\frac{T_r+\sqrt{T_r^2-4\Delta_r}}{2}.
\]
Then
\[
 \boxed{\lim_{N\to\infty}-\frac1N\log S_N
 =\gamma_r=\log k-\frac13\log\rho_r},\qquad
 \boxed{\rho_0<\rho_1<\rho_2<\rho_3}.
\]
For an alphabet of size \(k\), precisely \(\binom3r k^3(k-1)^{3-r}\) of the \(k^6\) ordered triples lie in class \(r\). The full \(k\)-state three-step survivor transfer matrix has characteristic polynomial
\[
 \boxed{z^{k-2}(z^2-T_rz+\Delta_r)}.
\]
The case \(k=2,r=0\) is exceptional: the Perron multiplier is the defective value \(1\), and **every** such schedule satisfies
\[
 \boxed{S_{3m}=\frac{2+3m}{2^{3m+1}}\qquad(m\ge0)}.
\]
Thus its finite-time survival has a linear prefactor although its escape exponent is still \(\log2\).

The dependence on temporal order begins sharply at period three: for an alternating two-stage schedule, permuting the same two holes leaves the escape exponent unchanged, but a three-stage schedule need not. In the binary map, the same three holes \(H_{00},H_{01},H_{11}\) give the respective three-step survivor matrices
\[
 P_{(00,11,01)}=\begin{pmatrix}1&0\\3&1\end{pmatrix},\qquad
 P_{(00,01,11)}=\begin{pmatrix}2&1\\3&2\end{pmatrix}.
\]
Consequently the first ordering has escape exponent \(\log2\), while the second has \(\log2-\tfrac13\log(2+\sqrt3)\). All three holes have the same individual Lebesgue measure \(1/4\) and appear exactly once per cycle in both cases.

## Assumptions and scope

All cylinder endpoints are assigned their usual half-open convention; ambiguity of base-\(k\) expansions affects a Lebesgue-null set and does not affect any survival probability. Hole membership is tested before the map is applied at each time. The schedule has period dividing three, not necessarily least period three. No small-hole, mixing, or genericity hypothesis is assumed. The classification addresses Lebesgue-measure survival and the exponential escape rate; it does not assert an analogous classification for arbitrary starting distributions or overlapping holes applied simultaneously.

## Proof

**Transfer identity.** Let \(u\) denote the all-ones column of length \(k\); let \(e_a\) denote its coordinate columns. Write \(J=uu^\top\), \(E_{ab}=e_ae_b^\top\), and \(A_i=J-E_{a_ib_i}\). A sequence of \(3m+1\) independent uniform base-\(k\) digits survives the first \(3m\) tests exactly when each successive pair avoids its prescribed word. Therefore, with \(P=A_1A_2A_3\),
\[
 \boxed{S_{3m}=k^{-(3m+1)}u^\top P^m u.}
\]
Every matrix \(A_i\) has rank at most two because its image is contained in \(\operatorname{span}\{u,e_{a_i}\}\). Hence \(P\) has rank at most two.

**Trace.** Expand \((J-E_1)(J-E_2)(J-E_3)\), using \(J^2=kJ\) and \(\operatorname{tr}(E_{a_ib_i}E_{a_jb_j})=\mathbf1_{\{b_i=a_j\}}\mathbf1_{\{b_j=a_i\}}\). Direct cyclic trace simplification yields
\[
 \operatorname{tr}P=k^3-3k+d_1+d_2+d_3-d_1d_2d_3=T_r.
\]
The cyclic wrap condition \(d_3\) arises from the term \(\operatorname{tr}(E_1JE_3)\); it cannot be dropped when identifying the spectrum of a repeated schedule.

**Second elementary coefficient.** On the exterior square, because each \(A_i\) is a difference of two rank-one maps, its second exterior power has the rank-one form
\[
 \bigwedge^{\!2}A_i=-(u\wedge e_{a_i})(u\wedge e_{b_i})^\top.
\]
The natural exterior inner product satisfies \(\langle u\wedge e_b,u\wedge e_a\rangle=k\mathbf1_{\{a=b\}}-1\). Taking the trace of the product of three exterior powers therefore gives
\[
 \operatorname{tr}(\bigwedge^{\!2}P)=-\prod_{i=1}^3(kd_i-1)=(-1)^r(k-1)^r=\Delta_r.
\]
This is the second elementary symmetric polynomial in the eigenvalues of \(P\). Since \(\operatorname{rank}P\le2\), its characteristic polynomial is precisely \(z^{k-2}(z^2-T_r z+\Delta_r)\). The coefficient \(\Delta_r\ne0\) also proves that \(\operatorname{rank}P=2\).

**The leading eigenvalue and the escape exponent.** The two nonzero eigenvalues are the roots of the displayed quadratic. The discriminant is positive: for \(r\) odd it exceeds \(T_r^2\); for \(r\) even, \(T_r\ge2(k-1)^{r/2}\), with equality only at \((k,r)=(2,0)\). Apart from that case, the positive root \(\rho_r\) strictly dominates the modulus of the other nonzero root. For \(k\ge3\), \(A_1A_2\) is entrywise positive because each entry is a sum of at least \(k-2\ge1\) allowed intermediate transitions, and \(A_3\) has no zero column, so \(P\) is positive. Perron–Frobenius therefore implies \(u^\top P^m u\sim c\rho_r^m\) with \(c>0\). For \(k=2,r\ge1\), the two eigenvalues \(\lambda_+>\lvert\lambda_-\rvert\) are distinct. Inclusion-exclusion of the three forbidden adjacent pairs gives \(a_0=u^\top Iu=2\) and \(a_1=u^\top Pu=5+2(d_1+d_2)-d_1d_2\ge5\). The coefficient of \(\lambda_+^m\) in \(a_m=u^\top P^m u\) is \((a_1-2\lambda_-)/(\lambda_+-\lambda_-)\), which is positive since \(\lambda_-<1\) in all three cases. At \(k=2,r=0\), trace and determinant imply \((P-I)^2=0\). The exact one-cycle count from digit inclusion-exclusion is \(u^\top Pu=5\), so \(u^\top P^m u=2+3m\) for all \(m\). This proves the claimed exponent along multiples of three. Since \(S_{3m+3}\le S_{3m+j}\le S_{3m}\) for \(j=0,1,2\), the limit exists and is the same for all \(N\).

**Strict ordering.** Set \(p_r(z)=z^2-T_rz+\Delta_r\). The first positive root obeys \(\rho_0<T_0<T_1<\rho_1\), with the equality \(T_0=2\) allowed at \(k=2\). Also
\[
 p_2(\rho_1)=k(k-1)-\rho_1<0,
\]
where the inequality follows from \(\rho_1>T_1=k^3-3k+1>k(k-1)\) for every \(k\ge2\). Therefore \(\rho_2>\rho_1\). As \(T_3=T_2\),
\[
 p_3(\rho_2)=-k(k-1)^2<0,
\]
so \(\rho_3>\rho_2\).

**Class counts.** Fix \(a_1,a_2,a_3\), giving \(k^3\) choices. Each \(b_i\) can be set equal to the next \(a\) in precisely one way or chosen differently in \(k-1\) ways. Choosing the \(r\) successful overlap positions proves the exact frequency formula.

**Minimal temporal-order example.** Cyclic survival matrices for two-stage schedules are \(A_1A_2\) and \(A_2A_1\); these have identical characteristic polynomials by \(\det(I-zA_1A_2)=\det(I-zA_2A_1)\). Thus switching the order of a fixed pair cannot change their escape exponent. In period three, direct multiplication gives the two matrices in the Finding section. The first is a nontrivial unipotent and the second has eigenvalues \(2\pm\sqrt3\). For the latter,
\[
 u^\top P^m u=(1+2/\sqrt3)(2+\sqrt3)^m+(1-2/\sqrt3)(2-\sqrt3)^m.
\]
This proves that order alone changes the asymptotic escape exponent and that three is the smallest switching period for which this can happen.

## Verification

The standalone `verify.py` reconstructs all matrices with exact integer arithmetic, checks traces and second characteristic coefficients for **all** \(k^6\) schedules for each \(k=2,3,4,5\), checks the exact class sizes and one-cycle survival counts, reproduces both displayed order-sensitive matrices, and checks the unipotent survival law for fourteen horizons. Execution of the included file returned `VERIFY_OK`. The universal proof uses the trace, exterior-square, and Perron arguments above rather than extrapolation from this finite computation.

## Relationship to prior work

Livorati, Georgiou, Dettmann and Leonel studied escape through oscillating and breathing time-dependent holes in the doubling map and used Ulam approximations and overlap-based analytical models. The present result treats a different, exactly Markov three-stage switching protocol, derives its full finite-dimensional characteristic polynomial for every alphabet size, and finds a sharp minimum period for **permutation-only** changes in escape exponent; no approximation enters.

Cheriyath and Agarwal treat holes specified by a *fixed union* of forbidden cylinders and obtain escape-rate comparisons from word-correlation generating functions. A fixed union excludes its words **at every time**; it is not the one-hole-per-time periodic protocol classified here. The standard transfer-matrix formalism from this literature is an ingredient, not a claim of novelty. Earlier exact two-stage alternating-hole and randomized switching results likewise do not imply the four-class three-stage spectrum, the period-three order sensitivity, or the exceptional polynomial prefactor.

## Limitations

Originality is assessed against the explicitly inspected references and documented searches, not certified across all possible prior literature. Periodic higher-word holes, unequal phase durations, simultaneous unions, and non-Lebesgue starting measures are outside this theorem. The checker tests a finite set of alphabet sizes; its outputs do not certify the algebraic identities for all sizes. At \(k=2,r=0\), an exponential-only ansatz without a polynomial prefactor is false.

## References

- A. L. P. Livorati, O. Georgiou, C. P. Dettmann, E. D. Leonel, *Escape through a time-dependent hole in the doubling map*, arXiv:1312.7030, first public preprint 25 December 2013; *Physical Review E* 89 (2014), 052913. Accessible text: https://arxiv.org/html/1312.7030v2.
- H. Cheriyath and N. Agarwal, *Subshifts of Finite Type with a Hole*, arXiv:1905.11767 (2019), *Journal of the Australian Mathematical Society* (2022). Accessible text: https://arxiv.org/html/1905.11767v5.
- O. Georgiou, C. P. Dettmann, E. G. Altmann, *Faster than expected escape for a class of fully chaotic maps*, arXiv:1207.7000 (2012). Used as contextual literature for finite Markov holes, not as a novelty certificate.
