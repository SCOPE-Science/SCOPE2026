# Sampling-law reversal of bounded-variation stability for random interval inversions

## Finding
For each integer \(n\ge2\), reverse a contiguous interval of a real \(n\)-vector and average the resulting vectors. Two natural sampling conventions yield qualitatively different sharp adjacent-variation operator norms.

* If each of the \(n(n+1)/2\) nonempty intervals is equally likely, then the sharp coefficient is exactly
  \[
  C_n^{\mathrm{interval}}=\frac{n-1}{n+1}<1.
  \]
* If an interval length is sampled uniformly from \(1,\ldots,n\), and then its starting position is sampled uniformly among its admissible placements, the sharp coefficient \(C_n^{\mathrm{length}}\) is at most one for every \(2\le n\le13\), but
  \[
  C_{14}^{\mathrm{length}}=\frac{5105521}{5045040}=1+\frac{60481}{5045040}>1.
  \]
  Thus fourteen sites are the exact first dimension of amplification. Moreover,
  \[
  \liminf_{n\to\infty}C_n^{\mathrm{length}}\ge1+\log\frac43>1.
  \]
The first conclusion holds for every dimension, while the second finite cutoff is exhaustively rationally certified and the asymptotic inequality follows from an explicit continuum step witness. No exact value of the length-uniform asymptotic coefficient is claimed.

## Assumptions and scope
All vectors are real, with sites indexed \(1,\ldots,n\) on a nonperiodic unit-edge path. Define \(V_n(h)=\sum_{i=1}^{n-1}|h_{i+1}-h_i|\). Reversal of \([a,b]\) acts by \((R_{a,b}h)_i=h_{a+b-i}\) for \(a\le i\le b\) and fixes other coordinates. Let \(P_n^{\mathrm{interval}}\) and \(P_n^{\mathrm{length}}\) denote their averages under the two specified laws. Define the sharp seminorm coefficient
\[
C_n(P)=\sup_{V_n(h)>0}\frac{V_n(Ph)}{V_n(h)}.
\]
Both averages preserve constants, so the quotient is meaningful, and every asserted finite sharp coefficient is attained on a single-jump signal.

## Proof
**Step reduction.** Put \(H^{(k)}_i=\mathbf1_{\{i>k\}}\), \(1\le k<n\). Every vector has the exact decomposition \(h=h_1\mathbf1+\sum_{k=1}^{n-1}(h_{k+1}-h_k)H^{(k)}\). If \(P\mathbf1=\mathbf1\), the triangle inequality for \(V_n\) implies
\[
C_n(P)=\max_{1\le k<n}V_n(PH^{(k)}).
\]
This equality is exact because each test step has input variation one.

**Uniform intervals.** Put \(N=n(n+1)/2\) and \(d_{ik}=N((PH^{(k)})_{i+1}-(PH^{(k)})_i)\), with \(1\le i,k<n\). Counting intervals whose reversed positions straddle the cut gives
\[
d_{ik}=\begin{cases}
(n-k)-\min(i,n-k),&i<k,\\
\frac{k(k-1)}2+\frac{(n-k-1)(n-k)}2+n-\min(k,n-k),&i=k,\\
k-\min(k,n-i),&i>k.
\end{cases}
\]
Each entry is nonnegative. The two endpoint responses are \((PH^{(k)})_1=(n-k)/N\) and \((PH^{(k)})_n=1-k/N\). Thus every step response is nondecreasing and has variation \(1-n/N=(n-1)/(n+1)\). Step reduction proves the sharp coefficient, with equality for every single jump. The counting identity includes intervals of length one.

**Length-uniform first onset.** An interval \([a,b]\) with length \(\ell=b-a+1\) has probability \(1/[n(n-\ell+1)]\). Consequently the exact rational test value for each \(k\) is
\[
q_{n,k}=\sum_{i=1}^{n-1}\left|\sum_{\ell=1}^n\frac1{n(n-\ell+1)}\sum_{a=1}^{n-\ell+1}\left(\mathbf1_{\{R_{a,a+\ell-1}(i+1)>k\}}-\mathbf1_{\{R_{a,a+\ell-1}(i)>k\}}\right)\right|.
\]
Here \(R_{a,b}(i)\) means the image of the **index** \(i\) under the reversal, not the action on data. The exact coefficient is \(\max_{1\le k<n}q_{n,k}\). The standalone `verify.py` uses only integer/rational arithmetic to evaluate both a direct step action and an independently built position-transition matrix, for every cut and every dimension \(2\le n\le14\). The resulting exact maxima, in order, are
\[
0,\ \frac12,\ \frac58,\ \frac{41}{60},\ \frac{271}{360},\ \frac{113}{140},\ \frac{2813}{3360},\ \frac{824}{945},\ \frac{5689}{6300},\ \frac{3254}{3465},\ \frac{322507}{332640},\ \frac{355991}{360360},\ \frac{5105521}{5045040}.
\]
The maximum at \(n=14\) is realized by \(k=5\) or \(k=9\), so distinct finite input vectors attain the displayed amplification. The exact finite certificate establishes the cutoff, not an extrapolated all-dimensional formula.

**Asymptotic witness.** In the continuum model choose an interval length \(\ell\) uniformly in \((0,1)\), then its left endpoint uniformly in \((0,1-\ell)\), and reverse that interval. For a step at \(t\), write \(F_t(x)\) for the expected image. For \(x<s\), the crossing probability from \(x\) to above \(s\) is
\[
G_s(x)=\int_0^1\frac{[\min(x,1-\ell)-\max\{0,x-\ell,(x+s-\ell)/2\}]_+}{1-\ell}\,d\ell.
\]
Reflection symmetry gives \(F_t(x)=1-G_{1-t}(1-x)\) when \(x>t\). Directly integrating at \(t=1/3\) yields
\[
G_{2/3}(2/3^-)=\tfrac12\log3-\tfrac23\log2,
\qquad G_{2/3}(1/3)=\tfrac13\log2.
\]
Hence \(F_{1/3}((1/3)^+)-F_{1/3}(2/3)=\log(2/\sqrt3)>0\), while \(F_{1/3}(0)=0\) and \(F_{1/3}(1)=1\). Summing absolute changes along the ordered sample positions \(0,(1/3)^+,2/3,1\) gives
\[
V(F_{1/3})\ge1+2\log(2/\sqrt3)=1+\log(4/3).
\]
To transfer this lower bound to finite dimensions, take \(k_n=\lfloor n/3\rfloor\) and test \(P_n^{\mathrm{length}}H^{(k_n)}\) at sites \(1,k_n+1,\lfloor2n/3\rfloor,n\). The four expected values converge respectively to the four continuum one-sided values above: these are Riemann sums over lengths and admissible left endpoints; the integrands are bounded by one, and boundary discontinuity sets have zero two-dimensional measure. Their three absolute successive differences provide the same lower bound on the limiting inferior of the sharp variation coefficients.

## Verification
Run `python3 verify.py` using the Python standard library. It compares the length-uniform step-action formula to independently constructed transition matrices for every \(2\le n\le14\), records every exact coefficient, and confirms the fourteen-site cutoff. It also checks the combinatorial uniform-interval gradient identity and its exact contraction coefficient on finite test dimensions. The unrestricted uniform-interval result and the asymptotic length-uniform lower bound follow from the preceding analytical proofs, not from finite numerical sampling.

## Relationship to prior work
Durrett's *Shuffling Chromosomes* introduces interval-reversal permutation models on a line and a circle. Cancrini–Caputo–Martinelli study spectral gaps for cyclic length-uniform reversal chains; Morris studies entropy and mixing time for cyclic reversal chains. Their primary results involve permutation-state relaxation and distributional total variation, rather than the path-seminorm operator induced on **one scalar signal by one averaged reversal**. In particular, neither their spectral-gap bounds nor their mixing estimates imply the first-amplification cutoff above. The present proof uses the single-jump basis for the finite path seminorm and does not claim results on mixing of full permutation distributions.

## Limitations
The result concerns one reversal-average step on an unweighted nonperiodic path. No exact formula for the length-uniform norm for all dimensions, no exact large-dimensional limit, and no multi-step, weighted, or cyclic extension is proved. The 2003 foundational paper's exact first public calendar day was not established; the recorded lead-source date uses the earliest verified day-precise preprint identified in the source comparison. Historical priority beyond the inspected and indexed literature is not independently certified.

## References
- Rick Durrett, *Shuffling Chromosomes*, Journal of Theoretical Probability 16 (2003), 725–750, DOI: https://doi.org/10.1023/A:1025676617383 ; author-hosted full text https://sites.math.duke.edu/~rtd/reprints/paper128.pdf .
- N. Cancrini, P. Caputo and F. Martinelli, *Relaxation time of \(L\)-reversal chains and other chromosome shuffles*, first arXiv version 2004-12-22, https://arxiv.org/abs/math/0412449 ; full text https://www.mat.uniroma3.it/users/caputo/research/aap_paper.pdf .
- Ben Morris, *Improved mixing time bounds for the Thorp shuffle and \(L\)-reversal chain*, first arXiv version 2008-02-04, https://arxiv.org/abs/0802.0339 .
