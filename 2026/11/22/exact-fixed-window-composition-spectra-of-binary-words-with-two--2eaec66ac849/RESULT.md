# Exact fixed-window composition spectra of binary words with two markers

## Finding

Let \(h\ge2\) and \(n\ge3h-1\) be integers. A source word is a binary word of length \(n\) with exactly two ones. The receiver sees the **unordered, multiplicity-preserving compositions** of all \(n-h+1\) consecutive length-\(h\) factors; a composition is its number of ones. For \(j\in\{0,1,2\}\), write \(N_j\) for the number of windows containing \(j\) ones. Define the equivalent two-coordinate profile
\[
T=N_1+2N_2,\qquad U=N_2,
\]
so that \(N_0=n-h+1-T+U\), \(N_1=T-2U\), and \(N_2=U\).

**Exact feasibility and capacity.** The attainable profiles are exactly
\[
\Omega_h=\left\{(t,u)\in\mathbb Z^2:2\le t\le2h,\quad0\le u\le\min\!\left(h-1,\left\lfloor\frac{t-1}{2}\right\rfloor\right)\right\}.
\]
In particular, the largest zero-error code with these readouts and the stated fixed composition has exactly
\[
\boxed{\left|\Omega_h\right|=h^2+h-1}
\]
codewords, independent of \(n\) once \(n\ge3h-1\). This saturation threshold is sharp: at \(n=3h-2\), precisely the profile \((2h,0)\) is absent, giving \(h^2+h-2\) profiles.

**Exact inverse fibers.** Let \(M_{n,h}(t,u)\) be the number of length-\(n\), weight-two source words producing \((t,u)\). For every \((t,u)\in\Omega_h\),
\[
\boxed{
M_{n,h}(t,u)=\begin{cases}
t-1, &2\le t\le h,\ u=0,\\
2n-3t+3,&h<t<2h,\ u=0,\\
2,&t<2h,\ u\ge1,\\
\binom{n-3h+3}{2},&t=2h,\ u=0,\\
n-3h+2+u,&t=2h,\ 1\le u\le h-1.
\end{cases}}
\]
All other profiles have zero preimages. At the saturation length, exactly two distinct profiles are singletons, namely \((2,0)\) and \((2h,0)\); for every \(n\ge3h\), the sole singleton profile is \((2,0)\), uniquely produced by the word with ones at both endpoints.

Consequently, if two source words are independently uniform among the \(\binom n2\) choices, their readouts agree with probability
\[
\frac{\sum_{(t,u)\in\Omega_h}M_{n,h}(t,u)^2}{\binom n2^2}
=1-\frac{12(h-1)}n+O_h(n^{-2})\qquad(n\to\infty).
\]
Thus, for fixed read width, almost all sufficiently long two-marker words lie in one large ambiguity fiber, despite the exact finite zero-error codebook above.

## Assumptions and scope

The words are linear, indexed, and not quotiented by reversal. The source weight is exactly two and is known to the receiver, as are \(h\) and \(n\). The readout includes every overlapping nonwrapping window of a **single exact length** \(h\); factor order and locations are discarded, but multiplicities are kept. There is no noise or missing read. The theorem is for \(h\ge2\), \(n\ge3h-1\), with the stated sharp boundary at \(n=3h-2\). The marker alphabet is binary, so the only possible window weights are zero, one, and two. A zero-error code selects no more than one source word from each readout fiber.

## Proof

**Window-incidence intervals.** Write the positions of the ones as \(1\le i<j\le n\). The starts of length-\(h\) windows containing the one at position \(i\) form the integer interval
\[
A_i=[\max\{1,i-h+1\},\min\{i,n-h+1\}]\cap\mathbb Z.
\]
When \(n\ge3h-2\), its size is \(c_i=\min\{i,h,n-i+1\}\). Each window counted in both \(A_i\) and \(A_j\) has two ones. Thus
\[
T=c_i+c_j,\qquad U=|A_i\cap A_j|.
\tag{1}
\]
In this length range, different positions have different incidence intervals. Because two positions cannot occur in all the same windows, their union has at least one element outside the intersection. Therefore \(T\ge2U+1\). Also, \(2\le T\le2h\) and \(U\le h-1\), since the markers are distinct. These prove the necessary inequalities of \(\Omega_h\).

**Realizing every feasible profile.** For \(u=0\) and \(2\le t\le2h\), choose \(a=\min\{h,t-1\}\), \(b=t-a\), and positions \(i=a\), \(j=n-b+1\). Both \(a,b\) lie in \(\{1,\ldots,h\}\); the marker windows are disjoint because \(j-i=n-t+1\ge h\) when \(n\ge3h-1\), giving \((T,U)=(t,0)\).

For \(u\ge1\), the feasibility condition implies \(2u+1\le t\le2h\) and \(u\le h-1\). If \(t\le h+u\), choose \(i=u\), \(j=t-u\); both positions lie in the first \(h\) places and their incidence intervals overlap in exactly \(u\) starts. If \(t\ge h+u\), choose \(i=t-h\), \(j=t-u\). Here \(c_i=t-h\), \(c_j=h\), and \(A_i\cap A_j\) has \(u\) elements. All positions lie inside \(\{1,\ldots,n\}\), since \(j\le2h-1\le n-h+1\). Equation (1) gives the desired profile. Thus \(\Omega_h\) is exact. Summing its admissible \(u\)-counts over \(t\) yields
\[
\sum_{k=1}^{h}k+\sum_{k=1}^{h-1}(k+1)=h^2+h-1.
\]

**Fiber counts with a positive intersection.** If \(t<2h\), some marker is within \(h-1\) places of an endpoint. When \(u\ge1\), both markers lie in the same endpoint neighborhood: they cannot lie near opposite endpoints, because the corresponding window-start intervals would be disjoint. In the left neighborhood, either both markers are in the first \(h\) positions, forcing \(i=u\), \(j=t-u\), or the later marker lies in the central zone, forcing \(i=t-h\), \(j=t-u\). The two formulas agree at their common boundary, and exactly one gives a permitted pair for each admissible \((t,u)\). Reflection supplies precisely one more pair. Therefore \(M_{n,h}(t,u)=2\) for \(t<2h\), \(u\ge1\).

**Disjoint window intervals below the full-incidence layer.** If \(u=0\) and \(2\le t\le h\), each marker must lie near a different endpoint; their incidence sizes \(a,b\ge1\) satisfy \(a+b=t\), providing exactly \(t-1\) ordered choices. If \(u=0\) and \(h<t<2h\), opposite-end boundary placements contribute \(2h-1-t\) pairs. The remaining possibilities have one marker in a boundary band and one in the central band where \(c_i=h\). There are \(n-h-t+2\) choices for each of the two endpoint orientations, because the marker distance must be at least \(h\). Summing yields \((2h-1-t)+2(n-h-t+2)=2n-3t+3\).

**Full-incidence layer.** For \(t=2h\), both markers lie in the central interval \(\{h,\ldots,n-h+1\}\), which has \(N=n-2h+2\) positions. Their distance \(d=j-i\) gives \(u=(h-d)_+\). For each \(1\le u\le h-1\), the distance is \(d=h-u\), so exactly \(N-d=n-3h+2+u\) pairs are possible. For \(u=0\), the distance must be at least \(h\); summing across distances gives \(\binom{N-h+1}{2}=\binom{n-3h+3}{2}\). This completes the complete inverse-fiber formula. The formulas add to \(\binom n2\), as expected from partitioning the words by their profiles.

**Sharp boundary and singleton classes.** A profile with \((t,u)=(2h,0)\) needs two markers of full incidence, at least \(h\) apart. The shortest possible word has first marker at position \(h\), second at \(2h\), and length \(3h-1\). At length \(3h-2\), all other profiles are realized by the same constructions above: when \(u=0\), \(t\le2h-1\) gives separation at least \(h\), and when \(u>0\), the displayed left-neighborhood constructions still fit inside the \(2h-1\) possible window starts. Thus the stated threshold is exact. Reading off the fiber formulas shows that \((2,0)\) is always singleton, the full-incidence disjoint case is singleton only at \(n=3h-1\), and every other feasible fiber has at least two words for \(n\ge3h-1\).

**Collision asymptotics.** The fiber \((2h,0)\) has \(\binom{n-3h+3}{2}=\binom n2[1-6(h-1)/n+O_h(n^{-2})]\) words. Every other fiber has \(O_h(n)\) words and there are \(h^2+h-2\) such fibers, so their total contribution to the normalized sum of squared fiber sizes is \(O_h(n^{-2})\). Squaring the dominant fiber proportion proves the displayed collision expansion.

## Verification

The self-contained standard-library script `verify_fixed_window.py` was run from its actual package directory. It constructs every weight-two source by its marker positions, counts its window compositions by independent marker-incidence intervals, and compares every fiber with the exact piecewise formula. It passed 696 complete parameter cases, including \(2\le h\le30\), \(3h-1\le n\le3h+20\), and each sharp boundary \(n=3h-2\). It separately compared 26,850 direct literal window enumerations with the incidence formula at smaller lengths. It checked that the predicted fiber sizes sum to \(\binom n2\). Run `python3 verify_fixed_window.py` alongside this file. Finite tests corroborate but do not replace the all-parameter counting proof.

## Relationship to prior work

Ye and Elishco's 2022 paper formalizes length-limited composition reconstruction and in Section VIII constructs coding families; it also observes that a fixed-read-length submultiset may suffice to reconstruct its codewords. It does not give the exact weight-two fixed-window feasibility region, sharp saturation, all inverse-fiber multiplicities, or collision asymptotic established here.

A published all-length-through-\(r\) result for two-marker words gives \(r(3r-1)/2\) distinguishable profiles at its saturation threshold, and a finer fiber signature based on observing **every** length up to \(r\). That strictly more informative experiment is different from observing only the single window length \(h\). In particular, its exact profile count exceeds the present single-length capacity by \((h-1)(h-2)/2\), and its wordwise generating identities are compatible with specializing to the present length. The genuinely new conclusions claimed here are the closed fixed-layer profile region, each enlarged fixed-layer ambiguity fiber, and their information-theoretic collision behavior, not the general incidence-generating machinery. Published length-three composition results either treat arbitrary source weights or combine lengths two and three; they do not state this all-\(h\) fixed-weight-two fiber law.

## Limitations

The finite capacity is restricted to error-free exact-length composition reads from words with two ones; it does not describe arbitrary Hamming weight, literal factor readouts, multiple fragment lengths, circular strings, noisy channels, or positive-distance error correction. The collision expansion assumes \(h\) fixed as \(n\to\infty\); no uniform two-parameter asymptotic is claimed. The general all-length-through-\(r\) literature provides nearby stronger observational information, and another author may have made the fixed-layer specialization already; exhaustive historical priority cannot be guaranteed. Independent mathematical validation has not been performed.

## References

1. Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963, first public 2022-08-31, especially Section VIII, https://arxiv.org/abs/2208.14963.
2. U. Gupta and H. Mahdavifar, *A New Algebraic Approach for String Reconstruction from Substring Compositions*, arXiv:2201.09955, first public 2022-01-24, full-composition setting, https://arxiv.org/abs/2201.09955.
3. *A sharp \(3r-1\) saturation law for two-marker length-limited composition decks*, public research note with complete length-limited fiber signatures, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-3r-1-saturation-law-for-two-marker-length-limited-compos--a872b80fc72c.
4. *Interval-support characterization for binary three-window composition multispectra and the sharp four-window obstruction*, public research note, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-interval-support-characterization-for-binary-three-window-compos--2d009d6ce2ea.
