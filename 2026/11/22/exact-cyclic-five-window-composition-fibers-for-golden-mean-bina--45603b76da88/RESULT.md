# Exact cyclic five-window composition fibers for golden-mean binary words

## Finding
For every integer \(n\ge5\), let \(\mathcal G_n\) consist of the indexed binary circular words \(a=(a_0,\ldots,a_{n-1})\in\{0,1\}^n\) with \(a_i a_{i+1}=0\) for every index modulo \(n\). The exact, noiseless read of such a word is its cyclic five-window **composition histogram** \(C(a)=(C_0,C_1,C_2,C_3)\), where \(C_j\) counts the \(n\) starting indices whose length-five window has exactly \(j\) ones. No such window has more than three ones. Define the weight and two observable coordinates by
\[
 w=\frac{C_1+2C_2+3C_3}{5},\qquad b=C_2,\qquad t=C_3.
\]
The full histogram is recovered from \((n,w,b,t)\) by \(C_1=5w-2b-3t\) and \(C_0=n-5w+b+2t\).

**Exact feasibility.** Besides the unique all-zero profile \((w,b,t)=(0,0,0)\), the triple \((w,b,t)\) occurs if and only if there exist integers \(p,q,r\ge0\), \(h=w-p-q-r\ge0\), such that
\[
1\le w\le\lfloor n/2\rfloor,\qquad b=3p+2q+r-2t,\qquad E=n-5w+3p+2q+r\ge0,
\]
with \(E=0\) whenever \(h=0\), and the following mutually exclusive conditions on \(t\):
\[
(p,t)=(0,0),\quad\text{or}\quad (p,t)=(w,w),\quad\text{or}\quad
0<p<w\ \text{and}\ \max(0,2p-w)\le t\le p-1.
\]
All choices are finite and explicit; no enumeration of source words is required.

**Exact inverse-fiber multiplicity.** Put \(B(w,0,t)=[t=0]\), \(B(w,w,t)=[t=w]\), and for \(0<p<w\), with \(k=p-t\), set
\[
 B(w,p,t)=\begin{cases}
 \dfrac{w}{k}\binom{p-1}{k-1}\binom{w-p-1}{k-1},&1\le k\le\min(p,w-p),\\
 0,&\text{otherwise}.
 \end{cases}
\]
For nonnegative \(E,h\), put \(H(E,0)=[E=0]\) and \(H(E,h)=\binom{E+h-1}{h-1}\) for \(h>0\). The number \(F_n(w,b,t)\) of **indexed** legal circular words with prescribed observations is exactly
\[
\boxed{F_n(w,b,t)=\frac{n}{w}
\sum_{\substack{p,q,r\ge0,\ h=w-p-q-r\ge0\\
 E=n-5w+3p+2q+r\ge0\\b=3p+2q+r-2t}}
B(w,p,t)\frac{(w-p)!}{q!r!h!}\,H(E,h)}
\]
when \(w\ge1\), with the all-zero fiber of size one. The sum is interpreted as zero when there are no feasible terms. Every right-hand side is an integer despite the prefactor \(n/w\).

**Exact multivariate distribution.** Set
\[
 L=x^3y^2+x^4y+\frac{x^5}{1-x},\qquad R=x^2y^3,\qquad
D=1-s(L+x^2yz)+s^2Lx^2y(z-y^2).
\]
Then the complete length/weight/read-fiber enumerator is the rational formal series
\[
\boxed{\Phi(x,s,y,z)=\frac{x}{1-x}-x\frac{\partial}{\partial x}\log D.}
\]
Its coefficient \([x^ns^wy^bz^t]\Phi\) is exactly \(F_n(w,b,t)\) for every \(n\ge5\); the all-zero word is included. Consequently the optimal size of a zero-error code in this observation model is the number of feasible triples \((w,b,t)\) in the explicit criterion above. At lengths \(n=5,6,\ldots,19\) those maxima are
\[
3,4,4,7,8,12,13,17,21,27,33,40,47,58,68.
\]

## Assumptions and scope
The alphabet is exactly the labeled binary alphabet; the prohibition of adjacent ones applies across the cyclic boundary. Words are **indexed**, not identified under rotation, even though the observation forgets the starting phase. Each of the \(n\) cyclic starting positions contributes one length-five composition read; positions are counted with multiplicity. The histogram forgets the ordering of the symbols within individual five-windows. The results assume exact observations without errors and assert neither noisy-channel bounds nor unique reconstruction of every input. The displayed formula is not an assertion about linear strings or ordered five-gram frequencies.

## Proof
**1. Zero-gap representation.** Any nonzero circular admissible word with \(w\) ones has a unique cyclic sequence of positive zero-gaps \((g_1,\ldots,g_w)\), up to choosing which one is designated first. Here \(g_i\) is the number of zeros between the \(i\)-th one and the next one. Its length is \(n=w+\sum_i g_i\). Define
\[
p=\#\{i:g_i=1\},\quad q=\#\{i:g_i=2\},\quad r=\#\{i:g_i=3\},\quad
 t=\#\{i:g_i=g_{i+1}=1\},
\]
with indices cyclically modulo \(w\). The remaining \(h=w-p-q-r\) gaps have length at least four.

**2. Literal five-window observations.** An admissible five-window has three ones if and only if it is `10101`. Its two successive zero-gaps each have length one. Thus \(C_3=t\), including cyclic wraparound. To count all pairs of one-occurrences within a length-five window, sum over pairs at forward distances two, three and four. A pair at distance \(d\) is contained in exactly \(5-d\) cyclic five-windows, counting starting positions with multiplicity. At distance two its endpoints flank a gap of length one; at distance three, a gap of length two; and at distance four, either a gap of length three or two consecutive gaps of length one. Consequently
\[
 C_2+3C_3=3p+2q+r+t,
\]
which proves \(C_2=3p+2q+r-2t\). Each one occurs in five windows, so \(C_1+2C_2+3C_3=5w\); summing all window classes recovers \(C_0\) and proves the claimed equivalence between the observations and \((w,b,t)\). These identities count occurrences even when the circular word has a smaller primitive period; no primitivity is assumed.

**3. Feasible integers and the sharp adjacency interval.** A gap of each of the types \(1,2,3,\ge4\) contributes at least \(1,2,3,4\) zeros. Therefore
\[
n\ge w+p+2q+3r+4h=5w-3p-2q-r.
\]
Surplus \(E=n-5w+3p+2q+r\) can be assigned to the \(h\) long gaps, and every nonnegative surplus is possible when \(h>0\); if \(h=0\), it must be zero. The cyclic locations of the \(p\) unit gaps form a binary circular length-\(w\) pattern. For \(0<p<w\), its number \(k\) of unit-gap runs equals \(p-t\). Both it and its complement have \(k\) nonempty cyclic runs. Thus \(1\le k\le\min(p,w-p)\), equivalently \(\max(0,2p-w)\le t\le p-1\). If all or no gaps are units, the cases are \(t=w\) and \(t=0\), respectively. Conversely, make any such cyclic run pattern, assign the remaining types \(2,3,\ge4\), and distribute the surplus among long gaps. This constructs a word with exactly the prescribed observation and proves necessity and sufficiency, with no unsupported feasibility conditions.

**4. Complete fiber count.** Fix \(p,q,r,h,E\). If \(0<p<w\), a circle of \(w\) labeled gap slots having \(k=p-t\) nonempty runs of unit gaps and \(k\) runs of non-unit gaps is counted by
\[
 \frac{w}{k}\binom{p-1}{k-1}\binom{w-p-1}{k-1}.
\]
Indeed, select a distinguished beginning of a unit-gap run, choose the two compositions into \(k\) positive run lengths, and divide by the \(k\) possible designated run beginnings. The pure cases each have one cyclic indicator pattern. Among the \(w-p\) non-unit slots, the assignments of gap lengths two, three and at least four number \((w-p)!/(q!r!h!)\); the extra zeros of long gaps are allocated in \(H(E,h)\) ways by stars and bars. For every indexed binary circular word of weight \(w\), there are \(w\) choices of its designated one; for every ordered gap list, there are \(n\) possible locations of that designated one. Double counting gives precisely \(n/w\) times the number of ordered labeled gap lists. This proves the boxed fiber formula, including its integrality and periodic words.

**5. Rational generating function.** A unit gap has length-weight and observation-weight \(R=x^2y^3\); non-unit gaps have aggregated weight \(L=x^3y^2+x^4y+x^5/(1-x)\), for gaps of length two, three, or at least four. Two adjacent unit gaps reduce the two-window count by two and add a three-window, contributing an interaction weight \(z/y^2\) at their junction. A two-state transfer matrix recording whether the preceding gap was a unit gap is therefore
\[
T=\begin{pmatrix}L&R\\L&Rz/y^2\end{pmatrix}.
\]
As formal power series, \(\operatorname{tr}(T^w)\) counts ordered cyclic gap lists of length \(w\) by total binary length and the histogram coordinates \((w,b,t)\). The identity
\[
\sum_{w\ge1}\frac{s^w}{w}\operatorname{tr}(T^w)=-\log\det(I-sT)
\]
is a formal series identity, without any analytic convergence assumptions. Multiplying each cyclic gap list by the factor \(n/w\) for indexed circular words is accomplished by \(x\partial_x\). Direct calculation gives \(\det(I-sT)=D\). Finally, the all-zero word contributes \(x/(1-x)\). Thus \(\Phi=x/(1-x)-x\partial_x\log D\), which is rational since \(D(0,s,y,z)=1\). Equivalence classes of the noiseless channel are exactly its nonempty fibers; choosing one representative per fiber is optimal. This completes the proof.

## Verification
Run `python3 verify_direct.py` and `python3 verify_transfer.py` in the directory containing these files. Both use only the Python standard library. The first independently enumerates literal cyclic five-windows for every admissible indexed word of lengths \(5\) through \(19\), and tests every exact \((w,b,t)\) inverse-fiber size against the closed gap formula. The second enumerates all five-window observation fibers through length \(30\) using a distinct eight-state de Bruijn closed-walk calculation and compares each complete histogram with the gap formula. These finite checks corroborate, but do not replace, the all-length proof above.

## Relationship to prior work
The foundational *String Reconstruction from Substring Compositions* [1] concerns complete **linear** composition observations, not this cyclic, five-window-only source. *Codes for DNA Sequence Profiles* [2] develops constrained de Bruijn graph methods for **ordered** read frequencies, unlike the coarser Hamming-weight-only observations here. The prior published classification [3] of cyclic **four-gram** profiles in the same no-adjacent-ones source does not imply the present five-window observation: the gap cycles \((1,1,2,2)\) and \((1,2,1,2)\) have exactly the same four-gram counts but different numbers, respectively one and zero, of adjacent unit-gap pairs, and hence distinct five-window histograms. The prior cyclic **three-window** composition realization theorem [4] has a different read length. The cyclic length-at-most-four composition enumeration [5] also lacks the five-window adjacency interaction. Classical transfer-matrix and cyclic run-counting techniques are methods used here, not claimed as new. The claimed advance is the explicit all-length five-window feasibility, inverse-fiber and rational multivariate spectrum for this constrained source.

## Limitations
The formula holds for exact cyclic length-five **composition** observations, binary words avoiding cyclic `11`, and lengths at least five. It does not determine the maximum error-correcting code size under noisy observations, extend directly to ordered five-gram reconstruction, or classify alphabets larger than two. The formula for the zero-error code size is an exact finite count of feasible triples, not a closed univariate quasipolynomial. An earlier equivalent formula in unindexed coding, symbolic dynamics, or Markov-type literature remains possible. These claims have not undergone independent scientific validation; computational tests are finite corroboration.

## References
1. J. Acharya and collaborators, *String Reconstruction from Substring Compositions*, arXiv:1403.2439 (first public 2014-03-10), https://arxiv.org/abs/1403.2439.
2. H. M. Kiah, G. J. Puleo and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517 (first public 2015-02-02), https://arxiv.org/abs/1502.00517.
3. *Exact fibers and uniquely reconstructible profiles for cyclic four-gram reads under a binary run-length constraint*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-fibers-and-uniquely-reconstructible-profiles-for-cyclic-fo--d7a18695ef7b.
4. *Cyclic binary trimer compositions: an exact realization and spectrum theorem*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-cyclic-binary-trimer-compositions-an-exact-realization-and-spect--5ce7c84ef38b.
5. *Exact codebook count for cyclic binary composition reads of lengths at most four*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-codebook-count-for-cyclic-binary-composition-reads-of-leng--5e91d703d058.
