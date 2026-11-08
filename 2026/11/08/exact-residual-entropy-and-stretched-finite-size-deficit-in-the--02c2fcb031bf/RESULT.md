# Exact residual entropy and stretched finite-size deficit in the three-state Apollonian Potts antiferromagnet

## Finding
For the deterministic triangular Apollonian graph \(G_t\) of generation \(t\geq2\), consider the zero-field, three-state antiferromagnetic Potts Hamiltonian
\[
H_t(\sigma)=J\sum_{\{u,v\}\in E(G_t)}\mathbf 1_{\sigma_u=\sigma_v},\qquad J>0,\quad\sigma:V(G_t)\to\{0,1,2\}.
\]
Its exact ground energy and number of labeled ground-state spin configurations are
\[
E_t=\frac J2(3^{t-1}+1),\qquad D_t=18b_t+6c_t,
\]
where the **integer** recurrence is initialized by \((a_2,b_2,c_2)=(2,1,9)\) and, for every \(t\geq2\),
\[
\begin{aligned}
a_{t+1}&=a_t^3+2b_t^3,\\
b_{t+1}&=b_t^2(a_t+b_t),\\
c_{t+1}&=3b_t^2c_t.
\end{aligned}
\]
In particular, \(D_2=72\), \(D_3=216\), and \(D_4=18\cdot117+6\cdot729=6480\).

The thermodynamic ground-state entropy exists and is strictly positive, with a **stretched-exponential finite-size correction**:
\[
\boxed{\log D_t=\mathfrak c\,3^t-\mathfrak k\,2^t+\log18+o(1),\qquad t\to\infty.}
\]
Here \(\mathfrak c=0.0859414684425757224\ldots\) and \(\mathfrak k=0.1339684066566889155\ldots>0\) are defined without numerical approximation below. Since \(|V(G_t)|=(3^t+5)/2\), the entropy per site is
\[
\boxed{\lim_{t\to\infty}\frac{\log D_t}{|V(G_t)|}=2\mathfrak c=0.1718829368851514448\ldots.}
\]
Equivalently, the correction to extensive ground-state entropy has exponent \(\log_3 2\) when expressed in terms of system size. No positive-temperature critical phenomenon is asserted.

## Assumptions and scope
The graph \(G_0\) is a triangle with three labeled original vertices. From \(G_t\), insert one new vertex **inside every bounded triangular face created at the previous subdivision**, joining it to that face's three corners; each such face is then replaced by its three new triangular subfaces. The exterior face is never subdivided. Consequently \(|V(G_t)|=(3^t+5)/2\), \(|E(G_t)|=3|V(G_t)|-6\). Spins use three *distinct, named* colors, no boundary color is fixed, and every edge has the same positive penalty \(J\) for equal endpoint colors. The theorem covers all integers \(t\geq2\), at zero external field and zero temperature.

For its exact constants, define \(r_2=2\), \(s_t=\log r_t\), and recursively
\[
r_{t+1}=\frac{r_t^3+2}{r_t+1},\quad
\Delta_t=\log(1+2e^{-3s_t}),\quad
\varepsilon_t=\Delta_t-\log(1+e^{-s_t}).
\]
Then the convergent expressions
\[
\mathfrak c=\frac{\log2}{9}+\sum_{t=2}^{\infty}\frac{\Delta_t}{3^{t+1}},\qquad
\mathfrak k=\frac{\log2}{4}+\sum_{t=2}^{\infty}\frac{\varepsilon_t}{2^{t+1}}
\]
are the constants appearing in the theorem. Both are positive.

## Proof
**Boundary-state reduction.** Let \(F_t(i,j,k)\) be the smallest possible number of monochromatic *new* edges in the depth-\(t\) filled triangle with its three corners held at colors \(i,j,k\), excluding the three outer edges. Let \(N_t(i,j,k)\) be the number of internal fillings attaining it. At depth zero, \(F_0\equiv0\) and \(N_0\equiv1\). For any triple \((i,j,k)\), the central vertex can be assigned \(d\in\{0,1,2\}\). The newly introduced edges cost \(\mathbf1_{d=i}+\mathbf1_{d=j}+\mathbf1_{d=k}\), and the three enclosed triangles have boundary triples \((i,j,d),(j,k,d),(k,i,d)\). Hence
\[
F_{t+1}(i,j,k)=\min_{d\in\{0,1,2\}}\left[\mathbf1_{d=i}+\mathbf1_{d=j}+\mathbf1_{d=k}+F_t(i,j,d)+F_t(j,k,d)+F_t(k,i,d)\right],
\]
while \(N_{t+1}\) sums products of the three subtriangle counts over *precisely the minimizing* choices of \(d\). Each internal vertex and edge belongs to exactly one recursively created subproblem; outer edges are counted only at the final root.

**Three boundary types.** Color permutations and cyclic or reflected corner permutations reduce the 27 boundary triples to types \(AAA,AAB,ABC\) (all equal, exactly two equal, all distinct). Directly applying the recurrence twice yields minimum internal energies \((0,1,2)\) and minimizing counts \((2,1,9)\) at depth two. Suppose at some depth \(t\geq2\) the three energies are \((x,x+1,x+2)\). The three possible center-color classes yield respectively the energy lists
\[
AAA:(3+3x,3+3x,3+3x),\quad
AAB:(3x+4,3x+4,3x+5),\quad
ABC:(3x+5,3x+5,3x+5).
\]
Thus the next three minima are \((3x+3,3x+4,3x+5)\), establishing their differences by induction and giving the all-equal boundary energy \(x_t=(3^{t-1}-3)/2\). Counting the minimizing central colors with their independent descendant fillings gives exactly
\[
(a_{t+1},b_{t+1},c_{t+1})=(a_t^3+2b_t^3,\ b_t^2(a_t+b_t),\ 3b_t^2c_t).
\]
The root's original three edges contribute \(3,1,0\) for the three types. Hence the total minimum is \(x_t+2=(3^{t-1}+1)/2\), achieved only by \(AAB\) and \(ABC\) outer triples. There are respectively 18 and 6 named outer triples. This proves the exact energy and degeneracy formulas for **all** stated generations.

**Asymptotic analysis.** Put \(r_t=a_t/b_t\), \(s_t=\log r_t\), and \(u_t=\log a_t\). The exact recurrences imply
\[
s_{t+1}=2s_t+\varepsilon_t,\qquad u_{t+1}=3u_t+\Delta_t.
\]
For \(r_t\geq2\),
\[
r_{t+1}=\frac{r_t^3+2}{r_t+1}\geq\frac23 r_t^2,
\]
so, starting from \(r_2=2\),
\[
s_t\geq\log(3/2)+2^{t-2}\log(4/3)\longrightarrow\infty.
\]
The elementary bound \(-\log(3/2)\leq\varepsilon_t\leq0\) and the displayed growth ensure convergence of both defining series, with \(\mathfrak k\geq\log(4/3)/4>0\) and \(\mathfrak c\geq\log2/9>0\). Since \(\varepsilon_t,\Delta_t\to0\), the two linear recurrences and their summable tails give
\[
u_t=\mathfrak c3^t+o(1),\qquad s_t=\mathfrak k2^t+o(1),\qquad\log b_t=\mathfrak c3^t-\mathfrak k2^t+o(1).
\]
Finally \(c_{t+1}/b_{t+1}=3(c_t/b_t)/(r_t+1)\). As \(r_t\to\infty\), this ratio tends to zero. Thus \(D_t=18b_t[1+c_t/(3b_t)]\), implying the stated \(\log D_t\) expansion, including its \(\log18\) constant. Division by \(|V(G_t)|\sim3^t/2\) yields the claimed entropy density.

## Verification
The attached `verify.py` independently implements the full 27-boundary-state minimum-plus-count recurrence, verifies its reduction and the exact formulas through generation nine, checks exact brute-force configurations for generations zero, one and two, and evaluates the convergent series numerically. The separately implemented C++ file `exhaustive.cpp` constructs each graph directly and checks every spin assignment for generations zero through three (including all \(3^{16}=43{,}046{,}721\) configurations at generation three, using global color symmetry). The two programs reproduce the counts \(6,36,72,216\) for generations zero to three and the energies \(0,1,2,5\) in units of \(J\). Commands: `python3 verify.py` and `c++ -O3 -std=c++17 exhaustive.cpp -o exhaustive && ./exhaustive`. The all-generation claim is proved by the boundary-state induction; enumeration is a finite check, not a replacement for that proof.

## Relationship to prior work
Andrade and Herrmann's 2004 preprint (subsequently published in 2005) analyzes *two-state Ising* models, including uniform antiferromagnetic bonds and a numerical residual entropy, on the same Apollonian graph. It does not provide a three-color ground-state census or the present finite-size asymptotic. Araújo, Andrade and Herrmann's 2010 preprint develops a general Potts transfer-matrix methodology on Apollonian graphs, but its physical calculations expressly concern **ferromagnetic** Potts interactions, rather than this three-state antiferromagnetic ground manifold. The present exact count concerns minimum-frustration three-colorings, not proper colorings: the graph contains a four-clique from its first subdivision, making its chromatic polynomial at three colors zero. A general transfer-matrix method does not by itself state or imply the proved closed recurrence and its \(2^t\) entropy correction without additional analysis. The two cited foundational studies motivate this calculation but are not claimed as new.

## Limitations
The model is a deterministic finite-generation planar network with a single constant antiferromagnetic coupling and exactly three named colors. These calculations do not treat magnetic fields, finite temperature, other Potts alphabets, stochastic Apollonian networks, or universality and finite-temperature phase transitions. The historical-priority review is limited to accessible published-index records and the primary sources described; unindexed earlier exact calculations of the same three-state antiferromagnetic model remain a residual risk. Independent verification has not been performed.

## References
1. R. F. S. Andrade and H. J. Herrmann, *Magnetic models on Apollonian networks*, arXiv:cond-mat/0411364v1 (first publicly posted 2004-11-14), https://arxiv.org/abs/cond-mat/0411364 ; Phys. Rev. E 71, 056131 (2005).
2. N. A. M. Araújo, R. F. S. Andrade and H. J. Herrmann, *q-state Potts model on the Apollonian network*, arXiv:1007.4494v1 (first publicly posted 2010-07-26), https://arxiv.org/abs/1007.4494 ; Phys. Rev. E 82, 046109 (2010).
3. R. Shrock, *Ground state entropy in Potts antiferromagnets*, Physica A 281 (2000), 221–232, https://doi.org/10.1016/S0378-4371(00)00023-6 ; general context, not a claimed source for this Apollonian calculation.
