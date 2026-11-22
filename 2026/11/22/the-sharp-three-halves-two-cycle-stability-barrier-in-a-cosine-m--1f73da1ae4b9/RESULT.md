# The sharp three-halves two-cycle stability barrier in a cosine–memristor map

## Finding

Consider the smooth real-plane discrete dynamical system
\[
F_{\alpha,\beta}(x,y)=\bigl(\alpha\cos x+\beta(y^2-1)x,\ y+x\bigr),
\qquad \alpha>0,\quad 0<\beta\le2.
\]
A *primitive two-cycle* is a pair of distinct states exchanged by the map. It is an *exponentially attracting two-cycle* (or *sink*) if both eigenvalues of the two-step Jacobian have modulus strictly smaller than one.

**Theorem (sharp parameter-only stability threshold).** For every choice of forcing \(\alpha>0\), **every** primitive two-cycle when \(3/2\le\beta\le2\) has a two-step Floquet multiplier of modulus **strictly greater than one**, and therefore none is attracting. For \(0<\beta\le1\), there are no primitive two-cycles at all. Conversely, for every \(1<\beta<3/2\), there exists \(\alpha_0(\beta)>0\) such that **every** \(0<\alpha<\alpha_0(\beta)\) produces an exponentially attracting primitive two-cycle. Therefore, within \(0<\beta\le2\), the existence of an attracting primitive two-cycle for *some* positive forcing is **equivalent** to
\[
\boxed{1<\beta<\frac32.}
\]
In particular, the source's illustrated choice \(\beta=17/10\), \(\alpha=1/10\), although it admits two real primitive two-cycles, admits **no attracting primitive two-cycle**. The existence and number of the two-cycles are known from an earlier exact census; the new assertion here is the sharp stability barrier, including the global exclusion for arbitrary positive forcing.

## Assumptions and scope

The state space is all of \(\mathbb R^2\), without a compact trapping region. Parameters are real with \(\alpha>0\) and \(0<\beta\le2\). Attraction is local exponential stability of the two-step map in both planar directions; it is not global basin attraction. No claim is made for \(\beta>2\), \(\alpha=0\), higher periods, or invariant probability measures. The forcing is not assumed to be small on the non-attracting side.

## Proof

**1. Exact parameterization of every two-cycle.** If \((x_0,y_0)\) and \((x_1,y_1)\) constitute a two-cycle, summing the two updates \(y_{i+1}-y_i=x_i\) gives \(x_1=-x_0\). A primitive two-cycle cannot have \(x_0=0\), because \(F_{\alpha,\beta}(0,y)=(\alpha,y)\). Swap the two phases if necessary and write the two points as
\[
(p,q-p/2)\quad\longleftrightarrow\quad(-p,q+p/2),\qquad p>0.
\]
Substitution into the two first-coordinate updates, then adding and subtracting those equations, gives exactly
\[
q^2+\frac{p^2}{4}=s:=1-\frac1\beta,
\qquad \alpha\cos p=\beta q p^2.
\tag{1}
\]
Reversing the calculation proves sufficiency as well. For \(0<\beta\le1\), the first equality is impossible. For \(1<\beta\le2\), put \(P=2\sqrt{s}\). Then \(0<p<P\le\sqrt2<\pi/2\), so \(\cos p>0\) and the second equality forces \(q>0\). Every primitive two-cycle is consequently represented by a solution of
\[
q=\sqrt{s-p^2/4},\qquad
\alpha=\frac{\beta p^2\sqrt{s-p^2/4}}{\cos p},\qquad 0<p<P.
\tag{2}
\]

**2. The exact Floquet formulas.** Write
\[
B=\beta p^2,\qquad t=\beta pq=\frac{\alpha\cos p}{p},
\qquad k=\alpha\sin p=t p\tan p.
\]
The ordinary Jacobians at the two phases, with the first phase listed in (1), reduce to
\[
J_0=\begin{pmatrix}-1-t-k&2t-B\\1&1\end{pmatrix},
\qquad
J_1=\begin{pmatrix}-1+t+k&-2t-B\\1&1\end{pmatrix}.
\]
For the return matrix \(M=J_1J_0\), direct multiplication gives
\[
\operatorname{tr}M=2-2B-(k+t)^2,
\qquad \det(I-M)=B^2-4kt-8t^2.
\tag{3}
\]
Using \(q^2=(P^2-p^2)/4\) and \(z=p^2\), the second identity is exactly
\[
\frac{\det(I-M)}{\beta^2p^2}
=3z-8s-p(P^2-z)\tan p.
\tag{4}
\]

**3. Exclusion when \(3/2\le\beta\le2\), small-amplitude case.** Here \(s\ge1/3\). If \(0<p\le1\), then \(\tan p>p\), \(P^2=4s\), and \(0<z\le1\), so (4) yields the *strict* bound
\[
\begin{aligned}
\frac{\det(I-M)}{\beta^2p^2}
&<z^2+(3-4s)z-8s\\
&\le z^2+\frac53 z-\frac83
=(z-1)\left(z+\frac83\right)\le0.
\end{aligned}
\]
Hence \(\det(I-M)<0\). The real characteristic polynomial \(\det(\lambda I-M)\) is negative at \(\lambda=1\) and tends to positive infinity as \(\lambda\to+\infty\), so it has a real multiplier \(\lambda>1\). This two-cycle is not attracting.

**4. Exclusion when \(3/2\le\beta\le2\), large-amplitude case.** Suppose \(p>1\), so \(z>1\) and \(P^2-z>0\). On \(0<p<\pi/2\), \(\tan p\ge p+p^3/3\) (for instance, differentiate \(\tan p-p-p^3/3\) and use \(\tan p\ge p\)). Thus with \(Q(z)=1+z+z^2/3\),
\[
(k+t)^2=\beta^2p^2q^2(1+p\tan p)^2
\ge\frac{\beta^2 z(P^2-z)}4Q(z)^2.
\]
Since \(\beta P^2=4(\beta-1)\), we obtain
\[
\begin{aligned}
2B+(k+t)^2-4
&\ge4(2\beta-3)+\beta(P^2-z)
\left[\frac{\beta z}{4}Q(z)^2-2\right]>0.
\end{aligned}
\tag{5}
\]
Indeed \(\beta\ge3/2\), \(z>1\), and \(Q(z)>7/3\), so the square bracket exceeds \(49/24-2=1/24>0\). Therefore \(\operatorname{tr}M< -2\) by (3). Were both Floquet multipliers in the closed unit disk, their sum would have absolute value at most two, a contradiction. This two-cycle also cannot attract. The cases \(p\le1\) and \(p>1\) exhaust all two-cycles, proving the forcing-uniform exclusion, including the endpoint \(\beta=3/2\).

**5. Sharpness: sinks for every \(1<\beta<3/2\) at small forcing.** Fix such a \(\beta\), set \(P=2\sqrt{1-1/\beta}\), and let \(p\uparrow P\) through values below \(P\). Define \(q\) and \(\alpha=\alpha(p)>0\) by (2). Since \(P<\sqrt2<\pi/2\), one has \(q\downarrow0\) and \(\alpha(p)\downarrow0\) in the sense of convergence (monotonicity is not needed). Each pair constructed from (1) is an exact primitive two-cycle. In (3), \(t,k\to0\) and \(B\to\beta P^2=4(\beta-1)\); moreover both phase Jacobians approach
\[
J_*=\begin{pmatrix}-1&-4(\beta-1)\\1&1\end{pmatrix},
\qquad J_*^2=(5-4\beta)I.
\]
Because \(-1<5-4\beta<1\), continuity of matrix eigenvalues implies that every cycle obtained with \(p\) sufficiently close to \(P\) is a strict exponential sink. The function \(p\mapsto\alpha(p)\) is positive and continuous on a terminal interval and tends to zero at its endpoint; by the intermediate value theorem its image contains an interval \((0,\alpha_0(\beta))\). Thus *every* forcing in that interval has an attracting two-cycle. This proves sharpness and the theorem.

## Verification

The standalone Python 3/SymPy/mpmath program `verify_cycle.py` reconstructs the two Jacobians, verifies (3) and the exact algebraic reduction (4), checks the factorization underlying the small-amplitude sign and the exact decomposition (5), and reproduces exact two-cycle returns to 70-digit precision. Six diagnostics at \(\beta=1.05,1.2,1.4,1.5,1.7,2\) check stable and unstable cases. Execute `python verify_cycle.py` from the extracted package. The infinite-parameter conclusions follow from the inequalities in the proof, not from these finite numerical checks.

## Relationship to prior work

Almatroud and Pham, *Building Fixed Point-Free Maps with Memristor*, *Mathematics* **11** (2023), article 1319, introduce the cosine–quadratic-memristance map as FPFM1, prove the absence of fixed points, and present numerical bifurcation and Lyapunov plots over parameter ranges straddling \(\beta=3/2\). They do not derive the all-forcing two-cycle sink obstruction or this sharp existence boundary. The publicly available exact census *A sharp two-cycle fold and a three-halves onset law for a fixed-point-free memristor map* already proves that the same family has two, one, or no primitive two-cycles on the stated parameter rectangle, but **explicitly leaves their stability undetermined**. The present theorem adds the parameter-only stability obstruction and proves its sharpness; it makes no novelty claim about the census, orbit parameterization, absence of fixed points, or existing numerical pictures. A published analysis of the distinct FPFM2 map with \(\beta(|y|-1)x\) has a different exact short-cycle stability criterion and does not imply this FPFM1 result.

## Limitations

No complete stability diagram as a function of both \(\alpha\) and \(\beta\) is claimed inside \(1<\beta<3/2\); only a nonempty interval of small positive forcing is proved to admit a sink. The classification does not address \(\beta>2\), where the cosine phase may change sign on the solution ellipse, nor any higher-period or chaotic invariant set. It asserts local hyperbolic attraction, not global convergence or safety for cryptographic applications. Unindexed equivalent stability studies remain a possible priority risk. Independent mathematical validation has not been performed.

## References

1. O. A. Almatroud and V.-T. Pham, *Building Fixed Point-Free Maps with Memristor*, *Mathematics* **11** (2023), 1319, doi:10.3390/math11061319, first publicly dated 2023-03-09; FPFM1 equation (5) and Sections 2–3.
2. *A sharp two-cycle fold and a three-halves onset law for a fixed-point-free memristor map*, published research record, 2026-11-01, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-a-sharp-two-cycle-fold-and-a-three-halves-onset-law-for-a-fixed--3b64e28eaf02/RESULT.md (same map; exact two-cycle census, no stability theorem).
3. *A locked two-cycle and a sharp persistence transition in an absolute-value memristor map*, published research record, 2026-11-02, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-locked-two-cycle-and-a-sharp-persistence-transition-in-an-abso--ab503072ca36/RESULT.md (distinct \(|y|-1\) memory law).
