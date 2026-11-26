# Parity-sampled Motzkin extremizers in even capacity-two Burgers traffic

## Finding

On a labelled cyclic ring of even length \(n\ge4\), let \(x_i\in\{0,1,2\}\) and update synchronously by
\[
 F(x)_i=x_i+\min(x_{i-1},2-x_i)-\min(x_i,2-x_{i+1}).
\]
Write \(N=\sum_i x_i\) for the conserved occupancy and \(\tau(x)\) for the first time the orbit enters its eventual temporal cycle, with \(\tau=0\) for periodic initial states. The sharp universal upper bound on \(\tau\) is \(n/2-1\). At **each** mass \(N=n-1\) and \(N=n+1\), the number of initial configurations attaining this bound is
\[
 E_{n,n-1}=E_{n,n+1}=2nM_{n-3},\qquad
 M_j=\sum_{r=0}^{\lfloor j/2\rfloor}\binom{j}{2r}\frac1{r+1}\binom{2r}{r}.
\]
The first counts per sector, for \(n=4,6,8,10,12\), are \(8,48,336,2540,20040\). With independent uniform initial symbols, conditional on either one of the two masses, the probability of attaining \(n/2-1\) tends to \(2/9\) along even \(n\). The combined unconditional contribution from these **two** mass sectors is asymptotic to \(2\sqrt3/(9\sqrt{\pi n})\).

## Scope and symmetry

Sites are labelled, not factored by any spatial symmetry. Indices are cyclic; the capacity, update, and even-length restriction are as stated. The extremizer population at \(N=n\) is not classified. The entry-time-preserving symmetry between the two sectors is **reflection composed with complement**, \((Ax)_i=2-x_{-i}\). For \(J_i(x)=\min(x_i,2-x_{i+1})\), one has \(J_i(Ax)=J_{-i-1}(x)\), so \(FA=AF\). This bijection exchanges \(N\) and \(2n-N\) and preserves temporal recurrence and \(\tau\). Complement alone is not an entry-time-preserving symmetry in general.

## Proof

**Height and universal bound.** Choose an integral height lift with \(h_i-h_{i-1}=x_i-1\), and let \(d=N-n\), so \(h_{i+n}=h_i+d\). Then \(J_i=1+h_i-\max(h_{i-1},h_{i+1})\), and the updated heights can be chosen as \(h_i(t+1)=\max(h_{i-1}(t),h_{i+1}(t))-1\). Consequently
\[
 W_i(t):=h_i(t)+t=\max_{0\le j\le t} h_{i-t+2j}(0).
\]
The inequalities \(W_{i+1}\le W_{i-1}\) for every \(i\) are equivalent to \(x_i+x_{i+1}\le2\) everywhere. In this language \(J_i=x_i\) and the update is a right shift. The reverse inequalities give \(x_i+x_{i+1}\ge2\), \(J_i=2-x_{i+1}\), and a left shift. Each language is therefore periodic. At \(t=n/2-1\), the max window has \(n/2\) parity-spaced entries. Sliding it forward by two replaces its first value \(h_j(0)\) with \(h_{j+n}(0)=h_j(0)+d\), making the maxima nonincreasing if \(d\le0\), nondecreasing if \(d\ge0\). All orbits reach a periodic language by this time. Any periodic state must already be in their union, since this union is invariant and the state is revisited along its orbit.

**Penultimate time at \(N=n-1\).** Put \(n=2m\) and abbreviate the initial heights to \(h_i\). At \(t=m-2\), a window slides from \(h_{k+2},\ldots,h_{k+n-2}\) (stride two) by discarding \(h_{k+2}\) and appending \(h_{k+n}=h_k-1\). A strict increase somewhere is equivalent to
\[
 h_k\ge h_{k+2j}+2\quad(1\le j\le m-1)\tag{*}
\]
for some \(k\). The left-shift language is impossible by mass, so (*) is equivalent to \(\tau=m-1\). A peak satisfying (*) has \(h_{k+r}<h_k\) for \(1\le r<n\): even offsets satisfy (*) and every odd offset is adjacent to one such even offset, with steps bounded by one. If another peak lay at \(k<\ell<k+n\), then \(h_\ell\le h_k-1=h_{k+n}\), contradicting the analogous strict inequality from the second peak on its next \(n-1\) sites. There is at most one peak modulo \(n\).

**Rooted walk count.** Fix the peak \(k\); the increments \(a_j=x_{k+j}-1\) have partial sums \(S_r=h_{k+r}-h_k\). Then \(S_{2j}\le-2\) for \(1\le j\le m-1\), and \(S_n=-1\). The first two increments equal \(-1\); the last two sum to \(+1\) if \(S_{n-2}=-2\) (two ordered choices), or \(+2\) if \(S_{n-2}=-3\) (one choice). There is no other possible penultimate even height. Negate the remaining intermediate increments after deleting the first and final pairs. The resulting walk starts at height zero and is nonnegative at the ends of its \(L=m-2\) pairs, finishing at height zero or one. It may visit \(-1\) between the steps of a pair only in \(0\to-1\to0\). If \(T\) denotes the Motzkin transfer on nonnegative heights (unit weights for horizontal, up and allowed down steps), the transfer of each pair is thus \(K=T^2+e_0e_0^{\mathsf T}\), and the rooted count is \(Q_L=2(K^L)_{00}+(K^L)_{01}\).

Use the formal series \(E(z)=\sum_L M_{2L}z^L\) and \(O(z)=\sum_L M_{2L+1}z^L\), where \(\mathcal M(u)=E(u^2)+uO(u^2)=1+u\mathcal M(u)+u^2\mathcal M(u)^2\) by first-step decomposition. Its odd part gives \(O=E+2zEO\). The base resolvent \(G=(I-zT^2)^{-1}\) has \(G_{00}=E\), \(G_{01}=O-E\), using \(Te_0=e_0+e_1\). Expanding the perturbed resolvent at each occurrence of \(ze_0e_0^{\mathsf T}\) gives
\[
 \sum_{L\ge0}Q_L z^L=\frac{2G_{00}+G_{01}}{1-zG_{00}}=\frac{E+O}{1-zE}=2O.
\]
These formal identities are coefficientwise finite. Each labelled extremizer has exactly one peak, so the census is \(nQ_{m-2}=2nM_{n-3}\). It is positive at every even \(n\ge4\), establishing sharpness. The involution \(A\) gives the same census in the upper sector.

**Asymptotics.** The square-root singularity of the Motzkin generating function gives \(M_j\sim (3\sqrt3/(2\sqrt\pi))3^j j^{-3/2}\). The occupancy of a uniform symbol has span one and variance \(2/3\); the local central limit estimate gives \([z^{n-1}](1+z+z^2)^n\sim \sqrt3\,3^n/(2\sqrt{\pi n})\). Taking the quotient yields \(2/9\). Adding the two counts and dividing by \(3^n\) gives the stated unconditional contribution.

## Verification and relationship to prior work

The accompanying standard-library programs and their recorded outputs provide bounded checks. `verify_even_motzkin.py` checks both sectors through \(n=12\), the peak criterion, and \(Q_L=2M_{2L+1}\) through \(L=17\). `verify.py` and `verify_independent.py` check the height and orbit descriptions through lengths ten and nine, respectively. The all-size argument does not rely on these computations.

The Burgers map and its asymptotic traffic phases are precedents, not claimed as new. See Nishinari and Takahashi, *Analytical properties of ultradiscrete Burgers equation and rule-184 cellular automaton*, [DOI 10.1088/0305-4470/31/24/006](https://doi.org/10.1088/0305-4470/31/24/006), especially §IV; their [multi-value traffic model](https://arxiv.org/abs/nlin/0002007), Eq. (1); and Boccara and Fukś, [*Number-conserving cellular automaton rules*](https://arxiv.org/abs/adap-org/9905004), Table 2 and the discussion of rule 6171534259461. Motzkin numbers themselves are catalogued as [OEIS A001006](https://oeis.org/A001006).

The published [directed three-colour cyclic automaton last-entry law](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-motzkin-last-entry-law-and-winding-selected-basins-in-a-directed--b672f4087fac) gives the different count \(3nM_{n-2}\) and clock \(n-1\) for a different rule. The binary Rule-184 Catalan counts are for capacity one. The distinction here is the off-critical capacity-two census at two specified masses on even rings, with the half-circumference time and a walk constrained at alternate instants. No claim of exhaustive historical priority, or of a total census over all densities, is made.
