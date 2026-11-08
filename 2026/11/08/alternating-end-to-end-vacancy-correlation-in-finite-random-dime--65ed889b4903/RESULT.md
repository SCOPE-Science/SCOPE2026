# Alternating end-to-end vacancy correlation in finite random dimer parking

## Finding
Consider irreversible random sequential adsorption of dimers on the path with \(n\) labeled sites. At each step an available adjacent pair is eventually attempted, and an attempted pair is accepted exactly when both sites are empty. Equivalently, assign the \(n-1\) edges independent continuous random priorities, examine the edges in increasing order, and greedily retain each edge with both endpoints free. Let \(U_n\) and \(V_n\) be the indicators that the first and last sites remain vacant in the jammed configuration.

**Theorem.** For all integers \(n\ge3\),
\[
(-1)^n\operatorname{Cov}(U_n,V_n)>0.
\]
The covariance of opposite endpoint vacancies alternates in sign at *every* finite size, and has the sharp superfactorial asymptotic
\[
\operatorname{Cov}(U_n,V_n)\sim(-1)^n\frac{2^{n-2}}{(n-1)!}\qquad(n\to\infty).
\]
Set \(b_n=\Pr(U_n=1)\) and \(q_n=\Pr(U_n=V_n=1)\). The exact finite formulas are
\[
b_n=\sum_{j=0}^{n-1}\frac{(-1)^j}{j!}\qquad(n\ge1),
\]
\[
q_n=\frac1{n-1}\sum_{j=0}^{n-4}(n-3-j)\frac{(-2)^j}{j!}\qquad(n\ge4).
\]
Thus \(\operatorname{Cov}(U_n,V_n)=q_n-b_n^2\). The case \(n=3\) has \(b_3=1/2\), \(q_3=0\), and covariance \(-1/4\). For \(n=2\) the two endpoint vacancy indicators are identically zero, hence covariance zero.

## Assumptions and scope
All possible positions of a length-two dimer have identical attempt rates; attempted placements are irreversible and rejected on overlap. The equivalent independent continuous random-priority construction makes the first accepted edge uniform over \(n-1\) edges, and makes disjoint residual subpaths independent. The result is finite-volume, with *free boundaries*. It is not asserted for periodic boundaries, length-three or longer adsorbates, biased arrivals, or adsorption–desorption dynamics. The asymptotic equivalence is for integer \(n\) tending to infinity.

## Proof
**1. Recursions.** Define \(b_0=0\), \(b_1=1\), \(q_1=1\), and \(q_2=0\). The first accepted dimer spans \(j,j+1\), uniformly over \(1\le j\le n-1\). It leaves independent subpaths of lengths \(j-1\) and \(n-j-1\). The left endpoint can survive only if the first edge starts at \(j\ge2\). Consequently, for \(n\ge2\),
\[
(n-1)b_n=\sum_{k=1}^{n-2} b_k,
\qquad
(n-1)q_n=\sum_{k=1}^{n-3}b_k b_{n-2-k}.
\]
All empty sums vanish. These equations encode the entire joint endpoint event, including the small-size boundary cases.

**2. Exact coefficients.** With \(B(z)=\sum_{n\ge1}b_nz^n\), the first recursion gives \(B'(z)-B(z)/z=zB(z)/(1-z)\), with \(B(z)/z\to1\) as \(z\to0\). Therefore
\[
B(z)=\frac{ze^{-z}}{1-z}.
\]
Its coefficients are the stated alternating exponential truncations. From the second recursion, \((n-1)q_n\) is the coefficient of \(z^{n-2}\) in \(B(z)^2=z^2e^{-2z}(1-z)^{-2}\); extracting coefficients gives the stated formula for \(q_n\).

**3. A sign-preserving integral representation.** Write \(m=n-4\ge0\), \(T_m(2)=\sum_{j=0}^m(-2)^j/j!\), and let \(e^{-1}\) and \(e^{-2}\) be the exponential constants. Finite-sum algebra yields
\[
q_n=T_m(2)-\frac{2(-2)^m}{(m+3)m!}.
\]
Taylor's remainder, with \(\Delta(t)=e^{-2t}-(1-t)^2\), then gives
\[
q_n-e^{-2}=\frac{2(-2)^m}{m!}\int_0^1(1-t)^m\Delta(t)\,dt.
\]
Likewise,
\[
b_n-e^{-1}=\frac{(-1)^{n+1}}{(n-1)!}\int_0^1(1-t)^{n-1}e^{-t}\,dt.
\]
Since \(\log(1-t)<-t\) for \(0<t<1\), we have \(e^{-2t}>(1-t)^2\) and hence \(\Delta(t)>0\). Both \(b_n\) and \(e^{-1}\) are positive. Since
\[
q_n-b_n^2=(q_n-e^{-2})-(b_n-e^{-1})(b_n+e^{-1}),
\]
the two terms on the right have **the same sign** \((-1)^n\) for every \(n\ge4\). Explicitly,
\[
\begin{aligned}
(-1)^n\operatorname{Cov}(U_n,V_n)
={}&\frac{2^{n-3}}{(n-4)!}\int_0^1(1-t)^{n-4}\Delta(t)\,dt\\
&+\frac{b_n+e^{-1}}{(n-1)!}\int_0^1(1-t)^{n-1}e^{-t}\,dt>0.
\end{aligned}
\]
The direct case \(n=3\) supplies the remaining strict inequality.

**4. Sharp scale.** Expansion near zero gives \(\Delta(t)=t^2+O(t^3)\). For \(m\to\infty\), beta-integral concentration at zero yields
\[
\int_0^1(1-t)^m\Delta(t)\,dt
\sim\int_0^1(1-t)^mt^2\,dt
=\frac{2}{(m+1)(m+2)(m+3)}.
\]
For rigor, \(\Delta(t)/t^2\) extends continuously to \([0,1]\) with value \(1\) at zero, is bounded, and the beta probability densities proportional to \(t^2(1-t)^m\) concentrate at zero. Thus the first displayed term in step 3 is asymptotic to \(2^{m+2}/(m+3)!=2^{n-2}/(n-1)!\). The second is at most \(O(1/((n-1)!n))\), using \(\int_0^1(1-t)^{n-1}dt=1/n\), and is therefore negligible on this scale. This proves the claimed asymptotic.

## Verification
The included standalone `verify.py` uses exact rational arithmetic to check the recursions, coefficient formulas and signs through \(n=100\). It also exhaustively enumerates all \((n-1)!\) priority orders for each \(3\le n\le9\), independently producing the two endpoint probabilities. Every tested identity matches the analytic expressions. These finite tests are consistency checks, not proofs of the universal inequalities or asymptotic; steps 1–4 supply those proofs.

## Relationship to prior work
The process is the classical one-dimensional lattice dimer adsorption model. Page (1959) studies the distribution and moments of total vacancies on a finite line, and Evans (1993) surveys irreversible adsorption, jamming and correlation methods. Bonnier, Boyer and Viot (1994) derive spatial pair distribution functions for one-dimensional lattice adsorption, emphasizing super-exponential decay. Their infinite-system pair functions do not by themselves identify the exact **two free endpoints of a path of arbitrary finite length**, and a result about total vacancy counts does not by itself identify this labeled pair event. The formula, sign alternation and sharp prefactor here are stated for that finite boundary pair. A later full-text analysis by Coletti and collaborators (2024) concerns a distinct nearest-neighbor exclusion process with single-site arrival choices and global density fluctuations, rather than this edge-priority dimer process.

## Limitations
The primary Page (1959) and Bonnier–Boyer–Viot (1994) articles were identifiable but their full texts were not accessible in the comparison; their abstracts and bibliographic descriptions cannot establish absence of an implicit finite-volume formula. Priority therefore remains qualified. The proof gives no claim of independent verification, no general correlation ordering for all interior site pairs, and no temporal correlation statement before jamming.

## References
1. E. S. Page, “The Distribution of Vacancies on a Line,” *Journal of the Royal Statistical Society B* **21** (1959), 364–374. https://doi.org/10.1111/j.2517-6161.1959.tb00343.x
2. J. W. Evans, “Random and cooperative sequential adsorption,” *Reviews of Modern Physics* **65** (1993), 1281–1329. https://doi.org/10.1103/RevModPhys.65.1281
3. B. Bonnier, D. Boyer, P. Viot, “Pair correlation function in random sequential adsorption processes,” *Journal of Physics A* **27** (1994), 3671–3682. https://doi.org/10.1088/0305-4470/27/11/017
4. C. F. Coletti, S. Gallo, A. Roldán-Correa, L. A. Valencia, “Fluctuations of the Occupation Density for a Parking Process,” *Journal of Statistical Physics* **191** (2024), article 146. https://doi.org/10.1007/s10955-024-03336-2
