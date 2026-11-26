# A repeated spectral bottleneck forces a linear-geometric tail in the card-merger shuffle

## Finding
Let \(n\) ordered cards be independently reshuffled uniformly at every round. In a random permutation, merge every maximal contiguous, increasing run of consecutive numerical labels; relabel the remaining blocks in order and repeat. Write \(X_n\) for the number of rounds until one block remains (\(X_1=0\)). For every **fixed** integer \(n\ge3\), as the integer observation horizon \(t\to\infty\),
\[
\Pr(X_n>t)=\bigl(c_n t+O_n(1)\bigr)2^{-t}.
\]
The leading constants are strictly positive and rational, determined by
\[
c_3=\frac23,\qquad c_n=\frac{2}{1-2p_{n,n}}\sum_{k=3}^{n-1}p_{n,k}c_k\quad(n\ge4),
\]
where \(p_{n,k}\) is the one-round transition probability from \(n\) to \(k\) blocks. Thus \(c_4=6\) and \(c_5=276/7\). For comparison,
\[
\Pr(X_2>t)=2^{-t},\qquad \Pr(X_3>t)=\frac{2t+3}{3\cdot2^t}\quad(t=0,1,2,\ldots).
\]
The extra linear factor is a genuine spectral multiplicity: the two smallest nonabsorbing block counts have identical holding probability \(1/2\), while all higher counts have smaller holding probabilities.

## Assumptions and scope
Every permutation at every stage is independently uniform. Runs must increase by exactly one at each adjacent step; decreasing numerical adjacency does not merge. The initial state \(n\) is a fixed finite integer while \(t\) tends to infinity. The estimate is not uniform in \(n\). Define integers \(a_0=a_1=1\) and \(a_j=ja_{j-1}+(j-1)a_{j-2}\) for integers \(j\ge2\). The established enumeration of block counts yields
\[
p_{n,k}=\frac{\binom{n-1}{k-1}a_{k-1}}{n!},\qquad1\le k\le n.
\]
All quantities above are exact finite rationals for each finite \(n\).

## Proof
**1. The unique leading double pole.** Set \(F_n(z)=\mathbb E[z^{X_n}]\); \(F_1(z)=1\). Conditioning on the number of blocks after the first shuffle, then using independent further shuffles, gives the *rational* generating-function identity
\[
F_n(z)=\frac{z\sum_{k=1}^{n-1}p_{n,k}F_k(z)}{1-zp_{n,n}}\quad(n\ge2).
\]
The two base states are exact:
\[
F_2(z)=\frac{z}{2-z},\qquad F_3(z)=\frac{z(z+2)}{3(2-z)^2}.
\]
Thus \(F_2\) has a simple pole at \(z=2\), whereas \(F_3\) has a double pole with coefficient
\[
\lim_{z\to2}(1-z/2)^2F_3(z)=2/3.
\]
In particular, this double pole is not a generic property of an ordinary geometric holding time: the transition from state 3 to 2 propagates a repeated eigenvalue through the transient chain.

**2. All larger states have smaller holding probability.** Let \(B_n(w)=\sum_{k=1}^{n}p_{n,k}w^{n-k}\), the generating polynomial of the number of mergers in one round. The published block enumeration gives
\[
B_n(w)=\sum_{j=0}^{n-1}\frac{n-j}{n}\frac{(w-1)^j}{j!}.
\]
Subtract consecutive polynomials:
\[
B_{n+1}(w)-B_n(w)=\frac{w-1}{n(n+1)}\sum_{j=0}^{n-1}\frac{(w-1)^j}{j!}.
\]
At \(w=0\), the left side is \(p_{n+1,n+1}-p_{n,n}\). The truncated alternating exponential equals the nonnegative derangement fraction
\[
\sum_{j=0}^{n-1}\frac{(-1)^j}{j!}=\frac{D_{n-1}}{(n-1)!},
\]
where \(D_m\) is the number of derangements of \(m\) labels. This number vanishes for \(m=1\) and is strictly positive for \(m\ge2\). Since \(p_{2,2}=p_{3,3}=1/2\), it follows that \(p_{n,n}<1/2\) for every \(n\ge4\).

**3. Leading coefficients propagate without cancellation.** Inductively every \(F_n\) has at most a double pole at \(z=2\); every other possible pole lies at a real point \(1/p_{k,k}>2\) for some \(4\le k\le n\). Multiplying the recurrence by \((1-z/2)^2\) and taking \(z\to2\) yields
\[
c_n=\frac{2}{1-2p_{n,n}}\sum_{k=3}^{n-1}p_{n,k}c_k.
\]
For all \(n\ge4\), \(p_{n,3}>0\); hence \(c_n>0\). The probability-generating function of the survival sequence \(S_n(t)=\Pr(X_n>t)\) is
\[
\sum_{t\ge0} S_n(t)z^t=\frac{1-F_n(z)}{1-z}.
\]
Since \(1/(1-z)\) evaluates to \(-1\) at \(z=2\), the double-pole coefficient for this survival generating function is likewise \(c_n\). Partial fractions give \(S_n(t)=(c_n(t+1)+O_n(1))2^{-t}\), equivalently the asserted \((c_nt+O_n(1))2^{-t}\). Any other poles lie strictly farther away; repeated poles away from two give exponentially smaller contributions. The explicit base-state distributions follow by expanding \(F_2\) and \(F_3\), yielding \(\Pr(X_3=t)=(2t-1)/(3\cdot2^t)\) for integer \(t\ge1\) and hence the survival identity. \(\square\)

## Verification
Run `python3 verify.py` (standard library only) beside this file. It performs exact rational transition-normalization checks for states through 20, exhaustive comparisons with every permutation through seven cards, checks the double holding maximum and positive rational constants, and independently recurses the entire integer-time probability table through eight starting cards. The checker reports 221 exact assertions passed. These bounded checks confirm numerical steps, but the all-\(n\), all-\(t\) conclusions rest on the generating-function proof above.

## Relationship to prior work
Rao, Zhang, Huang, and Cheng (2016) defined this random card-merging chain and derived the transition kernel and distributional recurrences. Chern, Jiu, and Simonelli (arXiv:2309.08841v1, submitted September 16, 2023) analyzed large-initial-state moments and a central limit theorem; their Section 2 contains the block-count generating polynomial used here. Neither their full inspected preprint nor the accessible abstract and cited description of the earlier work supplied the **fixed-state, long-horizon double-pole asymptotic** or its strict positive coefficient recurrence. The exact finite-time distribution in the earlier work is mathematically sufficient input from which one can derive this tail, so historical priority for any implicit equivalent analysis remains uncertain. This statement distinguishes the two asymptotic regimes (fixed state versus large initial state), and identifies the repeated leading transient eigenvalue rather than claiming a new transition kernel.

## Limitations
The result concerns independent uniform reshufflings and deterministic consecutive-increasing merging. It does not estimate \(c_n\) as \(n\to\infty\), establish a uniform-in-\(n\) error term, or address nonuniform shuffles. The 2016 full text was not accessible in the present source comparison; its exact distribution might contain an earlier equivalent tail conclusion. No independent external audit has been performed.

## References
- S. Chern, L. Jiu, and I. Simonelli, *A central limit theorem for a card shuffling problem*, arXiv:2309.08841v1 (first submitted 2023-09-16), https://arxiv.org/html/2309.08841v1, esp. Sections 1–2.
- M. B. Rao, H. Zhang, C. Huang, and F.-C. Cheng, *A discrete probability problem in card shuffling*, Communications in Statistics—Theory and Methods 45 (2016), 612–620, DOI:10.1080/03610926.2013.834451 (earlier model and distributional recurrence; full text unavailable for this comparison).
