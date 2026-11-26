# Two-stage positivity recovery for biharmonic heat on nonbinary Hamming three-cubes

## Finding
For integers \(q\ge3\), let \(G_q=K_q\square K_q\square K_q\), with combinatorial Laplacian \(L_q\), and let \(H_q(t)=\exp(-tL_q^2)\), \(t\ge0\). Put \(u=\exp(-q^2t)\) and define
\[
\begin{aligned}
F_{2,q}(u)&=1+(q-3)u+(3-2q)u^4+(q-1)u^9,\\
F_3(u)&=1-3u+3u^4-u^9.
\end{aligned}
\]
There are unique numbers \(\rho_q,\rho_*\in(0,1)\) such that \(F_{2,q}(\rho_q)=F_3(\rho_*)=0\). They obey \(0<\rho_*<\rho_q<1\), and \(\rho_*\) is independent of \(q\). More explicitly, \(\rho_*\) is the unique positive root in \((0,1)\) of
\[
u^5+u^4+u^3+2u^2+2u-1=0,
\]
and \(\rho_*=0.347969427509\ldots\). Set
\[
T_{2,q}=-\frac{\log\rho_q}{q^2},\qquad T_{3,q}=-\frac{\log\rho_*}{q^2}=\frac{1.055640655052\ldots}{q^2}.
\]
For \(0<t<T_{2,q}\), **exactly the distance-two and distance-three kernel entries** are negative. At \(t=T_{2,q}\), distance-two entries vanish, distance-three entries remain strictly negative, and distance-one entries are strictly positive. For \(T_{2,q}<t<T_{3,q}\), **exactly the distance-three entries** are negative. At \(t=T_{3,q}\), distance-three entries vanish and all other off-diagonal entries are strictly positive. In particular,
\[
\boxed{H_q(t)\text{ is entrywise nonnegative}\iff t=0\text{ or }t\ge T_{3,q}.}
\]
The final positivity time, after multiplication by \(q^2\), is **independent of the alphabet size**; the earlier distance-two recovery time is not. Every row sums to one, and its exact induced maximum norm, also equal to the induced \(\ell^1\) norm, is
\[
\boxed{\|H_q(t)\|_{\infty\to\infty}=1+\frac{2}{q^3}\bigl(3(q-1)^2[-F_{2,q}(u)]_++(q-1)^3[-F_3(u)]_+\bigr),}
\]
where \([x]_+=\max(x,0)\). It exceeds one exactly for \(0<t<T_{3,q}\). The roots \(\rho_q\) increase strictly with \(q\) and converge to the unique interior root \(\sigma=0.877627890623\ldots\) of \(1-2u^3+u^8=0\). Consequently \(q^2T_{2,q}\) decreases to \(-\log\sigma=0.130532589962\ldots\).

## Assumptions and scope
The graph is the Cartesian product of exactly three unweighted complete graphs, with alphabet size an integer \(q\ge3\); adjacency means differing in exactly one coordinate. The Laplacian is the **unnormalized** real symmetric graph Laplacian \(L=D-A\). Positive means every matrix entry is nonnegative; there is no operator-order claim. The norm is the usual counting-measure induced \(\ell^\infty\) matrix norm, and the equal \(\ell^1\) norm follows from symmetry. At \(t=0\), \(H_q(0)=I\), so the zero off-diagonal entries at time zero are distinguished from positive-time recoveries. All root uniqueness claims refer to open \((0,1)\).

## Proof
**1. Four-level functional calculus.** Let \(U=J_q/q\) and \(V=I_q-U\). The complete-graph Laplacian is \(qV\). On the threefold tensor product,
\[
L_q=q(V\otimes I\otimes I+I\otimes V\otimes I+I\otimes I\otimes V).
\]
For each subset \(S\subseteq\{1,2,3\}\), put \(P_S=\bigotimes_{j=1}^3 W_j\) with \(W_j=V\) for \(j\in S\) and \(W_j=U\) otherwise. The \(P_S\) are mutually orthogonal projections summing to \(I\), and \(L_qP_S=q|S|P_S\). Hence
\[
H_q(t)=\sum_{S\subseteq\{1,2,3\}}u^{|S|^2}P_S.
\]
For vertices at Hamming distance \(r\in\{0,1,2,3\}\), direct multiplication of \(U_{ab}=1/q\) and \(V_{ab}=\delta_{ab}-1/q\) gives the common matrix entry \(q^{-3}F_{r,q}(u)\), with
\[
\begin{aligned}
F_{0,q}&=1+3(q-1)u+3(q-1)^2u^4+(q-1)^3u^9,\\
F_{1,q}&=1+(2q-3)u+(q-1)(q-3)u^4-(q-1)^2u^9,\\
F_{2,q}&=1+(q-3)u+(3-2q)u^4+(q-1)u^9,\\
F_{3,q}&=F_3=1-3u+3u^4-u^9.
\end{aligned}
\]
The multiplicity of shell \(r\) in any row is \(\binom3r(q-1)^r\). The constant vector is an eigenvector with eigenvalue one, so every row sums to one.

**2. Only distance two and three can be negative.** Every coefficient of \(F_{0,q}\) is nonnegative and its constant term positive. For \(0<u<1\), since \(u^9\le u^4\),
\[
F_{1,q}(u)\ge1-u+2(q-1)(u-u^4)>0.
\]
Thus the only possible negative shells are \(r=2,3\).

**3. Exactly one positive-time recovery of each negative shell.** First,
\[
F_3(u)=-(u-1)^2(u^2+u+1)Q(u),\quad Q(u)=u^5+u^4+u^3+2u^2+2u-1.
\]
The polynomial \(Q\) is strictly increasing for \(u>0\), with \(Q(0)=-1\), \(Q(1)>0\), so it has precisely one root \(\rho_*\in(0,1)\). Therefore \(F_3(u)>0\) for \(0<u<\rho_*\), and \(F_3(u)<0\) for \(\rho_*<u<1\). Moreover \(Q(1/2)>0\), so \(\rho_*<1/2\).

For \(q\ge3\), the ordered nonzero coefficients of \(F_{2,q}\), from lowest to highest powers, have signs \(+,+,-,+\) for \(q>3\), or \(+,-,+\) for \(q=3\): exactly two sign changes. Descartes' rule allows at most two positive roots counted with multiplicity. One is \(u=1\), and \(F_{2,q}(0)=1>0\), while \(F'_{2,q}(1)=2q>0\), so \(F_{2,q}(u)<0\) for \(u<1\) close to one. By continuity there must be a second positive root \(\rho_q\in(0,1)\). These are the only two positive roots, both simple, and the signs are strictly positive for \(u<\rho_q\), negative for \(\rho_q<u<1\).

To order the two recoveries, use the exact relation
\[
F_{2,q}(u)=F_3(u)+q h(u),\qquad h(u)=u-2u^4+u^9.
\]
At \(u=\rho_*<1/2\), one has \(h(\rho_*)>\rho_*(1-2\rho_*^3)>0\), so \(F_{2,q}(\rho_*)>0\). The preceding unique-root sign classification implies \(\rho_q>\rho_*\). Since \(u=e^{-q^2t}\) decreases strictly with time, the distance-two entries recover first and distance-three entries recover last. The claimed sign intervals, boundary values, and final positivity ray follow.

**4. Sharp endpoint norm.** Each row sums to one and contains precisely \(3(q-1)^2\) distance-two entries and \((q-1)^3\) distance-three entries. The absolute sum of any real row of total sum one equals one plus twice the magnitude of all its negative entries. By vertex transitivity every row has the same absolute sum; this proves the displayed exact norm. It equals one exactly for \(t=0\) and all \(t\ge T_{3,q}\), and exceeds one at each strictly intervening time.

**5. Strict dependence of the first recovery, independence of the last.** The function \(h(u)/u=1-2u^3+u^8\) is positive near zero and negative just to the left of one, and equals zero at one. Descartes' rule counts at most two positive roots, so it has a unique root \(\sigma\in(0,1)\) besides one. Since \(h(\rho_*)>0\), one has \(\sigma>\rho_*\). Also \(F_{2,q}(\sigma)=F_3(\sigma)<0\). Hence \(\rho_q\in(\rho_*,\sigma)\) and \(h(\rho_q)>0\). Holding \(u=\rho_q\) fixed and increasing \(q\) strictly increases \(F_{2,q}(u)\), shifting its unique internal zero strictly right: \(\rho_{q+1}>\rho_q\). The bounded increasing sequence has a limit \(r\le\sigma\). Dividing \(F_3(\rho_q)+q h(\rho_q)=0\) by \(q\) shows \(h(r)=0\), and since \(r\ge\rho_3>\rho_*\), it follows that \(r=\sigma\). Applying \(-\log\) yields the asymptotic recovery-scale statement. Finally, \(F_3\), its unique root and thus \(q^2T_{3,q}\) are independent of \(q\).

## Verification
The standalone `verify_hamming3.py` constructs \(L_q\) independently from tensor-product Kronecker sums, computes dense \(\exp(-tL_q^2)\), and compares all entries with the four exact shell polynomials. It also checks stochastic row sums, induced maximum norms, and the root order for \(q=2,3,4\), with five representative interior time values per alphabet and **24,445 entry comparisons**. Run `python verify_hamming3.py` with NumPy and SciPy installed. The \(q=2\) numerical cases are crosschecks of known binary-cube behavior, not claimed as a new result. Finite tests do not prove the all-alphabet theorem; the analytical calculations above do.

## Relationship to prior work
Daners and Glück [1] give general criteria for uniform eventual positivity, but do not identify the exact Hamming three-cube kernel, the two different finite-time shell recoveries, or the universal normalized final cutoff. Published exact squared-Laplacian positivity and norm results on rectangular rook graphs [2] concern Cartesian products of **two**, not three, complete graphs. The present fourth spectral level has two distinct potentially negative shells. Published exact results on complete multipartite graphs [3] also do not cover \(K_q^{\square3}\) for \(q\ge3\), which is not complete multipartite. A related nonbinary Hamming-graph work [4] addresses the **fourth-order Runge–Kutta polynomial endpoint map**, not exact exponentiation of the squared Laplacian, and so neither implies nor contradicts the two recovery horizons. The distinct Boolean-cube result [5] gives a unique recovery for distances two and three throughout the binary family, including the \(q=2\) three-cube; that case is outside the present claim. The contribution concerns the exact nonbinary three-factor semigroup classification and its alphabet-dependent and alphabet-independent boundaries, not general tensor spectral calculus itself.

## Limitations
Only three coordinate factors with a common integer alphabet size are treated, all edges unweighted. The positivity law need not hold for four or more factors or unequal alphabets, and the proof does not establish a simple expression for the maximum transient norm over time. The first recovery root is implicitly algebraic of degree at most eight after removing \(u-1\). No independent validation or exhaustive historical-priority guarantee is claimed; a differently indexed association-scheme calculation could provide a previously unknown equivalent result.

## References
[1] D. Daners and J. Glück, *A criterion for the uniform eventual positivity of operator semigroups*, arXiv:1801.05179, first posted 2018-01-16, https://arxiv.org/abs/1801.05179 .

[2] *Exact positivity horizon and peak amplification of biharmonic heat on rook graphs*, published mathematical record (2026), https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-exact-positivity-horizon-and-peak-amplification-of-biharmonic-he--621e2ef18776/RESULT.md .

[3] *Sharp positivity cutoff for squared-Laplacian heat on every complete multipartite graph*, published mathematical record (2026), https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-sharp-positivity-cutoff-for-squared-laplacian-heat-on-every-comp--e4f9c89a420f/RESULT.md .

[4] *Alphabet-driven positivity barriers for RK4 on Hamming diffusion networks*, published mathematical record (2026), https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-alphabet-driven-positivity-barriers-for-rk4-on-hamming-diffusion--4d16a209d9cc/RESULT.md .

[5] *Distance-controlled zero crossings and the first reentrant biharmonic heat kernel on Boolean cubes*, published mathematical record (2026), https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-distance-controlled-zero-crossings-and-the-first-reentrant-bihar--f03089a5a92e/RESULT.md .
