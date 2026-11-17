# Three-update pulse sorting and a cubic extinction law for one-way excitable rings

## Finding

For each integer \(n\ge3\), let \(F\) be synchronous three-state Greenberg–Hastings excitation on the directed cycle with vertices \(\mathbb Z/n\mathbb Z\), in which vertex \(i\) consults only vertex \(i+1\). Let \(S\) be the left spatial translation, \((Sx)_i=x_{i+1}\). Then, as maps on every initial configuration,

\[
F^4=S\circ F^3.
\]

After at most **three** updates, every state is a rigidly translating train of isolated \(12\)-pulses, with at least one zero between consecutive pulses; the bound three is attained for every \(n\ge3\). In particular, every eventual period divides \(n\). The zero state is the unique fixed point.

For an initial configuration \(x\), define the number of surviving pulses \(K_n(x)\) to be the number of \(12\)-blocks in \(F^3(x)\). The full, all-initial-state distribution is

\[
H_n(z):=\sum_{x\in\{0,1,2\}^n}z^{K_n(x)}
=\operatorname{tr}\!\left(
\begin{pmatrix}1&2&0\\1&1&1\\z&1&1\end{pmatrix}^{n}
\right).
\]

Its transfer characteristic polynomial is \(\lambda^3-3\lambda^2+2-2z\). The number of configurations eventually extinguishing to the all-rest state is exactly

\[
E_n=H_n(0)=(1+\sqrt3)^n+(1-\sqrt3)^n+1.
\]

Consequently, for uniformly random independent initial states, the extinction probability is \(E_n/3^n\sim((1+\sqrt3)/3)^n\), while the survival probability approaches one exponentially fast. Both the three-update cutoff and the extinction law hold at *every* ring length, without an asymptotic restriction.

## Assumptions and scope

The alphabet is \(\{0,1,2\}\): zero is resting, one excited and two refractory. All indices are modulo \(n\). One update is exactly

\[
F(x)_i=\begin{cases}
2,&x_i=1,\\
0,&x_i=2,\\
1,&x_i=0\text{ and }x_{i+1}=1,\\
0,&x_i=0\text{ and }x_{i+1}\ne1.
\end{cases}
\]

The direction and the single consulted neighbor are essential. This is **not** the usual undirected nearest-neighbor Greenberg–Hastings rule, and it is not the three-color cyclic cellular automaton in which nonzero states also advance only by contact. A pulse is the cyclic occurrence of \(12\) with zero before the \(1\) and after the \(2\); distinct pulses are separated by at least one zero. The first periodic-entry time is the least nonnegative integer \(t\) for which \(F^t(x)\) belongs to a cycle of the finite map.

## Proof

**1. A local two-step identity.** Define the binary indicator

\[
m_i(x)={\bf1}\{x_i\in\{0,2\},\ x_{i+1}=0,\ x_{i+2}=1\},
\quad a_i(x)={\bf1}\{x_i=0,\ x_{i+1}=1\}.
\]

A direct case distinction on \(x_i\in\{0,1,2\}\) gives

\[
F^2(x)_i=2a_i(x)+m_i(x),\qquad
F^3(x)_i=2m_i(x)+m_{i+1}(x).
\]

For the second identity, a one at time two arises precisely from a marker \(m_i=1\), so advances to two at time three. A zero at time two can become one only when \(m_{i+1}=1\); this condition forces \(a_i=m_i=0\), ensuring the site is indeed zero. These are mutually exclusive events.

**2. Pulse separation and translation.** If \(m_i=1\), then \(m_{i+1}=m_{i+2}=0\), since the former requires \(x_{i+2}=0\) and the latter requires \(x_{i+2}\ne1\), contrary to \(x_{i+2}=1\). Therefore the formula in step 1 makes \(F^3(x)\) a disjoint union of cyclic \(12\)-pulses, each followed by at least one zero; no markers yields the all-zero state. For any such pulse train \(y\), each one becomes two, each two becomes zero, and a rest site becomes one exactly when the next site is one. Hence \(F(y)=Sy\). By translation equivariance \(FS=SF\), it follows for all \(t\ge3\) that

\[
F^{t+1}(x)=S F^t(x).
\]

The pulse trains are thus recurrent because \(S^n\) is the identity. Conversely every such pulse train is in the range of \(F^3\): if \(y\) is a pulse train, \(F^3(y)=S^3y\), so \(F^3(S^{-3}y)=y\). They are **exactly** the recurrent configurations. A nonempty train cannot be fixed by one-site translation, so zero is the unique fixed point.

The three-update bound is sharp. For \(n=3\), the word \(011\) has \(F^3(x)\ne S F^2(x)\). For \(n\ge4\), the word \(0^{n-4}0101\) has the same strict inequality: at the site indexed \(n-3\), \(F^3(x)_{n-3}=0\) while \((S F^2(x))_{n-3}=2\). Since any already periodic state obeys \(Fy=Sy\) by the exact recurrent classification, these witnesses cannot have entered their eventual cycles by time two.

**3. Exact counting of surviving pulses.** The marker condition \(m_i=1\) is equivalent to the appearance of either local triple \(001\) or \(201\), starting at \(i\). Read the cyclic initial word with a deterministic three-state suffix automaton: state \(A\) means the most recent symbol is \(1\); state \(B\) means the most recent symbol is \(2\), or it is \(0\) preceded by \(1\); state \(C\) means the most recent symbol is \(0\) preceded by \(0\) or \(2\). The transitions on reading \(0,1,2\), weighted by \(z\) exactly for the event \(C\to A\) on reading \(1\), have matrix

\[
Q(z)=\begin{pmatrix}1&2&0\\1&1&1\\z&1&1\end{pmatrix}.
\]

Every cyclic input word has exactly one compatible closed state itinerary, including the constant words. Thus \(\operatorname{tr}(Q(z)^n)\) counts each labelled initial word once, with exponent its number of markers, which equals its surviving pulse count by step 1. An exact determinant calculation gives \(\det(\lambda I-Q(z))=\lambda^3-3\lambda^2+2-2z\), proving the advertised polynomial formula and the finite recurrence

\[
H_n(z)=3H_{n-1}(z)+(2z-2)H_{n-3}(z)\quad(n\ge4),
\]

with \(H_1(z)=3\), \(H_2(z)=9\), and \(H_3(z)=21+6z\). The initial values here extend the transfer polynomial algebraically to \(n=1,2\); the **dynamical theorem** is asserted only for \(n\ge3\).

At \(z=0\), the eigenvalues are \(1\) and \(1\pm\sqrt3\), yielding the stated exact extinction formula. The negative eigenvalue has smaller modulus than \(1+\sqrt3\), so \(E_n\sim(1+\sqrt3)^n\). Division by \(3^n\) gives the limiting probability.

**4. Primitive-period refinement.** Put \(I_d=\operatorname{tr}(R^d)\), where

\[
R=\begin{pmatrix}1&1&0\\0&0&1\\1&0&0\end{pmatrix}.
\]

The directed graph of \(R\) is the three-state memory machine for cyclic binary pulse-position words with mutual distance at least three; consequently \(I_d\) counts pulse trains of spatial length \(d\). Its characteristic polynomial is \(\lambda^3-\lambda^2-1\), and \(I_1=I_2=1\), \(I_3=4\). For each divisor \(p\mid n\), the number of **primitive temporal orbits of least length \(p\)** is

\[
C_p=\frac1p\sum_{d\mid p}\mu(p/d)I_d,
\]

by Möbius inversion for translation-periodic cyclic words. Thus \(C_1=1\), \(C_2=0\), and all nontrivial periods divide \(n\). This is a statement about the full recurrent set, not an approximation or a bounded-enumeration conjecture.

## Verification

The standalone `check_exact.py` independently evaluates the local four-update identity on all \(3^5=243\) five-symbol windows and then exhaustively checks the pulse markers, exact third-step image, weighted transfer coefficients, extinction count, recurrent-image size and sharp cutoff on every initial word for \(3\le n\le10\). The standalone `check_direct.cpp` directly enumerates every initial word for \(3\le n\le12\), computes the synchronous map without the transfer matrix, and checks the three-update shift, pulse spacing and all pulse-count histograms. Commands:

```sh
python3 check_exact.py > check_exact.out
c++ -std=c++17 -O2 -Wall -Wextra check_direct.cpp -o check_direct
./check_direct > check_direct.out
```

The supplied `.out` files record the observed results. For example, at \(n=12\), the direct enumeration checked all \(531441\) initial words, found \(172929\) extinguishing states, and the surviving-pulse histogram \((172929,253176,96840,8448,48)\). These **finite** checks corroborate, but do not replace, the all-\(n\) proof above.

## Relationship to prior work

The Greenberg–Hastings excitation rule and the contrast with cyclic cellular automata are classical; see Fisch–Gravner–Griffeath (1993). Fisch–Gravner (1995), *One-dimensional Deterministic Greenberg–Hastings Models*, studies the symmetric interval neighborhood \(\{-r,\ldots,r\}\) on the line and its periodic-boundary simulations, rather than the **single directed successor** neighborhood used here. Gravner–Lyu–Sivakoff (preprint first public 2016-10-24) develops graph-excitation theory for simple **undirected** graphs and does not state the present one-way factorization, cubic initial-state census, or sharp ring-wide bound. The early Greenberg–Greene–Hastings reaction-diffusion paper was available only in abstract form for this comparison, so absolute priority is not established. Other graph-specific exact extinction and pulse-count results for undirected networks do not imply a claim about oriented successor-only updates.

## Limitations

The results hold only for deterministic synchronous threshold-one three-state excitation with *one directed outgoing neighbor per vertex* on a finite oriented cycle of length at least three. Neither undirected rings, higher thresholds, additional colors, nor graphs with branching are covered. The first update orientation matters for the sign of the shift. The proof is complete within this scope, but no independent mathematical audit or definitive all-literature historical-priority determination is claimed.

## References

1. R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, arXiv:patt-sol/9304001, submitted 1993-04-02. https://arxiv.org/abs/patt-sol/9304001
2. R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, Complex Systems 9 (1995), 329–348. https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first posted 2016-10-24; later Annals of Applied Probability, DOI 10.1214/17-AAP1350. https://arxiv.org/abs/1610.07320
4. J. M. Greenberg, C. Greene and S. P. Hastings, *A Combinatorial Problem Arising in the Study of Reaction-Diffusion Equations*, SIAM Journal on Algebraic and Discrete Methods 1 (1980), 34–42, DOI 10.1137/0601006. Historical comparison was restricted to its abstract.
