# A reentrant six-cycle gap and exact spatial zeta for Rule 73

## Finding
Let \(F_n\) denote the synchronous binary elementary cellular automaton Rule 73 on an indexed cyclic ring of length \(n\ge3\). Let \(c_n\) be the number of distinct *primitive temporal six-cycle orbits*; spatial rotations are not identified. Then
\[
\boxed{c_n>0\quad\Longleftrightarrow\quad n=8\ \text{or}\ n\ge12.}
\]
The first primitive six-periodic configurations occur at circumference eight, disappear completely at circumferences nine, ten and eleven, and then occur at every larger circumference. The first nonzero orbit counts are
\[
 c_8=4,\qquad c_{12}=12,\qquad c_{13}=13,\qquad c_{14}=14,\qquad c_{15}=45,\qquad c_{16}=116.
\]
All counts are determined by the **exact all-circumference generating function**
\[
 \boxed{\sum_{n\ge1} c_nz^n=\frac z6\frac{d}{dz}\log\frac{D_3(z)D_2(z)}{D_6(z)D_1(z)}.}
\]
Here the following integer polynomials specify its factors:
\[
\begin{aligned}
 A(z)&=1-z^3-z^4,\\
 B(z)&=1-2z^2-z^3+z^4,\\
 C(z)&=1-z^3-3z^4-2z^5-z^7+z^8+2z^9,\\
 E(z)&=1-z^2-z^3-3z^4-3z^5+3z^6+z^7+z^8\\
 &\qquad+7z^9+3z^{10}-2z^{11},\\
 D_1(z)&=A(z),\\
 D_2(z)&=(1-z)^2(1+z^2)^2B(z),\\
 D_3(z)&=(1+z+z^2)^2(1-z+z^3)^2C(z),\\
 D_6(z)&=(1-z)^5(1+z)^3(1+z^2)^4(1+z^4)^3\\
 &\qquad\cdot(1+z+z^2)^2(1-z+z^3)^2E(z).
\end{aligned}
\]
Each denominator has constant coefficient one, and the formal power series is taken at \(z=0\). Moreover, writing \(\alpha=1.61574999892981\ldots\) for the Perron root of
\[
 x^{11}-x^9-x^8-3x^7-3x^6+3x^5+x^4+x^3+7x^2+3x-2,
\]
we have the strictly larger temporal-six entropy and the exact asymptotic
\[
\boxed{c_n\sim\alpha^n/6}\qquad(n\to\infty).
\]

## Assumptions and scope
For bits \(a,b,c\in\{0,1\}\), the local rule is \(f(a,b,c)=1\) precisely on neighborhoods `000`, `011`, and `110`, and zero otherwise. The update is \(F_n(x)_i=f(x_{i-1},x_i,x_{i+1})\), with spatial subscripts interpreted modulo \(n\). The ring is indexed: no quotient is taken by spatial rotation, reflection, or bit complementation. A primitive temporal six-cycle orbit is an unordered set of six distinct configurations consecutively related by \(F_n\). The formal coefficient formula also applies at circumferences one and two using repeated spatial neighbors; the physical statement concerns all integers \(n\ge3\).

## Proof
**Time-column graph and periodic points.** For each \(t\in\{1,2,3,6\}\), encode a spatial site's periodic time history by a \(t\)-bit column \(a\in\{0,\ldots,2^t-1\}\), with bits \(a_j\) for \(0\le j<t\). Build a directed graph \(G_t\) whose vertices are ordered pairs \((a,b)\), and whose edges are exactly
\[
(a,b)\longrightarrow(b,c)\quad\Longleftrightarrow\quad
 b_{j+1\bmod t}=f(a_j,b_j,c_j)\ \text{for all}\ 0\le j<t.
\]
Let \(M_t\) be its adjacency matrix. Every closed length-\(n\) spatial walk corresponds bijectively to an indexed configuration fixed by \(F_n^t\): the time-zero bits give the configuration, and all subsequent bits satisfy the local rule. Consequently,
\[
 T_t(n):=\#\operatorname{Fix}(F_n^t)=\operatorname{tr}(M_t^n).
\]
Because all temporal periods dividing six are among \(1,2,3,6\), Möbius inversion gives
\[
 6c_n=T_6(n)-T_3(n)-T_2(n)+T_1(n).
\]

**Exact finite determinants.** The graphs are constructed by applying the eight-entry truth table to every triple of time columns. Only vertices in strongly connected components containing directed cycles contribute to traces. For temporal divisors \(1,2,3,6\), the sizes of these cyclic components are respectively
\[
[4],\quad[8,1,1],\quad[19],\quad[23,8,8,8,1,1].
\]
Computing every determinant with *integer Newton identities* on exact closed-walk traces yields \(\det(I-zM_t)=D_t(z)\), with the factors stated in the finding. This is a completely finite, explicit, independently repeatable algebraic step: `verification/verify_transfer.py` reconstructs the graphs, identifies their cyclic components and compares *every determinant coefficient* with the specified factors. The formal identity
\[
 -z\frac{d}{dz}\log\det(I-zM_t)=\sum_{n\ge1}T_t(n)z^n
\]
then proves the claimed generating function for every circumference, not merely the computationally tested ones.

**The exceptional gap and all larger circumferences.** The exact trace recurrences obtained from these determinants yield \(6c_n=0\) for all \(1\le n\le7\) and for \(n=9,10,11\), whereas \(6c_8=24\). The remaining infinite support assertion has a separate *constructive* proof. In the 23-vertex cyclic component of \(G_6\), encode the pair of six-bit columns \((a,b)\) as the integer \(64a+b\). Vertex `21` includes a column with least temporal period two. The same component contains a set of fifteen vertices whose column pairs have least temporal period three. For each of the twelve lengths \(12,13,\ldots,23\), there exists a closed walk based at vertex `21` visiting at least one such period-three vertex. The exact lists of vertex IDs are printed and checked edge-by-edge by `verification/verify_transfer.py`. Every one of these walks therefore produces a state of least period six: the period-two column excludes temporal periods one and three, while the period-three column excludes one and two. For any integer \(n\ge12\), write \(n=12q+r\) with \(q\ge1\) and \(0\le r<12\); concatenate the certified based walk of length \(12+r\) with \(q-1\) copies of that of length twelve. The result is a closed length-\(n\) walk still containing both temporal types, hence a primitive six-cycle state. This proves the all-length support assertion and identifies precisely the reentrant gap.

**Exponential rate.** The 23-vertex component of \(G_6\) is strongly connected and contains the genuine directed cycles `4032,63,4095,4032` and `2688,21,1344,42,2688`, of respective lengths three and four. Hence its adjacency matrix is primitive. Its characteristic polynomial contains the degree-eleven factor written in the finding, with remaining factors of strictly smaller spectral radius by primitivity. An exact positive-vector Collatz–Wielandt calculation, built from 180 matrix-vector updates, places its Perron eigenvalue in \((1.61574,1.61576)\), above the temporal-three and temporal-two Perron radii (respectively below \(1.5458\) and \(1.4903\)). All other components of \(G_6\) are isolated loops or directed eight-cycles, each of spectral radius one. Perron–Frobenius theory implies \(T_6(n)=\alpha^n+o(\alpha^n)\), and the other three trace terms are \(o(\alpha^n)\), establishing \(c_n\sim\alpha^n/6\).

## Verification
The standalone standard-library program `verification/verify_transfer.py` constructs all time-column graphs, computes cyclic strongly connected components and full characteristic determinants using integer arithmetic, establishes all small zero coefficients, prints twelve explicit mixed-clock return walks and checks their adjacency, and calculates Perron bounds. It terminates with `EXACT_TRANSFER_OK`. The independent program `verification/check_direct.py` applies the local rule directly to every initial state of every ring length three through fifteen, computes periodic-point counts for divisors of six, and verifies the primitive six-orbit census; it terminates with `BRUTE_RING_OK`. Both programs were run successfully from these packaged files. Direct finite experiments do not prove an infinite statement; the exact transfer identity and based-walk concatenation provide that proof.

## Relationship to prior work
Wolfram's *A New Kind of Science* (first published 2002) describes periodic Rule 73 blocks and persistent period-three regions. Sutner's section 3.1 gives the period-three existence spectrum and initial primitive three-cycle counts, not an all-size temporal-six census. Stricker's 2023 cycle-length classification explicitly reports full finite-ring cycle spectra through length 22 (some partial data further) and surveys Rule 73, but does not state this sixth-return rational function, the all-length reentrant support theorem or the associated entropy. Kang's 2014 study of Rule 73 and its symmetry relative Rule 109 uses a *spaced-neighbor* LDCA model; its period conclusions do not apply directly to the ordinary nearest-neighbor rule here. Previously published exact Rule 73 results determine period-one/two zeta functions, the occupation-weighted period-three zeta, and one-step image sizes. These do not determine the extra sixth-return factor \(E(z)\), the mixed-period bridge or the period-six entropy. Conjugation carries the result to Rule 109; the alternate name was also searched. The transfer-matrix method itself is classical and is not claimed as an innovation.

## Limitations
Finite historical cycle atlases may already have tabulated some of the short-length examples, so the finite numbers alone are not asserted to have priority. The contribution is their all-length rational census, structural existence criterion and asymptotic growth. No claim is made about initial conditions that are transient, attraction-basin populations, or periods other than six. A general corpus search cannot rule out obscure historical equivalent enumerations. Independent external mathematical validation has not been performed.

## References
- S. Wolfram, *A New Kind of Science* (Wolfram Media, first publication 2002-05-14), https://www.wolframscience.com/nks/notes-3-2--rule-73/ and https://www.wolframscience.com/nks/notes-6-6--repeating-blocks-in-cellular-automata/; publication date https://www.wolframscience.com/nks/citation/.
- K. Sutner, *Linear Cellular Automata and Automaticity*, section 3.1, https://www.cs.cmu.edu/~sutner/papers/sutner-ca-automaticity.pdf (public manuscript date not independently verified).
- H.-P. Stricker, *Classification of Elementary Cellular Automata Based on Their Limit Cycle Lengths in Z/k*, *Complex Systems* 32 (2023), 229–251, https://content.wolfram.com/sites/13/2024/01/32-3-1.pdf.
- L. Kang, *Complex Behavior in Long-Distance Cellular Automata*, *Complex Systems* 23 (2014), 93–115, https://content.wolfram.com/sites/13/2018/12/23-2-1.pdf.
- *Rule 73: exact temporal-two zeta and an exponential oscillation–equilibrium gap*, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-rule-73-exact-temporal-two-zeta-and-an-exponential-oscillation-e--91ecce9dc622.
- *Exact space-time occupation law and Gaussian concentration in Rule 73 three-cycles*, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-space-time-occupation-law-and-gaussian-concentration-in-ru--786af882d163.
- *Exact cyclic one-step image series of elementary cellular automaton Rule 73*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-cyclic-one-step-image-series-of-elementary-cellular-automa--4412da3b7a44.
