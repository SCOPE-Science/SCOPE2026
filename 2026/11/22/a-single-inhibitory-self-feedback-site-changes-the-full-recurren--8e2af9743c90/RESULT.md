# A single inhibitory self-feedback site changes the full recurrent census of ring NOR automata

## Finding
Let \(n\ge3\) and consider binary synchronous negative-AND (NOR) dynamics on the labelled ring \(\mathbb Z/n\mathbb Z\). Every site reads its two cyclic neighbors, but site zero additionally reads itself. For a state \(x\in\{0,1\}^n\), the update \(F_n\) is
\[
(F_n(x))_i=1\quad\Longleftrightarrow\quad x_{i-1}=x_{i+1}=0\ \text{and}\ (i\ne0\ \text{or}\ x_0=0).
\]
All indices are modulo \(n\). Let \(Q_n\) be the number of initially periodic labelled states, \(E_n\) the number of fixed states and \(O_n\) the number of primitive two-cycle orbits. Then every state is periodic after at most one update, this bound is sharp, and
\[
O_n=(Q_n-E_n)/2,\qquad
E_n=P_n-H_{n-3},
\]
where the Perrin sequence is \(P_0=3,P_1=0,P_2=2,P_j=P_{j-2}+P_{j-3}\) for \(j\ge3\), and \(H_0=H_1=1,H_2=2,H_j=H_{j-2}+H_{j-3}\) for \(j\ge3\) counts maximal independent sets of a path on \(j\) vertices.

For the identical ring with *no* self-reading site, the number of periodic states is
\[
R_n=\begin{cases}P_{2n},&n\ \mathrm{odd},\\P_n^2,&n\ \mathrm{even}.\end{cases}
\]
The feedback-induced difference \(\Delta_n=Q_n-R_n\) has the exact rational generating function
\[
\boxed{\displaystyle
\sum_{n\ge1}\Delta_n z^{n-1}=
\frac{3z^8-5z^7+2z^6+2z^5-5z^4+3z^3+z^2-z}
{(z^3-z-1)(z^3-z+1)(z^3-z^2+2z-1)}.}
\]
Here the coefficient extension to \(n=1,2\) is an algebraic transfer convention; the actual dynamical assertions concern \(n\ge3\). In particular \(R_4=4,Q_4=5\) (feedback increases periodic states), \(R_6=Q_6=25\), and \(R_{10}=289,Q_{10}=268\).

Let \(\lambda\approx1.754877666246693\) denote the largest real root of \(t^3-2t^2+t-1\), \(z_*=1/\lambda\), and let \(N(z)\), \(d(z)\) denote respectively the numerator and denominator in the boxed fraction. Then
\[
\lim_{n\to\infty}\frac{Q_n}{R_n}=1-\frac{N(z_*)}{d'(z_*)}
\approx 0.940639467358146.
\]
Thus one altered local input reduces the asymptotic population of periodic states by approximately \(5.936\%\) while causing an increase for the four-site ring.

## Assumptions and scope
The ring has \(n\ge3\) distinct vertices, nearest-neighbor edges, and exactly one extra self-input at vertex zero. States are labelled binary vectors, not spatial-isomorphism classes. The update is simultaneous, uses the previous time step, and is an inhibitory AND of negated inputs, not ordinary positive majority. A self-input is a local Boolean rule, not an additional distinct ordinary neighbor. Counts include fixed and exact least-period-two configurations; the only possible eventual periods are one and two.

## Proof
**1. Sharp entrance bound.** For any symmetric zero-or-one relation (including allowed self-loops), let \(\Phi(S)\) be the set of vertices with no related member in \(S\). Symmetry implies \(S\subseteq\Phi^2(S)\). Since \(\Phi\) reverses inclusion, \(\Phi^3(S)\subseteq\Phi(S)\). Applying the first inclusion to \(\Phi(S)\) gives the reverse inclusion, so \(\Phi^3=\Phi\). Consequently every image is immediately periodic with period dividing two. To see sharpness, take the state supported on all vertices except zero. Every vertex has two distinct cyclic neighbors, at least one of which lies in that support. The state therefore maps to the empty state, which maps to the full support. The original state differs from its second iterate, so it is not initially periodic. This works for all \(n\ge3\).

**2. Fixed states.** A fixed support must omit zero because of its self-input. Among supports omitting zero, the loop has no effect on the update, so a support is fixed exactly when it is a maximal independent set of the ordinary cycle \(C_n\) that omits zero. Indeed the NOR condition means that each selected vertex has no selected cyclic neighbor, and every unselected vertex, including zero, has a selected cyclic neighbor. There are \(P_n\) maximal independent sets of the ordinary cycle. Those containing zero correspond bijectively to maximal independent sets of the path induced by vertices \(2,3,\ldots,n-2\), giving \(H_{n-3}\). The recurrence for \(H_j\) follows by classifying the leftmost independent-dominating choice (gaps two or three). This gives \(E_n=P_n-H_{n-3}\).

**3. Periodic states as exact transfer traces.** For a periodic state \(x\), put \(y=F_n(x)\). Then \(F_n(y)=x\); conversely any such pair gives a periodic state. Write a column \(c_i=(x_i,y_i)\in\{0,1\}^2\), encoded by \(x_i+2y_i\in\{0,1,2,3\}\). On triples \((\ell,c,r)\), define the Boolean rule \(G_\varepsilon\) for \(\varepsilon\in\{0,1\}\):
\[
\begin{aligned}
G_\varepsilon(\ell,c,r)=1\quad\Longleftrightarrow\quad
&c_x=\neg(\ell_y\lor r_y\lor(\varepsilon\land c_y)),\\
&c_y=\neg(\ell_x\lor r_x\lor(\varepsilon\land c_x)).
\end{aligned}
\]
Index the sixteen ordered pairs \((\ell,c)\) of column symbols. Set the integer \(16\times16\) matrices
\[
(A_\varepsilon)_{(\ell,c),(c',r)}=
\mathbf 1_{\{c'=c\}}\mathbf 1_{\{G_\varepsilon(\ell,c,r)=1\}}.
\]
Put \(A=A_0\) and \(D=A_1\). The single marked local site uses \(D\), all others use \(A\). The trace closes the ring with no boundary correction, hence
\[
Q_n=\operatorname{tr}(DA^{n-1}),\qquad R_n=\operatorname{tr}(A^n)\quad(n\ge3).
\]
For the unmarked rule, the bipartite double cover of \(C_n\) consists of a single \(C_{2n}\) when \(n\) is odd and two copies of \(C_n\) when \(n\) is even. A mutually NOR-stable pair is exactly an inclusion-maximal independent set of this cover. The standard Perrin enumeration of cycle maximal independent sets proves the formula for \(R_n\).

**4. Finite exact algebra certificate for the generating function.** The transfer entries have been defined independently of any numerical data. Let
\[
\begin{aligned}
d(z)&=1-2z+z^3+z^4-3z^5+z^6-z^8+z^9,\\
N(z)&=3z^8-5z^7+2z^6+2z^5-5z^4+3z^3+z^2-z.
\end{aligned}
\]
Direct exact integer multiplication of these explicitly defined sixteen-state matrices verifies
\[
A\bigl(A^9-2A^8+A^6+A^5-3A^4+A^3-A+I\bigr)=0.
\]
It also verifies, writing \(h_k=\operatorname{tr}((D-A)A^k)\), that
\[
(h_0,\ldots,h_9)=(0,-1,-1,1,-2,0,-1,-8,-7,-21).
\]
These ten entries and the matrix annihilator show by coefficient recurrence that \(d(z)\sum_{k\ge0}h_kz^k=N(z)\) for **every** coefficient, not just the tested entries. Since \(h_{n-1}=Q_n-R_n\), the boxed identity follows. The standalone exact-integer checker reproduces the finite certificate without matrix libraries.

**5. Asymptotic retention fraction.** The Perrin sequence is asymptotic to \(\alpha^n\), where \(\alpha\) is the real root of \(t^3-t-1\); its square \(\lambda=\alpha^2\) solves \(t^3-2t^2+t-1\). Hence \(R_n\sim\lambda^n\), independent of the parity of \(n\). The rational series for \(\Delta_n\) has a simple dominant pole at \(z_*=1/\lambda\), with the other poles of strictly larger modulus. Residue extraction gives \(\Delta_n/R_n\to-N(z_*)/d'(z_*)\), proving the stated exact limiting ratio.

## Verification
The accompanying `verify_feedback.py` uses only Python 3 and arbitrary-precision integer arithmetic. It constructs the transfer matrices from the displayed triple rule, verifies the matrix annihilator and generating-function coefficient certificate, and independently enumerates all \(2^n\) labelled states for each \(3\le n\le12\). It checks \(F_n^3=F_n\), the recurrence, the fixed-state formula and the periodic-state counts from which the two-cycle counts follow. The computations check the finite algebra identity; the proof extends it to every \(n\) through the annihilator recurrence. The explicit state in step 1 proves sharpness for all \(n\), independently of the finite checker.

## Relationship to prior work
Bisdorff and Marichal identify Perrin numbers with maximal independent sets of unperturbed cycles and study their geometric symmetry orbits. Veliz-Cuba and Laubenbacher connect negative AND-NOT Boolean fixed points to maximal independent sets. These facts supply baseline enumerators and the fixed-state reduction, but neither constitutes an enumerated period-two law for the inhomogeneous one-self-input ring. General monotone/polarity arguments explain the period-two ceiling, not the exact rational feedback correction or its nonzero limiting proportion. Work on open-neighborhood NOR Rule 5 for odd *homogeneous* rings determines their preimage fibers; the extra self-input changes the update at one site and is not an equivalent homogeneous-ring instance.

## Limitations
The result concerns exact binary synchronous NOR dynamics only, not probabilistic asynchronous dynamics or arbitrary Boolean logical functions. The first two coefficient indices are formal algebraic extension values, not one- and two-vertex ring results. The prior-art survey cannot rule out all unindexed or inaccessible work, especially potentially related results on finite cyclic cellular automata or maximal independent sets of edge-modified cycles; this is not a priority certification. The asymptotic claim concerns *periodic-state counts*, not total attraction-basin sizes.

## References
1. R. Bisdorff and J.-L. Marichal, “Counting non-isomorphic maximal independent sets of the n-cycle graph,” arXiv:math/0701647 (first posted 2007-01-23), *Journal of Integer Sequences* 11 (2008), Article 08.5.7, https://arxiv.org/abs/math/0701647.
2. A. Veliz-Cuba and R. Laubenbacher, “On the computation of fixed points in Boolean networks,” published online 2011-10-15, *Journal of Applied Mathematics and Computing* 39 (2012), 145–153, https://doi.org/10.1007/s12190-011-0517-9.
3. J. Aracena, A. Richard, and L. Salinas, “Maximum number of fixed points in AND–OR–NOT networks,” *Journal of Computer and System Sciences* 80 (2014), 1175–1190, https://doi.org/10.1016/j.jcss.2014.04.025.
