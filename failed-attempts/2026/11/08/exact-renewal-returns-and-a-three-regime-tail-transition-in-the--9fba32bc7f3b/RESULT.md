# Exact renewal returns and a three-regime tail transition in the Pelikan random map

## Finding
Consider independent iterations of the interval map \(X\mapsto 2X\bmod 1\) with probability \(p\), and \(X\mapsto X/2\) with probability \(q=1-p\). Start \(X_0\) uniformly on the top dyadic shell \(I_0=[1/2,1)\), independently of all branch choices. Write \(\tau\) for the first positive return to \(I_0\), or \(\infty\) if no such return occurs. Put
\[
f(z)=\frac{1-\sqrt{1-4pqz^2}}{2qz},\qquad
G(z)=\mathbb E[z^\tau;\tau<\infty]=z\left(qf(z)+\frac{p}{2-f(z)}\right),
\]
where the branch is analytic at zero and \(f(z)=z\) when \(q=0\). The successive finite return-time increments form an **independent, identically distributed (possibly defective) renewal sequence**, with this generating function. On every finite return, the entrance coordinate is uniform on \(I_0\) and independent of the just-completed return time *and all previous return-time increments* (although successive entrance coordinates need not be independent).

For \(p\in(0,1)\), put \(R=(2\sqrt{pq})^{-1}\) and \(s=\sqrt{p/q}\), and write \(a_n=\Pr(\tau=n)\). There is a sharp *secondary return-tail transition* at \(p=4/5\):

* If \(0<p<4/5\), then for each parity of \(n\),
\[
a_n\sim\frac{Rs}{\sqrt{2\pi}}R^{-n}n^{-3/2}\left[A_p+(-1)^nB_p\right],\quad
A_p=q+\frac{p}{(2-s)^2},\quad B_p=q+\frac{p}{(2+s)^2}.
\]
Both parity constants are strictly positive.
* If \(p=4/5\), then \(a_n\sim [2\sqrt{2\pi}]^{-1}(4/5)^n n^{-1/2}\).
* If \(4/5<p<1\), then \(a_n\sim C_p\rho_p^n\), with
\[
\rho_p=\frac{p+4q}{2},\qquad C_p=\frac{p(p-4q)}{(p+4q)^2}>0.
\]
For \(p=1\), the exact formula is \(a_n=2^{-n}\). At \(p=0\), no return is possible.

The *first* critical transition occurs at \(p=1/2\). For \(0<p<1/2\),
\[\Pr(\tau<\infty)=\frac{p(3-4p)}{2-3p}<1.\]
For \(p\ge1/2\), return is almost sure. When \(p>1/2\), \(\mathbb E\tau=2p/(2p-1)\); at \(p=1/2\),
\[\Pr(\tau>n)\sim\sqrt{\frac2\pi}\,n^{-1/2},\qquad\mathbb E\tau=\infty.\]

## Assumptions and scope
All probability statements average independently sampled map choices and the initial uniform position on \(I_0\); return-time independence need not hold for a deterministic initial position. Dyadic endpoints form a null set and do not affect these statements. For \(p<1/2\), returns may terminate; the independent renewal increments are then defective, with \(\infty\) an absorbing terminal increment. The asserted exponential/branch-point asymptotics concern fixed \(p\), not uniform moving-parameter limits. The position-independence assertion concerns return times, not independence among all entrance coordinates.

## Proof
**1. Dyadic descent and first-hitting transform.** Put \(I_k=[2^{-k-1},2^{-k})\) for \(k\ge0\). On \(I_k\) with \(k\ge1\), doubling maps into \(I_{k-1}\) and halving into \(I_{k+1}\). Thus the index evolves as a nearest-neighbor walk with downward probability \(p\) until it first reaches zero. If \(\sigma_k\) is its hitting time from \(k\ge1\), the ballot/reflection principle gives
\[
\Pr(\sigma_k=n)=\frac{k}{n}\binom n{(n+k)/2}p^{(n+k)/2}q^{(n-k)/2}
\]
for \(n\ge k\) and matching parity, and zero otherwise. Set \(f(z)=\mathbb E[z^{\sigma_1};\sigma_1<\infty]\). The first-step decomposition gives \(f=z(p+qf^2)\), selecting the root analytic at zero. By the skip-free property, \(\mathbb E[z^{\sigma_k};\sigma_k<\infty]=f(z)^k\).

**2. Return generating function.** From a uniform point on \(I_0\), halving (probability \(q\)) lands in \(I_1\). Doubling (probability \(p\)) maps the uniform starting point to a uniform point on \([0,1)\): with probability \(1/2\), it returns directly to \(I_0\), and otherwise the new shell index is \(k\ge1\) with unconditional probability \(2^{-k-1}\). Hence
\[
G(z)=z\left[qf(z)+\frac p2+p\sum_{k\ge1}2^{-k-1}f(z)^k\right]
=z\left[qf(z)+\frac p{2-f(z)}\right].
\]
For \(0<p<1/2\), \(f(1)=p/q\); for \(p\ge1/2\), \(f(1)=1\). This proves the return-probability trichotomy. Differentiating \(f=z(p+qf^2)\) at \(z=1\) when \(p>1/2\) gives \(f'(1)=(2p-1)^{-1}\), hence \(G'(1)=1+(2p-1)^{-1}=2p/(2p-1)\).

**3. Independence of landing position and duration.** For a uniform initial position in any fixed \(I_k\), the random walk path determines the hitting time but does not depend on the point's position within that cell; the landing coordinate equals \(2^kX_0\), which is uniform on \(I_0\). For a doubling step from uniform \(I_0\), conditional on the resulting depth \(k\ge0\), the resulting point is uniform in \(I_k\), so its eventual landing is uniform on \(I_0\) for every successful itinerary and independent of the duration. The same holds for a halving step, whose eventual landing coordinate equals \(X_0\). Therefore for each finite integer \(n\) and Borel \(B\subset I_0\),
\[
\Pr(\tau=n,\ X_\tau\in B)=a_n\,2\operatorname{Leb}(B).
\]
At any completed return, the strong Markov property for fresh independent branch choices applies. Because the returned coordinate is uniform and independent of all past return durations, repeating the joint-kernel identity shows inductively that successive inter-return times are identically distributed and independent up to a possible final infinite increment. The returned coordinate need not be independent of the preceding entrance coordinate: for example, a contraction-first excursion returns to the same point.

**4. Singularity and tail laws.** For \(0<p<1\) the first-hitting generating function is analytic at zero and has square-root branch points at \(\pm R\), where \(R=(2\sqrt{pq})^{-1}\). At \(z=R\), \(f(R)=s=\sqrt{p/q}\). If \(p<4/5\), then \(s<2\) and the denominator \(2-f\) cannot vanish for \(|z|<R\): nonnegative coefficients give \(|f(z)|\le f(|z|)\le s\). Writing \(\delta=1-z/R\), one has \(f(z)=s-s\sqrt{2\delta}+O(\delta)\), so the square-root coefficient of \(G\) at \(R\) is \(-Rs\sqrt2 A_p\). Similarly at \(-R\), \(f=-s+s\sqrt{2(1+z/R)}+O(1+z/R)\), and the square-root coefficient is \(-Rs\sqrt2 B_p\). The standard binomial coefficient asymptotic \([z^n]\sqrt{1-z/R}\sim-R^{-n}/(2\sqrt\pi n^{3/2})\), together with its \(-R\) counterpart, gives the displayed parity-resolved law. There are no other singularities on the circle because the radical has only these two branch points and \(2-f\) is nonzero there for \(p<4/5\).

At \(p=4/5\), \(s=2\), and the simple pole in the outer rational function merges with the positive branch point:
\[
G(z)\sim \frac{Rp}{2\sqrt2}(1-z/R)^{-1/2},\qquad R=5/4.
\]
The negative branch point contributes only order \(R^{-n}n^{-3/2}\), giving the stated critical coefficient. If \(p>4/5\), the unique positive solution \(f(z_0)=2\) lies strictly below \(R\), with \(z_0=2/(p+4q)\). It is a simple pole of \(G\), with residue coefficient \(C_p=p(p-4q)/(p+4q)^2\) in the expansion \(C_p/(1-z/z_0)\); all other singularities have larger modulus. This gives \(a_n\sim C_p z_0^{-n}\). The endpoint \(p=1\) follows directly from \(G(z)=z/(2-z)\).

Finally, at \(p=1/2\), \(f(z)=1-\sqrt{2(1-z)}+O(1-z)\) as \(z\uparrow1\), and \(G(z)=1-\sqrt{2(1-z)}+O(1-z)\). Therefore the generating function \((1-G(z))/(1-z)=\sum_{n\ge0}\Pr(\tau>n)z^n\) has leading term \(\sqrt2(1-z)^{-1/2}\). The coefficient/Tauberian theorem for a monotone survival tail gives \(\Pr(\tau>n)\sim\sqrt{2/\pi}\,n^{-1/2}\), implying infinite mean.

## Verification
The standalone `check.py` uses exact rational arithmetic to compare the return-time coefficients from \(G\) with the independently computed ballot-weighted sum over all starting shell depths, for seven rational probabilities and the first 22 durations. It also checks the exact algebraic collision threshold and pole location. These finite checks only corroborate the algebra; the all-parameter and asymptotic statements follow from the proof.

## Relationship to prior work
Yan, Majumdar, Ruffo, Sato, Beck and Klages analyze the same random expanding/contracting map and identify the main critical point \(p=1/2\) through its invariant density, Lyapunov exponent and correlations. The dyadic countable-state Markov representation and return/recurrence classification are standard and are also treated in Brevitt and Klages' later work on an *open* Pelikan variant. The new quantitative target here is the **original closed map's exact first-return renewal kernel, its position-time factorization, and the sharp pole/branch-point return-tail transition at \(p=4/5\)**. The latter threshold coincides numerically with a convexity change of the invariant density reported in the 2024 study, but it is proved independently here for return-time singularities. Standard ballot theory and singularity-analysis coefficient formulas are used, not claimed as new.

## Limitations
Return times are annealed and use an initially uniform top shell. The spatial return locations are not asserted to be an iid sequence, and the theorem does not calculate the stationary two-point correlation function. For \(p<1/2\), defective returns make stationary renewal-time conclusions inapplicable without conditioning. Published formulas for more general random map families may admit specializations not exhaustively indexed here; independent literature validation remains outstanding.

## References
1. J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck, R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269 (first public August 18, 2023), *Chaos* **34**, 023128 (2024), DOI: 10.1063/5.0176310. Author-accessible full text: https://webspace.maths.qmul.ac.uk/r.klages/papers/rds_chaos.pdf.
2. S. Brevitt, R. Klages, *Quasi-stationary and quasi-ergodic distributions in the Pelikan random map*, arXiv:2607.19084 (2026). Open-variant state-chain analysis; distinct from the closed-map return-time asymptotics proved here.
3. P. Flajolet, R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), for standard square-root and pole coefficient transfer.
