# Exact composition-deletion sphere laws and three alphabet regimes

## Finding

Let \(q\ge2\), \(n\ge1\), and \(X\) be uniformly random in \(\{0,\ldots,q-1\}^n\). For each \(j=1,\ldots,n\), record the \(q\)-component symbol-count vectors of the length-\(j\) prefix and suffix. Their multiset \(\mathcal M(X)\) has exactly \(2n\) observations, with multiplicities retained. Let \(B_n\) be the number of **different multisets** remaining after deleting exactly one occurrence from \(\mathcal M(X)\), and put \(D_n=2n-B_n\).

Introduce independent uniform symbols \(A_i,B_i\in\{0,\ldots,q-1\}\), the walk \(S_0=0\), \(S_j=\sum_{i=1}^j(e_{A_i}-e_{B_i})\), and the number of positive-time returns \(Z_m=\sum_{j=1}^m\mathbf1\{S_j=0\}\), where \(Z_0=0\). Writing \(I_m=\mathbf1\{S_m=0\}\), the **exact distributional identities** are

\[
D_{2m+1}\overset{d}=1+2Z_m\quad(m\ge0),\qquad
D_{2m}\overset{d}=1+2Z_{m-1}+I_m\quad(m\ge1).
\]

Define the return probabilities and their generating function by

\[
u_{q,j}=q^{-2j}\sum_{a_1+\cdots+a_q=j}\binom{j}{a_1,\ldots,a_q}^{\!2},\quad
U_q(z)=\sum_{j\ge0}u_{q,j}z^j,\quad F_q(z)=1-\frac1{U_q(z)}.
\]

Set \(M_q(z,t)=[(1-z)(t+(1-t)U_q(z))]^{-1}\). Then the **complete finite-length probability generating functions** are

\[
\sum_{m\ge0}\mathbb E[t^{D_{2m+1}}]z^m=tM_q(z,t^2),
\]
\[
\sum_{m\ge1}\mathbb E[t^{D_{2m}}]z^m
=t\left[zM_q(z,t^2)+(t-1)\frac{F_q(z)}{1-t^2F_q(z)}\right].
\]

For fixed alphabet size, these have three different scaling regimes. If \(N\sim\mathcal N(0,1)\) and \(E\sim\mathrm{Exp}(1)\), then

\[
\frac{D_n}{2\sqrt n}\Rightarrow |N|\quad(q=2),\qquad
\frac{D_n}{(3\sqrt3/(2\pi))\log n}\Rightarrow E\quad(q=3).
\]

For each fixed \(q\ge4\), \(D_n\Rightarrow1+2G_q\), where \(G_q\) is geometric on \(\{0,1,\ldots\}\) with

\[
\Pr(G_q=r)=p_q(1-p_q)^r,\qquad
p_q=\frac1{U_q(1)}\in(0,1).
\]

## Assumptions and scope

This is the **single missing observation** channel, not deletion of a symbol from the source word. Exactly one composition occurrence is removed, even if the multiset contains several identical occurrences. Different deleted types yield different remaining multisets, whereas removing different copies of one type yields the same result. A composition at length \(j\) cannot equal a composition at length \(k\ne j\) because their coordinate sums differ. The source symbols are independent and uniform; \(q\) is a fixed integer at least two, not necessarily a prime power. All generating-function equalities are in formal power series, so no analytic convergence assumptions are required for them.

## Proof

**1. Reduction to symmetric-prefix matches.** Write \(P_j\) and \(Q_j\) for the compositions of the length-\(j\) prefix and suffix. Each length contributes one distinct type when \(P_j=Q_j\), and two otherwise. Consequently

\[
B_n=2n-\sum_{j=1}^n\mathbf1\{P_j=Q_j\}.
\]

Removing the common intersection of the prefix and suffix shows \(P_j=Q_j\) if and only if \(P_{n-j}=Q_{n-j}\). The length-\(n\) equality always holds. For \(1\le j\le\lfloor n/2\rfloor\), the comparison concerns disjoint groups of \(j\) symbols, one at each end. As \(j\) grows, the paired symbols from the two ends form independent pairs \((A_i,B_i)\), giving the walk \(S_j\). For odd \(n=2m+1\), every match in the first half is mirrored, and for even \(n=2m\) the central comparison is unpaired; these yield the stated two identities. The identities hold jointly in the nested return indicators, not just in each marginal.

**2. Return generating function.** Since the two samples of \(j\) symbols are independent and uniform, equality of their composition vectors has probability

\[
\Pr(S_j=0)=q^{-2j}\sum_{a_1+\cdots+a_q=j}\left(\frac{j!}{a_1!\cdots a_q!}\right)^2=u_{q,j}.
\]

Let \(T\) be the first positive return time, possibly infinite, and \(f_j=\Pr(T=j)\). Standard first-return decomposition, proved by conditioning on the first return, gives \(U_q(z)=1+F_q(z)U_q(z)\), or \(F_q(z)=1-U_q(z)^{-1}\). The chance of having no positive return through time \(m\) has generating function \(H_q(z)=(1-F_q(z))/(1-z)\). The event of exactly \(r\) positive returns by time \(m\) has bivariate generating function \(F_q(z)^r H_q(z)\); hence

\[
\sum_{m\ge0}\mathbb E[t^{Z_m}]z^m=
\frac{H_q(z)}{1-tF_q(z)}
=\frac1{(1-z)[t+(1-t)U_q(z)]}=M_q(z,t).
\]

For the even identity observe, for every \(m\ge1\), that \(\mathbf1\{S_m=0\}=1\) with \(Z_{m-1}=r\) exactly when the \((r+1)\)-st positive return occurs at time \(m\). Its generating function is \(F_q(z)^{r+1}\). Thus

\[
\sum_{m\ge1}\mathbb E[t^{2Z_{m-1}+I_m}]z^m
=zM_q(z,t^2)+(t-1)\frac{F_q(z)}{1-t^2F_q(z)}.
\]

Multiplying by \(t\) in each parity proves the two complete finite-length laws. Differentiating them, or taking expectations in the return identities, gives the explicit finite-length means

\[
\mathbb E B_{2m+1}=4m+1-2\sum_{j=1}^m u_{q,j},\quad
\mathbb E B_{2m}=4m-1-2\sum_{j=1}^{m-1}u_{q,j}-u_{q,m}.
\]

**3. Asymptotic return probabilities.** Project \(S_j\) to its first \(q-1\) coordinates; the omitted coordinate is minus their sum. The projected increment is aperiodic (zero steps have positive probability), spans the full integer lattice, and has covariance matrix

\[
\Sigma=2(q^{-1}I_{q-1}-q^{-2}\mathbf1\mathbf1^{\mathsf T}),\qquad
\det\Sigma=\frac{2^{q-1}}{q^q}.
\]

The classical lattice local central limit theorem therefore gives

\[
u_{q,j}\sim c_q j^{-(q-1)/2},\qquad
c_q=\frac{q^{q/2}}{(4\pi)^{(q-1)/2}}.
\]

This follows as well by multinomial Stirling expansion. For \(q=2\), Vandermonde's identity supplies the exact expression \(u_{2,j}=\binom{2j}{j}4^{-j}\) and \(U_2(z)=(1-z)^{-1/2}\). For \(q=3\), \(u_{3,j}\sim(3\sqrt3/(4\pi))j^{-1}\). For \(q\ge4\), the return probabilities are summable, and \(U_q(1)<\infty\).

**4. Limiting return-count laws and constants.** Differentiate \(M_q(z,t)\) at \(t=1\); for every integer \(k\ge1\),

\[
\sum_{m\ge0}\mathbb E[(Z_m)_k]z^m
=\frac{k!\,[U_q(z)-1]^k}{1-z},
\]

where \((z)_k=z(z-1)\cdots(z-k+1)\) is the falling factorial. When \(q=2\), the exact square-root singularity and standard coefficient asymptotics give

\[
\mathbb E[(Z_m)_k]\sim\frac{k!}{\Gamma(1+k/2)}m^{k/2}.
\]

These are precisely the moments of \(\sqrt2|N|\), and this half-normal law is moment-determinate. Thus \(Z_m/\sqrt m\Rightarrow\sqrt2|N|\). For \(q=3\), let \(c_3=3\sqrt3/(4\pi)\). Expanding \([U_3(z)-1]^k\) as a convolution of return probabilities gives, by bounding the simplex \(j_1+\cdots+j_k\le m\) between the boxes \(j_i\le m/k\) and \(j_i\le m\),

\[
\mathbb E[(Z_m)_k]\sim k!(c_3\log m)^k.
\]

The limiting moments are those of a mean-one exponential, which is moment-determinate; therefore \(Z_m/(c_3\log m)\Rightarrow E\). When \(q\ge4\), the walk is transient; the strong Markov property at successive returns makes the total number of positive returns \(G_q\) geometrically distributed, with stopping parameter \(1/U_q(1)\). Because \(Z_m\uparrow G_q\) almost surely and \(\Pr(I_m=1)=u_{q,m}\to0\), both parity formulas yield the stated tight limit. For \(q=2,3\), substitute \(m=\lfloor n/2\rfloor\) and \(D_n=1+2Z_m\), or its even version with a bounded extra indicator, to obtain the exact scaling constants displayed in the Finding.

## Verification

The accompanying `checker.py` uses only the Python standard library, enumerates all \(2^n\) words for \(q=2\) through \(n=14\), all \(3^n\) words for \(q=3\) through \(n=9\), and all \(4^n\) words for \(q=4\) through \(n=7\), totaling 84,133 source words. It independently constructs the deletion-sphere size from the composition types and obtains its complete rational distribution from the renewal equations, comparing exact distributions and means. It additionally tests normalization and nonnegativity through return depth 13 for \(2\le q\le7\). All checks passed. Finite calculations corroborate but cannot replace the infinite derivation and local central limit argument.

## Relationship to prior work

Chen, *Coding methods for string reconstruction from erroneous prefix-suffix compositions* (first publicly posted March 16, 2025), defines the composition multiset and single composition deletion and develops error-correcting constructions, focusing on binary coded sources rather than the uniform-source single-deletion sphere-size law. Ye and Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, supply related prefix/suffix symmetry in a deterministic reconstruction context, but the checked text does not give the walk-return distribution, parity-specific exact generating functions, or the alphabet phase transition. Gabrys, Pattabiraman, and Milenkovic, *Reconstruction of Sets of Strings from Prefix/Suffix Compositions*, analyze coding and missing measurements, again not this law. The exact source-law statement is not a claim of originality for local central limit theorems, renewal theory, or moment methods themselves. Other possibly unindexed work may subsume the result; literature priority is not independently certified.

## Limitations

The source is i.i.d. uniform, only one composition occurrence is deleted, and the full prefix/suffix spectrum is observed before deletion. Fixed \(q\) is essential for the asymptotic regimes; the result neither constructs optimal correction codes nor analyzes multiple missing measurements, noise in a composition vector, nonuniform source distributions, or simultaneous growth of \(q\) and \(n\). The finite checker does not establish the limiting laws independently.

## References

1. Zitan Chen, *Coding methods for string reconstruction from erroneous prefix-suffix compositions*, arXiv:2503.12342, first public version March 16, 2025. https://arxiv.org/abs/2503.12342
2. Zuo Ye and Ohad Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963. https://arxiv.org/abs/2208.14963
3. Ryan Gabrys, Srilakshmi Pattabiraman and Olgica Milenkovic, *Reconstruction of Sets of Strings from Prefix/Suffix Compositions*, arXiv:2110.02352. https://arxiv.org/abs/2110.02352
