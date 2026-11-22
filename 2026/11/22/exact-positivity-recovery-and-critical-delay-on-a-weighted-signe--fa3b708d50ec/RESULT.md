# Exact positivity recovery and critical delay on a weighted signed triangle

## Finding

Fix arbitrary real conductances \(a,b>0\) and a repulsive conductance magnitude \(q>0\). Define the symmetric, conservative signed Laplacian and its heat semigroup by
\[
L=\begin{pmatrix}a-q&q&-a\\q&b-q&-b\\-a&-b&a+b\end{pmatrix},
\qquad K(t)=e^{-tL}\quad(t\geq0).
\]
The positive edges connect vertices \(1,3\) and \(2,3\), with conductances \(a,b\); the edge \(1,2\) has conductance \(-q\). Put
\[
q_c=\frac{ab}{a+b},\quad S=a+b-q,\quad R=ab-q(a+b),\quad
\lambda_\pm=S\pm\sqrt{S^2-3R},\quad \Delta=\lambda_+-\lambda_-.
\]

**Complete positive-time classification.** If \(0<q<q_c\), every diagonal entry and both positive-edge transitions \(K_{13}(t),K_{23}(t)\) are strictly positive for all \(t>0\). The repulsive-edge entry \(K_{12}(t)=K_{21}(t)\) has exactly one simple positive zero \(T\): it is strictly negative on \((0,T)\) and strictly positive on \((T,\infty)\). Thus \(K(t)\) is entrywise nonnegative exactly for \(t=0\) or \(t\geq T\), and strictly positive exactly for \(t>T\). If \(q\geq q_c\), the entry \(K_{12}(t)\) remains strictly negative for **every** \(t>0\), so the semigroup has no positive-time entrywise-nonnegative operator.

In the stable regime \(0<q<q_c\), write
\[
A=\frac{q+\lambda_+/3}{\Delta},\qquad
B=\frac{q+\lambda_-/3}{\Delta}.
\]
Then \(A>B>0\), \(A-B=1/3\), and the **exact recovery time** \(T\) is the unique positive root of
\[
\frac13-Ae^{-\lambda_-T}+Be^{-\lambda_+T}=0.
\]
Using the induced real \(\ell^\infty\)-operator norm, the exact norm for all \(t\geq0\) is
\[
\|K(t)\|_{\infty\to\infty}
=1+2\max\left\{0,Ae^{-\lambda_-t}-Be^{-\lambda_+t}-\frac13\right\}.
\]
Its unique strict maximum above \(1\) occurs at
\[
t_{\rm peak}=\frac1\Delta\log\frac{B\lambda_+}{A\lambda_-},
\qquad 0<t_{\rm peak}<T.
\]
In particular, exact return to entrywise nonnegativity coincides with exact return to \(\ell^\infty\)-contractivity.

**Two sharp edge-strength regimes.** As \(q\downarrow0\) with \(a,b\) fixed,
\[
T=\frac{2q}{ab}+O(q^2),\qquad
t_{\rm peak}=\frac{q}{ab}+O(q^2),\qquad
\max_{t\geq0}\|K(t)\|_{\infty\to\infty}=1+\frac{q^2}{ab}+O(q^3).
\]
As \(q\uparrow q_c\), set \(\varepsilon=q_c-q\) and \(S_c=a+b-q_c\). Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon T
=\frac{2S_c}{3(a+b)}\log\left(1+\frac{3q_c}{2S_c}\right)>0},
\]
\[
t_{\rm peak}=\frac1{2S_c}\log\frac{q_c}{\varepsilon}+O(1),
\qquad \boxed{\lim_{q\uparrow q_c}\max_{t\geq0}\|K(t)\|_{\infty\to\infty}
=1+\frac{q_c}{S_c}=1+\frac{ab}{a^2+ab+b^2}}.
\]
Thus the sharp positivity horizon diverges at inverse distance to the stability boundary, whereas the peak time diverges only logarithmically and its amplitude converges to a finite value strictly above \(1\).

## Assumptions and scope

The theorem concerns the ordinary real symmetric row-sum-zero **repelling** signed Laplacian, not the alternative signed-degree Laplacian whose diagonal uses absolute weights. All three edge weights and all real times are quantified as stated. The time parameter is physical semigroup time, without additional normalization. The constant state is fixed by \(K(t)\), so every row sum equals \(1\). There is no claim concerning arbitrary graphs of more than three vertices, switching systems, or other matrix functions.

## Proof

**1. Spectrum.** The row sums of \(L\) vanish. Its trace is \(2S\) and the sum of its principal two-by-two minors is \(3R\); hence its spectrum is \(\{0,\lambda_-,\lambda_+\}\). The discriminant is positive because
\[
S^2-3R=a^2-ab+b^2+q(a+b)+q^2>0.
\]
The positive eigenvalues satisfy \(0<\lambda_-<\lambda_+\) exactly when \(R>0\), equivalently \(q<q_c\). At equality \(\lambda_-=0\), and above it \(\lambda_-<0<\lambda_+\).

**2. The repulsive-edge coefficient.** Let \(J\) be the all-ones three-by-three matrix. The spectral projectors at \(\lambda_-\) and \(\lambda_+\) are
\[
P_- =\frac{\lambda_+(I-J/3)-L}{\Delta},\qquad
P_+=\frac{L-\lambda_-(I-J/3)}{\Delta}.
\]
Therefore
\[
K(t)=J/3+e^{-\lambda_-t}P_-+e^{-\lambda_+t}P_+,
\qquad K_{12}(t)=\frac13-Ae^{-\lambda_-t}+Be^{-\lambda_+t}.
\]
In the stable regime, \(B>0\) and \(A-B=(\lambda_+-\lambda_-)/(3\Delta)=1/3\). Directly, \(K_{12}(0)=0\), \(K_{12}'(0)=-q<0\), and \(K_{12}(t)\to1/3>0\).

**3. The sign census.** An exponential polynomial \(c_0+c_1e^{-ut}+c_2e^{-vt}\), with real distinct \(u,v\), has at most two real zeros counting multiplicities: its derivative, after division by one nonzero exponential, is a constant plus a single strictly monotone exponential and therefore has at most one zero. This elementary zero count applies equally when \(u<0\). In the stable regime, \(K_{12}\) has a zero at \(0\), has negative derivative there, and eventually is positive. It therefore has exactly one other zero, which must be simple and have the sign pattern claimed.

The same two-zero bound applies to each \(K_{13}\) and \(K_{23}\). Both vanish at \(0\), have strictly positive derivatives \(a\) and \(b\), respectively, and tend to \(1/3>0\). A later nonpositive value would require two additional zeros counting a tangency twice; this is impossible. Hence both entries are strictly positive at every positive time. Each diagonal is strictly positive because it is a sum of nonnegative spectral-projector diagonal entries weighted by strictly positive exponentials, with the \(J/3\) term strictly positive.

For \(q=q_c\), the explicit formula becomes \(K_{12}(t)=-B(1-e^{-\lambda_+t})<0\), since \(A-B=1/3\). For \(q>q_c\), write \(L=L_0-qvv^{\mathsf T}\) with \(L_0\succeq0\) the positive-edge path Laplacian and \(v=(1,-1,0)^{\mathsf T}\). Rayleigh's principle gives \(\lambda_-\geq-2q\); consequently \(B=(q+\lambda_-/3)/\Delta>0\), while \(A>0\). Now
\[
K_{12}'(t)=A\lambda_-e^{-\lambda_-t}-B\lambda_+e^{-\lambda_+t}<0
\]
for all \(t\geq0\), because \(\lambda_-<0<\lambda_+\). This proves persistent negativity outside the stable region.

**4. Sharp norm and peak.** Every row of \(K(t)\) sums to \(1\). In the stable region, when \(K_{12}(t)<0\), it is the *only* negative entry (together with its symmetric counterpart), so rows one and two have absolute row sum \(1-2K_{12}(t)\), while row three has absolute row sum \(1\). At and after recovery all entries are nonnegative. This proves the norm formula. Moreover
\[
K_{12}'(t)=A\lambda_-e^{-\lambda_-t}-B\lambda_+e^{-\lambda_+t}.
\]
The derivative starts at \(-q\), becomes positive for large \(t\), and has precisely one zero; solving gives the displayed \(t_{\rm peak}\). Thus the norm attains its unique strict global maximum there.

**5. The two endpoint laws.** As \(q\to0^+\), the exponential series and the exact identity \((L^2)_{12}=ab+q(a+b)-2q^2\) yield uniformly near \(t=0\)
\[
K_{12}(t)=-qt+\frac{ab+q(a+b)-2q^2}{2}t^2+O(t^3).
\]
At \(q=0\) the positive two-edge path has strictly positive \(K_{12}(t)\) for each fixed \(t>0\); uniqueness of the positive zero therefore implies \(T\to0\). Division by the initial factor \(t\) and the implicit-function theorem give \(T=2q/(ab)+O(q^2)\). Differentiation of the same expansion gives \(t_{\rm peak}=q/(ab)+O(q^2)\), and substitution gives the quadratic norm excess.

For the other endpoint set \(\varepsilon=q_c-q\). Because \(R=(a+b)\varepsilon\),
\[
\lambda_- =\frac{3R}{S+\sqrt{S^2-3R}}
=\frac{3(a+b)}{2S_c}\varepsilon+O(\varepsilon^2),\quad
\lambda_+\to2S_c,\quad A\to\frac13+\frac{q_c}{2S_c},\quad B\to\frac{q_c}{2S_c}.
\]
At \(q_c\) the repulsive-edge entry remains negative at every finite positive time, so continuity and the unique-crossing property force \(T\to\infty\). At its zero the rapidly decaying exponential therefore tends to zero, and the zero equation implies
\[
\lambda_-T\longrightarrow\log(3A_c)=\log\left(1+\frac{3q_c}{2S_c}\right).
\]
This gives the inverse-distance law. The explicit peak-time expression gives the logarithmic law. At that time \(\lambda_-t_{\rm peak}\to0\) and \(e^{-\lambda_+t_{\rm peak}}\to0\), so \(K_{12}(t_{\rm peak})\to1/3-A_c=-q_c/(2S_c)\), yielding the finite limiting sharp amplification.

## Verification

The standalone standard-library Python script `check_signed_triangle.py` checks the exact quadratic minimal-polynomial identity for four rational parameter sets, independently evaluates the matrix exponential by scaled Taylor series and squaring for 16 stable parameter configurations and five selected times each, tests the exact entry and norm formulas, and probes critical asymptotics. These computations are finite consistency tests; the proofs of uniqueness and infinite-time sign behavior are the analytic arguments above.

For a reproducible example, \(a=b=1\), \(q=1/4\) give \(\lambda_-=1/2\), \(\lambda_+=3\), \(A=1/2\), \(B=1/6\),
\[
K_{12}(t)=\frac13-\frac12e^{-t/2}+\frac16e^{-3t},\qquad
t_{\rm peak}=\frac{2}{5}\log2,\quad T\approx0.687767925034.
\]
The corresponding maximal induced norm is approximately \(1.058792136080\).

## Relationship to prior work

Zelazo and Bürger (2014) give the effective-resistance criterion for positive semidefiniteness of a Laplacian with one negative link, which specializes here to \(q\le q_c\). Chen et al. (2020) establish the equivalence, for symmetric signed Laplacians, between a simple zero ground state with nonnegative remaining spectrum and eventual exponential positivity; their theorem implies the *existence* of some positivity time when \(q<q_c\). Fontan et al. (2022) develop eventual-positivity criteria for signed-network consensus, including the symmetric case. The claimed contribution here is different: complete individual-entry signs, exact *single* recovery and norm-peak formulas, and the sharp inverse-distance versus logarithmic two-clock law near the spectral boundary. No general eventual-positivity criterion or effective-resistance bound is claimed as new.

## Limitations

The results require exactly three vertices, two strictly positive links and one strictly negative link, with the repelling row-sum-zero Laplacian convention. The recovery time for general \(a,b,q\) is defined as a unique transcendental root rather than expressed in elementary closed form. No assertion is made about larger signed graphs, nonsymmetric generators, multiple repulsive links, or any universal sharp bound across such classes. Historical priority for specialized three-state exponential-polynomial formulas is not exhaustively resolved; independent validation has not been performed.

## References

- D. Zelazo and M. Bürger, *On the Definiteness of the Weighted Laplacian and its Connection to Effective Resistance*, arXiv:1408.2187, first public version 10 August 2014. https://arxiv.org/abs/1408.2187
- W. Chen, D. Wang, J. Liu, Y. Chen, S. Z. Khong, T. Başar, K. H. Johansson, and L. Qiu, *On Spectral Properties of Signed Laplacians with Connections to Eventual Positivity*, arXiv:2009.03581, first public version 8 September 2020. https://arxiv.org/abs/2009.03581
- A. Fontan, L. Wang, Y. Hong, G. Shi, and C. Altafini, *Multi-agent consensus over time-invariant and time-varying signed digraphs via eventual positivity*, arXiv:2203.04215, first public version 8 March 2022. https://arxiv.org/html/2203.04215v1
