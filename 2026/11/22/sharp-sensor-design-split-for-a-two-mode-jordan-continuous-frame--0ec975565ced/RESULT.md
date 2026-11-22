# Sharp sensor-design split for a two-mode Jordan continuous frame

## Finding
Let \(a,c>0\), \(H=\mathbb C^2\) with its standard Hermitian norm, and
\[
A=\begin{pmatrix}-a&c\\0&-a\end{pmatrix},\qquad T(t)=e^{tA}\quad(t\ge0).
\]
For a sensor \(\varphi\in H\), the orbit-frame operator is
\[
W_\varphi=\int_0^\infty T(t)\varphi\varphi^*T(t)^*\,dt.
\]
Write \(r=c/(2a)\). The orbit is a continuous frame if and only if the second coordinate of \(\varphi\) is nonzero. Among all such sensors,
\[
\inf_\varphi\frac{\lambda_{\max}(W_\varphi)}{\lambda_{\min}(W_\varphi)}
=\max\{r^2,r^{-2}\},
\]
attained only by \(\varphi\propto(-r,1)\). For unit sensors \(\|\varphi\|=1\),
\[
\lambda_{\min}(W_\varphi)\le\frac1{4a},
\]
with equality if and only if \(r\ge1\) and, up to a unit complex scalar,
\[
\varphi=\frac{(\sqrt{r^2-1}-r,\ 1)}{\sqrt{1+(\sqrt{r^2-1}-r)^2}}.
\]
If \(r<1\), the maximum lower frame bound is strictly below \(1/(4a)\), and its maximizer differs from the unique condition-number minimizer. If \(r>1\), the two optimizers also differ. They coincide only at \(r=1\), which is exactly the tight-frame case.

## Assumptions and scope
All parameters \(a,c\) are strictly positive and all frame bounds use Lebesgue measure \(dt\) on \([0,\infty)\). The frame operator acts on standard \(\mathbb C^2\), with no change of metric. Optimization of condition number permits any nonzero generating sensor; optimization of the lower frame bound imposes \(\|\varphi\|=1\). No discretization, infinite-dimensional extension, or optimal subcritical numerical value is claimed.

## Proof
Since \(A=-aI+cN\) with \(N^2=0\),
\[
T(t)=e^{-at}\begin{pmatrix}1&ct\\0&1\end{pmatrix}.
\]
For \(\varphi=(u,v)\) with \(v\ne0\), set \(z=u/v\), \(w=z+r\), and \(m=1/(2a)\). The elementary moments \(\int_0^\infty t^je^{-2at}dt=j!/(2a)^{j+1}\) give the exact operator identity
\[
W_\varphi=m|v|^2M(w),\qquad
M(w)=\begin{pmatrix}|w|^2+r^2&w\\\overline w&1\end{pmatrix},
\]
with \(\operatorname{tr}M(w)=r^2+1+|w|^2\) and \(\det M(w)=r^2\). The determinant is positive for \(v\ne0\), while \(v=0\) leaves the orbit in a one-dimensional subspace. This proves the frame criterion. At fixed determinant, the ratio of positive eigenvalues is strictly increasing in their sum. Hence the unique optimum of the condition number is at \(w=0\); there \(M(0)=\operatorname{diag}(r^2,1)\), proving the claimed formula and optimizer.

Now assume \(\|\varphi\|=1\). Then \(|v|^2=1/d\), with \(d=1+|w-r|^2\), and \(W_\varphi=mM(w)/d\). Writing \(w=s+it\), direct determinant expansion gives the **exact negative-square certificate**
\[
4\det\!\left(M(w)-\frac d2I\right)
=-\left[(r^2-|w|^2-1)^2+4r^2t^2\right]\le0.
\]
Therefore the smaller eigenvalue of \(M(w)/d\) never exceeds \(1/2\), proving the universal \(1/(4a)\) bound. Equality forces \(t=0\) and \(s^2=r^2-1\), which requires \(r\ge1\). At \(r=1\), the sole choice is \(s=0\), giving \(M/d=I/2\). At \(r>1\), the negative root \(s=-\sqrt{r^2-1}\) is inadmissible because \(d>2\) and the bottom-right diagonal of \(M-dI/2\) is negative. For the positive root \(s=\sqrt{r^2-1}\), \(d<2\), the same determinant is zero and the bottom-right entry is positive; thus \(M-dI/2\) is positive semidefinite, with its smallest eigenvalue zero. This proves attainment and uniqueness of the equality sensor.

If \(r<1\), the determinant certificate is strictly negative for every finite \(w\), and hence the lower bound is always strictly below \(1/(4a)\). Its maximum over the compact unit sphere is attained because eigenvalues depend continuously on \(\varphi\), so the maximal value is strictly below \(1/(4a)\). At the condition-number optimizer \(w=0\), perturbing to small positive real \(w\) strictly increases the normalized lower bound for \(r\ne1\). Indeed, the smaller eigenvalue of \(M(w)\) has derivative zero at \(w=0\) when \(r\ne1\), while \(d'(0)=-2r<0\); explicitly the derivative of \(\lambda_{\min}(M(w)/d)\) there equals \(2r\min(r^2,1)/(1+r^2)^2>0\). Hence the two sensor objectives differ for \(r<1\) as well. At \(r=1\), the condition-number optimum is the unique unit sensor attaining the universal lower bound. Finally \(\kappa=1\) is possible precisely at \(r=1\), proving the tight-frame assertion.

## Verification
All identities are exact consequences of the semigroup exponential and its first three exponential moments. The two by two determinant certificate covers complex sensors, not only real ones. The positivity test at \(r>1\) checks the correct branch of the equality equation. A supplemental numerical cross-check of the determinant identity and eigenvalue cap for real and complex sensors passed; no numerical sampling is used to justify a global extremum.

## Relationship to prior work
Bailey, Gallardo-Gutiérrez and Partington establish a general correspondence between continuous semigroup frames and discrete frames of the cogenerator, including transfer of frame bounds and tightness. Their inspected examples concern composition/shift semigroups and model spaces, not optimal unit-sensor design in the stable defective Jordan family. The classical continuous-time controllability Gramian and Lyapunov equation are background tools. An existing indexed result optimizes a **discrete-time diagonal** two-mode actuator Gramian; its assumptions and objective do not directly give the present nonnormal **continuous-time Jordan** phase boundary. The new content here is the simultaneous sharp solution of two normalized design criteria and the exceptional coupling where they agree.

## Limitations
The model is finite-dimensional and specific to the standard two-state Jordan generator. The subcritical optimal lower frame bound is proved strictly below the universal ceiling but is not evaluated explicitly. General optimal actuator design and the use of Lyapunov Gramians are longstanding; an equivalent older special-case optimization cannot be excluded without exhaustive historical coverage. The work has not undergone independent audit.

## References
- V. Bailey, E. A. Gallardo-Gutiérrez and J. R. Partington, *Frames Associated with \(C_0\)-Semigroups*, arXiv:2611.13867v1, first posted 10 November 2026, https://arxiv.org/html/2611.13867v1.
- Classical continuous-time controllability Gramian and Lyapunov identity (used as background; the explicit optimization is proved above).
