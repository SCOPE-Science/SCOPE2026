# A sixteen-point Fourier observability crossover for second-shortest chords in Catalan matchings

## Finding
For every integer \(m\ge4\), sample uniformly a noncrossing perfect matching on \(2m\) cyclically ordered, individually labeled points \(\mathbb Z_{2m}\). Let \(X_i\) indicate that the chord joining \(i\) to \(i+3\) is present (modulo \(2m\)), and let \(K_m=\operatorname{Cov}(X_0,\dots,X_{2m-1})\). Thus \(X_i\) observes the shortest non-boundary chord, enclosing exactly two consecutive vertices. Set
\[
 C_s=\frac{1}{s+1}\binom{2s}{s},\qquad
 p_m=\frac{C_{m-2}}{C_m},\qquad q_m=\frac{C_{m-4}}{C_m},\qquad
 D_3(t)=1+2\cos t+2\cos(2t)+2\cos(3t).
\]
The unitary discrete Fourier basis diagonalizes the *ordinary*, probability-normalized covariance \(K_m\), with the complete spectrum
\[
 \boxed{\Lambda_{m,0}=p_m+(2m-7)q_m-2mp_m^2,\quad
 \Lambda_{m,j}=p_m-q_mD_3(\pi j/m)\quad(1\le j<2m).}
\]
Every eigenvalue is positive. The unique minimum is the constant frequency \(j=0\) for \(4\le m\le7\). For every \(m\ge8\) it occurs exactly at frequencies \(j=1,2m-1\). Hence the first-mode observability switch occurs at **sixteen boundary vertices**.

Let \(\kappa_m=\max_j\Lambda_{m,j}/\min_j\Lambda_{m,j}\). Then
\[
 \boxed{\kappa_m\le \frac{21}{5}\qquad(m\ge4),}
\]
with equality *only* at \(m=4\). The maximizing Fourier frequency eventually approaches the interior angle
\[
 \theta_*=\arccos\!\left(\frac{\sqrt7-1}{6}\right),
\]
in either orientation; the limiting condition ratio is exactly
\[
 \boxed{\lim_{m\to\infty}\kappa_m=\frac{439+14\sqrt7}{243}.}
\]
This is a finite-size, position-resolved harmonic-observability theorem; it is not merely a formula for the total number of short chords.

## Assumptions and scope
The vertices are \(0,1,\ldots,2m-1\) in cyclic order and all Catalan-number many noncrossing perfect matchings are equally probable. A chord \(\{i,i+3\}\) is distinguished by its start \(i\), so there are \(2m\) coordinates. The restriction \(m\ge4\) guarantees that the length-three chord and its reverse are distinct observations. Fourier vectors are \((e^{2\pi i j r/(2m)})_{r=0}^{2m-1}/\sqrt{2m}\). Condition ratios refer to the eigenvalues of the unscaled covariance, not to its inverse or to an unnormalized Gram matrix.

## Proof
**1. Exact one- and two-chord probabilities.** A prescribed chord \(\{i,i+3\}\) forces the unique interior pair \(\{i+1,i+2\}\). The remaining \(2m-4\) vertices admit \(C_{m-2}\) noncrossing matchings; thus \(\mathbb EX_i=p_m\). Distinct indicated chords whose starting points have cyclic distance 1, 2, or 3 conflict by crossing or sharing an endpoint. Two indicated chords at distance at least 4 in both cyclic directions occupy disjoint blocks of four vertices and leave exactly \(C_{m-4}\) choices. Consequently, writing \(d\) for their cyclic start separation,
\[
 \mathbb E[X_0X_d]=\begin{cases}
 p_m,&d=0,\\
 0,&1\le\min(d,2m-d)\le3,\\
 q_m,&4\le d\le2m-4.
 \end{cases}
\]
The first row of the covariance matrix is therefore \(p_m-p_m^2\) at displacement zero, \(-p_m^2\) at cyclic displacements 1, 2, 3, and \(q_m-p_m^2\) elsewhere. The geometric-sum identity for nonzero characters gives the displayed Fourier eigenvalues. At the constant character, simply sum the first row.

**2. Strict positive definiteness.** There exists a noncrossing matching with no indicated chords: pair consecutive vertices \((0,1),(2,3),\ldots\). For each \(i\), the matching containing \((i,i+3),(i+1,i+2)\) and then consecutive pairings along the remaining clockwise arc has *exactly* the single indicated chord \(i\). All these matchings have positive sampling probability. Thus the support of the observation vector contains the origin and every standard basis vector. Its covariance is positive definite (any nonzero linear functional takes distinct values at these support points).

**3. Lowest nonconstant Fourier mode.** Set \(c=\cos t\). Then \(D_3(t)=8c^3+4c^2-4c-1\). Its stationary cosines are \(c_\pm=(-1\pm\sqrt7)/6\). On \([-1,1]\) the secondary local maximum is \((-7+14\sqrt7)/27<2\), while \(D_3(\pi/m)\ge D_3(\pi/5)=(3+\sqrt5)/2>2\) for \(m\ge5\). Since \(D_3\) increases on \([c_+,1]\), its maximum among the nonzero sampled arguments \(\pi j/m\), \(1\le j<2m\), occurs exactly at \(j=1,2m-1\) for \(m\ge5\). For \(m=4\), the sampled values can be inspected directly; the constant mode is smaller than all nonconstant ones.

**4. Sharp switch at \(m=8\).** Write \(T_m=2m(1-p_m^2/q_m)\). From the exact probabilities,
\[
 T_m=\frac{12m(4m^2-10m+1)}{(m-2)(m-1)(2m-3)(2m-1)},\qquad
 \Lambda_{m,0}-\Lambda_{m,1}=q_m\{T_m-[7-D_3(\pi/m)]\}.
\]
For \(m=4,\ldots,7\) the bracket is strictly negative, and for \(m=8,\ldots,11\) it is strictly positive. These eight finite inequalities have reproducible *exact rational interval certificates* in `check.py`: use the alternating arctangent series and \(\pi=16\arctan(1/5)-4\arctan(1/239)\), then the alternating cosine Taylor bounds of degrees 14 and 16. This is a rigorous rational sign test, not floating-point evidence. For every \(m\ge12\),
\[
 T_m-\frac{12}{m}
 =\frac{12(10m^3-34m^2+25m-6)}{m(m-2)(m-1)(2m-3)(2m-1)}\ge0,
\]
where the numerator polynomial has positive coefficients in \(m-4\). Also \(7-D_3(\pi/m)\le14\pi^2/m^2<140/m^2<12/m\) for \(m\ge12\). Hence the difference is positive in all remaining cases.

**5. Sharp all-size condition bound.** The global minimum of \(D_3\) on the cosine interval is \(D_{\min}=-(7+14\sqrt7)/27>-2\), so \(\Lambda_{m,j}<p_m+2q_m\) for each nonzero frequency. The constant mode is also smaller than \(p_m+q_m\); indeed \(p_m+q_m-\Lambda_{m,0}\) has positive denominator and numerator proportional to
\[
 8(m-4)^4+76(m-4)^3+244(m-4)^2+299(m-4)+120.
\]
At \(m=4\), the explicit eigenvalues give \(\Lambda_{4,0}=5/98\) and \(\max_j\Lambda_{4,j}=3/14\), hence \(\kappa_4=21/5\). For \(m=5,6,7\), using the proven constant-mode minimum, the rational bounds
\[
 \kappa_5<147/43,\quad\kappa_6<99/34,\quad\kappa_7<7436/2779
\]
all lie below \(21/5\). At \(m=8\), \(D_3(\pi/8)<6\), giving \(\kappa_8<10/3\). For \(m\ge9\), the ratio
\[
 q_m/p_m=\frac{(m-1)(m-2)}{4(2m-5)(2m-7)}
 \le\frac{14}{143}
\]
is decreasing, while \(\Lambda_{m,1}\ge p_m-7q_m\). Thus
\[
 \kappa_m<\frac{p_m+2q_m}{p_m-7q_m}\le\frac{19}{5}<\frac{21}{5}.
\]
The equality case is therefore unique.

**6. Limiting spectrum.** The exact Catalan quotients yield \(p_m\to1/16\), \(q_m\to1/256\), and \(\Lambda_{m,0}\to9/256\). The minimum nonconstant eigenvalue tends to \((16-7)/256=9/256\). The sampled mesh becomes dense, and the unique continuous minimizing cosine \(c_+\) gives \(\max_j\Lambda_{m,j}\to(439+14\sqrt7)/6912\). Dividing by the minimum establishes the sharp limit and the location of any maximizing frequencies.

## Verification
Run `python3 check.py` with standard Python 3. It independently enumerates all \(C_m\) matchings for \(m=4,5,6,7,8\), checks the entire cyclic pair-moment kernel, certifies the eight finite crossover signs by exact rational bounds for \(\pi\) and cosine, checks the rational bounds for an additional range, and compares finite Fourier transforms through \(m=100\). All 25,638 assertions passed in the reproduced run. All-size inequalities, positivity and the limit are proved above; finite tests alone are not extrapolated to infinitely many \(m\).

## Relationship to prior work
The literature on Catalan noncrossing matchings includes distributional and cyclic-sieving results for **adjacent** short edges: Young's *Linear k-Chord Diagrams* (2020), and Alexandersson–Linusson–Potka–Uhlin's *Refined Catalan and Narayana cyclic sieving* (2020 preprint; 2021 journal). In the latter, Section 4.2 and Theorem 27 treat the number of adjacent short edges, rather than individual length-three chord observations or their Fourier covariance. Their Section 9 treats marked regions, not a position-resolved spectrum. These works motivate local chord statistics but do not supply the new finite-size switch or interior maximum displayed here.

The same elementary Catalan deletion method also underlies other local-pattern covariance calculations; the novelty assessed here concerns the complete spatial Fourier conclusion for the second-shortest chord pattern, including an interior highest-variance angle and a sharp global conditioning optimum. The proof is not a claim that Catalan enumeration or Fourier diagonalization themselves are new.

## Limitations
Only uniformly sampled noncrossing perfect matchings of a single labeled circular boundary, with the prescribed chord span three and \(m\ge4\), are covered. The theorem does not classify arbitrary chord spans, weighted matchings, arbitrary linear measurements, or higher-order moments. A thorough published-history search and targeted existing-result comparisons found no exact covering theorem, but historical priority is not independently certified; an earlier unindexed specialization or an implicit consequence of a broader published chord-correlation theorem remains possible. The full text of Young's 2020 paper was not available for complete inspection; its abstract explicitly restricts the refined statistics to short (adjacent) chords, making hidden full-theorem coverage unlikely but not impossible.

## References
1. D. Young, *Linear k-Chord Diagrams*, Journal of Integer Sequences **23** (2020), Article 20.9.1, published 13 October 2020. https://cs.uwaterloo.ca/journals/JIS/VOL23/Young/young5.html
2. P. Alexandersson, S. Linusson, S. Potka, J. Uhlin, *Refined Catalan and Narayana cyclic sieving*, arXiv:2010.11157, first posted 21 October 2020; Combinatorial Theory **1** (2021). https://arxiv.org/abs/2010.11157
3. M. Milich, T. Mütze, M. Pergel, *On flips in planar matchings*, Discrete Applied Mathematics **289** (2021), 427–445; preprint linked at https://wrap.warwick.ac.uk/142371/ . Related ensemble and rotation, but a different question.
