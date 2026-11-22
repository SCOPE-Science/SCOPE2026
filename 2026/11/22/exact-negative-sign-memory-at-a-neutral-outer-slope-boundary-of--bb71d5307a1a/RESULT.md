# Exact negative sign-memory at a neutral outer-slope boundary of a fixed-point-free map

## Finding
For each integer \(m\ge2\), the natural neutral-outer-slope member of the fixed-point-free four-branch family has a uniquely determined absolutely continuous stationary law. Its sign output exhibits an *exact, negative, macroscopic-lag autocorrelation trough* although the probability of a sign change at one step tends to zero as \(m\to\infty\).

With \(S(x)=\operatorname{sgn}(x)\), define \(C_m(n)=\int S(x)S(f_m^n(x))\,d\mu_m(x)\). For every integer \(0\le n\le m\),
\[
\boxed{C_m(n)=\frac{1-7m+4n+8m(1-1/m)^n}{m+1}.}
\]
Its minimum for these lags has limiting value \(4\log 2-3\), attained at rescaled lag \(\log2\). More precisely,
\[
\sup_{0\le t\le1}\left|C_m(\lfloor tm\rfloor)-(8e^{-t}+4t-7)\right|\longrightarrow0.
\]

## Assumptions and scope
The integer \(m\) is at least two. On the real interval \([-m,m]\), use the piecewise-affine map
\[
f_m(x)=\begin{cases}
x+1,&-m\le x\le-1,\\
m(x+1),&-1<x<0,\\
m(x-1),&0\le x<1,\\
x-1,&1\le x\le m.
\end{cases}
\]
This is the specialization \((m_1,m_2,b_1,a,b_2)=(1,m,1,1,m)\) of the four-branch García-Grimaldo--Campos-Cantón family. It is invariant on \([-m,m]\), and has no fixed points. Breakpoint orbits and their preimages form a countable set of zero Lebesgue measure; the stationary statements concern the absolutely continuous law, not all invariant probabilities.

For \(0\le k\le m-1\), let \(R_k=(k,k+1)\) and \(L_k=(-k-1,-k)\). The density of the unique absolutely continuous invariant probability \(\mu_m\) is
\[
\boxed{h_m(x)=\frac{m-k}{m(m+1)}\quad(k<|x|<k+1).}
\]
The sign observable is \(+1\) on the positive half and \(-1\) on the negative half. Its stationary mean is zero and variance is one.

## Proof
**1. Markov dynamics and stationary density.** Every outer cell \(R_k\) or \(L_k\) with \(k>0\) maps bijectively, by translation, onto the cell of the same sign and index \(k-1\). Each central cell \(R_0\) or \(L_0\) maps by slope \(m\) across all \(m\) cells of the *opposite* sign. Relative to normalized Lebesgue measure on the central cell, its next landing index is exactly uniform on \(\{0,\ldots,m-1\}\). All cell densities are constant under the transfer operator, so the cell probabilities \(\pi(R_k)=\pi(L_k)=(m-k)/[m(m+1)]\) satisfy every balance equation, and their total is one. This proves the asserted explicit invariant density.

Every itinerary of \(m\) consecutive steps contains a central expanding branch, so the derivative of every smooth branch of \(f_m^m\) has magnitude at least \(m>1\). The finite Markov graph is irreducible, and has central return loops of lengths two and three; hence it is aperiodic. By the elementary finite-Markov uniformly-expanding interval-map theorem (equivalently, contraction of generating cylinders and the Perron--Frobenius transfer argument), this gives the unique absolutely continuous invariant probability. No uniqueness among arbitrary singular invariant probabilities is asserted.

**2. Uniform renewal clock.** Each visit to either central cell starts a new excursion into the opposite sign. Its duration \(T\) until the *next* central visit is independent of the past and uniformly distributed on \(\{1,2,\ldots,m\}\): the first iterate chooses one of the opposite-sign cells uniformly and translation then decrements that cell's index. The returned coordinate is uniform in the next central cell, so successive durations are independent. Signs flip at excursion starts and remain unchanged during the exterior translations.

Let \(q_m(n)\) be the expected sign at time \(n\), relative to its sign at a central departure at time zero. For \(0\le n\le m\), conditioning on the uniform first duration gives
\[
q_m(0)=1,\qquad q_m(n)=\frac{m-n}{m}-\frac1m\sum_{r=1}^{n}q_m(n-r).
\]
Subtracting consecutive recurrences yields \(q_m(n)+1=(1-1/m)(q_m(n-1)+1)\); therefore
\[
q_m(n)=2(1-1/m)^n-1\qquad(0\le n\le m).
\]

**3. Exact time-stationary correlation.** A stationary point in one of the cells of index \(r-1\) waits exactly \(r\) steps until the next sign flip. Consequently its residual waiting-time distribution is
\[
\rho_m(r)=\frac{2(m-r+1)}{m(m+1)},\qquad1\le r\le m.
\]
Conditional on this first flip, the future sign relative to the original sign has expected value \(-q_m(n-r)\). For \(0\le n\le m\),
\[
C_m(n)=\mathbb P(R>n)-\sum_{r=1}^{n}\rho_m(r)q_m(n-r)
=1-\frac4{m(m+1)}\sum_{r=1}^{n}(m-r+1)(1-1/m)^{n-r}.
\]
The finite geometric-arithmetic sum is exactly
\[
\sum_{r=1}^{n}(m-r+1)(1-1/m)^{n-r}=m(2m-n)-2m^2(1-1/m)^n.
\]
Substitution yields the boxed formula. In particular \(C_m(0)=1\), while \(C_m(1)=1-4/(m+1)\), so the stationary probability of a sign change in one step is \(2/(m+1)\).

**4. Exact minimizing lag and macroscopic limit.** For \(0\le n<m\),
\[
C_m(n+1)-C_m(n)=\frac{4-8(1-1/m)^n}{m+1}.
\]
Thus the sequence first decreases and then increases, with minimum at \(n_m=\lceil\log(1/2)/\log(1-1/m)\rceil\). Equality in a step would require \(2(m-1)^n=m^n\), which, because consecutive integers are coprime, occurs only for \((m,n)=(2,1)\), producing the stated tie. Since \((1-1/m)^m<1/2\), this minimum lies in the asserted lag range. As \(m\to\infty\), \(n_m/m\to\log2\), and \((1-1/m)^{\lfloor tm\rfloor}\to e^{-t}\) uniformly on \([0,1]\). The limiting smooth profile has its unique minimum \(4\log2-3<0\) at \(t=\log2\).

## Verification
The standalone Python checker `verify_stationary_sign.py` evaluates the finite-state transition matrix using exact rational arithmetic. It independently compares the matrix-derived correlations against the claimed closed form for all \(m=2,\ldots,30\) and \(0\le n\le m\), checks the invariant cell probabilities, and checks minimizing indices and branch maps. It passes 493 exact correlation comparisons. These finite checks are supplementary; the proof of the statement for all integers \(m\ge2\) is the analytic argument above.

Run with `python3 verify_stationary_sign.py` using Python's standard library only.

## Relationship to prior work
García-Grimaldo and Campos-Cantón introduced the PWL fixed-point-free family in their 2021 article. The 2023 FPGA article studies its numerical bifurcations, Lyapunov exponents, state histograms and implementation; it does not state this stationary sign-correlation formula. Their 2023 doctoral thesis includes exact fixed-point classification for the source family and numerical autocorrelation of other pseudorandom outputs, but the inspected source-family and autocorrelation sections do not yield this precise stationary-sign theorem. Broader general finite-state Markov-renewal methods provide ingredients, not the model-specific density, the closed lag law or its sharp universal trough. The earlier full 2021 article and a 2022 comparative chapter were not fully available for inspection; priority is accordingly qualified rather than independently certified.

## Limitations
The formula is asserted only for integer inner slopes and neutral outer slope, and for lags up to \(m\). The theorem concerns the mathematical absolutely continuous stationary state, not singular invariant measures, finite-precision hardware or computational security. Universal negative correlation does not itself establish a cryptographic vulnerability. Exact applicability to other parameter chambers is not claimed; unseen equivalent prior literature remains a possible publication-priority risk.

## References
1. García-Grimaldo, C., and Campos-Cantón, E., *Chaotic Features of a Class of Discrete Maps without Fixed Points*, International Journal of Bifurcation and Chaos **31** (2021), 2150200. https://doi.org/10.1142/S021812742150200X. Public date reported as 26 October 2021 by MaRDI bibliographic record: https://portal.mardi4nfdi.de/wiki/Chaotic_features_of_a_class_of_discrete_maps_without_fixed_points.
2. García-Grimaldo, C., Bermudez-Marquez, C. F., Tlelo-Cuautle, E., and Campos-Cantón, E., *FPGA Implementation of a Chaotic Map with No Fixed Point*, Electronics **12** (2023), 444, 14 January 2023. https://doi.org/10.3390/electronics12020444.
3. García Grimaldo, C. A., *Design of Piecewise Linear Chaotic Maps and Their Application in Pseudorandom Number Generation*, doctoral thesis (2023), sections 3.1, 3.3, 6.3.3. https://repositorio.ipicyt.edu.mx/bitstream/handle/11627/6492/TesisClaudioGarcia-VersionFinal.pdf?sequence=4.
4. García-Grimaldo, C., and Campos-Cantón, E., *Comparative Analysis of Chaotic Features of Maps Without Fixed Points*, in *Complex Systems and Their Applications* (2022), pp. 151–176. https://doi.org/10.1007/978-3-031-02472-6_8.
