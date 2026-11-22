# A sharp half-retention bimodality threshold for periodic shot-noise first-passage summands

## Finding
For deterministic interarrival times and exponentially marked renewal shot noise, the normalized contributions to the exact finite-threshold mean first-passage-time (MFPT) series are log-concave for every threshold **if and only if** the one-period retained fraction satisfies \(0<q\leq 1/2\). For \(q>1/2\), the contributions have **exactly two strict local modes** for an explicit, nonempty interval of thresholds (apart from isolated ties): the first is index \(1\), and the second occurs at index at least \(3\). The first change in their global maximizing index skips index \(2\), at a finite, exactly specified crossover.

Define
\[
 a_n(q)=\frac{1-q^n}{n+1}\quad(n\geq1),\qquad
 M(q)=\max_{n\geq2}a_n(q).
\]
For \(q>1/2\), one has \(M(q)>a_1(q)=(1-q)/2\). Every threshold
\[
 \frac1{M(q)}<x<\frac2{1-q},\qquad
 x\notin\{1/a_n(q):n\geq1\},
\]
produces exactly two strict local maxima of the MFPT summands. Conversely, no threshold gives two strict local maxima if \(q\leq1/2\).

Moreover the first global-mode transition away from index \(1\), as \(x\) increases from \(1\), is at
\[
 x_c(q)=\min_{n\geq3}\left(\frac{n!}{\prod_{j=1}^{n-1}(1-q^j)}\right)^{1/(n-1)},
 \qquad \frac1{M(q)}<x_c(q)<\frac2{1-q}.
\]
For \(1<x<x_c(q)\), index \(1\) uniquely maximizes the entire sequence. At \(x=x_c(q)\), index \(1\) ties globally with an index at least \(3\), while index \(2\) is strictly below them. For any \(x>x_c(q)\), index \(1\) is not a global maximizer. This is a statement about the **auxiliary series weights**, not the probability distribution of the physical first-crossing index.

## Assumptions and scope
Fix \(w>0\), relaxation \(\gamma>0\), exponential mark rate \(\lambda>0\), and threshold \(b>0\). Let jumps of independent \(\operatorname{Exp}(\lambda)\) amplitudes arrive at deterministic times \(w,2w,3w,\ldots\), and let the signal decay exponentially at rate \(\gamma\) between jumps, initially at zero. Put \(q=e^{-\gamma w}\in(0,1)\) and \(x=\lambda b\). Let \(T_b\) be the first time the signal exceeds \(b\), and define
\[
 C_0=1,\qquad C_n=\frac{x^n}{n!}\prod_{j=1}^{n-1}(1-q^j)\quad(n\geq1),
\qquad \mathbb E T_b=w\sum_{n=0}^{\infty}C_n.
\]
The exact MFPT expansion, the definition of its auxiliary Poisson smoothing weights, and its adjacent-term ratio come from Wang and Zhang (2026); the classification above concerns these exact finite-threshold contributions. A strict local mode at a positive index exceeds both adjacent terms; at index zero it means \(C_0>C_1\). Normalization by \(\sum_j C_j\) does not affect locations of modes.

## Proof
**Premise and convergence.** The embedded process immediately after arrivals satisfies \(R_n=qR_{n-1}+E_n\), where \(E_n\) are independent rate-one exponentials and \(R_0=0\). From the first-step renewal equation for the hitting index (or the established exact renewal MFPT expansion), the displayed series holds. Because \(0<\prod_{j=1}^{n-1}(1-q^j)\le1\), it converges absolutely. The ratio identities are
\[
 \frac{C_1}{C_0}=x,\qquad
 \frac{C_{n+1}}{C_n}=x a_n(q),\quad n\ge1.
\]

**Single-hump ratio lemma.** For \(n\ge1\), direct multiplication by positive denominators gives
\[
 a_{n+1}>a_n\iff F_n(q)>1,\quad
 F_n(q)=q^n\bigl[(n+2)-(n+1)q\bigr].
\]
A key *strict*, globally valid identity is
\[
 F_n(q)-F_{n+1}(q)=(n+2)q^n(1-q)^2>0.
\]
Also \(F_n(q)\to0\) and \(F_1(q)=q(3-2q)\), which exceeds \(1\) exactly when \(q>1/2\) (within \(0<q<1\)). Thus \(a_n\) decreases from its first term when \(q<1/2\); at \(q=1/2\) its first two terms tie and all subsequent terms decrease; at \(q>1/2\) it first strictly increases and eventually strictly decreases, with at most one adjacent equality. As \(a_n\to0\), the maximum \(M(q)\) is finite and attained. For \(q>1/2\), \(M(q)>a_1(q)\).

**Log-concavity and two local modes.** At \(q\le1/2\), the ratio \(C_1/C_0=x\) exceeds \(C_2/C_1=xa_1\), and subsequent adjacent ratios are nonincreasing. Hence \(C_n^2\ge C_{n-1}C_{n+1}\) for every \(n\ge1\), for all \(x>0\); this precludes two separated strict modes. Conversely, for \(q>1/2\), the strict inequality \(a_2>a_1\) gives \(C_2^2<C_1C_3\) at every positive \(x\), so log-concavity fails throughout that regime. At \(q>1/2\), choose \(x\) strictly between \(1/M(q)\) and \(1/a_1(q)\), avoiding equality with any reciprocal \(1/a_n(q)\). Then \(x>1\), \(C_1>C_0\), \(C_2<C_1\), at least one later ratio \(C_{n+1}/C_n>1\), and all sufficiently late ratios fall below one. Since the later ratio sequence is single-humped, there is exactly one later strict minimum and one later strict maximum, with no other local maxima; the later maximum is at index at least \(3\). Conversely, such a later strict peak requires some \(a_n>a_1\) and hence \(q>1/2\).

**Exact global-mode jump.** Write \(B_n=\prod_{j=1}^{n-1}(1-q^j)\). For each \(n\ge3\), the equality \(C_n=C_1\) is equivalent to \(x=(n!/B_n)^{1/(n-1)}\). The minimum over \(n\ge3\) exists because \(B_n\le1\) and \((n!)^{1/(n-1)}\to\infty\). At \(x=1/M(q)\), every later ratio is at most one and \(C_2<C_1\), so \(C_n<C_1\) for every \(n\ge2\). At \(x=1/a_1(q)\), one has \(C_2=C_1\) but \(C_3>C_2\), since \(a_2>a_1\). Each \(C_n/C_1\) strictly increases as a function of \(x\), and the family has a uniform vanishing tail on bounded \(x\)-intervals. Hence \(x_c\) lies strictly between these endpoints and is the exact unique transition where some \(n\ge3\) first matches and then surpasses \(C_1\). The inequality \(x_c<1/a_1\) ensures \(C_2<C_1\) at the transition; \(x_c>1/M\ge3>1\) ensures \(C_0<C_1\). Therefore the initial global maximizer after \(x=1\) jumps over index \(2\).

## Verification
The included standalone `proof_check.py` uses standard-library exact rational arithmetic, checks the finite adjacent-ratio lemma and finite-window log-concavity across rational parameters, and exhibits a strict two-mode example. Running `python proof_check.py` produces `exact_rational_checks_passed= 21199`. At \(q=3/4\), \(x=15/2\), the finite contribution sequence has strict modes at indices \(1\) and \(5\), and its global mode is \(5\). These finite checks are not proofs of the quantifiers over all real parameters or all indices; those follow from the displayed identities and asymptotic bounds.

## Relationship to prior work
Wang and Zhang (2026, arXiv:2611.18675) established the exact finite-threshold MFPT series and its adjacent-term ratio, and analyzed large-threshold saddle displacement and Poisson-smoothing accuracy. The present classification *uses and credits* that formula; it isolates an additional sharp **finite-threshold shape transition**, including two local modes and a nonadjacent global-mode jump for deterministic arrivals. Brémont (2025/2026, arXiv:2510.21670) studies high-threshold product asymptotics and renewal shot-noise FPT scaling, not this auxiliary-summand modal phase diagram. The auxiliary weights must not be confused with the physical hitting-index distribution.

## Limitations
The result is specialized to exactly periodic interarrivals, exponential marks and exponential relaxation. It does not assert that first-passage times, sample paths, or physical crossing-index probabilities are bimodal. Values at isolated reciprocal-ratio ties can create flat adjacent modes, which the stated strict two-mode interval excludes. The global transition formula is exact but generally requires minimization over integers; no elementary closed formula for the competing index is asserted. Historical papers on the same coefficient sequence could affect originality; independent assessment remains outstanding.

## References
Wang, Y., and Zhang, J. (2026), *Exact mean first-passage time and a Poisson-smoothing crossover in renewal shot noise*, arXiv:2611.18675v1, https://arxiv.org/html/2611.18675v1 (first public posting reported by arXiv: 2026-10-29).

Brémont, J. (2025; revised 2026), *Beyond Poisson: First-Passage Asymptotics of Renewal Shot Noise*, arXiv:2510.21670, https://arxiv.org/abs/2510.21670.
