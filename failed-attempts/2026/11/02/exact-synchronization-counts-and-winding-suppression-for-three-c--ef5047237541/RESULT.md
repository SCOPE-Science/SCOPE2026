# Exact synchronization counts and winding suppression for three-color cyclic automata on prism ladders

## Finding

Let \(G_n=C_n\square K_2\) be the simple, labelled circular ladder (prism graph) with two rows and \(n\ge3\) cyclic columns. In synchronous three-color cyclic cellular automata (CCA), a vertex of color \(c\in\mathbb Z/3\mathbb Z\) advances to \(c+1\pmod3\) if some adjacent vertex currently has color \(c+1\pmod3\), and otherwise retains its color. A configuration *synchronizes* if it eventually becomes spatially constant. Let \(S_n\) be the number of initially labelled colorings that synchronize.

Define the following Laurent-polynomial transfer matrix:
\[
T(z)=\begin{pmatrix}
1+z+z^{-1}&1+z^{-1}&z^{-1}\\
1+z&1+z+z^{-1}&1+z^{-1}\\
z&1+z&1+z+z^{-1}
\end{pmatrix}.
\]
For every integer \(n\ge3\), the **exact** synchronization-basin size is
\[
\boxed{S_n=3[z^0]\operatorname{tr}(T(z)^n)}.
\]
Its first four values are \(S_3=261\), \(S_4=1485\), \(S_5=8409\), and \(S_6=49215\). In particular the uniform-random initial synchronization probability is \(S_n/9^n\).

There is also a sharp asymptotic with an explicit algebraic exponential rate:
\[
\boxed{S_n=\frac{3\Lambda^n}{\sqrt{2\pi\sigma^2n}}\bigl(1+O(n^{-1})\bigr)},\qquad
\Lambda=\frac{7+\sqrt{33}}2,\qquad
\sigma^2=\frac54-\frac{19\sqrt{33}}{132}>0.
\]
Thus
\[
\Pr(\mathrm{synchronization})\sim\frac{3}{\sqrt{2\pi\sigma^2n}}\left(\frac{\Lambda}{9}\right)^n,
\qquad \Lambda/9\approx0.7080312581.
\]

For comparison, on the open ladder \(H_n=P_n\square K_2\), with the same \(2n\) labelled vertices and the same CCA rule, the exact synchronizing count is
\[
O_n=3\mathbf 1^{\mathsf T}T(1)^{n-1}\mathbf1.
\]
Writing \(t=(\sqrt{33}-1)/4\), \(B=(2+t)^2/(2+t^2)\), the **cyclic seam suppression law** is
\[
\boxed{\frac{S_n}{O_n}\sim\frac{\Lambda}{B\sqrt{2\pi\sigma^2}}n^{-1/2}}
\qquad\biggl(\frac{\Lambda}{B\sqrt{2\pi\sigma^2}}\approx1.3115981446\biggr).
\]
The polynomial loss comes specifically from the zero-winding condition around the cyclic seam; the exponential growth rate is the same for the open and closed ladders.

## Assumptions and scope

Rows and cyclic columns are labelled. For \(n=3\), each row is the ordinary triangle, and the graph is the triangular prism. A graph edge is present between neighboring columns within either row and between the two vertices in each column. All initial colors are equally weighted among the \(3^{2n}\) possibilities. Temporal updating is synchronous and uses the **CCA successor-contact rule**, not the Greenberg--Hastings refractory rule; their initial discrete 1-forms are different. A fixed state of three-color CCA on a connected graph is spatially constant, so synchronization here is the same as eventual entry into the three monochromatic fixed states.

## Proof

**1. Exact-lift criterion (prior theorem plus elementary graph integration).** For oriented adjacent vertices with colors \(a,b\in\mathbb Z/3\mathbb Z\), define \(\delta(a,b)\) to be the unique integer in \(\{-1,0,1\}\) congruent to \(b-a\pmod3\). Theorem 3 of Gravner--Lyu--Sivakoff (2016) proves, for the three-color CCA on *every* finite connected graph, that synchronization occurs exactly when the integral of this discrete 1-form vanishes on every directed graph cycle. The relevant theorem is explicitly acknowledged as prior work.

Fix an origin vertex \(v_0\). Vanishing of every cycle integral is equivalent to the existence of a well-defined integer height \(h\), with \(h(v_0)=0\), such that \(h(v)-h(u)=\delta(c(u),c(v))\) along every oriented edge. Consequently \(|h(v)-h(u)|\le1\) on edges. Conversely, any such height and any choice of \(c(v_0)\in\{0,1,2\}\) determine a unique irrotational coloring by reducing heights modulo three. Since the permitted height differences are exactly the representatives \(-1,0,1\), this correspondence is bijective and has the factor three claimed above.

**2. Transfer matrix.** Denote the top and bottom integer heights in cyclic column \(i\) by \(p_i,q_i\) and define \(d_i=q_i-p_i\in\{-1,0,1\}\). Put \(a_i=p_{i+1}-p_i\in\{-1,0,1\}\). The bottom horizontal step is \(a_i+d_{i+1}-d_i\), which must also lie in \(\{-1,0,1\}\). Thus the Laurent polynomial weighting transitions \(d_i=d\) to \(d_{i+1}=e\) is
\[
T_{d,e}(z)=\sum_{a\in\{-1,0,1\}}\mathbf1\{|a+e-d|\le1\}z^a,
\qquad d,e\in\{-1,0,1\}.
\]
In order \(-1,0,1\), these entries are exactly the displayed matrix. Periodic column indexing requires \(d_{n+1}=d_1\). It also requires \(p_{n+1}=p_1\), equivalently \(\sum_{i=1}^n a_i=0\); then the bottom row closes automatically. Therefore \([z^0]\operatorname{tr}(T(z)^n)\) counts precisely the normalized integer heights, and the lift criterion proves the exact formula for \(S_n\). For the open ladder there is no horizontal closure: freely summing the initial and final vertical differences gives \(O_n=3\mathbf1^{\mathsf T}T(1)^{n-1}\mathbf1\).

**3. Spectral formula and asymptotics.** Write \(s=z+z^{-1}\). Direct expansion of the determinant gives the polynomial identity
\[
\det(\lambda I-T(z))=(\lambda-s)
\bigl(\lambda^2-(3+2s)\lambda+s^2+s-2\bigr).
\]
Consequently, the three eigenvalues of \(T(z)\) are \(s\) and
\[
\lambda_{\pm}(s)=\frac{3+2s\pm\sqrt{17+8s}}2.
\]
On the Fourier unit circle \(z=e^{i\theta}\), \(s=2\cos\theta\). The principal eigenvalue \(\lambda_+(2\cos\theta)\) has a unique maximum \(\Lambda=(7+\sqrt{33})/2\) in modulus at \(\theta=0\); the other two eigenvalues stay strictly below \(\Lambda\) in modulus. Moreover,
\[
\log\lambda_+(2\cos\theta)=\log\Lambda-\frac{\sigma^2\theta^2}{2}+O(\theta^4),
\quad \sigma^2=\frac{2(1+2/\sqrt{33})}{\Lambda}=\frac54-\frac{19\sqrt{33}}{132}.
\]
The constant-term formula is the Fourier integral \(S_n=(3/2\pi)\int_{-\pi}^{\pi}\operatorname{tr}(T(e^{i\theta})^n)\,d\theta\). The strict unique maximum and analytic even expansion imply the displayed Gaussian Laplace asymptotic with relative error \(O(n^{-1})\). For the open ladder, the Perron eigenvector of \(T(1)\) is \((1,t,1)^{\mathsf T}\); hence \(\mathbf1^{\mathsf T}T(1)^{n-1}\mathbf1\sim B\Lambda^{n-1}\) with \(B=(2+t)^2/(2+t^2)\). Dividing the two asymptotics proves the seam suppression law.

## Verification

The two standalone programs `verify_transfer_dynamics.py` and `verify_cycle_basis.py` both use only the Python standard library. The first independently counts Laurent transfer paths and directly evolves every initial coloring through the graph-diameter cutoff for \(n=3,4,5,6\). The second directly tests the top-ring and all elementary-square integer circulations, which form a cycle basis. Both return \((261,1485,8409,49215)\); direct trajectory enumeration covers exactly \(729+6561+59049+531441=597780\) labelled states. The program `verify_open.py` independently checks the open-ladder formula through \(n=6\). The auxiliary program `verify_spectral.py` checks the determinant identity by exact rational evaluations and the leading asymptotic ratio at larger \(n\) without floating-point enumeration of trajectories. All reported executions appear in `VERIFICATION_OUTPUT.txt`.

## Relationship to prior work

The non-numerical dynamical equivalence between synchronization and irrotationality is Theorem 3 of Gravner, Lyu and Sivakoff (2016), and is not a new claim. Their Theorem 5 supplies a general combinatorial upper bound on synchronization probability but does not give a circular-ladder count or its leading constant. Standard height-function and transfer-matrix techniques explain how to enumerate irrotational colorings once the exact-lift criterion is known. The result here is the exact all-length three-state transfer, its explicit Perron eigenvalue and Gaussian correction, and the quantitative comparison between open and cyclic boundary conditions.

## Limitations

No period census, basin subdivision beyond synchronization versus nonsynchronization, or transient-time distribution is established for the nonsynchronizing configurations. The formulas do not apply to Greenberg--Hastings dynamics, four or more colors, wider cylinders, or other graph products. The originality comparison is based on the identified primary literature, published research records, and targeted searches; unindexed equivalent height-function enumerations remain possible. The verification for small sizes supports but does not replace the all-size transfer and asymptotic proofs.

## References

J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first posted 2016-10-24. See the definitions in Section 2, Theorem 3 (irrotationality characterization), and Theorem 5 (general probability bound). https://arxiv.org/abs/1610.07320
