# Two local feedback defects create a parity reversibility boundary and twin nilpotent clocks

## Finding

Consider the cyclic binary nearest-neighbor dynamics defined below with exactly two sites using self-feedback. The following statements hold for every ring size \(n\ge3\) and every separation \(1\le d\le\lfloor n/2\rfloor\).

1. The map is reversible exactly when \(n\) is even and \(d\) is odd. If it is not reversible, its kernel dimension is one for odd \(n\) and two for even \(n\) with even \(d\).
2. Its characteristic polynomial and two Smith invariant factors are computed from an explicit two-dimensional polynomial transfer matrix. They give an exact formula for the number of initial states having *each* specified first periodic-entry time and eventual least period, without enumerating the exponentially many states.
3. Two distinct infinite resonances produce a single full-size nilpotent Jordan block: for every integer \(r\ge2\), at \((n,d)=(2^r-1,1)\) or \((n,d)=(2^r+1,2)\), the map satisfies \(T^n=0\) but \(T^{n-1}\ne0\). Thus every state extinguishes within \(n\) updates and this global cutoff is sharp.

In particular, moving two feedback sites from odd to even separation on an even-length ring switches the entire configuration space from immediate periodicity to a map with a two-dimensional one-step kernel. The two nilpotent families show that local feedback can also tune the entire finite system to a sharp extinction clock at infinitely many odd lengths.

## Assumptions and scope

Let \(V=\mathbb F_2^n\), with site indices modulo \(n\). For \(n\ge3\) and distinct sites \(0,d\), put
\[
(T_{n,d}x)_j=x_{j-1}+x_{j+1}+\mathbf 1_{\{j\in\{0,d\}\}}x_j\pmod2.
\]
This is the synchronous cyclic Rule 90 network with Rule 150 at sites \(0,d\). The unordered defect placement is determined, up to graph rotation and reflection, by the shorter separation \(1\le d\le\lfloor n/2\rfloor\). For a state \(x\), its first periodic-entry time is the smallest \(k\ge0\) for which \(T^k x\) is periodic; its eventual least period is the least \(m\ge1\) satisfying \(T^{k+m}x=T^kx\).

Let \(s\) be an indeterminate over \(\mathbb F_2\). Define \(f_0(s)=0\), \(f_1(s)=1\), and \(f_{j+1}(s)=s f_j(s)+f_{j-1}(s)\). Define
\[
H_\epsilon(s)=\begin{pmatrix}s+\epsilon&1\\1&0\end{pmatrix},\qquad
M_{n,d}(s)=H_{\delta_{n-1}}(s)\cdots H_{\delta_0}(s),
\]
where \(\delta_j=1\) exactly for \(j=0,d\), and otherwise \(\delta_j=0\). Set \(K=M_{n,d}-I_2\) (the same as addition in characteristic two). The monic Smith invariants are
\[
q_1(s)=\gcd(K_{11},K_{12},K_{21},K_{22}),\qquad q_2(s)=\det K/q_1(s).
\]
All gcds are monic; the matrices have determinant one, and \(q_1q_2\) has degree \(n\). Write \(q_i=s^{e_i}h_i\) with \(h_i(0)=1\), including \(h_i=1\) when necessary.

## Proof

**Two-generator presentation.** The eigenvalue relations for the \(\mathbb F_2[s]\)-module \(V\), where multiplication by \(s\) is the operator \(T\), are
\[
x_{j+1}=(s+\delta_j)x_j+x_{j-1}.
\]
Each relation eliminates the next site with unit coefficient; carrying the pair of consecutive generators around the ring leaves the two relations \((M_{n,d}-I_2)(x_0,x_{n-1})^\mathsf T=0\), up to cyclic reordering. Elementary row/column operations over \(\mathbb F_2[s]\) therefore give the module isomorphism
\[
V\cong \mathbb F_2[s]/(q_1)\oplus\mathbb F_2[s]/(q_2).
\]
The cyclic determinant–monodromy identity gives \(\det(sI-T)=\det(M-I_2)\), and expanding the two marked diagonal perturbations against the uniform cyclic nearest-neighbor operator yields the exact identity
\[
\boxed{\det(sI-T_{n,d})=s f_n(s)+f_d(s)f_{n-d}(s).}
\]
One may equivalently verify the identity by multiplying the \(n\) two-by-two matrices: both expressions obey the same recurrence on the unmarked arcs and agree at the adjoining-defect boundary. The standalone polynomial checker performs independent exact symbolic calculations for 1,023 placements up to \(n=64\); the all-size statement follows from the preceding determinant expansion, not from this finite check.

**Reversibility.** At \(s=0\), \(f_j(0)\) is one for odd \(j\) and zero for even \(j\). Therefore \(\det T=f_d(0)f_{n-d}(0)\) is one exactly if \(n\) is even and \(d\) is odd. For the precise kernel dimension, at \(s=0\) each unmarked transfer is \(S=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\) and each marked transfer is \(B=\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\). The two unmarked arc lengths are \(d-1\) and \(n-d-1\). Since \(S^2=I\), evaluating the four parity possibilities for their product yields \(\dim\ker(M(0)-I)\) equal to zero for even \(n\), odd \(d\); one for odd \(n\); and two for even \(n\), even \(d\). The two-generator presentation identifies this with \(\dim\ker T\).

**Exact first-entry and period counts.** In a cyclic summand \(\mathbb F_2[s]/(s^e h)\) with \(h(0)=1\), the kernel of \(s^k(s^m-1)\) has dimension \(\min(k,e)+\deg\gcd(h,s^m-1)\). Hence, with \(N_{k,m}=|\{x:T^{k+m}x=T^kx\}|\),
\[
\boxed{N_{k,m}=2^{\sum_{i=1}^2[\min(k,e_i)+\deg\gcd(h_i,s^m-1)]}.}
\]
Define \(N_{-1,m}=0\). Möbius inversion on the divisors of \(m\) and subtraction of nested transient kernels now give the **exact** number with first periodic-entry time exactly \(k\) and eventual least period exactly \(m\):
\[
\boxed{E_{k,m}=\sum_{j\mid m}\mu(m/j)(N_{k,j}-N_{k-1,j}).}
\]
In particular, the number of primitive temporal \(m\)-cycles is \(E_{0,m}/m\). No convergence assumption or finite-length extrapolation is used.

**Two full nilpotent resonances.** The recurrence for \(f_j\) gives \(f_{2a}=s f_a^2\) in characteristic two; inductively \(f_{2^r}=s^{2^r-1}\). At \(d=1\), the characteristic polynomial simplifies to \(f_{n+1}\). At \(d=2\), it simplifies to \(s^2 f_{n-1}\). Consequently it is \(s^n\) at both stated infinite families. Since those lengths are odd, the preceding kernel classification gives \(\dim\ker T=1\), so the nilpotent Jordan form has exactly one block. A block of total size \(n\) proves \(T^n=0\) and \(T^{n-1}\ne0\).

## Verification

Run `python3 verify_transfer.py` and `python3 verify_direct.py` from the directory containing both standalone files, using only Python's standard library. The first checks exact polynomial monodromies, Smith factors, reversibility, and the special nilpotent families for all 1,023 admissible placements with \(3\le n\le64\). The independently constructed binary-matrix checker compares each predicted fixed-iterate population against exact bit-matrix ranks for 80 placements with \(3\le n\le18\), multiple entry times and periods, and exhaustively classifies all binary initial states for \(3\le n\le10\). It additionally tests single-block nilpotence and sharpness at \((7,1),(9,2),(15,1),(17,2)\). These are finite corroborations; the proof of the infinite assertions is the algebra above.

## Relationship to prior work

Tadaki's 1993 analysis studies periodicity and relaxation for uniform Rule 90 and Rule 150 with Dirichlet endpoints, including a dyadic nilpotence pattern for uniform Rule 90; it does not describe the two-site feedback perturbation on a cyclic ring. Cattell's 1995 thesis develops the broader general characteristic-polynomial framework for one-dimensional hybrid linear automata and explicitly studies cyclic boundary conditions (notably section 3.6). The characteristic-polynomial methodology, and the general use of polynomial linear-algebra invariants for finite cellular automata, are established background, not originality claims. The additional content here is the two-defect distance-dependent parity boundary, the two specified sharp nilpotent infinite families, and a complete first-entry/eventual-period census obtained by resolving *both* invariant factors. Martin–Odlyzko–Wolfram (1984) treated additive cellular automata and characteristic-polynomial dynamics in a general setting.

## Limitations

This result concerns synchronous binary nearest-neighbor XOR dynamics with exactly two local self-feedback sites on a simple labelled ring, not arbitrary heterogeneous automata or infinite lattices. The two nilpotent families are proven sufficient, not claimed exhaustive over all separations and lengths. Exact counts are specified algorithmically via monic polynomial gcds, rather than expanded into a uniform list of possible temporal periods. General earlier hybrid-cellular-automaton theory may permit an alternative derivation of some specializations; historical-priority searches do not prove uniqueness. No independent external validation has been conducted.

## References

- Shin-ichi Tadaki, *Orbits in one-dimensional finite linear cellular automata*, preprint first posted 14 May 1993, https://arxiv.org/abs/cond-mat/9305012.
- Kevin Michael Cattell, *Characteristic Polynomials of One-Dimensional Linear Hybrid Cellular Automata*, PhD dissertation, University of Victoria, 1995, section 3.6, https://dspace.library.uvic.ca/bitstream/handle/1828/9439/Cattell_KevinMichael_PhD_1995.pdf.
- O. Martin, A. M. Odlyzko, and S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258, https://content.wolfram.com/sw-publications/2020/07/algebraic-properties-cellular-automata.pdf.
