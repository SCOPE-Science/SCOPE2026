# Sharp categorical block overlap and a uniform hitting bound for finite-memory sources

## Finding

Fix an alphabet of size \(q\ge3\), a context length \(d\ge1\), and a lower bound \(0<b<1/q\) on every one-symbol conditional probability. Put
\[
a=1-(q-1)b,\qquad \theta=2\sqrt{ab}+(q-2)b,
\qquad t=\tfrac12\log(a/b),\qquad u=\sqrt{ab}/\theta.
\]
For any order-\(d\) sliding-window Markov chain \(P\) on \([q]^d\) with every allowed conditional probability at least \(b\), define its length-\(d\) block overlap by
\[
c(P,d)=1-\delta(P^d)=\min_{x,y\in[q]^d}\sum_{w\in[q]^d}\min\{P^d(x,w),P^d(y,w)\}.
\]
The sharp universal lower bound is
\[
\boxed{c(P,d)\ge c_{q,d}(b):=
\sum_{k+\ell\le d}\frac{d!}{k!\ell!(d-k-\ell)!}(q-2)^{d-k-\ell}
 a^{\min(k,\ell)}b^{d-\min(k,\ell)}.}
\]
Equality is attained by a strictly positive finite-memory transition kernel. Thus this is an exact minimax block-overlap formula, not just a lower estimate. It has the random-walk representation
\[
\boxed{c_{q,d}(b)=\theta^d\,\mathbb E\exp(-t|S_d|),}
\]
where \(S_d\) is a sum of \(d\) independent increments that equal \(-1,0,1\) with probabilities \(u,1-2u,u\), respectively. For fixed \(q,b\),
\[
\boxed{c_{q,d}(b)\sim \frac{\coth(t/2)}{\sqrt{4\pi u\,d}}\,\theta^d\quad(d\to\infty).}
\]
In contrast with the binary parity plateaux, \(c_{q,d+1}(b)<c_{q,d}(b)\) for every \(d\ge0\), with \(c_{q,0}(b):=1\).

Let \(\pi\) be the stationary law and \(\tau_w=\inf\{n\ge0:X_n=w\}\). Every such chain also satisfies, for all start states \(z\) and target states \(w\),
\[
\boxed{\pi(w)\mathbb E_z\tau_w\le
B_{q,d}(b):=\frac{1-a^d}{1-a}+\frac{d(a^d-b^d)}{c_{q,d}(b)}.}
\]
In particular, these normalized hitting times are bounded by a constant depending only on \(q,b\), uniformly in \(d\), whenever
\[
\boxed{b>\frac{1}{2q-1+2\sqrt{q-1}},}
\]
equivalently \(a<\theta\). This last condition is sufficient for the true hitting-time bound; the assertion does **not** characterize the necessary condition for uniform hitting times. It is, however, the exact dividing condition for uniform boundedness in \(d\) of the displayed explicit bound \(B_{q,d}(b)\).

## Assumptions and scope

The states are length-\(d\) words over \([q]=\{1,\ldots,q\}\). From state \((x_1,\ldots,x_d)\), append a symbol \(j\in[q]\), drawn with probability \(p(j\mid x_1,\ldots,x_d)\), and discard the oldest symbol. Assume \(p(j\mid x)\ge b\) for every context and symbol. Consequently \(p(j\mid x)\le a\), and the finite chain is irreducible and aperiodic. Here \(\delta(K)=\max_{x,y}\tfrac12\sum_z|K(x,z)-K(y,z)|\), and \(\pi\) denotes the unique invariant probability distribution.

The minimax statement fixes \(q,d,b\) and varies all allowed context-dependent transition tables. The asymptotic statement fixes \(q,b\) and lets \(d\) grow; no estimate is claimed uniform as \(b\uparrow1/q\) or \(b\downarrow0\). The sum for \(c_{q,d}\) is a finite, exact expression for each positive integer \(d\).

## Proof

**1. Weighted extremal-overlap lemma.** Let \(A=(a,b,\ldots,b)\) and \(B=(b,a,b,\ldots,b)\), and define
\[
F_n(s,t)=\sum_{v\in[q]^n}\min\{s A^{\otimes n}(v),t B^{\otimes n}(v)\}\quad(s,t\ge0).
\]
We prove simultaneously for all integers \(n\ge0\) and all nonnegative \(s,t\) that the overlap of any two depth-\(n\) categorical stochastic trees, with each conditional probability at least \(b\), carrying initial masses \(s,t\), is at least \(F_n(s,t)\). At depth zero the overlap is \(\min(s,t)=F_0(s,t)\). Given first-symbol laws \(p,r\), applying the induction hypothesis under each first-symbol branch gives a bound
\[
\sum_{j=1}^q F_n(sp_j,tr_j).
\]
For fixed \(s,t\), this expression is jointly concave in \((p,r)\), since each summand is a sum of minima of two nonnegative linear expressions. A concave function on a product of compact polytopes has a minimizing vertex. The vertices of the simplex with all coordinates at least \(b\) are the \(q\) permutations of \((a,b,\ldots,b)\). If the vertices \(p,r\) peak on different symbols, permutation symmetry of product laws makes the displayed sum exactly \(F_{n+1}(s,t)\). If the peaks coincide, homogeneity gives \(\sum_jp_jF_n(s,t)=F_n(s,t)\), which is no smaller than \(F_{n+1}(s,t)\) by marginalization: \(\sum_j\min(x_j,y_j)\le\min(\sum_jx_j,\sum_jy_j)\). Hence every choice of conditional laws has overlap at least \(F_{n+1}(s,t)\). This proves the weighted claim, including unequal starting masses. Taking \(s=t=1\), \(n=d\) proves the block-overlap bound.

**2. Sharp realization.** In every context, use the conditional distribution \(A\) when the oldest symbol is \(1\), and \(B\) when it is \(2\); choose the uniform distribution for all other oldest symbols. Starting from \((1,\ldots,1)\) and \((2,\ldots,2)\), respectively, the first \(d\) newly appended symbols are independent with laws \(A\) and \(B\): during these \(d\) steps the oldest symbol remains one of the original symbols. Their resulting states are exactly those newly appended words, so their overlap is \(F_d(1,1)\). The bound is therefore attained. Each transition is strictly positive.

**3. Exact formula and aperiodic local limit.** For a word with \(k\) occurrences of symbol \(1\), \(\ell\) occurrences of symbol \(2\), and \(r=d-k-\ell\) other symbols, its two product probabilities are \(a^k b^{d-k}\) and \(a^\ell b^{d-\ell}\). Their minimum is \(a^{\min(k,\ell)}b^{d-\min(k,\ell)}\), proving the multinomial formula.

Let \(R\) be the normalized geometric-mean law, \(R(v)=\sqrt{A^{\otimes d}(v)B^{\otimes d}(v)}/\theta^d\). The one-step \(R\)-law assigns probability \(u\) to each distinguished symbol and \(b/\theta\) to each of the other \(q-2\) symbols, so under \(R\) the signed difference between the distinguished symbol counts is \(S_d\). Since \(\min(x,y)=\sqrt{xy}\exp[-\tfrac12|\log(x/y)|]\), the tilt formula follows. Here \(u>0\) and \(1-2u=(q-2)b/\theta>0\); this walk is span-one and aperiodic with variance \(2u\). Its lattice local central limit theorem yields \(\sqrt d\,\Pr(S_d=k)\to (4\pi u)^{-1/2}\) for every fixed integer \(k\), with a uniform bound on \(\sqrt d\Pr(S_d=k)\). Dominated convergence with \(e^{-t|k|}\) gives the asserted asymptotic, since \(\sum_{k\in\mathbb Z}e^{-t|k|}=\coth(t/2)\). Contractivity under projection makes \(c_{q,d+1}\le c_{q,d}\); the inequality is strict because a word consisting of a neutral third symbol has equal positive mass under the two product distributions, while its one-step extensions have distinct distributions.

**4. Hitting bound.** Fix a target word \(w\). Set \(\Omega_s(w)=\max_zP^s(z,w)-\min_zP^s(z,w)\). For \(0\le s<d\), the probability of reaching the prescribed final \(s\) symbols is at most \(a^s\), so \(\Omega_s(w)\le a^s\). At exactly \(d\) steps any prescribed new word has probability between \(b^d\) and \(a^d\); therefore for all \(0\le j<d\), \(\Omega_{d+j}(w)\le a^d-b^d\). Since applying \(P^d\) to a function contracts its oscillation by \(\delta(P^d)\le1-c_{q,d}\),
\[
\Omega_{kd+j}(w)\le(a^d-b^d)(1-c_{q,d})^{k-1}
\quad(k\ge1,\ 0\le j<d).
\]
The finite irreducible aperiodic chain has the deviation-matrix identity
\[
\pi(w)\mathbb E_z\tau_w
=\sum_{s\ge0}\bigl(P^s(w,w)-P^s(z,w)\bigr)
\le\sum_{s\ge0}\Omega_s(w).
\]
Summing the two displayed envelopes proves \(B_{q,d}\). Finally the local-limit formula implies the second summand has asymptotic order \(d^{3/2}(a/\theta)^d\), because \(b<a\). It is uniformly bounded in \(d\) exactly when \(a<\theta\), and diverges at equality or above. Writing \(r=\sqrt{a/b}>1\), the inequality \(a<2\sqrt{ab}+(q-2)b\) is \(r^2<2r+q-2\), equivalent to \(r<1+\sqrt{q-1}\); substitution of \(a=1-(q-1)b\) gives the claimed explicit threshold for \(b\).

## Verification

The accompanying standalone `check.py` uses only the Python standard library. Running `python check.py` checks exact rational multinomial identities; weighted overlap minimization against all pairs of extreme adaptive categorical laws in multiple small cases; rational block-kernel overlap inequalities for randomly chosen admissible transition tables; exact attainment by the oldest-symbol construction; strict monotonicity; and finite numerical comparisons to the tilted lazy-walk formula and the local-limit constant. All 12,277 diagnostic assertions passed in the recorded run. Computation is a finite consistency check only: the universal depth, all-admissible-kernel and large-depth assertions follow from the proof above, not from those tests.

## Relationship to prior work

Maciej Skórski, *Learning Finite-Memory Binary Sources*, arXiv:2610.40845v1, establishes the sharp **binary** overlap formula and extremal context rule (Theorems 3–4). Its Appendix B.2 treats arbitrary finite alphabets using a general block-overlap parameter and derives a weaker affinity-based sufficient criterion (Theorem 24 and Corollary 26). The hitting-time deviation formula and its head–tail method are already established there, and are used here rather than claimed as new. The distinctions established here are the exact minimax block overlap for every alphabet size at least three, its explicit aperiodic walk asymptotic and sharp constant, and the resulting stronger sufficient regime for the general-alphabet hitting bound.

Makur and Singh, *Doeblin Coefficients and Related Measures*, arXiv:2309.08475v2, develops general overlapping-mass and contraction principles. Those general principles do not themselves supply the categorical minimax product law or explicit threshold. A known stronger classification for finite-alphabet memory sources could supersede this statement; the historical-priority conclusion is provisional.

## Limitations

The threshold \(b>1/(2q-1+2\sqrt{q-1})\) is sufficient, not established to be necessary for actual uniform normalized hitting times. The bound \(B_{q,d}\) may be loose. The asymptotic constant is pointwise for fixed \(q,b\); it is not asserted uniform near the endpoints of the permitted parameter interval. The statement does not cover zero conditional probabilities, infinite alphabets, or variable-length memories. No independent validation is claimed.

## References

1. Maciej Skórski, *Learning Finite-Memory Binary Sources*, arXiv:2610.40845v1 (first public version 29 October 2026), https://arxiv.org/html/2610.40845v1, especially Sections 4.1–4.3 and Appendix B.2.
2. Anuran Makur and Japneet Singh, *Doeblin Coefficients and Related Measures*, arXiv:2309.08475v2, https://arxiv.org/html/2309.08475v2, especially Sections II-A and II-E.
