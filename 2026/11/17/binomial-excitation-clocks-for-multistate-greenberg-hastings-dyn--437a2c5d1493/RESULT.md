# Binomial excitation clocks for multistate Greenberg–Hastings dynamics on transitive tournaments

## Finding
For every pair of integers \(n\ge1\), \(k\ge3\), the finite \(k\)-state Greenberg–Hastings process on the transitive directed tournament has an exact, closed first-extinction-time census. It is controlled by a triangular recoding that converts the nonlinear total number of active time steps into a Hamming-weight statistic.

For an initial configuration \(x\), let \(B(x)\) be the length of the uninterrupted sequence of rounds during which at least one site is excited (in state \(1\)); set \(B(x)=0\) when no site is initially excited. For each \(0\le b\le n\),
\[
\#\{x:B(x)=b\}=\binom nb(k-1)^{n-b}.
\]
Writing \(T(x)\) for the first time at which all sites have state \(0\), its generating polynomial is
\[
\boxed{\sum_x z^{T(x)}=\sum_{t=0}^{k-2}\bigl((t+1)^n-t^n\bigr)z^t+z^{k-2}\left((k-1+z)^n-(k-1)^n\right).}
\]
Here \(0^n=0\) because \(n\ge1\). Every state dies out. The exact worst-case time is \(n+k-2\), and only the single word \(x_i\equiv i-n+1\pmod k\) attains it. In particular its uniform probability is \(k^{-n}\).

Under independent uniform initial colors, the burst length has the exact \(\operatorname{Bin}(n,1/k)\) distribution, although it need not equal the number of initially excited sites for an individual word. For fixed \(k\),
\[
\frac{T-n/k-(k-2)}{\sqrt{n(k-1)/k^2}}\Longrightarrow\mathcal N(0,1),
\qquad \mathbb E[T]=\frac nk+k-2+O_k\!\left(\left(\frac{k-1}k\right)^n\right).
\]
The latter statement is asymptotic for fixed \(k\), not uniform in \(k\).

## Assumptions and scope
Vertices are indexed \(1,\ldots,n\); for every \(i<j\) there is a directed arc \(i\to j\). Each site's input consists **only of its outgoing neighbors**, so the vertex \(n\) has no incoming influence under this convention. The state alphabet is \(\mathbb Z/k\mathbb Z\), represented by \(0,1,\ldots,k-1\). At each integer time, all vertices update simultaneously. State \(0\) remains zero except when at least one out-neighbor is in state \(1\), when it becomes \(1\); all states \(1,\ldots,k-1\) increase by one modulo \(k\), independently of neighbors. The excitation threshold is exactly one and the graph includes no loops or reverse arcs. The natural absorbing state is the all-zero word.

## Proof
**1. Consecutive burst lemma.** If a state has no vertex in state \(1\), then the next state cannot have any vertex in state \(1\): no resting vertex is triggered and all already-positive vertices progress from a state other than \(1\). Therefore any nonempty global excitation trace consists of times \(0,1,\ldots,b-1\) for some finite \(b\). Finiteness here will follow from the suffix induction below.

**2. Suffix induction and triangular bijection.** Process the vertices backwards from the sink \(n\) to vertex \(1\). Suppose the suffix to the right of vertex \(i\) exhibits excitation for exactly the first \(b\) rounds. During each such round, an initially resting vertex \(i\) is triggered, while a positive vertex advances automatically; hence its first \(b\) updates are \(a\mapsto a+1\pmod k\), regardless of its initial state \(a=x_i\). At time \(b\), the vertex is in state \(a+b\pmod k\). Exactly one initial value, namely \(a\equiv1-b\pmod k\), makes it excited at that time. If that value is chosen, the enlarged suffix has excitation rounds \(0,\ldots,b\). Otherwise no site is excited at time \(b\), so all later rounds are also unexcited. This also covers \(b=0\): the only initially excited value is \(a=1\). Thus adding a new site increases the length by **one** for precisely one of the \(k\) initial colors, and leaves it unchanged for the other \(k-1\).

Equivalently, define \(b_{n+1}=0\), and for \(i=n,n-1,\ldots,1\), put
\[
d_i\equiv x_i+b_{i+1}\pmod k,\qquad b_i=b_{i+1}+\mathbf1_{\{d_i=1\}}.
\]
The preceding argument proves that \(b_i\) is the active-burst length of the suffix \(i,\ldots,n\). Given the digits \(d_n,d_{n-1},\ldots,d_1\), one can recover each \(b_{i+1}\) and then \(x_i\equiv d_i-b_{i+1}\pmod k\); hence \(x\mapsto d\) is a bijection of the full \(k^n\)-element state set. Moreover, \(B(x)=b_1=\#\{i:d_i=1\}\). Counting these digits gives the binomial population formula for \(B\), including \(b=0\).

**3. Actual extinction time.** When \(B=b\ge1\), the last excited vertex appears at time \(b-1\), passes successively through states \(2,3,\ldots,k-1\), and first becomes resting at time \(b+k-2\). No other site can remain nonzero after that time, because any site not already in the refractory chain at that last round had its last excitation even earlier, or was initially refractory and dies out by time \(k-2\). Consequently \(T=b+k-2\) whenever \(b\ge1\). If \(B=0\), all initial colors belong to \(\{0,2,\ldots,k-1\}\), no excitation ever occurs, and the extinction time is simply \(\max\bigl(\{k-x_i:x_i\ge2\}\cup\{0\}\bigr)\). For each \(0\le t\le k-2\), there are exactly \((t+1)^n\) such words with extinction time at most \(t\), namely those with every entry in \(\{0,k-t,\ldots,k-1\}\). Taking first differences gives \((t+1)^n-t^n\) words at time \(t\). Combining the disjoint \(B=0\) and \(B\ge1\) cases proves the displayed polynomial.

**4. Sharpness and probability.** The bijection makes \(B=n\) equivalent to \(d_i=1\) at every index. Recursing from \(i=n\) gives the unique initial word \(x_i\equiv i-n+1\pmod k\). Its first extinction time is \(n+k-2\), while every other word has a smaller burst or has none. Under uniform input, the \(d_i\) are independent uniform digits, so \(B\) has exact binomial distribution with success parameter \(1/k\). The only difference between \(T\) and \(B+k-2\) occurs when \(B=0\), an event of probability \(((k-1)/k)^n\). On that event their difference is bounded in magnitude by \(k-2\). The binomial central limit theorem and the bounded rare correction prove the displayed asymptotic statements.

## Verification
Two independent exhaustive implementations accompany this result. `verify_direct.cpp` evolves each labelled initial state directly using the complete directed adjacency convention, for \(k=3\) through \(n=10\), \(k=4\) through \(n=8\), and \(k=5\) through \(n=7\). It checks every first-extinction histogram against the coefficient formula. `verify_suffix.py` builds independent time traces for one new upstream vertex from the active time set of the downstream suffix, checking the burst polynomial for all \(3\le k\le7\) and \(1\le n\le7\). Both pass. All programs and their captured complete outputs are embedded alongside this document. The finite tests corroborate, but are not substituted for, the unrestricted induction proof.

For example, at \(k=3\), \(n=4\), the populations at extinction times \(0,1,2,3,4,5\) are respectively \(1,15,32,24,8,1\), summing to \(3^4=81\).

## Relationship to prior work
Fisch, Gravner, and Griffeath (1993) set out multi-color Greenberg–Hastings and cyclic-contact excitable models for spatial media. Gravner, Lyu, and Sivakoff (2016), especially its Introduction, Theorem 3 and the tournament expansion in Section 3, study excitation on **undirected** simple graphs, despite the name “tournament expansion” for their auxiliary maximum-ranking process. Their model, hypotheses and conclusions do not give this directed complete-feedforward extinction census. Related analyses of cyclic successor-contact dynamics on transitive tournaments address a distinct update law: in that rule only successor contact can advance *every* color, rather than automatically advancing positive refractory states. Neither that result nor exact excitation censuses on undirected graph families imply the present all-\(k\) binomial recoding, time distribution or unique extremizer.

## Limitations
The scope is restricted to complete acyclic orientations, threshold-one excitation, and homogeneous refractory length \(k-2\). For an arbitrary directed acyclic graph, the bijection's “one of \(k\) colors extends the burst” property need not hold. No claim of absolute historical priority is made: an equivalent result might appear in material not covered by the accessible literature. The 1993 foundational paper was available in abstract form but not as inspected full text; the 2016 relevant source was inspected in full HTML. The analysis is mathematical and computationally checked but has not undergone an independent external audit.

## References
1. R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, arXiv:patt-sol/9304001, first submitted 1993-04-02, https://arxiv.org/abs/patt-sol/9304001.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first submitted 2016-10-24, https://arxiv.org/html/1610.07320v1.
3. J. M. Greenberg and S. P. Hastings, *Spatial patterns for discrete models of diffusion in excitable media*, SIAM Journal on Applied Mathematics 34 (1978), 515–523. This original physical model provides historical context; the theorem here concerns a directed network specialization.
