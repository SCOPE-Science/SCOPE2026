# Sharp positivity frontier for irrational-rotation rational arrival processes

## Finding

For the three-coordinate, exactly normalized rational arrival process of Peralta [1], the full set of admissible perturbation amplitudes has an explicit sharp boundary. Put
\[
q=\cot(\varphi/2),\qquad
\varepsilon_\star(\varphi)=\frac{2}{q-1+\sqrt{2(q^2+9)}}.
\]
When \(0<\varphi<\pi\) and \(\varphi/\pi\) is irrational, every finite-order joint arrival density is strictly positive at every finite nonnegative interarrival-time vector **if and only if** \(0\le\varepsilon\le\varepsilon_\star(\varphi)\), for \(\varepsilon\in[0,1]\). For \(\varepsilon>\varepsilon_\star(\varphi)\), some joint density is negative even at a vector of strictly positive finite waiting times.

More precisely, for the \(k\)-th density \(f_k\) and \(T_k=\sum_{j=1}^k t_j\), the **exact normalized-density infimum** over all finite orders and all finite nonnegative waiting-time vectors is
\[
\inf_{k\ge1}\ \inf_{t_1,\ldots,t_k\ge0}
 e^{T_k}f_k(t_1,\ldots,t_k)
 =1-\frac{\varepsilon}{\varepsilon_\star(\varphi)}.
\]
At the critical amplitude this infimum is zero but is not attained by any finite density. For every nonzero admissible amplitude, the construction is a genuinely non-Markovian rational arrival process, by the nonrealizability argument of [1].

## Assumptions and scope

Fix \(\varphi\in(0,\pi)\) with \(\varphi/\pi\notin\mathbb Q\), and write \(c=\cos\varphi\), \(s=\sin\varphi\). For \(\varepsilon\in[0,1]\), define the row vector and two matrices
\[
\nu=(1-\varepsilon,\varepsilon,0),\quad
G_0=\begin{pmatrix}-1&0&0\\0&-2&0\\0&0&-2\end{pmatrix},\quad
G_1=\begin{pmatrix}
1&0&0\\
2-c+s&c&-s\\
2-c-s&s&c
\end{pmatrix}.
\]
For every integer \(k\ge1\) and every finite \(t_1,\ldots,t_k\ge0\), define
\[
f_k(t_1,\ldots,t_k)=\nu e^{G_0t_1}G_1\cdots e^{G_0t_k}G_1\mathbf1.
\]
All assertions concern these matrices, finite \(k\), and finite real waiting times. Positivity is not asserted for other rational arrival constructions or for rational \(\varphi/\pi\). Exact normalization and consistency of the algebraic densities follow from \((G_0+G_1)\mathbf1=0\) and \(\nu\mathbf1=1\), even before nonnegativity is established; the probabilistic interpretation is valid precisely in the nonnegative range.

## Proof

**1. Exact oscillatory density.** From the block-triangular product identity in [1, Lemma 2], writing \(z=e^{i\varphi}\) and \(T_j=t_1+\cdots+t_j\), one has
\[
f_k=e^{-T_k}\bigl(1-\varepsilon+\varepsilon S_k\bigr),\qquad
S_k=\sum_{j=1}^{k}e^{-T_j}w_j,
\]
where
\[
w_j=\operatorname{Re}\bigl((1+i)(2z^{j-1}-z^j)\bigr)
\quad(1\le j<k),\qquad
w_k=2\operatorname{Re}\bigl((1+i)z^{k-1}\bigr).
\]
The formula holds for \(k=1\) with only its terminal term.

**2. Two exact classes of partial sums.** Set
\[
A=(1+i)\left(1+\frac1{1-z}\right),\qquad B=\frac{1+i}{1-z}.
\]
For each \(m<k\), direct telescoping gives
\[
W_m:=\sum_{j=1}^{m}w_j=\operatorname{Re}\bigl(A(1-z^m)\bigr).
\]
The terminal partial sum, which has a different last summand, is
\[
W_k=\operatorname{Re}A-\operatorname{Re}(Bz^k).
\]
Consequently, with \(\alpha=\operatorname{Re}A-|A|\) and \(\beta=\operatorname{Re}A-|B|\),
\[
W_m\ge\alpha\quad(m<k),\qquad W_k\ge\beta>\alpha.
\]
The inequality is strict because \(A/B=2-z\) and \(|2-z|>1\) for \(0<\varphi<\pi\). Also \(\operatorname{Im}A>0\), hence \(\alpha<0\).

Using
\[
\frac1{1-e^{i\varphi}}=\frac12+\frac i2\cot(\varphi/2),
\]
we obtain
\[
A=\frac{3-q}{2}+i\frac{3+q}{2},\qquad
\alpha=\frac{3-q}{2}-\sqrt{\frac{q^2+9}{2}},\qquad
\frac1{1-\alpha}=\varepsilon_\star(\varphi).
\]

**3. Universal lower bound and the critical endpoint.** Put \(a_j=e^{-T_j}\), so \(1\ge a_1\ge\cdots\ge a_k>0\). Summation by parts, with the terminal partial sum above, yields
\[
S_k=\sum_{j=1}^{k-1}W_j(a_j-a_{j+1})+W_k a_k
\ge \alpha a_1+(\beta-\alpha)a_k>\alpha.
\]
The last inequality uses \(\alpha<0\), \(a_1\le1\), \(a_k>0\), and \(\beta>\alpha\). Therefore for \(0<\varepsilon<\varepsilon_\star\),
\[
1-\varepsilon+\varepsilon S_k>1-\varepsilon(1-\alpha)>0,
\]
and at \(\varepsilon=\varepsilon_\star\) the bracket remains strictly positive because \(S_k>\alpha\). At \(\varepsilon=0\), the density is simply \(e^{-T_k}\).

**4. Sharpness over all orders.** Irrationality of \(\varphi/\pi\) implies \(\{z^m:m\ge1\}\) is dense on the unit circle. Hence
\[
\inf_{m\ge1}\operatorname{Re}\bigl(A(1-z^m)\bigr)=\alpha.
\]
For any fixed \(m\), take order \(k=m+1\), let \(t_1=\cdots=t_m=0\), and let \(t_{m+1}=L\) tend to infinity. Then \(a_1=\cdots=a_m=1\), \(a_{m+1}=e^{-L}\), and
\[
S_{m+1}=W_m+e^{-L}w_{m+1}\longrightarrow W_m.
\]
Thus the infimum over all \(k\) and finite nonnegative vectors equals \(\alpha\), proving the claimed exact normalized-density infimum. If \(\varepsilon>\varepsilon_\star\), choose \(m\) with \(W_m<1-1/\varepsilon\), then choose sufficiently large finite \(L\): the density bracket is strictly negative. Continuity makes all first \(m\) zero delays replaceable by small strictly positive delays without changing this sign. This establishes necessity even on the strictly positive orthant.

**5. Non-Markovian interval.** The exact normalization identity is independent of the amplitude. For every \(\varepsilon>0\), [1, Lemma 7] gives a bounded origin-density sequence whose generating function has noncanceling poles at \(e^{\pm i\varphi}\). The Perron–Frobenius obstruction in [1, Proposition 8 and Theorem 9] excludes any finite-dimensional nonnegative Markovian arrival representation. The argument requires positivity to interpret the formulas as a process; steps 3–4 establish precisely when it applies.

## Verification

The standalone standard-library checker `verify.py` tests, for six angles and orders through 18, the direct matrix-product density against the closed formula; both partial-sum identities; the oscillatory lower bounds; the critical-endpoint strictness; and finite negative-density witnesses above the threshold. It passed 50,694 deterministic and seeded finite assertions. These are diagnostic checks only; the proof of the infinite-order infimum is the analytic argument using summation by parts and density of irrational rotations.

For the irrational angle \(\varphi=\pi/\sqrt2\), the sharp amplitude is approximately \(0.526915669239\), compared with the sufficient interval \(\varepsilon<0.184953749154\) supplied by [1, Proposition 4]. This comparison is a concrete numerical illustration of a provable difference in the two thresholds, not a separate empirical assertion of universality.

## Relationship to prior work

Peralta [1] introduced the exact same matrices, derived the joint-density identity (Lemma 2), established normalization (Proposition 3), and proved non-Markovian nonrealizability (Theorem 9). Proposition 4 supplied the sufficient condition \(\varepsilon<1/(1+M)\) where \(M=\sqrt2(2+1/\sin(\varphi/2))\). That criterion does not state a necessary bound, an endpoint result, or an exact infimum. The present finding computes the sharp admissible amplitude from the exact extremal oscillatory partial sums and proves necessity and the strict critical endpoint.

The earlier finite-dimensional point-process framework of Asmussen and Bladt [2], and Telek's two-matrix question [3], motivate the class but do not define the specific 2026 irrational-rotation construction. The present theorem is specialized to that construction; it does not assert a general classification of all non-Markovian rational arrival processes.

## Limitations

The angle must have irrational \(\varphi/\pi\) for the exact dense-rotation infimum; a rational angle has a finite orbit and may have a different threshold. The theorem concerns the specified matrices and \(\varepsilon\in[0,1]\) only. The critical amplitude is pointwise strictly positive in every finite dimension but lacks a uniform positive lower bound for the normalized densities across arbitrary order and delays. This is an exact analytical refinement of a known counterexample, not a new proof of non-Markovian nonrealizability or a universal RAP-to-MAP criterion. Historical-priority assessment is limited to the inspected motivating full text and targeted literature comparisons; independent validation has not been performed.

## References

[1] O. Peralta, *Rational arrival processes with strictly positive densities need not be Markovian*, arXiv:2603.28047v1, first posted 2026-03-30. https://arxiv.org/html/2603.28047v1

[2] S. Asmussen and M. Bladt, *Point processes with finite-dimensional conditional probabilities*, Stochastic Processes and their Applications **82** (1999), 127–142. https://doi.org/10.1016/S0304-4149(99)00006-X

[3] M. Telek, *The two-matrix problem*, Queueing Systems **100** (2022), 265–267. https://doi.org/10.1007/s11134-022-09812-4
